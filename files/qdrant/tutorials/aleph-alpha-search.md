# Multimodal Semantic Search with Aleph Alpha

| Time: 30 min | Level: Beginner |  |  |
|---|---|---|---|


This tutorial shows you how to run a proper multimodal semantic search system with a few lines of code, without the need to annotate the data or train your networks.

In most cases, semantic search is limited to homogenous data types for both documents and queries (text-text, image-image, audio-audio, etc.). With the recent growth of multimodal architectures, it is now possible to encode different data types into the same latent space. That opens up some great possibilities, as you can finally explore non-textual data, for example visual, with text queries.

In the past, this would require labelling every image with a description of what it presents. Right now, you can rely on vector embeddings, which can represent all
the inputs in the same space.

 *Figure 1: Two examples of text-image pairs presenting a similar object, encoded by a multimodal network into the same
2D latent space. Both texts are examples of English pangrams.
https://deepai.org generated the images with pangrams used as input prompts.* 

## Sample dataset

You will be using[ COCO ](https://cocodataset.org/), a large-scale object detection, segmentation, and captioning dataset. It provides
various splits, 330,000 images in total. For demonstration purposes, this tutorials uses the[ 2017 validation split ](http://images.cocodataset.org/zips/train2017.zip)that contains 5000 images from different
categories with total size about 19GB.

`wget http://images.cocodataset.org/zips/train2017.zip`

## Prerequisites

There is no need to curate your datasets and train the models.[ Aleph Alpha ](https://www.aleph-alpha.com/), already has multimodality and multilinguality already built-in. There is an[ official Python client ](https://github.com/Aleph-Alpha/aleph-alpha-client)that simplifies the integration.

In order to enable the search capabilities, you need to build the search index to query on. For this example,
you are going to vectorize the images and store their embeddings along with the filenames. You can then return the most
similar files for given query.

There are two things you need to set up before you start:

1. You need to have a Qdrant instance running. If you want to launch it locally,[ Docker is the fastest way to do that ](https://qdrant.tech/documentation/quick_start/#installation).
2. You need to have a registered[ Aleph Alpha account ](https://app.aleph-alpha.com/).
3. Upon registration, create an API key (see:[ API Tokens ](https://app.aleph-alpha.com/profile)).


Now you can store the Aleph Alpha API key in a variable and choose the model your are going to use.

```
aa_token  =   "<< your_token >>" 

model  =   "luminous-base" 

```

## Vectorize the dataset

In this example, images have been extracted and are stored in the `val2017` directory:

```
from   aleph_alpha_client   import  (

    Prompt,

    AsyncClient,

    SemanticEmbeddingRequest,

    SemanticRepresentation,

    Image,

)



from   glob   import  glob



ids, vectors, payloads  =  [], [], []

async   with  AsyncClient(token = aa_token)  as  client:

     for  i, image_path  in   enumerate (glob( "./val2017/*.jpg" )):

         # Convert the JPEG file into the embedding by calling 

         # Aleph Alpha API 

        prompt  =  Image . from_file(image_path)

        prompt  =  Prompt . from_image(prompt)

        query_params  =  {

             "prompt" : prompt,

             "representation" : SemanticRepresentation . Symmetric,

             "compress_to_size" :  128 ,

        }

        query_request  =  SemanticEmbeddingRequest( ** query_params)

        query_response  =   await  client . semantic_embed(request = query_request, model = model)



         # Finally store the id, vector and the payload 

        ids . append(i)

        vectors . append(query_response . embedding)

        payloads . append({ "filename" : image_path})

```

## Load embeddings into Qdrant

Add all created embeddings, along with their ids and payloads into the `COCO` collection.

```
import   qdrant_client 

from   qdrant_client.http.models   import  Batch, VectorParams, Distance



qdrant_client  =  qdrant_client . QdrantClient()

qdrant_client . recreate_collection(

    collection_name = "COCO" ,

    vectors_config = VectorParams(

        size = len (vectors[ 0 ]),

        distance = Distance . COSINE,

    )

)

qdrant_client . upsert(

    collection_name = "COCO" ,

    points = Batch(

        ids = ids,

        vectors = vectors,

        payloads = payloads,

    )

)

```

## Query the database

The `luminous-base` , model can provide you the vectors for both texts and images, which means you can run both
text queries and reverse image search. Assume you want to find images similar to the one below:

Image: [ An image used to query the database ](https://qdrant.tech/docs/integrations/aleph-alpha/visual_search_query.png)

Image: [ An image used to query the database ](https://qdrant.tech/docs/integrations/aleph-alpha/visual_search_query.png)

With the following code snippet create its vector embedding and then perform the lookup in Qdrant:

```
async   with  AsyncCliet(token = aa_token)  as  client:

    prompt  =  ImagePrompt . from_file( "query.jpg" )

    prompt  =  Prompt . from_image(prompt)



    query_params  =  {

         "prompt" : prompt,

         "representation" : SemanticRepresentation . Symmetric,

         "compress_to_size" :  128 ,

    }

    query_request  =  SemanticEmbeddingRequest( ** query_params)

    query_response  =   await  client . semantic_embed(request = query_request, model = model)



    results  =  qdrant . search(

        collection_name = "COCO" ,

        query_vector = query_response . embedding,

        limit = 3 ,

    )

     print (results)

```

Here are the results:

Image: [ Visual search results ](https://qdrant.tech/docs/integrations/aleph-alpha/visual_search_results.png)

Image: [ Visual search results ](https://qdrant.tech/docs/integrations/aleph-alpha/visual_search_results.png)

 **Note:** AlephAlpha models can provide embeddings for English, French, German, Italian
and Spanish. Your search is not only multimodal, but also multilingual, without any need for translations.

```
text  =   "Surfing" 



async   with  AsyncClient(token = aa_token)  as  client:

    query_params  =  {

         "prompt" : Prompt . from_text(text),

         "representation" : SemanticRepresentation . Symmetric,

         "compres_to_size" :  128 ,

    }

    query_request  =  SemanticEmbeddingRequest( ** query_params)

    query_response  =   await  client . semantic_embed(request = query_request, model = model)



    results  =  qdrant . search(

        collection_name = "COCO" ,

        query_vector = query_response . embedding,

        limit = 3 ,

    )

     print (results)

```

Here are the top 3 results for “Surfing”:

Image: [ Text search results ](https://qdrant.tech/docs/integrations/aleph-alpha/text_search_results.png)

Image: [ Text search results ](https://qdrant.tech/docs/integrations/aleph-alpha/text_search_results.png)

##### Table of contents

- [ Sample dataset ](https://qdrant.tech/documentation/tutorials/aleph-alpha-search/#sample-dataset)
- [ Prerequisites ](https://qdrant.tech/documentation/tutorials/aleph-alpha-search/#prerequisites)
- [ Vectorize the dataset ](https://qdrant.tech/documentation/tutorials/aleph-alpha-search/#vectorize-the-dataset)
- [ Load embeddings into Qdrant ](https://qdrant.tech/documentation/tutorials/aleph-alpha-search/#load-embeddings-into-qdrant)
- [ Query the database ](https://qdrant.tech/documentation/tutorials/aleph-alpha-search/#query-the-database)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/tutorials/aleph-alpha-search.md)
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