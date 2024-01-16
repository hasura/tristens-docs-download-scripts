# Getting Started with MariaDB in Hasura Cloud

## Introduction​

This guide will help you get set up with[ Hasura Cloud ](https://hasura.io/docs/latest/hasura-cloud/overview/)and our MariaDB integration. This is
the easiest way to set up Hasura Engine and the MariaDB GraphQL Data Connector.

Supported versions:

1. Hasura GraphQL Engine `v2.24.0` onwards
2. Hasura supports most databases with standard implementations of **MariaDB 10.5 and higher** including: Amazon RDS,
Amazon Aurora, Digital Ocean and SkySQL.


Supported features

Hasura currently supports queries, mutations (INSERT, UPDATE, DELETE), table relationships, remote relationships and
permissions on MariaDB.

Note that Hasura doesn't yet support the ability to modify the database schema for MariaDB, so the database you connect
to should already contain tables and data. You should also ideally have access to it outside of Hasura to modify the
schema.

## Try it out​

### Step 1: Create an account on Hasura Cloud and create a new Hasura Project​

Navigate to[ cloud.hasura.io ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-cloud-hasura-io&tech=default&skip_onboarding=true),
and create a new Hasura Cloud account.

Once you create a project on Hasura Cloud, hit the "Launch Console" button to open the Hasura Console for your project.

Image: [ Connect new or existing database ](https://hasura.io/docs/assets/images/create-project-8451135f7ff89b8f6e8fb3d29fd01ade.png)

### Step 2: Connect to a MariaDB database​

From the Console, click the `Data` tab:

Image: [ Connect database ](https://hasura.io/docs/assets/images/connect-db-console-d08a940e3d5f1f710ba1c83383920b77.png)

Select the MariaDB data source driver. Enter a database display name and the JDBC Connection URL for your MariaDB
instance.

The JDBC connection URL should look like this:

`jdbc : mariadb : //<hostname > : <port > /<database name > ? user=<username > &password=<password>`

For example:

```
jdbc : mariadb : //myhost.mycompany.com/mariadbtest ? user=abc &password=pqr    # assuming the default port 3306
jdbc : mariadb : //localhost : 4533/mariadbtest ? user=abc &password=pqr          # assuming MariaDB is running on port 4533
```

For more information see[ MariaDB Connection URL syntax ](https://mariadb.com/kb/en/about-mariadb-connector-j/#using-the-driver).

Click `Connect Database` .

Ensure your password escapes special characters

Due to the potential variations in drivers, it's crucial to escape special characters used in the password of the
connection string. These include `{ } % & #` . To escape a character, use the appropriate escape sequence based on your
database's driver's documentation.

### Step 3: Track tables and run GraphQL API queries​

Now that you have successfully connected your MariaDB database to Hasura, you can track tables and use Hasura to
automatically build a GraphQL API on top of it.

## Keep up to date​

If you'd like to stay informed about the status of MariaDB support, subscribe to our newsletter and join our discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/mariadb/cloud/#introduction)
- [ Try it out ](https://hasura.io/docs/latest/databases/mariadb/cloud/#try-it-out)
    - [ Step 1: Create an account on Hasura Cloud and create a new Hasura Project ](https://hasura.io/docs/latest/databases/mariadb/cloud/#step-1-create-an-account-on-hasura-cloud-and-create-a-new-hasura-project)

- [ Step 2: Connect to a MariaDB database ](https://hasura.io/docs/latest/databases/mariadb/cloud/#step-2-connect-to-a-mariadb-database)

- [ Step 3: Track tables and run GraphQL API queries ](https://hasura.io/docs/latest/databases/mariadb/cloud/#step-3-track-tables-and-run-graphql-api-queries)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/mariadb/cloud/#keep-up-to-date)


Image: [ hasura-webinar ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683628053/main-web/Group_11457_vceb9f.png)

### Ship faster with low-code APIs on MySQL, MariaDB, and Oracle

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)