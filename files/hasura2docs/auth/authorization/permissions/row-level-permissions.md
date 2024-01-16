# Configure Row Permissions

## Introduction​

Row permissions are powerful boolean expressions that help you restrict access to database rows for each database
operation and user role.

For example on a `select` operation utilizing the `X-Hasura-User-Id` session variable, you can match the user ID
in the row with the row permission: `{"id":{"_eq":"X-Hasura-User-Id"}}` 

Row-level permissions can be defined using static values, values in columns ( *including those in related
tables or nested objects* ), session variables and operators.

Depending on the operation, the permission can be run in different ways. In the case of `select` , your permission is
used to determine whether a row can be read. In the case of `insert` , `update` and `delete` , the
boolean expression determines whether the mutation as a whole is allowed.

## Operators​

In the particular permission expression example: `{"id":{"_eq":"X-Hasura-User-Id"}}` the `_eq` is the operator, and
denotes equality.

Hasura Engine has an extensive list of operators that can be used to build row-level permission expressions.
A different set of operators is available depending on the type of value which the operator is applied to, eg: string,
boolean, integer. Generally these are the same operators that you use to[ filter query results ](https://hasura.io/docs/latest/queries/postgres/filters/index/)along with a few others.

[ Check out this list ](https://hasura.io/docs/latest/auth/authorization/permissions/permissions-operators/)for all supported permissions
operators.

## Simple row level permissions​

Using the Hasura Console, you can construct permissions easily using the builder interface or manually editing the text
field. You are also able to set permissions using the Hasura CLI or API.

The following is an example of a simple permission to restrict access for `select` to rows of a products table where
the value in the `price` column is less than 1000. Let's assume this is useful for a low-level admin role.

- Console
- CLI
- API


You can define simple `select` operation permissions using boolean expressions on the Hasura Console in **Data ->
[table] -> Permissions -> select** .

Image: [ Using boolean expressions to build rules ](https://hasura.io/docs/assets/images/authorization_simple-boolean-expression_2-16-1-a9d30b4f05113575a77965f757827796.png)

You can define permissions using boolean expressions in the `metadata -> databases -> [database-name] -> tables ->
[table-name].yaml` file, eg:

```
-   table :
     schema :  public
     name :  products
   select_permissions :
     -   role :  user
       permission :
         columns :   [ ]
         filter :
           price :
           _lt :   1000
```

Apply the Metadata by running:

`hasura metadata apply`

You can define permissions using boolean expressions when using the[ permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/). Example with a Postgres db:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_select_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "products" ,
     "role" :   "user" ,
     "permission" :   {
       "columns" :   "*" ,
       "filter" :   {
         "price" :   {
           "_lt" :   1000
         }
       }
     }
   }
}
```

You can construct more complex boolean expressions using the `_and` , `_or` and `not` logical operators:

For example, using the `_and` operator, you can construct a rule to restrict access for `select` to rows where the
value in the `price` column is less than 1000 **and** the value in the `name` column starts with "acme":

- Console
- CLI
- API


You can define permissions using the `_and` operator on the Hasura Console in **Data -> [table] -> Permissions ->
select** as follows:

Image: [ Example of a rule with the _and operator ](https://hasura.io/docs/assets/images/composite-boolean-expression_2.16.1-8df9901ece0389d56b9c0489799523b5.png)

You can define permissions using the `_and` operator in the `metadata -> databases -> [database-name] -> tables ->
[table-name].yaml` file eg:

```
-   table :
     schema :  public
     name :  products
   select_permissions :
     -   role :  user
       permission :
         columns :   [ ]
         filter :
           _and :
             -   price :   {   _lt :   1000   }
             -   name :   {   _ilike :  acme%  }
```

Apply the Metadata by running:

`hasura metadata apply`

You can define permissions using the `_and` operator when using the[ permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/). Example with a Postgres db:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_select_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "products" ,
     "role" :   "user" ,
     "permission" :   {
       "columns" :   "*" ,
       "filter" :   {
         "$and" :   [
           {
             "price" :   {
               "_lt" :   1000
             }
           } ,
           {
             "name" :   {
               "_ilike" :   "acme%"
             }
           }
         ]
       }
     }
   }
}
```

## Permissions with session variables​

Session variables that have been resolved from authentication tokens by either your authentication webhook or by
Hasura Engine using the JWT configuration are available for constructing row-level permissions.

For example, to allow a `user` to access only the products which they've added, you can use the `X-Hasura-User-ID` session variable to compare against the `added_by_user_id` column in the `products` table.

- Console
- CLI
- API


You can use session variables in your permissions on the Hasura Console in **Data -> [table] -> Permissions -> insert /
select / update / delete** as follows:

Image: [ Using session variables to build rules ](https://hasura.io/docs/assets/images/session-variables-in-permissions-simple-example_2.16.1-c203499c3db84f06e0dd45b93e3915f9.png)

You can use session variables in your permissions in the `metadata -> databases -> [database-name] -> tables ->
[table-name].yaml` file, eg:

```
-   table :
     schema :  public
     name :  products
   select_permissions :
     -   role :  user
       permission :
         columns :
           -  id
           -  name
           -  description
           -  price
           -  manufacturer
           -  category
           -  image
           -  added_by_user_id
         filter :
           added_by_user_id :
             _eq :  X - Hasura - User - Id
```

Apply the Metadata by running:

`hasura metadata apply`

You can define session variables in permissions tables when using the[ permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/). Example using a Postgres db:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_select_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "products" ,
     "role" :   "user" ,
     "permission" :   {
       "columns" :   "*" ,
       "filter" :   {
         "added_by_user_id" :   "X-Hasura-User-Id"
       }
     }
   }
}
```

Array session variables in permission rules

Support for using session variables for array operators like `_in` , `_nin` , `_has_any_keys` , `_has_all_keys` is
available in versions `v1.0.0-beta.3` and above.

When you use array operators such as `_in` in the permissions builder in the Hasura Console, it will automatically open
an array for your values. If your session variable value is already an array, you can click the `[X-Hasura-Allowed-Ids]` suggestion to remove the brackets and set your session variable in its place.

## Permissions with relationships or nested objects​

You can leverage[ table relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/)to define permission rules with
fields from a nested object.

For example, Let's say you want to check that the user making the request to a `products` table is a
member of the vendor organization which owns the product.

You have a column on the `products` table called `vendor_id` which denotes which vendor the product belongs to. You
also have an array relationship in the `products` table called `usersInVendorsByVendorId` which links to the `users_in_vendors` table which is just a table of `user_id` and `vendor_id` which shows which users are in which
vendor.

We can use this relationship to check that the user making the request is a member of the vendor which the
product belongs to.

- Console
- CLI
- API


You can use a nested object to build rules on the Hasura Console in **Data -> [table] -> Permissions -> insert /
select / update / delete** as follows:

Image: [ Using a nested object to build rules ](https://hasura.io/docs/assets/images/row-level-permissions_related-table-permission_2.16-9da812a5e750eb84ea19c9729204e966.png)

You can add permissions using relationships or nested objects in the `metadata -> databases -> [database-name] -> tables
-> [table-name].yaml` eg:

```
-   table :
     schema :  public
     name :  products
   select_permissions :
     -   role :  manager
       permission :
         columns :   [ ]
         filter :
           usersInVendorsByVendorId :
             user_id :
               _eq :  X - Hasura - User - Id
