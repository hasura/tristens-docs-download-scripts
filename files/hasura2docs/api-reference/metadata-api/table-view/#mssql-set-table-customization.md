# Metadata API Reference: Tables/Views

## Introduction​

Track/untrack a table/view in Hasura GraphQL Engine.

Only tracked tables/views are available for querying/mutating/subscribing data over the GraphQL API.

Supported from

The Metadata API is supported for versions `v2.0.0` and above and replaces the older[ schema/Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

## pg_track_table​

 `pg_track_table` is used to add a table/view to the GraphQL schema with configuration. You can customize the root field
names.

Add a table/view `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_track_table" ,
   "args" :   {
     "source" :   "default" ,
     "table" :   "author" ,
     "configuration" :   {
       "custom_root_fields" :   {
         "select" :   "Authors" ,
         "select_by_pk" :   "Author" ,
         "select_aggregate" :   "AuthorAggregate" ,
         "insert" :   "AddAuthors" ,
         "insert_one" : "AddAuthor" ,
         "update" :   "UpdateAuthors" ,
         "update_by_pk" :   "UpdateAuthor" ,
         "delete" :   "DeleteAuthors" ,
         "delete_by_pk" :   "DeleteAuthor"
       } ,
       "column_config" :   {
         "id" :   {
           "custom_name" :   "authorId" ,
           "comment" :   "The ID of the Author"
         }
       } ,
       "comment" :   "Authors of books"
     } ,
     "apollo_federation_config" :   {
       "enable" :   "v1"
     }
   }
}
```

A table can be tracked with a `custom name` . This can be useful when a table name is not GraphQL compliant, like `Users Address` . A `custom name` like `users_address` will complement the `"Users Address"` table, so that it can be
added to the GraphQL schema.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "pg_track_table" ,
    "args" :   {
      "source" :   "default" ,
      "table" :   "Author Details" ,
      "configuration" :   {
         "custom_name" :   "author_details"
      }
    }
}
```

The GraphQL nodes and typenames that are generated will be according to the `identifier` . For example, in this case, the
nodes generated will be:

- `users_address`
- `users_address_one`
- `users_address_aggregate`
- `insert_users_address`
- `insert_users_address_one`
- `update_users_address`
- `update_users_address_by_pk`
- `delete_users_address`
- `delete_users_address_by_pk`


Note

Hasura GraphQL Engine requires the constraint names (if any) of a table to be[ GraphQL compliant ](https://spec.graphql.org/June2018/#sec-Names)in order to be able to track it.

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| configuration | false | [ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config) | Configuration for the table/view |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| apollo_federation_config | false | [ ApolloFederationConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apollofederationconfig) | Apollo federation configuration for the table |


## pg_track_tables​

Supported from

 `pg_track_tables` is supported for versions `v2.26.0` and above.

 `pg_track_tables` is used to track multiple tables at once. It is typically faster to track more than one table using
this API, compared to repeating `pg_track_table` for each table you want to track.

 `pg_track_tables` works in very similar fashion to `pg_track_table` , except it allows you to pass multiple tables,
each using the same args format as `pg_track_table` .

Add two tables/views `author` and `book` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_track_tables" ,
   "args" :   {
     "tables" :   [
       {
         "source" :   "default" ,
         "table" :   "author" ,
         "configuration" :   {
           "custom_root_fields" :   {
             "select" :   "Authors" ,
             "select_by_pk" :   "Author" ,
             "select_aggregate" :   "AuthorAggregate" ,
             "insert" :   "AddAuthors" ,
             "insert_one" : "AddAuthor" ,
             "update" :   "UpdateAuthors" ,
             "update_by_pk" :   "UpdateAuthor" ,
             "delete" :   "DeleteAuthors" ,
             "delete_by_pk" :   "DeleteAuthor"
           } ,
           "column_config" :   {
             "id" :   {
               "custom_name" :   "authorId" ,
               "comment" :   "The ID of the Author"
             }
           } ,
           "comment" :   "Authors of books"
         } ,
         "apollo_federation_config" :   {
           "enable" :   "v1"
         }
       } ,
       {
         "source" :   "default" ,
         "table" :   "book" ,
         "configuration" :   {
           "custom_root_fields" :   {
             "select" :   "Books" ,
             "select_by_pk" :   "Book" ,
             "select_aggregate" :   "BookAggregate" ,
             "insert" :   "AddBooks" ,
             "insert_one" : "AddBook" ,
             "update" :   "UpdateBooks" ,
             "update_by_pk" :   "UpdateBook" ,
             "delete" :   "DeleteBooks" ,
             "delete_by_pk" :   "DeleteBook"
           }
         } ,
         "apollo_federation_config" :   {
           "enable" :   "v1"
         }
       }
     ]
   }
}
```

