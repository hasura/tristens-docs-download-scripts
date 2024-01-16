# Postgres: Computed Fields

## What are computed fields?​

Computed fields are virtual values or objects that are dynamically computed and can be queried along with a table/view's
columns. Computed fields are computed upon request. They are computed by executing[ custom SQL functions ](https://www.postgresql.org/docs/current/sql-createfunction.html)(a.k.a. stored procedures) using
other columns of the table/view and other custom inputs if needed.

Note

Computed fields are only exposed over the GraphQL API and the database schema is not modified on addition of a computed
field.

### Supported SQL functions​

Only functions which satisfy the following constraints can be added as a computed field to a table/view. ( *terminology
from* [ Postgres docs ](https://www.postgresql.org/docs/current/sql-createfunction.html)):

- **Function behavior** : ONLY `STABLE` or `IMMUTABLE`
- **Argument modes** : ONLY `IN`
- **Table Argument** : One input argument with a table row type
- **Return type** : Either `SETOF <table-name>` or `BASE` type


Note

- Functions used as computed fields can also accept other arguments other than the mandatory table row argument. Values
for these extra arguments can be passed as arguments to the computed field in the GraphQL API.
- Functions used as computed fields do not need to be tracked by the Hasura GraphQL Engine.


## Computed field types​

Based on the SQL function's return type, we can define two types of computed fields:

### 1. Scalar computed fields​

Computed fields whose associated SQL function returns a[ base type ](https://www.postgresql.org/docs/current/extend-type-system.html#id-1.8.3.5.9)like *Integer* , *Boolean* , *Geography* etc. are scalar computed fields.

 **Example:** 

Let's say we have the following schema:

`authors ( id integer ,  first_name text ,  last_name text )`

[ Define an SQL function ](https://hasura.io/docs/latest/schema/postgres/custom-functions/#pg-create-sql-functions)called `author_full_name` :

```
CREATE   FUNCTION  author_full_name ( author_row authors )
RETURNS TEXT  AS  $$
   SELECT  author_row . first_name  ||   ' '   ||  author_row . last_name
$$  LANGUAGE   sql  STABLE ;
```

[ Add a computed field ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#pg-adding-computed-field)called `full_name` to the `authors` table using the SQL function
above.

Query data from the `authors` table:

### 2. Table computed fields​

Computed fields whose associated SQL function returns `SETOF <table-name>` are table computed fields. The return table
must be tracked to define such a computed field.

 **Example:** 

Let's say we have the following schema:

```
authors ( id integer ,  first_name text ,  last_name text )
articles ( id integer ,  title text ,  content text ,  author_id integer )
```

Now we can define a[ table relationship ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/)on the `authors` table to fetch
authors along with their articles.

We can make use of computed fields to fetch the author's articles with a search parameter.

[ Define an SQL function ](https://hasura.io/docs/latest/schema/postgres/custom-functions/#pg-create-sql-functions)called `filter_author_articles` :

```
CREATE   FUNCTION  filter_author_articles ( author_row authors ,  search text )
RETURNS SETOF articles  AS  $$
   SELECT   *
   FROM  articles
   WHERE
     (  title ilike  ( '%'   ||  search  ||   '%' )
       OR  content ilike  ( '%'   ||  search  ||   '%' )
     )   AND  author_id  =  author_row . id
$$  LANGUAGE   sql  STABLE ;
```

[ Add a computed field ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#pg-adding-computed-field)called `filtered_articles` to the `authors` table using the SQL
function above.

Query data from the `authors` table:

## Adding a computed field to a table/view​

- Console
- CLI
- API


Head to the `Modify` tab of the table/view and click on the `Add` button in the `Computed fields` section:

Image: [ Add computed field ](https://hasura.io/docs/assets/images/computed-field-create-033edb3d7b65b71bd2d15d4cca986cbb.png)

You can add a computed field by updating the `metadata > databases > [db-name] > tables > [table_name].yaml` file:

```
-   table :
     schema :  public
     name :  authors
   computed_fields :
     -   name :  full_name
       definition :
         function :
           schema :  public
           name :  author_full_name
         table_argument :   null
       comment :   ''
```

Apply the Metadata by running:

`hasura metadata apply`

A computed field can be added to a table/view using the[ pg_add_computed_field ](https://hasura.io/docs/latest/api-reference/metadata-api/computed-field/#metadata-pg-add-computed-field)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_add_computed_field" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   {
       "name" :   "authors" ,
       "schema" :   "public"
     } ,
     "name" :   "full_name" ,
     "definition" :   {
       "function" :   {
         "name" :   "author_full_name" ,
         "schema" :   "public"
       } ,
       "table_argument" :   "author_row"
     }
   }
}
```

## Computed fields permissions​

[ Access control ](https://hasura.io/docs/latest/auth/authorization/index/)to computed fields depends on the type of computed field.

- For **scalar computed fields** , permissions are managed similar to the[ columns permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/column-level-permissions/)of the table.
- For **table computed fields** , the permissions set on the return table are respected.


## Accessing Hasura session variables in computed fields​

It can be useful to have access to the session variable from the SQL function defining a computed field. For instance,
suppose we want to record which users have liked which articles. We can do so using a table `article_likes` that
specifies a many-to-many relationship between `articles` and `users` . In such a case it can be useful to know if the
current user has liked a specific article, and this information can be exposed as a *Boolean* computed field on `articles` .

Create a function with an argument for session variables and add it with the[ pg_add_computed_field ](https://hasura.io/docs/latest/api-reference/metadata-api/computed-field/#metadata-pg-add-computed-field)API with the `session_argument` key set. The session argument is a JSON object where keys are session variable names (in lower case)
and values are strings. Use the `->>` JSON operator to fetch the value of a session variable as shown in the following
example.

```
-- 'hasura_session' will be the session argument
CREATE   OR  REPLACE  FUNCTION  article_liked_by_user ( article_row articles ,  hasura_session json )
RETURNS boolean  AS  $$
SELECT   EXISTS   (
     SELECT   1
     FROM  article_likes  A
     WHERE   A . user_id  =  hasura_session  - > >   'x-hasura-user-id'   AND   A . article_id  =  article_row . id
) ;
$$  LANGUAGE   sql  STABLE ;
```

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" : "pg_add_computed_field" ,
     "args" : {
         "source" :   "<db_name>" ,
         "table" : {
             "name" : "articles" ,
             "schema" : "public"
         } ,
         "name" : "liked_by_user" ,
         "definition" : {
             "function" : {
                 "name" : "article_liked_by_user" ,
                 "schema" : "public"
             } ,
             "table_argument" : "article_row" ,
             "session_argument" : "hasura_session"
         }
     }
}
```

Note

The specified session argument is not included in the argument options of the computed field in the GraphQL schema.

Supported from

This feature is available in `v1.3.0` and above

## Computed fields vs. Postgres generated columns​

Postgres, from version `12` , is introducing[ Generated Columns ](https://www.postgresql.org/docs/12/ddl-generated-columns.html). The value of generated columns is
also computed from other columns of a table. Postgres' generated columns come with their own limitations. Hasura's
computed fields are defined via an SQL function, which allows users to define any complex business logic in a function.
Generated columns will go together with computed fields where Hasura treats generated columns as normal Postgres
columns.

## Computed fields in Remote Relationships​

Using computed fields in[ Remote Relationships ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/index/)allows transformation
of data from table columns before joining with data from remote sources. For instance, suppose we want to extract
certain field from a `json` column and join it with a field in a Remote Schema by argument value. We would define a
computed field which returns a scalar type of the field value in the `json` column and use it to join the graphql field
of the Remote Schema. Consider the following Postgres schema.

```
CREATE   TABLE   "user"   ( id SERIAL PRIMARY KEY ,   name  TEXT  UNIQUE   NOT   NULL ,  address json  NOT   NULL ) ;
-- SQL function returns city of a "user" using "->>" json operator
CREATE   FUNCTION  get_city ( table_row  "user" )
RETURNS TEXT  AS  $$
   SELECT  table_row . address  - > >   'city'
$$  LANGUAGE   sql  STABLE ;
```

Now, let's track the table and add computed field `user_city` using the SQL function `get_city` . Consider the following
Remote Schema.

```
type   Query   {
   get_coordinates ( city :   String ) :   Coordinates
}
type   Coordinates   {
   lat :   Float
   long :   Float
}
```

[ Define a remote relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-pg-create-remote-relationship)with name `user_location` from `user_city` scalar computed field to `get_coordinates` Remote Schema field. We can query
users with the pincode of their residing place.

Note

Only `Scalar computed fields` are allowed to join fields from remote sources

Supported from

This feature is available in `v2.0.1` and above

### What did you think of this doc?

- [ What are computed fields? ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#what-are-computed-fields)
    - [ Supported SQL functions ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#supported-sql-functions)
- [ Computed field types ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#computed-field-types)
    - [ 1. Scalar computed fields ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#1-scalar-computed-fields)

- [ 2. Table computed fields ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#2-table-computed-fields)
- [ Adding a computed field to a table/view ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#pg-adding-computed-field)
- [ Computed fields permissions ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#computed-fields-permissions)
- [ Accessing Hasura session variables in computed fields ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#accessing-hasura-session-variables-in-computed-fields)
- [ Computed fields vs. Postgres generated columns ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#computed-fields-vs-postgres-generated-columns)
- [ Computed fields in Remote Relationships ](https://hasura.io/docs/latest/schema/postgres/computed-fields/#computed-fields-in-remote-relationships)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)