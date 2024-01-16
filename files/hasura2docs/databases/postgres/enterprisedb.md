# Connecting Hasura to an EnterpriseDB (BigAnimal) Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ EnterpriseDB ](https://www.enterprisedb.com/products/biganimal-cloud-postgresql)(BigAnimal) Postgres database to a
Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/). If you're exploring EnterpriseDB Postgres and are interested in
migrating an existing Postgres database - such as from Heroku - check out their[ docs ](https://www.enterprisedb.com/docs/biganimal/latest/migration/cold_migration/)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/enterprisedb/#create-pg-db-enterprisedb).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
Postgres Database URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a BigAnimal Postgres DB on EnterpriseDB​

Log into[ EnterpriseDB ](https://www.enterprisedb.com/dashboard)and head to your dashboard.

From your dashboard, scroll down and click `Test drive for free` in the BigAnimal section:

Image: [ Test drive BigAnimal ](https://hasura.io/docs/assets/images/big-animal-test-drive-fa33a517479333d96217e63aafe392c5.png)

EnterpriseDB will create a free trial and redirect you to your BigAnimal portal. From this portal, click `Create New Cluster` :

Image: [ Create new cluster ](https://hasura.io/docs/assets/images/big-animal-create-new-cluster-e61c37b85f883aa698d7f0e7337396b8.png)

Select the type of cluster and provider you plan to use, then click `Next: Cluster Settings` :

Image: [ Choose type and provider ](https://hasura.io/docs/assets/images/big-animal-cluster-type-provider-7ab1d0ad8d148e3bc6d3f95251b96802.png)

Enter a cluster name and password:

Image: [ Add name and password ](https://hasura.io/docs/assets/images/big-animal-cluster-name-password-9dae4f4e3e0010b69b8c26d3674125a8.png)

Choose a database type, region, and instance type:

Image: [ Choose cluster type and region ](https://hasura.io/docs/assets/images/big-animal-cluster-type-region-36309026756fdff49073d4e8f36c6711.png)

Select your storage and networking requirements, then click `Create Cluster` :

Image: [ Choose storage and networking ](https://hasura.io/docs/assets/images/big-animal-storage-networking-6924b68e64580ebec82f58b01342dc16.png)

You'll be redirected to your BigAnimal portal and should see your cluster provisioning like this:

Image: [ Cluster provisioning ](https://hasura.io/docs/assets/images/big-animal-provisioning-70da75115faab2b953aa0d919ebe4513.png)

Congratulations! You've now created a BigAnimal Postgres instance on EnterpriseDB which you can use with Hasura GraphQL
Engine. Follow the steps below to connect it to Hasura.

## Step 4: Get the database connection parameters and finish connecting the database​

The structure of the database connection URL looks as follows:

`postgresql:// < user-name > : < password > @ < host-server > : < port > / < database-name >`

BigAnimal doesn't provide an out-of-the-box connection string matching the format above. Instead, we'll use the
parameters from the `Connect` tab and pass them to Hasura.

After BigAnimal has provisioned the cluster, click on the title:

Image: [ Cluster ready ](https://hasura.io/docs/assets/images/big-animal-cluster-ready-fb016e762fd7a601c9ddb2613af95a02.png)

From the cluster's dashboard, choose the `Connect` tab:

Image: [ Cluster connection parameters ](https://hasura.io/docs/assets/images/big-animal-connection-parameters-b371f85effbfef691f405794f1b0616e.png)

For each of the following under `Connection Info` , click `Copy` and paste their values into the appropriate fields on
the Hasura Console:

| BigAnimal parameter | Hasura parameter |
|---|---|
| Dbname | Database Name |
| Read/Write Host | Host |
| Port | Port |
| User | Username |


Back on the Hasura Console, paste your values into the mapped field:

Image: [ Connect to Hasura Console ](https://hasura.io/docs/assets/images/big-animal-connect-db-cd6f785b804a07e2a5746cc2662b143f.png)

Note

BigAnimal doesn't present your password on the `Connect` tab. You'll need to provide the password you used to create the
cluster in Hasura's `Password` field.

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

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/enterprisedb/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/enterprisedb/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/enterprisedb/#create-hasura-project)
- [ Step 3: Create a BigAnimal Postgres DB on EnterpriseDB ](https://hasura.io/docs/latest/databases/postgres/enterprisedb/#create-pg-db-enterprisedb)
- [ Step 4: Get the database connection parameters and finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/enterprisedb/#get-db-url)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/enterprisedb/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)