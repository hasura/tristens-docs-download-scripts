# DLT(Data Load Tool)

[ DLT ](https://dlthub.com/)is an open-source library that you can add to your Python scripts to load data from various and often messy data sources into well-structured, live datasets.

With the DLT-Qdrant integration, you can now select Qdrant as a DLT destination to load data into.

 **DLT Enables** 

- Automated maintenance - with schema inference, alerts and short declarative code, maintenance becomes simple.
- Run it where Python runs - on Airflow, serverless functions, notebooks. Scales on micro and large infrastructure alike.
- User-friendly, declarative interface that removes knowledge obstacles for beginners while empowering senior professionals.


## Usage

To get started, install `dlt` with the `qdrant` extra.

`pip install  "dlt[qdrant]" 
`

Configure the destination in the DLT secrets file. The file is located at `~/.dlt/secrets.toml` by default. Add the following section to the secrets file.

```
[destination.qdrant.credentials]

location =  "https://your-qdrant-url" 

api_key =  "your-qdrant-api-key" 

```

The location will default to `http://localhost:6333` and `api_key` is not defined - which are the defaults for a local Qdrant instance.
Find more information about DLT configurations[ here ](https://dlthub.com/docs/general-usage/credentials).

Define the source of the data.

```
import   dlt 

from   dlt.destinations.qdrant   import  qdrant_adapter



movies  =  [

    {

         "title" :  "Blade Runner" ,

         "year" :  1982 ,

         "description" :  "The film is about a dystopian vision of the future that combines noir elements with sci-fi imagery." 

    },

    {

         "title" :  "Ghost in the Shell" ,

         "year" :  1995 ,

         "description" :  "The film is about a cyborg policewoman and her partner who set out to find the main culprit behind brain hacking, the Puppet Master." 

    },

    {

         "title" :  "The Matrix" ,

         "year" :  1999 ,

         "description" :  "The movie is set in the 22nd century and tells the story of a computer hacker who joins an underground group fighting the powerful computers that rule the earth." 

    }

]

```

Define the pipeline.

```
pipeline  =  dlt . pipeline(

    pipeline_name = "movies" ,

    destination = "qdrant" ,

    dataset_name = "movies_dataset" ,

)

```

Run the pipeline.

```
info  =  pipeline . run(

    qdrant_adapter(

        movies,

        embed = [ "title" ,  "description" ]

    )

)

```

The data is now loaded into Qdrant.

To use vector search after the data has been loaded, you must specify which fields Qdrant needs to generate embeddings for. You do that by wrapping the data (or[ DLT resource ](https://dlthub.com/docs/general-usage/resource)) with the `qdrant_adapter` function.

## Write disposition

A DLT[ write disposition ](https://dlthub.com/docs/dlt-ecosystem/destinations/qdrant/#write-disposition)defines how the data should be written to the destination. All write dispositions are supported by the Qdrant destination.

## DLT Sync

Qdrant destination supports syncing of the[ DLT state ](https://dlthub.com/docs/general-usage/state#syncing-state-with-destination).

## Next steps

- The comprehensive Qdrant DLT destination documentation can be found[ here ](https://dlthub.com/docs/dlt-ecosystem/destinations/qdrant/).


##### Table of contents

- [ Usage ](https://qdrant.tech/documentation/frameworks/dlt/#usage)
- [ Write disposition ](https://qdrant.tech/documentation/frameworks/dlt/#write-disposition)
- [ DLT Sync ](https://qdrant.tech/documentation/frameworks/dlt/#dlt-sync)
- [ Next steps ](https://qdrant.tech/documentation/frameworks/dlt/#next-steps)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/dlt.md)
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