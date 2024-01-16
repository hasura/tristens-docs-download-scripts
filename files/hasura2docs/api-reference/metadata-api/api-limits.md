# Metadata API Reference: API Limits

## Introduction​

Here's the API to manage[ API Limits ](https://hasura.io/docs/latest/security/api-limits/)related metadata.

## set_api_limits​

You can configure api limits using the `set_api_limits` API.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "set_api_limits" ,
     "args" :   {
         "disabled" :   false ,
         "depth_limit" :   {
             "global" :   5 ,
             "per_role" :   {
                 "myrole" :   3
             }
         } ,
         "node_limit" :   {
             "global" :   5 ,
             "per_role" :   {
                 "myrole" :   3
             }
         } ,
         "time_limit" :   {
             "global" :   5 ,
             "per_role" :   {
                 "myrole" :   3
             }
         } ,
         "batch_limit" :   {
             "global" :   5 ,
             "per_role" :   {
                 "myrole" :   3
             }
         } ,
         "rate_limit" :   {
             "global" :   {
                 "unique_params" :   "IP" ,
                 "max_reqs_per_min" :   100
             } ,
             "per_role" :   {
                 "myrole" :   {
                     "unique_params" :   [ "x-hasura-id" ,   "x-hasura-team-id" ] ,
                     "max_reqs_per_min" :   10
                 }
             }
         }
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| disabled | false | boolean | Default value is false (Limits are enabled by default) |
| depth_limit | false | [ APILimitOption ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apilimitoption) | Restriction based on its depth, preventing deeply nested queries |
| node_limit | false | [ APILimitOption ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apilimitoption) | Restriction based on the number of nodes in GraphQL operation response |
| time_limit | false | [ APILimitOption ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apilimitoption) | Restricts the time that a GraphQL operation is allowed to take. The duration is specified in seconds |
| batch_limit | false | [ APILimitOption ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apilimitoption) | Restricts the number of GraphQL operations in a batched request |
| rate_limit | false | [ RateLimitOption ](https://hasura.io/docs/latest/api-reference/syntax-defs/#ratelimitoption) | Restricts number of GraphQL operations per minute |


In the above metadata spec:

1. The API Limits are enabled by default, i.e the default value of `disabled` is `false`
2. When `disabled` is `false` and none of the API Limits are set then no API limits are applied.
3. The `global` field in all the API Limits is mandatory, and is used as the default API limit if no `per_role` option
is set for the user.
4. The `per_role` can be used to override the `global` API Limit value
5. For `rate_limit` if no `unique_params` are provided then, the requests will be rate-limited on the `role_name` i.e
the `X-HASURA-ROLE` that is used to issue the request


Note

The API will throw a warning if the configured `time_limit` is greater than the Cloud time limit. The Cloud time limit
will be used in such cases.

## remove_api_limits​

You can remove **all** the api limits that have been set using `remove_api_limit` API.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "remove_api_limits"
     "args" :   { }
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/api-limits/#introduction)
- [ set_api_limits ](https://hasura.io/docs/latest/api-reference/metadata-api/api-limits/#metadata-set-api-limits)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/api-limits/#set-api-limits-syntax)
- [ remove_api_limits ](https://hasura.io/docs/latest/api-reference/metadata-api/api-limits/#metadata-remove-api-limits)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)