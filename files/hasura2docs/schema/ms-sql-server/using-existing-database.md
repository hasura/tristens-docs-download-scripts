# Set Up a GraphQL Schema Using an Existing MS SQL Server Database

## Introduction​

When you have an existing database with a schema already present, you don't need to create tables or views or run DDL
queries through the Hasura Console.

All you need to do is indicate to Hasura GraphQL Engine which tables and views you want to expose over GraphQL and how
they are connected to each other so that you can query them as a "graph".

## Step 1: Track tables/views​

Tracking a table or a view means telling Hasura GraphQL Engine that you want to expose that table/view over GraphQL.

### To track a table or a view​

- Console
- CLI
- API


1. Head to the `Data -> Schema` section of the Console.
2. Under the heading `Untracked Tables/Views` , click on the `Track` button next to the table/view name.


To track the table and expose it over the GraphQL API, add it to the `tables.yaml` file in the `metadata` directory as
follows:

```
-   table :
     schema :  dbo
     name :  <table name >
```

Apply the Metadata by running:

`hasura metadata apply`

To track a table and expose it over the GraphQL API, use the[ mssql_track_table Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-track-table):

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "mssql_track_table" ,
    "args" :   {
       "source" :   "<db_name>" ,
       "schema" :   "dbo" ,
       "name" :   "<table name>"
    }
}
```

### To track all tables and views present in the database​

- Console
- CLI
- API


1. Head to the `Data -> Schema` section of the Console.
2. Under the heading `Untracked Tables/Views` , click the `Track All` button.


To track all tables and expose them over the GraphQL API, add them to the `tables.yaml` file in the `metadata` directory
as follows:

```
-   table :
     schema :  dbo
     name :  <table - name - 1 >
-   table :
     schema :  dbo
     name :  <table - name - 2 >
```

To automate this, you could add the tables in a loop through a script.

Apply the Metadata by running:

`hasura metadata apply`

To track all tables and expose them over the GraphQL API, use the[ mssql_track_table Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-track-table):

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bulk" ,
   "args" :   [
     {
        "type" :   "mssql_track_table" ,
        "args" :   {
           "source" :   "<db_name>" ,
           "schema" :   "dbo" ,
           "name" :   "<table-name-1>"
        }
     } ,
     {
        "type" :   "mssql_track_table" ,
        "args" :   {
           "source" :   "<db_name>" ,
           "schema" :   "dbo" ,
           "name" :   "<table-name-2>"
        }
     }
   ]
}
```

To automate this, you could add the `mssql_track_table` requests to the `bulk` request in a loop through a script.

## Step 2: Track foreign-keys​

Tracking a foreign-key means creating a[ relationship ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/index/)between the
tables involved in the foreign-key.

### To track a foreign-key between two tables in the database​

- Console
- CLI
- API


