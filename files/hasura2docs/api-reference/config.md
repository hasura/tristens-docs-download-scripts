# Config API Reference

## Introduction​

The Config API is an admin only endpoint which gives info on the server configuration.

## Endpoint​

All requests are `GET` requests to the `/v1alpha1/config` endpoint.

## API Spec​

### Request​

```
GET   /v1alpha1/config   HTTP/1.1
X-Hasura-Role :   admin
```

### Sample response​

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
   "version" :   "v1.0.0-beta.3" ,
   "is_function_permissions_inferred" :   true ,
   "is_remote_schema_permissions_enabled" :   false ,
   "is_admin_secret_set" :   true ,
   "is_auth_hook_set" :   false ,
   "is_jwt_set" :   true ,
   "jwt" :   {
     "claims_namespace" :   "https://hasura.io/jwt/claims" ,
     "claims_format" :   "json"
   } ,
   "is_allow_list_enabled" :   false ,
   "live_queries" :   {
     "batch_size" :   100 ,
     "refetch_delay" :   1
   }
}
```

## Disabling Config API​

The `enabled-apis` flag or the `HASURA_GRAPHQL_ENABLED_APIS` env var can
be used to enable/disable this API. By default, this API is enabled. To
disable it, you need to explicitly state that this API is not enabled.
i.e. remove it from the list of enabled APIs.

```
# enable only graphql & Metadata apis, disable config
--enabled-apis = "graphql,metadata"
HASURA_GRAPHQL_ENABLED_APIS = "graphql,metadata"
```

See[ GraphQL Engine server config reference ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/)for info on setting the above flag/env var.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/config/#introduction)
- [ Endpoint ](https://hasura.io/docs/latest/api-reference/config/#endpoint)
- [ API Spec ](https://hasura.io/docs/latest/api-reference/config/#api-spec)
    - [ Request ](https://hasura.io/docs/latest/api-reference/config/#request)

- [ Sample response ](https://hasura.io/docs/latest/api-reference/config/#sample-response)
- [ Disabling Config API ](https://hasura.io/docs/latest/api-reference/config/#disabling-config-api)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)