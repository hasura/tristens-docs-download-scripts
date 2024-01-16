# Connect Hasura to Weaviate

## Introduction​

[ Weaviate ](https://weaviate.io/)is a cloud-native, modular, real-time vector search engine that allows you to build
intelligent applications by using machine learning models as the data layer. It is open-source and can be deployed
on-premise or in the cloud.

Connecting vector databases to Hasura

To connect a vector database to Hasura, you'll need to take advantage of[ Hasura Data Connectors ](https://hasura.io/docs/latest/databases/data-connectors/). You can deploy any custom data connector agent to Hasura
Cloud using our CLI plugin. For more information, refer to the[ docs ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/).

If you're curious what other connectors are available, check out our[ NDC Hub ](https://github.com/hasura/ndc-hub).

## Step 1: Deploy a data connector agent​

We'll use the Hasura CLI to deploy a custom data connector agent to Hasura Cloud. Below, we're using the `create` command and naming our connector `weaviate-connector:v1` . We're also passing in the GitHub repo URL for the connector
agent using the `--github-repo-url` flag:

`hasura connector create weaviate-connector:v1 --github-repo-url https://github.com/hasura/weaviate_gdc/tree/main`

We can check on the progress of the deployment using the `status` command:

`hasura connector status weaviate-connector:v1`

Once the `DONE` status is returned, we can grab the URL for our data connector agent using the `list` command:

`hasura connector list`

This will return a list of all the custom data connector agents you own. **The second value returned is the URL which
we'll use in the next step; copy it to your clipboard.** 

## Step 2: Add the data connector agent to your Hasura Cloud project​

In your Cloud project, navigate to the `Data` tab and click `Manage` in the left-hand sidebar.

At the bottom of the screen, you'll see an expandable section titled `Data Connector Agents` .

Image: [ Add the agent for a Weaviate database ](https://hasura.io/docs/assets/images/weaviate_add-agent-11a552f3b592d1a359b8335f5c88515b.png)

Click this and scroll down to `Add Agent` .

Name this agent `weaviate` and paste the URL you copied from the CLI into the `URL` field and click `Connect` .

Image: [ Add the agent for a Weaviate database ](https://hasura.io/docs/assets/images/weaviate_configure-agent-9ad09330a817b5cf3ab0b126e0d01893.png)

## Step 3: Select the driver​

Navigate to the `Data` tab and select `Connect Database` , then select `Weaviate` from the list of drivers:

Image: [ Configure the Weaviate agent ](https://hasura.io/docs/assets/images/weaviate_connect-db-07eb8ad8167113b53c674bab8ba5ed1a.png)

## Step 4: Connect your database​

At this point, we'll need to configure a few parameters:

Image: [ Connect Weaviate database ](https://hasura.io/docs/assets/images/connect-weaveate-database-f8039e47f1c43c1b95dbe207546a6585.png)

| Parameter | Description |
|---|---|
| Database Name | The name of your Weaviate database. |
|  `apiKey`  | The API key for your Weaviate database. |
|  `host`  | The URL of your Weaviate database. |
|  `openAPIKey`  | The OpenAI key for use with your Weaviate database. |
|  `scheme`  | The URL scheme for your Weaviate database (http/https). |


Where can I find these parameters?

For the Weaviate-specific parameters, on the[ Weaviate Cloud Services' Console ](https://console.weaviate.cloud/dashboard), you can see your cluster's connection
information on the cluster's card.

You can register for an OpenAI key[ here ](https://openai.com/blog/openai-api).

## Step 5: Track your tables​

To make schemas accessible for querying using GraphQL, we'll need to track them. In the example below, we're tracking a
schema called `Resume` by checking the box next to it and clicking `Track Selected` :

Image: [ Connect Weaviate database ](https://hasura.io/docs/assets/images/track-tables-71a2b79bf2c3ea9e698748e7b6586cb8.png)

Tracking this schema will generate a type available in your GraphQL API that you can query against 🎉

Don't have any tables to track?

You will need to define the schema in your vector database. For a walkthrough of setting up a Weaviate schema, refer to
this[ tutorial ](https://weaviate.io/developers/weaviate/configuration/schema-configuration).

## Step 6: Define a remote relationship​

The information stored in Weaviate is vectorized and not in a human-readable format. We want to be able to return the
information from our relational database using the vectorized data from Weaviate. To do this, we need to define a remote
relationship.

In the example below, we're defining a remote relationship between the `Resume` schema in our vector database and the `application` table in our relational database. This way, whenever we query the vectorized information in our `Resume` table, we can return the information from our relational database.

Image: [ Define remote relationship ](https://hasura.io/docs/assets/images/define-remote-relationship-267b7aaae050ea67964037ec437d009e.png)

## Step 7: Query your data​

You can now query across both your vector database and your existing relational database tables as if they were in one
location!

In our example, we have two tables in our relational database:

1. `candidate`


Image: [ Candidate 1 table ](https://hasura.io/docs/assets/images/candidate-e1f408e26afe8aac9847fac73dfb2ad3.png)

1. `application`


Image: [ Application 2 table ](https://hasura.io/docs/assets/images/application-aed493965d82a8b75a93f78a2d4b1f07.png)

Our vector database stores the resumes as:

Image: [ Resume store ](https://hasura.io/docs/assets/images/resume-store-aefd57ed64ecbfa247bd3af4134f46be.png)

If we head to the `API` tab in the Hasura Console, in our GraphQL query, we are able to fetch all the candidate and
application information for a resume. Hasura brings this all together to provide this seamless querying experience.

Image: [ Execute query ](https://hasura.io/docs/assets/images/execute-query-0a5b6adcc66607c34390c4117930b3e8.png)

## Next Steps​

- Check out our[ Learn tutorial ](https://hasura.io/learn/graphql/vectordbs/introduction/)on Generative AI using Hasura,
Weaviate, Next.js and Tailwind CSS 🎉
- Learn more about[ Hasura Data Connectors ](https://hasura.io/docs/latest/databases/data-connectors/).
- Check out the available connectors on the[ NDC Hub ](https://github.com/hasura/ndc-hub)... or build your own!


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/vector-databases/weaviate/#introduction)
- [ Step 1: Deploy a data connector agent ](https://hasura.io/docs/latest/databases/vector-databases/weaviate/#step-1-deploy-a-data-connector-agent)
- [ Step 2: Add the data connector agent to your Hasura Cloud project ](https://hasura.io/docs/latest/databases/vector-databases/weaviate/#step-2-add-the-data-connector-agent-to-your-hasura-cloud-project)
- [ Step 3: Select the driver ](https://hasura.io/docs/latest/databases/vector-databases/weaviate/#step-3-select-the-driver)
- [ Step 4: Connect your database ](https://hasura.io/docs/latest/databases/vector-databases/weaviate/#step-4-connect-your-database)
- [ Step 5: Track your tables ](https://hasura.io/docs/latest/databases/vector-databases/weaviate/#step-5-track-your-tables)
- [ Step 6: Define a remote relationship ](https://hasura.io/docs/latest/databases/vector-databases/weaviate/#step-6-define-a-remote-relationship)
- [ Step 7: Query your data ](https://hasura.io/docs/latest/databases/vector-databases/weaviate/#step-7-query-your-data)
- [ Next Steps ](https://hasura.io/docs/latest/databases/vector-databases/weaviate/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)