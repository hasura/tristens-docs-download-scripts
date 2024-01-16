# BigQuery

## Introduction​

Hasura allows connecting to a[ BigQuery ](https://cloud.google.com/bigquery)database and building a GraphQL API based on
the database schema.

Supported versions:

Hasura GraphQL Engine `v2.0.0-alpha.1` onwards

## Get Started​

To try Hasura with BigQuery, you'll need your own new or existing BigQuery database.

Here is how you can get started with Hasura and BigQuery:

[ Get started with BigQuery ](https://hasura.io/docs/latest/databases/bigquery/getting-started/index/)

## Managing data with the Hasura Console​

The Hasura Console is a web UI that allows you to manage your data and metadata. It is available at `http://localhost:8080/console` when you run Hasura locally, or from your project's Console endpoint when you use[ Hasura Cloud ](https://cloud.hasura.io).

The data-management features (such as creating tables) are available in the `Data` tab. You can access your GraphQL API
in the `API` tab and interact with it using the GraphiQL interface.

Console support

We recommend using your preferred BigQuery client instead. The Hasura Console is designed to be a tool for managing your
GraphQL API, and not a full-fledged database management tool.

## Minimum required IAM permissions​

- BigQuery queries through Hasura require the `bigquery.jobs.create` and `bigquery.jobs.get` permissions to send a job
to the BigQuery servers.
- The `bigquery.tables.getData` permission allows Hasura to query your BigQuery data source. Note that mutations are not
currently supported for BigQuery, and so no corresponding `updateData` permission is required.
- To use the Hasura Console to edit your data source, several different permissions may be required depending on your
actions:
    - `bigquery.datasets.create` and `bigquery.datasets.delete` for creating and deleting datasets.

- `bigquery.routines.create` , `bigquery.routines.update` , and `bigquery.routines.delete` for managing user-defined
functions and stored procedures.

- `bigquery.table.create` , `bigquery.tables.list` , `bigquery.tables.get` , `bigquery.tables.delete` , and `bigquery.tables.update` to manage the dataset definition.


## Supported features​

Hasura currently supports queries and relationships on BigQuery.

## Keep up to date​

If you'd like to stay informed about the status of BigQuery support, subscribe to our newsletter and join our discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


## Know more​

- [ Get started ](https://hasura.io/docs/latest/databases/bigquery/getting-started/index/)
- [ Schema ](https://hasura.io/docs/latest/schema/bigquery/index/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/bigquery/index/#introduction)
- [ Get Started ](https://hasura.io/docs/latest/databases/bigquery/index/#get-started)
- [ Managing data with the Hasura Console ](https://hasura.io/docs/latest/databases/bigquery/index/#managing-data-with-the-hasura-console)
- [ Minimum required IAM permissions ](https://hasura.io/docs/latest/databases/bigquery/index/#minimum-required-iam-permissions)
- [ Supported features ](https://hasura.io/docs/latest/databases/bigquery/index/#supported-features)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/bigquery/index/#keep-up-to-date)
- [ Know more ](https://hasura.io/docs/latest/databases/bigquery/index/#know-more)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)