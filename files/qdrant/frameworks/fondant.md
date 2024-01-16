# ML6 Fondant

[ Fondant ](https://fondant.ai/en/stable/)is an open-source framework that aims to simplify and speed up large-scale data processing by making containerized components reusable across pipelines and execution environments.

Fondant features a Qdrant component image to load textual data and embeddings into a the database.

## Usage

 **A data load pipeline for RAG using Qdrant** .

```
from   fondant.pipeline   import  ComponentOp, Pipeline



pipeline  =  Pipeline(

    pipeline_name = "ingestion-pipeline" ,

    pipeline_description = "Pipeline to prepare and process  \

    data for building a RAG solution" ,

    base_path = "./data-dir" ,

)



# An example data source component 

load_from_source  =  ComponentOp(

    component_dir = "path/to/data-source-component" ,

    arguments = {

         "n_rows_to_load" :  10 ,

         # Custom arguments for the component 

    },

)



chunk_text_op  =  ComponentOp . from_registry(

    name = "chunk_text" ,

    arguments = {

         "chunk_size" :  512 ,

         "chunk_overlap" :  32 ,

    },

)



embed_text_op  =  ComponentOp . from_registry(

    name = "embed_text" ,

    arguments = {

         "model_provider" :  "huggingface" ,

         "model" :  "all-MiniLM-L6-v2" ,

    },

)



# Getting the Qdrant component from the Fondant registry 

index_qdrant_op  =  ComponentOp . from_registry(

    name = "index_qdrant" ,

    arguments = {

         "url" :  "http:localhost:6333" ,

         "collection_name" :  "some-collection-name" ,

    },

)



# Construct your pipeline 

pipeline . add_op(load_from_source)

pipeline . add_op(chunk_text_op, dependencies = load_from_source)

pipeline . add_op(embed_text_op, dependencies = chunk_text_op)

pipeline . add_op(index_qdrant_op, dependencies = embed_text_op)

```

## Next steps

Find the FondantAI docs[ here ](https://fondant.ai/en/stable/).

##### Table of contents

- [ Usage ](https://qdrant.tech/documentation/frameworks/fondant/#usage)
- [ Next steps ](https://qdrant.tech/documentation/frameworks/fondant/#next-steps)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/fondant.md)
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