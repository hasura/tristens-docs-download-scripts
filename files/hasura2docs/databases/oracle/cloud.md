# Getting Started with Oracle in Hasura Cloud

## Introduction​

This guide will help you get set up with[ Hasura Cloud ](https://hasura.io/docs/latest/hasura-cloud/overview/)and our Oracle integration.

Supported versions

1. Hasura GraphQL Engine `v2.24.0` onwards
2. Hasura supports most databases with standard implementations of **Oracle 18.0 and higher** including Amazon RDS.


Supported features

Hasura currently supports queries, mutations (INSERT, UPDATE, DELETE), table relationships, remote relationships and
permissions on Oracle.

Note that Hasura doesn't yet support the ability to modify the database schema for Oracle, so the database you connect
to should already contain tables and data. You should also ideally have access to it outside of Hasura to modify the
schema.

## Try it out​

### Step 1: Create an account on Hasura Cloud and create a new Hasura Project​

Navigate to[ cloud.hasura.io ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-cloud-hasura-io&tech=default&skip_onboarding=true),
and create a new Hasura Cloud account.

Once you create a project on Hasura Cloud, hit the "Launch Console" button to open the Hasura Console for your project.

Image: [ Connect new or existing database ](https://hasura.io/docs/assets/images/create-project-8451135f7ff89b8f6e8fb3d29fd01ade.png)

### Step 2: Connect to a Oracle database​

From the Console, click the `Data` tab:

Image: [ Connect database ](https://hasura.io/docs/assets/images/connect-db-console-d08a940e3d5f1f710ba1c83383920b77.png)

Select the Oracle data source driver.

Already have a data source connected?

You'll need to click `Manage` in the sidenav and then `Connect Database` to bring up the different available agents.

Enter a database display name and the JDBC Connection URL for your Oracle instance. The JDBC connection URL should look
like this:

`jdbc : oracle : thin : <username > /<password > @<hostname > : <port > : <service - name >`

For example:

```
jdbc : oracle : thin : myuser/mypassword@myhost.mycompany.com : oracletest   # assuming the default port 1521
jdbc : oracle : thin : myuser/mypassword@myhost.mycompany.com : 1234 : oracletest   # assuming Oracle is running on port 1234
```

Click `Connect Database` .

Ensure your password escapes special characters

Due to the potential variations in drivers, it's crucial to escape special characters used in the password of the
connection string. These include `{ } % & #` . To escape a character, use the appropriate escape sequence based on your
database's driver's documentation.

### Step 3: Track tables and run GraphQL API queries​

Now that you have successfully connected your Oracle database to Hasura, you can track tables and use Hasura to
automatically build a GraphQL API on top of it.

## Keep up to date​

If you'd like to stay informed about the status of Oracle support, subscribe to our newsletter and join our Discord!

- [ Join the newsletter list ](https://hasura.io/newsletter/)
- [ Join the Hasura Discord ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/oracle/cloud/#introduction)
- [ Try it out ](https://hasura.io/docs/latest/databases/oracle/cloud/#try-it-out)
    - [ Step 1: Create an account on Hasura Cloud and create a new Hasura Project ](https://hasura.io/docs/latest/databases/oracle/cloud/#step-1-create-an-account-on-hasura-cloud-and-create-a-new-hasura-project)

- [ Step 2: Connect to a Oracle database ](https://hasura.io/docs/latest/databases/oracle/cloud/#step-2-connect-to-a-oracle-database)

- [ Step 3: Track tables and run GraphQL API queries ](https://hasura.io/docs/latest/databases/oracle/cloud/#step-3-track-tables-and-run-graphql-api-queries)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/oracle/cloud/#keep-up-to-date)


Image: [ hasura-webinar ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683628053/main-web/Group_11457_vceb9f.png)

### Ship faster with low-code APIs on MySQL, MariaDB, and Oracle

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)