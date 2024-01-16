# Postgres Views

## Introduction​

A[ Postgres view ](https://www.postgresql.org/docs/current/sql-createview.html)is a virtual table in Postgres. It
represents the result of a query to one or more underlying tables in Postgres. Views are used to simplify complex
queries since these queries are defined once in the view, and can then be directly queried via the same.

Note

Please refer to the Postgres documentation for more details on[ standard views ](https://www.postgresql.org/docs/current/sql-createview.html)and[ materialized views ](https://www.postgresql.org/docs/current/rules-materializedviews.html).

## Standard views​

[ Standard views ](https://www.postgresql.org/docs/current/sql-createview.html)represent the result of a query without
actually storing data.

### Examples​

 **View with authors whose rating is larger than 6:** 

```
CREATE   VIEW  popular_authors  AS
   SELECT  name ,  rating
   FROM  authors
   WHERE  rating  >   6 ;
```

The created view can now be queried as follows:

`SELECT  name ,  rating  from  popular_authors ;`

 **View with authors ordered by their rating:** 

```
CREATE   VIEW  authors_ordered_by_rating  AS
     SELECT  name ,  rating
     FROM  authors
     ORDER   BY  rating ;
```

The created view can now be queried as follows:

`SELECT  name ,  rating  from  authors_ordered_by_rating ;`

## Materialized views​

Compared to the standard view described above,[ materialized views ](https://www.postgresql.org/docs/current/rules-materializedviews.html) **do** store data physically
in the database. Materialized views are used if data from complex queries needs to be accessed quickly.

### Example​

 **Materialized view with authors whose rating is larger than 6 and who are active, ordered by rating:** 

```
CREATE  MATERIALIZED  VIEW  popular_active_authors  AS
     SELECT  name ,  rating
     FROM  authors
     WHERE  rating  >   6   AND  is_active  =   TRUE
     ORDER   BY  rating ;
```

The created materialized view can now be queried as follows:

`SELECT  name ,  rating  from  popular_active_authors ;`

### Refreshing materialized views​

Materialized views don't always have the most recent data. Since the result of a query is stored in a materialized view
like in a cache, you need to make sure to refresh it periodically:

`REFRESH MATERIALIZED  VIEW  popular_active_authors ;`

Materialized views can be refreshed when their underlying source data changes using[ Postgres triggers ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/triggers/).

## Postgres views & Hasura​

After creating a view, you can expose it over your GraphQL API and query it like a normal table.

See[ this page ](https://hasura.io/docs/latest/schema/postgres/views/)for more info on how to create and expose views in Hasura.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/views/#introduction)
- [ Standard views ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/views/#standard-views)
    - [ Examples ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/views/#examples)
- [ Materialized views ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/views/#materialized-views)
    - [ Example ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/views/#example)

- [ Refreshing materialized views ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/views/#refreshing-materialized-views)
- [ Postgres views & Hasura ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/views/#postgres-views--hasura)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)