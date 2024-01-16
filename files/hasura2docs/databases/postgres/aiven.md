# Connecting Hasura to an Aiven Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ Aiven Postgres ](https://aiven.io/postgresql?utm_source=website&utm_medium=referral&utm_campaign=hasura)database to a
Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring Aiven and are interested in
migrating an existing Postgres database - such as from Heroku - check out their[ docs ](https://docs.aiven.io/docs/products/postgresql/howto/migrate-pg-dump-restore?utm_source=website&utm_medium=referral&utm_campaign=hasura)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/aiven/#create-pg-db-aiven).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
Postgres Database URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Postgres DB on Aiven​

Note

If you have an existing Aiven Postgres database, you can skip this step and move on to[ step 4 ](https://hasura.io/docs/latest/databases/postgres/aiven/#connect-hasura-aiven).

Log into the[ Aiven console ](https://console.aiven.io/signup?utm_source=website&utm_medium=referral&utm_campaign=hasura).

On the Aiven console, click `+ Create a new service` :

Image: [ Create a new service on Aiven ](https://hasura.io/docs/assets/images/create-new-service-89f41e6b832966fa7fa0f7e8bba470b3.png)

Select `Postgres` :

Image: [ Select Postgres on Aiven ](https://hasura.io/docs/assets/images/select-postgres-5d8755062e974841a1b501de1caf9ca2.png)

Scroll down and select the `Cloud Provider` , `Region` and `Service Plan` based on your requirements.

In the end, enter a `Name` for the service:

Image: [ Create a service on Aiven ](https://hasura.io/docs/assets/images/create-service-aacff5b7ae5fce9ec40ef5b3f079c732.png)

Then click `Create service` .

Note

If you're using a database user other than the default one, make sure to give it the right[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#managed-pg-permissions).

## Step 4: Allow connections to your DB from Hasura​

On the `Services` dashboard, click on your DB:

Image: [ Select DB on Aiven ](https://hasura.io/docs/assets/images/select-db-fb29bf6ea91dd428b3572ce8196d528f.png)

Scroll down to `Allowed IP Addresses` and click on `Change` :

Image: [ Change allowed IP addresses on Aiven ](data:image/png;base64,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)

If you're using Hasura Cloud, you can quickly find your IP address from the `Hasura Cloud IP` field on the project's
details view:

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/hasura-cloud-ip-86181dcc16cbac471b8a2c5237a23b24.png)

Note

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

Add the Hasura IP address that you copied, click on the `+` :

Image: [ Add the Hasura IP on Aiven ](https://hasura.io/docs/assets/images/add-hasura-ip-2df45bfd90ad57608c9e49fbaba0df40.png)

Then click on `Save changes` .

## Step 5: Get the database connection URL​

The structure of the database connection URL looks as follows:

`postgresql:// < user-name > : < password > @ < public-ip > : < postgres-port > / < db > ?sslmode = require`

To get it, navigate to the `Overview` tab of your database dashboard and copy the `Service URI` :

Image: [ Copy the service URI on Aiven ](https://hasura.io/docs/assets/images/copy-service-uri-ef7f3141644d01e0777af57d584e9fee.png)

## Step 6: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in[ step 5 ](https://hasura.io/docs/latest/databases/postgres/aiven/#get-db-url-aiven):

Image: [ Database setup ](https://hasura.io/docs/assets/images/Aiven-complete-ab6b056cf00c3a3d21f0ad6234f39da3.png)

Then click `Connect Database` .

Note

For security reasons, it is recommended to set database URLs as[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)and
using the env vars to connect to the databases in place of the raw database URLs.

Voilà. You are ready to start developing.

Image: [ Hasura Console ](https://hasura.io/docs/assets/images/hasura-console-5685707ef939a6ca7cc2c5fb6ed7dda8.png)

## Next steps​

- You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.
- If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).


You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.

If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).

Image: [ Project actions ](https://hasura.io/docs/assets/images/project-manage-5b37a214a39b39b6287136606da021c4.png)

Note

For more information on which Postgres features we support, check out[ this page ](https://hasura.io/docs/latest/databases/feature-support/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/aiven/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/aiven/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/aiven/#create-hasura-project-aiven)
- [ Step 3: Create a Postgres DB on Aiven ](https://hasura.io/docs/latest/databases/postgres/aiven/#create-pg-db-aiven)
- [ Step 4: Allow connections to your DB from Hasura ](https://hasura.io/docs/latest/databases/postgres/aiven/#connect-hasura-aiven)
- [ Step 5: Get the database connection URL ](https://hasura.io/docs/latest/databases/postgres/aiven/#get-db-url-aiven)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/aiven/#step-6-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/aiven/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)