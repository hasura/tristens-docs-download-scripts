# Schema/Metadata API Reference: RESTified GraphQL Endpoints (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

## Introduction​

Add/Remove a RESTified GraphQL endpoint to Hasura GraphQL Engine.

## create_rest_endpoint​

 `create_rest_endpoint` is used to associate a URL template with a query.

An example request as follows:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "create_rest_endpoint" ,
     "args" :   {
         "name" :   "example-name" ,
         "url" :   "example" ,
         "methods" :   [ "POST" , "PUT" , "PATCH" ] ,
         "definition" :   {
             "query" :   {
               "query_name" :   "example_mutation" ,
               "collection_name" :   "test_collection"
             }
         } ,
         "comment" :   "some optional comment"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | Text | A unique identifier for the endpoint |
| url | true | [ EndpointUrl ](https://hasura.io/docs/latest/api-reference/syntax-defs/#endpointurl) | URL of the REST endpoint |
| methods | true | [ EndpointMethods ](https://hasura.io/docs/latest/api-reference/syntax-defs/#endpointmethods) | Non-Empty case sensitive list of supported HTTP Methods |
| definition | true | [ EndpointDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#endpointdef) | Definition for the REST endpoint |
| comment | false | Text | comment |


Supported from

RESTified endpoints are supported from versions `v2.0.0-alpha.1` and
above.

## drop_rest_endpoint​

 `drop_rest_endpoint` is used to delete an existing RESTified GraphQL Endpoint.

An example request as follows:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "drop_rest_endpoint" ,
     "args" :   {
         "name" :   "name_of_the_endpoint"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | Text | URL of the RESTified endpoint |


Supported from

RESTified endpoints are supported from versions `v2.0.0-alpha.1` and above.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/restified-endpoints/#schema-metadata-create-rest-endpoint/#introduction)
- [ create_rest_endpoint ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/restified-endpoints/#schema-metadata-create-rest-endpoint/#schema-metadata-create-rest-endpoint)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/restified-endpoints/#schema-metadata-create-rest-endpoint/#schema-metadata-create-rest-endpoint-syntax)
- [ drop_rest_endpoint ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/restified-endpoints/#schema-metadata-create-rest-endpoint/#schema-metadata-drop-rest-endpoint)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/restified-endpoints/#schema-metadata-create-rest-endpoint/#schema-metadata-drop-rest-endpoint-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)