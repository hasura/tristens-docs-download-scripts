# API Reference: Common Syntax Definitions

## TableName​

```
String |
[ QualifiedTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#qualifiedtable)
```

## QualifiedTable​

```
{
    "name": String,
    "schema": String
}
```

## BigQuery TableName​

```
{
    "name": String,
    "dataset": String
}
```

## SourceName​

 `String` 

## FunctionName​

```
String |
[ QualifiedFunction ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#qualifiedfunction)
```

## QualifiedFunction​

```
{
    "name": String,
    "schema": String
}
```

## BigQuery FunctionName​

```
{
    "name": String,
    "dataset": String
}
```

## LogicalModelName​

 `String` 

## RoleName​

 `String` 

## ComputedFieldName​

 `String` 

## PGConfiguration​

| Key | Required | Schema | Description |
|---|---|---|---|
| connection_info | true | [ PGSourceConnectionInfo ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgsourceconnectioninfo) | Connection parameters for the source |
| read_replicas | false | [[ PGSourceConnectionInfo ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgsourceconnectioninfo)] | Optional list of read replica configuration *(supported only in cloud/enterprise versions)*  |
| extensions_schema | false | String | Name of the schema where the graphql-engine will install database extensions (default: `public` ) |
| connection_template | false | [ PGConnectionTemplate ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgconnectiontemplate) | DB connection template *(supported only in cloud/enterprise versions)*  |
| connection_set | false | [[ ConnectionSetElementConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#connectionsetelementconfig)] | Connection Set used for DB connection template *(supported only in cloud/enterprise versions)*  |


## MsSQLConfiguration​

| Key | Required | Schema | Description |
|---|---|---|---|
| connection_info | true | [ MsSQLSourceConnectionInfo ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#mssqlsourceconnectioninfo) | Connection parameters for the source |
| read_replicas | true | [[ MsSQLSourceConnectionInfo ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#mssqlsourceconnectioninfo)] | Optional list of read replica configuration *(supported only in cloud/enterprise versions)*  |


## BigQueryConfiguration​

| Key | Required | Schema | Description |
|---|---|---|---|
| service_account | true |  `JSON String` | `JSON` |[ FromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#fromenv) | Service account for BigQuery database |
| project_id | true |  `String` |[ FromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#fromenv) | Project Id for BigQuery database |
| datasets | true |  `[String]` |[ FromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#fromenv) | List of BigQuery datasets |
| global_select_limit | false |  `Integer`  | The maximum number of rows that can be returned, defaults to `1000`  |


## PGSourceConnectionInfo​

| Key | Required | Schema | Description |
|---|---|---|---|
| database_url | true |  `String` |[ FromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#fromenv)|[ PGConnectionParameters ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgconnectionparameters)|[ DynamicFromFile ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#dynamicfromfile) | The database connection URL as a string, from an environment variable, as connection parameters, or dynamically read from a file at connect time |
| pool_settings | false | [ PGPoolSettings ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgpoolsettings) | Connection pool settings |
| use_prepared_statements | false | Boolean | If set to `true` the server prepares statement before executing on the source database (default: `false` ). For more details, refer to the[ Postgres docs ](https://www.postgresql.org/docs/current/sql-prepare.html) |
| isolation_level | false |  `read-committed` | `repeatable-read` | `serializable`  | The transaction isolation level in which the queries made to the source will be run with (default: `read-committed` ). |
| ssl_configuration | false | [ PGCertSettings ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcertsettings) | The client SSL certificate settings for the database ( *Only available in Cloud* ). |


Note

When `use_prepared_statements` is `true` , all SQL queries compiled from GraphQL queries will be[ prepared ](https://www.postgresql.org/docs/current/sql-prepare.html)before being executed, meaning that the database
server will cache queries and query plans.

This can result in an improvement in performance when serving mostly complex queries with little variation. But it's a
trade-off that increases memory usage, and under other circumstances the result is not a net performance gain. And
because the prepared statements cache is local to each database connection, the connection pool parameters also
influence its efficiency.

The only way to reasonably know if enabling prepared statements will increase the performance of a Hasura GraphQL Engine
instance is to benchmark it under a representative query load.

This option interacts with the[ Query Tags ](https://hasura.io/docs/latest/observability/query-tags/)feature (see for details), and the two
generally shouldn't be enabled at the same time.

## MsSQLSourceConnectionInfo​

| Key | Required | Schema | Description |
|---|---|---|---|
| connection_string | true |  `String` |[ FromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#fromenv) | The database connection string, or as an environment variable |
| pool_settings | false | [ MsSQLPoolSettings ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#mssqlpoolsettings) | Connection pool settings |
| isolation_level | false |  `read-uncommited` | `read-committed` | `repeatable-read` | `snapshot` | `serializable`  | The transaction isolation level in which the queries made to the source will be run with (default: `read-committed` ). |


## FromEnv​

| Key | Required | Schema | Description |
|---|---|---|---|
| from_env | true |  `String`  | Name of the environment variable |


## DynamicFromFile​

| Key | Required | Schema | Description |
|---|---|---|---|
| dynamic_from_file | true |  `String`  | Filepath to a file containing a connection string. This is read before each connect, and when in use connection errors will force a re-read. For example, this can support environments where passwords are frequently rotated (not supported on Hasura Cloud). To use this the `HASURA_ GRAPHQL_ DYNAMIC_ SECRETS_ ALLOWED_ PATH_ PREFIX` variable must be set and non-empty. Hasura will validate that the path supplied in `dynamic_ from_ file` has the required prefix (e.g., `/path/to/your/secrets` ). |


## PGConnectionParameters​

| Key | Required | Schema | Description |
|---|---|---|---|
| username | true |  `String`  | The Postgres user to be connected |
| password | false |  `String`  | The Postgres user's password |
| database | true |  `String`  | The database name |
| host | true |  `String`  | The name of the host to connect to |
| port | true |  `Integer`  | The port number to connect with, at the server host |


## PGPoolSettings​

| Key | Required | Schema | Description |
|---|---|---|---|
| max_connections | false |  `Integer`  | Maximum number of connections to be kept in the pool (default: 50) |
| total_max_connections | false |  `Integer`  | Maximum number of total connections to be maintained across any number of Hasura Cloud instances (default: 1000). Takes precedence over `max_ connections` in Cloud projects. *(Only available in Hasura Cloud)*  |
| idle_timeout | false |  `Integer`  | The idle timeout (in seconds) per connection (180 seconds for self-hosted & 30 seconds for Cloud). |
| retries | false |  `Integer`  | Number of retries to perform when failing to acquire connection (default: 1). Note that this configuration does not affect user/statement errors on PG. |
| pool_timeout | false |  `Integer`  | Maximum time to wait while acquiring a Postgres connection from the pool, in seconds (default: forever) |
| connection_lifetime | false |  `Integer`  | Time from connection creation after which the connection should be destroyed and a new one created. A value of 0 indicates we should never destroy an active connection. If 0 is passed, memory from large query results may not be reclaimed. (default: 600 sec) |


## PGCertSettings​

| Key | Required | Schema | Description |
|---|---|---|---|
| sslmode | true |  `String`  | The SSL connection mode. See the libpq ssl[ support docs ](https://www.postgresql.org/docs/9.1/libpq-ssl.html)for more details. |
| sslrootcert | false | [ FromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#fromenv) | Environment variable which stores trusted certificate authorities. |
| sslcert | false | [ FromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#fromenv) | Environment variable which stores the client certificate. |
| sslkey | false | [ FromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#fromenv) | Environment variable which stores the client private key. |
| sslpassword | false | [ FromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#fromenv) | Password in the case where the sslkey is encrypted. |


## MsSQLPoolSettings​

Pool settings have two disjoint cases.

This schema indicates that the source uses a connection pool (the default):

| Key | Required | Schema | Description |
|---|---|---|---|
| max_connections | false |  `Integer`  | Maximum number of connections to be kept in the pool (default: 50) |
| total_max_connections | false |  `Integer`  | Maximum number of total connections across any number of Hasura Cloud instances (default: 50). Takes precedence over `max_ connections` in Cloud projects. *(Only available in Cloud)*  |
| idle_timeout | false |  `Integer`  | The idle timeout (in seconds) per connection (default: 5) |


This schema indicates that the source does not use a connection pool:

| Key | Required | Schema | Description |
|---|---|---|---|
| enable | true |  `Bool`  | Set to `false` to disable the connection pool entirely |


## PGColumnType​

`String`

1. Numeric types| Type | Alias | Description |
|---|---|---|
|  `serial`  |  | autoincrementing integer |
|  `bigserial`  |  | autoincrementing bigint |
|  `integer`  |  | 4 bytes, typical choice for integer |
|  `smallint`  |  | 2 bytes |
|  `bigint`  |  | 8 bytes |
|  `real`  |  `float4`  | 6 decimal digits precision, inexact |
|  `double precision`  |  `float8`  | 15 decimal digits precision, inexact |
|  `numeric`  |  `decimal`  | arbitrary precision, exact |
2. Character types| Type | Alias | Description |
|---|---|---|
|  `varchar`  |  `text`  | typical choice for storing string types |
3. Date/Time types| Type | Alias | Description |
|---|---|---|
|  `timestamp with time zone`  |  `timestamptz`  | both date and time, with time zone. Allowed values should be of ISO8601 format. E.g. 2016-07-20T17:30:15Z, 2016-07-20T17:30:15+05:30, 2016-07-20T17:30:15.234890+05:30 |
|  `time with time zone`  |  `timetz`  | time of day only, with time zone. Allowed values should be of ISO8601 format. E.g. 17:30:15Z, 17:30:15+05:30, 17:30:15.234890+05:30 |
|  `date`  |  | date (no time of day). Allowed values are yyyy-mm-dd |
4. Boolean type| Type | Alias | Description |
|---|---|---|
|  `boolean`  |  | state of true or false |
5. JSON types| Type | Alias | Description |
|---|---|---|
|  `json`  |  | Stored as plain text |
|  `jsonb`  |  | Stored in a binary format and can be indexed |


Numeric types

| Type | Alias | Description |
|---|---|---|
|  `serial`  |  | autoincrementing integer |
|  `bigserial`  |  | autoincrementing bigint |
|  `integer`  |  | 4 bytes, typical choice for integer |
|  `smallint`  |  | 2 bytes |
|  `bigint`  |  | 8 bytes |
|  `real`  |  `float4`  | 6 decimal digits precision, inexact |
|  `double precision`  |  `float8`  | 15 decimal digits precision, inexact |
|  `numeric`  |  `decimal`  | arbitrary precision, exact |


Character types

| Type | Alias | Description |
|---|---|---|
|  `varchar`  |  `text`  | typical choice for storing string types |


Date/Time types

| Type | Alias | Description |
|---|---|---|
|  `timestamp with time zone`  |  `timestamptz`  | both date and time, with time zone. Allowed values should be of ISO8601 format. E.g. 2016-07-20T17:30:15Z, 2016-07-20T17:30:15+05:30, 2016-07-20T17:30:15.234890+05:30 |
|  `time with time zone`  |  `timetz`  | time of day only, with time zone. Allowed values should be of ISO8601 format. E.g. 17:30:15Z, 17:30:15+05:30, 17:30:15.234890+05:30 |
|  `date`  |  | date (no time of day). Allowed values are yyyy-mm-dd |


Boolean type

| Type | Alias | Description |
|---|---|---|
|  `boolean`  |  | state of true or false |


JSON types

| Type | Alias | Description |
|---|---|---|
|  `json`  |  | Stored as plain text |
|  `jsonb`  |  | Stored in a binary format and can be indexed |


## PGColumn​

`String`

## RelationshipName​

`String`

## Table Config​

| Key | Required | Schema | Description |
|---|---|---|---|
| custom_name | false |  `String`  | Customize the `<table-name>` with the provided custom name value. The GraphQL nodes for the table will be generated according to the custom name. |
| custom_root_fields | false | [ Custom Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#custom-root-fields) | Customize the root fields |
| column_config | false | [ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnconfig) | Customize the columns |
| custom_column_names (deprecated) | false | [ CustomColumnNames ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customcolumnnames) | Customize the column fields (deprecated in favour of custom_name on[ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnconfig)) |
| comment | false |  `String`  | Customize the description shown in GraphQL introspection. If null or omitted then if a comment exists on the database table, it is used as the description (Postgres-only), and if not, an autogenerated description is used instead. |


## Custom Root Fields​

| Key | Required | Schema | Description |
|---|---|---|---|
| select | false |  `String` |[ CustomRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customrootfield) | Customize the `<table-name>` root field. Using a `String` customizes the field name. |
| select_by_pk | false |  `String` |[ CustomRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customrootfield) | Customize the `<table-name>_ by_ pk` root field. Using a `String` customizes the field name. |
| select_aggregate | false |  `String` |[ CustomRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customrootfield) | Customize the `<table-name>_ aggregate` root field. Using a `String` customizes the field name. |
| select_stream | false |  `String` |[ CustomRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customrootfield) | Customize the `<table-name>_ stream` root field. Using a `String` customizes the field name. |
| insert | false |  `String` |[ CustomRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customrootfield) | Customize the `insert_ <table-name>` root field. Using a `String` customizes the field name. |
| insert_one | false |  `String` |[ CustomRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customrootfield) | Customize the `insert_ <table-name>_ one` root field. Using a `String` customizes the field name. |
| update | false |  `String` |[ CustomRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customrootfield) | Customize the `update_ <table-name>` root field. Using a `String` customizes the field name. |
| update_by_pk | false |  `String` |[ CustomRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customrootfield) | Customize the `update_ <table-name>_ by_ pk` root field. Using a `String` customizes the field name. |
| delete | false |  `String` |[ CustomRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customrootfield) | Customize the `delete_ <table-name>` root field. Using a `String` customizes the field name. |
| delete_by_pk | false |  `String` |[ CustomRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customrootfield) | Customize the `delete_ <table-name>_ by_ pk` root field. Using a `String` customizes the field name. |


## CustomRootField​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | false |  `String`  | The custom root field name |
| comment | false |  `String`  | Customize the description shown for the root field in GraphQL introspection. If null or omitted then an autogenerated description is used instead. |


## ColumnConfig​

A[JSONObject][https://tools.ietf.org/html/rfc7159]of table column name to `ColumnConfigValue` .

```
{
    "column1" :
[ ColumnConfigValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnconfigvalue)
,
    "column2" :
[ ColumnConfigValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnconfigvalue)
,
    ...
}
```

## ColumnConfigValue​

Configuration properties for particular column, as specified on[ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnconfig).

| Key | Required | Schema | Description |
|---|---|---|---|
| custom_name | false |  `String`  | Customize the name of the field in the GraphQL schema |
| comment | false |  `String`  | Customize the description shown for the field in GraphQL introspection. If null or omitted then an autogenerated description is used instead. |


## Custom Function Root Fields​

| Key | Required | Schema | Description |
|---|---|---|---|
| function | false |  `String`  | Customize the `<function-name>` root field |
| function_aggregate | false |  `String`  | Customize the `<function-name>_ aggregate` root field |


## InputValidationDefinition​

| Key | Required | Schema | Description |
|---|---|---|---|
| url | true | [ WebhookURL ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#webhookurl) | The input validations's webhook URL |
| headers | false | [[ HeaderFromValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerfromvalue)|[ HeaderFromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerfromenv)] | List of defined headers to be sent to the handler |
| forward_client_headers | false | boolean | If set to `true` the client headers are forwarded to the webhook handler (default: `false` ) |
| timeout | false | Integer | Number of seconds to wait for response before timing out. Default: 10 |


## InputValidation​

| Key | Required | Schema | Description |
|---|---|---|---|
| type | true |  `String`  | The interface for input validation. (Currently only supports "http") |
| definition | true | [ InputValidationDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#input-validation-definition) | The definition for the input validation |


## InsertPermission​

| Key | Required | Schema | Description |
|---|---|---|---|
| check | true | [ BoolExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#boolexp) | This expression has to hold true for every new row that is inserted |
| set | false | [ ColumnPresetsExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnpresetexp) | Preset values for columns that can be sourced from session variables or static values |
| columns | false | [ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)array (or) `'*'`  | Can insert into only these columns (or all when `'*'` is specified) |
| backend_only | false | Boolean | When set to `true` the mutation is accessible only if the `x-hasura-use-backend-only-permissions` session variable exists and is set to `true` and the request is made with `x-hasura-admin-secret` set if any auth is configured |
| validate_input | false | [ InputValidation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#input-validation) | The input validation definition for the insert mutation. |


## SelectPermission​

| Key | Required | Schema | Description |
|---|---|---|---|
| columns | true | [ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)array (or) `'*'`  | Only these columns are selectable (or all when `'*'` is specified) |
| computed_fields | false | [ ComputedFieldName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#computedfieldname)array | Only these computed fields are selectable |
| filter | true | [ BoolExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#boolexp) | Only the rows where this expression holds true are selectable |
| limit | false |  `Integer`  | The maximum number of rows that can be returned |
| allow_aggregations | false |  `Boolean`  | Toggle allowing aggregate queries |
| query_root_fields | false | [ QueryRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#queryRootField)array | Only given root fields will be enabled in the `query` root field. An empty list will mean no query root fields are enabled . |
| subscription_root_fields | false | [ SubscriptionRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#subscriptionRootField)array | Only given root fields will be enabled in the `subscription` root field. An empty list will mean no subscription root fields are enabled. |


Note

The `query_root_fields` and the `subscription_root_fields` are only available in v2.8.0 and above

## UpdatePermission​

| Key | Required | Schema | Description |
|---|---|---|---|
| columns | true | [ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)array (or) `'*'`  | Only these columns are selectable (or all when `'*'` is specified) |
| filter | true | [ BoolExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#boolexp) | Only the rows where this precondition holds true are updatable |
| check | false | [ BoolExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#boolexp) | Postcondition which must be satisfied by rows which have been updated |
| set | false | [ ColumnPresetsExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnpresetexp) | Preset values for columns that can be sourced from session variables or static values. |
| backend_only | false | Boolean | When set to `true` the mutation is accessible only if the `x-hasura-use-backend-only-permissions` session variable exists and is set to `true` and the request is made with `x-hasura-admin-secret` set if any auth is configured |
| validate_input | false | [ InputValidation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#input-validation) | The input validation definition for the insert mutation. |


## DeletePermission​

| Key | Required | Schema | Description |
|---|---|---|---|
| filter | true | [ BoolExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#boolexp) | Only the rows where this expression holds true are deletable |
| backend_only | false | Boolean | When set to `true` the mutation is accessible only if the `x-hasura-use-backend-only-permissions` session variable exists and is set to `true` and the request is made with `x-hasura-admin-secret` set if any auth is configured |
| validate_input | false | [ InputValidation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#input-validation) | The input validation definition for the insert mutation. |


## LogicalModelSelectPermission​

| Key | Required | Schema | Description |
|---|---|---|---|
| columns | true | [ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)array (or) `'*'`  | Only these columns are selectable (or all when `'*'` is specified) |
| filter | true | [ BoolExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#boolexp) | Only the rows where this expression holds true are selectable |


## ObjRelUsing​

| Key | Required | Schema | Description |
|---|---|---|---|
| foreign_key_constraint_on | false | [ ObjRelUsingChoice ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#objrelusingchoice) | The column with foreign key constraint or the remote table and column |
| manual_configuration | false | [ ObjRelUsingManualMapping ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#objrelusingmanualmapping) | Manual mapping of table and columns |


Note

There has to be at least one and only one of `foreign_key_constraint_on` and `manual_configuration` .

## ObjRelUsingChoice​

```
[ SameTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#sametable)
|
[ RemoteTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remotetable)
```

## SameTable​

`[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)`

## RemoteTable​

```
{
  "table"  :
[ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#tablename)
"column" :
[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)
}
```

Supported from

Supported in `v2.0.0-alpha.3` and above.

## ObjRelUsingManualMapping​

| Key | Required | Schema | Description |
|---|---|---|---|
| remote_table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#tablename) | The table to which the relationship has to be established |
| column_mapping | true | Object ([ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn):[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)) | Mapping of columns from current table to remote table |
| insertion_order | false | [ InsertOrder ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#insertorder) | insertion order: before or after parent (default: "before_parent") |


## InsertOrder​

Describes when should the referenced table row be inserted in relation to the current table row in case of a nested
insert. Defaults to "before_parent".

`"before_parent" | "after_parent"`

Supported from

Supported in `v2.0.0-alpha.3` and above.

## ArrRelUsing​

| Key | Required | Schema | Description |
|---|---|---|---|
| foreign_key_constraint_on | false | [ ArrRelUsingFKeyOn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#arrrelusingfkeyon) | The column with foreign key constraint |
| manual_configuration | false | [ ArrRelUsingManualMapping ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#arrrelusingmanualmapping) | Manual mapping of table and columns |


## ArrRelUsingFKeyOn​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#tablename) | Name of the table |
| column | true | [ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn) | Name of the column with foreign key constraint |


## ArrRelUsingManualMapping​

| Key | Required | Schema | Description |
|---|---|---|---|
| remote_table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#tablename) | The table to which the relationship has to be established |
| column_mapping | true | Object ([ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn):[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)) | Mapping of columns from current table to remote table |


## ScheduledEventStatus​

`scheduled | locked | delivered | error | dead`

## BoolExp​

```
[ AndExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#andexp)
|
[ OrExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#orexp)
|
[ NotExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#notexp)
|
[ ExistsExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#existsexp)
|
[ TrueExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#trueexp)
|
[ ColumnExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnexp)
```

## AndExp​

```
{
  "$and" : [
[ BoolExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#boolexp)
]
}
```

## OrExp​

```
{
  "$or" : [
[ BoolExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#boolexp)
]
}
```

## NotExp​

```
{
  "$not" :
[ BoolExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#boolexp)
}
```

## ExistsExp​

```
{
  "$exists" : {
    "_table" :
[ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#tablename)
,
    "_where" :
[ BoolExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#taboolexpblename)
}
}
```

## TrueExp​

`{}`

## ColumnExp​

```
{
[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)
| scalar
[ ComputedFieldName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#computedfieldname)
|
[ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#relationshipname)
|
[ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remoterelationshipname)
: {
[ Operator ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#metadataoperator)
: Value }
}
```

## Operator​

 **Generic operators (all column types except json, jsonb) :** 

| Operator | PostgreSQL equivalent |
|---|---|
|  `"$eq"`  |  `=`  |
|  `"$ne"`  |  `<>`  |
|  `"$gt"`  |  `>`  |
|  `"$lt"`  |  `<`  |
|  `"$gte"`  |  `>=`  |
|  `"$lte"`  |  `<=`  |
|  `"$in"`  |  `IN`  |
|  `"$nin"`  |  `NOT IN`  |


(For more details, refer to the Postgres docs for[ comparison operators ](https://www.postgresql.org/docs/current/functions-comparison.html)and[ list based search operators ](https://www.postgresql.org/docs/current/functions-comparisons.html).)

 **Text related operators :** 

| Operator | PostgreSQL equivalent |
|---|---|
|  `"$like"`  |  `LIKE`  |
|  `"$nlike"`  |  `NOT LIKE`  |
|  `"$ilike"`  |  `ILIKE`  |
|  `"$nilike"`  |  `NOT ILIKE`  |
|  `"$similar"`  |  `SIMILAR TO`  |
|  `"$nsimilar"`  |  `NOT SIMILAR TO`  |
|  `$regex`  |  `~`  |
|  `$iregex`  |  `~*`  |
|  `$nregex`  |  `!~`  |
|  `$niregex`  |  `!~*`  |


(For more details on text related operators, refer to the[ Postgres docs ](https://www.postgresql.org/docs/current/functions-matching.html).)

 **Operators for comparing columns (all column types except json, jsonb):** 

 **Column Comparison Operator** 

```
{
[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)
: {
[ Operator ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#metadataoperator)
: {
[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)
| ["$",
[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)
]
    }
  }
}
```

Column comparison operators can be used to compare columns of the same table or a related table. To compare a column of
a table with another column of :

1. The same table -


```
{
[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)
: {
[ Operator ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#metadataoperator)
: {
[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)
}
  }
}
```

1. The table on which the permission is being defined on -


```
{
[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)
: {
[ Operator ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#metadataoperator)
: {
      ["$",
[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)
]
    }
  }
}
```

| Operator | PostgreSQL equivalent |
|---|---|
|  `"$ceq"`  |  `=`  |
|  `"$cne"`  |  `<>`  |
|  `"$cgt"`  |  `>`  |
|  `"$clt"`  |  `<`  |
|  `"$cgte"`  |  `>=`  |
|  `"$clte"`  |  `<=`  |


(For more details on comparison operators, refer to the[ Postgres docs ](https://www.postgresql.org/docs/current/functions-comparison.html).)

 **Checking for NULL values :** 

| Operator | PostgreSQL equivalent |
|---|---|
|  `_ is_ null` (takes true/false as values) |  `IS NULL`  |


(For more details on the `IS NULL` expression, refer to the[ Postgres docs ](https://www.postgresql.org/docs/current/functions-comparison.html).)

 **JSONB operators :** 

| Operator | PostgreSQL equivalent |
|---|---|
|  `_ contains`  |  `@>`  |
|  `_ contained_ in`  |  `<@`  |
|  `_ has_ key`  |  `?`  |
|  `_ has_ keys_ any`  |  `?!`  |
|  `_ has_ keys_ all`  |  `?&`  |


(For more details on JSONB operators, refer to the[ Postgres docs ](https://www.postgresql.org/docs/current/static/functions-json.html#FUNCTIONS-JSONB-OP-TABLE).)

 **PostGIS related operators on GEOMETRY columns:** 

| Operator | PostGIS equivalent |
|---|---|
|  `_ st_ contains`  |  `ST_ Contains(column, input)`  |
|  `_ st_ crosses`  |  `ST_ Crosses(column, input)`  |
|  `_ st_ equals`  |  `ST_ Equals(column, input)`  |
|  `_ st_ 3d_ intersects`  |  `ST_ 3DIntersects(column, input)`  |
|  `_ st_ intersects`  |  `ST_ Intersects(column, input)`  |
|  `_ st_ overlaps`  |  `ST_ Overlaps(column, input)`  |
|  `_ st_ touches`  |  `ST_ Touches(column, input)`  |
|  `_ st_ within`  |  `ST_ Within(column, input)`  |
|  `_ st_ d_ within`  |  `ST_ DWithin(column, input)`  |
|  `_ st_ 3d_ d_ within`  |  `ST_ 3DDWithin(column, input)`  |


(For more details on spatial relationship operators, refer to the[ PostGIS docs ](http://postgis.net/workshops/postgis-intro/spatial_relationships.html).)

Note

- All operators take a JSON representation of `geometry/geography` values as input value.
- The input value for `_st_d_within` operator is an object:


All operators take a JSON representation of `geometry/geography` values as input value.

The input value for `_st_d_within` operator is an object:

```
{
  field-name : {_st_d_within: {distance: Float, from: Value} }
}
```

## Object​

A[ JSONObject ](https://tools.ietf.org/html/rfc7159)

```
{
  "k1" : v1,
  "k2" : v2,
  ..
}
```

## Empty Object​

An empty[ JSONObject ](https://tools.ietf.org/html/rfc7159)

`{ }`

## ColumnPresetsExp​

A[ JSONObject ](https://tools.ietf.org/html/rfc7159)of a Postgres column name to value mapping, where the value can be
static or derived from a session variable.

```
{
  "column1" : colVal1,
  "column2" : colVal2,
  ..
}
```

E.g. where `id` is derived from a session variable and `city` is a static value.

```
{
   "id" :   "x-hasura-User-Id" ,
   "city" :   "San Francisco"
}
```

Note

If the value of any key begins with "x-hasura-" ( *case-insensitive* ), the value of the column specified in the key will
be derived from a session variable of the same name.

## Query root field​

```
[ select ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#select)
|
[ select_by_pk ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#selectByPk)
|
[ select_aggregate ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#selectAggregate)
```

## Subscription root field​

```
[ select ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#select)
|
[ select_by_pk ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#selectByPk)
|
[ select_aggregate ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#selectAggregate)
|
[ select_stream ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#selectStream)
```

## RemoteSchemaName​

`String`

## RemoteSchemaDef​

```
{
  "url" : url-string,
  "url_from_env" : env-var-string,
  "headers": [
    {
      "name": header-name-string,
      "value": header-value-string,
      "value_from_env": env-var-string
    }
  ],
  "forward_client_headers": boolean,
  "timeout_seconds": integer,
  "customization":
[ RemoteSchemaCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remoteschemacustomization)
}
```

## RemoteSchemaCustomization​

```
{
  "root_fields_namespace": String,
  "type_names": {
    "prefix": String,
    "suffix": String,
    "mapping": {
        String: String
        }
    },
  "field_names": [
      {
      "parent_type": String,
      "prefix": String,
      "suffix": String,
      "mapping": {
          String: String
          }
      }
    ]
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
|  `root_ fields_ namespace`  | false | String | If provided, the fields of the Remote Schema will be nested under this top level field |
|  `type_ names`  | false | [ RemoteTypeCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remotetypecustomization) | Customization of type names in the Remote Schema |
|  `field_ names`  | false | [[ RemoteFieldCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remotefieldcustomization)] | Customization of field names for types in the Remote Schema |


## RemoteTypeCustomization​

| Key | Required | Schema | Description |
|---|---|---|---|
|  `prefix`  | false | String | Prefix applied to type names in the Remote Schema |
|  `suffix`  | false | String | Suffix applied to type names in the Remote Schema |
|  `mapping`  | false |  `{String: String}`  | Explicit mapping of type names in the Remote Schema Note: explicit mapping takes precedence over `prefix` and `suffix` . |


- Type name prefix and suffix will be applied to all types in the schema except the root types (for query, mutation and
subscription), types starting with `__` , standard scalar types ( `Int` , `Float` , `String` , `Boolean` , and `ID` ), and
types with an explicit mapping.
- Root types, types starting with `__` , and standard scalar types may only be customized with an explicit mapping.


## RemoteFieldCustomization​

| Key | Required | Schema | Description |
|---|---|---|---|
|  `parent_ type`  | true | String | Name of the parent type (in the original Remote Schema) for fields to be customized |
|  `prefix`  | false | String | Prefix applied to field names in parent type |
|  `suffix`  | false | String | Suffix applied to field names in the parent type |
|  `mapping`  | false |  `{String: String}`  | Explicit mapping of field names in the parent type Note: explicit mapping takes precedence over `prefix` and `suffix` . |


- Fields that are part of an interface must be renamed consistently across all object types that implement that
interface.


## SourceCustomization​

```
{
  "root_fields": {
    "namespace": String,
    "prefix": String,
    "suffix": String
    },
  "type_names": {
    "prefix": String,
    "suffix": String
    },
  "naming_convention": String
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
|  `root_ fields`  | false | [ RootFieldsCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#rootfieldscustomization) | Customization of root field names for a source |
|  `type_ names`  | false | [ SourceTypeCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#sourcetypecustomization) | Customization of type names for a source |
|  `naming_ convention`  | false | String | Naming conventions for a source |


Note

Please note that the naming convention feature is an experimental feature for now. To use this feature, please use the `--experimental-features=naming_convention` flag or set the `HASURA_GRAPHQL_EXPERIMENTAL_FEATURES` environment variable
to `naming_convention` .

The naming convention can either be `graphql-default` or `hasura-default` (default). **The  graphql-default  naming
convention is supported only for postgres databases right now.** Typecase for each of the naming convention is mentioned
below:

`graphql-default`

| Naming Convention | Field names | Type names | Arguments | Enum values |
|---|---|---|---|---|
| hasura-default | Snake case | Snake case | Snake case | as defined |
| graphql-default | Camel case | Pascal case | Camel case | Uppercased |


The naming convention can be overridden by `custom_name` in[ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#table-config)or by setting[ Custom Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#custom-root-fields).

## RootFieldsCustomization​

| Key | Required | Schema | Description |
|---|---|---|---|
|  `namespace`  | false | String | Namespace root field under which fields for this source will be nested |
|  `prefix`  | false | String | Prefix to be prepended to all root fields in this source |
|  `suffix`  | false | String | Suffix to be appended to all root fields in this source |


## SourceTypeCustomization​

| Key | Required | Schema | Description |
|---|---|---|---|
|  `prefix`  | false | String | Prefix to be prepended to all type names in this source |
|  `suffix`  | false | String | Suffix to be appended to all type names in this source |


## CollectionName​

`String`

## QueryName​

`String`

## CollectionQuery​

```
{
  "name": String,
  "query": String
}
```

## AllowlistScope​

```
{
  "global": Boolean,
  "roles" : [
[ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#rolename)
]
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
| global | false | Boolean | When set to `false` a non empty array of role names is expected in the `roles` key. When set to `true` , the `roles` key must be omitted. (default: `true` ) |
| roles | when `global` is set to `false`  | [[ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#rolename)] | Roles to which the a query collection's queries should be accessible. *(supported only in cloud/enterprise versions)*  |


## EndpointUrl​

`String`

## EndpointMethods​

`[String]`

## EndpointDefinition​

```
{
  "query": {
    "query_name : String, "collection_name" : CollectionName
  }
}
```

## CustomColumnNames​

Deprecation

CustomColumnNames is deprecated in favour of using the `custom_name` property on columns in[ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnconfig). If both CustomColumnNames and[ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnconfig)is used, any `custom_name ` properties used in[ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnconfig)will take precedence and any overlapped values in `custom_column_names` will be discarded.

A[ JSONObject ](https://tools.ietf.org/html/rfc7159)of Postgres column name to GraphQL name mapping

```
{
  "column1" : String,
  "column2" : String,
  ..
}
```

## ActionName​

`String`

## WebhookURL​

A String value which supports templating environment variables enclosed in `{{` and `}}` .

`String`

Template example: `https://{{ACTION_API_DOMAIN}}/create-user` 

## HeaderFromValue​

| Key | required | Schema | Description |
|---|---|---|---|
| name | true | String | Name of the header |
| value | true | String | Value of the header |


The `value` field supports templating environment variables enclosed in `{{` and `}}` .

Template example: `header-{{HEADER_FROM_ENV}}` 

## HeaderFromEnv​

| Key | required | Schema | Description |
|---|---|---|---|
| name | true | String | Name of the header |
| value_from_env | true | String | Name of the environment variable which holds the value of the header |


## GraphQLType​

A GraphQL[ Type Reference ](https://spec.graphql.org/June2018/#sec-Type-References)string.

`String`

Example: `String!` for non-nullable String type and `[String]` for array of String types

## GraphQLName​

A string literal that conform to[ GraphQL spec ](https://spec.graphql.org/June2018/#Name).

`String`

## ActionDefinition​

| Key | Required | Schema | Description |
|---|---|---|---|
| arguments | false | Array of[ InputArgument ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#inputargument) | Input arguments |
| output_type | true | [ GraphQLType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqltype) | The output type of the action. Only object and list of objects are allowed. |
| kind | false | [ `synchronous` | `asynchronous` ] | The kind of the mutation action (default: `synchronous` ). If the type of the action is `query` then the `kind` field should be omitted. |
| headers | false | [[ HeaderFromValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerfromvalue)|[ HeaderFromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerfromenv)] | List of defined headers to be sent to the handler |
| forward_client_headers | false | boolean | If set to `true` the client headers are forwarded to the webhook handler (default: `false` ) |
| handler | true | [ WebhookURL ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#webhookurl) | The action's webhook URL |
| type | false | [ `mutation` | `query` ] | The type of the action (default: `mutation` ) |
| timeout | false | Integer | Number of seconds to wait for response before timing out. Default: 30 |
| request_transform | false | [ RequestTransformation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#requesttransformation) | Request Transformation to be applied to this Action's request |
| response_transform | false | [ ResponseTransformation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#responsetransformation) | Response Transformation to be applied to this Action's response |


## InputArgument​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | text | Name of the argument |
| type | true | [ GraphQLType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqltype) | Type of the argument |


Note

The `GraphQL Types` used in creating an action must be defined before via[ Custom Types ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-types/)

## ComputedFieldDefinition​

| Key | Required | Schema | Description |
|---|---|---|---|
| function | true | [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#functionname) | The SQL function |
| table_argument | false | String | Name of the argument which accepts a table row type. If omitted, the first argument is considered a table argument |
| session_argument | false | String | Name of the argument which accepts the Hasura session object as a JSON/JSONB value. If omitted, the Hasura session object is not passed to the function |


## BigQuery ComputedFieldDefinition​

| Key | Required | Schema | Description |
|---|---|---|---|
| function | true | [ BigQuery FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#bigqueryfunctionname) | The user defined SQL function |
| argument_mapping | true | Object ( `String` : `String` ) | Mapping from the argument name of the function to the column name of the table |
| return_table | false | [ BigQuery TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#bigquerytablename) | Name of the table which the function returns |


## LogicalModelField​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true |  `String`  | The name of the Logical Model field |
| type | true | [ Logical Model Type ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#logicalmodeltype) | A Logical Model field type |
| description | false |  `String`  | An extended description of the field |


## LogicalModelType​

A Logical Model type is one of either:

A scalar:

| Key | Required | Schema | Description |
|---|---|---|---|
| scalar | true |  `String`  | The type of the exposed column, according to the underlying data source |
| nullable | false |  `Boolean`  | True if the field should be exposed over the GraphQL API as a nullable field (default: `false` ) |


An array:

| Key | Required | Schema | Description |
|---|---|---|---|
| array | true | [ Logical Model Type ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#logicalmodeltype) | A Logical Model type, which this denotes an array of |
| nullable | false |  `Boolean`  | True if the field should be exposed over the GraphQL API as a nullable field (default: `false` ) |


A reference to another logical model:

| Key | Required | Schema | Description |
|---|---|---|---|
| logical_model | true | [ Logical Model Type ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#logicalmodeltype) | A Logical Model type, which this refers to. Recursive and mutually recursive references are permitted. |
| nullable | false |  `Boolean`  | True if the field should be exposed over the GraphQL API as a nullable field (default: `false` ) |


## NativeQueryArgument​

| Key | Required | Schema | Description |
|---|---|---|---|
| type | true |  `String`  | The type of the column, according to the underlying data source |
| nullable | false |  `Boolean`  | True if the underlying column is nullable (default: `false` ) |
| description | false |  `String`  | An extended description of the argument |


## NativeQueryRelationship​

| Key | Required | Schema | Description |
|---|---|---|---|
| remote_native_query | true |  `String`  | The Native Query to which the relationship has to be established |
| column_mapping | true | Object (local-column : remote-column) | Mapping of columns from current table to remote table |


## Stored Procedure Argument​

| Key | Required | Schema | Description |
|---|---|---|---|
| type | true |  `String`  | The type of the column, according to the underlying data source |
| nullable | false |  `Boolean`  | True if the underlying column is nullable (default: `false` ) |
| description | false |  `String`  | An extended description of the argument |


## Stored Procedure Configuration​

| Key | Required | Schema | Description |
|---|---|---|---|
| custom_name | false |  `String`  | Customize the `<stored-procedure-name>` with the provided custom name value. The GraphQL nodes for the stored procedure will be generated according to the custom name. |
| exposed_as | true |  `String`  | In which part of the schema should we expose this stored procedure? Currently only "query" is supported. |


## Function Configuration​

| Key | Required | Schema | Description |
|---|---|---|---|
| custom_name | false |  `String`  | Customize the `<function-name>` with the provided custom name value. The GraphQL nodes for the function will be generated according to the custom name. |
| custom_root_fields | false | [ Custom Function Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#custom-function-root-fields) | Customize the root fields |
| session_argument | false |  *String*  | Function argument which accepts session info JSON |
| exposed_as | false |  *String*  | In which part of the schema should we expose this function? Either "mutation" or "query". |


Note

Currently, only functions which satisfy the following constraints can be exposed over the GraphQL API ( *terminology
from* [ Postgres docs ](https://www.postgresql.org/docs/current/sql-createfunction.html)):

- **Function behavior** : `STABLE` or `IMMUTABLE` functions may *only* be exposed as queries (i.e. with `exposed_as: query` ) `VOLATILE` functions may be exposed as mutations or queries.
- **Return type** : MUST be `SETOF <table-name>` OR `<table_name>` where `<table-name>` is already tracked
- **Argument modes** : ONLY `IN`


## InputObjectType​

A simple JSON object to define[ GraphQL Input Object ](https://spec.graphql.org/June2018/#sec-Input-Objects)

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ GraphQLName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqlname) | Name of the Input object type |
| description | false | String | Description of the Input object type |
| fields | true | Array of[ InputObjectField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#inputobjectfield) | Fields of the Input object type |


### InputObjectField​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ GraphQLName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqlname) | Name of the Input object field |
| description | false | String | Description of the Input object field |
| type | true | [ GraphQLType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqltype) | GraphQL ype of the input object field |


## ObjectType​

A simple JSON object to define[ GraphQL Object ](https://spec.graphql.org/June2018/#sec-Objects)

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ GraphQLName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqlname) | Name of the Object type |
| description | false | String | Description of the Object type |
| fields | true | Array of[ ObjectField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#objectfield) | Fields of the Object type |
| relationships | false | Array of[ ObjectRelationship ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#objectrelationship) | Relationships of the Object type to tables |


### ObjectField​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ GraphQLName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqlname) | Name of the Input object field |
| description | false | String | Description of the Input object field |
| type | true | [ GraphQLType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqltype) | GraphQL type of the input object field |


### ObjectRelationship​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#relationshipname) | Name of the relationship, shouldn't conflict with existing field names |
| type | true | [ `object` | `array` ] | Type of the relationship |
| remote_table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#tablename) | The table to which relationship is defined |
| field_mapping | true | Object ([ ObjectField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#objectfield)name : Remote table's[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)) | Mapping of fields of object type to columns of remote table |


## ScalarType​

A simple JSON object to define[ GraphQL Scalar ](https://spec.graphql.org/June2018/#sec-Scalars)

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ GraphQLName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqlname) | Name of the Scalar type |
| description | false | String | Description of the Scalar type |


## EnumType​

A simple JSON object to define[ GraphQL Enum ](https://spec.graphql.org/June2018/#sec-Enums)

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ GraphQLName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqlname) | Name of the Enum type |
| description | false | String | Description of the Enum type |
| values | true | Array of[ EnumValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#enumvalue) | Values of the Enum type |


### EnumValue​

| Key | Required | Schema | Description |
|---|---|---|---|
| value | true | [ GraphQLName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqlname) | Value of the Enum type |
| description | false | String | Description of the value |
| is_deprecated | false | Boolean | If set to `true` , the enum value is marked as deprecated |


## TriggerName​

`String`

## OperationSpec​

| Key | Required | Schema | Description |
|---|---|---|---|
| columns | true | [ EventTriggerColumns ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#eventtriggercolumns) | List of columns or "*" to listen to changes |
| payload | false | [ EventTriggerColumns ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#eventtriggercolumns) | List of columns or "*" to send as part of webhook payload |


## EventTriggerColumns​

```
"*" | [
[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)
]
```

## RequestTransformation​

| Key | required | Schema | Description |
|---|---|---|---|
| version | false | "1"|"2" | Sets the `RequestTransformation` schema version. Version `1` uses a `String` for the `body` field and Version `2` takes a[ BodyTransform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#bodytransform). Defaults to version `1` . |
| method | false | String | Change the request method to this value. |
| url | false | String | Change the request URL to this value. |
| body | false | [ BodyTransform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#bodytransform)|String | A template script for transforming the request body. |
| content_type | false | String | Replace the Content-Type with this value. Default: "application/json" *(valid only for version 1)*  |
| query_params | false | Object (String : String)|String | Replace the query params on the URL with this value. You can specify a dictionary of key/value pairs which is converted into a query string or directly give a query string. |
| request_headers | false | [ TransformHeaders ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#transformheaders) | Request Header Transformation. |
| template_engine | false | [ TemplateEngine ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#templateengine) | Template language to be used for this transformation. Default: "Kriti" |


Supported from

Version 2 is supported in `v2.5.0` and above. You must remove any "version 2" schemas from your Metadata prior to
downgrading to `v2.4.0` or earlier

Note

HGE provides the following functions that can be used in the template:

- `not` : This function takes a boolean and returns its negation.eg::
- `escapeUri` : This function takes a string and escapes it as per URI specification.eg::
- `getSessionVariable` : This function takes a string and returns the session variable of the given name. This function
can throw the following errors:
    - Session variable {variable name} not found
eg::


 `not` : This function takes a boolean and returns its negation.

eg::

```
  > {{not(true)}}
  false
```

 `escapeUri` : This function takes a string and escapes it as per URI specification.

eg::

```
  > {{ escapeUri("?foo=bar/baz") }}
  "%3Ffoo%3Dbar%2Fbaz"
```

 `getSessionVariable` : This function takes a string and returns the session variable of the given name. This function
can throw the following errors:

eg::

```
  > {{getSessionVariable("myVariableName")}}
  "myVariableValue"
```

## TransformHeaders​

| Key | required | Schema | Description |
|---|---|---|---|
| add_headers | false | Object ([ HeaderKey ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerkey):[ HeaderValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headervalue)) | A map of Header Key Value pairs to be added to the request. |
| remove_headers | false | Array of ([ HeaderKey ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerkey)) | Headers to be removed from the request. |


## HeaderKey​

`String`

## HeaderValue​

`String`

## BodyTransform​

| Key | required | Schema | Description |
|---|---|---|---|
| action | true | remove|transform|x_www_form_urlencoded | The action to perform on the request body. |
| template | false | String | The transformation template to be applied to the body. This is required if the action is *transform* . |
| form_template | false | Object ([ String ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string):[ String ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string)) | The key/value pairs to be used in a `x-www-url-formencoded` body. The values can be transfomation templates. |


## TemplateEngine​

The JSON templating language to be used for this JSON transformation.

`"Kriti"`

## ResponseTransformation​

| Key | required | Schema | Description |
|---|---|---|---|
| version | false | "1"|"2" | Sets the *RequestTransformation* schema version. Version *1* uses a *String* for the *body* field and Version *2* takes a[ BodyTransform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#bodytransform). Defaults to version *1* . |
| body | false | [ BodyTransform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#bodytransform)| `String`  | A template script for transforming the response body. |
| template_engine | false | [ TemplateEngine ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#templateengine) | Template language to be used for this transformation. Default: "Kriti" |


## RetryConf​

| Key | required | Schema | Description |
|---|---|---|---|
| num_retries | false | Integer | Number of times to retry delivery. Default: 0 |
| interval_sec | false | Integer | Number of seconds to wait between each retry. Default: 10 |
| timeout_sec | false | Integer | Number of seconds to wait for response before timing out. Default: 60 |


## RemoteRelationshipName​

`String`

## RemoteRelationshipDefinition​

| Key | required | Schema | Description |
|---|---|---|---|
| to_source | false | [ ToSourceRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#tosourcerelationshipdefinition) | Remote Relationship definition to a table on a different database |
| to_remote_schema | false | [ ToSchemaRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#toschemarelationshipdefinition) | Remote Relationship definition to a Remote Schema |


Note

Note: *One* of and *only one* of `to_source` and `to_remote_schema` must be present

## ToSourceRelationshipDefinition​

| Key | required | Schema | Description |
|---|---|---|---|
| relationship_type | true | "object"|"array" | The type of the relationship |
| field_mapping | true | Object ([ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn):[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)) | Mapping of columns from current table to remote table |
| source | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#sourcename) | Name of the source of the target table |
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#tablename) | Name of the target table |


## ToSchemaRelationshipDefinition​

| Key | Required | Schema | Description |
|---|---|---|---|
| remote_schema | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema to join with |
| lhs_fields | true | [[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgcolumn)|[ ComputedFieldName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#computedfieldname)] | Column/Computed field(s) in the table that is used for joining with Remote Schema field. All join keys in `remote_ field` must appear here. |
| remote_field | true | [ RemoteField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remotefield) | The schema tree ending at the field in Remote Schema which needs to be joined with. |


## RemoteField​

```
{
  FieldName: {
    "arguments": InputArguments "field": RemoteField # optional
  }
}
```

 `RemoteField` is a recursive tree structure that points to the field in the Remote Schema that needs to be joined with.
It is recursive because the remote field maybe nested deeply in the Remote Schema.

Examples:

```
{
  "message": {
    "arguments":{
      "message_id":"$id"
      }
  }
}
```

```
{
  "messages": {
    "arguments": {
      "limit": 100
    },
    "field": {
    "private": {
      "arguments": {
        "id" : "$id"
      }
    }
    }
  }
}
```

## InputArguments​

```
{
  InputField : $PGColumn | Scalar
}
```

Table columns can be referred by prefixing `$` e.g `$id` .

## RemoteSchemaPermission​

| Key | Required | Schema | Description |
|---|---|---|---|
| schema | true | GraphQL SDL | GraphQL SDL defining the role based schema |


## UrlFromEnv​

| Key | required | Schema | Description |
|---|---|---|---|
| from_env | true |  `String`  | Name of the environment variable which has the URL |


## RetryConfST​

| Key | required | Schema | Description |
|---|---|---|---|
| num_retries | false | Integer | Number of times to retry delivery. Default: 0 |
| retry_interval_seconds | false | Integer | Number of seconds to wait between each retry. Default: 10 |
| timeout_seconds | false | Integer | Number of seconds to wait for response before timing out. Default: 60 |
| tolerance_seconds | false | Integer | Number of seconds between scheduled time and actual delivery time that is acceptable. If the time difference is more than this, then the event is dropped. Default: 21600 (6 hours) |


## ApolloFederationConfig​

| Key | required | Schema | Description |
|---|---|---|---|
| enable | true | String | Apollo federation version (can be `"v1"` only) |


## AutoEventTriggerCleanupConfig​

| Key | required | Schema | Description |
|---|---|---|---|
| schedule | true | Cron Expression | Cron expression at which the cleanup should be invoked. |
| clear_older_than | true | Integer | Event logs retention period (in hours). 168 hours of retention period means that the logs older than 7 days will be removed. |
| batch_size | false | Integer | Maximum number of logs to delete in a single statement during the cleanup action. If there are more events to be cleaned than the `batch_ size` then the cleanup action will execute multiple statements sequentially until all old event logs are cleared. Default 10000 |
| timeout | false | Integer | Maximum time (in seconds) that a batch can take during the cleanup process. If a batch times out, the cleanup process is halted. Default: 60 |
| clean_invocation_logs | false | Bool | Should corresponding invocation logs be cleaned. Default `false`  |
| paused | false | Bool | Is the auto-cleanup process paused. Default `false`  |


## TriggerLogCleanupSources​

| Key | required | Schema | Description |
|---|---|---|---|
| sources | true |  `'*'` |[ [SourceName] ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#sourcename) | Sources for which to update the cleaner status (or all sources when `'*'` is provided) |


## EventTriggerQualifier​

| Key | required | Schema | Description |
|---|---|---|---|
| event_triggers | true | [ [TriggerName] ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#triggername) | List of trigger names |
| source_name | true | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#sourcename) | Source to which the Event Triggers belong |


## APILimitOption​

| Key | required | Schema | Description |
|---|---|---|---|
| global | true | Integer | Mandatory limit to be set at the global level |
| per_role | false | Object ( `String` : Integer) | Map of role name to limit value. This defines limits for each role |


## RateLimitOption​

| Key | required | Schema | Description |
|---|---|---|---|
| global | true | [ RateLimitPerRoleOption ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#ratelimitperroleoption) | Mandatory rate limit to be set at the global level |
| per_role | false | Object ( `String` :[ RateLimitPerRoleOption ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#ratelimitperroleoption)) | Map of role name to rate limit config. This defines limits for each role |


## RateLimitPerRoleOption​

| Key | required | Schema | Description |
|---|---|---|---|
| unique_params | false |  `String` |[ `String` ] | This would be either fixed value `IP` or a list of Session variables |
| max_reqs_per_min | true | Integer | Maximum requests per minute to be allowed |


## PGConnectionTemplate​

| Key | required | Schema | Description |
|---|---|---|---|
| template | true | String | Template for the dynamic DB connection |
| version | false | Int | Version of the template (Possible value is 1, default: 1) |


## ConnectionSetElementConfig​

| Key | required | Schema | Description |
|---|---|---|---|
| name | true | String | name of the connection |
| connection_info | true | [ PGSourceConnectionInfo ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgsourceconnectioninfo) | Connection parameters for the source |


## RequestContext​

| Key | required | Schema | Description |
|---|---|---|---|
| headers | false | Object ([ HeaderKey ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerkey):[ HeaderValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headervalue)) | Request header |
| session | false | Object (String : String) | Request session variables |
| query | false | [ QueryContext ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#queryContext) | Operation details |


## QueryContext​

| Key | required | Schema | Description |  |  |
|---|---|---|---|---|---|
| operation_type | true | query | mutation | subscription | Type of the graphql operation |
| operation_name | false | String | Name of the graphql operation |  |  |


## Attribute​

| Key | required | Schema | Description |
|---|---|---|---|
| name | true | String | Name of the attribute |
| value | true | String | Value of the attribute |


## OTLPExporter​

| Key | required | Schema | Description |
|---|---|---|---|
| otlp_traces_endpoint | true |  `String`  | OpenTelemetry compliant receiver endpoint URL for traces (usually having path "/v1/traces") |
| otlp_metrics_endpoint | true |  `String`  | OpenTelemetry compliant receiver endpoint URL for metrics (usually having path "/v1/metrics") |
| otlp_logs_endpoint | true |  `String`  | OpenTelemetry compliant receiver endpoint URL for logs (usually having path "/v1/logs") |
| protocol | false |  `String`  | Protocol to be used for the communication with the receiver. Currently only supports `http/protobuf`  |
| headers | false | [[ HeaderFromValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerfromvalue)|[ HeaderFromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerfromenv)] | List of defined headers to be sent to the receiver |
| resource_attributes | false | [[ Attribute ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#attribute)] | List of resource attributes to be sent to the receiver |
| traces_propagators | false | ["tracecontext"] | List of trace propagations to exchange context between services and processes |


## OpenTelemetryBatchSpanProcessor​

| Key | required | Schema | Description |
|---|---|---|---|
| max_export_batch_size | false |  `Integer`  | Maximum number of spans or logs allowed per export request. Default value is 512 |


### What did you think of this doc?

- [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#tablename)
- [ QualifiedTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#qualifiedtable)
- [ BigQuery TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#bigquerytablename)
- [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#sourcename)
- [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#functionname)
- [ QualifiedFunction ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#qualifiedfunction)
- [ BigQuery FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#bigqueryfunctionname)
- [ LogicalModelName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#logicalmodelname)
- [ RoleName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#rolename)
- [ ComputedFieldName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#computedfieldname)
- [ PGConfiguration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgconfiguration)
- [ MsSQLConfiguration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#mssqlconfiguration)
- [ BigQueryConfiguration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#bigqueryconfiguration)
- [ PGSourceConnectionInfo ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgsourceconnectioninfo)
- [ MsSQLSourceConnectionInfo ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#mssqlsourceconnectioninfo)
- [ FromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#fromenv)
- [ DynamicFromFile ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#dynamicfromfile)
- [ PGConnectionParameters ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgconnectionparameters)
- [ PGPoolSettings ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgpoolsettings)
- [ PGCertSettings ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcertsettings)
- [ MsSQLPoolSettings ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#mssqlpoolsettings)
- [ PGColumnType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumntype)
- [ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgcolumn)
- [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#relationshipname)
- [ Table Config ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#table-config)
- [ Custom Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#custom-root-fields)
- [ CustomRootField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customrootfield)
- [ ColumnConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnconfig)
- [ ColumnConfigValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnconfigvalue)
- [ Custom Function Root Fields ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#custom-function-root-fields)
- [ InputValidationDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#input-validation-definition)
- [ InputValidation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#input-validation)
- [ InsertPermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#insertpermission)
- [ SelectPermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#selectpermission)
- [ UpdatePermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#updatepermission)
- [ DeletePermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#deletepermission)
- [ LogicalModelSelectPermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#logicalmodelselectpermission)
- [ ObjRelUsing ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#objrelusing)
- [ ObjRelUsingChoice ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#objrelusingchoice)
- [ SameTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#sametable)
- [ RemoteTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remotetable)
- [ ObjRelUsingManualMapping ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#objrelusingmanualmapping)
- [ InsertOrder ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#insertorder)
- [ ArrRelUsing ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#arrrelusing)
- [ ArrRelUsingFKeyOn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#arrrelusingfkeyon)
- [ ArrRelUsingManualMapping ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#arrrelusingmanualmapping)
- [ ScheduledEventStatus ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#scheduledEventStatus)
- [ BoolExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#boolexp)
- [ AndExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#andexp)
- [ OrExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#orexp)
- [ NotExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#notexp)
- [ ExistsExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#existsexp)
- [ TrueExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#trueexp)
- [ ColumnExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnexp)
- [ Operator ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#metadataoperator)
- [ Object ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#object)
- [ Empty Object ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#empty-object)
- [ ColumnPresetsExp ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#columnpresetexp)
- [ Query root field ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#queryRootField)
- [ Subscription root field ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#subscriptionRootField)
- [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remoteschemaname)
- [ RemoteSchemaDef ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remoteschemadef)
- [ RemoteSchemaCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remoteschemacustomization)
- [ RemoteTypeCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remotetypecustomization)
- [ RemoteFieldCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remotefieldcustomization)
- [ SourceCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#sourcecustomization)
- [ RootFieldsCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#rootfieldscustomization)
- [ SourceTypeCustomization ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#sourcetypecustomization)
- [ CollectionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#collectionname)
- [ QueryName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#queryname)
- [ CollectionQuery ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#collectionquery)
- [ AllowlistScope ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#allowlistscope)
- [ EndpointUrl ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#endpointurl)
- [ EndpointMethods ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#endpointmethods)
- [ EndpointDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#endpointdef)
- [ CustomColumnNames ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#customcolumnnames)
- [ ActionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#actionname)
- [ WebhookURL ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#webhookurl)
- [ HeaderFromValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerfromvalue)
- [ HeaderFromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerfromenv)
- [ GraphQLType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqltype)
- [ GraphQLName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#graphqlname)
- [ ActionDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#actiondefinition)
- [ InputArgument ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#inputargument)
- [ ComputedFieldDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#computedfielddefinition)
- [ BigQuery ComputedFieldDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#bigquerycomputedfielddefinition)
- [ LogicalModelField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#logicalmodelfield)
- [ LogicalModelType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#logicalmodeltype)
- [ NativeQueryArgument ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#nativequeryargument)
- [ NativeQueryRelationship ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#nativequeryrelationship)
- [ Stored Procedure Argument ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#stored-procedure-argument)
- [ Stored Procedure Configuration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#stored-procedure-configuration)
- [ Function Configuration ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#function-configuration)
- [ InputObjectType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#inputobjecttype)
    - [ InputObjectField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#inputobjectfield)
- [ ObjectType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#objecttype)
    - [ ObjectField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#objectfield)

- [ ObjectRelationship ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#objectrelationship)
- [ ScalarType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#scalartype)
- [ EnumType ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#enumtype)
    - [ EnumValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#enumvalue)
- [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#triggername)
- [ OperationSpec ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#operationspec)
- [ EventTriggerColumns ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#eventtriggercolumns)
- [ RequestTransformation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#requesttransformation)
- [ TransformHeaders ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#transformheaders)
- [ HeaderKey ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headerkey)
- [ HeaderValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#headervalue)
- [ BodyTransform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#bodytransform)
- [ TemplateEngine ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#templateengine)
- [ ResponseTransformation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#responsetransformation)
- [ RetryConf ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#retryconf)
- [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remoterelationshipname)
- [ RemoteRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remoterelationshipdefinition)
- [ ToSourceRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#tosourcerelationshipdefinition)
- [ ToSchemaRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#toschemarelationshipdefinition)
- [ RemoteField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remotefield)
- [ InputArguments ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#inputarguments)
- [ RemoteSchemaPermission ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#remoteschemapermission)
- [ UrlFromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#urlfromenv)
- [ RetryConfST ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#retryconfst)
- [ ApolloFederationConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#apollofederationconfig)
- [ AutoEventTriggerCleanupConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#autoeventtriggercleanupconfig)
- [ TriggerLogCleanupSources ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#triggerlogcleanupsources)
- [ EventTriggerQualifier ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#eventtriggerqualifier)
- [ APILimitOption ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#apilimitoption)
- [ RateLimitOption ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#ratelimitoption)
- [ RateLimitPerRoleOption ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#ratelimitperroleoption)
- [ PGConnectionTemplate ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#pgconnectiontemplate)
- [ ConnectionSetElementConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#connectionsetelementconfig)
- [ RequestContext ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#requestcontext)
- [ QueryContext ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#queryContext)
- [ Attribute ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#attribute)
- [ OTLPExporter ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#otlpexporter)
- [ OpenTelemetryBatchSpanProcessor ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename/#opentelemetrybatchspanprocessor)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)