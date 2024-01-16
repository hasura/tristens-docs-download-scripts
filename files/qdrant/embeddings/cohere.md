# Cohere

Qdrant is compatible with Cohere[ co.embed API ](https://docs.cohere.ai/reference/embed)and its official Python SDK that
might be installed as any other package:

`pip install cohere
`

The embeddings returned by co.embed API might be used directly in the Qdrant client’s calls:

```
import   cohere 

import   qdrant_client 



from   qdrant_client.http.models   import  Batch



cohere_client  =  cohere . Client( "<< your_api_key >>" )

qdrant_client  =  qdrant_client . QdrantClient()

qdrant_client . upsert(

    collection_name = "MyCollection" ,

    points = Batch(

        ids = [ 1 ],

        vectors = cohere_client . embed(

            model = "large" ,

            texts = [ "The best vector database" ],

        ) . embeddings,

    ),

)

```

If you are interested in seeing an end-to-end project created with co.embed API and Qdrant, please check out the
“[ Question Answering as a Service with Cohere and Qdrant ](https://qdrant.tech/articles/qa-with-cohere-and-qdrant/)” article.

## Embed v3

Embed v3 is a new family of Cohere models, released in November 2023. The new models require passing an additional
parameter to the API call: `input_type` . It determines the type of task you want to use the embeddings for.

- `input_type="search_document"` - for documents to store in Qdrant
- `input_type="search_query"` - for search queries to find the most relevant documents
- `input_type="classification"` - for classification tasks
- `input_type="clustering"` - for text clustering


While implementing semantic search applications, such as RAG, you should use `input_type="search_document"` for the
indexed documents and `input_type="search_query"` for the search queries. The following example shows how to index
documents with the Embed v3 model:

```
import   cohere 

import   qdrant_client 



from   qdrant_client.http.models   import  Batch



cohere_client  =  cohere . Client( "<< your_api_key >>" )

qdrant_client  =  qdrant_client . QdrantClient()

qdrant_client . upsert(

    collection_name = "MyCollection" ,

    points = Batch(

        ids = [ 1 ],

        vectors = cohere_client . embed(

            model = "embed-english-v3.0" ,   # New Embed v3 model 

            input_type = "search_document" ,   # Input type for documents 

            texts = [ "Qdrant is the a vector database written in Rust" ],

        ) . embeddings,

    ),

)

```

Once the documents are indexed, you can search for the most relevant documents using the Embed v3 model:

```
qdrant_client . search(

    collection_name = "MyCollection" ,

    query = cohere_client . embed(

        model = "embed-english-v3.0" ,   # New Embed v3 model 

        input_type = "search_query" ,   # Input type for search queries 

        texts = [ "The best vector database" ],

    ) . embeddings[ 0 ],

)

```

##### Table of contents

- [ Embed v3 ](https://qdrant.tech/documentation/embeddings/cohere/#embed-v3)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/cohere.md)
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