# Metadata API Reference: Databases

## Introduction​

Add/remove databases in Hasura GraphQL Engine.

Supported from

The Metadata API is supported for versions `v2.0.0` and above and
replaces the older[ schema/Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

## pg_add_source​

 `pg_add_source` is used to connect a Postgres database to Hasura.

Add a database with name `pg1` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_add_source" ,
   "args" :   {
     "name" :   "pg1" ,
     "configuration" :   {
       "connection_info" :   {
         "database_url" :   {
            "from_env" :   "<DB_URL_ENV_VAR>"
          } ,
         "pool_settings" :   {
           "max_connections" :   50 ,
           "idle_timeout" :   180 ,
           "retries" :   1 ,
           "pool_timeout" :   360 ,
           "connection_lifetime" :   600
         } ,
         "use_prepared_statements" :   true ,
         "isolation_level" :   "read-committed"
       } ,
       "connection_template" :   {
         "template" :   "{{ if $.request.session?[\"x-hasura-role\"] == \"admin\" }} {{$.primary}} {{else}} {{$.connection_set.db_1}} {{ end }}"
       } ,
       "connection_set" :   [
         {
           "name" :   "db_1" ,
           "connection_info" :   {
             "database_url" :   {
               "from_env" :   "<DB_URL_ENV_VAR>"
             }
           }
         }
       ]
     } ,
     "replace_configuration" :   false ,
     "customization" :   {
       "root_fields" :   {
         "namespace" :   "some_field_name" ,
         "prefix" :   "some_field_name_prefix" ,
         "suffix" :   "some_field_name_suffix"
       } ,
       "type_names" :   {
         "prefix" :   "some_type_name_prefix" ,
         "suffix" :   "some_type_name_suffix"
       } ,
       "naming_convention" :   "hasura-default"
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the Postgres database |
| configuration | true | [ PGConfiguration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgconfiguration) | Database connection configuration |
| replace_configuration | false | Boolean | If set to `true` the configuration and customization will be replaced if the source with given name already exists (default: `false` ) |
| customization | false | [ SourceCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcecustomization) | Customize root fields and type names for the source |


Deprecated field

The `replace_configuration` field is deprecated in favour of the[ pg_update_source API ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#metadata-pg-update-source).

Note

The schema specified in the `extensions_schema` is expected to exist in the[ search path ](https://www.postgresql.org/docs/current/ddl-schemas.html#DDL-SCHEMAS-PATH)of your database.

## pg_drop_source​

 `pg_drop_source` is used to remove a Postgres database from Hasura.

Remove a database with name `pg1` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_drop_source" ,
   "args" :   {
     "name" :   "pg1" ,
     "cascade" :   true
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the Postgres database |
| cascade | false | Boolean | When set to `true` , the effect (if possible) is cascaded to any Metadata dependent objects (relationships, permissions etc.) from other sources (default: `false` ) |


## pg_get_source_tables​

 `pg_get_source_tables` is used to list the tables available on a given Postgres
database.

List the tables available on a database with name `pg1` :

```
{
  "type": "pg_get_source_tables",
  "args": {
    "source": "pg1"
  }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the Postgres database |


## rename_source​

 `rename_source` is used to rename an existing source.

Given there already exists a database with name `pg1` , we can rename it to `pg2` using:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "rename_source" ,
   "args" :   {
     "name" :   "pg1" ,
     "new_name" :   "pg2"
   }
}
```

Note that all settings are kept, only the name is changed.

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the database |
| new_name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the database |


## pg_update_source​

 `pg_update_source` is used to update Postgres source in Hasura.

Update a database with name `pg1` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_update_source" ,
   "args" :   {
     "name" :   "pg1" ,
     "configuration" :   {
       "connection_info" :   {
         "database_url" :   {
            "from_env" :   "<DB_URL_ENV_VAR>"
          } ,
         "pool_settings" :   {
           "max_connections" :   50 ,
           "idle_timeout" :   180 ,
           "retries" :   1 ,
           "pool_timeout" :   360 ,
           "connection_lifetime" :   600
         } ,
         "use_prepared_statements" :   true ,
         "isolation_level" :   "read-committed" ,
       }
     } ,
     "customization" :   {
       "root_fields" :   {
         "namespace" :   "some_field_name" ,
         "prefix" :   "some_field_name_prefix" ,
         "suffix" :   "some_field_name_suffix"
       } ,
       "type_names" :   {
         "prefix" :   "some_type_name_prefix" ,
         "suffix" :   "some_type_name_suffix"
       } ,
       "naming_convention" :   "hasura-default"
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the Postgres database |
| configuration | false | [ PGConfiguration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgconfiguration) | Database connection configuration |
| customization | false | [ SourceCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcecustomization) | Customize root fields and type names for the source |


## mssql_add_source​

 `mssql_add_source` is used to connect an MS SQL Server database to Hasura.

Add a database with name `mssql1` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_add_source" ,
   "args" :   {
     "name" :   "mssql1" ,
     "configuration" :   {
       "connection_info" :   {
         "connection_string" :   {
            "from_env" :   "<CONN_STRING_ENV_VAR>"
          } ,
         "pool_settings" :   {
           "max_connections" :   50 ,
           "idle_timeout" :   180
         }
       }
     } ,
     "customization" :   {
       "root_fields" :   {
         "namespace" :   "some_field_name" ,
         "prefix" :   "some_field_name_prefix" ,
         "suffix" :   "some_field_name_suffix"
       } ,
       "type_names" :   {
         "prefix" :   "some_type_name_prefix" ,
         "suffix" :   "some_type_name_suffix"
       }
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the MS SQL Server database |
| configuration | true | [ MsSQLConfiguration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#mssqlconfiguration) | Database connection configuration |
| replace_configuration | false | Boolean | If set to `true` the configuration and customization will be replaced if the source with given name already exists (default: `false` ) |
| customization | false | [ SourceCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcecustomization) | Customize root fields and type names for the source |


Deprecated field

The `replace_configuration` field is deprecated in favour of the[ mssql_update_source API ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source).

## mssql_drop_source​

 `mssql_drop_source` is used to remove an MS SQL Server database from Hasura.

Remove a database with name `mssql1` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_drop_source" ,
   "args" :   {
     "name" :   "mssql1"
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the MS SQL Server database |
| cascade | false | Boolean | When set to `true` , the effect (if possible) is cascaded to any Metadata dependent objects (relationships, permissions etc.) from other sources (default: `false` ) |


## mssql_get_source_tables​

 `mssql_get_source_tables` is used to list the tables available on a given
MS SQL Server database.

List the tables available on a database with name `mssql1` :

```
{
  "type": "mssql_get_source_tables",
  "args": {
    "source": "mssql1"
  }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the MS SQL Server database |


## mssql_update_source​

 `mssql_update_source` is used to update an already existing MS SQL Server source in Hasura.

Update a database with name `mssql1` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_update_source" ,
   "args" :   {
     "name" :   "mssql1" ,
     "configuration" :   {
       "connection_info" :   {
         "connection_string" :   {
            "from_env" :   "<CONN_STRING_ENV_VAR>"
          } ,
         "pool_settings" :   {
           "max_connections" :   50 ,
           "idle_timeout" :   180
         }
       }
     } ,
     "customization" :   {
       "root_fields" :   {
         "namespace" :   "some_field_name" ,
         "prefix" :   "some_field_name_prefix" ,
         "suffix" :   "some_field_name_suffix"
       } ,
       "type_names" :   {
         "prefix" :   "some_type_name_prefix" ,
         "suffix" :   "some_type_name_suffix"
       }
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the MS SQL Server database |
| configuration | false | [ MsSQLConfiguration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#mssqlconfiguration) | Database connection configuration |
| customization | false | [ SourceCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcecustomization) | Customize root fields and type names for the source |


## bigquery_add_source​

 `bigquery_add_source` is used to connect a BigQuery database to Hasura.

Add a database with name `bigquery1` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_add_source" ,
   "args" :   {
     "name" :   "bigquery1" ,
     "configuration" :   {
       "service_account" :   "bigquery_service_account" ,
       "project_id" :   "bigquery_project_id" ,
       "datasets" :   [ "dataset1" ,   "dataset2" ]
     } ,
     "customization" :   {
       "root_fields" :   {
         "namespace" :   "some_field_name" ,
         "prefix" :   "some_field_name_prefix" ,
         "suffix" :   "some_field_name_suffix"
       } ,
       "type_names" :   {
         "prefix" :   "some_type_name_prefix" ,
         "suffix" :   "some_type_name_suffix"
       }
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the BigQuery database |
| configuration | true | [ BigQueryConfiguration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#bigqueryconfiguration) | Database connection configuration |
| replace_configuration | false | Boolean | If set to `true` the configuration and customization will be replaced if the source with given name already exists (default: `false` ) |
| customization | false | [ SourceCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcecustomization) | Customize root fields and type names for the source |


Deprecated field

The `replace_configuration` field is deprecated in favour of the[ bigquery_update_source API ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#metadata-bigquery-update-source).

## bigquery_drop_source​

 `bigquery_drop_source` is used to remove a BigQuery database from Hasura.

Remove a database with name `bigquery1` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_drop_source" ,
   "args" :   {
     "name" :   "bigquery1"
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the BigQuery database |
| cascade | false | Boolean | When set to `true` , the effect (if possible) is cascaded to any Metadata dependent objects (relationships, permissions etc.) from other sources (default: `false` ) |


## bigquery_update_source​

 `bigquery_update_source` is used to update an already existing BigQuery source in Hasura.

Update a database with name `bigquery1` :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_update_source" ,
   "args" :   {
     "name" :   "bigquery1" ,
     "configuration" :   {
       "service_account" :   "bigquery_service_account" ,
       "project_id" :   "bigquery_project_id" ,
       "datasets" :   [ "dataset1" ,   "dataset2" ]
     } ,
     "customization" :   {
       "root_fields" :   {
         "namespace" :   "some_field_name" ,
         "prefix" :   "some_field_name_prefix" ,
         "suffix" :   "some_field_name_suffix"
       } ,
       "type_names" :   {
         "prefix" :   "some_type_name_prefix" ,
         "suffix" :   "some_type_name_suffix"
       }
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the BigQuery database |
| configuration | false | [ BigQueryConfiguration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#bigqueryconfiguration) | Database connection configuration |
| customization | false | [ SourceCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcecustomization) | Customize root fields and type names for the source |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#introduction)
- [ pg_add_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-pg-add-source)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-pg-add-source-syntax)
- [ pg_drop_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-pg-drop-source)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-pg-drop-source-syntax)
- [ pg_get_source_tables ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-pg-get-source-tables)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-pg-get-source-tables-syntax)
- [ rename_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-rename-source)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-rename-source-syntax)
- [ pg_update_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-pg-update-source)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-pg-update-source-syntax)
- [ mssql_add_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#mssql-add-source)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#mssql-add-source-syntax)
- [ mssql_drop_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#mssql-drop-source)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#mssql-drop-source-syntax)
- [ mssql_get_source_tables ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#mssql-get-source-tables)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#mssql-get-source-tables-syntax)
- [ mssql_update_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#mssql-update-source)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#mssql-update-source-syntax)
- [ bigquery_add_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-bigquery-add-source)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-bigquery-add-source-syntax)
- [ bigquery_drop_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-bigquery-drop-source)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-bigquery-drop-source-syntax)
- [ bigquery_update_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-bigquery-update-source)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#mssql-update-source-syntax/#metadata-bigquery-update-source-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)