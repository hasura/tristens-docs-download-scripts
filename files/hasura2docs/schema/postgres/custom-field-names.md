# Postgres: Customize Auto-Generated Field Names

## Introduction​

Hasura auto-generates GraphQL field names based on your database table and column names. If you'd like to change the
defaults, it is possible to override and rename the auto-generated table and column field names exposed over the GraphQL
API.

Supported from

This feature is supported in versions `v1.0.0-beta.8` and later.

## Expose columns with a different name in the GraphQL API​

- Console
- CLI
- API


Head to the `Data -> [table-name] -> Modify` . On the relevant field, click `Edit` and change the GraphQL field name to a
name of your choice.

Image: [ Customize GraphQL field name ](https://hasura.io/docs/assets/images/custom-field-name-column-5fc6adece66b711272f393887908f32f.png)

You can customize auto-generated field names in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  author
   configuration :
     column_config :
       addr :
         custom_name :  address
```

Apply the Metadata by running:

`hasura metadata apply`

A custom field name can be set for a column via the following 2 methods:

1. passing a[ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config)with the[ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#columnconfig)to the[ pg_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-track-table)API while tracking a table:
2. using the[ pg_set_table_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-set-table-customization)API to
set the[ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#columnconfig):


passing a[ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config)with the[ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#columnconfig)to the[ pg_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-track-table)API while tracking a table:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_track_table" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "author" ,
     "configuration" :   {
       "column_config" :   {
         "addr" :   {
           "custom_name" :   "address"
         }
       }
     }
   }
}
```

using the[ pg_set_table_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-set-table-customization)API to
set the[ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#columnconfig):

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_set_table_customization" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "author" ,
     "column_config" :   {
       "addr" :   {
         "custom_name" :   "address"
       }
     }
   }
}
```

## Expose table root fields with a different name in the GraphQL API​

- Console
- CLI
- API


Head to the `Data -> [table-name] -> Modify` . Click the `Edit` button in the `Custom GraphQL Root Fields` section and
define names over which you'd like to expose the table root fields.

Image: [ Customize GraphQL root field ](https://hasura.io/docs/assets/images/custom-field-name-root-fields-a1325bd4179d60ff548cdcb615f635b8.png)

You can expose table root fields with a different name in the GraphQL API in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  author
   configuration :
     custom_root_fields :
       select_by_pk :  author
       select :  authors
```

After that, apply the Metadata by running:

`hasura metadata apply`

A custom field name can be set for a table root field via the following 2 methods:

1. passing a[ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config)with the[ Custom Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#custom-root-fields)names to the[ pg_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-track-table)API while tracking a table:
2. using the[ pg_set_table_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-set-table-customization)Metadata API to set the[ Custom Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#custom-root-fields)names


passing a[ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config)with the[ Custom Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#custom-root-fields)names to the[ pg_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-track-table)API while tracking a table:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_track_table" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "author" ,
     "configuration" :   {
       "custom_root_fields" :   {
         "select" :   "authors" ,
         "select_by_pk" :   "author"
       }
     }
   }
}
```

using the[ pg_set_table_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-set-table-customization)Metadata API to set the[ Custom Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#custom-root-fields)names

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_set_table_customization" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "author" ,
     "custom_root_fields" :   {
         "select" :   "authors" ,
         "select_by_pk" :   "author"
     }
   }
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/custom-field-names/#introduction)
- [ Expose columns with a different name in the GraphQL API ](https://hasura.io/docs/latest/schema/postgres/custom-field-names/#expose-columns-with-a-different-name-in-the-graphql-api)
- [ Expose table root fields with a different name in the GraphQL API ](https://hasura.io/docs/latest/schema/postgres/custom-field-names/#expose-table-root-fields-with-a-different-name-in-the-graphql-api)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)