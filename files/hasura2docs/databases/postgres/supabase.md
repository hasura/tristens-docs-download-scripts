# Connecting Hasura to a Supabase Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ Supabase Postgres database ](https://supabase.com/database)to a
Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring Supabase Postgres and are
interested in migrating an existing Postgres database - such as from Heroku - check out their[ docs ](https://supabase.com/docs/guides/migrations/heroku)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/supabase/#create-pg-db-supabase).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
Postgres Database URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Postgres DB on Supabase​

Log into[ Supabase ](https://app.supabase.com/)using your GitHub login.

From your dashboard, click `New project` :

Image: [ Create a new project with Supabase ](https://hasura.io/docs/assets/images/supabase-create-new-project-a3bc49f9ae9906b46e0163c36ce33525.png)

If you don't already have an organization within Supabase, you'll need to create a one. Click `New organization` :

Image: [ Create a new organization with Supabase ](https://hasura.io/docs/assets/images/supabase-create-new-organization-beb95804c0c1d7061ffc84adc343dfd7.png)

Fill in a name and click `Create organization` :

Image: [ Name your organization with Supabase ](https://hasura.io/docs/assets/images/supabase-new-organization-name-82e5d33bd5c4e653aa2762cd2bb7216b.png)

After creating your organization, you'll be presented with the `Create a new project` view. Fill in the necessary
information and click `Create new project` :

Image: [ Confirm project creation ](https://hasura.io/docs/assets/images/supabase-create-new-project-confirm-bcc16910c5f710b2d930b2eeab3f5eff.png)

You'll be redirected to your project's dashboard. After a few minutes, your database should be provisioned. You'll know
you're ready once your dashboard changes from this:

Image: [ Dashboard as project is being provisioned ](https://hasura.io/docs/assets/images/supabase-dashboard-provisioning-d0b551627f0f545ac3cc60aba7d34819.png)

To this:

Image: [ Dashboard view after provisioning is complete ](https://hasura.io/docs/assets/images/supabase-dashboard-ready-0e3640b089632432ff5e207289c8b636.png)

Congratulations! You've now created a Postgres instance on Supabase which you can use with Hasura GraphQL Engine. Follow
the steps below to connect it to Hasura.

## Step 4: Get the database connection URL​

The structure of the database connection URL looks as follows:

`postgresql:// < user-name > : < password > @ < host-server > : < port > / < database-name >`

From your database's dashboard, click the `Settings` icon on the side navigation:

Image: [ From dashboard, choose settings on the left-hand side ](https://hasura.io/docs/assets/images/supabase-dashboard-settings-87c18012035c575b0aced34b32269444.png)

Choose `Database` :

Image: [ Database information within the settings view ](https://hasura.io/docs/assets/images/supabase-database-view-060e6e9181e38cf0efba3322c76c189e.png)

Then scroll down to find the `Connection string` section. Select the `URI` option and copy the string:

Image: [ Grab the PG db connection string ](https://hasura.io/docs/assets/images/supabase-copy-uri-68c8aebca6a81e1f5c6861e4e684baf4.png)

Note

You'll need to replace `[YOUR-PASSWORD]` with your project's password.

## Step 5: Finish connecting the database​

Back on the Hasura Console, enter the database URI that we retrieved in the previous step:

Image: [ Connect the database on Hasura Console ](https://hasura.io/docs/assets/images/supabase-connected-db-90248365c283b3063e895d67b191cc05.png)

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

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/supabase/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/supabase/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/supabase/#create-hasura-project)
- [ Step 3: Create a Postgres DB on Supabase ](https://hasura.io/docs/latest/databases/postgres/supabase/#create-pg-db-supabase)
- [ Step 4: Get the database connection URL ](https://hasura.io/docs/latest/databases/postgres/supabase/#get-db-url)
- [ Step 5: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/supabase/#step-5-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/supabase/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)