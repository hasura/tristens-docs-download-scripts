# Connecting Hasura to an Azure Cosmos DB for PostgreSQL

## Introduction​

This guide explains how to connect a new[ Azure Cosmos DB for PostgreSQL ](https://learn.microsoft.com/en-us/azure/cosmos-db/postgresql/introduction)to a Hasura
instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring Azure Cosmos DB for PostgreSQL,
check out their[ docs ](https://azure.microsoft.com/en-us/products/cosmos-db/#overview)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/azure-cosmos/#create-pg-db-azure).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
Postgres Database URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Cosmos DB on Azure​

You can start a free trial with[ Azure Cosmos DB ](https://cosmos.azure.com/try/). Select Azure Cosmos DB for PostgreSQL
and click `Create` :

Image: [ Create Azure Cosmos ](https://hasura.io/docs/assets/images/cosmos-create-45356b77c8d03a16b9e814e3e68b1bdc.png)

After signing up, you're redirected to your database's home on your Azure portal.

## Step 4: Get the connection string​

The structure of the database connection URL looks as follows:

`postgres:// < username > : < your_password > @ < host > : < port > / < db_name > ?sslmode = require`

Note

Be sure to update the password for the database before continuing. You can do this by clicking on the banner at the top
of the page.

Click `Connection strings` in the side navigation:

Image: [ Azure Cosmos DB Dashboard ](https://hasura.io/docs/assets/images/cosmos-dashboard-52bf9a81804906728d58dfa69461906e.png)

Copy the value labeled as `PostgreSQL connection URL` .

Image: [ Connection strings for the database ](https://hasura.io/docs/assets/images/cosmos-connection-url-161e5b25c2ac0fcce4472a56d00b8050.png)

## Step 5: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in[ step 4 ](https://hasura.io/docs/latest/databases/postgres/azure-cosmos/#get-db-url-azure-cosmos):

Image: [ Database setup ](https://hasura.io/docs/assets/images/cosmos-connect-3f4f791cd4f7c5fdf7c394974e665af0.png)

Then click `Connect Database` .

Note

For security reasons, it is recommended to set database URLs as[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/#manage-project-env-vars)and using the env vars to connect to the
databases in place of the raw database URLs.

Voilà. You are ready to start developing.

Image: [ Hasura Console ](https://hasura.io/docs/assets/images/hasura-console-5685707ef939a6ca7cc2c5fb6ed7dda8.png)

## Next steps​

- You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.
- If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/#manage-project-collaborators),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/#manage-project-env-vars)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/#manage-project-domains)).


You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.

If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/#manage-project-collaborators),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/#manage-project-env-vars)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/#manage-project-domains)).

Image: [ Project actions ](https://hasura.io/docs/assets/images/project-manage-5b37a214a39b39b6287136606da021c4.png)

Note

For more information on which Azure Cosmos DB features we support, check out[ this page ](https://hasura.io/docs/latest/databases/feature-support/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/azure-cosmos/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/azure-cosmos/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/azure-cosmos/#create-hasura-project-azure)
- [ Step 3: Create a Cosmos DB on Azure ](https://hasura.io/docs/latest/databases/postgres/azure-cosmos/#create-pg-db-azure)
- [ Step 4: Get the connection string ](https://hasura.io/docs/latest/databases/postgres/azure-cosmos/#get-db-url-azure-cosmos)
- [ Step 5: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/azure-cosmos/#step-5-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/azure-cosmos/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)