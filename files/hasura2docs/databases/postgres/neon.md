# Connecting Hasura to a Neon Serverless Postgres Database

## Introduction​

This guide explains how to connect a new[ Neon ](https://neon.tech/)serverless Postgres database to a[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)instance.

## Creating a New Neon Database​

### Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

### Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to `Data -> Manage -> Connect Database -> Create New Database` :

Click on `Connect Neon Database` to create and connect a new Postgres database to your Hasura Project.

Image: [ Connect Neon database ](https://hasura.io/docs/assets/images/connect_neon_database-20d34cdbe67ad3bdd7dab65e2f0b19cb.png)

On the next step, you'll be prompted to Login/Sign up for Neon. We recommend `Continue with Hasura` for a seamless
experience.

Image: [ Neon Authentication ](https://hasura.io/docs/assets/images/neon_authentication-ea9e3addb3019efe4f3a7d0d9d54d396.png)

After successful authorization, a new Neon Postgres database will be created and connected to your Hasura Project with
the connection string associated with the environment variable `PG_DATABASE_URL` .

### Step 3 (optional): Load a template​

Once the database is successfully connected, you can explore Hasura's GraphQL API by loading any of the templates from
the template gallery instantly.

For example: to get started, you could try the `Welcome to Hasura` template:

Image: [ Hello World Template ](https://hasura.io/docs/assets/images/hasura_hello_world_template-7f2a4140a577886d76e3c550c7b8cf6b.png)

This installs a schema with data that you can now query using your Hasura GraphQL API from the `API` tab.

Voilà! You are ready to start developing.

Image: [ Hasura Console ](https://hasura.io/docs/assets/images/hasura-console-5685707ef939a6ca7cc2c5fb6ed7dda8.png)

Note

You can visit the Neon console from the `Data` tab to manage your created database.

Image: [ Neon Console Link ](https://hasura.io/docs/assets/images/neon_console_link_page-3b054ef2da6469db0eb4577ab97c1822.png)

## Migrating an existing database to Neon​

If you want to migrate your existing database to Neon, you must use Postgres's `pg_dump` utility to copy over your
database.

`pg_dump -h  < host >  -U  < username >   < dbname >   |  psql  < neon-connection-string >`

For more info, follow[ Neon's detailed guide for importing a database ](https://neon.tech/docs/how-to-guides/import-an-existing-database/).

Note

If you're migrating from Heroku, check out Neon's platform-specific[ migration guide ](https://neon.tech/docs/how-to-guides/hasura-heroku-migration/).

## Neon Free Tier​

With Neon's Free Tier, you can create one free project with the following limits:

- 10[ branches ](https://neon.tech/branching/)
- 3 GB of storage per branch
- Up to 3 compute endpoints with 1 vCPU and 4 GBs of RAM
- A point-in-time restore window of 7 days of reasonable usage


For more info, check out Neon's[ Technical Preview Free Tier ](https://neon.tech/docs/reference/technical-preview-free-tier/).

Note

If you've already reached the Neon free-tier project limit, please head to your[ Neon console ](https://console.neon.tech/)and delete an unused project to be able to create and connect a new one from
the Hasura Console.

Image: [ Neon Free Tier Warning ](https://hasura.io/docs/assets/images/free_tier_exceeded_neon-902d76e60770c630d68c5dcf172ceb5c.png)

Note

For more information on which Postgres features we support, check out[ this page ](https://hasura.io/docs/latest/databases/feature-support/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/neon/#introduction)
- [ Creating a New Neon Database ](https://hasura.io/docs/latest/databases/postgres/neon/#creating-a-new-neon-database)
    - [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/neon/#step-1-sign-up-or-log-in-to-hasura-cloud)

- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/neon/#step-2-create-a-hasura-cloud-project)

- [ Step 3 (optional): Load a template ](https://hasura.io/docs/latest/databases/postgres/neon/#step-3-optional-load-a-template)
- [ Migrating an existing database to Neon ](https://hasura.io/docs/latest/databases/postgres/neon/#migrating-an-existing-database-to-neon)
- [ Neon Free Tier ](https://hasura.io/docs/latest/databases/postgres/neon/#neon-free-tier)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)