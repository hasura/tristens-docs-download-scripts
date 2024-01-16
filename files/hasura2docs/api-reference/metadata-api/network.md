# Metadata API Reference: Network Options (v2.0 and above)

## Introduction​

Here's the API to modify any `Network` metadata. One of the options is
to manage a `TLS allowlist` .

## TLS allow list​

The TLS allow list represents a set of services that are permitted to use
self-signed certificates - primarily intended for use in development and
staging environments, services can be whitelisted by a `host` , and
optionally (service id) `port` .

## add_host_to_tls_allowlist​

 `add_host_to_tls_allowlist` is used to add any string

This API could be supplied with just the hostname in the `args` field of
the request instead of the complete object.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "add_host_to_tls_allowlist" ,
     "args" :   {
         "host" :   "graphql.hasura.io" ,
         "suffix" :   "4183" ,
         "permissions" :   [ "self-signed" ]
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| host | true |  `String`  | the hostname/domain of the endpoint |
| suffix | false |  `String`  | suffix for the service (this is usually reserved for the service port number) |
| permissions | false |  `[String]`  | Can be only `["self-signed"]` until more permissions are supported. "self-signed" allows self-signed, name mismatches, and non-X509.V3 certificates. |


## drop_host_from_tls_allowlist​

 `drop_host_from_tls_allowlist` is used to drop an endpoint from the TLS allow list.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "drop_host_from_tls_allowlist" ,
     "args" :   {
         "host" :   "graphql.hasura.io" ,
         "suffix" :   "4183"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| host | true |  `String`  | the hostname/domain of the endpoint that was previously added to the allow list |
| suffix | false |  `String`  | suffix for the service (this is usually reserved for the service port number) |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/network/#introduction)
- [ TLS allow list ](https://hasura.io/docs/latest/api-reference/metadata-api/network/#tls-allow-list)
- [ add_host_to_tls_allowlist ](https://hasura.io/docs/latest/api-reference/metadata-api/network/#metadata-add-host-to-tls-allowlist)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/network/#add-host-to-tls-allowlist-syntax)
- [ drop_host_from_tls_allowlist ](https://hasura.io/docs/latest/api-reference/metadata-api/network/#metadata-drop-host-from-tls-allowlist)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/network/#drop-host-from-tls-allowlist-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)