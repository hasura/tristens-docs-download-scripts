# Schema/Metadata API Reference: Remote Relationships (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

## Introduction​

Remote Relationships allow you to join tables with Remote Schemas.

## create_remote_relationship​

 `create_remote_relationship` is used to create a new remote relationship
with an existing Remote Schema.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "create_remote_relationship" ,
    "args" : {
       "name" :   "sample_remote_relationship" ,
       "table" :   "users" ,
       "hasura_fields" :   [ "id" ] ,
       "remote_schema" :   "my-remote-schema" ,
       "remote_field" :   {
         "messages" :   {
            "arguments" :   {
               "id" : "$id"
            }
         }
       }
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| table | true | [ QualifiedTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#qualifiedtable) | Object with table name and schema |
| hasura_fields | true | [[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgcolumn)|[ ComputedFieldName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#computedfieldname)] | Column/Computed field(s) in the table that is used for joining with Remote Schema field. All join keys in `remote_ field` must appear here. |
| remote_schema | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema to join with |
| remote_field | true | [ RemoteField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remotefield) | The schema tree ending at the field in Remote Schema which needs to be joined with. |


## update_remote_relationship​

 `update_remote_relationship` is used to update an existing remote relationship.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "update_remote_relationship" ,
   "args" :   {
      "name" :   "sample_remote_relationship" ,
      "table" :   "users" ,
      "hasura_fields" :   [ "id" ] ,
      "remote_schema" :   "my-remote-schema" ,
      "remote_field" :   {
        "posts" :   {
           "arguments" :   {
              "id" :   "$id" ,
              "likes" :   {
                 "lte" : "1000"
              }
           }
        }
      }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| table | true | [ QualifiedTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#qualifiedtable) | Object with table name and schema |
| hasura_fields | true | [[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgcolumn)] | Column(s) in the table that is used for joining with Remote Schema field. All join keys in `remote_ field` must appear here. |
| remote_schema | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema to join with |
| remote_field | true | [ RemoteField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remotefield) | The schema tree ending at the field in Remote Schema which needs to be joined with. |


## delete_remote_relationship​

 `delete_remote_relationship` is used to delete an existing remote relationship.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "delete_remote_relationship" ,
     "args"   :   {
        "table" : {
           "name" : "users" ,
           "schema" : "public"
        } ,
        "name" : "sample_remote_relationship"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ QualifiedTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#qualifiedtable) | Object with table name and schema |
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-create-remote-relationship/#introduction)
- [ create_remote_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-create-remote-relationship/#schema-metadata-create-remote-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-create-remote-relationship/#schema-metadata-create-remote-relationship-syntax)
- [ update_remote_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-create-remote-relationship/#schema-metadata-update-remote-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-create-remote-relationship/#schema-metadata-update-remote-relationship-syntax)
- [ delete_remote_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-create-remote-relationship/#schema-metadata-delete-remote-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-create-remote-relationship/#schema-metadata-delete-remote-relationship-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)