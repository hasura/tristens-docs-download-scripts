# Connecting Hasura to a Google Cloud SQL for SQL Server Database

## Introduction​

This guide explains how to connect a new or existing[ Google Cloud SQL for SQL Server database ](https://cloud.google.com/sql)to a Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions.

Hasura Cloud vs self-hosting

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#create-pg-db-gcp).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is successfully initialized, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for an
ODBC URL. We'll grab this after creating our database and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-002ccaffc2e89e74c45f00d91aa28374.png)

## Step 3: Create a SQL Server DB on Google Cloud SQL​

Existing database

If you have an existing SQL Server database on GCP, you can skip this step and move on to[ step 4 ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#allow-connections).

Log into the[ GCP console ](https://console.cloud.google.com/).

On the left-side navigation, scroll down to `Storage` and click on `SQL` :

Image: [ Navigate to SQL in GCP ](https://hasura.io/docs/assets/images/navigate-to-sql-b51fa2f423b5367b08f746c5fc8626a7.png)

On the top, click on `Create instance` :

Image: [ Create database instance in GCP ](https://hasura.io/docs/assets/images/create-instance-eccce009582ef540ea272255dcb01c2c.png)

Select SQL Server:

Image: [ Select SQL Server database instance in GCP ](https://hasura.io/docs/assets/images/select-sql-server-a048c863533ee6c639c2c4b42dd10884.png)

Choose an instance ID, as well as a default user password. If required, choose a specific region and zone.

Image: [ Configure database instance in GCP ](https://hasura.io/docs/assets/images/configure-instance-sql-server-4601c1bfef174fe39bde3c821e61b2e4.png)

Then click `Create` .

## Step 4: Allow connections to your DB from Hasura​

We need to allowlist the IP on which Hasura is running to be able to communicate with the database.

On the dashboard of your Google Cloud SQL database instance, on the left sidebar, click on `Connections` and then the `Networking` tab. Then, scroll down ot the checkbox `Public IP` , and click `Add a network` :

Image: [ Navigate to connections in GCP ](https://hasura.io/docs/assets/images/connections-09ef69c331b0459d0c96a8299564f5eb.png)

If using Hasura Cloud, from your project's dashboard, copy the Hasura Cloud IP address:

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/hasura-cloud-ip-86181dcc16cbac471b8a2c5237a23b24.png)

Self-hosted IP addresses

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

Enter the Hasura IP address that you copied along with a name (e.g., `Hasura` ):

Image: [ Add a new network in GCP ](https://hasura.io/docs/assets/images/add-network-c390647b8721c8624cfd579f75c7babc.png)

Then click `Done` and `Save` .

## Step 5: Construct the database connection URL​

The structure of the database connection URL is as follows:

`Driver={ODBC Driver 17 for SQL Server};Server=<server>;Database=<db-name>;UID=<username>;PWD=<password>`

- `username` : Google Cloud SQL defaults your `sa` username to `sqlserver` . If you have a separate database user, use
their username. Otherwise, use `sqlserver` .
- `password` : If you have a separate database user, use their password. Otherwise, use the password that you chose when
creating the database.
- `server` : The public IP can be obtained by clicking on `Overview` on the left-side navigation and then scrolling down
to `Connect to this instance` :


Image: [ Find the public IP for a Google Cloud SQL MS SQL Server database ](https://hasura.io/docs/assets/images/public-ip-ms-sql-6e1b6b4fb6241e71db2dcb7778be5774.png)

## Step 6: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in[ step 5 ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#construct-db-url-gcp):

Image: [ Database setup ](https://hasura.io/docs/assets/images/ms-sql-complete-c9e97d3618003a0b41374eca946f51ad.png)

Then click `Connect Database` .

Secrets in env vars

For security reasons, it is recommended to set database URLs as[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)use
those to connect to the databases in place of the raw database URLs. This prevents connections strings leaking in plain
text via metadata in version control.

Voilà. You are ready to start developing.

Image: [ Hasura Console ](https://hasura.io/docs/assets/images/hasura-console-5685707ef939a6ca7cc2c5fb6ed7dda8.png)

## Next steps​

- You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.
- If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).


You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.

If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).

Image: [ Project actions ](https://hasura.io/docs/assets/images/project-manage-5b37a214a39b39b6287136606da021c4.png)

MySQL feature support

For more information on which MySQL features we support, check out[ this page ](https://hasura.io/docs/latest/databases/mysql/index/#feature-support).

### Auth Proxy​

Google Cloud SQL offers a[ Cloud SQL Auth proxy ](https://cloud.google.com/sql/docs/sqlserver/sql-proxy)that can be used
to connect to your database. This is useful if you want to connect to your database from a local machine or a server
that doesn't have a public IP address.

To use the Cloud SQL Auth proxy, follow the instructions in the[ Cloud SQL Auth proxy docs ](https://cloud.google.com/sql/docs/sqlserver/sql-proxy#install).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#create-hasura-project-gcp)
- [ Step 3: Create a SQL Server DB on Google Cloud SQL ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#create-ms-sql-db-gcp)
- [ Step 4: Allow connections to your DB from Hasura ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#allow-connections)
- [ Step 5: Construct the database connection URL ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#construct-db-url-gcp)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#step-6-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#next-steps)
    - [ Auth Proxy ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/#auth-proxy)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)