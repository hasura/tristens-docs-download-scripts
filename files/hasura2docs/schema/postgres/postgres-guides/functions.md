# Postgres Custom Functions

## Introduction​

[ Postgres custom functions ](https://www.postgresql.org/docs/current/sql-createfunction.html)allow you to customize your
database schema by defining a set of operations that can include several statements such as declarations, assignments
and conditional workflows. Postgres functions are similar to views but allow more procedural computations and can take
arguments. Custom SQL functions are also referred to as **stored procedures** .

Note

For more information on Postgres custom functions, please refer to the[ Postgres documentation ](https://www.postgresql.org/docs/current/sql-createfunction.html).

## Examples​

 **Searching articles** 

We can create the following function that we can call later to search articles based on the input text argument `search` .

```
CREATE   FUNCTION  search_articles ( search text )
RETURNS SETOF article  AS  $$
     SELECT   *
     FROM  article
     WHERE
      title ilike  ( '%'   ||  search  ||   '%' )
       OR  content ilike  ( '%'   ||  search  ||   '%' )
$$  LANGUAGE   sql  STABLE ;
```

Let's break this function apart:

- Function name: `search_articles`
- Parameters: there is one parameter where `search` is the name and `text` is the type
- Return type: `SETOF article`
- Function body: Block from `SELECT` until the end of the `WHERE` clause
- Language: The response is returned in the `sql` language


## Postgres custom functions & Hasura​

Postgres custom functions can be exposed in Hasura's GraphQL schema as a top-level field or as a computed field for a table.
They are typically used for performing custom business logic in the database.

Refer to[ Custom SQL functions ](https://hasura.io/docs/latest/schema/postgres/custom-functions/)and[ Computed fields ](https://hasura.io/docs/latest/schema/postgres/computed-fields/)for more use cases and for instructions on how to create and
expose Postgres custom functions in Hasura.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/functions/#introduction)
- [ Examples ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/functions/#examples)
- [ Postgres custom functions & Hasura ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/functions/#postgres-custom-functions--hasura)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)