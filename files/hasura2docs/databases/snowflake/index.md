# Snowflake

## Introduction​

Hasura supports connecting to a[ Snowflake ](https://www.snowflake.com)service to automatically build a GraphQL API based on its schema.

Supported versions:

1. Hasura GraphQL Engine `v2.24.0` onwards


## Get Started​

To try Hasura with Snowflake, you'll need a new or existing Snowflake instance.

Here are 2 ways you can get started with Hasura and Snowflake:

1. [ Hasura Cloud ](https://hasura.io/docs/latest/databases/snowflake/getting-started/cloud/): You'll need to be able to access your Snowflake
instance service from Hasura Cloud.
2. [ Docker ](https://hasura.io/docs/latest/databases/snowflake/getting-started/docker/): Run Hasura with Docker and then connect your Snowflake
instance to Hasura.


## Feature Support​

### Queries​

### Mutations​

### Subscriptions​

### Event Triggers​

## Managing data with the Hasura Console​

The Hasura Console is a web UI that allows you to manage your data and metadata. It is available at `http://localhost:8080/console` when you run Hasura locally, or from your project's Console endpoint when you use[ Hasura Cloud ](https://cloud.hasura.io).

The data-management features (such as creating tables) are available in the `Data` tab. You can access your GraphQL API
in the `API` tab and interact with it using the GraphiQL interface.

Console support

We recommend using your preferred Snowflake client instead. The Hasura Console is designed to be a tool for managing
your GraphQL API, and not a full-fledged database management tool.

## Keep up to date​

Note

Currently, Hasura supports read-only queries, subscriptions, relationships, and permissions on Snowflake.

If you'd like to stay informed about the status of Snowflake support, subscribe to our newsletter and join our
discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


## Know more​

- [ Get started ](https://hasura.io/docs/latest/databases/snowflake/getting-started/index/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/snowflake/index/#introduction)
- [ Get Started ](https://hasura.io/docs/latest/databases/snowflake/index/#get-started)
- [ Feature Support ](https://hasura.io/docs/latest/databases/snowflake/index/#feature-support)
    - [ Queries ](https://hasura.io/docs/latest/databases/snowflake/index/#queries)

- [ Mutations ](https://hasura.io/docs/latest/databases/snowflake/index/#mutations)

- [ Subscriptions ](https://hasura.io/docs/latest/databases/snowflake/index/#subscriptions)

- [ Event Triggers ](https://hasura.io/docs/latest/databases/snowflake/index/#event-triggers)
- [ Managing data with the Hasura Console ](https://hasura.io/docs/latest/databases/snowflake/index/#managing-data-with-the-hasura-console)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/snowflake/index/#keep-up-to-date)
- [ Know more ](https://hasura.io/docs/latest/databases/snowflake/index/#know-more)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677756408/main-web/Group_11455_1_ziz1fz.png)

### Combining Snowflake and PostgreSQL to build low-latency apps on historical data insights

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)