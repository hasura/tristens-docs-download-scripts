# ClickHouse

## Introduction​

Hasura supports connecting to a[ Clickhouse ](https://www.clickhouse.com)service to automatically build a GraphQL API
based on its schema.

Supported versions:

1. Hasura GraphQL Engine `v2.30.0` onwards


## Get Started​

To try Hasura with ClickHouse, you'll need a new or existing ClickHouse instance.

Here are 2 ways you can get started with Hasura and ClickHouse:

1. [ Hasura Cloud ](https://hasura.io/docs/latest/databases/clickhouse/getting-started/cloud/): You'll need to be able to access your ClickHouse
instance service from Hasura Cloud.
2. [ Docker ](https://hasura.io/docs/latest/databases/clickhouse/getting-started/docker/): Run Hasura with Docker and then connect your ClickHouse
instance to Hasura.


## Managing data with the Hasura Console​

The Hasura Console is a web UI that allows you to manage your data and metadata. It is available at `http://localhost:8080/console` when you run Hasura locally, or from your project's Console endpoint when you use[ Hasura Cloud ](https://cloud.hasura.io).

The data-management features (such as creating tables) are available in the `Data` tab. You can access your GraphQL API
in the `API` tab and interact with it using the GraphiQL interface.

Console support

We recommend using your preferred ClickHouse client instead. The Hasura Console is designed to be a tool for managing
your GraphQL API, and not a full-fledged database management tool.

## Keep up to date​

Note

Currently, Hasura supports read-only queries, subscriptions, relationships, and permissions on ClickHouse.

If you'd like to stay informed about the status of ClickHouse support, subscribe to our newsletter and join our discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


## Know more​

- [ Get started ](https://hasura.io/docs/latest/databases/clickhouse/getting-started/index/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/clickhouse/index/#introduction)
- [ Get Started ](https://hasura.io/docs/latest/databases/clickhouse/index/#get-started)
- [ Managing data with the Hasura Console ](https://hasura.io/docs/latest/databases/clickhouse/index/#managing-data-with-the-hasura-console)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/clickhouse/index/#keep-up-to-date)
- [ Know more ](https://hasura.io/docs/latest/databases/clickhouse/index/#know-more)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)