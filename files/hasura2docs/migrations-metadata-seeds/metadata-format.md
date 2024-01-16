# Metadata Format Reference

## Introduction​

With Metadata config `v3` , the Metadata that is exported from the server by the CLI is a directory of multiple files and
directories as per the example below:

```
📂 metadata
├─ 📂 databases
│  ├─ 📄 databases.yaml
│  └─ 📂 default
│     ├─ 📂 tables
│     │  ├─ 📄 public_author.yaml
│     │  ├─ 📄 public_article.yaml
│     │  └─ 📄 tables.yaml
│     └─ 📂 functions
│        ├─ 📄 public_search_author.yaml
│        └─ 📄 functions.yaml
├─ 📄 actions.graphql
├─ 📄 actions.yaml
├─ 📄 allow_list.yaml
├─ 📄 api_limits.yaml
├─ 📄 cron_triggers.yaml
├─ 📄 graphql_schema_introspection.yaml
├─ 📄 inherited_roles.yaml
├─ 📄 network.yaml
├─ 📄 query_collections.yaml
├─ 📄 remote_schemas.yaml
├─ 📄 rest_endpoints.yaml
└─ 📄 version.yaml
```

Internally in Hasura Server, Metadata is maintained as a JSON blob in the `hdb_metadata` table of the Metadata database.

note

For `config v2` , see[ Metadata format reference (config v2) ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/).

## Metadata directory format​

The following files will be generated in the `metadata/` directory of your project:

Note

The output of the[ export_metadata ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-export-metadata)Metadata
API is a JSON version of the Metadata files.

### databases​

```
📂 databases
├─ 📄 databases.yaml
└─ 📂 default
  ├─ 📂 tables
  │  ├─ 📄 public_author.yaml
  │  ├─ 📄 public_article.yaml
  │  └─ 📄 tables.yaml
  └─ 📂 functions
     ├─ 📄 public_search_author.yaml
     └─ 📄 functions.yaml
```

#### databases.yaml​

```
-   name :  default
   kind :  postgres
   configuration :
     connection_info :
       use_prepared_statements :   false
       database_url :
         from_env :  PG_DATABASE_URL
       isolation_level :  read - committed
   tables :   '!include default/tables/tables.yaml'
```

Note

 `database_url` can be set as a string literal by omitting the `from_env` property.

#### [database-name]​

Directory with Metadata related to a database.

```
📂 default
├─ 📂 tables
│  ├─ 📄 public_author.yaml
│  ├─ 📄 public_article.yaml
│  └─ 📄 tables.yaml
└─ 📂 functions
   ├─ 📄 public_search_author.yaml
   └─ 📄 functions.yaml
```

##### tables​

Directory with Metadata related to a database's tables and views.

```
📂 tables
├─ 📄 public_author.yaml
├─ 📄 public_article.yaml
└─ 📄 tables.yaml
```

###### tables.yaml​

The `tables.yaml` file contains a list of all further database table `yaml` files which need to be included in the
metadata.

 **Example** : A `tables.yaml` file which specifies further `author` and `article` table files

```
-   '!include public_author.yaml'
-   '!include public_article.yaml'
```

###### [table-name].yaml​

The specific files for each database table contain all the Metadata information regarding each database table.

These files can contain information relating to the table for:

- Relationships including object and array relationships
- Remote relationships including those to Remote Schemas and remote databases
- Operation permissions per role
- Event Triggers
- Computed fields
- Whether the table is an enum table
- GraphQL field customization


 **Example** : A `public_author.yaml` table Metadata file specifying some of the above.

```
table :
   name :  author
   schema :  public
array_relationships :
   -   name :  articles
     using :
       foreign_key_constraint_on :
         column :  author_id
         table :
           name :  article
           schema :  public
insert_permissions :
   -   role :  user
     permission :
       check :
         id :
           _eq :  X - Hasura - User - Id
       set :
         id :  x - hasura - user - id
       columns :
         -  name
select_permissions :
   -   role :  user
     permission :
       columns :
         -  id
         -  name
       filter :
         id :
           _eq :  X - Hasura - User - Id
       allow_aggregations :   true
       query_root_fields :
         -  select
         -  select_by_pk
       subscription_root_fields :
         -  select
         -  select_by_pk
delete_permissions :
   -   role :  user
     permission :
       backend_only :   true
       filter :   { }
event_triggers :
   -   name :  author_created
     definition :
       enable_manual :   false
       insert :
         columns :   '*'
     retry_conf :
       interval_sec :   10
       num_retries :   0
       timeout_sec :   60
     webhook :  http : //httpbin.org/post
```