```

Apply the Metadata by running:

`hasura metadata apply`

You can add permissions using relationships or nested objects when using the[ permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/). Example using a Postgres db:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_select_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "products" ,
     "role" :   "manager" ,
     "permission" :   {
       "columns" :   "*" ,
       "filter" :   {
         "usersInVendorsByVendorId" :   {
           "user_id" :   {
             "_eq" :   "X-Hasura-User-Id"
           }
         }
       }
     }
   }
}
```

This permission rule reads as " *If the user's id is listed as a member of the vendor which owns the product then allow
access to the product* ."

Array and object relationships work similarly

- The above example would have worked even if the relationship were an object relationship.
- You can also check out this more elaborate[ example ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#nested-object-permissions-example).


## Permission with remote relationships​

Just like in-source relationships, you can also use remote source relationships to define permission rules with fields
from the remote source.

Supported from

Hasura GraphQL Engine `v2.33.0` and onwards.

For example, let's say you have a Snowflake database for storing product reviews and a Postgres database for products.

You have a remote source relationship defined **from** the `reviews` table in Snowflake **to** the `products` table in
Postgres. The `products` table has a column of `owner_id` .

We can use this remote relationship to define a permission on the `products` table to make sure that the user can only
fetch the reviews that belong to them (i.e., for which the corresponding `owner_id` is equal to the `x-hasura-user-id` ).

- Console
- CLI
- API


You can use a nested object to build rules on the Hasura Console in **Data -> [table] -> Permissions -> insert /
select / update / delete** as follows:

Image: [ Using a remote source relationship to build rules ](https://hasura.io/docs/assets/images/row-level-permission-remote-source-relationship_2.33-865a61777debd598dd7ce47b4005e337.png)

You can add permissions using relationships or nested objects in the `metadata -> databases -> [database-name] -> tables
-> [table-name].yaml` eg:

```
-   table :
     schema :  public
     name :  reviews
   select_permissions :
     -   role :  user
       permission :
         columns :  *
         filter :
           review_product :
             owner_id :
               _eq :  X - Hasura - User - Id
```

Apply the Metadata by running:

`hasura metadata apply`

You can add permissions using relationships or nested objects when using the[ permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/). Example using a Snowflake db:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "snowflake_create_select_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "reviews" ,
     "role" :   "user" ,
     "permission" :   {
       "columns" :   "*" ,
       "filter" :   {
         "review_product" :   {
           "owner_id" :   {
             "_eq" :   "X-Hasura-User-Id"
           }
         }
       }
     }
   }
}
```

What does this permission rule do?

This permission rule reads as " *If the user's id corresponds to the user who owns the product, then allow
access to the review* ."

### Limitations with remote relationship predicates​

The remote relationship predicate must follow this template:

```
{
   "<rel name>" :   {
     "<remote column name>" :   {
       "<op>" :   "<some session variable name or some literal text>"
     }
   }
}
```

- The remote relationship predicate can only be one level deep. However, the predicate can be nested in an `_and` , `_or` , `_not` or `_exists` node.
- Only `_eq` , `_neq` , `_gt` , `_lt` , `_gte` , `_lte` , `_in` , `_nin` , `_like` , `_nlike` and `_is_null` operators are
supported for comparing fields.
- Only columns from the remote source can be compared with session variables or literal text only.
- The remote source relationship permission can only be defined for Postgres and[ data
connector ](https://hasura.io/docs/latest/databases/data-connectors/)backends.
- The remote source relationship backend (on the right-hand side) can be **Postgres only** .
- Subscriptions on tables that use remote relationships in permissions are **not supported** .


The remote relationship predicate can only be one level deep. However, the predicate can be nested in an `_and` , `_or` , `_not` or `_exists` node.

Only `_eq` , `_neq` , `_gt` , `_lt` , `_gte` , `_lte` , `_in` , `_nin` , `_like` , `_nlike` and `_is_null` operators are
supported for comparing fields.

Only columns from the remote source can be compared with session variables or literal text only.

The remote source relationship permission can only be defined for Postgres and[ data
connector ](https://hasura.io/docs/latest/databases/data-connectors/)backends.

The remote source relationship backend (on the right-hand side) can be **Postgres only** .

Subscriptions on tables that use remote relationships in permissions are **not supported** .

## Permissions with unrelated tables or views​

You can use the `_exists` operator to set a permission rule based on tables or views that are not related to our table.

For example, say you want to allow a user to `insert` a `product` only if the value of the `allow_product_create` column in the `users` table is set to `true` .

In this case we'll need to check that both the user who is making the request exists in the `users` table AND that
the `allow_product_create` column is set to `true` . Let's assume the user's id is passed in the `X-Hasura-User-ID` session variable.

- Console
- CLI
- API


You can set permissions using unrelated tables on the Hasura Console in **Data -> [table] -> Permissions -> insert /
select / update / delete** as follows:

Image: [ Use an unrelated table to build rules ](https://hasura.io/docs/assets/images/row-level-permissions_unrelated-table-permission_2.16-0d465997e8167f2e00605cafc6a05ceb.png)

You can set permissions using unrelated tables in the `metadata -> databases -> [database-name] -> tables ->
[table-name].yaml` , eg:

```
-   table :
     schema :  public
     name :  products
   insert_permissions :
     -   role :  user
       permission :
         check :
           _exists :
             _where :
               _and :
                 -   id :   {   _eq :  X - Hasura - User - Id  }
                 -   allow_product_create :   {   _eq :   true   }
             _table :
               schema :  public
               name :  users
         columns :
           -  id
           -  name
           -  price
           -  description
