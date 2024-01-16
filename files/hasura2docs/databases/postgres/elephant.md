# Connecting Hasura to an ElephantSQL Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ ElephantSQL Postgres ](https://www.elephantsql.com/)database to a
Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/elephant/#create-pg-db-elephant).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
Postgres Database URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Postgres DB on ElephantSQL​

Log into[ ElephantSQL ](https://customer.elephantsql.com/login).

If this is your first time logging into ElephantSQL, you'll need to create a team. Complete the form and click `Create team` .

Image: [ Create Elephant team ](https://hasura.io/docs/assets/images/elephant-create-team-465483c8ab152eb4cc1378efef6c92b4.png)

From here, you'll need to create a new instance:

Image: [ Create new Elephant instance ](https://hasura.io/docs/assets/images/elephant-create-instance-1e98a85f4bb72aeaba3f3cff65299f81.png)

Choose a name, plan, and - if necessary - tags for this instance. Click `Select Region` when complete:

Image: [ Add details to Elephant instance ](https://hasura.io/docs/assets/images/elephant-instance-details-dcef7c79f98b78f429af37feae544626.png)

Choose a region and click `Review` :

Image: [ Choose region for Elephant instance ](https://hasura.io/docs/assets/images/elephant-select-region-d798e3e5b180937118ac95d6d70b2c3e.png)

Confirm your selections and click `Create instance` :

Image: [ Create Elephant instance ](https://hasura.io/docs/assets/images/elephant-confirm-instance-4f0dc9efa8015b1b62fddbae4f2221fa.png)

Congratulations! You've now created an ElephantSQL Postgres instance you can use with Hasura GraphQL Engine. Follow the
steps below to connect it to Hasura.

## Step 4: Get the database connection URL​

From your dashboard, click on the name of your instance:

Image: [ Choose Elephant instance ](https://hasura.io/docs/assets/images/elephant-choose-instance-7077a4cf3a673ca2bda4839144bf3516.png)

The structure of the database connection URL looks as follows:

`postgres:// < user-name > : < password > @ < host-server >`

From the `Details` view, copy the URL string to your clipboard:

Image: [ Get the connection string for the database ](https://hasura.io/docs/assets/images/elephant-connection-string-d5a72bec2da561ec55313825ff795ff7.png)

## Step 5: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in the previous step:

Image: [ Add the connection string to your Hasura Console ](https://hasura.io/docs/assets/images/elephant-connect-db-87960825228b2faf08b5129db0d18568.png)

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

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/elephant/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/elephant/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/elephant/#create-hasura-project-do)
- [ Step 3: Create a Postgres DB on ElephantSQL ](https://hasura.io/docs/latest/databases/postgres/elephant/#create-pg-db-elephant)
- [ Step 4: Get the database connection URL ](https://hasura.io/docs/latest/databases/postgres/elephant/#get-db-url)
- [ Step 5: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/elephant/#step-5-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/elephant/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)