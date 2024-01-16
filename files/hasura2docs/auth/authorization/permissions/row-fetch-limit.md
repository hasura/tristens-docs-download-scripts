# Row Fetch Limit

## Introduction​

Limit the number of rows returned in a response on `select` operations.

- Console
- CLI
- API


You can set a row fetch limit on the Hasura Console in **Data -> [table] -> Permissions -> select -> Row select
permissions -> Limit number of rows** as per the image below:

Image: [ Row fetch limit ](https://hasura.io/docs/assets/images/authorization_row-fetch-limit_2-16-1-322d5e39214506a7a76d1ce8320a6de6.png)

You can set a row fetch limit for a table in the `metadata -> databases -> [database-name] -> tables -> 
[table-name].yaml` file, eg:

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
         filter :
           user_id :
             _eq :  X - Hasura - User - Id
         limit :   1
```

Apply the Metadata by running:

`hasura metadata apply`

You can set a row fetch limit for a table when using the[ permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/). Example using a Postgres db:

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
          "columns" :   "*" ,
          "filter" :   {
             "id" :   {
                "_eq" :   "X-Hasura-User-Id"
             }
          } ,
          "limit" :   1
       }
    }
}
```

In the above example, this configuration restricts the number of accessible rows ( *based on the row permission* : `{"id":{"_eq":"X-Hasura-User-Id"}}` ) to 1.

Setting row fetch limits is useful for preventing abuse of your API especially if it is exposed to the public. You
can[ also configure other limits ](https://hasura.io/docs/latest/security/security-best-practices/#limit-the-api).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authorization/permissions/row-fetch-limit/#introduction)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)