# Connecting Hasura to a Timescale Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ Timescale Postgres ](https://www.timescale.com/)database to a
Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring Timescale Postgres and are
interested in migrating an existing Postgres database - such as from Heroku - check out their[ docs ](https://docs.timescale.com/timescaledb/latest/how-to-guides/migrate-data/)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/timescale-cloud/#create-pg-db-timescale).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

You will get prompted for a Postgres Database URL. We will create this in the next step and then come back here.

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to `Data -> Manage -> Connect Database -> Connect existing database` :

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Postgres DB on Timescale Cloud​

Log into the[ Timescale Cloud portal ](https://portal.timescale.cloud/login).

On the Timescale dashboard, under `Services` , click on `+ Create new service` :

Image: [ Create a new service on Timescale ](https://hasura.io/docs/assets/images/create-new-service-27c215f4fcc74ae50a86b49e4326eef1.png)

Select the Postgres option:

Image: [ Select Postgres on Timescale ](https://hasura.io/docs/assets/images/select-postgres-d6efb12083f72feed594c2a70110d5da.png)

Scroll down and select the `Cloud Provider` , `Region` and `Service Plan` based on your requirements.

In the end, enter a `Name` for the service:

Image: [ Create a service on Timescale ](https://hasura.io/docs/assets/images/create-service-13dd1c09096f23eb5114c3ac2f346ed8.png)

Then click `Create service` .

Note

If you're using a database user other than the default one, make sure to give it the right[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#managed-pg-permissions).

## Step 4: Allow connections to your DB from Hasura​

On the `Services` dashboard, click on your DB:

Image: [ Select DB on Timescale ](https://hasura.io/docs/assets/images/select-db-929e2cb6aa824d74181834256505eab3.png)

Scroll down to `Allowed IP Addresses` and click on `Change` :

Image: [ Change allowed IP addresses on Timescale ](data:image/png;base64,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)

If using Hasura Cloud, from your project's dashboard, copy the Hasura Cloud IP address:

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/hasura-cloud-ip-86181dcc16cbac471b8a2c5237a23b24.png)

Note

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

Add the Hasura IP address that you copied, click on the `+` and then click on `Save changes` :

Image: [ Add the Hasura IP on Timescale ](https://hasura.io/docs/assets/images/add-hasura-ip-7f7be82dd4ec2b43d3942398ec130d98.png)

## Step 5: Get the database connection URL​

The structure of the database connection URL looks as follows:

`postgresql:// < user-name > : < password > @ < public-ip > : < postgres-port > / < db > ?sslmode = require`

To get it, navigate to the `Overview` tab of your database dashboard and copy the `Service URI` :

Image: [ Copy the service URI on Timescale ](https://hasura.io/docs/assets/images/copy-service-uri-801761684f9c519bcd382aadb3a6eb85.png)

## Step 6: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in[ step 5 ](https://hasura.io/docs/latest/databases/postgres/timescale-cloud/#get-db-url-timescale):

Image: [ Database setup ](https://hasura.io/docs/assets/images/TS-complete-31b8432a6afa643b8d524da59c760cb1.png)

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

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/timescale-cloud/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/timescale-cloud/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/timescale-cloud/#create-hasura-project-timescale)
- [ Step 3: Create a Postgres DB on Timescale Cloud ](https://hasura.io/docs/latest/databases/postgres/timescale-cloud/#create-pg-db-timescale)
- [ Step 4: Allow connections to your DB from Hasura ](https://hasura.io/docs/latest/databases/postgres/timescale-cloud/#step-4-allow-connections-to-your-db-from-hasura)
- [ Step 5: Get the database connection URL ](https://hasura.io/docs/latest/databases/postgres/timescale-cloud/#get-db-url-timescale)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/timescale-cloud/#step-6-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/timescale-cloud/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)