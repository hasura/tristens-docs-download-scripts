# Health Check API Reference

## Introduction​

The Health API is a public endpoint which gives info on the server
health.

## Endpoint​

All requests are `GET` requests to the `/healthz` endpoint. There's also `/hasura/healthz` available as an alternative, which mirrors `/healthz` completely.

## API Spec​

### Request​

`GET   /healthz?strict=false   HTTP/1.1`

#### Parameters​

| Name | Required | type | Description |
|---|---|---|---|
| strict | false | boolean | If set to `true` , response returns `500` if inconsistent objects exist (default: `false` ) |


### Response​

Depending on the server health status any of the following responses can
be returned:

| Server condition | strict parameter | HTTP Status | Message |
|---|---|---|---|
| All healthy | Any | 200 | OK |
| Serving requests but some Metadata objects are inconsistent/not-available |  `false`  | 200 | WARN: inconsistent objects in schema |
| Serving requests but some Metadata objects are inconsistent/not-available |  `true`  | 500 | ERROR: inconsistent objects in schema |
| Unhealthy | Any | 500 | ERROR |


Note

If there are Metadata inconsistencies, you should use the Hasura Console
or the[ get_inconsistent_metadata ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-get-inconsistent-metadata)Metadata API to find out
what the inconsistent objects are and resolve them.

#### Sample response​

`HTTP/1.1   200   OK`

## Disabling Health Check API​

The `healthz` API endpoint is public and cannot be disabled.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/health/#introduction)
- [ Endpoint ](https://hasura.io/docs/latest/api-reference/health/#endpoint)
- [ API Spec ](https://hasura.io/docs/latest/api-reference/health/#api-spec)
    - [ Request ](https://hasura.io/docs/latest/api-reference/health/#request)

- [ Response ](https://hasura.io/docs/latest/api-reference/health/#response)
- [ Disabling Health Check API ](https://hasura.io/docs/latest/api-reference/health/#disabling-health-check-api)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)