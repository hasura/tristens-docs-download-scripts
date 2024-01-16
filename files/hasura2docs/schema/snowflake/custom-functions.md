# Snowflake: Extend Schema with User-defined Functions

Supported from

Snowflake UDFs are supported from v2.26.0.

## What are user-defined functions?​

[ User-defined functions ](https://docs.snowflake.com/en/sql-reference/udf-overview)(UDFs) are custom functions that can
be used to either encapsulate some custom business logic or extend the built-in SQL functions and operators.

Hasura GraphQL Engine lets you expose certain types of custom functions as top-level fields in the GraphQL API to allow
querying them.

### Supported functions​

Currently, only functions which satisfy the following constraints can be exposed as top level fields in the GraphQL API:

- The function must return rows in the format of an **existing tracked table** in the schema.


## Creating functions​

Functions can be created the Snowflake UI. See the[ Snowflake docs ](https://quickstarts.snowflake.com/guide/getting_started_with_user_defined_sql_functions/?index=..%2F..index#0)for details.

## Track functions​

Functions can be present in the underlying Snowflake database without being exposed over the GraphQL API. In order to
expose a function over the GraphQL API, it needs to be **tracked** .

- Console
- API


You can track any existing supported functions in your database from the `Data -> Manage` page.

Image: [ Track functions ](https://hasura.io/docs/assets/images/snowflake-function-track-5cd1733cbc834be0167fa64fe3f0947b.png)

Click `Track as Root Field` and select the return table.

Image: [ Select function return table ](https://hasura.io/docs/assets/images/snowflake-function-select-table-13a8bea93b8e7fc4f3b47b1b340dd3ae.png)

To track the function and expose it over the GraphQL API, make the following API call to the[ snowflake_track_function ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-snowflake-track-function)Metadata
API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "snowflake_track_function" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "schema" :   "public" ,
     "name" :   [ "name" ,   "of" ,   "function" ] ,
     "configuration" :   {
       "response" :   { "type" :   "table" ,   "table" :  TABLE_NAME }
     }
   }
}
```

Note

Snowflake doesn't currently support direct reference of tables in the return type of function definitions. To accomadate
for this, Hasura currently requires that the response be specified in metadata.

## Use cases​

Custom functions are ideal solutions for retrieving some derived data based on some custom business logic that requires
user input to be calculated based on inputs. If your custom logic does not require any user input, you can use[ views ](https://hasura.io/docs/latest/schema/postgres/views/)instead.

## Querying custom functions using GraphQL queries​

### Using arguments with custom functions​

As with tables, arguments like `where` , `limit` , `order_by` , `offset` , etc. are also available for use with
function-based queries.

 **For example** , limit the number of articles returned by the function defined in the text-search example above:

```
query   {
   search_articles ( args :   {   search :   "hasura"   } ,   limit :   5 )   {
     id
     title
     content
   }
}
```

### What did you think of this doc?

- [ What are user-defined functions? ](https://hasura.io/docs/latest/schema/snowflake/custom-functions/#what-are-user-defined-functions)
    - [ Supported functions ](https://hasura.io/docs/latest/schema/snowflake/custom-functions/#snowflake-supported-sql-functions)
- [ Creating functions ](https://hasura.io/docs/latest/schema/snowflake/custom-functions/#snowflake-create-sql-functions)
- [ Track functions ](https://hasura.io/docs/latest/schema/snowflake/custom-functions/#snowflake-track-custom-sql-functions)
- [ Use cases ](https://hasura.io/docs/latest/schema/snowflake/custom-functions/#use-cases)
- [ Querying custom functions using GraphQL queries ](https://hasura.io/docs/latest/schema/snowflake/custom-functions/#querying-custom-functions-using-graphql-queries)
    - [ Using arguments with custom functions ](https://hasura.io/docs/latest/schema/snowflake/custom-functions/#using-arguments-with-custom-functions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)