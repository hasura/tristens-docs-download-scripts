# Connecting Hasura to a Google Cloud SQL for MySQL Database

## Introduction​

This guide explains how to connect a new or existing[ Google Cloud SQL for MySQL database ](https://cloud.google.com/sql)to a Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions.

Hasura Cloud or self-hosted steps

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/mysql/gcp/#create-pg-db-gcp).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
JDBC URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-5c65131e5694b42ca900190bda80f4ab.png)

## Step 3: Create a MySQL DB on Google Cloud SQL​

Already have an existing database?

If you have an existing MySQL database on Google Cloud SQL, you can skip this step and move on to[ step 4 ](https://hasura.io/docs/latest/databases/mysql/gcp/#allow-connections).

Log into the[ GCP console ](https://console.cloud.google.com/).

On the left-side navigation, scroll down to `Storage` and click on `SQL` :

Image: [ Navigate to SQL in GCP ](https://hasura.io/docs/assets/images/navigate-to-sql-b51fa2f423b5367b08f746c5fc8626a7.png)

On the top, click on `Create instance` :

Image: [ Create database instance in GCP ](https://hasura.io/docs/assets/images/create-instance-eccce009582ef540ea272255dcb01c2c.png)

Select MySQL:

Image: [ Select MySQL database instance in GCP ](https://hasura.io/docs/assets/images/select-MySQL-197bc885e3daf7c84447e7d35bbc17b5.png)

Select an instance ID, as well as a default user password. Choose a preset, and, if required, a specific region and
zone.

Image: [ Configure database instance in GCP ](https://hasura.io/docs/assets/images/configure-instance-2615e2a0e3d5ccbb37fa2d5fc961ce5a.png)

Then click `Create Instance` .

## Step 4: Allow connections to your DB from Hasura​

On the dashboard of your Google Cloud SQL database instance, on the left sidebar, click on `Connections` and then the `Networking` tab. Then scroll down to the checkbox `Public IP` , and click `Add a network` :

Image: [ Navigate to connections in GCP ](https://hasura.io/docs/assets/images/connections-3546b4cedbdc74ed78bc4d97ebbfaaab.png)

If using Hasura Cloud, from your project's dashboard, copy the Hasura Cloud IP address:

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/hasura-cloud-ip-86181dcc16cbac471b8a2c5237a23b24.png)

Note

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

Enter the Hasura IP address that you copied along with a name (e.g., `Hasura` ):

Image: [ Add a new network in GCP ](https://hasura.io/docs/assets/images/add-network-c390647b8721c8624cfd579f75c7babc.png)

Then click `Done` and `Save` .

## Step 5: Construct the database connection URL​

The structure of the database connection URL looks as follows:

`jdbc:mysql://<hostname>:<port>/<database_name>?user=<username>&password=<password>`

- `port` : The default port for MySQL is `3306` if not specified otherwise.
- `database_name` : The name is `mysql` by default unless otherwise specified.
- `username` : If you have a separate database user, the username will be theirs. If you didn't specify a user, the
default username is `root` .
- `password` : If you have a separate database user, use their password. Otherwise, use the password that you chose when
creating the database.
- `hostname` : The public IP can be obtained by clicking on `Overview` on the left-side navigation and then scrolling
down to `Connect to this instance` :


Image: [ Find the public IP for a GCP MySQL database ](https://hasura.io/docs/assets/images/public-ip-e92ab2ab6515a7af23dc40f935a490b5.png)

About Cloud SQL connections

If you're having trouble creating your connection string, check out[ Google Cloud SQL's docs ](https://cloud.google.com/sql/docs/mysql/connect-overview?_ga=2.46986085.-395235927.1674823952#external-connection-methods).

## Step 6: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we created in[ step 5 ](https://hasura.io/docs/latest/databases/mysql/gcp/#construct-db-url-gcp):

Image: [ Database setup ](https://hasura.io/docs/assets/images/gcp-complete-4d0b6c63324ff2657a94a33e797382a6.png)

Then click `Connect Database` .

Database URL security

It is recommended to set database connection URLs as[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)in Hasura Engine
instead of raw database URLs which would be saved to metadata and likely committed to a repository which may be a
security risk.

Ensure your password escapes special characters

Due to the potential variations in drivers, it's crucial to escape special characters used in the password of the
connection string. These include `{ } % & #` . To escape a character, use the appropriate escape sequence based on your
database's driver's documentation.

Track the tables on which you want to create your API, and voilà: you're ready to start developing.

Image: [ Hasura Console ](https://hasura.io/docs/assets/images/hasura-console-2a47467c355f156fbf952f58fe76df7b.png)

## Next steps​

- You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.
- If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).


You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.

If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).

Image: [ Project actions ](https://hasura.io/docs/assets/images/project-manage-5b37a214a39b39b6287136606da021c4.png)

MySQL feature support

For more information on which MySQL features we support, check out[ this page ](https://hasura.io/docs/latest/databases/mysql/index/#feature-support).

### Auth Proxy​

Google Cloud SQL offers a[ Cloud SQL Auth proxy ](https://cloud.google.com/sql/docs/mysql/sql-proxy)that can be used to
connect to your database. This is useful if you want to connect to your database from a local machine or a server that
doesn't have a public IP address.

To use the Cloud SQL Auth proxy, follow the instructions in the[ Cloud SQL Auth proxy docs ](https://cloud.google.com/sql/docs/mysql/sql-proxy#install).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/mysql/gcp/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/mysql/gcp/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/mysql/gcp/#create-hasura-project-gcp)
- [ Step 3: Create a MySQL DB on Google Cloud SQL ](https://hasura.io/docs/latest/databases/mysql/gcp/#create-mysql-db-gcp)
- [ Step 4: Allow connections to your DB from Hasura ](https://hasura.io/docs/latest/databases/mysql/gcp/#allow-connections)
- [ Step 5: Construct the database connection URL ](https://hasura.io/docs/latest/databases/mysql/gcp/#construct-db-url-gcp)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/mysql/gcp/#step-6-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/mysql/gcp/#next-steps)
    - [ Auth Proxy ](https://hasura.io/docs/latest/databases/mysql/gcp/#auth-proxy)


Image: [ hasura-webinar ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683628053/main-web/Group_11457_vceb9f.png)

### Ship faster with low-code APIs on MySQL, MariaDB, and Oracle

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)