# Modeling One-to-Many Table Relationships

## Introduction​

A `one-to-many` relationship between two tables can be established via a **foreign key constraint** .

Say we have the following two tables in our database schema:

```
authors  (
  id  SERIAL   PRIMARY   KEY ,
  name  TEXT
)
articles  (
  id  SERIAL   PRIMARY   KEY ,
  author_id  INT
  title  TEXT
   . . .
)
```

These two tables are related via a `one-to-many` relationship. i.e:

- an `author` can have many `articles`
- an `article` has one `author`


## Step 1: Set up a table relationship in the database​

This `one-to-many` relationship can be established in the database by:

1. Adding a **foreign key constraint** from the `articles` table to the `authors` table using the `author_id` and `id` columns of the tables respectively.


This will ensure that the value of `author_id` column in the `articles` table is present in the `id` column of the `authors` table.

## Step 2: Set up GraphQL relationships​

To access the nested objects via the GraphQL API,[ create the following relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/create/):

- Array relationship, `articles` from `authors` table using `articles :: author_id -> id`
- Object relationship, `author` from `articles` table using `author_id -> authors :: id`


## Query using one-to-many relationships​

We can now:

- fetch a list of `authors` with their `articles` :


- fetch a list of `articles` with their `author` :


## Insert using one-to-many relationships​

We can now:

- insert an `author` with their `articles` where the author might already exist (assume unique `name` for `author` ):


- insert `articles` with their `author` where the `author` might already exist (assume unique `name` for `author` ):


Note

You can avoid the `on_conflict` clause if you will never have conflicts.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-many/#introduction)
- [ Step 1: Set up a table relationship in the database ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-many/#step-1-set-up-a-table-relationship-in-the-database)
- [ Step 2: Set up GraphQL relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-many/#step-2-set-up-graphql-relationships)
- [ Query using one-to-many relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-many/#query-using-one-to-many-relationships)
- [ Insert using one-to-many relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-many/#insert-using-one-to-many-relationships)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)