# Metadata API Reference: Inherited Roles

## Introduction​

Inherited roles allow you to create a role which inherits permissions
from other existing roles.

Supported from

The Metadata API is supported for versions `v2.0.0` and above and
replaces the older[ schema/Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

## add_inherited_role​

 `add_inherited_role` is used to create a new inherited role with other existing roles.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "add_inherited_role" ,
    "args" : {
       "role_name" :   "sample_inherited_role" ,
       "role_set" :   [
          "role1" ,
          "role2"
       ]
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| role_name | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the inherited role |
| role_set | true | [[ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename)] | List of non-inherited roles from which permissions should be inherited |


## drop_inherited_role​

 `drop_inherited_role` is used to delete an existing inherited role.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "drop_inherited_role" ,
     "args"   :   {
        "role_name" :   "sample_inherited_role"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| role_name | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the inherited role |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/inherited-roles/#metadata-add-inherited-role-syntax/#introduction)
- [ add_inherited_role ](https://hasura.io/docs/latest/api-reference/metadata-api/inherited-roles/#metadata-add-inherited-role-syntax/#metadata-add-inherited-role)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/inherited-roles/#metadata-add-inherited-role-syntax/#metadata-add-inherited-role-syntax)
- [ drop_inherited_role ](https://hasura.io/docs/latest/api-reference/metadata-api/inherited-roles/#metadata-add-inherited-role-syntax/#metadata-drop-inherited-role)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/inherited-roles/#metadata-add-inherited-role-syntax/#metadata-drop-inherited-role-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)