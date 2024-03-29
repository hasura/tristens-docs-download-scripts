# Schema API Reference: Run SQL (v2.0 and above)

## run_sql​

 `run_sql` can be used to run arbitrary SQL statements.

Multiple SQL statements can be separated by a `;` , however, only the
result of the last SQL statement will be returned.

Admin-only

This is an admin-only request, i.e. the request can only be executed
with `X-Hasura-Role: admin` . This can be set by passing `X-Hasura-Admin-Secret` or by setting the right role in webhook/JWT
authorization mode.

This is deliberate as it is hard to enforce any sort of permissions on
arbitrary SQL. If you find yourself in the need of using `run_sql` to
run custom DML requests, consider creating a view. You can now define
permissions on that particular view for various roles.

Supported from

The schema API is supported for versions `v2.0.0` and above and replaces
the older[ schema/Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

### Supported databases​

 `run_sql` can be invoked on most supported databases, but typically it requires
a prefix corresponding to that database.

In order to use it, you will need to specify the correct `type` in the query, as
below:

| Database | type parameter |
|---|---|
| Postgres |  `"run_ sql"` or `"pg_ run_ sql"`  |
| MS SQL Server |  `"mssql_ run_ sql"`  |
| Citus |  `"citus_ run_ sql"`  |
| CockroachDB |  `"cockroach_ run_ sql"`  |
| BigQuery |  `"bigquery_ run_ sql"`  |


When using a data connector, use the connector's prefix.

All examples below will use the Postgres `type` parameter, `"run_sql"` .

### Use cases​

1. To execute DDL operations that are not supported by the Console
(e.g. managing indexes).
2. Run custom DML requests from backend microservices instead of
installing libraries to speak to Postgres.


An example:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
         "source" :   "default" ,
         "sql" :   "CREATE UNIQUE INDEX ON films (title);"
     }
}
```

While `run_sql` lets you run any SQL, it tries to ensure that the Hasura
GraphQL Engine's state (relationships, permissions etc.) is consistent
i.e. you cannot drop a column on which any Metadata is dependent on (say
a permission or a relationship). The effects, however, can be cascaded.

Example: If we were to drop the 'bio' column from the author table
(let's say the column is used in some permission), you would see an
error.

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
         "source" :   "default" ,
         "sql" :   "ALTER TABLE author DROP COLUMN name"
     }
}
```

```
HTTP/1.1   400   BAD REQUEST
Content-Type :   application/json
{
     "path" :   "$.args" ,
     "error" :   "cannot drop due to the following dependent objects: permission author.user.select"
}
```

We can however, cascade these changes.

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
         "source" :   "default" ,
         "sql" :   "ALTER TABLE author DROP COLUMN bio" ,
         "cascade"   :   true
     }
}
```

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "result_type" :   "CommandOk"
}
```

With the above request, the dependent permission is also dropped.

Example: If we were to drop a foreign key constraint from the article
table (let's say the column involved in the foreign key is used to
define a relationship), you would see an error.

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
         "source" :   "default" ,
         "sql" :   "ALTER TABLE article DROP CONSTRAINT article_author_id_fkey"
     }
}
```

```
HTTP/1.1   400   BAD REQUEST
Content-Type :   application/json
{
     "path" :   "$.args" ,
     "error" :   "cannot drop due to the following dependent objects: constraint article.article_author_id_fkey"
}
```

We can however, cascade these changes.

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
         "source" :   "default" ,
         "sql" :   "ALTER TABLE article DROP CONSTRAINT article_author_id_fkey" ,
         "cascade"   :   true
     }
}
```

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "result_type" :   "CommandOk"
}
```

With the above request, the dependent permission is also dropped.

In general, the SQL operations that will affect Hasura Metadata are:

1. Dropping columns
2. Dropping tables
3. Dropping foreign keys
4. Altering types of columns
5. Dropping SQL functions
6. Overloading SQL functions


In case of 1, 2 and 3 the dependent objects (if any) can be dropped
using `cascade` . However, when altering type of columns, if any objects
are affected, the change cannot be cascaded. So, those dependent objects
have to be manually dropped before executing the SQL statement. Dropping
SQL functions will cascade the functions in Metadata even without using `cascade` since no other objects depend on them. Overloading tracked SQL
functions is not allowed.

Set `check_metadata_consistency` field to `false` to force the server to
not consider Metadata dependencies.

### Args syntax​

| Key | Required | Supported databases | Schema | Description |
|---|---|---|---|---|
|  `sql`  | true |  *all*  | String | The sql to be executed |
|  `source`  | false |  *all*  | String | The database on which the sql is to be executed (default: 'default' database) |
|  `cascade`  | false | Postgres and MS SQL Server | Boolean | When set to `true` , the effect (if possible) is cascaded to any hasuradb dependent objects (relationships, permissions, templates). |
|  `check_ metadata_ consistency`  | false | Postgres and MS SQL Server | Boolean | When set to `false` , the sql is executed without checking Metadata dependencies. |
|  `read_ only`  | false | Postgres | Boolean | When set to `true` , the request will be run in `READ ONLY` transaction access mode which means only `select` queries will be successful. This flag ensures that the GraphQL schema is not modified and is hence highly performant. |


### Response​

The response is a JSON Object with the following structure.

| Key | Always present | Schema | Description |
|---|---|---|---|
| result_type | true | String | One of "CommandOk" or "TuplesOk" |
| result | false |  `[[Text]]` (An array of rows, each row an array of columns) | This is present only when the `result_ type` is "TuplesOk" |


Note

The first row in the `result` (when present) will be the names of the
columns.

### Some examples​

An SQL query returning results.

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
         "source" :   "default" ,
         "sql" :   "select user_id, first_name from author limit 2;"
     }
}
```

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "result_type" :   "TuplesOk" ,
     "result" :   [
         [
             "user_id" ,
             "first_name"
         ] ,
         [
             "1" ,
             "andre"
         ] ,
         [
             "2" ,
             "angela"
         ]
     ]
}
```

An SQL query to create a table:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "run_sql" ,
   "args" :   {
     "source" :   "default" ,
     "sql" :   "create table item ( id serial,  name text,  category text,  primary key (id))" ,
     "check_metadata_consistency" :   false
   }
}
```

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
   "result_type" :   "CommandOk" ,
   "result" :   null
}
```

### What did you think of this doc?

- [ run_sql ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql-syntax/#schema-run-sql)
    - [ Supported databases ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql-syntax/#supported-databases)

- [ Use cases ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql-syntax/#use-cases)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql-syntax/#schema-run-sql-syntax)

- [ Response ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql-syntax/#response)

- [ Some examples ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql-syntax/#some-examples)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)