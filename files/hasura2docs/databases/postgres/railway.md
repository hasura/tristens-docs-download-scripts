# Connecting Hasura to a Railway Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ Railway Postgres database ](https://docs.railway.app/databases/postgresql)to a Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring Railway Postgres and are
interested in migrating an existing Postgres database - such as from Heroku - check out their[ docs ](https://railway.app/heroku)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/railway/#create-pg-db-railway).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
Postgres Database URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Postgres DB on Railway​

Log into[ Railway ](https://railway.app/dashboard).

From your dashboard, click `New Project` :

Image: [ Create a new project with Railway ](https://hasura.io/docs/assets/images/railway-new-project-5504c587761b38416573adc88813afa6.png)

Select `Provision PostgreSQL` :

Image: [ Create a new PG db with Railway ](https://hasura.io/docs/assets/images/railway-new-pg-dd08ec57d8e6a35ce0133448852845ca.png)

Railway will redirect you to the project's dashboard. After a few seconds, you should see the `Activity` card update
with information about your new instance. Congratulations! You've now created a Postgres instance on Railway which you
can use with Hasura GraphQL Engine. Follow the steps below to connect it to Hasura.

## Step 4: Get the database connection URL​

The structure of the database connection URL looks as follows:

`postgresql:// < user-name > : < password > @ < host-server > : < port > / < database-name >`

Click on the `PostgreSQL` card to see details related to this instance.

Image: [ Access your the details of the db from the card ](https://hasura.io/docs/assets/images/railway-choose-pg-c6700e013cd8562a9522ac359a452fa7.png)

Choose the `Connect` tab and copy the `Postgres Connection URL` :

Image: [ Go to the connect tab and grab the connection string ](https://hasura.io/docs/assets/images/railway-connection-string-5fae2da35b821b55953dbf209a3702fd.png)

## Step 5: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in the previous step:

Image: [ Connect the database on Hasura Console ](https://hasura.io/docs/assets/images/render-connect-db-4a2d659189e6c22cfc0a30df9e902702.png)

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

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/railway/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/railway/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/railway/#create-hasura-project)
- [ Step 3: Create a Postgres DB on Railway ](https://hasura.io/docs/latest/databases/postgres/railway/#create-pg-db-railway)
- [ Step 4: Get the database connection URL ](https://hasura.io/docs/latest/databases/postgres/railway/#get-db-url)
- [ Step 5: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/railway/#step-5-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/railway/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)