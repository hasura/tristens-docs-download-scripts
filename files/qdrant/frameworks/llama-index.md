# LlamaIndex (GPT Index)

LlamaIndex (formerly GPT Index) acts as an interface between your external data and Large Language Models. So you can bring your
private data and augment LLMs with it. LlamaIndex simplifies data ingestion and indexing, integrating Qdrant as a vector index.

Installing LlamaIndex is straightforward if we use pip as a package manager. Qdrant is not installed by default, so we need to
install it separately:

`pip install llama-index qdrant-client
`

LlamaIndex requires providing an instance of `QdrantClient` , so it can interact with Qdrant server.

```
from   llama_index.vector_stores.qdrant   import  QdrantVectorStore



import   qdrant_client 



client  =  qdrant_client . QdrantClient(

     "<qdrant-url>" ,

    api_key = "<qdrant-api-key>" ,  # For Qdrant Cloud, None for local instance 

)



index  =  QdrantVectorStore(client = client, collection_name = "documents" )

```

The library[ comes with a notebook ](https://github.com/jerryjliu/llama_index/blob/main/docs/examples/vector_stores/QdrantIndexDemo.ipynb)that shows an end-to-end example of how to use Qdrant within LlamaIndex.

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