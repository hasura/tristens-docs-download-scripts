# Postgres Indexes

## Introduction​

[ Postgres indexes ](https://www.postgresql.org/docs/current/sql-createindex.html)are a way of increasing query
performance based on columns that are queried frequently. The concept is similar to the one of an index in a book. It
helps accessing the data you're looking for more quickly by maintaining additional metadata.

Note

Learn more about indexes in the[ Postgres documentation ](https://www.postgresql.org/docs/current/sql-createindex.html).

## Example​

 **Create an index on the column name in the table authors:** 

Let's say the database receives a large number of requests of authors being queried by their name, for example:

`SELECT   *   FROM  authors  WHERE  name  =   'J.K. Rowling' ;`

We can now create an index on the `name` column of the `authors` table:

`CREATE   INDEX  author_name_index  ON  authors  ( name ) ;`

Since the database is now able to look up the result of these queries more quickly, the performance of these queries
will increase significantly.

## Postgres indexes & Hasura​

Indexes can be used to optimize query performance in Hasura.[ Refer to this page ](https://hasura.io/docs/latest/queries/postgres/performance/#pg-data-validation-pg-indexes)for information about query
performance and how to add Postgres indexes to Hasura.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/indexes/#introduction)
- [ Example ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/indexes/#example)
- [ Postgres indexes & Hasura ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/indexes/#postgres-indexes--hasura)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)