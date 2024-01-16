# BigQuery: Customize Auto-Generated Field Names

## Introduction​

Hasura auto-generates GraphQL field names based on your database table and column names. If you'd like to change the
defaults, it is possible to override and rename the auto-generated table and column field names exposed over the GraphQL
API.

Supported from

This feature is supported in versions `v2.0.8` and later.

## Expose columns with a different name in the GraphQL API​

- Console
- CLI
- API


Console support coming soon

You can customize auto-generated field names in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     dataset :  hasura
     name :  author
   configuration :
     column_config :
       addr :
         custom_name :  address
```

Apply the Metadata by running:

`hasura metadata apply`

A custom field name can be set for a column via the following 2 methods:

1. Passing a[ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config)with the[ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#columnconfig)to the[ bigquery_set_table_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-bigquery-set-table-customization)API while tracking a table:
2. Customization can be done at the time of creation using[ bigquery_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-bigquery-track-table)API also.


Passing a[ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config)with the[ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#columnconfig)to the[ bigquery_set_table_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-bigquery-set-table-customization)API while tracking a table:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_set_table_customization" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "authors" ,
     "configuration" :   {
       "column_config" :   {
         "id" :   {
           "custom_name" :   "AuthorId"
         }
       }
     }
   }
}
```

Customization can be done at the time of creation using[ bigquery_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-bigquery-track-table)API also.

## Expose table root fields with a different name in the GraphQL API​

- Console
- CLI
- API


Console support coming soon

You can expose table root fields with a different name in the GraphQL API in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     dataset :  hasura
     name :  authors
   configuration :
     custom_root_fields :
       select :  authors_aggregate
```

After that, apply the Metadata by running:

`hasura metadata apply`

A custom field name can be set for a table root field via the following 2 methods:

1. Passing a[ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config)with the[ Custom Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#custom-root-fields)to the[ bigquery_set_table_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-bigquery-set-table-customization)API while tracking a table:
2. Customization can be done at the time of creation using[ bigquery_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-bigquery-track-table)API also.


Passing a[ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#table-config)with the[ Custom Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#custom-root-fields)to the[ bigquery_set_table_customization ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-bigquery-set-table-customization)API while tracking a table:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_set_table_customization" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "authors" ,
     "configuration" :   {
       "column_config" :   {
         "id" :   {
           "custom_name" :   "AuthorId"
         }
       } ,
       "custom_root_fields" :   {
         "select" :   "authors" ,
         "select_aggregate" :   "authors_aggregate"
       }
     }
   }
}
```

Customization can be done at the time of creation using[ bigquery_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-bigquery-track-table)API also.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/bigquery/custom-field-names/#introduction)
- [ Expose columns with a different name in the GraphQL API ](https://hasura.io/docs/latest/schema/bigquery/custom-field-names/#expose-columns-with-a-different-name-in-the-graphql-api)
- [ Expose table root fields with a different name in the GraphQL API ](https://hasura.io/docs/latest/schema/bigquery/custom-field-names/#expose-table-root-fields-with-a-different-name-in-the-graphql-api)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)