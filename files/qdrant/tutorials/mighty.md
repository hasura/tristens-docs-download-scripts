# Semantic Search with Mighty and Qdrant

Much like Qdrant, the[ Mighty ](https://max.io/)inference server is written in Rust and promises to offer low latency and high scalability. This brief demo combines Mighty and Qdrant into a simple semantic search service that is efficient, affordable and easy to setup. We will use[ Rust ](https://rust-lang.org)and our[ qdrant_client crate ](https://docs.rs/qdrant_client)for this integration.

## Initial setup

For Mighty, start up a[ docker container ](https://hub.docker.com/layers/maxdotio/mighty-sentence-transformers/0.9.9/images/sha256-0d92a89fbdc2c211d927f193c2d0d34470ecd963e8179798d8d391a4053f6caf?context=explore)with an open port 5050. Just loading the port in a window shows the following:

```
{

   "name" :  "sentence-transformers/all-MiniLM-L6-v2" ,

   "architectures" : [

     "BertModel" 

  ],

   "model_type" :  "bert" ,

   "max_position_embeddings" :  512 ,

   "labels" :  null ,

   "named_entities" :  null ,

   "image_size" :  null ,

   "source" :  "https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2" 

}

```

Note that this uses the `MiniLM-L6-v2` model from Hugging Face. As per their website, the model “maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search”. The distance measure to use is cosine similarity.

Verify that mighty works by calling `curl https://<address>:5050/sentence-transformer?q=hello+mighty` . This will give you a result like (formatted via `jq` ):

```
{

     "outputs" : [

        [

             -0.05019686743617058 ,

             0.051746174693107605 ,

             0.048117730766534805 ,

             ...   ( 381   values   skipped) 

        ]

    ],

     "shape" : [

         1 ,

         384 

    ],

     "texts" : [

         "Hello mighty" 

    ],

     "took" :  77 

}

```

For Qdrant, follow our[ cloud documentation ](../../cloud/cloud-quick-start/)to spin up a[ free tier ](https://cloud.qdrant.io/). Make sure to retrieve an API key.

## Implement model API

For mighty, you will need a way to emit HTTP(S) requests. This version uses the[ reqwest ](https://docs.rs/reqwest)crate, so add the following to your `Cargo.toml` ’s dependencies section:

```
[dependencies]

reqwest =  { version =  "0.11.18" , default-features =  false , features = [ "json" ,  "rustls-tls" ] }

```

Mighty offers a variety of model APIs which will download and cache the model on first use. For semantic search, use the `sentence-transformer` API (as in the above `curl` command). The Rust code to make the call is:

```
use   anyhow::anyhow; 

use   reqwest::Client; 

use   serde::Deserialize; 

use   serde_json::Value   as   JsonValue; 



#[derive(Deserialize)] 

struct   EmbeddingsResponse   { 

     pub   outputs:  Vec < Vec < f32 >> , 

} 



pub   async   fn   get_mighty_embedding ( 

     client:  & Client , 

     url:  & str , 

     text:  & str 

)   ->  anyhow :: Result < Vec < f32 >>   { 

     let   response   =   client.get(url).query( & [( "text" ,   text)]).send(). await ? ; 



     if   ! response.status().is_success()   { 

         return   Err (anyhow ! ( 

             "Mighty API returned status code {}" , 

             response.status() 

         )); 

     } 



     let   embeddings:  EmbeddingsResponse   =   response.json(). await ? ; 

     // ignore multiple embeddings at the moment

     embeddings.get( 0 ).ok_or_else( ||   anyhow ! ( "mighty returned empty embedding" )) 

} 

```

Note that mighty can return multiple embeddings (if the input is too long to fit the model, it is automatically split).

## Create embeddings and run a query

Use this code to create embeddings both for insertion and search. On the Qdrant side, take the embedding and run a query:

```
use   anyhow::anyhow; 

use   qdrant_client::prelude:: * ; 



pub   const   SEARCH_LIMIT:  u64   =   5 ; 

const   COLLECTION_NAME:  & str   =   "mighty" ; 



pub   async   fn   qdrant_search_embeddings ( 

     qdrant_client:  & QdrantClient , 

     vector:  Vec < f32 > , 

)   ->  anyhow :: Result < Vec < ScoredPoint >>   { 

     qdrant_client 

         .search_points( & SearchPoints   { 

             collection_name:  COLLECTION_NAME .to_string(), 

             vector, 

             limit:  SEARCH_LIMIT , 

             with_payload:  Some ( true .into()), 

             .. Default ::default() 

         }) 

         . await 

         .map_err( | err |   anyhow ! ( "Failed to search Qdrant: {}" ,   err)) 

} 

```

You can convert the[ ScoredPoint ](https://docs.rs/qdrant-client/latest/qdrant_client/qdrant/struct.ScoredPoint.html)s to fit your desired output format.

##### Table of contents

- [ Initial setup ](https://qdrant.tech/documentation/tutorials/mighty/#initial-setup)
- [ Implement model API ](https://qdrant.tech/documentation/tutorials/mighty/#implement-model-api)
- [ Create embeddings and run a query ](https://qdrant.tech/documentation/tutorials/mighty/#create-embeddings-and-run-a-query)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/tutorials/mighty.md)
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