# Postgres Triggers

## Introduction​

[ Postgres triggers ](https://www.postgresql.org/docs/current/sql-createtrigger.html)are used to invoke previously
defined Postgres functions *before* or *after* a specific database event (e.g. `INSERT` ) occurs.

Note

For more information on Postgres triggers, please refer to the[ Postgres documentation ](https://www.postgresql.org/docs/current/sql-createtrigger.html). We also have a Learn Tutorial
focusing on PostgresSQL.[ Information on triggers ](https://hasura.io/learn/database/postgresql/triggers/)can be found
here.

## Examples​

 **Trigger a Postgres function before an article is inserted or updated:** 

Let's say we want to check if an author is active before a corresponding article can be inserted or updated. We can do
so with the following Postgres function:

```
CREATE   FUNCTION  check_author_active ( )
    RETURNS trigger  AS  $ BODY $
     DECLARE  active_author BOOLEAN ;
     BEGIN
     SELECT  author . is_active  INTO  active_author  FROM   "authors"  author  WHERE  author . id  =   NEW . "author_id" ;
     IF  active_author  !=   TRUE   THEN
         RAISE   EXCEPTION   'Author must be active' ;
     END   IF ;
     RETURN   NEW ;
     END ;
    $ BODY $  LANGUAGE  plpgsql ;
```

Now we want to have this function executed whenever a new article is about to be inserted or updated. We can create a
Postgres trigger as follows:

`CREATE  TRIGGER insert_article BEFORE  INSERT   OR   UPDATE   ON   "articles"   FOR  EACH  ROW   EXECUTE   PROCEDURE  check_author_active ( ) ;`

If someone now tries to insert an article for an author that is not active, the following error will be thrown:

`unexpected  :  Author must be active`

 **Refresh a materialized view when an author gets inserted:** 

Let's say we want to refresh a materialized view whenever a new author is inserted.

The following Postgres function refreshes a materialized view:

```
CREATE   FUNCTION  refresh_materialized_view ( )
  RETURNS trigger  AS  $ BODY $
   BEGIN
  REFRESH MATERIALIZED  VIEW  popular_active_authors ;
   RETURN   NULL ;
   END ;
  $ BODY $  LANGUAGE  plpgsql ;
```

Now, to make sure this function gets called whenever a new author is inserted, we can create the following Postgres
trigger:

`CREATE  TRIGGER update_materialized_view AFTER  INSERT   ON   "authors"   FOR  EACH  ROW   EXECUTE   PROCEDURE  refresh_materialized_view ( ) ;`

## Postgres triggers & Hasura​

Postgres triggers can be used to perform business logic such as data validation and can be added[ as described here ](https://hasura.io/docs/latest/schema/postgres/data-validations/#pg-data-validations-pg-triggers).

Note

Hasura also has[ Event Triggers ](https://hasura.io/docs/latest/event-triggers/overview/)that can be used to invoke external HTTP APIs for executing
custom business logic on database events.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/triggers/#introduction)
- [ Examples ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/triggers/#examples)
- [ Postgres triggers & Hasura ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/triggers/#postgres-triggers--hasura)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)