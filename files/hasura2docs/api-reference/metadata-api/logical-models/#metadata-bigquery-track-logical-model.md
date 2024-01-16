# Metadata API Reference: Logical models

## Introduction​

Track/untrack Logical Models in the Hasura GraphQL Engine.

Supported from

Logical models are supported from v2.26.0.

## pg_track_logical_model​

 `pg_track_logical_model` is used to add a Logical Model to the GraphQL schema.

Track a Logical Model as follows:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_track_logical_model" ,
   "args" :   {
     "source" :   "default" ,
     "name" :   "<name>" ,
     "fields" :   [
       {
         "name" :   "<field name>" ,
         "type" :   "<PostgreSQL field type>" ,
         "nullable" :   false  |  true ,
         "description" :   "<optional field description>"
       } ,
      ...
     ]
   }
}
```

The type of each field can be either a[ PostgreSQL data type ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/)or references to other Logical Models, and each field can be marked as nullable or not, see[ LogicalModelType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodeltype).

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |
| fields | false | Array of[ LogicalModelField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelfield) | Configuration for each field exposed by the Logical Model GraphQL type |


## pg_untrack_logical_model​

 `pg_untrack_logical_model` is used to remove a Logical Model from the GraphQL schema.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_untrack_logical_model" ,
     "args" :   {
       "source" :   "default" ,
       "name" :   "<name>"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |


## pg_create_logical_model_select_permission​

 `pg_create_logical_model_select_permission` is used to add a permission to an existing Logical Model.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_logical_model_select_permission" ,
   "args" :   {
     "source" :   "default" ,
     "name" :   "<logical model name>" ,
     "role" :   "<role name>" ,
     "permission" :   {
       "columns" :   "*"  |  [
         "column 1" ,
         "column 2" ,
        ...
       ] ,
       "filter" :  <boolean expression>
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the role |
| permission | true | [ LogicalModelSelectPermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelselectpermission) | Permission configuration |


## pg_drop_logical_model_select_permission​

 `pg_drop_logical_model_select_permission` is used to drop an existing Logical Model permission.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_drop_logical_model_select_permission" ,
     "args" :   {
        "source" :   "default" ,
        "function" :   "get_articles" ,
        "role" :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the role |


## mssql_track_logical_model​

 `mssql_track_logical_model` is used to add a Logical Model to the GraphQL schema.

Track a Logical Model as follows:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_track_logical_model" ,
   "args" :   {
     "source" :   "default" ,
     "name" :   "<name>" ,
     "fields" :   [
       {
         "name" :   "<field name>" ,
         "type" :   "<SQL Server field type>" ,
         "nullable" :   false  |  true ,
         "description" :   "<optional field description>"
       } ,
      ...
     ]
   }
}
```

The type of each field can be either a SQL Server data type
or references to other Logical Models, and each field can be marked as nullable or not, see[ LogicalModelType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodeltype).

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |
| fields | false | Array of[ LogicalModelField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelfield) | Configuration for each field exposed by the Logical Model GraphQL type |


