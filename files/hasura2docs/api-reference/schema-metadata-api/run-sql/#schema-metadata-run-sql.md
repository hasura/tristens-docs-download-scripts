# Schema/Metadata API Reference: Run SQL (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

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

### Use cases​

1. To execute DDL operations that are not supported by the Console
(e.g. managing indexes).
2. Run custom DML requests from backend microservices instead of
installing libraries to speak to Postgres.


An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
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
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
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
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
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
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
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
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
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

| Key | Required | Schema | Description |
|---|---|---|---|
| sql | true | String | The sql to be executed |
| cascade | false | Boolean | When set to `true` , the effect (if possible) is cascaded to any hasuradb dependent objects (relationships, permissions, templates). |
| check_metadata_consistency | false | Boolean | When set to `false` , the sql is executed without checking Metadata dependencies. |
| read_only | false | Boolean | When set to `true` , the request will be run in `READ ONLY` transaction access mode which means only `select` queries will be successful. This flag ensures that the GraphQL schema is not modified and is hence highly performant. |


### Response​

The response is a JSON Object with the following structure.

| Key | Always present | Schema | Description |
|---|---|---|---|
| result_type | true | String | One of "CommandOk" or "TuplesOk" |
| result | false |  `[[Text]]` (An array of rows, each row an array of columns) | This is present only when the `result_ type` is "TuplesOk" |


Note

The first row in the `result` (when present) will be the names of the columns.

### Some examples​

An SQL query returning results.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "run_sql" ,
     "args" :   {
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
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "run_sql" ,
   "args" :   {
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

- [ run_sql ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/run-sql/#schema-metadata-run-sql/#schema-metadata-run-sql)
    - [ Use cases ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/run-sql/#schema-metadata-run-sql/#use-cases)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/run-sql/#schema-metadata-run-sql/#schema-metadata-run-sql-syntax)

- [ Response ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/run-sql/#schema-metadata-run-sql/#response)

- [ Some examples ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/run-sql/#schema-metadata-run-sql/#some-examples)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)