##### functions​

Directory with Metadata related to a database's functions tracked to be exposed as top-level GraphQL fields.

```
📂 functions
├─ 📄 public_search_author.yaml
└─ 📄 functions.yaml
```

###### functions.yaml​

The `functions.yaml` file contains a list of all further database function `yaml` files which need to be included in the
Metadata to be exposed as top-level GraphQL fields.

 **Example** : A `functions.yaml` file which specifies further `search_author` function file

`-   '!include public_search_author.yaml'`

###### [function-name].yaml​

The specific files for each database function contain all the Metadata information regarding exposing the database
function as a top-level GraphQL field.

 **Example** : A `public_search_author.yaml` function Metadata file

```
function :
   name :  search_author
   schema :  public
permissions :
   -   role :  user
```

### actions.graphql​

The `actions.graphql` file contains all the GraphQL[ Actions ](https://hasura.io/docs/latest/actions/overview/)and their[ custom type ](https://hasura.io/docs/latest/actions/types/index/)definitions.

 **Example** : A query action called `greet` and two custom types called `SampleInput` and `SampleOutput` 

```
type   Query   {
   greet ( arg1 :   SampleInput ! ) :   SampleOutput
}
input   SampleInput   {
   username :   String !
}
type   SampleOutput   {
   greetings :   String !
}
```

### actions.yaml​

The `actions.yaml` file contains Metadata related to[ actions ](https://hasura.io/docs/latest/actions/overview/).

 **Example** : An action called `greet` with the `handler` set to `<base_url>/greet` and two custom types called `SampleInput` and `SampleOutput` 

```
actions :
   -   name :  greet
     definition :
       kind :   ''
       handler :  <base_url > /greet
       forward_client_headers :   true
       headers :
         -   value :  application/json
           name :  Content - Type
custom_types :
   enums :   [ ]
   input_objects :
     -   name :  SampleInput
   objects :
     -   name :  SampleOutput
   scalars :   [ ]
```

 **Example** : Same example as above but with the base URL of the `handler` passed as an environment variable

```
actions :
   -   name :  greet
     definition :
       kind :   ''
       handler :   '{{ACTION_BASE_URL}}/greet'
       forward_client_headers :   true
       headers :
         -   value :  application/json
           name :  Content - Type
custom_types :
   enums :   [ ]
   input_objects :
     -   name :  SampleInput
   objects :
     -   name :  SampleOutput
   scalars :   [ ]
```

### allow_list.yaml​

The `allow_list.yaml` file contains the Metadata related to the[ allow list ](https://hasura.io/docs/latest/security/allow-list/).

 **Example** : A query collection called `allowed-queries` set as the allow-list

`-   collection :  allowed - queries`

### api_limits.yaml​

For Hasura Cloud and Hasura Enterprise the `api_limits.yaml` file contains the Metadata related to[ api limits ](https://hasura.io/docs/latest/security/api-limits/).

 **Example** : An api limit setting with global limits and a specific limit for a `customer` role

```
depth_limit :
   global :   10
   per_role :
     customer :   5
disabled :   false
node_limit :
   global :   10
   per_role :
     customer :   5
rate_limit :
   global :
     max_reqs_per_min :   100
     unique_params :   null
   per_role :
     customer :
       max_reqs_per_min :   60
       unique_params :   null
time_limit :
   global :   10
   per_role :
     customer :   5
```

### cron_triggers.yaml​

The `cron_triggers.yaml` file contains Metadata related to[ cron triggers ](https://hasura.io/docs/latest/scheduled-triggers/create-cron-trigger/).
The `webhook` can be an HTTP endpoint or an environment variable containing the HTTP endpoint.

 **Example** : A cron trigger called `test-trigger` 

```
-   name :  test - trigger
webhook :  <webhook - url >
schedule :  0 12 * * 1 - 5
include_in_metadata :   true
payload :   { }
retry_conf :
   num_retries :   1
   timeout_seconds :   60
   tolerance_seconds :   21600
   retry_interval_seconds :   10
```

Note

The Metadata about a cron trigger will not be stored if `Include this trigger in Hasura Metadata` is disabled in the
advanced option of `events` on the Console or `include_in_metadata` is passed as `false` via the API.

### graphql_schema_introspection.yaml​

For Hasura Cloud and Hasura Enterprise the `graphql_schema_introspection.yaml` file enables disabling of GraphQL
introspection for specified roles.

 **Example** : Disabling introspection for roles `customer` and `user` 

```
disabled_for_roles :
   -  customer
   -  user
```

### inherited_roles.yaml​

The `inherited_roles.yaml` file contains Metadata related to[ inherited roles ](https://hasura.io/docs/latest/auth/authorization/inherited-roles/).

 **Example** : An inherited role of `manager` which inherits from `user` and `customer` 

```
-   role_name :  manager
   role_set :
     -  user
     -  customer
```

### network.yaml​

The `network.yaml` file contains Metadata related to[ network options ](https://hasura.io/docs/latest/api-reference/metadata-api/network/).

 **Example** : A TLS Allowlist to represent a set of services that are permitted to use self-signed certificates

```
tls_allowlist :
   -   host :  graphql.hasura.io
     permissions :
       -  self - signed
     suffix :  core.graphql
```

### query_collections.yaml​

The `query_collections.yaml` file contains Metadata information about[ query collections ](https://hasura.io/docs/latest/api-reference/metadata-api/query-collections/).

 **Example** : A query collection called `sample-collection` which contains two queries `test` and `test2` 

```
-   name :  sample - collection
   definition :
     queries :
       -   name :  test
         query :   | -
          query test  {
            books  {
              id
              author_id
              title
             }
           }
       -   name :  test2
         query :   | -
          query test2  {
              authors {
                  id
                  author_name
               }
           }
```

### remote_schemas.yaml​

The `remote_schemas.yaml` file contains the Metadata related to[ Remote Schemas ](https://hasura.io/docs/latest/remote-schemas/overview/).

 **Example** : A Remote Schema called `my-remote-schema` with the URL `<remote-schema-url>` 

```
-   name :  my - remote - schema
   definition :
     url :  <remote - schema - url >
     timeout_seconds :   40
```

 **Example** : A Remote Schema called `my-remote-schema` with the URL passed as environment variable

```
-   name :  my - remote - schema
   definition :
     url_from_env :  REMOTE_SCHEMA
     timeout_seconds :   40
```

### rest_endpoints.yaml​

The `rest_endpoints.yaml` file contains the Metadata related to[ REST endpoints ](https://hasura.io/docs/latest/api-reference/restified/).

 **Example** : An example of a defined restified endpoint which gets an author based on their `id` 

```
-   comment :  Get an author based on their id
   definition :
     query :
       collection_name :  allowed - queries
       query_name :  Author by Id
   methods :
     -  GET
   name :  Author by Id
   url :  author/ : id
```

### version.yaml​

The `version.yaml` file contains the Metadata format version.

`version :   3`

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#introduction)
- [ Metadata directory format ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#metadata-directory-format)
    - [ databases ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#databases)
        - [ databases.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#databasesyaml)

- [ database-name ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#database-name)
    - [ tables ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#tables)
        - [ tables.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#tablesyaml)

- [ table-name.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#table-nameyaml)

- [ functions ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#functions)
    - [ functions.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#functionsyaml)

- [ function-name.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#function-nameyaml)

- [ tables ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#tables)
    - [ tables.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#tablesyaml)

- [ functions ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#functions)
    - [ functions.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#functionsyaml)

- [ database-name ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#database-name)
    - [ tables ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#tables)
        - [ tables.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#tablesyaml)

- [ actions.graphql ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#actionsgraphql)

- [ actions.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#actionsyaml)

- [ allow_list.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#allow_listyaml)

- [ api_limits.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#api_limitsyaml)

- [ cron_triggers.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#cron_triggersyaml)

- [ graphql_schema_introspection.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#graphql_schema_introspectionyaml)

- [ inherited_roles.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#inherited_rolesyaml)

- [ network.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#networkyaml)

- [ query_collections.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#query_collectionsyaml)

- [ remote_schemas.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#remote_schemasyaml)

- [ rest_endpoints.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#rest_endpointsyaml)

- [ version.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#versionyaml)

- [ databases ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#databases)
    - [ databases.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/#databasesyaml)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)