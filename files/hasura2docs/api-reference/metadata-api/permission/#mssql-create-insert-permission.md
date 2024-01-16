# Metadata API Reference: Permissions

## Introduction​

The permission layer is designed to restrict the operations that can be
performed by various users. Permissions can be defined on various
operations (insert/select/update/delete) at a role level granularity. By
default, the `admin` role has unrestricted access to all operations.

Variables in rules

All `X-Hasura-*` header values can be used in the permission rules.
These values can come with the request and can be validated using
webhook or can be sent with the JWT token.

Supported from

The Metadata API is supported for versions `v2.0.0` and above and
replaces the older[ schema/Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

## pg_create_insert_permission​

An insert permission is used to enforce constraints on the data that is being inserted.

Let's look at an example, a permission for the `user` role to insert
into the `article` table. What is the constraint that we would like to
enforce here? *A user can only insert articles for themselves* .

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_create_insert_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
         "role"   :   "user" ,
         "permission"   :   {
             "check"   :   {
                 "author_id"   :   "X-HASURA-USER-ID"
             } ,
             "set" : {
                 "id" : "X-HASURA-USER-ID"
             } ,
             "columns" : [ "name" , "author_id" ] ,
             "validate_input" :   {
                 "type" :   "http" ,
                 "definition" :   {
                 "forward_client_headers" :   true ,
                 "headers" :   [ ] ,
                 "timeout" :   10 ,
                 "url" :   "http://www.somedomain.com/validateUser"
                 }
             }
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
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_create_insert_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
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
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_drop_insert_permission​

The `pg_drop_insert_permission` API is used to drop an existing insert
permission for a role on a table.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_drop_insert_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
         "role"   :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_create_select_permission​

A select permission is used to restrict access to only the specified columns and rows.

Let's look at an example, a permission for the `user` role to select
from the `article` table: all columns can be read, as well as the rows
that have been published or authored by the user themselves.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_create_select_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user" ,
         "source" :   "default" ,
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
- All query and subscription root fields are enabled.


Let's take another example to show how to enable a particular set of
root fields.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_create_select_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "guest" ,
         "source" :   "default" ,
         "permission"   :   {
             "columns"   :   "*" ,
             "filter"   :   { } ,
             "query_root_fields" :   [ "select_by_pk" ] ,
             "subscription_root_fields" :   [ "select_by_pk" ]
         }
     }
}
```

This reads as follows - for the `guest` role:

- Allow access to all the rows.
- Allow selecting all the columns.
- Allow only the `select_by_pk` root field in the `query` and `subscription` root fields. The
other root fields will be disabled.


The select permission of the `guest` role is configured in a way such that, it can:

1. The access to the `article` table is restricted to what can be accessed through relationships to the `article` table.
2. If the `guest` has the access to the primary key value, it can access the data corresponding to that primary key.


### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| permission | true | [ SelectPermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#selectpermission) | The permission definition |
| comment | false | text | Comment |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_drop_select_permission​

The `pg_drop_select_permission` is used to drop an existing select
permission for a role on a table.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_drop_select_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user" ,
         "source" :   "default"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_create_update_permission​

An update permission is used to restrict the columns and rows that can
be updated. Its structure is quite similar to the select permission.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_create_update_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
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
             } ,
             "validate_input" :   {
                 "type" :   "http" ,
                 "definition" :   {
                 "forward_client_headers" :   true ,
                 "headers" :   [ ] ,
                 "timeout" :   10 ,
                 "url" :   "http://www.somedomain.com/validateUser"
                 }
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
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_drop_update_permission​

The `pg_drop_update_permission` API is used to drop an existing update
permission for a role on a table.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_drop_update_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
         "role"   :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_create_delete_permission​

A delete permission is used to restrict the rows that can be deleted.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_create_delete_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
         "role"   :   "user" ,
         "permission"   :   {
             "filter"   :   {
                 "author_id"   :   "X-HASURA-USER-ID"
             } ,
             "validate_input" :   {
                 "type" :   "http" ,
                 "definition" :   {
                 "forward_client_headers" :   true ,
                 "headers" :   [ ] ,
                 "timeout" :   10 ,
                 "url" :   "http://www.somedomain.com/validateUser"
                 }
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
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_drop_delete_permission​

The `pg_drop_delete_permission` API is used to drop an existing delete permission for a role on a table.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_drop_delete_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user" ,
         "source" :   "default"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_set_permission_comment​

 `pg_set_permission_comment` is used to set/update the comment on a permission. Setting the comment to `null` removes it.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
Authorization :   Bearer <auth-token> # optional if cookie is set
X-Hasura-Role :   admin
{
     "type" :   "pg_set_permission_comment" ,
     "args" :   {
         "table" :   "article" ,
         "source" :   "default" ,
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
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_create_insert_permission​

An insert permission is used to enforce constraints on the data that is being inserted.

Let's look at an example, a permission for the `user` role to insert
into the `article` table. What is the constraint that we would like to
enforce here? *A user can only insert articles for themselves* .

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_create_insert_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
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
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_create_insert_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
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
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_drop_insert_permission​

The `mssql_drop_insert_permission` API is used to drop an existing insert permission for a role on a table.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_drop_insert_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
         "role"   :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_create_select_permission​

A select permission is used to restrict access to only the specified
columns and rows.

Let's look at an example, a permission for the `user` role to select
from the `article` table: all columns can be read, as well as the rows
that have been published or authored by the user themselves.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_create_select_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user" ,
         "source" :   "default" ,
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
- All query and subscription root fields are enabled.


Let's take another example to show how to enable a particular set of
root fields.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_create_select_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "guest" ,
         "source" :   "default" ,
         "permission"   :   {
             "columns"   :   "*" ,
             "filter"   :   { } ,
             "query_root_fields" :   [ "select_by_pk" ] ,
             "subscription_root_fields" :   [ "select_by_pk" ]
         }
     }
}
```

