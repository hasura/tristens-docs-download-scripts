# Postgres: Tables Basics

## Introduction​

Adding tables allows you to define the GraphQL types of your schema including their corresponding fields.

## Creating tables​

Let's say we want to create two simple tables for `articles` and `author` schema:

```
author  (
  id  SERIAL   PRIMARY   KEY ,
  name  TEXT
)
articles  (
  id  SERIAL   PRIMARY   KEY ,
  title  TEXT ,
  content  TEXT ,
  rating  INT ,
  author_id  INT
)
```

- Console
- CLI
- API


Open the Hasura Console and head to the `Data` tab and click on the button on the left side bar to open up an interface
to create tables.

For example, here is the schema for the `articles` table in this interface:

Image: [ Schema for an article table ](https://hasura.io/docs/assets/images/create-table-graphql-8578eb643df725a4329f071ba6d489d7.png)

1. [ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
following SQL statement to the `up.sql` file:
2. Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)` the above statement:
3. Apply the migration by running:


[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
following SQL statement to the `up.sql` file:

`CREATE   TABLE  articles ( id  serial   NOT   NULL ,  title  text   NOT   NULL ,  content  text   NOT   NULL ,  rating  integer   NOT   NULL ,  author_id  serial   NOT   NULL ,   PRIMARY   KEY   ( id ) ) ;`

Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)` the above statement:

`DROP   TABLE  articles ;`

Apply the migration by running:

`hasura migrate apply`

You can create a table by making an API call to the[ run_sql ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql)schema API:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "run_sql" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "sql" :   "CREATE TABLE articles(id serial NOT NULL, title text NOT NULL, content text NOT NULL, rating integer NOT NULL, author_id serial NOT NULL, PRIMARY KEY (id));"
   }
}
```

## Tracking tables​

Tables can be present in the underlying Postgres database without being exposed over the GraphQL API. In order to expose
a table over the GraphQL API, it needs to be **tracked** .

- Console
- CLI
- API


When a table is created via the Hasura Console, it gets tracked by default.

You can track any existing tables in your database from the `Data -> Schema` page:

Image: [ Track table ](https://hasura.io/docs/assets/images/schema-track-tables-a2941feb62b228ea11823238db29f653.png)

1. To track the table and expose it over the GraphQL API, edit the `tables.yaml` file in the `metadata` directory as
follows:
2. Apply the metadata by running:


To track the table and expose it over the GraphQL API, edit the `tables.yaml` file in the `metadata` directory as
follows:

```
-   table :
     schema :  public
     name :  authors
-   table :
     schema :  public
     name :  articles
```

Apply the metadata by running:

`hasura metadata apply`

To track the table and expose it over the GraphQL API, make the following API call to the[ pg_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-track-table)metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_track_table" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "schema" :   "public" ,
     "name" :   "articles"
   }
}
```

## Generated GraphQL schema types​

As soon as a table is created and tracked, the corresponding GraphQL schema types and query/mutation fields will be
automatically generated.

The following object type is generated for the `articles` table we just created and tracked:

```
# Object type
type   Articles   {
   id :   Int
   title :   String
   content :   String
   rating :   Int
   author_id :   Int
}
```

Let's analyze the above type:

- `Articles` is the name of the type
- `id` , `title` , `content` , `rating` and `author_id` are fields of the `Articles` type
- `Int` and `String` are types that fields can have


The following query/mutation fields are generated for the `articles` table we just created and tracked:

```
# Query field
articles   (
   where :   articles_bool_exp
   limit :   Int
   offset :   Int
   order_by :   [ articles_order_by ! ]
) :   [ articles ! ] !
# insert/upsert mutation field
insert_articles   (
   objects :   [ articles_insert_input ! ] !
   on_conflict :   articles_on_conflict
) :   articles_mutation_response
# update mutation field
update_articles   (
   where :   articles_bool_exp !
   _inc :   articles_inc_input
   _set :   articles_set_input
) :   articles_mutation_response
# delete mutation field
delete_articles   (
   where :   articles_bool_exp !
) :   articles_mutation_response
```

These auto-generated fields will allow you to query and mutate data in our table.

See the[ query ](https://hasura.io/docs/latest/api-reference/graphql-api/query/)and[ mutation ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/)API
references for the full specifications.

### GraphQL types documentation​

Hasura automatically picks up any comments that might have been added to your tables and columns and adds them as
GraphQL descriptions of the auto-generated types and fields.

## Try out basic GraphQL requests​

At this point, you should be able to try out basic GraphQL queries/mutations on the newly created tables from the `API` tab in the Console. *(You may want to add some sample data into the tables first)* 

- Query all rows in the `articles` table:
- Insert data in the `author` table:


Query all rows in the `articles` table:

Insert data in the `author` table:

Note

author's `id` does not need to be passed as an input as it is of type `serial` (auto incrementing integer).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/tables/#introduction)
- [ Creating tables ](https://hasura.io/docs/latest/schema/postgres/tables/#pg-create-tables)
- [ Tracking tables ](https://hasura.io/docs/latest/schema/postgres/tables/#tracking-tables)
- [ Generated GraphQL schema types ](https://hasura.io/docs/latest/schema/postgres/tables/#generated-graphql-schema-types)
    - [ GraphQL types documentation ](https://hasura.io/docs/latest/schema/postgres/tables/#graphql-types-documentation)
- [ Try out basic GraphQL requests ](https://hasura.io/docs/latest/schema/postgres/tables/#try-out-basic-graphql-requests)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)