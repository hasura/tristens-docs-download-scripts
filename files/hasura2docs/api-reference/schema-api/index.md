# Schema API Reference

## Introduction​

The schema API provides the following features:

1. Execute SQL on the underlying Postgres database, supports schema
modifying actions.


This is primarily intended to be used as an `admin` API to manage the
Hasura schema.

Supported from

The schema API is supported for versions `v2.0.0` and above and replaces
the older[ schema/Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

## Endpoint​

All requests are `POST` requests to the `/v2/query` endpoint.

## Request structure​

```
POST   /v2/query   HTTP/1.1
{
   "type": "<query-type>",
   "args": <args-object>
}
```

### Request body​

[ Query ](https://hasura.io/docs/latest/api-reference/schema-api/index/#schema-query)

#### Query​

| Key | Required | Schema | Description |
|---|---|---|---|
| type | true | String | Type of the query |
| args | true | JSON Value | The arguments to the query |
| version | false | Integer | Version of the API (default: 1) |


## Request types​

The various types of queries are listed in the following table:

| type | args | version | Synopsis |
|---|---|---|---|
|  **bulk**  | [ Query ](https://hasura.io/docs/latest/api-reference/schema-api/index/#schema-query)array | 1 | Execute multiple operations in a single query |
| [ run_sql ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql) | [ run_sql_args ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql-syntax) | 1 | Run SQL directly on Postgres |


## Response structure​

| Status code | Description | Response structure |
|---|---|---|
| 200 | Success | Request specific |
| 400 | Bad request |  `{ "path" : String, "error" : String}`  |
| 401 | Unauthorized |  `{"error" : String}`  |
| 500 | Internal server error |  `{"error" : String}`  |


## Disabling schema API​

Since this API can be used to make changes to the GraphQL schema, it can
be disabled, especially in production deployments.

The `enabled-apis` flag or the `HASURA_GRAPHQL_ENABLED_APIS` env var can
be used to enable/disable this API. By default, the schema/Metadata API
is enabled. To disable it, you need to explicitly state that this API is
not enabled i.e. remove it from the list of enabled APIs.

```
# enable only graphql api, disable Metadata and pgdump
--enabled-apis = "graphql"
HASURA_GRAPHQL_ENABLED_APIS = "graphql"
```

See[ GraphQL Engine server config reference ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/)for info on setting the above flag/env var.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-api/index/#introduction)
- [ Endpoint ](https://hasura.io/docs/latest/api-reference/schema-api/index/#endpoint)
- [ Request structure ](https://hasura.io/docs/latest/api-reference/schema-api/index/#request-structure)
    - [ Request body ](https://hasura.io/docs/latest/api-reference/schema-api/index/#request-body)
- [ Request types ](https://hasura.io/docs/latest/api-reference/schema-api/index/#request-types)
- [ Response structure ](https://hasura.io/docs/latest/api-reference/schema-api/index/#response-structure)
- [ Disabling schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/#disabling-schema-api)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)