This reads as follows - for the `guest` role:

- Allow access to all the rows.
- Allow selecting all the columns.
- Allow only the `select_by_pk` root field in the `query` and `subscription` root fields. The
other root fields will be disabled.


The select permission of the `guest` role is configured in a way such that, it can:

1. The access to the `article` table is restricted to what can be accessed through relationships to the `article` table.
2. If the `guest` has the access to the primary key value, it can access the data corresponding to that primary key.


### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| permission | true | [ SelectPermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#selectpermission) | The permission definition |
| comment | false | text | Comment |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_drop_select_permission​

The `mssql_drop_select_permission` is used to drop an existing select permission for a role on a table.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_drop_select_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user" ,
         "source" :   "default"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_create_update_permission​

An update permission is used to restrict the columns and rows that can
be updated. Its structure is quite similar to the select permission.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_create_update_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
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
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_drop_update_permission​

The `mssql_drop_update_permission` API is used to drop an existing
update permission for a role on a table.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_drop_update_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
         "role"   :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_create_delete_permission​

A delete permission is used to restrict the rows that can be deleted.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_create_delete_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "source" :   "default" ,
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
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_drop_delete_permission​

The `mssql_drop_delete_permission` API is used to drop an existing
delete permission for a role on a table.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_drop_delete_permission" ,
     "args"   :   {
         "table"   :   "article" ,
         "role"   :   "user" ,
         "source" :   "default"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Role |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_set_permission_comment​

 `mssql_set_permission_comment` is used to set/update the comment on a permission. Setting the comment to `null` removes it.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
Authorization :   Bearer <auth-token> # optional if cookie is set
X-Hasura-Role :   admin
{
     "type" :   "mssql_set_permission_comment" ,
     "args" :   {
         "table" :   "article" ,
         "source" :   "default" ,
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
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#introduction)
- [ pg_create_insert_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-create-insert-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-create-insert-permission-syntax)
- [ pg_drop_insert_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-drop-insert-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-drop-insert-permission-syntax)
- [ pg_create_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-create-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-create-select-permission-syntax)
- [ pg_drop_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-drop-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-drop-select-permission-syntax)
- [ pg_create_update_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-create-update-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-create-update-permission-syntax)
- [ pg_drop_update_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-drop-update-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-drop-update-permission-syntax)
- [ pg_create_delete_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-create-delete-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-create-delete-permission-syntax)
- [ pg_drop_delete_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-drop-delete-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-drop-delete-permission-syntax)
- [ pg_set_permission_comment ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-set-permission-comment)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#metadata-pg-set-permission-comment-syntax)
- [ mssql_create_insert_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-create-insert-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-create-insert-permission-syntax)
- [ mssql_drop_insert_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-drop-insert-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-drop-insert-permission-syntax)
- [ mssql_create_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-create-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-create-select-permission-syntax)
- [ mssql_drop_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-drop-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-drop-select-permission-syntax)
- [ mssql_create_update_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-create-update-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-create-update-permission-syntax)
- [ mssql_drop_update_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-drop-update-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-drop-update-permission-syntax)
- [ mssql_create_delete_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-create-delete-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-create-delete-permission-syntax)
- [ mssql_drop_delete_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-drop-delete-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-drop-delete-permission-syntax)
- [ mssql_set_permission_comment ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-set-permission-comment)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#mssql-create-insert-permission/#mssql-set-permission-comment-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)