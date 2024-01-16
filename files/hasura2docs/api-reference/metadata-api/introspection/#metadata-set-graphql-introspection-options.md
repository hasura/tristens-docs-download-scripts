# Metadata API Reference: GraphQL Introspection Options

## Introduction​

API to set GraphQL introspection options. One of the options is to
disable introspection for the specified roles.

## set_graphql_introspection_options​

 `set_graphql_schema_introspection_options` is used to set graphql
introspection options. Calling this API will replace existing (if any)
introspection options.

This API can be used to disable graphql introspection for the specified roles.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "set_graphql_schema_introspection_options" ,
     "args" :   {
         "disabled_for_roles" :   [
             "guest" ,
             "public"
         ]
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| disabled_for_roles | true | Array of[ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Roles for which GraphQL schema introspection should be disabled *(supported only in cloud/enterprise versions)*  |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/introspection/#metadata-set-graphql-introspection-options/#introduction)
- [ set_graphql_introspection_options ](https://hasura.io/docs/latest/api-reference/metadata-api/introspection/#metadata-set-graphql-introspection-options/#metadata-set-graphql-introspection-options)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/introspection/#metadata-set-graphql-introspection-options/#metadata-set-graphql-schema-introspection-options-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)