1. Head to the `Data -> Schema` section of the Console.
2. Click on a table involved in the foreign-key and head to the `Relationships` tab.
3. You should see a suggested relationship based on the foreign-key. Click `Add` , give a name to your relationship
(this will be the name of the[ nested object ](https://hasura.io/docs/latest/queries/ms-sql-server/nested-object-queries/)in the GraphQL
query), and hit `Save` to create the relationship.
4. Repeat with the other table involved in the foreign-key.


To track a relationship and expose it over the GraphQL API, add it to the `tables.yaml` file in the `metadata` directory
as follows:

 **Object relationship** 

```
-   table :
     schema :  dbo
     name :  <table name >
   object_relationships :
     -   name :  <relationship name >
       using :
         foreign_key_constraint_on :  <reference column >
```

 **Array relationship** 

```
-   table :
       schema :  dbo
       name :  <table name >
    array_relationships :
    -   name :  <relationship name >
       using :
       foreign_key_constraint_on :
          column :  <reference column >
          table :
             schema :  dbo
             name :  <reference table name >
```

Apply the Metadata by running:

`hasura metadata apply`

 **Object relationship** 

You can create an object relationship by using the[ mssql_create_object_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#mssql-create-object-relationship)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "mssql_create_object_relationship" ,
    "args" :   {
       "source" :   "<db_name>" ,
       "table" :   "<table name>" ,
       "name" :   "<relationship name>" ,
       "using" :   {
          "foreign_key_constraint_on" :   "<reference column>"
       }
    }
}
```

 **Array relationship** 

You can create an array relationship by using the[ mssql_create_array_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#mssql-create-array-relationship)metadata
API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "mssql_create_array_relationship" ,
    "args" :   {
       "source" :   "<db_name>" ,
       "table" :   "<table name>" ,
       "name" :   "<relationship name>" ,
       "using" :   {
          "foreign_key_constraint_on"   :   {
             "table"   :   "<reference table name>" ,
             "column"   :   "<reference column>"
          }
       }
    }
}
```

### To track all the foreign-keys of all tables in the database​

- Console
- CLI
- API


1. Head to the `Data -> Schema` section of the Console.
2. Under the heading `Untracked foreign-key relations` , click the `Track All` button to automatically create
relationships based on the foreign-keys.


To track all relationships and expose them over the GraphQL API, add them to the `tables.yaml` file in the `metadata` directory as follows:

 **Object relationship** 

```
-   table :
     schema :  dbo
     name :  <table name >
   object_relationships :
     -   name :  <relationship name >
       using :
         foreign_key_constraint_on :  <reference column >
```

 **Array relationship** 

```
-   table :
     schema :  dbo
     name :  <table name >
   array_relationships :
     -   name :  <relationship name >
       using :
         foreign_key_constraint_on :
           column :  <reference column >
           table :
             schema :  dbo
             name :  <reference table name >
```

To automate this, you could add the relationships in a loop through a script.

Apply the Metadata by running:

`hasura metadata apply`

You can create multiple relationships by using the[ mssql_create_object_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#mssql-create-object-relationship)and
the[ mssql_create_array_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#mssql-create-array-relationship)Metadata APIs:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bulk" ,
   "args" :   [
     {
       "type" :   "mssql_create_object_relationship" ,
       "args" :   {
         "source" :   "<db_name>" ,
         "table" :   "<table name>" ,
         "name" :   "<relationship name>" ,
         "using" :   {
           "foreign_key_constraint_on" :   "<reference column>"
         }
       }
     } ,
     {
       "type" :   "mssql_create_array_relationship" ,
       "args" :   {
         "source" :   "<db_name>" ,
         "table" :   "<table name>" ,
         "name" :   "<relationship name>" ,
         "using" :   {
           "foreign_key_constraint_on"   :   {
             "table"   :   "<reference table name>" ,
             "column"   :   "<reference column>"
           }
         }
       }
     }
   ]
}
```

To automate this, you could add the create relationships requests to the `bulk` request in a loop through a script.

Relationship nomenclature

In this case, Hasura GraphQL Engine will **automatically generate relationship names** (the names of the[ nested objects ](https://hasura.io/docs/latest/queries/ms-sql-server/nested-object-queries/)in the GraphQL query) based on the table names and
the foreign-key names.

The name is generated in the following format:

- For object relationships: `singular of foreignTableName`
- For array relationships: `plural of foreignTableName`


For example, for the foreign-key `article.author_id -> author.id` , the relationship names will be `author` for `article` table and `articles` for `author` table.

In case a field with the generated name already exists, a new name will be generated of the form: `camel case of (singular/plural of foreignTableName + _by_ + foreignKeyColumnName)` 

Note that, **this is just an arbitrary naming convention** chosen by Hasura to ensure the generation of unique
relationship names. You can choose to rename your relationships to anything you wish. You can **change the relationship
names** with a name of your choice as shown in[ MS SQL Server: Renaming relationships ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/rename/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/ms-sql-server/using-existing-database/#introduction)
- [ Step 1: Track tables/views ](https://hasura.io/docs/latest/schema/ms-sql-server/using-existing-database/#step-1-track-tablesviews)
    - [ To track a table or a view ](https://hasura.io/docs/latest/schema/ms-sql-server/using-existing-database/#to-track-a-table-or-a-view)

- [ To track all tables and views present in the database ](https://hasura.io/docs/latest/schema/ms-sql-server/using-existing-database/#to-track-all-tables-and-views-present-in-the-database)
- [ Step 2: Track foreign-keys ](https://hasura.io/docs/latest/schema/ms-sql-server/using-existing-database/#step-2-track-foreign-keys)
    - [ To track a foreign-key between two tables in the database ](https://hasura.io/docs/latest/schema/ms-sql-server/using-existing-database/#to-track-a-foreign-key-between-two-tables-in-the-database)

- [ To track all the foreign-keys of all tables in the database ](https://hasura.io/docs/latest/schema/ms-sql-server/using-existing-database/#to-track-all-the-foreign-keys-of-all-tables-in-the-database)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)