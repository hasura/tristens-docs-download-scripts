# Get Started with Hasura and MongoDB in Docker

## Introduction​

This guide will help you get set up with the[ Enterprise Edition ](https://hasura.io/docs/latest/enterprise/overview/)of Hasura GraphQL Engine
with our MongoDB integration using Docker Compose. This is the easiest way to set up Hasura Enterprise Edition and the
MongoDB GraphQL Data Connector.

Supported versions:

Hasura GraphQL Engine `v2.27.0` onwards

Supported features

Hasura currently supports queries, table relationships, remote relationships and permissions on MongoDB databases.

A[ logical model ](https://hasura.io/docs/latest/schema/mongodb/logical-models/)or database[ validation schema ](https://www.mongodb.com/docs/upcoming/core/schema-validation/specify-json-schema/#std-label-schema-validation-json)is required for generating your GraphQL schema.

## Deploying Hasura Enterprise with Docker​

### Prerequisites​

This tutorial assumes that the following prerequisites have been met:

- You have[ Docker ](https://docs.docker.com/install/)and[ Docker Compose ](https://docs.docker.com/compose/install/)working on your machine.
- You have[ MongoDB Compass ](https://www.mongodb.com/products/compass)installed on your machine.


### Step 1: Get the Docker Compose file​

The[ install manifests ](https://github.com/hasura/graphql-engine/tree/master/install-manifests)repo contains all
installation manifests required to deploy Hasura anywhere. The Docker Compose manifest also contains a Postgres database
in order to store the Hasura metadata and a Redis instance for caching.

```
# in a new directory run
wget  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/enterprise/mongodb/docker-compose.yaml
# or run
curl  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/enterprise/mongodb/docker-compose.yaml -o docker-compose.yml
```

Four containers are created

When you use these to launch the services, you'll see four containers running. The first two are Hasura GraphQL Engine
and a Postgres Database for storing Hasura's metadata. The third container is the MongoDB GraphQL Connector agent. The
fourth container is a copy of[ MongoDB Community Edition ](https://hub.docker.com/_/mongo).

### Step 2: Set the Hasura Enterprise Edition license key and the admin secret​

If you've been provided a license key by the Hasura team, you can edit the downloaded `docker-compose.yaml` to set
the license key and admin secret.

```
---
graphql-engine :
   image :  hasura/graphql - engine : v2.27.0
   environment :
     HASURA_GRAPHQL_EE_LICENSE_KEY :  <license key >
     HASURA_GRAPHQL_ADMIN_SECRET :  <your secretkey >
```

An[ admin secret key ](https://hasura.io/docs/latest/deployment/securing-graphql-endpoint/)is required to make sure that your GraphQL endpoint and
the Hasura Console are not publicly accessible.

I don't have a license key

If you don't already have a license key and are interested in trying out Hasura Enterprise Edition with MongoDB, you can
start a free 30-day trial. Leave the `HASURA_GRAPHQL_EE_LICENSE_KEY` environment variable commented out we'll return to
this in Step 6.

Secure the admin secret

The `HASURA_GRAPHQL_ADMIN_SECRET` should never be passed from the client to the Hasura GraphQL Engine as it would give
the client full admin rights to your Hasura instance. See[ Authentication & Authorization ](https://hasura.io/docs/latest/auth/overview/)for
information on setting up auth in Hasura.

### Step 3: Run the containers​

The following command will create and run the containers in the Docker Compose manifest:

`docker  compose up -d`

### Step 4: Create a MongoDB database​

I already have a MongoDB database

This guide assumes you don't have a MongoDB instance already set up. If you do, you can skip to[ Step 6 ](https://hasura.io/docs/latest/databases/mongodb/docker/#step-6-load-the-hasura-console).

Open[ MongoDB Compass ](https://www.mongodb.com/products/compass)and create a new connection using this connection string:

`mongodb://mongouser:mongopassword@localhost:27017/?authMechanism=DEFAULT`

Create a new database called demo using the MongoShell at the bottom of the MongoDB compass screen by entering the
command:

`use demo;`

Via MongoShell, create a new `users` collection:

`db . createCollection ( 'users' ) ;`

If you don't see your changes, you can refresh your databases on the left-hand sidebar. Once applied, you can view the `users` Collection in MongoDB Compass:

Image: [ Creating your first MongoDB Collection. ](https://hasura.io/docs/assets/images/mongo-collection-7b277fcac148f178e2bb3064cce842af.png)

### Step 5: Insert your first sample Documents​

Insert a few sample documents to query on afterwards.

```
db . users . insertMany ( [
   {
     name :   'John' ,
     age :   44 ,
     email :   'john@example.com' ,
     user_meta :   {
       user_role :   'user' ,
       email_verified :   true ,
     } ,
   } ,
   {
     name :   'Jane' ,
     age :   24 ,
     email :   'jane@example.com' ,
     user_meta :   {
       user_role :   'user' ,
       email_verified :   true ,
     } ,
   } ,
   {
     name :   'Emma' ,
     age :   36 ,
     email :   'emma@example.com' ,
     user_meta :   {
       user_role :   'manager' ,
       email_verified :   true ,
     } ,
   } ,
   {
     name :   'Liam' ,
     age :   64 ,
     email :   'liam@example.com' ,
     user_meta :   {
       user_role :   'manager' ,
       email_verified :   true ,
     } ,
   } ,
] ) ;
```

You should see an output similar to this:

Image: [ Inserting your sample Documents in MongoDB. ](https://hasura.io/docs/assets/images/mongo-documents-aeeeb3cdbca08bda573ba481c0185027.png)

### Step 6: Load the Hasura Console​

Open the Hasura Console by navigating to `http://localhost:8080/console` . You will need to input your admin secret key
as set in your Docker Compose file to log in.

30-day free trial

If you don't already have a license key, you can start a 30-day free trial by clicking the `ENTERPRISE` button in the
top navigation. You can read more details[ here ](https://hasura.io/docs/latest/enterprise/try-hasura-enterprise-edition/).

Image: [ Enterprise Edition Trial register button ](https://hasura.io/docs/assets/images/Trials_Register_Button-21f7c94a1f16bc85ed93899268a16ef2.png)

### Step 7: Connect to MongoDB​

Visit `Data` > `Manage` to connect your MongoDB database.
If you've connected using the Docker guide above, your MongoDB data connector should be pre-connected to your Hasura
instance.

Then click, `Connect Database` .

If you're using the Docker guide you can also connect your database using the following details:

- Database Name: `mongodb`
- Connection: `mongodb://mongouser:mongopassword@mongodb:27017`
- db: `demo`


Image: [ Connecting to MongoDB - Selecting MongoDB ](https://hasura.io/docs/assets/images/connection-1-mongodb-select-4ebb76bb74d0f068c3192b405a525980.png)

Image: [ Connecting to MongoDB - Connecting your database ](https://hasura.io/docs/assets/images/connection-2-mongodb-connect-database-e1534d332759ee24beb89514bb897ea7.png)

If you're using a MongoDB instance hosted on MongoDB Atlas or elsewhere, simply add the connection details for your
instance and click `Connect Database` .

### Step 8: Tracking Collections​

Once your database has been connected, select the database name from the left-hand sidebar.

You should see your `users` Collection listed here. Select it, and select `Track Selected` .

How do we generate your Collection's schema?

Since MongoDB is a NoSQL database, Documents can be variable within each of the Collections.
Hasura supports and recommends defining a[ logical model ](https://hasura.io/docs/latest/schema/mongodb/logical-models/)for each Collection which will define the Document schema.

We also support optionally generating a schema automatically from your database's[ validation schema ](https://www.mongodb.com/docs/upcoming/core/schema-validation/specify-json-schema/#std-label-schema-validation-json)if one is available.

Image: [ Tracking a Collection - Select Collection ](https://hasura.io/docs/assets/images/track-1-select-26fb00b79bd31f61a7bb609340219b6e.png)

You will now see a modal with a few options for setting up your Collection's schema.

- **Infer Schema from Document** allows you to take a single Document from your Collection and infer the
- **Use Existing Logical Model** allows you to select a previously created[ logical model ](https://hasura.io/docs/latest/schema/mongodb/logical-models/).
- **Use Database Schema** allows you to use your database's[ validation schema ](https://www.mongodb.com/docs/upcoming/core/schema-validation/specify-json-schema/#std-label-schema-validation-json)if one is present in your database (a GraphQL schema will be automatically generated for you).


Image: [ Tracking a Collection - Sample Documents ](https://hasura.io/docs/assets/images/track-2-sample-8c39b8f3a6dbe0b7cec20cf232f327b0.png)

Your `users` Collection is now added to your GraphQL API! 🎉

Make your Collection available to other roles

By default, this Collection is only available to `admin` users. To make it available for more user groups, select the
Collection name from the left-hand sidebar, and select `Permissions` to setup permission rules for the Collection. You
can read more about permissions[ here ](https://hasura.io/docs/latest/auth/authorization/index/).

### Step 9: Running your first query​

Select API from your header, this will take you to GraphiQL, our API testing utility.

Entering the following query and running will return all your users:

```
query   allUsers   {
   users   {
     _id
     age
     email
     name
     user_meta   {
       email_verified
       user_role
     }
   }
}
```

Image: [ Connecting to MongoDB - Making a GraphQL query. ](https://hasura.io/docs/assets/images/gql-query-0223174bc0b7ca5aa5f03d7fea885f7a.png)

Entering the following will only return users with the names 'John' or 'Jane':

```
query   userFiltered   {
   users ( where :   {   name :   {   _in :   [ "John" ,   "Jane" ]   }   } )   {
     _id
     age
     email
     name
     user_meta   {
       email_verified
       user_role
     }
   }
}
```

## Keep up to date​

Please watch this space to get the latest docs on how you can try these features out via the Console or by manipulating
Metadata in JSON/YAML directly.

If you'd like to stay informed about the status of MongoDB support, subscribe to our newsletter and join our Discord!

- [ Hasura Newsletter ](https://hasura.io/newsletter/)
- [ Hasura Discord ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/mongodb/docker/#introduction)
- [ Deploying Hasura Enterprise with Docker ](https://hasura.io/docs/latest/databases/mongodb/docker/#deploying-hasura-enterprise-with-docker)
    - [ Prerequisites ](https://hasura.io/docs/latest/databases/mongodb/docker/#prerequisites)

- [ Step 1: Get the Docker Compose file ](https://hasura.io/docs/latest/databases/mongodb/docker/#step-1-get-the-docker-compose-file)

- [ Step 2: Set the Hasura Enterprise Edition license key and the admin secret ](https://hasura.io/docs/latest/databases/mongodb/docker/#step-2-set-the-hasura-enterprise-edition-license-key-and-the-admin-secret)

- [ Step 3: Run the containers ](https://hasura.io/docs/latest/databases/mongodb/docker/#step-3-run-the-containers)

- [ Step 4: Create a MongoDB database ](https://hasura.io/docs/latest/databases/mongodb/docker/#step-4-create-a-mongodb-database)

- [ Step 5: Insert your first sample Documents ](https://hasura.io/docs/latest/databases/mongodb/docker/#step-5-insert-your-first-sample-documents)

- [ Step 6: Load the Hasura Console ](https://hasura.io/docs/latest/databases/mongodb/docker/#step-6-load-the-hasura-console)

- [ Step 7: Connect to MongoDB ](https://hasura.io/docs/latest/databases/mongodb/docker/#step-7-connect-to-mongodb)

- [ Step 8: Tracking Collections ](https://hasura.io/docs/latest/databases/mongodb/docker/#step-8-tracking-collections)

- [ Step 9: Running your first query ](https://hasura.io/docs/latest/databases/mongodb/docker/#step-9-running-your-first-query)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/mongodb/docker/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)