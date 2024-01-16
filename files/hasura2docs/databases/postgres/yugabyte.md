# Connecting Hasura to a Yugabyte Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ Yugabyte Postgres database ](https://www.yugabyte.com/)to a Hasura
instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring Yugabyte Postgres and are
interested in migrating an existing Postgres database - such as from Heroku - check out their[ docs ](https://docs.yugabyte.com/preview/migrate/migrate-steps/)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/yugabyte/#create-pg-db-yugabyte).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

You will get prompted for a Postgres Database URL. We will create this in the next step and then come back here.

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to `Data -> Manage -> Connect Database -> Connect existing database` :

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Postgres DB on Yugabyte​

Log into the[ Yugabyte Cloud dashboard ](https://cloud.yugabyte.com/login).

On the Yugabyte Cloud dashboard, click on `Create a free cluster` :

Image: [ Create cluster on Yugabyte ](https://hasura.io/docs/assets/images/yb-step-2-0c69e83aebea09a6bfb3680458761eb5.png)

Select the `Managed Free` option and then click `Next` .

Image: [ Managed Free cluster on Yugabyte ](https://hasura.io/docs/assets/images/yb-step-3a-fa0e49d0ddb80786dea12d3868e962e7.png)

Select a `Cloud Provider` and `Region` and then click `Next` .

Image: [ Cloud Provider and Region on Yugabyte ](https://hasura.io/docs/assets/images/yb-step-3b-07f87fc640c522ac65294cb72857110e.png)

Note

If you're using a database user other than the default one, make sure to give it the right[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#managed-pg-permissions).

Download your credentials and then click `Create Cluster` .

Image: [ Create cluster on Yugabyte after downloading credentials ](https://hasura.io/docs/assets/images/yb-step-3c-224de784be4a73652b152a67e84ac4f9.png)

## Step 4: Allow connections to your DB from Hasura​

From the cluster's dashboard, click `Add IP Allow List` :

Image: [ Add IP Allow List on Yugabyte ](https://hasura.io/docs/assets/images/yb-step-3d-e276e03fa993e260c017d4b1214c2c0a.png)

Within the modal, click `Create New List and Add to Cluster` :

Image: [ Create New List and Add to Cluster on Yugabyte ](https://hasura.io/docs/assets/images/yb-step-3e-9f5823b26f0058f51f05d1e492cea6e4.png)

If using Hasura Cloud, from your project's dashboard, copy the Hasura Cloud IP address:

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/hasura-cloud-ip-86181dcc16cbac471b8a2c5237a23b24.png)

Note

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

Image: [ Add Hasura IP to database in Allow List on Yugabyte ](https://hasura.io/docs/assets/images/yb-step-3f-c6fe9c2a2abc2cf868700daee298bf85.png)

Then click `Save` .

## Step 5: Construct the database connection URL​

The structure of the database connection URL looks as follows:

`postgresql:// < user-name > : < password > @ < public-ip > : < postgres-port > / < db > ?ssl = true & sslmode = require`

To get it, from the cluster's dashboard, click `Run your own application` :

Image: [ Run your own application on cluster dashboard ](https://hasura.io/docs/assets/images/yb-step-3g-026d58a32260c6ea4181dda02d4130cc.png)

Click the `Optimize for Hasura Cloud` checkbox and then copy your connection string:

Image: [ Copy connection string on cluster dashboard ](https://hasura.io/docs/assets/images/yb-step-3h-0ee9ade2ef9e34e3d971c0d5b252f82f.png)

## Step 6: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we just copied and replace the `<DB USER>` and `<DB PASSWORD>` with the information from your credentials downloaded in[ step 3 ](https://hasura.io/docs/latest/databases/postgres/yugabyte/#create-pg-db-yugabyte):

Image: [ Database setup ](https://hasura.io/docs/assets/images/yb-step-3i-6a84c233259844bde0c93ff1d8628852.png)

Then click `Connect Database` .

Note

For security reasons, it is recommended to set database URLs as[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)and
using the env vars to connect to the databases in place of the raw database URLs.

Voilà. You are ready to start developing.

Image: [ Hasura Console ](https://hasura.io/docs/assets/images/hasura-console-5685707ef939a6ca7cc2c5fb6ed7dda8.png)

## Next steps​

- You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura. If you're completely
new to Yugabyte and want to learn more, check out[ this tutorial ](https://hasura.io/learn/database/yugabyte/introduction/)from our Learn site.
- If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).


You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura. If you're completely
new to Yugabyte and want to learn more, check out[ this tutorial ](https://hasura.io/learn/database/yugabyte/introduction/)from our Learn site.

If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).

Image: [ Project actions ](https://hasura.io/docs/assets/images/project-manage-5b37a214a39b39b6287136606da021c4.png)

Note

For more information on which Postgres features we support, check out[ this page ](https://hasura.io/docs/latest/databases/feature-support/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/yugabyte/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/yugabyte/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/yugabyte/#create-hasura-project-yugabyte)
- [ Step 3: Create a Postgres DB on Yugabyte ](https://hasura.io/docs/latest/databases/postgres/yugabyte/#create-pg-db-yugabyte)
- [ Step 4: Allow connections to your DB from Hasura ](https://hasura.io/docs/latest/databases/postgres/yugabyte/#step-4-allow-connections-to-your-db-from-hasura)
- [ Step 5: Construct the database connection URL ](https://hasura.io/docs/latest/databases/postgres/yugabyte/#construct-db-url-yugabyte)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/yugabyte/#step-6-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/yugabyte/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)