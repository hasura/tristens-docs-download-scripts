# Column Presets

## Introduction​

While this is not strictly a permission configuration, defining role-based column presets for `insert` and `update` operations on any column automatically removes the ability to manually insert or update it for that role.

The respective fields will also be removed from the generated GraphQL schema for that role.

This setup very useful in avoiding sensitive user information being sent in the request and instead leveraging
session variables or static data for that information.

- Console
- CLI
- API


You can define column presets for either `insert` or `update` operations in the Hasura Console in **Data ->
[table] -> Permissions -> insert / update** as follows:

Image: [ Set column preset ](https://hasura.io/docs/assets/images/set_column_preset_console_2.10.1-0bb8b5a33f206bfe7ff7bb215c2f42a2.png)

You can define column presets for table columns in the `metadata > databases -> [database-name] -> tables -> 
[table-name].yaml` , eg: `public_users.yaml` :

```
table :
   name :  users
   schema :  public
insert_permissions :
   -   role :  user
     permission :
       check :   { }
       set :
         id :  x - hasura - User - Id
       columns :
         -  id
```

Apply the Metadata by running:

`hasura metadata apply`

You can define column presets with either the[ insert ](https://hasura.io/docs/latest/api-reference/syntax-defs/#insertpermission)or[ update ](https://hasura.io/docs/latest/api-reference/syntax-defs/#updatepermission)[ permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/). Example using a Postgres db:

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
       "set" :   {
         "id" :   "x-hasura-user-id"
     }
   } ,
     "source" :   "default"
   }
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authorization/permissions/column-presets/#introduction)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)