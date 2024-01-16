# Oracle

## Introduction​

Hasura enables you to connect to Oracle databases to automatically build a GraphQL API based on your database schema.

At present, our Oracle integration is available in Hasura Cloud and Docker environments, where you can run Hasura
GraphQL Engine and connect the Oracle GraphQL Data Connector to it. For more information on GraphQL Data Connectors
check out[ our blog post on the topic ](https://hasura.io/blog/hasura-graphql-data-connectors/).

To get started with Oracle:

- In Hasura Cloud, check out our[ Getting Started with Oracle in Hasura Cloud ](https://hasura.io/docs/latest/databases/oracle/cloud/)guide
- In a Docker environment, check out our[ Getting Started with Docker ](https://hasura.io/docs/latest/databases/oracle/docker/)guide


Supported versions

1. Hasura GraphQL Engine `v2.24.0` onwards
2. Hasura supports most databases with standard implementations of **Oracle 18.0 and higher** including Amazon RDS.


Supported features

Hasura currently supports queries, mutations (INSERT, UPDATE, DELETE), table relationships, remote relationships and
permissions on Oracle.

Note that Hasura doesn't yet support the ability to modify the database schema for Oracle, so the database you connect
to should already contain tables and data. You should also ideally have access to it outside of Hasura to modify the
schema.

## Feature Support​

### Queries​

### Mutations​

### Subscriptions​

### Event Triggers​

## Coming soon for Oracle​

- [ Subscriptions ](https://hasura.io/docs/latest/subscriptions/overview/)
- [ Event triggers ](https://hasura.io/docs/latest/event-triggers/overview/)


## Managing data with the Hasura Console​

The Hasura Console is a web UI that allows you to manage your data and metadata. It is available at `http://localhost:8080/console` when you run Hasura locally, or from your project's Console endpoint when you use[ Hasura Cloud ](https://cloud.hasura.io).

The data-management features (such as creating tables) are available in the `Data` tab. You can access your GraphQL API
in the `API` tab and interact with it using the GraphiQL interface.

Console support

We recommend using your preferred Oracle client instead. The Hasura Console is designed to be a tool for managing
your GraphQL API, and not a full-fledged database management tool.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/oracle/index/#introduction)
- [ Feature Support ](https://hasura.io/docs/latest/databases/oracle/index/#feature-support)
    - [ Queries ](https://hasura.io/docs/latest/databases/oracle/index/#queries)

- [ Mutations ](https://hasura.io/docs/latest/databases/oracle/index/#mutations)

- [ Subscriptions ](https://hasura.io/docs/latest/databases/oracle/index/#subscriptions)

- [ Event Triggers ](https://hasura.io/docs/latest/databases/oracle/index/#event-triggers)
- [ Coming soon for Oracle ](https://hasura.io/docs/latest/databases/oracle/index/#coming-soon-for-oracle)
- [ Managing data with the Hasura Console ](https://hasura.io/docs/latest/databases/oracle/index/#managing-data-with-the-hasura-console)


Image: [ hasura-webinar ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683628053/main-web/Group_11457_vceb9f.png)

### Ship faster with low-code APIs on MySQL, MariaDB, and Oracle

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)