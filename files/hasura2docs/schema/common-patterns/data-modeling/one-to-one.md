# Modeling One-to-One Table Relationships

## Introduction​

A `one-to-one` relationship between two tables can be established via a **unique foreign key constraint** .

Say we have the following two tables in our database schema:

```
authors  (
  id  SERIAL   PRIMARY   KEY ,
  name  TEXT
)
passport_info  (
  id  SERIAL   PRIMARY   KEY ,
  owner_id  INT   NOT   NULL
  passport_number  TEXT
   . . .
)
```

These two tables are related via a `one-to-one` relationship. i.e.:

- an `author` can have one `passport_info`
- a `passport_info` has one `owner`


## Step 1: Set up a table relationship in the database​

This `one-to-one` relationship can be established in the database by:

1. Adding a **foreign key constraint** from the `passport_info` table to the `authors` table using the `owner_id` and `id` columns of the tables respectively
2. Adding a **unique constraint** to the `owner_id` column for the `passport_info` table


This will ensure that the value of the `owner_id` column in `passport_info` table is present in the `id` column of the `authors` table and there will be only one row with a particular `owner_id` .

## Step 2: Set up GraphQL relationships​

To access the nested objects via the GraphQL API,[ create the following relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/create/):

- Object relationship, `passport_info` from the `authors` table using `id -> passport_info :: owner_id`
- Object relationship, `owner` from the `passport_info` table using `owner_id -> authors :: id`


## Query using one-to-one relationships​

We can now:

- fetch a list of `authors` with their `passport_info` :


- fetch a list of `passport_infos` with their `owner` :


## Insert using one-to-one relationships​

We can now:

- insert `passport_info` with their `owner` where the `owner` might already exist (assume unique `name` for `owner` ):


Note

You can avoid the `on_conflict` clause if you will never have conflicts.

### Caveat for nested inserts​

Due to the way nested inserts are typically handled (described[ here ](https://hasura.io/docs/latest/mutations/postgres/insert/#pg-nested-inserts)), the order of object insertion needs to be specified using the[ insertion_order ](https://hasura.io/docs/latest/api-reference/syntax-defs/#objrelusingmanualmapping)option while creating one-to-one
relationships via the API. This is necessary to ensure nested inserts are possible using either side as the parent which
would otherwise error out with a `Not-NULL violation` error in one of the cases.

In our example, inserting a `passport_info` with their nested `owner` will work seamlessly but trying to insert an `author` with their nested `passport_info` will throw a constraint violation error in case the insertion order is not
specified for the `owner` object relationship.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-one/#introduction)
- [ Step 1: Set up a table relationship in the database ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-one/#step-1-set-up-a-table-relationship-in-the-database)
- [ Step 2: Set up GraphQL relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-one/#step-2-set-up-graphql-relationships)
- [ Query using one-to-one relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-one/#query-using-one-to-one-relationships)
- [ Insert using one-to-one relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-one/#one-to-one-insert)
    - [ Caveat for nested inserts ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-one/#caveat-for-nested-inserts)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)