```

Apply the Metadata by running:

`hasura metadata apply`

You can set permissions for unrelated tables when using the[ permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/). Example using a Postgres db:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_insert_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "products" ,
     "role" :   "user" ,
     "permission" :   {
       "columns" :   "*" ,
       "check" :   {
         "$exists" :   {
           "_table" :   "users" ,
           "_where" :   {
             "$and" :   [
               {
                 "id" :   "X-Hasura-User-Id"
               } ,
               {
                 "allow_product_create" :   true
               }
             ]
           }
         }
       }
     }
   }
}
```

This permission rule reads as " *if there exists a row in the table*  `users`  *whose*  `id`  *is the same as the requesting
user's*  `id`  *AND has the*  `allow_product_create`  *column set to true, allow access to insert products* ."

## Post-update check row permissions​

The update database operation has both a "Pre-update check" and a "Post-update check" for its row permissions. This
is useful if your new data post update is unknown until it is changed.

For example, say that in an update mutation we are updating a number by an amount and the result is not allowed to be
negative or higher than a certain value. This would be a perfect place to use the "Post-update check" permission.

Image: [ Post-update check row permission ](https://hasura.io/docs/assets/images/permissions_post-update-check_2-17-0-c0b79e6a91e779ac72b125e6c014a0a6.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#introduction)
- [ Operators ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#operators)
- [ Simple row level permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#simple-row-level-permissions)
- [ Permissions with session variables ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#permissions-with-session-variables)
- [ Permissions with relationships or nested objects ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#relationships-in-permissions)
- [ Permission with remote relationships ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#remote-relationships-in-permission)
    - [ Limitations with remote relationship predicates ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#limitations-with-remote-relationship-predicates)
- [ Permissions with unrelated tables or views ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#unrelated-tables-in-permissions)
- [ Post-update check row permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#post-update-check-row-permissions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)