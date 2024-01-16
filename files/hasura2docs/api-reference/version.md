# Version API Reference

## Introduction​

The `/v1/version` is a public endpoint that responds with the server
type and current server version in JSON format.

## Endpoint​

All requests are `GET` requests to the `/v1/version` endpoint.

## API Spec​

### Request​

`GET   /v1/version   HTTP/1.1`

### Sample response​

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
   "server_type" :   "ce" ,
   "version" :   "v1.0.0-alpha01"
}
```

## Disabling Version API​

The `version` API endpoint is public and cannot be disabled.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/version/#introduction)
- [ Endpoint ](https://hasura.io/docs/latest/api-reference/version/#endpoint)
- [ API Spec ](https://hasura.io/docs/latest/api-reference/version/#api-spec)
    - [ Request ](https://hasura.io/docs/latest/api-reference/version/#request)

- [ Sample response ](https://hasura.io/docs/latest/api-reference/version/#sample-response)
- [ Disabling Version API ](https://hasura.io/docs/latest/api-reference/version/#disabling-version-api)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)