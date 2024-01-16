# OpenAI

Qdrant can also easily work with[ OpenAI embeddings ](https://platform.openai.com/docs/guides/embeddings/embeddings).

There is an official OpenAI Python package that simplifies obtaining them, and it might be installed with pip:

`pip install openai
`

Once installed, the package exposes the method allowing to retrieve the embedding for given text. OpenAI requires an API key that has to be provided either as an environmental variable `OPENAI_API_KEY` or set in the source code directly, as presented below:

```
import   openai 

import   qdrant_client 



from   qdrant_client.http.models   import  Batch



# Provide OpenAI API key and choose one of the available models: 

# https://beta.openai.com/docs/models/overview 

openai . api_key  =   "<< your_api_key >>" 

embedding_model  =   "text-embedding-ada-002" 



response  =  openai . Embedding . create(

     input = "The best vector database" ,

    model = embedding_model,

)



qdrant_client  =  qdrant_client . QdrantClient()

qdrant_client . upsert(

    collection_name = "MyCollection" ,

    points = Batch(

        ids = [ 1 ],

        vectors = [response[ "data" ][ 0 ][ "embedding" ]],

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