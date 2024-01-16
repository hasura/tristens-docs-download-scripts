# Schema/Metadata API Reference: Tables/Views (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will continue to function.

## Introduction​

Track/untrack a table/view in Hasura GraphQL Engine.

Only tracked tables/views are available for querying/mutating/subscribing data over the GraphQL API.

## track_table​

 `track_table` is used to add a table/view to the GraphQL schema.

Add a table/view `author` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "track_table" ,
     "args" :   {
         "schema" :   "public" ,
         "name" :   "author"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| is_enum | false | Boolean | When set to `true` , creates the table as an[ enum table ](https://hasura.io/docs/latest/schema/postgres/enums/#pg-create-enum-table). |
| apollo_federation_config | false | [ ApolloFederationConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apollofederationconfig) | Apollo federation configuration for the table |


## set_table_is_enum​

 `set_table_is_enum` sets whether an already-tracked table should be used as an[ enum table ](https://hasura.io/docs/latest/schema/postgres/enums/#pg-create-enum-table).

Use table `user_role` as an enum table:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "set_table_is_enum" ,
   "args" :   {
     "table" :   {
       "schema" :   "public" ,
       "name" :   "user_role"
     } ,
     "is_enum" :   true
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| is_enum | true | Boolean | Whether or not the table should be used as an `enum table <enum table>` . |


## track_table v2​

Version 2 of `track_table` is used to add a table/view to the GraphQL schema with configuration. You can customize the
root field names.

Add a table/view `author` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "track_table" ,
    "version" :   2 ,
    "args" :   {
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
         "custom_column_names" :   {
            "id" :   "authorId"
         }
      }
    }
}
```

A table can be tracked with a `custom name` . This can be useful when a table name is not GraphQL compliant, like `Users Address` . A `custom name` like `users_address` will complement the `"Users Address"` table, so that it can be
added to the GraphQL schema.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "track_table" ,
    "version" :   2 ,
    "args" :   {
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

GraphQL Engine requires the constraint names (if any) of a table to be[ GraphQL compliant ](https://spec.graphql.org/June2018/#sec-Names)in order to be able to track it.

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| configuration | false | [ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config) | Configuration for the table/view |
| apollo_federation_config | false | [ ApolloFederationConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#apollofederationconfig) | Apollo federation configuration for the table |


## set_table_custom_fields (deprecated)​

 `set_table_custom_fields` has been deprecated. Use the[ set_table_customization ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-set-table-customization)API to set the custom table fields.

 `set_table_custom_fields` in version `2` sets the custom root fields and custom column names of already tracked table.
This will **replace** the already present custom fields configuration.

Set custom fields for table/view `author` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "set_table_custom_fields" ,
    "version" :   2 ,
    "args" :   {
      "table" :   "author" ,
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
      "custom_column_names" :   {
         "id" :   "authorId"
      }
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| custom_root_fields | false | [ Custom Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#custom-root-fields) | Customize the root fields |
| custom_column_names | false | [ CustomColumnNames ](https://hasura.io/docs/latest/api-reference/syntax-defs/#customcolumnnames) | Customize the column fields |


## set_table_customization​

 `set_table_customization` allows you to customize any given table with a custom name, custom root fields and custom
column names of an already tracked table. This will **replace** the already present customization.

[ set_table_custom_fields ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-set-table-custom-fields)has been deprecated in favour of this API.

Set the configuration for a table/view called `author` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "set_table_customization" ,
    "args" :   {
      "table" :   "author_details" ,
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
        "custom_column_names" :   {
           "id" :   "authorId"
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


## untrack_table​

 `untrack_table` is used to remove a table/view from the GraphQL schema.

Remove a table/view `author` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "untrack_table" ,
     "args" :   {
         "table" :   {
             "schema" :   "public" ,
             "name" :   "author"
          } ,
         "cascade" :   true
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| cascade | false | Boolean | When set to `true` , the effect (if possible) is cascaded to any Metadata dependent objects (relationships, permissions, templates) |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#introduction)
- [ track_table ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-track-table)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-track-table-syntax)
- [ set_table_is_enum ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-set-table-is-enum)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-set-table-is-enum-syntax)
- [ track_table v2 ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-track-table-v2)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-track-table-syntax-v2)
- [ set_table_custom_fields (deprecated) ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-set-table-custom-fields)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-set-table-custom-fields-syntax)
- [ set_table_customization ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-set-table-customization)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-set-table-customization-syntax)
- [ untrack_table ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-untrack-table)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum/#schema-metadata-untrack-table-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)