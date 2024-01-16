# Connecting Hasura to an Aiven MySQL Database

## Introduction​

This guide explains how to connect a new or existing[ Aiven MySQL ](https://aiven.io/mysql?utm_source=website&utm_medium=referral&utm_campaign=hasura)database to a Hasura
instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/mysql/aiven/#create-mysql-db-aiven).

Supported From

Aiven-hosted MySQL databases are supported from Hasura `v2.35.0` onwards.

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Choose the MySQL driver and
then click `Connect Existing Database` :

Image: [ Choose MySQL driver ](https://hasura.io/docs/assets/images/aiven-mysql-choose-driver-a26509d6e67206707d6bf9a9fcf3b565.png)

We'll provision the database on Aiven in the next step and then return to this page to complete the connection.

## Step 3: Create a MySQL DB on Aiven​

Note

If you have an existing Aiven MySQL database, you can skip this step and move on to[ step 4 ](https://hasura.io/docs/latest/databases/mysql/aiven/#connect-hasura-aiven).

Log into the[ Aiven console ](https://console.aiven.io/signup?utm_source=website&utm_medium=referral&utm_campaign=hasura).

On the Aiven console, click `+ Create a new service` and choose `MySQL` :

Image: [ Create MySQL instance on Aiven ](https://hasura.io/docs/assets/images/aiven-create-mysql-56b4a769ee14d404631ce46918c6aa6e.png)

Scroll down and select the `Cloud Provider` , `Region` and `Service Plan` based on your requirements. Then click `Create free service` :

Image: [ Configure MySQL service ](https://hasura.io/docs/assets/images/aiven-mysql-configuration-d8d6c1210d190a97d4168a0f8cabbb79.png)

## Step 4: Allow connections to your DB from Hasura​

On the `Services` dashboard, click on your DB and scroll down to `Allowed IP Addresses` and click on `Change` :

Image: [ Change allowed IP addresses on Aiven ](https://hasura.io/docs/assets/images/aiven-mysql-change-ip-0d0510e2171ed4f913b926d8efea548c.png)

If you're using Hasura Cloud, you can quickly find your IP address from the `Hasura Cloud IP` field on the project's
details view:

Image: [ Hasura Cloud IP ](https://hasura.io/docs/assets/images/aiven-mysql-hasura-cloud-ip-6874a2e3a0440e6c1a7642db2633209e.png)

Note

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

Add the Hasura IP address that you copied, click on the `+` :

Image: [ Hasura Cloud IP ](https://hasura.io/docs/assets/images/aiven-mysql-hasura-cloud-ip-set-0bd1226fbba08da7c41c13dcd3d7640a.png)

Then click on `Close` .

## Step 5: Get the database connection URL​

The MySQL connector utilizes JDBC connection strings to connect to the database. The format of the connection string is
as follows:

`jdbc:mysql:// < hostname > : < port > / < database name > ?user = < username >& password = < password >`

You'll have to transform the connection string provided by Aiven into the format above. Navigate to the `Overview` tab
of your database dashboard and use the `Service URI` to construct the connection string:

Image: [ Connection URI ](https://hasura.io/docs/assets/images/aiven-mysql-connection-uri-e19c0f64abea3c5a661a5da6aa975e95.png)

## Step 6: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in[ step 5 ](https://hasura.io/docs/latest/databases/mysql/aiven/#get-db-url-aiven):

Image: [ Finish connecting ](https://hasura.io/docs/assets/images/aiven-mysql-finish-connecting-2986c96b3d9b08497b45ffb8b9edaabb.png)

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

For more information on which MySQL features we support, check out[ this page ](https://hasura.io/docs/latest/databases/feature-support/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/mysql/aiven/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/mysql/aiven/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/mysql/aiven/#create-hasura-project-aiven)
- [ Step 3: Create a MySQL DB on Aiven ](https://hasura.io/docs/latest/databases/mysql/aiven/#create-mysql-db-aiven)
- [ Step 4: Allow connections to your DB from Hasura ](https://hasura.io/docs/latest/databases/mysql/aiven/#connect-hasura-aiven)
- [ Step 5: Get the database connection URL ](https://hasura.io/docs/latest/databases/mysql/aiven/#get-db-url-aiven)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/mysql/aiven/#step-6-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/mysql/aiven/#next-steps)


Image: [ hasura-webinar ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683628053/main-web/Group_11457_vceb9f.png)

### Ship faster with low-code APIs on MySQL, MariaDB, and Oracle

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)