By default, if some of the tables specified in `pg_track_tables` fail to track, these tables will be skipped.
Information about the tables that failed to track will be returned as warnings in the response.

To track tables in an all-or-nothing fashion, you can disallow warnings by using the `allow_warnings` property:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_track_tables" ,
   "args" :   {
     "allow_warnings" :   false ,
     "tables" :   [
       {
         "source" :   "default" ,
         "table" :   "author"
       } ,
       {
         "source" :   "default" ,
         "table" :   "book"
       }
     ]
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| tables | true | [[ pg_track_table Args ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-track-table-syntax)] | An array of track table arguments. |
| allow_warnings | false | Boolean | If set to `false` , any warnings will cause the API call to fail and no new tables to be tracked. Otherwise tables that fail to track will be raised as warnings. (default: `true` ) |


## pg_untrack_table​

 `untrack_table` is used to remove a table/view from the GraphQL schema.

Remove a table/view `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_untrack_table" ,
   "args" :   {
     "table" :   {
       "schema" :   "public" ,
       "name" :   "author"
     } ,
     "source" :   "default" ,
     "cascade" :   true
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| cascade | false | Boolean | When set to `true` , the effect (if possible) is cascaded to any Metadata dependent objects (relationships, permissions, templates). (default: `false` ) |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_untrack_tables​

Supported from

 `pg_untrack_tables` is supported for versions `v2.26.0` and above.

 `pg_untrack_tables` is used to remove multiple tables/views from the GraphQL schema at once. It is typically faster to
untrack more than one table using this API, compared to repeating `pg_untrack_table` for each table you want to
untrack.

 `pg_untrack_tables` works in very similar fashion to `pg_untrack_table` , except it allows you to pass multiple tables,
each using the same args format as `pg_untrack_table` .

Remove two tables/views, `author` and `book` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_untrack_tables" ,
   "args" :   {
     "tables" :   [
       {
         "table" :   {
           "schema" :   "public" ,
           "name" :   "author"
         } ,
         "source" :   "default" ,
         "cascade" :   true
       } ,
       {
         "table" :   {
           "schema" :   "public" ,
           "name" :   "book"
         } ,
         "source" :   "default" ,
         "cascade" :   true
       }
     ]
   }
}
```

By default, if some of the tables specified in `pg_untrack_tables` fail to untrack, these tables will be skipped.
Information about the tables that failed to untrack will be returned as warnings in the response.

To untrack tables in an all-or-nothing fashion, you can disallow warnings by using the `allow_warnings` property:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_untrack_tables" ,
   "args" :   {
     "allow_warnings" :   false ,
     "tables" :   [
       {
         "source" :   "default" ,
         "table" :   "author" ,
         "cascade" :   true
       } ,
       {
         "source" :   "default" ,
         "table" :   "book" ,
         "cascade" :   true
       }
     ]
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| tables | true | [[ pg_untrack_table Args ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-untrack-table-syntax)] | An array of untrack table arguments. |
| allow_warnings | false | Boolean | If set to `false` , any warnings will cause the API call to fail and no tables to be untracked. Otherwise tables that fail to untrack will be raised as warnings. (default: `true` ) |


## pg_set_table_is_enum​

 `pg_set_table_is_enum` sets whether an already-tracked table should be used as an[ enum table ](https://hasura.io/docs/latest/schema/postgres/enums/#pg-create-enum-table).

Use table `user_role` as an enum table:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_set_table_is_enum" ,
   "args" :   {
     "table" :   {
       "schema" :   "public" ,
       "name" :   "user_role"
     } ,
     "source" :   "default" ,
     "is_enum" :   true
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| is_enum | true | Boolean | Whether or not the table should be used as an `enum table <enum table>` . |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_set_table_customization​

 `pg_set_table_customization` allows you to customize any given table with a custom name, custom root fields and custom
column names of an already tracked table. This will **replace** the already present customization.

Set the configuration for a table/view called `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_set_table_customization" ,
   "args" :   {
     "table" :   "author_details" ,
     "source" :   "default" ,
     "configuration" :   {
       "identifier" :   "author" ,
       "custom_root_fields" :   {
         "select" :   "Authors" ,
         "select_by_pk" :   "Author" ,
         "select_aggregate" :   "AuthorAggregate" ,
         "insert" :   "AddAuthors" ,
         "insert_one" : "AddAuthor" ,
         "update" :   "UpdateAuthors" ,
         "update_by_pk" :   "UpdateAuthor" ,
         "delete" :   "DeleteAuthors" ,
         "delete_by_pk" :   "DeleteAuthor"
       } ,
       "column_config" :   {
         "id" :   {
           "custom_name" :   "authorId" ,
           "comment" :   "The ID of the Author"
         }
       }
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| configuration | false | [ TableConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config) | Configuration for the table/view |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_set_apollo_federation_config​

 `pg_set_apollo_federation_config` allows you to set apollo federation configuration for an already tracked postgres
table. Enabling Apollo Federation will allow you to use the table type generated by Hasura in other subgraphs.

Set the Apollo Federation configuration for a postgres table called `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_set_apollo_federation_config" ,
   "args" :   {
     "table" :   "author_details" ,
     "source" :   "default" ,
     "apollo_federation_config" :   {
       "enable" :   "v1"
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| apollo_federation_config | false | [ ApolloFederationConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apollofederationconfig) | Configuration for the table/view |


Note

Setting `apollo_federation_config` to `null` will disable Apollo Federation support on the table.

## pg_test_connection_template​

 `pg_test_connection_template` allows you to test the connection template set for a source.

Test the connection template for a postgres source called `default` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_test_connection_template" ,
   "args" :   {
     "source_name" :   "default" ,
     "request_context" :   {
       "headers" :   {
         "x-hasura-id" :   1 ,
         "x-hasura-role" :   "user"
       } ,
       "session" :   {
         "x-hasura-role" :   "user"
       } ,
       "query" :   {
         "operation_type" :   "query" ,
         "operation_name" :   "users_by_pk"
       }
     } ,
     "connection_template" :   {
         "template" :   "{{ if $.request.session?[\"x-hasura-role\"] == \"user\" }} {{$.connection_set.connection_set_member_name}} {{else}} {{$.primary}} {{ end }}"
       }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source_name | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| request_context | true | [ RequestContext ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requestcontext) | Request context |
| connection_template | false | [ PGConnectionTemplate ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgconnectiontemplate) | DB connection template |


Enterprise only

Connection template feature is an enterprise edition only feature.

## mssql_track_table​

 `mssql_track_table` is used to add a table/view to the GraphQL schema with configuration. You can customize the root
field names.

Add a table/view `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_track_table" ,
     "args" :   {
       "table" :   "author" ,
       "source" :   "default"
     }
}
```

Note

Hasura GraphQL Engine requires the constraint names (if any) of a table to be[ GraphQL compliant ](https://spec.graphql.org/June2018/#sec-Names)in order to be able to track it.

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| configuration | false | [ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config) | Configuration for the table/view |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| apollo_federation_config | false | [ ApolloFederationConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apollofederationconfig) | Apollo federation configuration for the table |


## mssql_track_tables​

Supported from

 `mssql_track_tables` is supported for versions `v2.26.0` and above.

 `mssql_track_tables` is used to track multiple tables at once. It is typically faster to track more than one table using
this API, compared to repeating `mssql_track_table` for each table you want to track.

 `mssql_track_tables` works in very similar fashion to `mssql_track_table` , except it allows you to pass multiple tables,
each using the same args format as `mssql_track_table` .

Add two tables/views `author` and `book` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_track_tables" ,
   "args" :   {
     "tables" :   [
       {
         "source" :   "default" ,
         "table" :   "author"
       } ,
       {
         "source" :   "default" ,
         "table" :   "book"
       }
     ]
   }
}
```

By default, if some of the tables specified in `mssql_track_tables` fail to track, these tables will be skipped.
Information about the tables that failed to track will be returned as warnings in the response.

To track tables in an all-or-nothing fashion, you can disallow warnings by using the `allow_warnings` property:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_track_tables" ,
   "args" :   {
     "allow_warnings" :   false ,
     "tables" :   [
       {
         "source" :   "default" ,
         "table" :   "author"
       } ,
       {
         "source" :   "default" ,
         "table" :   "book"
       }
     ]
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| tables | true | [[ mssql_track_table Args ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-track-table-syntax)] | An array of track table arguments. |
| allow_warnings | false | Boolean | If set to `false` , any warnings will cause the API call to fail and no new tables to be tracked. Otherwise tables that fail to track will be raised as warnings. (default: `true` ) |


## mssql_untrack_table​

 `untrack_table` is used to remove a table/view from the GraphQL schema.

Remove a table/view `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_untrack_table" ,
   "args" :   {
     "table" :   {
       "schema" :   "dbo" ,
       "name" :   "author"
     } ,
     "source" :   "default" ,
     "cascade" :   true
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| cascade | false | Boolean | When set to `true` , the effect (if possible) is cascaded to any Metadata dependent objects (relationships, permissions, templates). (default: `false` ) |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_untrack_tables​

Supported from

 `mssql_untrack_tables` is supported for versions `v2.26.0` and above.

 `mssql_untrack_tables` is used to remove multiple tables/views from the GraphQL schema at once. It is typically faster to
untrack more than one table using this API, compared to repeating `mssql_untrack_table` for each table you want to
untrack.

 `mssql_untrack_tables` works in very similar fashion to `mssql_untrack_table` , except it allows you to pass multiple tables,
each using the same args format as `mssql_untrack_table` .

Remove two tables/views, `author` and `book` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_untrack_tables" ,
   "args" :   {
     "tables" :   [
       {
         "table" :   {
           "schema" :   "dbo" ,
           "name" :   "author"
         } ,
         "source" :   "default" ,
         "cascade" :   true
       } ,
       {
         "table" :   {
           "schema" :   "dbo" ,
           "name" :   "book"
         } ,
         "source" :   "default" ,
         "cascade" :   true
       }
     ]
   }
}
```

By default, if some of the tables specified in `mssql_untrack_tables` fail to untrack, these tables will be skipped.
Information about the tables that failed to untrack will be returned as warnings in the response.

To untrack tables in an all-or-nothing fashion, you can disallow warnings by using the `allow_warnings` property:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_untrack_tables" ,
   "args" :   {
     "allow_warnings" :   false ,
     "tables" :   [
       {
         "source" :   "default" ,
         "table" :   "author" ,
         "cascade" :   true
       } ,
       {
         "source" :   "default" ,
         "table" :   "book" ,
         "cascade" :   true
       }
     ]
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| tables | true | [[ mssql_untrack_table Args ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-untrack-table-syntax)] | An array of untrack table arguments. |
| allow_warnings | false | Boolean | If set to `false` , any warnings will cause the API call to fail and no tables to be untracked. Otherwise tables that fail to untrack will be raised as warnings. (default: `true` ) |


## mssql_set_table_customization​

 `mssql_set_table_customization` allows you to customize any given table with a custom name, custom root fields and
custom column names of an already tracked table. This will **replace** the already present customization.

Set the configuration for a table/view called `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_set_table_customization" ,
   "args" :   {
     "table" :   "author_details" ,
     "source" :   "default" ,
     "configuration" :   {
       "identifier" :   "author" ,
       "custom_root_fields" :   {
         "select" :   "Authors" ,
         "select_aggregate" :   "AuthorAggregate" ,
       } ,
       "column_config" :   {
         "id" :   {
           "custom_name" :   "authorId" ,
           "comment" :   "The ID of the Author"
         }
       }
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| configuration | false | [ TableConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config) | Configuration for the table/view |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_set_apollo_federation_config​

 `mssql_set_apollo_federation_config` allows you to set apollo federation configuration for an already tracked mssql
table. Enabling Apollo Federation will allow you to use the table type generated by Hasura in other subgraphs.

Set the Apollo Federation configuration for a mssql table called `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_set_apollo_federation_config" ,
   "args" :   {
     "table" :   "author_details" ,
     "source" :   "default" ,
     "apollo_federation_config" :   {
       "enable" :   "v1"
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| apollo_federation_config | false | [ ApolloFederationConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apollofederationconfig) | Configuration for the table/view |


Note

Setting `apollo_federation_config` to `null` will disable Apollo Federation support on the table.

## bigquery_track_table​

 `bigquery_track_table` is used to add a table/view to the GraphQL schema with configuration. You can customize the root
field names.

Add a table/view `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "bigquery_track_table" ,
     "args" :   {
       "table" :   {
         "dataset" :   "hasura" ,
         "name" :   "author" ,
       } ,
       "source" :   "default"
     }
}
```

In the case of BigQuery, dataset names are prefixed to table/view names to form a unique root field name, such that the
above example will result in the root field name being `hasura_author` .

Note

Hasura GraphQL Engine requires the constraint names (if any) of a table to be[ GraphQL compliant ](https://spec.graphql.org/June2018/#sec-Names)in order to be able to track it.

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | {"dataset":_, "name":_} | Name of the table |
| configuration | false | [ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config) | Configuration for the table/view |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| apollo_federation_config | false | [ ApolloFederationConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apollofederationconfig) | Apollo federation configuration for the table |


## bigquery_track_tables​

Supported from

 `bigquery_track_tables` is supported for versions `v2.26.0` and above.

 `bigquery_track_tables` is used to track multiple tables at once. It is typically faster to track more than one table using
this API, compared to repeating `bigquery_track_table` for each table you want to track.

 `bigquery_track_tables` works in very similar fashion to `bigquery_track_table` , except it allows you to pass multiple tables,
each using the same args format as `bigquery_track_table` .

Add two tables/views `author` and `book` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_track_tables" ,
   "args" :   {
     "tables" :   [
       {
         "source" :   "default" ,
         "table" :   {
           "dataset" :   "hasura" ,
           "name" :   "author"
         }
       } ,
       {
         "source" :   "default" ,
         "table" :   {
           "dataset" :   "hasura" ,
           "name" :   "book"
         }
       }
     ]
   }
}
```

By default, if some of the tables specified in `bigquery_track_tables` fail to track, these tables will be skipped.
Information about the tables that failed to track will be returned as warnings in the response.

To track tables in an all-or-nothing fashion, you can disallow warnings by using the `allow_warnings` property:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_track_tables" ,
   "args" :   {
     "allow_warnings" :   false ,
     "tables" :   [
       {
         "source" :   "default" ,
         "table" :   {
           "dataset" :   "hasura" ,
           "name" :   "author"
         }
       } ,
       {
         "source" :   "default" ,
         "table" :   {
           "dataset" :   "hasura" ,
           "name" :   "book"
         }
       }
     ]
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| tables | true | [[ bigquery_track_table Args ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-track-table-syntax)] | An array of track table arguments. |
| allow_warnings | false | Boolean | If set to `false` , any warnings will cause the API call to fail and no new tables to be tracked. Otherwise tables that fail to track will be raised as warnings. (default: `true` ) |


## bigquery_untrack_table​

 `bigquery_untrack_table` is used to remove a table/view from the GraphQL schema.

Remove a table/view `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_untrack_table" ,
   "args" :   {
     "table" :   {
       "dataset" :   "hasura" ,
       "name" :   "author"
     } ,
     "source" :   "default" ,
     "cascade" :   true
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | {"dataset":_, "name":_} | Name of the table |
| cascade | false | Boolean | When set to `true` , the effect (if possible) is cascaded to any Metadata dependent objects (relationships, permissions, templates). (default: `false` ) |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## bigquery_untrack_tables​

Supported from

 `bigquery_untrack_tables` is supported for versions `v2.26.0` and above.

 `bigquery_untrack_tables` is used to remove multiple tables/views from the GraphQL schema at once. It is typically faster to
untrack more than one table using this API, compared to repeating `bigquery_untrack_table` for each table you want to
untrack.

 `bigquery_untrack_tables` works in very similar fashion to `bigquery_untrack_table` , except it allows you to pass multiple tables,
each using the same args format as `bigquery_untrack_table` .

Remove two tables/views, `author` and `book` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_untrack_tables" ,
   "args" :   {
     "tables" :   [
       {
         "table" :   {
           "dataset" :   "hasura" ,
           "name" :   "author"
         } ,
         "source" :   "default" ,
         "cascade" :   true
       } ,
       {
         "table" :   {
           "dataset" :   "hasura" ,
           "name" :   "book"
         } ,
         "source" :   "default" ,
         "cascade" :   true
       }
     ]
   }
}
```

By default, if some of the tables specified in `bigquery_untrack_tables` fail to untrack, these tables will be skipped.
Information about the tables that failed to untrack will be returned as warnings in the response.

To untrack tables in an all-or-nothing fashion, you can disallow warnings by using the `allow_warnings` property:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_untrack_tables" ,
   "args" :   {
     "allow_warnings" :   false ,
     "tables" :   [
       {
         "table" :   {
           "dataset" :   "hasura" ,
           "name" :   "author"
         } ,
         "source" :   "default" ,
         "cascade" :   true
       } ,
       {
         "table" :   {
           "dataset" :   "hasura" ,
           "name" :   "book"
         } ,
         "source" :   "default" ,
         "cascade" :   true
       }
     ]
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| tables | true | [[ bigquery_untrack_table Args ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-untrack-table-syntax)] | An array of untrack table arguments. |
| allow_warnings | false | Boolean | If set to `false` , any warnings will cause the API call to fail and no tables to be untracked. Otherwise tables that fail to untrack will be raised as warnings. (default: `true` ) |


## bigquery_set_table_customization​

 `bigquery_set_table_customization` allows you to customize any given table with a custom name, custom root fields and
custom column names of an already tracked table. This will **replace** the already present customization.

Set the configuration for a table/view called `hasura_author_details` to `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_set_table_customization" ,
   "args" :   {
     "table" :   {
       "dataset" :   "hasura" ,
       "name" :   "author_details" ,
     } ,
     "source" :   "default" ,
     "configuration" :   {
       "custom_name" :   "author" ,
       "custom_root_fields" :   {
         "select" :   "Authors" ,
         "select_aggregate" :   "AuthorAggregate" ,
       } ,
       "column_config" :   {
         "id" :   {
           "custom_name" :   "authorId" ,
           "comment" :   "The ID of the Author"
         }
       }
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | {"dataset":_, "name":_} | Name of the table |
| configuration | false | [ TableConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config) | Configuration for the table/view |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## bigquery_set_apollo_federation_config​

 `bigquery_set_apollo_federation_config` allows you to set apollo federation configuration for an already tracked
bigquery table. Enabling Apollo Federation will allow you to use the table type generated by Hasura in other subgraphs.

Set the Apollo Federation configuration for a bigquery table called `author` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_set_apollo_federation_config" ,
   "args" :   {
     "table" :   "author_details" ,
     "source" :   "default" ,
     "apollo_federation_config" :   {
       "enable" :   "v1"
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| apollo_federation_config | false | [ ApolloFederationConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apollofederationconfig) | Configuration for the table/view |


Note

Setting `apollo_federation_config` to `null` will disable Apollo Federation support on the table.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#introduction)
- [ pg_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-track-table)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-track-table-syntax)
- [ pg_track_tables ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-track-tables)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-track-tables-syntax)
- [ pg_untrack_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-untrack-table)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-untrack-table-syntax)
- [ pg_untrack_tables ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-untrack-tables)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-untrack-tables-syntax)
- [ pg_set_table_is_enum ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-set-table-is-enum)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-set-table-is-enum-syntax)
- [ pg_set_table_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-set-table-customization)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-set-table-customization-syntax)
- [ pg_set_apollo_federation_config ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-set-apollo-federation-config)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-set-apollo-federation-config-syntax)
- [ pg_test_connection_template ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-test-connection-template)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-pg-test-connection-template-syntax)
- [ mssql_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-track-table)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-track-table-syntax)
- [ mssql_track_tables ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-track-tables)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-track-tables-syntax)
- [ mssql_untrack_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-untrack-table)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-untrack-table-syntax)
- [ mssql_untrack_tables ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-untrack-tables)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-untrack-tables-syntax)
- [ mssql_set_table_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-set-table-customization)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#mssql-set-table-customization-syntax)
- [ mssql_set_apollo_federation_config ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-mssql-set-apollo-federation-config)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-mssql-set-apollo-federation-config-syntax)
- [ bigquery_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-track-table)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-track-table-syntax)
- [ bigquery_track_tables ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-track-tables)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-track-tables-syntax)
- [ bigquery_untrack_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-untrack-table)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-untrack-table-syntax)
- [ bigquery_untrack_tables ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-untrack-tables)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-untrack-tables-syntax)
- [ bigquery_set_table_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-set-table-customization)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-set-table-customization-syntax)
- [ bigquery_set_apollo_federation_config ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-set-apollo-federation-config)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#mssql-set-table-customization/#metadata-bigquery-set-apollo-federation-config-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)