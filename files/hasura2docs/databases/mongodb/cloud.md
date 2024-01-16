# Get Started with MongoDB in Hasura Cloud

## Introduction​

This guide will help you get set up with[ Hasura Cloud ](https://hasura.io/docs/latest/hasura-cloud/overview/)and our MongoDB integration. This is
the easiest way to set up Hasura Engine and the MongoDB GraphQL Data Connector.

Supported versions:

Hasura GraphQL Engine `v2.27.0` onwards

Supported features

Hasura currently supports queries, table relationships, remote relationships and permissions on MongoDB databases.

A[ logical model ](https://hasura.io/docs/latest/schema/mongodb/logical-models/)or database[ validation schema ](https://www.mongodb.com/docs/upcoming/core/schema-validation/specify-json-schema/#std-label-schema-validation-json)is required for generating your GraphQL schema.

## Try it out​

### Step 1: Create an account on Hasura Cloud and create a new Hasura Project​

Navigate to your[ Hasura Cloud account ](https://cloud.hasura.io/)or[ create a new one ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-cloud-hasura-io&tech=default&skip_onboarding=true)if you do not have one.

Create a project on Hasura Cloud and hit the "Launch Console" button to open the Hasura Console for your project.

Image: [ Connect new or existing database ](https://hasura.io/docs/assets/images/create-project-8451135f7ff89b8f6e8fb3d29fd01ade.png)

### Step 2: Connect to MongoDB​

From the Console, visit `Data` > `Manage` to connect your MongoDB database.

Then click, `Connect Database` .

Connect your database using the following details:

- Database Name: (visual name of the database in Hasura)
- Connection: (in the format of `mongodb://[username]:[password]@[host]:[port]` )
- db: (name of the MongoDB database being connected to)


Image: [ Connecting to MongoDB - Selecting MongoDB ](https://hasura.io/docs/assets/images/connection-1-mongodb-select-4ebb76bb74d0f068c3192b405a525980.png)

Image: [ Connecting to MongoDB - Connecting your database ](https://hasura.io/docs/assets/images/connection-2-mongodb-connect-database-e1534d332759ee24beb89514bb897ea7.png)

### Step 3: Tracking Collections​

Once your database has been connected, select the database name from the left-hand sidebar.

You should see your `users` Collection listed here. Select it, and select `Track Selected` .

How do we generate your Collection's schema?

Since MongoDB is a NoSQL database, Documents can be variable within each of the Collections.
Hasura supports and recommends defining a[ logical model ](https://hasura.io/docs/latest/schema/mongodb/logical-models/)for each Collection
which will define the Document schema.

We also support optionally generating a schema automatically from your database's[ validation schema ](https://www.mongodb.com/docs/upcoming/core/schema-validation/specify-json-schema/#std-label-schema-validation-json)if one is available.

Image: [ Tracking a Collection - Select Collection ](https://hasura.io/docs/assets/images/track-1-select-26fb00b79bd31f61a7bb609340219b6e.png)

You will now see a modal with a few options for setting up your Collection's schema.

- **Infer Schema from Document** allows you to take a single Document from your Collection and infer the
- **Use Existing Logical Model** allows you to select a previously created[ logical model ](https://hasura.io/docs/latest/schema/mongodb/logical-models/).
- **Use Database Schema** allows you to use your database's[ validation schema ](https://www.mongodb.com/docs/upcoming/core/schema-validation/specify-json-schema/#std-label-schema-validation-json)if one is present in your database (a GraphQL schema will be automatically generated for you).


Image: [ Tracking a Collection - Sample Documents ](https://hasura.io/docs/assets/images/track-2-sample-8c39b8f3a6dbe0b7cec20cf232f327b0.png)

Your Collection has now added to your GraphQL API! 🎉

Make your Collection available to other roles

By default, this Collection is only available to `admin` users. To make it available for more user groups, select the
Collection name from the left-hand sidebar, and select `Permissions` to setup permission rules for the Collection. You
can read more about permissions[ here ](https://hasura.io/docs/latest/auth/authorization/index/).

### Step 4: Running your first query​

Click on the API tab in the Console navigation which will take you to GraphiQL, our API testing tool.

Utilize the explorer located on the left-hand sidebar to assist you in composing your query (the resulting query will
be populated in the body area). When you’re ready, click on the play button to execute your GraphQL query.
Your query’s result will be populated in the right-hand column of the interface.

Image: [ Connecting to MongoDB - Making a GraphQL query. ](https://hasura.io/docs/assets/images/gql-query-0223174bc0b7ca5aa5f03d7fea885f7a.png)

## Keep up to date​

If you'd like to stay informed about the status of MongoDB support, subscribe to our newsletter and join our Discord!

- [ Hasura Newsletter ](https://hasura.io/newsletter/)
- [ Hasura Discord ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/mongodb/cloud/#introduction)
- [ Try it out ](https://hasura.io/docs/latest/databases/mongodb/cloud/#try-it-out)
    - [ Step 1: Create an account on Hasura Cloud and create a new Hasura Project ](https://hasura.io/docs/latest/databases/mongodb/cloud/#step-1-create-an-account-on-hasura-cloud-and-create-a-new-hasura-project)

- [ Step 2: Connect to MongoDB ](https://hasura.io/docs/latest/databases/mongodb/cloud/#step-2-connect-to-mongodb)

- [ Step 3: Tracking Collections ](https://hasura.io/docs/latest/databases/mongodb/cloud/#step-3-tracking-collections)

- [ Step 4: Running your first query ](https://hasura.io/docs/latest/databases/mongodb/cloud/#step-4-running-your-first-query)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/mongodb/cloud/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)