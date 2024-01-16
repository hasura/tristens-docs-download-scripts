# BigQuery: GraphQL Queries

## Introduction​

GraphQL queries are used to fetch data from the server.

Hasura GraphQL Engine auto-generates queries as part of the GraphQL schema from your BigQuery schema model. It generates
a range of possible queries and operators that also work with relationships defined in your SQL schema.

All tables of the database tracked by the GraphQL Engine can be queried over the GraphQL endpoint. If you have a tracked
table in your database, its query field is added as a nested field under the `query_root` root level type.

## Auto-generated query field schema​

 **For example** , the auto-generated schema for the query field for a table `author` looks like the following:

```
author   (
   distinct_on :   [ author_select_column ]
   where :   author_bool_exp
   limit :   Int
   offset :   Int
   order_by :    [ author_order_by ! ]
) :   [ author ]
# single object select
author_by_pk   (
   # all primary key columns args
   id :   Int !
) :   author
```

See the[ Query API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/)for the full specifications.

Note

The query field will be of the format `<dataset_name>_<table_name>` .

## Exploring queries​

You can explore the entire schema and the available queries using the `GraphiQL` interface in the Hasura Console.

Let's take a look at the different queries you can run using the Hasura GraphQL Engine. We'll use examples based on a
typical author/article schema for reference.

- [ Simple object queries ](https://hasura.io/docs/latest/queries/bigquery/simple-object-queries/)
- [ Nested object queries ](https://hasura.io/docs/latest/queries/bigquery/nested-object-queries/)
- [ Aggregation queries ](https://hasura.io/docs/latest/queries/bigquery/aggregation-queries/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/queries/bigquery/index/#introduction)
- [ Auto-generated query field schema ](https://hasura.io/docs/latest/queries/bigquery/index/#auto-generated-query-field-schema)
- [ Exploring queries ](https://hasura.io/docs/latest/queries/bigquery/index/#exploring-queries)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)