# Metadata API Reference: Stored Procedures

## Introduction​

Track/untrack Stored Procedures in the Hasura GraphQL Engine.

Supported from

Stored Procedures are supported from v2.26.0.

## mssql_track_stored_procedure​

 `mssql_track_stored_procedure` is used to add a Stored Procedure to the GraphQL schema.

Track a Stored Procedure as follows:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_track_stored_procedure" ,
   "args" :   {
     "source" :  <source-name> ,
     "stored_procedure" :  <name> |  {   "schema" :  <schema-name> ,   "name" :  <procedure-name>  } ,
     "configuration" :   {
       "exposed_as" :   "query" ,
       "custom_name" :  <custom-name>
     } ,
     "arguments" :   {
      <name> :   {
         "type" :   "<type>" ,
         "nullable" :   false  |  true ,
         "description" :  <string>
       }
     } ,
     "returns" :  <logical-model-name>
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database |
| stored_procedure | true | [ QueryName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#queryname) | Name of the stored procedure |
| configuration | true | [ StoredProcedureConfiguration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#stored-procedure-configuration) | Configuration for the Stored Procedure |
| arguments | false | Mapping from String to[ StoredProcedureArgument ](https://hasura.io/docs/latest/api-reference/syntax-defs/#stored-procedure-argument) | Configuration for each argument |
| returns | true | [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#logicalmodelname) | Name of the logical model representing the resulting schema |


## mssql_untrack_stored_procedure​

 `mssql_untrack_stored_procedure` is used to remove a Stored Procedure from the GraphQL schema.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_untrack_stored_procedure" ,
     "args" :   {
       "source" :   "default" ,
       "stored_procedure" :   "<name>"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database |
| stored_procedure | true | [ QueryName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#queryname) | Name of the stored procedure |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/stored-procedures/#introduction)
- [ mssql_track_stored_procedure ](https://hasura.io/docs/latest/api-reference/metadata-api/stored-procedures/#metadata-mssql-track-stored-procedure)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/stored-procedures/#metadata-mssql-track-stored-procedure-syntax)
- [ mssql_untrack_stored_procedure ](https://hasura.io/docs/latest/api-reference/metadata-api/stored-procedures/#metadata-mssql-untrack-stored-procedure)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/stored-procedures/#metadata-pg-untrack-stored-procedure-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)