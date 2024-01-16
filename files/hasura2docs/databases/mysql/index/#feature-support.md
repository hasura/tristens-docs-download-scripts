# MySQL

## Introduction​

Hasura enables you to connect to MySQL databases to automatically build a rich GraphQL API based on your database
schema.

At present, our MySQL integration is available in Hasura Cloud and Docker environments, where you can run Hasura GraphQL
Engine and connect the MySQL GraphQL Data Connector to it. For more information on GraphQL Data Connectors check out[ our blog post on the topic ](https://hasura.io/blog/hasura-graphql-data-connectors/).

To get started with MySQL:

- In Hasura Cloud, check out our[ Getting Started with MySQL in Hasura Cloud ](https://hasura.io/docs/latest/databases/mysql/cloud/)guide
- In a Docker environment, check out our[ Getting Started with Docker ](https://hasura.io/docs/latest/databases/mysql/docker/)guide


Supported versions:

1. Hasura GraphQL Engine `v2.24.0` onwards
2. Hasura supports most databases with standard implementations of **MySQL 8.0 and higher** including: Amazon RDS,
Amazon Aurora, Google Cloud SQL and Digital Ocean.
3. PlanetScale and certain other providers are unsupported.


Supported features

Hasura currently supports queries, mutations (INSERT, UPDATE, DELETE), table relationships, remote relationships and
permissions on MySQL.

Note that Hasura doesn't yet support the ability to modify the database schema for MySQL, so the database you connect to
should already contain tables and data. You should also ideally have access to it outside of Hasura to modify the
schema.

## Feature Support​

### Queries​

### Mutations​

### Subscriptions​

### Event Triggers​

## Coming soon for MySQL​

- [ Subscriptions ](https://hasura.io/docs/latest/subscriptions/overview/)
- [ Event triggers ](https://hasura.io/docs/latest/event-triggers/overview/)


## Managing data with the Hasura Console​

The Hasura Console is a web UI that allows you to manage your data and metadata. It is available at `http://localhost:8080/console` when you run Hasura locally, or from your project's Console endpoint when you use[ Hasura Cloud ](https://cloud.hasura.io).

The data-management features (such as creating tables) are available in the `Data` tab. You can access your GraphQL API
in the `API` tab and interact with it using the GraphiQL interface.

Console support

We recommend using your preferred MySQL client instead. The Hasura Console is designed to be a tool for managing
your GraphQL API, and not a full-fledged database management tool.

## Resources​

- Check out the[ Getting Started with Docker ](https://hasura.io/docs/latest/databases/mysql/docker/)guide.
- [ Connect a Google Cloud SQL for MySQL database ](https://hasura.io/docs/latest/databases/mysql/gcp/).
- If you're interested in learning more about MySQL, check out[ this tutorial ](https://hasura.io/learn/database/mysql/introduction/)from our Learn site.


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/mysql/index/#feature-support/#introduction)
- [ Feature Support ](https://hasura.io/docs/latest/databases/mysql/index/#feature-support/#feature-support)
    - [ Queries ](https://hasura.io/docs/latest/databases/mysql/index/#feature-support/#queries)

- [ Mutations ](https://hasura.io/docs/latest/databases/mysql/index/#feature-support/#mutations)

- [ Subscriptions ](https://hasura.io/docs/latest/databases/mysql/index/#feature-support/#subscriptions)

- [ Event Triggers ](https://hasura.io/docs/latest/databases/mysql/index/#feature-support/#event-triggers)
- [ Coming soon for MySQL ](https://hasura.io/docs/latest/databases/mysql/index/#feature-support/#coming-soon-for-mysql)
- [ Managing data with the Hasura Console ](https://hasura.io/docs/latest/databases/mysql/index/#feature-support/#managing-data-with-the-hasura-console)
- [ Resources ](https://hasura.io/docs/latest/databases/mysql/index/#feature-support/#resources)


Image: [ hasura-webinar ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683628053/main-web/Group_11457_vceb9f.png)

### Ship faster with low-code APIs on MySQL, MariaDB, and Oracle

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)