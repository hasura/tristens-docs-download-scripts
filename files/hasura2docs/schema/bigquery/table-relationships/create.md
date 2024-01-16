# BigQuery: Create Relationships

## Introduction​

A relationship from one table or Native Query to another can be created by defining a link between a column of the table to a column of
the other table.

Typically, relationships are defined using foreign-key constraints. Because BigQuery doesn't support a notion of primary
or foreign keys, we can instead model this relationship using manual object and array relationships.

## Using manual relationships​

Say we created two tables, `authors(id, name)` and `articles(id, title, content, rating, author_id)` .

Let us now connect these tables to enable nested queries using manual relationships.

### Add an object relationship​

Each article has one author. This is an `object relationship` .

- Console
- API


In the Console, select the `articles` table and navigate to the `Relationships` tab, then click `Configure` under `Add a new relationship manually` .

Add an `object relationship` named `author` for the `articles` table as shown here:

Image: [ Create an object relationship ](https://hasura.io/docs/assets/images/bigquery-add-object-rel-step-1-06492b18da6e087081eb0a3145cc1710.png)

Image: [ View object relationships ](https://hasura.io/docs/assets/images/bigquery-add-object-rel-step-2-1c277cbfaa3973e3dd65e253f4d3f172.png)

You can create an object relationship by using the[ bigquery_create_object_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-bq-create-object-relationship)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_create_object_relationship" ,
   "args" :   {
     "source" :   "bigquery" ,
     "table" :   {
       "dataset" :   "<dataset_name>" ,
       "name" :   "articles"
     } ,
     "name" :   "author" ,
     "using" :   {
       "manual_configuration" :   {
         "remote_table" :   {
           "dataset" :   "<dataset_name>" ,
           "name" :   "authors"
         } ,
         "column_mapping" :   {
           "author_id" :   "id"
         }
       }
     }
   }
}
```

If we now click the `API` link along the top navigation bar, we should be able to see `GraphiQL` .

If we run the following query, we can see that we've now added an `author` object relationship under the `bigquery_articles` table:

Note

The query field will be of the format `<dataset_name>_<table_name>` .

### Add an array relationship​

For each author, there are many possible related articles. If we wanted to establish the articles for each author, we
would return an array. We model this in the Hasura Console using an array relationship (we can also think of this as
being a one-to-many relationship between authors and articles).

- Console
- API


In the Console, select the `authors` table and navigate to the `Relationships` tab, then click `Configure` under `Add a new relationship manually` .

Image: [ Add an array relationship ](https://hasura.io/docs/assets/images/bigquery-add-array-rel-step-1-2b8e1bf79eaacf0531c2292964a4c3f6.png)

Image: [ View array relationships in Relationships tab ](https://hasura.io/docs/assets/images/bigquery-add-array-rel-step-2-43ff938b5ae24ea5645842a99044f285.png)

You can create an array relationship by using the[ bigquery_create_array_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-bq-create-array-relationship)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_create_array_relationship" ,
   "args" :   {
     "source" :   "bigquery" ,
     "table" :   {
       "dataset" :   "hasura" ,
       "name" :   "authors"
     } ,
     "name" :   "articles" ,
     "using" :   {
       "manual_configuration" :   {
         "remote_table" :   {
           "dataset" :   "hasura" ,
           "name" :   "articles"
         } ,
         "column_mapping" :   {
           "id" :   "author_id"
         }
       }
     }
   }
}
```

If we now click the `API` link along the top navigation bar, we should be able to see `GraphiQL` .

If we run the following query, we can see that we've now added an `articles` array relationship under the `bigquery_authors` table:

Note

The query field will be of the format `<dataset_name>_<table_name>` .

## Tracking relationships between tables and Native Queries​

As mentioned in the Introduction section above, a relationship from a table to a Native Query can only be set up manually.

- API


Given a table named `articles` and an existing Native Query named `get_author` ,
we can set up a relationship between the two.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bulk" ,
   "args" :   [
     {
       "type" :   "bigquery_create_object_relationship" ,
       "args" :   {
         "source" :   "<db_name>" ,
         "table" :   "articles" ,
         "name" :   "author" ,
         "using" :   {
           "manual_configuration" :   {
             "remote_native_query" :   "get_author" ,
             "column_mapping" :   {
               "id" :   "author_id"
             }
           }
         }
       }
     }
   ]
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/bigquery/table-relationships/create/#introduction)
- [ Using manual relationships ](https://hasura.io/docs/latest/schema/bigquery/table-relationships/create/#bq-create-manual-relationships)
    - [ Add an object relationship ](https://hasura.io/docs/latest/schema/bigquery/table-relationships/create/#add-an-object-relationship)

- [ Add an array relationship ](https://hasura.io/docs/latest/schema/bigquery/table-relationships/create/#add-an-array-relationship)
- [ Tracking relationships between tables and Native Queries ](https://hasura.io/docs/latest/schema/bigquery/table-relationships/create/#tracking-relationships-between-tables-and-native-queries)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)