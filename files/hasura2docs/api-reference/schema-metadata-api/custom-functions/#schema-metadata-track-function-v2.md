# Schema/Metadata API Reference: Custom Functions (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

## Introduction​

Track/untrack a custom SQL function in the Hasura GraphQL Engine.

Only tracked custom functions are available for
querying/mutating/subscribing data over the GraphQL API.

## track_function​

 `track_function` is used to add a custom SQL function to the `query` root field of the GraphQL schema. Also refer a note[ here ](https://hasura.io/docs/latest/api-reference/syntax-defs/#function-req-note).

Add an SQL function `search_articles` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "track_function" ,
     "args" :   {
         "schema" :   "public" ,
         "name" :   "search_articles"
     }
}
```

## track_function v2​

Version 2 of `track_function` is used to add a custom SQL function to
the GraphQL schema. It supports more configuration options than v1, and
also supports tracking functions as mutations. Also refer a note[ here ](https://hasura.io/docs/latest/api-reference/syntax-defs/#function-req-note).

Track an SQL function called `search_articles` with a Hasura session
argument:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "track_function" ,
     "version" :   2 ,
     "args" :   {
         "function" :   {
             "schema" :   "public" ,
             "name" :   "search_articles"
         } ,
         "configuration" :   {
             "session_argument" :   "hasura_session"
         }
     }
}
```

Track `VOLATILE` SQL function `reset_widget` as a mutation, so it
appears as a top-level field under the `mutation` root field:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "track_function" ,
     "version" :   2 ,
     "args" :   {
         "function" :   {
             "schema" :   "public" ,
             "name" :   "reset_widget"
         } ,
         "configuration" :   {
             "exposed_as" :   "mutation"
         }
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


## untrack_function​

 `untrack_function` is used to remove a SQL function from the GraphQL
schema.

Remove an SQL function `search_articles` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "untrack_function" ,
     "args" :   {
         "schema" :   "public" ,
         "name" :   "search_articles"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#functionname) | Name of the SQL function |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-functions/#schema-metadata-track-function-v2/#introduction)
- [ track_function ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-functions/#schema-metadata-track-function-v2/#schema-metadata-track-function)
- [ track_function v2 ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-functions/#schema-metadata-track-function-v2/#schema-metadata-track-function-v2)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-functions/#schema-metadata-track-function-v2/#schema-metadata-track-function-syntax-v2)
- [ untrack_function ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-functions/#schema-metadata-track-function-v2/#schema-metadata-untrack-function)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-functions/#schema-metadata-track-function-v2/#schema-metadata-untrack-function-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)