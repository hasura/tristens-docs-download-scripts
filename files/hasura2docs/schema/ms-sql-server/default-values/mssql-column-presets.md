# MS SQL Server: Setting Values for Fields Using Role-Based Column Presets

## Introduction​

Let's say you want certain fields to have their values set automatically using session variables or fixed values when a
row is created/updated with a particular[ user role ](https://hasura.io/docs/latest/auth/authorization/roles-variables/).

Hasura GraphQL Engine's column presets let you define role-based values for any field/column. These values can either be
a session variable value or a static value.

Column preset restricts mutation access for configured role

Column preset values are not overridable by the user. ie. If a column has a preset defined for a given role, access to
the column for the mutation will be restricted for users with that role.

 **Example:** Say we have a field `user_id` in a table `article` which is to be set to the id of the user, from the value
of the user's session variable whenever a new row is added to the `article` table.

## Step 1: Configure a column preset​

- Console
- CLI
- API


Support will be added soon.

You can set column presets in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  article
   insert_permissions :
     -   role :  user
       permission :
         check :   { }
         set :
           user_id :  x - hasura - User - Id
         columns :
           -  content
           -  rating
           -  title
         backend_only :   false
```

Apply the Metadata by running:

`hasura metadata apply`

You can add column presets by using the[ mssql_create_insert_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission)metadata
API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type"   :   "mssql_create_insert_permission" ,
   "args"   :   {
     "source" :   "<db_name>" ,
     "table"   :   "article" ,
     "role"   :   "user" ,
     "permission"   :   {
       "check"   :   { } ,
       "set" : {
         "user_id" : "X-Hasura-User-Id"
       } ,
       "columns" : [ "title" ,   "content" ,   "rating" ]
     }
   }
}
```

Note

To set a column preset for a nested object's column, simply set the corresponding column preset in the remote table.

## Step 2: Run an insert mutation​

Head to the GraphiQL interface in the Console and try making an insert mutation on the `article` table with the
following headers ( *to run through this example, don't forget to also grant the*  `user`  *role sufficient permissions to
select from the*  `article`  *table* ):

- `X-Hasura-Role` --> `user` ( *to test the behavior for the configured role* )
- `X-Hasura-User-Id` --> `1` ( *this is the value we should expect in the*  `user_id`  *field* )


As mentioned earlier, you'll notice when you add the `X-Hasura-Role` header that the field, `user_id` , is no longer
available as the mutation type's field:

Image: [ Write an insert mutation ](https://hasura.io/docs/assets/images/column-preset-schema-change-for-role-e282bb99ddafdf92f20c095800f647ef.png)

Now, if we run the following insert mutation, we'll see that the `user_id` field is indeed being set with the value
passed in the `X-Hasura-User-Id` variable:

Image: [ Run the insert mutation ](https://hasura.io/docs/assets/images/column-preset-mutation-result-1a9a809c5ce533a436591fb9ef59f17c.png)

Note

Not passing the configured header will result in a run-time error:

```
{
   "errors" :   [
     {
       "path" :   "$" ,
       "error" :   "\"x-hasura-user-id\" header is expected but not found" ,
       "code" :   "not-found"
     }
   ]
}
```

## Also see​

- [ MS SQL Server: Setting default values for fields using MS SQL Server defaults ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-defaults/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-column-presets/#introduction)
- [ Step 1: Configure a column preset ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-column-presets/#step-1-configure-a-column-preset)
- [ Step 2: Run an insert mutation ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-column-presets/#step-2-run-an-insert-mutation)
- [ Also see ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-column-presets/#also-see)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)