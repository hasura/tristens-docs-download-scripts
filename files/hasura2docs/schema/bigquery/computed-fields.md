# BigQuery: Computed Fields

## What are computed fields?​

Computed fields are virtual fields that are dynamically computed and can be queried along with a table's columns.
Computed fields are computed upon request. They are computed by executing user-defined SQL functions using other columns
of the table and other custom inputs if needed.

Note

Computed fields are only exposed over the GraphQL API and the BigQuery database schema is not modified on addition of a
computed field.

### Supported SQL functions​

Currently, only[ table-valued functions ](https://cloud.google.com/bigquery/docs/reference/standard-sql/table-functions),
which return a table, can be added as computed fields. Support for computed fields that return a scalar type is being
tracked in this[ GitHub issue ](https://github.com/hasura/graphql-engine/issues/8521).

#### Creating a table-valued function​

A table-valued function can be created using the[ CREATE TABLE FUNCTION ](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_table_function_statement)SQL statement. BigQuery infers the returning table type based on the `RETURNS TABLE<..>` syntax present in the SQL
statement.

- If `RETURNS TABLE` is included, it specifies the custom schema of the return table as a comma-separated list of column
name and data type pairs. While[ adding such functions as computed fields ](https://hasura.io/docs/latest/schema/bigquery/computed-fields/#bigquery-adding-computed-field), it is not
required to provide `return_table` in the[ definition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#bigquerycomputedfielddefinition)as BigQuery[ provides enough information ](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines#Routine)about the returning table schema to Hasura.Example:
- If `RETURNS TABLE` is absent, BigQuery infers the returning table from the query statement present in the function
body, implicitly. While[ adding such functions as computed fields ](https://hasura.io/docs/latest/schema/bigquery/computed-fields/#bigquery-adding-computed-field), it is required to
provide `return_table` in the[ definition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#bigquerycomputedfielddefinition)as BigQuery
does not provide any information about the returning table to Hasura.Example:


If `RETURNS TABLE` is included, it specifies the custom schema of the return table as a comma-separated list of column
name and data type pairs. While[ adding such functions as computed fields ](https://hasura.io/docs/latest/schema/bigquery/computed-fields/#bigquery-adding-computed-field), it is not
required to provide `return_table` in the[ definition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#bigquerycomputedfielddefinition)as BigQuery[ provides enough information ](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines#Routine)about the returning table schema to Hasura.

Example:

```
CREATE   TABLE   FUNCTION   ` google_project.hasura_test.fetch_articles ` ( a_id INT64 ,  search STRING )
RETURNS   TABLE < id INT64 ,  title STRING ,  content STRING >   AS   (
     (   SELECT  t . id ,  t . title ,  t . content
          FROM  hasura_test . article t
          WHERE  t . author_id  =  a_id  AND   ( t . title  like   ` search `   or  t . content  like   ` search ` )
     )
) ;
```

If `RETURNS TABLE` is absent, BigQuery infers the returning table from the query statement present in the function
body, implicitly. While[ adding such functions as computed fields ](https://hasura.io/docs/latest/schema/bigquery/computed-fields/#bigquery-adding-computed-field), it is required to
provide `return_table` in the[ definition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#bigquerycomputedfielddefinition)as BigQuery
does not provide any information about the returning table to Hasura.

Example:

```
CREATE   TABLE   FUNCTION   ` google_project.hasura_test.fetch_articles ` ( a_id INT64 ,  search STRING )   AS   (
     (   SELECT  t . *
          FROM  hasura_test . article t
          WHERE  t . author_id  =  a_id  AND   ( t . title  like   ` search `   or  t . content  like   ` search ` )
     )
) ;
```

Note

Table functions without `RETURNS TABLE` should return all columns, possibly by using the `*` operator, to avoid any
execution exceptions when a column that is not being returned is included in the selection set of computed field.

## Adding computed fields to a table​

- Console
- CLI
- API


Console support will be added soon.

You can add a computed field by updating the `metadata > databases > [db-name] > tables > [table_name].yaml` file:

```
-   table :
     dataset :  hasura
     name :  authors
   computed_fields :
     -   name :  fetch_articles
       definition :
         function :
           dataset :  hasura
           name :  search_articles
         return_table :
           dataset :  hasura
           name :  articles
         argument_mapping :
           author_id_arg :  author_id
       comment :   ''
```

Apply the Metadata by running:

`hasura metadata apply`

A computed field can be added to a table using the[ bigquery_add_computed_field ](https://hasura.io/docs/latest/api-reference/metadata-api/computed-field/#metadata-bigquery-add-computed-field)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_add_computed_field" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   {
       "name" :   "author" ,
       "dataset" :   "hasura"
     } ,
     "name" :   "fetch_articles" ,
     "definition" :   {
       "function" :   {
         "name" :   "fetch_articles" ,
         "dataset" :   "hasura"
       } ,
       "return_table" :   {
         "name" :   "article" ,
         "dataset" :   "hasura"
       } ,
       "argument_mapping" :   {
         "author_id_arg" :   "author_id"
       }
     }
   }
}
```

## Computed fields permissions​

[ Access control ](https://hasura.io/docs/latest/auth/authorization/index/)to computed fields depends on the presence of the `RETURNS TABLE` clause
in the[ creating computed field ](https://hasura.io/docs/latest/schema/bigquery/computed-fields/#bigquery-create-table-function)SQL statement.

If `RETURNS TABLE` 

- is present, then the function returns a custom table schema. Select permissions are managed through `computed_fields` in the[ permission definition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#selectpermission).
- is absent, then the permissions set on `return_table` are respected.


### What did you think of this doc?

- [ What are computed fields? ](https://hasura.io/docs/latest/schema/bigquery/computed-fields/#what-are-computed-fields)
    - [ Supported SQL functions ](https://hasura.io/docs/latest/schema/bigquery/computed-fields/#supported-sql-functions)
- [ Adding computed fields to a table ](https://hasura.io/docs/latest/schema/bigquery/computed-fields/#bigquery-adding-computed-field)
- [ Computed fields permissions ](https://hasura.io/docs/latest/schema/bigquery/computed-fields/#computed-fields-permissions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)