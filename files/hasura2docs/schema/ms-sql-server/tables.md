# MS SQL Server: Tables Basics

## Introduction​

Adding tables allows you to define the GraphQL types of your schema including their corresponding fields.

## Creating tables​

Let's say we want to create two simple tables for `articles` and `authors` schema:

```
authors  (
  id  int   PRIMARY   KEY ,
  name  text
)
articles  (
  id  int   PRIMARY   KEY ,
  title  text ,
  content  text ,
  rating  int ,
  author_id  int
)
```

- Console
- CLI
- API


Open the Hasura Console and head to the `Data` tab and click on the button on the left side bar to open up an interface
to create tables.

For example, here is the schema for the `articles` table in this interface:

Image: [ Schema for an article table ](https://hasura.io/docs/assets/images/create-table-graphql-mssql-316cc2366725a27cc3b887052319c8f2.png)

1. [ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
following SQL statement to the `up.sql` file:
2. Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)the above statement:
3. Apply the migration by running:


[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
following SQL statement to the `up.sql` file:

`CREATE   TABLE  articles ( id  int   NOT   NULL ,  title  text   NOT   NULL ,  content  text   NOT   NULL ,  rating  int   NOT   NULL ,  author_id  int   NOT   NULL ,   PRIMARY   KEY   ( id ) ) ;`

Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)the above statement:

`DROP   TABLE  articles ;`

Apply the migration by running:

`hasura migrate apply`

You can create a table by making an API call to the[ schema_run_sql Metadata API ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql):

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "run_sql" ,
   "args" :   {
     "source" :   "<db-name>" ,
     "sql" :   "CREATE TABLE articles(id int NOT NULL, title text NOT NULL, content text NOT NULL, rating int NOT NULL, author_id int NOT NULL, PRIMARY KEY (id));"
   }
}
```

## Tracking tables​

Tables can be present in the underlying MS SQL Server database without being exposed over the GraphQL API. In order to
expose a table over the GraphQL API, it needs to be **tracked** .

- Console
- CLI
- API


When a table is created via the Hasura Console, it gets tracked by default.

You can track any existing tables in your database from the `Data -> Schema` page:

Image: [ Track table ](https://hasura.io/docs/assets/images/schema-track-tables-mssql-e48c8443241835198fa7c4a73bcc70c2.png)

1. To track the table and expose it over the GraphQL API, edit the `tables.yaml` file in the `metadata` directory as
follows:
2. Apply the Metadata by running:


To track the table and expose it over the GraphQL API, edit the `tables.yaml` file in the `metadata` directory as
follows:

```
-   table :
     schema :  dbo
     name :  authors
-   table :
     schema :  dbo
     name :  articles
```

Apply the Metadata by running:

`hasura metadata apply`

To track the table and expose it over the GraphQL API, make the following API call to the[ mssql_track_table Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-track-table):

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_track_table" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "authors"
   }
}
```

## Generated GraphQL schema types​

As soon as a table is created and tracked, the corresponding GraphQL schema types and query fields will be automatically
generated.

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


The following query fields are generated for the `articles` table we just created and tracked:

```
# Query field
articles   (
   where :   articles_bool_exp
   limit :   Int
   offset :   Int
   order_by :   [ articles_order_by ! ]
) :   [ articles ! ] !
```

These auto-generated fields will allow you to query data in our table.

See the[ query ](https://hasura.io/docs/latest/api-reference/graphql-api/query/)API reference for the full specifications.

## Try out basic GraphQL requests​

At this point, you should be able to try out basic GraphQL queries on the newly created tables from the `API` tab in the
console. *(You may want to add some sample data into the tables first)* 

- Query all rows in the `articles` table:


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/ms-sql-server/tables/#introduction)
- [ Creating tables ](https://hasura.io/docs/latest/schema/ms-sql-server/tables/#ms-sql-server-create-tables)
- [ Tracking tables ](https://hasura.io/docs/latest/schema/ms-sql-server/tables/#tracking-tables)
- [ Generated GraphQL schema types ](https://hasura.io/docs/latest/schema/ms-sql-server/tables/#generated-graphql-schema-types)
- [ Try out basic GraphQL requests ](https://hasura.io/docs/latest/schema/ms-sql-server/tables/#try-out-basic-graphql-requests)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)