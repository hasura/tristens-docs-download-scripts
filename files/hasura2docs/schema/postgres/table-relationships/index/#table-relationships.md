# Postgres: Relationships Between Tables/Views/Native Queries

## Introduction​

To make[ nested object queries ](https://hasura.io/docs/latest/queries/postgres/nested-object-queries/), the tables/views/Native Queries in your
database need to be connected via relationships.

Let's say we have the following tables in our database: `authors` , `passport_infos` , `articles` and `tags` .

## Table relationships​

The tables/views in any relational database are typically related to each other via one of the following types of table
relationships:

| Type | Example | Meaning |
|---|---|---|
|  `one-to-one`  |  `owner` and `passport_ infos`  |     - an `owner` can have one `passport_ info`
    - a `passport_ info` can have one `owner`
 |
|  `one-to-many`  |  `authors` and `articles`  |     - an `author` can have many `articles`
    - an `article` can have one `author`
 |
|  `many-to-many`  |  `articles` and `tags`  |     - an `article` can have many `tags`
    - a `tag` can have many `articles`
 |


- an `owner` can have one `passport_ info`
- a `passport_ info` can have one `owner`


- an `author` can have many `articles`
- an `article` can have one `author`


- an `article` can have many `tags`
- a `tag` can have many `articles`


## GraphQL schema relationships​

Each table relationship, as you can see from the above section, will have two component relationships (one in either
direction) in the GraphQL schema. These relationships can be one of the following types:

| Type | Example | Meaning |
|---|---|---|
|  `object relationship` (one-to-one) | an `article` can have one `author`  | an `article` object will have a single nested author object called `author`  |
|  `array relationship` (one-to-many) | an `author` can have many `articles`  | an `author` object will have an array of nested article objects called `articles`  |


Note

The relationship name is used to refer to the nested objects in queries. For example, " `articles` " of an `author` and
" `author` " of an `article` .

## Managing GraphQL relationships​

See the following to manage the object/array relationships between tables/views for the GraphQL schema:

- [ Postgres: Creating relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/create/)
- [ Postgres: Renaming relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/rename/)


## Table relationships modeling guides​

The following guides will help you model the different types of table relationships in the database:

- [ Modeling one-to-one table relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-one/)
- [ Modeling one-to-many table relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-many/)
- [ Modeling many-to-many table relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/many-to-many/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/#table-relationships/#introduction)
- [ Table relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/#table-relationships/#table-relationships)
- [ GraphQL schema relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/#table-relationships/#pg-graphql-relationships)
- [ Managing GraphQL relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/#table-relationships/#managing-graphql-relationships)
- [ Table relationships modeling guides ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/#table-relationships/#table-relationships-modeling-guides)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)