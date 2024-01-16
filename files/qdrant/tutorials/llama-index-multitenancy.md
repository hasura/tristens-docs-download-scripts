# Multitenancy with LlamaIndex

If you are building a service that serves vectors for many independent users, and you want to isolate their
data, the best practice is to use a single collection with payload-based partitioning. This approach is
called **multitenancy** . Our guide on the[ Separate Partitions ](https://qdrant.tech/documentation/guides/multiple-partitions/)describes
how to set it up in general, but if you use[ LlamaIndex ](https://qdrant.tech/documentation/integrations/llama-index/)as a
backend, you may prefer reading a more specific instruction. So here it is!

## Prerequisites

This tutorial assumes that you have already installed Qdrant and LlamaIndex. If you haven’t, please run the
following commands:

`pip install qdrant-client llama-index
`

We are going to use a local Docker-based instance of Qdrant. If you want to use a remote instance, please
adjust the code accordingly. Here is how we can start a local instance:

`docker run -d --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant:latest
`

## Setting up LlamaIndex pipeline

We are going to implement an end-to-end example of multitenant application using LlamaIndex. We’ll be
indexing the documentation of different Python libraries, and we definitely don’t want any users to see the
results coming from a library they are not interested in. In real case scenarios, this is even more dangerous,
as the documents may contain sensitive information.

### Creating vector store

[ QdrantVectorStore ](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo.html)is a
wrapper around Qdrant that provides all the necessary methods to work with your vector database in LlamaIndex.
Let’s create a vector store for our collection. It requires setting a collection name and passing an instance
of `QdrantClient` .

```
from   qdrant_client   import  QdrantClient

from   llama_index.vector_stores   import  QdrantVectorStore



client  =  QdrantClient( "http://localhost:6333" )



vector_store  =  QdrantVectorStore(

    collection_name = "my_collection" ,

    client = client,

)

```

### Defining chunking strategy and embedding model

Any semantic search application requires a way to convert text queries into vectors - an embedding model. `ServiceContext` is a bundle of commonly used resources used during the indexing and querying stage in any
LlamaIndex application. We can also use it to set up an embedding model - in our case, a local[ BAAI/bge-small-en-v1.5 ](https://huggingface.co/BAAI/bge-small-en-v1.5).
set up

```
from   llama_index   import  ServiceContext



service_context  =  ServiceContext . from_defaults(

    embed_model = "local:BAAI/bge-small-en-v1.5" ,

)

```

We can also control how our documents are split into chunks, or nodes using LLamaIndex’s terminology.
The `SimpleNodeParser` splits documents into fixed length chunks with an overlap. The defaults are
reasonable, but we can also adjust them if we want to. Both values are defined in tokens.

```
from   llama_index.node_parser   import  SimpleNodeParser



node_parser  =  SimpleNodeParser . from_defaults(chunk_size = 512 , chunk_overlap = 32 )

```

Now we also need to inform the `ServiceContext` about our choices:

```
service_context  =  ServiceContext . from_defaults(

    embed_model = "local:BAAI/bge-large-en-v1.5" ,

    node_parser = node_parser,

)

```

Both embedding model and selected node parser will be implicitly used during the indexing and querying.

### Combining everything together

The last missing piece, before we can start indexing, is the `VectorStoreIndex` . It is a wrapper around `VectorStore` that provides a convenient interface for indexing and querying. It also requires a `ServiceContext` to be initialized.

```
from   llama_index   import  VectorStoreIndex



index  =  VectorStoreIndex . from_vector_store(

    vector_store = vector_store, service_context = service_context

)

```

## Indexing documents

No matter how our documents are generated, LlamaIndex will automatically split them into nodes, if
required, encode using selected embedding model, and then store in the vector store. Let’s define
some documents manually and insert them into Qdrant collection. Our documents are going to have
a single metadata attribute - a library name they belong to.

```
from   llama_index.schema   import  Document



documents  =  [

    Document(

        text = "LlamaIndex is a simple, flexible data framework for connecting custom data sources to large language models." ,

        metadata = {

             "library" :  "llama-index" ,

        },

    ),

    Document(

        text = "Qdrant is a vector database & vector similarity search engine." ,

        metadata = {

             "library" :  "qdrant" ,

        },

    ),

]

```

Now we can index them using our `VectorStoreIndex` :

```
for  document  in  documents:

    index . insert(document)

```

### Performance considerations

Our documents have been split into nodes, encoded using the embedding model, and stored in the vector
store. However, we don’t want to allow our users to search for all the documents in the collection,
but only for the documents that belong to a library they are interested in. For that reason, we need
to set up the Qdrant[ payload index ](https://qdrant.tech/documentation/concepts/indexing/#payload-index), so the search
is more efficient.

```
from   qdrant_client   import  models



client . create_payload_index(

    collection_name = "my_collection" ,

    field_name = "metadata.library" ,

    field_type = models . PayloadSchemaType . KEYWORD,

)

```

The payload index is not the only thing we want to change. Since none of the search
queries will be executed on the whole collection, we can also change its configuration, so the HNSW
graph is not built globally. This is also done due to[ performance reasons ](https://qdrant.tech/documentation/guides/multiple-partitions/#calibrate-performance). **You should not be changing these parameters, if you know there will be some global search operations
done on the collection.** 

```
client . update_collection(

    collection_name = "my_collection" ,

    hnsw_config = models . HnswConfigDiff(payload_m = 16 , m = 0 ),

)

```

Once both operations are completed, we can start searching for our documents.

## Querying documents with constraints

Let’s assume we are searching for some information about large language models, but are only allowed to
use Qdrant documentation. LlamaIndex has a concept of retrievers, responsible for finding the most
relevant nodes for a given query. Our `VectorStoreIndex` can be used as a retriever, with some additional
constraints - in our case value of the `library` metadata attribute.

```
from   llama_index.vector_stores.types   import  MetadataFilters, ExactMatchFilter



qdrant_retriever  =  index . as_retriever(

    filters = MetadataFilters(

        filters = [

            ExactMatchFilter(

                key = "library" ,

                value = "qdrant" ,

            )

        ]

    )

)



nodes_with_scores  =  qdrant_retriever . retrieve( "large language models" )

for  node  in  nodes_with_scores:

     print (node . text, node . score)

# Output: Qdrant is a vector database & vector similarity search engine. 0.60551536 

```

The description of Qdrant was the best match, even though it didn’t mention large language models
at all. However, it was the only document that belonged to the `qdrant` library, so there was no
other choice. Let’s try to search for something that is not present in the collection.

Let’s define another retrieve, this time for the `llama-index` library:

```
llama_index_retriever  =  index . as_retriever(

    filters = MetadataFilters(

        filters = [

            ExactMatchFilter(

                key = "library" ,

                value = "llama-index" ,

            )

        ]

    )

)



nodes_with_scores  =  llama_index_retriever . retrieve( "large language models" )

for  node  in  nodes_with_scores:

     print (node . text, node . score)

# Output: LlamaIndex is a simple, flexible data framework for connecting custom data sources to large language models. 0.63576734 

```

The results returned by both retrievers are different, due to the different constraints, so we implemented
a real multitenant search application!

##### Table of contents

- [ Prerequisites ](https://qdrant.tech/documentation/tutorials/llama-index-multitenancy/#prerequisites)
- [ Setting up LlamaIndex pipeline ](https://qdrant.tech/documentation/tutorials/llama-index-multitenancy/#setting-up-llamaindex-pipeline)
    - [ Creating vector store ](https://qdrant.tech/documentation/tutorials/llama-index-multitenancy/#creating-vector-store)

- [ Defining chunking strategy and embedding model ](https://qdrant.tech/documentation/tutorials/llama-index-multitenancy/#defining-chunking-strategy-and-embedding-model)

- [ Combining everything together ](https://qdrant.tech/documentation/tutorials/llama-index-multitenancy/#combining-everything-together)
- [ Indexing documents ](https://qdrant.tech/documentation/tutorials/llama-index-multitenancy/#indexing-documents)
    - [ Performance considerations ](https://qdrant.tech/documentation/tutorials/llama-index-multitenancy/#performance-considerations)
- [ Querying documents with constraints ](https://qdrant.tech/documentation/tutorials/llama-index-multitenancy/#querying-documents-with-constraints)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/tutorials/llama-index-multitenancy.md)
- [ 
 Create an Issue
 ](https://github.com/qdrant/landing_page/issues/new/choose)


#### Product

- [ 
Use cases
 ](https://qdrant.tech/use-cases/)
- [ 
Solutions
 ](https://qdrant.tech/solutions/)
- [ 
Benchmarks
 ](https://qdrant.tech/benchmarks/)
- [ 
Demos
 ](https://qdrant.tech/demo/)
- [ 
Pricing
 ](https://qdrant.tech/pricing/)


#### Community

- [ 
 
Github
 ](https://github.com/qdrant/qdrant)
- [ 
 
Discord
 ](https://qdrant.to/discord)
- [ 
 
Twitter
 ](https://qdrant.to/twitter)
- [ 
 
Newsletter
 ](https://qdrant.tech/subscribe/)
- [ 
 
Contact us
 ](https://qdrant.to/contact-us)


#### Company

- [ 
Jobs
 ](https://qdrant.join.com)
- [ 
Privacy Policy
 ](https://qdrant.tech/legal/privacy-policy/)
- [ 
Terms
 ](https://qdrant.tech/legal/terms_and_conditions/)
- [ 
Impressum
 ](https://qdrant.tech/legal/impressum/)
- [ 
Credits
 ](https://qdrant.tech/legal/credits/)


#### Latest Publications

#### Combining the precision of exact keyword search with NN-based ranking

#### Qdrant 1.7.0 brought a bunch of new features. Let's take a closer look at them!

#### Qdrant 1.6 brings recommendations strategies and more flexibility to the Recommendation API.

- [  ](https://github.com/qdrant/qdrant)
- [  ](https://qdrant.to/linkedin)
- [  ](https://qdrant.to/twitter)
- [  ](https://qdrant.to/discord)
- [  ](https://www.youtube.com/channel/UC6ftm8PwH1RU_LM1jwG0LQA)


##### Thanks for using Qdrant!

Subscribe to our e-mail newsletter if you want to be updated on new features and news regarding
Qdrant.

Like what we are doing? Consider giving us a ⭐[ on Github ](https://github.com/qdrant/qdrant).

We use cookies to learn more about you. At any time you can delete or block cookies through your browser settings.