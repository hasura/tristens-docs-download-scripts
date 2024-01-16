# LangChain

LangChain is a library that makes developing Large Language Models based applications much easier. It unifies the interfaces
to different libraries, including major embedding providers and Qdrant. Using LangChain, you can focus on the business value
instead of writing the boilerplate.

Langchain comes with the Qdrant integration by default. It might be installed with pip:

`pip install langchain
`

Qdrant acts as a vector index that may store the embeddings with the documents used to generate them. There are various ways
how to use it, but calling `Qdrant.from_texts` is probably the most straightforward way how to get started:

```
from   langchain.vectorstores   import  Qdrant

from   langchain.embeddings   import  HuggingFaceEmbeddings



embeddings  =  HuggingFaceEmbeddings(

    model_name = "sentence-transformers/all-mpnet-base-v2" 

)

doc_store  =  Qdrant . from_texts(

    texts, embeddings, url = "<qdrant-url>" , api_key = "<qdrant-api-key>" , collection_name = "texts" 

)

```

Calling `Qdrant.from_documents` or `Qdrant.from_texts` will always recreate the collection and remove all the existing points.
That’s fine for some experiments, but you’ll prefer not to start from scratch every single time in a real-world scenario.
If you prefer reusing an existing collection, you can create an instance of Qdrant on your own:

```
import   qdrant_client 



embeddings  =  HuggingFaceEmbeddings(

    model_name = "sentence-transformers/all-mpnet-base-v2" 

)



client  =  qdrant_client . QdrantClient(

     "<qdrant-url>" ,

    api_key = "<qdrant-api-key>" ,  # For Qdrant Cloud, None for local instance 

)



doc_store  =  Qdrant(

    client = client, collection_name = "texts" , 

    embeddings = embeddings,

)

```

## Local mode

Python client allows you to run the same code in local mode without running the Qdrant server. That’s great for testing things
out and debugging or if you plan to store just a small amount of vectors. The embeddings might be fully kepy in memory or
persisted on disk.

### In-memory

For some testing scenarios and quick experiments, you may prefer to keep all the data in memory only, so it gets lost when the
client is destroyed - usually at the end of your script/notebook.

```
qdrant  =  Qdrant . from_documents(

    docs, embeddings, 

    location = ":memory:" ,   # Local mode with in-memory storage only 

    collection_name = "my_documents" ,

)

```

### On-disk storage

Local mode, without using the Qdrant server, may also store your vectors on disk so they’re persisted between runs.

```
qdrant  =  Qdrant . from_documents(

    docs, embeddings, 

    path = "/tmp/local_qdrant" ,

    collection_name = "my_documents" ,

)

```

### On-premise server deployment

No matter if you choose to launch Qdrant locally with[ a Docker container ](https://qdrant.tech/documentation/guides/installation/), or
select a Kubernetes deployment with[ the official Helm chart ](https://github.com/qdrant/qdrant-helm), the way you’re
going to connect to such an instance will be identical. You’ll need to provide a URL pointing to the service.

```
url  =   "<---qdrant url here --->" 

qdrant  =  Qdrant . from_documents(

    docs, 

    embeddings, 

    url, 

    prefer_grpc = True , 

    collection_name = "my_documents" ,

)

```

## Next steps

If you’d like to know more about running Qdrant in a LangChain-based application, please read our article[ Question Answering with LangChain and Qdrant without boilerplate ](https://qdrant.tech/articles/langchain-integration/). Some more information
might also be found in the[ LangChain documentation ](https://python.langchain.com/docs/integrations/vectorstores/qdrant).

##### Table of contents

- [ Local mode ](https://qdrant.tech/documentation/frameworks/langchain/#local-mode)
    - [ In-memory ](https://qdrant.tech/documentation/frameworks/langchain/#in-memory)

- [ On-disk storage ](https://qdrant.tech/documentation/frameworks/langchain/#on-disk-storage)

- [ On-premise server deployment ](https://qdrant.tech/documentation/frameworks/langchain/#on-premise-server-deployment)
- [ Next steps ](https://qdrant.tech/documentation/frameworks/langchain/#next-steps)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/langchain.md)
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