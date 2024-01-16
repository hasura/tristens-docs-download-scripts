# Schema/Metadata API Reference: Actions (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

## Introduction​

 **actions** are user defined mutations with custom business logic.

## create_action​

 `create_action` is used to define an action. There shouldn't be an
existing action with the same name.

Create a synchronous action with name `create_user` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "create_action" ,
    "args" : {
       "name" : "create_user" ,
       "definition" : {
          "kind" : "synchronous" ,
          "arguments" : [
             {
                "name" : "username" ,
                "type" : "String!"
             } ,
             {
                "name" : "email" ,
                "type" : "String!"
             }
          ] ,
          "output_type" : "User" ,
          "handler" : "https://action.my_app.com/create-user" ,
          "timeout" : 60
       } ,
       "comment" :   "Custom action to create user"
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ ActionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#actionname) | Name of the action |
| definition | true | [ ActionDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#actiondefinition) | Definition of the action |
| comment | false | text | comment |


## drop_action​

 `drop_action` is used to remove an action. Permissions defined on the
Actions are also dropped automatically.

Drop an action `create_user` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "drop_action" ,
    "args" : {
       "name" : "create_user" ,
       "clear_data" :   true
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ ActionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#actionname) | Name of the action |
| clear_data | false | boolean | If set to `true` and action kind is `asynchronous` , related data is deleted from catalog. (default: `true` ) |


## update_action​

 `update_action` is used to update the definition of the action.
Definition thus provided is replaced with existing one.

Update an action `create_user` by making it's kind to `asynchronous` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "update_action" ,
    "args" : {
       "name" : "create_user" ,
       "definition" : {
          "kind" : "asynchronous" ,
          "arguments" : [
             {
                "name" : "username" ,
                "type" : "String!"
             } ,
             {
                "name" : "email" ,
                "type" : "String!"
             }
          ] ,
          "output_type" : "User" ,
          "handler" : "https://action.my_app.com/create-user"
       } ,
       "comment" :   "Custom action to create user" ,
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ ActionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#actionname) | Name of the action |
| definition | true | [ ActionDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#actiondefinition) | Definition of the action to be replaced |
| comment | false | text | comment |


## create_action_permission​

 `create_action_permission` is used to define a permission to make action
visible for a role.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "create_action_permission" ,
   "args" :   {
     "action" :   "create_user" ,
     "role" :   "user"
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| action | true | [ ActionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#actionname) | Name of the action |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the role |
| comment | false | text | comment |


## drop_action_permission​

 `drop_action_permission` is used to drop a permission defined on an action.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "drop_action_permission" ,
   "args" :   {
     "action" :   "create_user" ,
     "role" :   "user"
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ ActionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#actionname) | Name of the action |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the role |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax/#introduction)
- [ create_action ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax/#schema-metadata-create-action)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax/#schema-metadata-create-action-syntax)
- [ drop_action ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax/#schema-metadata-drop-action)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax/#schema-metadata-drop-action-syntax)
- [ update_action ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax/#schema-metadata-update-action)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax/#schema-metadata-update-action-syntax)
- [ create_action_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax/#schema-metadata-create-action-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax/#schema-metadata-create-action-permission-syntax)
- [ drop_action_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax/#schema-metadata-drop-action-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax/#schema-metadata-drop-action-permission-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)