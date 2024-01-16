# Connecting Hasura to a MongoDB Atlas hosted database

## Introduction​

This guide explains how to connect a new or existing[ MongoDB Atlas hosted database ](https://www.mongodb.com/docs/atlas/getting-started/)to a Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions.

Hasura Cloud vs self-hosting

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/mongodb/mongodb-atlas/#create-pg-db-gcp).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is successfully initialized, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a `mongodb:// URL` . We'll grab this after creating our database and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/mongodb-connect-db-efeefb94cc538bf3a5e6d19bb7b109b9.png)

## Step 3: Create a Database in MongoDB Atlas​

Existing database

If you have an existing database on MongoDB Atlas, you can skip this step and move on to[ step 4 ](https://hasura.io/docs/latest/databases/mongodb/mongodb-atlas/#allow-connections).

Log into the[ MongoDB Atlas control panel ](https://cloud.mongodb.com/).

On the left-side navigation, under `Deployment` , click on `Database` .

Select `Build a Database` when prompted.

Image: [ MongoDB Atlas Build Database ](https://hasura.io/docs/assets/images/1-atlas-build-db-17a64110d3ff3bdbc17cfbd401a06d28.png)

Select your instance type, and enter your MongoDB cluster specifics.

Match your MongoDB Atlas and Hasura Cloud hosting provider and region.

Keeping your MongoDB Atlas in the same hosting provider and region as your Hasura Cloud project will help reduce latency and will yield the best performance.

Image: [ MongoDB Atlas Instance Details ](https://hasura.io/docs/assets/images/2-atlas-database-1c21133308010f45e79d4b8f7d553183.png)

## Step 4: Allow connections to your MongoDB Atlas database from Hasura​

We need to allowlist the IP on which Hasura is running to be able to communicate with the database.

After clicking create you should be taken to the Quickstart for your MongoDB cluster.

At this stage you can configure any other credentials for your cluster as needed and setup your MongoDB cluster to allow connecting to your Hasura Cloud project.

If using Hasura Cloud, from your project's dashboard, copy the Hasura Cloud IP address:

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/hasura-cloud-ip-86181dcc16cbac471b8a2c5237a23b24.png)

Self-hosted IP addresses

If you're using a self-hosted solution, you can select `Add My Current IP Address` to allow the local IP address that you're connected from, if hosting on the same IP as your instance - or you can retrieve the IP address from your self-hosted server.

At the bottom of your MongoDB Atlas Quickstart, there should be an area for `Where would you like to connect from?` .
(If you don't see this, you can also access IP whitelisting through the `Network Access` section in the left sidebar).

Then to setup your allowed IP address:

- Select Cloud Environment for the type of IP address.
- Enter the Hasura IP address that you copied along with a name (e.g., `Hasura` ):


Image: [ Add a new network in MongoDB Atlas ](https://hasura.io/docs/assets/images/3-hasura-network-2eceec8745c80f5aab294b639174f2e3.png)

Then click `Finish and Close` at the bottom of the page.

## Step 5: Get your database connection URL​

Once you've finished the getting started guide select `Database` from the top-left corner.
When you get a listing of your database clusters, select `Connect` on the one you just created.

Image: [ MongoDB Atlas - Connect to database ](https://hasura.io/docs/assets/images/4-atlas-connect-database-21ee7ef056d21d211999265647db96b5.png)

You should get a number of options for how to connect, from here select `Drivers` :

Image: [ MongoDB Atlas - Select drivers ](https://hasura.io/docs/assets/images/4-atlas-options-b1c07b0100e4dc5614c782c1c4847246.png)

From the drivers instructions you can select and copy your connection connection string (note: you'll have to swap out your database's user access control password manually):

Image: [ MongoDB Atlas - Get connection string ](https://hasura.io/docs/assets/images/4-atlas-connection-string-8398753b2643119a7c55949ee0b16821.png)

If you've forgotten your MongoDB Atlas database user password, you can reset it from `Database Access` in the left-hand sidebar.

Image: [ MongoDB Atlas - Reset Password ](https://hasura.io/docs/assets/images/4-atlas-reset-password-9462ece98a4724cbace0a0bb67b21a75.png)

## Step 6: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in[ step 5 ](https://hasura.io/docs/latest/databases/mongodb/mongodb-atlas/#atlas-get-url)under `connection` .

Your `db` is the database name within your cluster.
If you've loaded the sample data, there should be a few samples available (such as `sample_analytics` ).

Image: [ Database setup ](https://hasura.io/docs/assets/images/5-database-url-3b5dc5c3ce98df73f5c54994e2ab2cbb.png)

Then click `Connect Database` .

Voilà. You are ready to start developing.

Image: [ Hasura Console ](https://hasura.io/docs/assets/images/hasura-console-5685707ef939a6ca7cc2c5fb6ed7dda8.png)

## Next steps​

- You can check out getting started guide for MongoDB on[ Cloud ](https://hasura.io/docs/latest/databases/mongodb/cloud/)or using[ Docker ](https://hasura.io/docs/latest/databases/mongodb/docker/)for a more detailed instructions for setting up your MongoDB database with Hasura.
- You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.
- If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).


You can check out getting started guide for MongoDB on[ Cloud ](https://hasura.io/docs/latest/databases/mongodb/cloud/)or using[ Docker ](https://hasura.io/docs/latest/databases/mongodb/docker/)for a more detailed instructions for setting up your MongoDB database with Hasura.

You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.

If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).

Image: [ Project actions ](https://hasura.io/docs/assets/images/project-manage-5b37a214a39b39b6287136606da021c4.png)

MongoDB feature support

For more information on which MongoDB features we support, check out[ this page ](https://hasura.io/docs/latest/databases/mongodb/index/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/mongodb/mongodb-atlas/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/mongodb/mongodb-atlas/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/mongodb/mongodb-atlas/#create-hasura-project-atlas)
- [ Step 3: Create a Database in MongoDB Atlas ](https://hasura.io/docs/latest/databases/mongodb/mongodb-atlas/#create-atlas-db)
- [ Step 4: Allow connections to your MongoDB Atlas database from Hasura ](https://hasura.io/docs/latest/databases/mongodb/mongodb-atlas/#allow-connections)
- [ Step 5: Get your database connection URL ](https://hasura.io/docs/latest/databases/mongodb/mongodb-atlas/#atlas-get-url)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/mongodb/mongodb-atlas/#step-6-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/mongodb/mongodb-atlas/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)