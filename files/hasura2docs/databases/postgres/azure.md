# Connecting Hasura to an Azure Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ Azure Postgres database ](https://azure.microsoft.com/en-us/products/postgresql/)to a Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring Azure Postgres and are interested
in migrating an existing Postgres database - such as from Heroku - check out their[ docs ](https://learn.microsoft.com/en-us/azure/dms/tutorial-postgresql-azure-postgresql-online-portal)before continuing
below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/azure/#create-pg-db-azure).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
Postgres Database URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Postgres DB on Azure​

Log into the[ Azure portal ](https://portal.azure.com).

On the Azure portal, type "postgres" in the search window and choose `Azure Database for PostgreSQL servers` :

Image: [ Navigate to 'Azure Database for PostgreSQL servers' ](https://hasura.io/docs/assets/images/navigate-4dfbe0a406f2e748b6cb2358d970c088.png)

Click the `+ Create` button to create a new Postgres database:

Image: [ Create a Postgres database on Azure ](https://hasura.io/docs/assets/images/create-db-5c60c3134ecca1384f07f33a2933d2fe.png)

Choose the plan that fits your requirements. For this tutorial, we'll choose `Flexible server` :

Image: [ Select 'Flexible server' on Azure ](https://hasura.io/docs/assets/images/select-db-95db8c285050eef7423d71b1ec158871.png)

Configure your database with all required fields:

Image: [ Configure database on Azure ](https://hasura.io/docs/assets/images/basic-configuration-c0e83404e0f13a3c6b4f2c8a2ff821cb.png)

Then click `Next : Networking >` .

## Step 4: Allow connections to your DB from Hasura​

If you're using Hasura Cloud, you can quickly find your IP address from the `Hasura Cloud IP` field on the project's
details view:

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/hasura-cloud-ip-86181dcc16cbac471b8a2c5237a23b24.png)

Self-hosted instances

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

Add the Hasura IP address that you copied:

Image: [ Add Hasura IP on Azure ](https://hasura.io/docs/assets/images/network-configuration-478f2f33cba68999370ff56c78aeaa1a.png)

Then click `Save` on the top left.

Optionally, select `Allow public access from any Azure service within Azure to this server` , if you require intra-Azure
connectivity.

Finally, click `Review + create` to review your settings, and if you're happy, create the database.

Postgres permissions

If you're using a database user other than the default one, make sure to give it the right[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#managed-pg-permissions).

JIT compatibility

For Azure flexible server, Hasura `v1.x` does not work with[ JIT ](https://www.postgresql.org/docs/11/runtime-config-query.html#GUC-JIT)turned on. JIT can be turned off from Azure
console. Hasura `v2.x` works fine with JIT enabled.

## Step 5: Construct the database connection URL​

The structure of the database connection URL looks as follows:

`postgresql:// < user-name > : < password > @ < public-ip > : < postgres-port > / < db >`

On the database dashboard, click on `Overview` :

Image: [ Construct the database connection string for Azure ](https://hasura.io/docs/assets/images/get-database-connection-string-9f4d815db2db4d9653c73f4f505795c9.png)

- `user-name` : If you have a separate database user, the user name will be their name. If you didn't specify a user, use
the `Admin username` (see screenshot above). **Note:** you need to escape the `@` . Replace it with `%40` .
- `password` : If you have a separate database user, use their password. Otherwise, use the password that you chose when
creating the database.
- `public-ip` : On the screenshot above, the `Server name` is the public IP.
- `postgres-port` : The default port for Postgres is `5432` .
- `db` : The DB is `postgres` by default unless otherwise specified.


## Step 6: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in[ step 5 ](https://hasura.io/docs/latest/databases/postgres/azure/#get-db-url-azure):

Image: [ Database setup ](https://hasura.io/docs/assets/images/azure-complete-45671b7337ba0e6b0cba13cca2563d3c.png)

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

For more information on which Postgres features we support, check out[ this page ](https://hasura.io/docs/latest/databases/feature-support/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/azure/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/azure/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/azure/#create-hasura-project-azure)
- [ Step 3: Create a Postgres DB on Azure ](https://hasura.io/docs/latest/databases/postgres/azure/#create-pg-db-azure)
- [ Step 4: Allow connections to your DB from Hasura ](https://hasura.io/docs/latest/databases/postgres/azure/#step-4-allow-connections-to-your-db-from-hasura)
- [ Step 5: Construct the database connection URL ](https://hasura.io/docs/latest/databases/postgres/azure/#get-db-url-azure)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/azure/#step-6-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/azure/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)