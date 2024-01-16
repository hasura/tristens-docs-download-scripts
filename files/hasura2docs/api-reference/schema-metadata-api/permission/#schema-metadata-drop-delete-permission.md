# Schema/Metadata API Reference: Permissions (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

## Introduction​

The permission layer is designed to restrict the operations that can be
performed by various users. Permissions can be defined on various
operations (insert/select/update/delete) at a role level granularity. By
default, the `admin` role has unrestricted access to all operations.

Variables in rules

All `X-Hasura-*` header values can be used in the permission rules.
These values can come with the request and can be validated using
webhook or can be sent with the JWT token.

## create_insert_permission​

An insert permission is used to enforce constraints on the data that is
being inserted.

Let's look at an example, a permission for the `user` role to insert
into the `article` table. What is the constraint that we would like to
enforce here? *A user can only insert articles for themselves* .

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "create_insert_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user" ,
         "permission"   :   {
             "check"   :   {
                 "author_id"   :   "X-HASURA-USER-ID"
             } ,
             "set" : {
                 "id" : "X-HASURA-USER-ID"
             } ,
             "columns" : [ "name" , "author_id" ]
         }
     }
}
```

This reads as follows - for the `user` role:

- For every row that is being inserted into the *article* table, allow
insert only if the `check` passes i.e. that the `author_id` column
value is the same as the value in the request header `X-HASURA-USER-ID` ".
- If the above `check` passes, then access for insert will be limited
to columns `name` and `author_id` only.
- When this insert happens, the value of the column `id` will be
automatically `set` to the value of the resolved session variable `X-HASURA-USER-ID` .


The argument for `check` is a boolean expression which has the same
syntax as the `where` clause in the `select` query, making it extremely
expressive.

An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "create_insert_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user" ,
         "permission"   :   {
             "check"   :   {
                 "author_id"   :   "X-HASURA-USER-ID" ,
                 "$or"   :   [
                     {
                         "category"   :   "editorial" ,
                         "is_reviewed"   :   false
                     } ,
                     {
                         "category"   :   {   "$neq"   :   "editorial" }
                     }
                 ]
             }
         }
     }
}
```

In the above definition, the row is allowed to be inserted if the `author_id` is the same as the request's user id and `is_reviewed` is `false` when the `category` is "editorial".

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| permission | true | [ InsertPermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#insertpermission) | The permission definition |
| comment | false | text | Comment |


## drop_insert_permission​

The `drop_insert_permission` API is used to drop an existing insert
permission for a role on a table.

An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "drop_insert_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |


## create_select_permission​

A select permission is used to restrict access to only the specified
columns and rows.

Let's look at an example, a permission for the `user` role to select
from the `article` table: all columns can be read, as well as the rows
that have been published or authored by the user themselves.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "create_select_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user" ,
         "permission"   :   {
             "columns"   :   "*" ,
             "filter"   :   {
                 "$or"   :   [
                     {   "author_id"   :   "X-HASURA-USER-ID"   } ,
                     {   "is_published"   :   true   }
                 ]
              } ,
              "limit" :   10 ,
              "allow_aggregations" :   true
         }
     }
}
```

This reads as follows - For the `user` role:

- Allow selecting rows where the `check` passes i.e. `is_published` is `true` or the `author_id` matches the value of the session variable `X-HASURA-USER-ID` .
- Allow selecting all columns (because the `columns` key is set to `*` ).
- `limit` the numbers of rows returned by a query to the `article` table by the `user` role to a maximum of 10.
- Allow aggregate queries.


### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| permission | true | [ SelectPermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#selectpermission) | The permission definition |
| comment | false | text | Comment |


## drop_select_permission​

The `drop_select_permission` is used to drop an existing select
permission for a role on a table.

An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "drop_select_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |


## create_update_permission​

An update permission is used to restrict the columns and rows that can
be updated. Its structure is quite similar to the select permission.

An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "create_update_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user" ,
         "permission"   :   {
             "columns"   :   [ "title" ,   "content" ,   "category" ] ,
             "filter"   :   {
                 "author_id"   :   "X-HASURA-USER-ID"
             } ,
             "check"   :   {
                 "content"   :   {
                   "_ne" :   ""
                 }
             } ,
             "set" : {
                 "updated_at"   :   "NOW()"
             }
         }
     }
}
```

This reads as follows - for the `user` role:

- Allow updating only those rows where the `filter` passes i.e. the
value of the `author_id` column of a row matches the value of the
session variable `X-HASURA-USER-ID` .
- If the above `filter` passes for a given row, allow updating only
the `title` , `content` and `category` columns ( *as specified in the*  `columns`  *key* ).
- After the update happens, verify that the `check` condition holds
for the updated row i.e. that the value in the `content` column is
not empty.
- When this update happens, the value of the column `updated_at` will
be automatically `set` to the current timestamp.


Note

It is important to deny updates to columns that will determine the row
ownership. In the above example, the `author_id` column determines the
ownership of a row in the `article` table. Columns such as this should
never be allowed to be updated.

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| permission | true | [ UpdatePermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#updatepermission) | The permission definition |
| comment | false | text | Comment |


## drop_update_permission​

The `drop_update_permission` API is used to drop an existing update
permission for a role on a table.

An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "drop_update_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |


## create_delete_permission​

A delete permission is used to restrict the rows that can be deleted.

An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "create_delete_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user" ,
         "permission"   :   {
             "filter"   :   {
                 "author_id"   :   "X-HASURA-USER-ID"
             }
         }
     }
}
```

This reads as follows:

" `delete` for the `user` role on the `article` table is allowed on rows
where `author_id` is the same as the request header `X-HASURA-USER-ID` value."

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| permission | true | [ DeletePermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#deletepermission) | The permission definition |
| comment | false | text | Comment |


## drop_delete_permission​

The `drop_delete_permission` API is used to drop an existing delete
permission for a role on a table.

An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "drop_delete_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |


## set_permission_comment​

 `set_permission_comment` is used to set/update the comment on a
permission. Setting the comment to `null` removes it.

An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
Authorization :   Bearer <auth-token> # optional if cookie is set
X-Hasura-Role :   admin
{
     "type" :   "set_permission_comment" ,
     "args" :   {
         "table" :   "article" ,
         "role" :   "user" ,
         "type"   :   "update" ,
         "comment"   :   "can only modify their own rows"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | The role in the permission |
| type | true | permission type (one of select/update/delete/insert) | The type of the permission |
| comment | false | Text | Comment |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#introduction)
- [ create_insert_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-create-insert-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-create-insert-permission-syntax)
- [ drop_insert_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-drop-insert-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-drop-insert-permission-syntax)
- [ create_select_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-create-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-create-select-permission-syntax)
- [ drop_select_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-drop-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-drop-select-permission-syntax)
- [ create_update_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-create-update-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-create-update-permission-syntax)
- [ drop_update_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-drop-update-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-drop-update-permission-syntax)
- [ create_delete_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-create-delete-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-create-delete-permission-syntax)
- [ drop_delete_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-drop-delete-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-drop-delete-permission-syntax)
- [ set_permission_comment ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-set-permission-comment)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission/#schema-metadata-set-permission-comment-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)