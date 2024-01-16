# Connecting Hasura to a DigitalOcean Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ DigitalOcean Postgres ](https://www.digitalocean.com/products/managed-databases-postgresql)database to a Hasura
instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring DigitalOcean Postgres and are
interested in migrating an existing Postgres database - such as from Heroku - check out their[ docs ](https://docs.digitalocean.com/products/databases/postgresql/how-to/migrate/)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/digital-ocean/#create-pg-db-do).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
Postgres Database URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Postgres DB on DigitalOcean​

Log into[ DigitalOcean ](https://cloud.digitalocean.com/).

On the top right, click the `Create` button. Then click on `Databases` :

Image: [ Create database on DigitalOcean ](https://hasura.io/docs/assets/images/create-database-2b3f9e18946c84f49a1e28efcbc0b24f.png)

Scroll down and choose a `Cluster configuration` , as well as a `Datacenter` based on your requirements.

Scroll to the bottom and choose a unique database cluster name. Also, select a project the new database will be
associated with.

Image: [ Select cluster name for database on DigitalOcean ](https://hasura.io/docs/assets/images/cluster-name-552af5b78fae57f75e4f3a5161b4fcc5.png)

Then click `Create a Database Cluster` .

## Step 4: Allow connections to your DB from Hasura​

Navigate to the database cluster's `Overview` page:

Image: [ Navigate to database settings in DigitalOcean ](https://hasura.io/docs/assets/images/db-settings-fcea8132a76c43a751c9e5259c521605.png)

Scroll down to `Trusted sources` and click the `Edit` button:

Image: [ Edit trusted sources for database in DigitalOcean ](https://hasura.io/docs/assets/images/edit-trusted-sources-fab05a7814aaf19b2455316188400689.png)

If you're using Hasura Cloud, you can quickly find your IP address from the `Hasura Cloud IP` field on the project's
details view:

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/hasura-cloud-ip-86181dcc16cbac471b8a2c5237a23b24.png)

Note

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

Enter the Hasura IP address that you copied:

Image: [ Add Hasura IP to database in DigitalOcean ](https://hasura.io/docs/assets/images/add-hasura-ip-565007b44c975f05f844a8e25d916a58.png)

Then click `Save` .

Note

If you're using a database user other than the default one, make sure to give it the right[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#managed-pg-permissions).

## Step 5: Get the database connection URL​

The structure of the database connection URL looks as follows:

`postgresql:// < user-name > : < password > @ < public-ip > : < postgres-port > / < db > ?sslmode = require`

To get it, navigate to the database cluster's `Overview` page:

Image: [ Navigate to database overview in DigitalOcean ](https://hasura.io/docs/assets/images/db-overview-072a9dc932eefa96213ffde26144b810.png)

Scroll down to `Connection details` . Select `Public network` on the left and `Connection string` on the right.

Image: [ Get the database connection string in DigitalOcean ](https://hasura.io/docs/assets/images/connection-string-5aa1b08b77b54468e3f94c25fdac4378.png)

Then click the `Copy` button for the next step.

## Step 6: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in[ step 5 ](https://hasura.io/docs/latest/databases/postgres/digital-ocean/#get-db-url-do):

Image: [ Database setup ](https://hasura.io/docs/assets/images/DO-complete-ac15c347f676c037c1ccac743208cc48.png)

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

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/digital-ocean/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/digital-ocean/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/digital-ocean/#create-hasura-project-do)
- [ Step 3: Create a Postgres DB on DigitalOcean ](https://hasura.io/docs/latest/databases/postgres/digital-ocean/#create-pg-db-do)
- [ Step 4: Allow connections to your DB from Hasura ](https://hasura.io/docs/latest/databases/postgres/digital-ocean/#step-4-allow-connections-to-your-db-from-hasura)
- [ Step 5: Get the database connection URL ](https://hasura.io/docs/latest/databases/postgres/digital-ocean/#get-db-url-do)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/digital-ocean/#step-6-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/digital-ocean/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)