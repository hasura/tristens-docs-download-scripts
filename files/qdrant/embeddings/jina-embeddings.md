# Jina Embeddings

Qdrant can also easily work with[ Jina embeddings ](https://jina.ai/embeddings/)which allow for model input lengths of up to 8192 tokens.

To call their endpoint, all you need is an API key obtainable[ here ](https://jina.ai/embeddings/).

```
import   qdrant_client 

import   requests 



from   qdrant_client.http.models   import  Distance, VectorParams

from   qdrant_client.http.models   import  Batch



# Provide Jina API key and choose one of the available models. 

# You can get a free trial key here: https://jina.ai/embeddings/ 

JINA_API_KEY  =   "jina_xxxxxxxxxxx" 

MODEL  =   "jina-embeddings-v2-base-en"    # or "jina-embeddings-v2-base-en" 

EMBEDDING_SIZE  =   768    # 512 for small variant 



# Get embeddings from the API 

url  =   "https://api.jina.ai/v1/embeddings" 



headers  =  {

     "Content-Type" :  "application/json" ,

     "Authorization" :  f "Bearer  { JINA_API_KEY } " ,

}



data  =  {

     "input" : [ "Your text string goes here" ,  "You can send multiple texts" ],

     "model" : MODEL,

}



response  =  requests . post(url, headers = headers, json = data)

embeddings  =  [d[ "embedding" ]  for  d  in  response . json()[ "data" ]]





# Index the embeddings into Qdrant 

qdrant_client  =  qdrant_client . QdrantClient( ":memory:" )

qdrant_client . create_collection(

    collection_name = "MyCollection" ,

    vectors_config = VectorParams(size = EMBEDDING_SIZE, distance = Distance . DOT),

)





qdrant_client . upsert(

    collection_name = "MyCollection" ,

    points = Batch(

        ids = list ( range ( len (embeddings))),

        vectors = embeddings,

    ),

)

```

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