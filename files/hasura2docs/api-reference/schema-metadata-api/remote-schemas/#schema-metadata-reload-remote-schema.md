# Schema/Metadata API Reference: Remote Schemas (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

## Introduction​

Add/Remove a remote GraphQL server as Remote Schema in Hasura GraphQL Engine.

## add_remote_schema​

 `add_remote_schema` is used to add a remote GraphQL server as remote
schema. GraphQL Engine stitches it's schema with existing.

An example request as follows:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "add_remote_schema" ,
     "args" :   {
         "name" :   "my remote schema" ,
         "definition" :   {
             "url" :   "https://remote-server.com/graphql" ,
             "headers" :   [ { "name" :   "X-Server-Request-From" ,   "value" :   "Hasura" } ] ,
             "forward_client_headers" :   false ,
             "timeout_seconds" :   60
         } ,
         "comment" :   "some optional comment"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema |
| definition | true | [ RemoteSchemaDef ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemadef) | Definition for the Remote Schema |
| comment | false | Text | comment |


## update_remote_schema​

 `update_remote_schema` is used to update the configuration of a remote
schema. If the Remote Schema URL has changed then it will perform a
introspection as well. After introspection, if there are any
inconsistencies detected with other Metadata objects (like remote
relationships or Remote Schema permissions) they will be reported as *inconsistent_metadata* .

An example request as follows:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "update_remote_schema" ,
     "args" :   {
         "name" :   "my remote schema" ,
         "definition" :   {
             "url" :   "https://remote-server.com/graphql" ,
             "headers" :   [ { "name" :   "X-Server-Request-From" ,   "value" :   "Hasura" } ] ,
             "forward_client_headers" :   false ,
             "timeout_seconds" :   60
         } ,
         "comment" :   "some optional comment"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema |
| definition | true | [ RemoteSchemaDef ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemadef) | Definition for the Remote Schema |
| comment | false | Text | comment |


## remove_remote_schema​

 `remove_remote_schema` is used to delete a Remote Schema. GraphQL Engine
de-stitches it's schema.

An example request as follows:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "remove_remote_schema" ,
     "args" :   {
         "name" :   "my remote schema"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema |


## reload_remote_schema​

 `reload_remote_schema` is used to refresh schema of the remote server.
GraphQL Engine refetches schema from server and stitches.

An example request as follows:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "reload_remote_schema" ,
     "args" :   {
         "name" :   "my remote schema"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-reload-remote-schema/#introduction)
- [ add_remote_schema ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-reload-remote-schema/#schema-metadata-add-remote-schema)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-reload-remote-schema/#schema-metadata-add-remote-schema-syntax)
- [ update_remote_schema ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-reload-remote-schema/#schema-metadata-update-remote-schema)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-reload-remote-schema/#schema-metadata-update-remote-schema-syntax)
- [ remove_remote_schema ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-reload-remote-schema/#schema-metadata-remove-remote-schema)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-reload-remote-schema/#schema-metadata-remove-remote-schema-syntax)
- [ reload_remote_schema ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-reload-remote-schema/#schema-metadata-reload-remote-schema)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-reload-remote-schema/#schema-metadata-reload-remote-schema-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)