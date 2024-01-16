# Connecting Hasura to an MS SQL on Azure Database

## Introduction​

This guide explains how to connect a new or existing[ MS SQL database on Azure ](https://azure.microsoft.com/en-us/products/azure-sql/database/)to a Hasura instance, either
on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring MS SQL on Azure, and are
interested in migrating an existing MS SQL database, check out their[ docs ](https://learn.microsoft.com/en-us/azure/dms/tutorial-sql-server-to-azure-sql)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#create-pg-db-mssql).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to `Data -> Manage -> Connect Database -> Connect existing database` :

You will get prompted for a MS SQL Database URL. We will create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-mssql-setup-d37474a007bdd34406904b6df269acd8.png)

## Step 3: Create an MS SQL Instance on Azure​

Log into the[ Azure Console ](https://portal.azure.com/#home).

On the top, click on `Search` and type "SQL Server" into the search field. Then click on `SQL Servers` :

Image: [ Navigate to SQL Servers on Azure ](https://hasura.io/docs/assets/images/select-sql-server-step-1-cdfa31b786c96ded3402f57fc25ada5e.png)

Click on the `Create` button:

Image: [ Create database in Azure ](https://hasura.io/docs/assets/images/click-on-create-step-2-fb2fc70cf59c27c2b0053df569543b52.png)

Select the current `Subscription` (Billing Account) and the resource group. Fill in all the necessary fields. In the
Authentication part, select `Use SQL Authentication` and fill the username and password for the SQL user.

Image: [ Fill all required fields to create database ](https://hasura.io/docs/assets/images/fill-required-fields-step-3-d1dc66fe096302ccb829c92c07d6bb91.png)

Change additional settings or add tags to the instance if required. Once you reach to `Review + Create` tab, review all
the fields. You can go back and change any field if required. Then, click on `Create` to start deploying the server
instance.

Image: [ Review and create SQL Server instance ](https://hasura.io/docs/assets/images/review-and-create-step-4-964939d37236cdefa8ff285a46f657a4.png)

## Step 4: Allow connections to your DB from Hasura​

Once Azure provisions the server, navigate to the server instance page and click on `Show networking settings` .

Image: [ Go to networking settings ](https://hasura.io/docs/assets/images/server-created-go-to-network-f3d6d027defa297bc80a0bb0a3c090f6.png)

If using Hasura Cloud, from your project's dashboard, copy the Hasura Cloud IP address:

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/hasura-cloud-ip-86181dcc16cbac471b8a2c5237a23b24.png)

Note

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

On Azure, under `Firewall rules` in networking settings, click on `Add a firewall rule` . Name the firewall rule and
paste the Hasura instance's IP address on both the `Start IP` and `End IP` input boxes:

Image: [ Add IP to firewall ](https://hasura.io/docs/assets/images/add-ip-and-save-2d44f9240b266666f275a80468c52494.png)

After entering the IP of your Hasura instance, click on `OK` and then click on `Save` at end of the page for the changes
to take effect.

## Step 5: Create database​

Go to the SQL Server instance's home and click on `Create Database` 

Image: [ Create Database on SQL Server ](https://hasura.io/docs/assets/images/click-on-create-db-step-6-57b9b592f398b51093983f938855e2cb.png)

Fill in all the required fields and additional settings if required. Click on `Review + create` and create the database.

Image: [ Review and create database ](https://hasura.io/docs/assets/images/create-db-step-7-724452553d76f2e4de88777671f2c028.png)

## Step 6: Construct the database connection URL​

The structure of the database connection URL looks as follows:

`Driver={ODBC Driver 17 for SQL Server};Server=myServerAddress;Database=myDataBase;UID=myUsername;PWD=myPassword;`

We recommend copying and pasting this string into the Hasura Console's `Database URL` field (in the next step) to serve
as a template. Using the information below, you can modify the attributes to meet your databases's values.

Copy the server name from instance home.

Image: [ Copy server name ](https://hasura.io/docs/assets/images/copy-server-name-2ec2e70b8bf35b195c6dd44d544b2294.png)

- `Driver` : Driver to use for connection to the SQL Server. If you are not sure, use `ODBC Driver 17 for SQL Server` .
- `Server` : The server name copied from the instance page.
- `Database` : Database name created in[ step 5 ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#create-db-on-mssql-instance).
- `UID` : Username for the SQL User created in[ step 3 ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#create-mssql-server-instance).
- `PWD` : Password for the SQL User created in[ step 3 ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#create-mssql-server-instance).


## Step 6: Finish connecting the database​

Back on the Hasura Console, enter and modify the connection string that we referenced in[ step 6 ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#construct-db-url-mssql):

Image: [ Database setup ](https://hasura.io/docs/assets/images/connect-to-hasura-step-8-aaa01ef4acd25048ac963c14bd87cead.png)

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

For more information on which SQL Server features we support, check out[this page]/databases/supported-databases.mdx).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#create-hasura-project-mssql-azure)
- [ Step 3: Create an MS SQL Instance on Azure ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#create-pg-db-mssql)
- [ Step 4: Allow connections to your DB from Hasura ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#step-4-allow-connections-to-your-db-from-hasura)
- [ Step 5: Create database ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#create-db-on-mssql-instance)
- [ Step 6: Construct the database connection URL ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#construct-db-url-mssql)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#step-6-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/ms-sql-server/mssql/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)