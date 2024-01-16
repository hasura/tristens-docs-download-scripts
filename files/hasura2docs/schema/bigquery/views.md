# BigQuery: Extend Schema with Views

## What are views?​

[ Views ](https://cloud.google.com/bigquery/docs/views)can be used to expose the results of a custom query as a virtual table. Views are not persisted physically
i.e. the query defining a view is executed whenever data is requested from the view.

Hasura GraphQL Engine lets you expose views over the GraphQL API to allow querying them using both `queries` and `subscriptions` just like regular tables.

## Creating views​

- Console
- CLI
- API


Views can be created using SQL which can be run in the Hasura Console:

- Head to the `Data -> SQL` section of the Hasura Console
- Enter your[ create view SQL statement ](https://cloud.google.com/bigquery/docs/views)
- Hit the `Run` button


1. [ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add
your[ create view SQL statement ](https://cloud.google.com/bigquery/docs/views)to the `up.sql` file. Also, add an SQL statement to the `down.sql` file that
reverts the previous statement.
2. Apply the Migration and Metadata by running:


[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add
your[ create view SQL statement ](https://cloud.google.com/bigquery/docs/views)to the `up.sql` file. Also, add an SQL statement to the `down.sql` file that
reverts the previous statement.

Apply the Migration and Metadata by running:

`hasura migrate apply`

You can add a view by using the `bigquery_run_sql` schema API:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_run_sql" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "sql" :   "<create view statement>"
   }
}
```

## Tracking views​

Views can be present in the underlying BigQuery database without being exposed over the GraphQL API. In order to expose
a view over the GraphQL API, it needs to be **tracked** .

- Console
- CLI
- API


While creating views from the `Data -> SQL` page, selecting the `Track this` checkbox will expose the new view over the
GraphQL API right after creation.

You can track any existing views in your database from the `Data -> Schema` page:

Image: [ Track views ](data:image/png;base64,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)

1. To track the view and expose it over the GraphQL API, edit the `tables.yaml` file in the `metadata` directory as
follows:
2. Apply the Metadata by running:


To track the view and expose it over the GraphQL API, edit the `tables.yaml` file in the `metadata` directory as
follows:

```
-   table :
     dataset :  my_data
     name :  author
-   table :
     dataset :  my_data
     name :  article
-   table :
     dataset :  my_data
     name :  <name of view >
```

Apply the Metadata by running:

`hasura metadata apply`

To track the view and expose it over the GraphQL API, make the following API call to the[ bigquery_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-bigquery-track-table)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "bigquery_track_table" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "dataset" :   "my_data" ,
     "name" :   "<name of view>"
   }
}
```

## Use cases​

Views are ideal solutions for retrieving some derived data based on some custom business logic.

Let's look at a few example use cases for views:

### Example: Group by and then aggregate​

Sometimes we might want to fetch some data derived by aggregating (avg, min, max, etc.) over a group of rows in a table.

Let’s say we want to fetch the average article rating for each author in the following schema:

```
my_data . author ( id  integer ,  name string ,  city string ,  email string ,  phone string ,  address string )
my_data . article ( id  integer ,  title string ,  content string ,  rating  integer ,  author_id  integer )
```

A view that averages the rating of articles for each author can be created using the following SQL query:

```
CREATE   VIEW  my_data . author_average_rating  AS   (
   SELECT  author_id ,   avg ( rating )  avg_rating
     FROM  my_data . article
     GROUP   BY  author_id
)
```

### Example: Hide certain fields of a table​

Sometimes we might have some sensitive information in a table which we wouldn't want to expose.

Let's say, we want to expose the following `author` table without the fields `email` , `phone` and `address` :

`author ( id  integer ,  name string ,  city string ,  email string ,  phone string ,  address string )`

A view that only exposes the non-sensitive fields of the `author` table can be created using the following SQL query:

```
CREATE   VIEW  my_data . author_public  AS   (
   SELECT  id ,  name ,  city
     FROM  author
)
```

### What did you think of this doc?

- [ What are views? ](https://hasura.io/docs/latest/schema/bigquery/views/#what-are-views)
- [ Creating views ](https://hasura.io/docs/latest/schema/bigquery/views/#bigquery-create-views)
- [ Tracking views ](https://hasura.io/docs/latest/schema/bigquery/views/#tracking-views)
- [ Use cases ](https://hasura.io/docs/latest/schema/bigquery/views/#use-cases)
    - [ Example: Group by and then aggregate ](https://hasura.io/docs/latest/schema/bigquery/views/#example-group-by-and-then-aggregate)

- [ Example: Hide certain fields of a table ](https://hasura.io/docs/latest/schema/bigquery/views/#example-hide-certain-fields-of-a-table)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)