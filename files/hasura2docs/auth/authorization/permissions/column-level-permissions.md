# Column Permissions

## Introduction​

Column permissions determine which columns are accessible in the rows which are accessible.

- Console
- CLI
- API


Column-level permissions are simple selections on the Hasura Console in **Data -> [table] -> Permissions -> insert /
select / update** as per this example:

Image: [ Column level permissions ](https://hasura.io/docs/assets/images/authorization_column-permissions_2.16-f0bb74f55bc26e9f2dc77090f7915fd9.png)

You can set column-level permissions in the `metadata -> databases -> [database-name] -> tables -> [table-name].yaml` file, eg:

```
-   table :
     schema :  public
     name :  users
   select_permissions :
     -   role :  user
       permission :
         columns :
           -  id
           -  name
           -  email
         filter :
           id :
           _eq :  X - Hasura - User - Id
```

Apply the metadata by running:

`hasura metadata apply`

You can set column-level permissions when using the[ permissions metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/). Example using a Postgres db:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_select_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "users" ,
     "role" :   "user" ,
     "permission" :   {
       "columns" :   [
         "id" ,
         "name" ,
         "email" ,
       ] ,
       "filter" :   {
         "id" :   "X-Hasura-User-Id"
       }
     }
   }
}
```

In this example, the role `user` has only partial access to columns of the accessible rows for the `select` operation.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authorization/permissions/column-level-permissions/#introduction)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)