# Metadata API Reference: Native Queries

## Introduction​

Track/untrack Native Queries in the Hasura GraphQL Engine.

Supported from

Native queries are supported from v2.26.0.

## pg_track_native_query​

 `pg_track_native_query` is used to add a Native Query to the GraphQL schema.

Track a Native Query as follows:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_track_native_query" ,
   "args" :   {
     "source" :   "default" ,
     "root_field_name" :   "<name>" ,
     "type" :   "query" ,
     "arguments" :   {
       "<name>" :   {
         "type" :   "<postgres field type>" ,
         "nullable" :   false  |  true ,
         "description" :   "<optional field description>"
       }
     } ,
     "array_relationships" :  <Native Query relationship> ,
     "object_relationshps" :  <Native Query relationship> ,
     "code" :   "<SQL query>" ,
     "returns" :   "<logical model name>"
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| root_field_name | true | [ QueryName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#queryname) | Name of the Native Query |
| type | false |  `"query"`  | The type of the GraphQL query (currently must be `"query"` ) |
| arguments | false | Mapping from String to[ NativeQueryArgument ](https://hasura.io/docs/latest/api-reference/syntax-defs/#nativequeryargument) | Configuration for each argument |
| code | true | String | The SQL to run on request |
| returns | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the logical model representing the resulting schema |


### Native Query relationships​

See[ Native Query relationship ](https://hasura.io/docs/latest/api-reference/syntax-defs/#nativequeryrelationship).

## pg_untrack_native_query​

 `pg_untrack_native_query` is used to remove a Native Query from the GraphQL schema.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_untrack_native_query" ,
     "args" :   {
       "source" :   "default" ,
       "root_field_name" :   "<name>"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| root_field_name | true | [ QueryName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#queryname) | Name of the Native Query |


## mssql_track_native_query​

 `mssql_track_native_query` is used to add a Native Query to the GraphQL schema.

Track a Native Query as follows:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_track_native_query" ,
   "args" :   {
     "source" :   "default" ,
     "root_field_name" :   "<name>" ,
     "type" :   "query" ,
     "arguments" :   {
       "<name>" :   {
         "type" :   "<mssql field type>" ,
         "nullable" :   false  |  true ,
         "description" :   "<optional field description>"
       }
     } ,
     "array_relationships" :  <Native Query relationship> ,
     "object_relationshps" :  <Native Query relationship> ,
     "code" :   "<SQL query>" ,
     "returns" :   "<logical model name>"
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| root_field_name | true | [ QueryName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#queryname) | Name of the Native Query |
| type | false |  `"query"`  | The type of the GraphQL query (currently must be `"query"` ) |
| arguments | false | Mapping from String to[ NativeQueryArgument ](https://hasura.io/docs/latest/api-reference/syntax-defs/#nativequeryargument) | Configuration for each argument |
| code | true | String | The SQL to run on request |
| returns | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the logical model representing the resulting schema |


## mssql_untrack_native_query​

 `mssql_untrack_native_query` is used to remove a Native Query from the GraphQL schema.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_untrack_native_query" ,
     "args" :   {
       "source" :   "default" ,
       "root_field_name" :   "<name>"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| root_field_name | true | [ QueryName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#queryname) | Name of the Native Query |


## bigquery_track_native_query​

 `bigquery_track_native_query` is used to add a Native Query to the GraphQL schema.

Track a Native Query as follows:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_track_native_query" ,
   "args" :   {
     "source" :   "default" ,
     "root_field_name" :   "<name>" ,
     "type" :   "query" ,
     "arguments" :   {
       "<name>" :   {
         "type" :   "<bigquery field type>" ,
         "nullable" :   false  |  true ,
         "description" :   "<optional field description>"
       }
     } ,
     "array_relationships" :  <Native Query relationship> ,
     "object_relationshps" :  <Native Query relationship> ,
     "code" :   "<SQL query>" ,
     "returns" :   "<logical model name>"
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| root_field_name | true | [ QueryName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#queryname) | Name of the Native Query |
| type | false |  `"query"`  | The type of the GraphQL query (currently must be `"query"` ) |
| arguments | false | Mapping from String to[ NativeQueryArgument ](https://hasura.io/docs/latest/api-reference/syntax-defs/#nativequeryargument) | Configuration for each argument |
| code | true | String | The SQL to run on request |
| returns | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the logical model representing the resulting schema |


## bigquery_untrack_native_query​

 `bigquery_untrack_native_query` is used to remove a Native Query from the GraphQL schema.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "bigquery_untrack_native_query" ,
     "args" :   {
       "source" :   "default" ,
       "root_field_name" :   "<name>"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database (default: `default` ) |
| root_field_name | true | [ QueryName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#queryname) | Name of the Native Query |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#introduction)
- [ pg_track_native_query ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-pg-track-native-query)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-pg-track-native-query-syntax)

- [ Native Query relationships ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#native-query-relationships)
- [ pg_untrack_native_query ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-pg-untrack-native-query)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-pg-untrack-native-query-syntax)
- [ mssql_track_native_query ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-mssql-track-native-query)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-mssql-track-native-query-syntax)
- [ mssql_untrack_native_query ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-mssql-untrack-native-query)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-mssql-untrack-native-query-syntax)
- [ bigquery_track_native_query ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-bigquery-track-native-query)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-bigquery-track-native-query-syntax)
- [ bigquery_untrack_native_query ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-bigquery-untrack-native-query)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/native-queries/#metadata-mssql-untrack-native-query/#metadata-bigquery-untrack-native-query-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)