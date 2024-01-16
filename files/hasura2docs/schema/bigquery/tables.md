# BigQuery: Tables Basics

## Introduction​

Adding tables allows you to define the GraphQL types of your schema including their corresponding fields.

## Creating tables​

Let's say we want to create two simple tables for `articles` and `author` schema:

```
authors  (
     ` id `  INT64 ,
     ` name `  STRING
) ;
articles  (
     ` id `  INT64 ,
     ` title `  STRING ,
     ` body `  STRING ,
     ` author_id `  INT64 ,
     ` is_published `   BOOL ,
     ` published_on `   DATETIME ,
     ` rating `  INT64
) ;
```

- Console
- CLI
- API


Open the Hasura Console and head to the `Data` tab and click on the button on the left side bar to open up an interface
to create tables.

For example, here is the schema for the `articles` table in this interface:

Image: [ Schema for an article table ](https://hasura.io/docs/assets/images/create-table-graphql-bigquery-11dc0beb188eb0564389ea9e3e4d7689.png)

1. [ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
following SQL statement to the `up.sql` file:
2. Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)` the above statement:
3. Apply the migration by running:


[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
following SQL statement to the `up.sql` file:

```
CREATE   TABLE   ` bigquery.authors `   (
     ` id `  INT64 ,
     ` name `  STRING
) ;
CREATE   TABLE   ` bigquery.articles `   (
     ` id `  INT64 ,
     ` title `  STRING ,
     ` body `  STRING ,
     ` author_id `  INT64 ,
     ` is_published `   BOOL ,
     ` published_on `   DATETIME ,
     ` rating `  INT64
) ;
```

Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)` the above statement:

```
DROP   TABLE   ` hasura.author ` ;
DROP   TABLE   ` hasura.article ` ;
```

Apply the migration by running:

`hasura migrate apply`

You can create a table by making an API call to the[ run_sql ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql)schema API:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "bigquery_run_sql" ,
     "args" :   {
         "source" :   "<db_name>" ,
         "sql" :   "CREATE TABLE `bigquery.author` (`id` INT64,`name` STRING);CREATE TABLE `bigquery.article` (`id` INT64,`title` STRING,`body` STRING,`author_id` INT64,`is_published` BOOL,`published_on` DATETIME,`rating` INT64);"
     }
}
```

## Tracking tables​

Tables can be present in the underlying BigQuery database without being exposed over the GraphQL API. In order to expose
a table over the GraphQL API, it needs to be **tracked** .

- Console
- CLI
- API


When a table is created via the Hasura Console, it gets tracked by default.

You can track any existing tables in your database from the `Data -> Schema` page:

Image: [ Track table ](https://hasura.io/docs/assets/images/schema-track-tables-bigquery-a897b1bd3fb2ba8e7548430cfec9849a.png)

1. To track the table and expose it over the GraphQL API, edit the `tables.yaml` file in the `metadata` directory as
follows:
2. Apply the metadata by running:


To track the table and expose it over the GraphQL API, edit the `tables.yaml` file in the `metadata` directory as
follows:

```
-   table :
     dataset :  bigquery
     name :  authors
-   table :
     dataset :  bigquery
     name :  articles
```

Apply the metadata by running:

`hasura metadata apply`

To track the table and expose it over the GraphQL API, make the following API call to the[ bigquery_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-bigquery-track-table)metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_track_table" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   {
         "dataset" :   "bigquery" ,
         "name" :   "articles"
     }
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
   body :   String
   author_id :   Int
   is_published :   Boolean
   published_on :   Datetime
   rating :   Int
}
```

Let's analyze the above type:

- `Articles` is the name of the type
- `id` , `title` , `body` , and so on are fields of the `Articles` type
- `Int` and `String` , `Boolean` and `Datetime` are types that fields can have


The following query/mutation fields are generated for the `articles` table we just created and tracked:

```
# Query field: fetch data from the table: "bigquery.articles"
bigquery_articles (
     distinct_on :   [ bigquery_articles_select_column ! ]
     limit :   Int
     offset :   Int
     order_by :   [ bigquery_articles_order_by ! ]
     where :   bigquery_articles_bool_exp
) :   [ bigquery_articles ! ] !
# Query field: fetch aggregated fields from the table: "bigquery.articles"
bigquery_articles_aggregate (
     distinct_on :   [ bigquery_articles_select_column ! ]
     limit :   Int
     offset :   Int
     order_by :   [ bigquery_articles_order_by ! ]
     where :   bigquery_articles_bool_exp
) :   bigquery_articles_aggregate !
```

These auto-generated fields will allow you to query data in the table.

See the[ query ](https://hasura.io/docs/latest/api-reference/graphql-api/query/)API reference for the full specifications.

### GraphQL types documentation​

Hasura automatically picks up any comments that might have been added to your tables and columns and adds them as
GraphQL descriptions of the auto-generated types and fields.

## Try out basic GraphQL requests​

At this point, you should be able to try out basic GraphQL queries/mutations on the newly created tables from the `API` tab in the Console. *(You may want to add some sample data into the tables first)* 

- Query all rows in the `articles` table:


Query all rows in the `articles` table:

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/bigquery/tables/#introduction)
- [ Creating tables ](https://hasura.io/docs/latest/schema/bigquery/tables/#creating-tables)
- [ Tracking tables ](https://hasura.io/docs/latest/schema/bigquery/tables/#tracking-tables)
- [ Generated GraphQL schema types ](https://hasura.io/docs/latest/schema/bigquery/tables/#generated-graphql-schema-types)
    - [ GraphQL types documentation ](https://hasura.io/docs/latest/schema/bigquery/tables/#graphql-types-documentation)
- [ Try out basic GraphQL requests ](https://hasura.io/docs/latest/schema/bigquery/tables/#try-out-basic-graphql-requests)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)