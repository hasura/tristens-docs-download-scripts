# Metadata API Reference: Custom Functions

## Introduction​

Track/untrack a custom SQL function in the Hasura GraphQL Engine.

Only tracked custom functions are available for
querying/mutating/subscribing data over the GraphQL API.

Supported from

The Metadata API is supported for versions `v2.0.0` and above and
replaces the older[ schema/Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

## pg_track_function​

 `pg_track_function` is used to add a custom SQL function to the GraphQL
schema. It supports more configuration options than v1, and also
supports tracking custom functions as mutations. Also refer a note[ here ](https://hasura.io/docs/latest/api-reference/syntax-defs/#function-req-note).

Track an SQL function called `search_articles` with a Hasura session argument:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_track_function" ,
     "args" :   {
         "source" :   "default" ,
         "function" :   {
             "schema" :   "public" ,
             "name" :   "search_articles"
         } ,
         "configuration" :   {
             "session_argument" :   "hasura_session"
         } ,
         "comment" :   "This function helps search for articles"
     }
}
```

Track `VOLATILE` SQL function `reset_widget` as a mutation, so it
appears as a top-level field under the `mutation` root field:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_track_function" ,
     "args" :   {
         "function" :   {
             "schema" :   "public" ,
             "name" :   "reset_widget"
         } ,
         "configuration" :   {
             "exposed_as" :   "mutation"
         } ,
         "source" :   "default"
     }
}
```

If `exposed_as` is omitted, the location in the schema to expose the
function will be inferred from the function's volatility, with `VOLATILE` functions appearing under the `mutation` root, and others
ending up under `query/subscription` .

In most cases you will want `VOLATILE` functions to only be exposed as
mutations, and only `STABLE` and `IMMUTABLE` functions to be queries.
When tracking `VOLATILE` functions under the `query` root, the user
needs to guarantee that the field is idempotent and side-effect free, in
the context of the resulting GraphQL API.

One such use case might be a function that wraps a simple query and
performs some logging visible only to administrators.

Note

It's easy to accidentally give an SQL function the wrong volatility (or
for a function to end up with `VOLATILE` mistakenly, since it's the
default).

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| function | true | [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#functionname) | Name of the SQL function |
| configuration | false | [ Function Configuration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#function-configuration) | Configuration for the SQL function |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the function (default: `default` ) |
| comment | false | String | Comment for the function. This comment would replace the auto-generated comment for the function field in the GraphQL schema. |


## pg_untrack_function​

 `pg_untrack_function` is used to remove a SQL function from the GraphQL schema.

Remove an SQL function `search_articles` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_untrack_function" ,
     "args" :   {
         "function" :   {
            "schema" :   "public" ,
            "name" :   "search_articles"
         } ,
         "source" :   "default"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| function | true | [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#functionname) | Name of the SQL function |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the function (default: `default` ) |


## pg_set_function_customization​

 `pg_set_function_customization` allows you to customize any given
function with a custom name and custom root fields of an already tracked
function. This will **replace** the already present customization.

Set the configuration for a function called `search_articles` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "pg_set_function_customization" ,
    "args" :   {
      "function" :   "search_articles" ,
      "source" :   "default" ,
      "configuration" :   {
        "custom_root_fields" :   {
          "function" :   "FindArticles" ,
          "function_aggregate" :   "FindArticlesAgg"
        }
      }
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| function | true | [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#functionname) | Name of the function |
| configuration | false | [ Function Configuration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#function-configuration) | Configuration for the function |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the function (default: `default` ) |


## pg_create_function_permission​

 `pg_create_function_permission` is used to add permission to an existing
custom function. To add a function permission, the provided role should
have select permissions to the target table of the function.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_create_function_permission" ,
     "args" :   {
        "function" :   "get_articles" ,
        "source" :   "default" ,
        "role" :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| function | true | [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#functionname) | Name of the SQL function |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the role |
| source | false | Text | Name of the source database of the function (default: `default` ) |


## pg_drop_function_permission​

 `pg_drop_function_permission` is used to drop an existing function permission.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_drop_function_permission" ,
     "args" :   {
        "function" :   "get_articles" ,
        "role" :   "user" ,
        "source" :   "default"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| function | true | [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#functionname) | Name of the SQL function |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the role |
| source | false | Text | Name of the source database of the function (default: `default` ) |


## snowflake_track_function​

 `snowflake_track_function` is used to add a custom SQL function to the GraphQL
schema. Also refer a note[ here ](https://hasura.io/docs/latest/api-reference/syntax-defs/#function-req-note).

Track an SQL function called `search_articles` with a return table of `articles` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "snowflake_track_function" ,
     "args" :   {
         "function" :   [ "search_articles" ] ,
         "source" :   "default" ,
         "configuration" :   {
             "response" :   {
                 "type" :   "table" ,
                 "table" :   [ "articles" ]
             }
         }
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| function | true | [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#functionname) | Name of the SQL function |
| source | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the function |
| configuration | true | [ Function Configuration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#function-configuration) | Configuration for the SQL function |


## snowflake_untrack_function​

 `snowflake_untrack_function` is used to remove a SQL function from the GraphQL schema.

Remove an SQL function `search_articles` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "snowflake_untrack_function" ,
     "args" :   {
         "function" :   [ "search_articles" ] ,
         "source" :   "default"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| function | true | [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#functionname) | Name of the SQL function |
| source | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the function |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#introduction)
- [ pg_track_function ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-pg-track-function)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-pg-track-function-syntax)
- [ pg_untrack_function ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-pg-untrack-function)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-pg-untrack-function-syntax)
- [ pg_set_function_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-pg-set-function-customization)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-pg-set-function-customization-syntax)
- [ pg_create_function_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-pg-create-function-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-pg-create-function-permission-syntax)
- [ pg_drop_function_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-pg-drop-function-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-pg-drop-function-permission-syntax)
- [ snowflake_track_function ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-snowflake-track-function)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-snowflake-track-function-syntax)
- [ snowflake_untrack_function ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-snowflake-untrack-function)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-functions/#metadata-pg-track-function-syntax/#metadata-snowflake-untrack-function-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)