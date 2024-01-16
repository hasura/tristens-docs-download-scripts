# MS SQL Server

## Introduction​

Hasura allows connecting to a SQL Server database and build a GraphQL API based on the database schema.

Supported versions:

1. Hasura GraphQL Engine `v2.0.0-alpha.2` onwards
2. SQL Server 2016 and upwards


## Get Started​

To try Hasura with SQL Server, you'll need your own new or existing SQL Server database.

Here are 2 ways you can get started with Hasura and SQL Server:

1. [ Hasura Cloud ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/cloud/): You'll need to be able to access your SQL Server
database from Hasura Cloud.
2. [ Docker ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/docker/): Run Hasura with Docker and then connect your SQL
Server database to Hasura.


## Supported features​

Hasura currently supports queries, subscriptions, mutations, relationships, permissions, and Event Triggers on MS SQL
Server.

## Managing data with the Hasura Console​

The Hasura Console is a web UI that allows you to manage your data and metadata. It is available at `http://localhost:8080/console` when you run Hasura locally, or from your project's Console endpoint when you use[ Hasura Cloud ](https://cloud.hasura.io).

The data-management features (such as creating tables) are available in the `Data` tab. You can access your GraphQL API
in the `API` tab and interact with it using the GraphiQL interface.

Console support

We recommend using your preferred MS SQL Server client instead. The Hasura Console is designed to be a tool for managing
your GraphQL API, and not a full-fledged database management tool.

## Required permissions​

Assuming a `CONNECT` permission already exists, the following permissions are required for Hasura to function
completely. Note that missing permissions may cause the corresponding features to work incorrectly:

- To use the Hasura Console to alter your schema, you will need appropriate schema permissions, such as `CREATE TABLE` , `CREATE VIEW` , `CREATE FUNCTION` , and `CREATE PROCEDURE` , depending on what you want to do.
- To perform queries and mutations, Hasura will need permission to `DELETE` , `INSERT` , `SELECT` , and `UPDATE` .
- To call MSSQL stored procedures via Hasura, the `EXECUTE` permission is also required.


## Keep up to date​

If you'd like to stay informed about the status of SQL Server support, subscribe to our newsletter and join our discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


Additional Resources

This Hands-on Demo walks you through Getting Started with Hasura on SQL Server & common use cases. -[ View Recording here ](https://hasura.io/events/webinar/hasura-sql-server/?pg=docs&plcmt=body&cta=view-recording&tech=).

We also have a tutorial available on our Learn site -[ check out the Microsoft SQL Server tutorial ](https://hasura.io/learn/database/microsoft-sql-server/introduction/).

## Know more​

- [ Get Started ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/index/)
- [ Connect a Google Cloud SQL for MS SQL Server database ](https://hasura.io/docs/latest/databases/ms-sql-server/gcp/)
- [ Schema ](https://hasura.io/docs/latest/schema/ms-sql-server/index/)
- [ Queries ](https://hasura.io/docs/latest/queries/ms-sql-server/index/)
- [ Mutations ](https://hasura.io/docs/latest/mutations/ms-sql-server/index/)
- [ Subscriptions ](https://hasura.io/docs/latest/subscriptions/ms-sql-server/index/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/ms-sql-server/index/#introduction)
- [ Get Started ](https://hasura.io/docs/latest/databases/ms-sql-server/index/#get-started)
- [ Supported features ](https://hasura.io/docs/latest/databases/ms-sql-server/index/#supported-features)
- [ Managing data with the Hasura Console ](https://hasura.io/docs/latest/databases/ms-sql-server/index/#managing-data-with-the-hasura-console)
- [ Required permissions ](https://hasura.io/docs/latest/databases/ms-sql-server/index/#required-permissions)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/ms-sql-server/index/#keep-up-to-date)
- [ Know more ](https://hasura.io/docs/latest/databases/ms-sql-server/index/#know-more)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)