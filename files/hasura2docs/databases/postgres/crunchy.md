# Connecting Hasura to a Crunchy Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ Crunchy Postgres ](https://www.crunchydata.com/)database to a
Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring Crunchy Postgres and are
interested in migrating an existing Postgres database - such as from Heroku - check out their[ docs ](https://www.crunchydata.com/migrate-from-heroku)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/crunchy/#create-pg-db-crunchy).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
Postgres Database URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Postgres DB on Crunchy​

Log into[ Crunchy ](https://crunchybridge.com/dashboard).

From your dashboard, click `Create Cluster` :

Image: [ Crunchy dashboard ](https://hasura.io/docs/assets/images/crunchy-dashboard-9feabcd60c928d00eef03515762bfd3c.png)

Fill in the necessary information and click `Create Cluster` :

Image: [ Create a new cluster with Crunchy ](https://hasura.io/docs/assets/images/crunchy-create-cluster-273303b2ec1e583f027a08080c578627.png)

Note

After creating the cluster, you'll be redirected to its dashboard. Keep an eye on the `Status` row of the Cluster
Overview card. While you can access your connection string immediately, the cluster must first be provisioned in order
for Hasura to be able to connect.

Congratulations! You've now created a Postgres instance on Crunchy which you can use with Hasura GraphQL Engine. Follow
the steps below to connect it to Hasura.

## Step 4: Get the database connection URL​

The structure of the database connection URL looks as follows:

`postgres:// < user-name > : < password > @ < host-server > : < port > / < database-name >`

Click on the Hasura card to see your connection string:

Image: [ Create a new cluster with Crunchy ](https://hasura.io/docs/assets/images/crunchy-cluster-dashboard-a45aa0b870a53d872f1bf4312afa7463.png)

At the bottom of the instructions, we'll select `Superuser` (which will be `postgres` ) for our role:

Image: [ Create a new cluster with Crunchy ](https://hasura.io/docs/assets/images/crunchy-connection-string-user-c1e02a76f01725b8d9c66af04d42084f.png)

Copy the connection string:

Image: [ Create a new cluster with Crunchy ](https://hasura.io/docs/assets/images/crunchy-connection-string-full-b57a540de00f031971bc52d809de2bc9.png)

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

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/crunchy/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/crunchy/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/crunchy/#create-hasura-project)
- [ Step 3: Create a Postgres DB on Crunchy ](https://hasura.io/docs/latest/databases/postgres/crunchy/#create-pg-db-crunchy)
- [ Step 4: Get the database connection URL ](https://hasura.io/docs/latest/databases/postgres/crunchy/#get-db-url)
- [ Step 5: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/crunchy/#step-5-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/crunchy/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)