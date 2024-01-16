# Metadata API Reference: Custom Types

## Introduction​

 **Custom Types** are user-defined GraphQL types which help to define[ Actions ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/).

Supported from

The Metadata API is supported for versions `v2.0.0` and above and
replaces the older[ schema/Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

## set_custom_types​

 `set_custom_types` is used to set user-defined GraphQL types. This API
will replace the given types with existing ones.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "set_custom_types" ,
   "args" :   {
     "scalars" :   [ ] ,
     "enums" :   [ ] ,
     "input_objects" :   [
       {
         "name" :   "User" ,
         "fields" :   [
           {
             "name" :   "username" ,
             "type" :   "String!"
           } ,
           {
             "name" :   "password" ,
             "type" :   "String!"
           }
         ]
       }
     ] ,
     "objects" :   [
       {
         "name" :   "UserId" ,
         "fields" :   [
           {
             "name" :   "id" ,
             "type" :   "Int!"
           }
         ] ,
         "relationships" :   [
           {
             "name" :   "posts" ,
             "type" :   "array" ,
             "remote_table" :   "post" ,
             "field_mapping" :   {
               "id" :   "user_id"
             }
           }
         ]
       }
     ]
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| input_objects | false | Array of[ InputObjectType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#inputobjecttype) | Set of GraphQL `Input Object`  |
| objects | false | Array of[ ObjectType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#objecttype) | Set of GraphQL `Object`  |
| scalars | false | Array of[ ScalarType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#scalartype) | Set of GraphQL `Scalar`  |
| enums | false | Array of[ EnumType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#enumtype) | Set of GraphQL `Enum`  |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-types/#introduction)
- [ set_custom_types ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-types/#metadata-set-custom-types)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-types/#metadata-set-custom-types-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)