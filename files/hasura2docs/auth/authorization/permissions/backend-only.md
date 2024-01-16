# Backend Only Mutations

## Introduction​

If a mutation permission is marked as "backend only", it is accessible to the given role only if the `x-hasura-use-backend-only-permissions` session variable exists on the request and is set to `true` . The `x-hasura-admin-secret` must also be present if any auth is configured.

This is useful if you would like to hide a mutation from a public facing API but allow access to it via a trusted
backend.

Setting "backend only" is available for `insert` , `update` and `delete` mutations.

- Console
- CLI
- API


You can set a mutate permission for a role as backend only in the Hasura Console in **Data -> [table] -> Permissions ->
[role] -> insert / update / delete -> Backend only ** 

Image: [ Allow backends only in Hasura Console ](https://hasura.io/docs/assets/images/allow-backends-only_console_2.10.1-0b5a145df85d5baa5b727c8bb9b1d5aa.png)

You can set a mutate permission for a role as backend only in the `metadata -> databases -> [database-name] -> tables ->
[table-name].yaml` file, eg: `public_users.yaml` :

```
table :
   name :  users
   schema :  public
insert_permissions :
   -   role :  user
     permission :
       check :   { }
       columns :
         -  id
       backend_only :   true
delete_permissions :
   -   role :  user
     permission :
       backend_only :   true
       filter :   { }
```

You can set a mutate permission for a role as backend only with the Metadata API and the[ insert ](https://hasura.io/docs/latest/api-reference/syntax-defs/#insertpermission),[ update ](https://hasura.io/docs/latest/api-reference/syntax-defs/#updatepermission)or[ delete ](https://hasura.io/docs/latest/api-reference/syntax-defs/#deletepermission)permissions.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_insert_permission" ,
   "args" :   {
     "table" :   {
       "name" :   "users" ,
       "schema" :   "public"
     } ,
     "role" :   "user" ,
     "permission" :   {
       "check" :   { } ,
       "columns" :   [
         "id"
       ] ,
       "set" :   { } ,
       "backend_only" :   true
     } ,
     "source" :   "default"
   }
}
```

Supported from

Backend only permissions for `update` and `delete` mutations are supported in Hasura GraphQL Engine versions `v2.8.0` and above.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authorization/permissions/backend-only/#introduction)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)