## mssql_untrack_logical_model​

 `mssql_untrack_logical_model` is used to remove a Logical Model from the GraphQL schema.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_untrack_logical_model" ,
     "args" :   {
       "source" :   "default" ,
       "name" :   "<name>"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |


## mssql_create_logical_model_select_permission​

 `mssql_create_logical_model_select_permission` is used to add a permission to an existing Logical Model.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_create_logical_model_select_permission" ,
   "args" :   {
     "source" :   "default" ,
     "name" :   "<logical model name>" ,
     "role" :   "<role name>" ,
     "permission" :   {
       "columns" :   "*"  |  [
         "column 1" ,
         "column 2" ,
        ...
       ] ,
       "filter" :  <boolean expression>
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the role |
| permission | true | [ LogicalModelSelectPermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelselectpermission) | Permission configuration |


## mssql_drop_logical_model_select_permission​

 `mssql_drop_logical_model_select_permission` is used to drop an existing Logical Model permission.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_drop_logical_model_select_permission" ,
     "args" :   {
        "source" :   "default" ,
        "function" :   "get_articles" ,
        "role" :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the role |


## bigquery_track_logical_model​

 `bigquery_track_logical_model` is used to add a Logical Model to the GraphQL schema.

Track a Logical Model as follows:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_track_logical_model" ,
   "args" :   {
     "source" :   "default" ,
     "name" :   "<name>" ,
     "fields" :   [
       {
         "name" :   "<field name>" ,
         "type" :   "<BigQuery field type>" ,
         "nullable" :   false  |  true ,
         "description" :   "<optional field description>"
       } ,
      ...
     ]
   }
}
```

The type of each field can be either a[ BigQuery data type ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/)or references to other Logical Models, and each field can be marked as nullable or not, see[ LogicalModelType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodeltype).

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |
| fields | false | Array of[ LogicalModelField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelfield) | Configuration for each field exposed by the Logical Model GraphQL type |


## bigquery_untrack_logical_model​

 `bigquery_untrack_logical_model` is used to remove a Logical Model from the GraphQL schema.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "bigquery_untrack_logical_model" ,
     "args" :   {
       "source" :   "default" ,
       "name" :   "<name>"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |


## bigquery_create_logical_model_select_permission​

 `bigquery_create_logical_model_select_permission` is used to add a permission to an existing Logical Model.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_create_logical_model_select_permission" ,
   "args" :   {
     "source" :   "default" ,
     "name" :   "<logical model name>" ,
     "role" :   "<role name>" ,
     "permission" :   {
       "columns" :   "*"  |  [
         "column 1" ,
         "column 2" ,
        ...
       ] ,
       "filter" :  <boolean expression>
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the role |
| permission | true | [ LogicalModelSelectPermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelselectpermission) | Permission configuration |


## bigquery_drop_logical_model_select_permission​

 `bigquery_drop_logical_model_select_permission` is used to drop an existing Logical Model permission.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "bigquery_drop_logical_model_select_permission" ,
     "args" :   {
        "source" :   "default" ,
        "function" :   "get_articles" ,
        "role" :   "user"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| name | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the Logical Model |
| role | true | [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#rolename) | Name of the role |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#introduction)
- [ pg_track_logical_model ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-pg-track-logical-model)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-pg-track-logical-model-syntax)
- [ pg_untrack_logical_model ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-pg-untrack-logical-model)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-pg-untrack-logical-model-syntax)
- [ pg_create_logical_model_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-pg-create-logical-model-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-pg-create-logical-model-select-permission-syntax)
- [ pg_drop_logical_model_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-pg-drop-logical-model-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-pg-drop-logical-model-select-permission-syntax)
- [ mssql_track_logical_model ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-mssql-track-logical-model)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-mssql-track-logical-model-syntax)
- [ mssql_untrack_logical_model ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-mssql-untrack-logical-model)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-mssql-untrack-logical-model-syntax)
- [ mssql_create_logical_model_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-mssql-create-logical-model-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-mssql-create-logical-model-select-permission-syntax)
- [ mssql_drop_logical_model_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-mssql-drop-logical-model-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-mssql-drop-logical-model-select-permission-syntax)
- [ bigquery_track_logical_model ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-bigquery-track-logical-model)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-bigquery-track-logical-model-syntax)
- [ bigquery_untrack_logical_model ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-bigquery-untrack-logical-model)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-bigquery-untrack-logical-model-syntax)
- [ bigquery_create_logical_model_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-bigquery-create-logical-model-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-bigquery-create-logical-model-select-permission-syntax)
- [ bigquery_drop_logical_model_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-bigquery-drop-logical-model-select-permission)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/logical-models/#metadata-bigquery-track-logical-model/#metadata-bigquery-drop-logical-model-select-permission-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)