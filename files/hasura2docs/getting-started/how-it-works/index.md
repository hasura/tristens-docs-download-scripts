# How Hasura GraphQL Engine Works

## Introduction​

The Hasura GraphQL Engine automatically generates a unified GraphQL schema from your databases, REST
endpoints, GraphQL endpoints and other sources allowing you to connect data together and work with it faster and more
powerfully than ever before. Hasura also comprises other features and services to provide a full-featured backend
engine for powering your API.

## Databases​

Given a database, the Hasura GraphQL Engine automatically generates a GraphQL schema and processes GraphQL queries,
subscriptions and mutations.

By default, Hasura supports[ PostgreSQL and multiple other databases ](https://hasura.io/docs/latest/databases/overview/).

## Tracking Tables & Schema Generation​

When you track a table in the Hasura GraphQL Engine, it automatically generates the following for it:

- A GraphQL **type definition** for the table
- A **query** field with `where` , `order_by` , `limit` , `offset` , and `distinct_on` arguments.
- A **query by primary key** field.
- A **query aggregate** field with `where` , `order_by` , `limit` , `offset` , and `distinct_on` arguments and
returning, `count` , `max` , `min` , `sum` and many other aggregates.
- An **insert mutation** field with `on_conflict` argument that supports upsert and bulk inserts.
- An **insert one mutation** field with `on_conflict` argument that supports upsert.
- An **update mutation** field with `where` argument that supports bulk updates.
- An **update by primary key mutation** field.
- A **delete mutation** field with `where` argument that supports bulk deletes.
- A **delete by primary key mutation** field.
- A **subscription** field with `where` , `order_by` , `limit` and `offset` arguments.
- A **subscription by primary key** field.
- A **subscription aggregate** field with `where` , `order_by` , `limit` , `offset` , and `distinct_on` arguments and
returning, `count` , `max` , `min` , `sum` and many other aggregates.
- A **subscription stream** field with `where` , and `cursor` arguments.


A GraphQL **type definition** for the table

A **query** field with `where` , `order_by` , `limit` , `offset` , and `distinct_on` arguments.

A **query by primary key** field.

A **query aggregate** field with `where` , `order_by` , `limit` , `offset` , and `distinct_on` arguments and
returning, `count` , `max` , `min` , `sum` and many other aggregates.

An **insert mutation** field with `on_conflict` argument that supports upsert and bulk inserts.

An **insert one mutation** field with `on_conflict` argument that supports upsert.

An **update mutation** field with `where` argument that supports bulk updates.

An **update by primary key mutation** field.

A **delete mutation** field with `where` argument that supports bulk deletes.

A **delete by primary key mutation** field.

A **subscription** field with `where` , `order_by` , `limit` and `offset` arguments.

A **subscription by primary key** field.

A **subscription aggregate** field with `where` , `order_by` , `limit` , `offset` , and `distinct_on` arguments and
returning, `count` , `max` , `min` , `sum` and many other aggregates.

A **subscription stream** field with `where` , and `cursor` arguments.

## Views​

When you track a view with a[ database which supports views ](https://hasura.io/docs/latest/databases/feature-support/)in Hasura GraphQL Engine,
it also automatically generates the same as the above but without the `_by_pk` fields. Depending on the type of
view created, Hasura may not generate the `insert` , `update` and `delete` mutation fields.

## Relationships​

When you create a relationship between a table/view with another table/view in the Hasura GraphQL Engine, it does
the following:

- Augments the type of the table/view by adding a reference to the nested type to allow fetching nested objects.
- Augments the `where` and `order_by` clauses to allow filtering and sorting based on nested objects.


## Resolvers​

The Hasura GraphQL Engine does not have any resolvers. The Hasura GraphQL Engine is actually a compiler that
compiles your GraphQL query into an efficient SQL query.

Hasura's GraphQL syntax is also optimized to expose the power of the underlying SQL so that you can make optimized
queries via GraphQL.

## Metadata​

Hasura Metadata is the description of the exposed Hasura GraphQL API and all other configuration. All the
information required for schema generation is stored by the Hasura GraphQL Engine as Metadata as a JSON blob in
a "catalogue" which is a Postgres schema in the specified Metadata database. When using the Hasura CLI, Hasura
Metadata is[ exposed as yaml files ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/)which can be checked into
version control to keep the your codebase in-sync with your database schema and Hasura changes.

See[ Metadata format ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/)for more details.

Hasura requires a PostgreSQL database to store Metadata

While you can use any[ supported database ](https://hasura.io/docs/latest/databases/overview/)for your datasource, Hasura requires a PostgreSQL database to store Metadata.

## Authorization​

Hasura uses attribute-based authorization where access control is done by creating rules for each model. For
example, in the case of database tables, you can create rules for database operations (select, insert, update,
delete) and the permissions that it must enforce in each case. These access control rules use dynamic session
variables that are passed to the GraphQL Engine from your authentication service with every request.

## Actions​

Actions are a way to extend Hasura's schema with REST APIs. You need to provide the schema for the API and the REST
API endpoint which is then called for resolving the result.

## Remote Schemas​

Using Remote Schemas you can add an existing GraphQL API into Hasura. You just have to provide the endpoint for it.
Hasura will introspect and merge the API into the existing schema. Additionally, you can provide permissions for the
Remote Schemas and create relationships with other models in Hasura too.

## Event Triggers​

Event Triggers use database triggers to capture DML activity and sends it reliably (at least once) to a configured
webhook.

## Hasura Cloud​

[ Hasura Cloud ](https://cloud.hasura.io/)empowers you to create highly optimized, managed and massively scalable
Hasura instances in seconds and includes extra reliability, monitoring, caching, tracing, security and deployment
features. You can also deploy Hasura manually using our Community Edition Docker image which includes all the core
features of GraphQL Engine.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#introduction)
- [ Databases ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#databases)
- [ Tracking Tables & Schema Generation ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#tracking-tables--schema-generation)
- [ Views ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#views)
- [ Relationships ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#relationships)
- [ Resolvers ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#resolvers)
- [ Metadata ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#metadata)
- [ Authorization ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#authorization)
- [ Actions ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#actions)
- [ Remote Schemas ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#remote-schemas)
- [ Event Triggers ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#event-triggers)
- [ Hasura Cloud ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#hasura-cloud)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)