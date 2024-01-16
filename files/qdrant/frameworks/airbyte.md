# Airbyte

[ Airbyte ](https://airbyte.com/)is an open-source data integration platform that helps you replicate your data
between different systems. It has a[ growing list of connectors ](https://docs.airbyte.io/integrations)that can
be used to ingest data from multiple sources. Building data pipelines is also crucial for managing the data in
Qdrant, and Airbyte is a great tool for this purpose.

Airbyte may take care of the data ingestion from a selected source, while Qdrant will help you to build a search
engine on top of it. There are three supported modes of how the data can be ingested into Qdrant:

- **Full Refresh Sync**
- **Incremental - Append Sync**
- **Incremental - Append + Deduped**


You can read more about these modes in the[ Airbyte documentation ](https://docs.airbyte.io/integrations/destinations/qdrant).

## Prerequisites

Before you start, make sure you have the following:

1. Airbyte instance, either[ Open Source ](https://airbyte.com/solutions/airbyte-open-source),[ Self-Managed ](https://airbyte.com/solutions/airbyte-enterprise), or[ Cloud ](https://airbyte.com/solutions/airbyte-cloud).
2. Running instance of Qdrant. It has to be accessible by URL from the machine where Airbyte is running.
You can follow the[ installation guide ](https://qdrant.tech/documentation/guides/installation/)to set up Qdrant.


## Setting up Qdrant as a destination

Once you have a running instance of Airbyte, you can set up Qdrant as a destination directly in the UI.
Airbyte’s Qdrant destination is connected with a single collection in Qdrant.

Image: [ Airbyte Qdrant destination ](https://qdrant.tech/documentation/frameworks/airbyte/qdrant-destination.png)

Image: [ Airbyte Qdrant destination ](https://qdrant.tech/documentation/frameworks/airbyte/qdrant-destination.png)

### Text processing

Airbyte has some built-in mechanisms to transform your texts into embeddings. You can choose how you want to
chunk your fields into pieces before calculating the embeddings, but also which fields should be used to
create the point payload.

Image: [ Processing settings ](https://qdrant.tech/documentation/frameworks/airbyte/processing.png)

Image: [ Processing settings ](https://qdrant.tech/documentation/frameworks/airbyte/processing.png)

### Embeddings

You can choose the model that will be used to calculate the embeddings. Currently, Airbyte supports multiple
models, including OpenAI and Cohere.

Image: [ Embeddings settings ](https://qdrant.tech/documentation/frameworks/airbyte/embedding.png)

Image: [ Embeddings settings ](https://qdrant.tech/documentation/frameworks/airbyte/embedding.png)

Using some precomputed embeddings from your data source is also possible. In this case, you can pass the field
name containing the embeddings and their dimensionality.

Image: [ Precomputed embeddings settings ](https://qdrant.tech/documentation/frameworks/airbyte/precomputed-embedding.png)

Image: [ Precomputed embeddings settings ](https://qdrant.tech/documentation/frameworks/airbyte/precomputed-embedding.png)

### Qdrant connection details

Finally, we can configure the target Qdrant instance and collection. In case you use the built-in authentication
mechanism, here is where you can pass the token.

Image: [ Qdrant connection details ](https://qdrant.tech/documentation/frameworks/airbyte/qdrant-config.png)

Image: [ Qdrant connection details ](https://qdrant.tech/documentation/frameworks/airbyte/qdrant-config.png)

Once you confirm creating the destination, Airbyte will test if a specified Qdrant cluster is accessible and
might be used as a destination.

## Setting up connection

Airbyte combines sources and destinations into a single entity called a connection. Once you have a destination
configured and a source, you can create a connection between them. It doesn’t matter what source you use, as
long as Airbyte supports it. The process is pretty straightforward, but depends on the source you use.

Image: [ Airbyte connection ](https://qdrant.tech/documentation/frameworks/airbyte/connection.png)

Image: [ Airbyte connection ](https://qdrant.tech/documentation/frameworks/airbyte/connection.png)

More information about creating connections can be found in the[ Airbyte documentation ](https://docs.airbyte.com/understanding-airbyte/connections/).

##### Table of contents

- [ Prerequisites ](https://qdrant.tech/documentation/frameworks/airbyte/#prerequisites)
- [ Setting up Qdrant as a destination ](https://qdrant.tech/documentation/frameworks/airbyte/#setting-up-qdrant-as-a-destination)
    - [ Text processing ](https://qdrant.tech/documentation/frameworks/airbyte/#text-processing)

- [ Embeddings ](https://qdrant.tech/documentation/frameworks/airbyte/#embeddings)

- [ Qdrant connection details ](https://qdrant.tech/documentation/frameworks/airbyte/#qdrant-connection-details)
- [ Setting up connection ](https://qdrant.tech/documentation/frameworks/airbyte/#setting-up-connection)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/airbyte.md)
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