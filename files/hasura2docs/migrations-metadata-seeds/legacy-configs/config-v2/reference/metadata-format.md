# Metadata Format Reference (config v2)

## Introduction​

With `config v2` , the Metadata that is exported from the server by the CLI is a directory of multiple files.

Note

For `config v1` , see[ Metadata file format reference (config v1) ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v1/reference/metadata-file-format/).

## Metadata directory format​

The following files will be generated in the `metadata/` directory of your project:

- [ actions.graphql ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#actionsgraphql)
- [ actions.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#actionsyaml)
- [ allow_list.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#allow_listyaml)
- [ cron_triggers.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#cron_triggersyaml)
- [ functions.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#functionsyaml)
- [ query_collections.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#query_collectionsyaml)
- [ remote_schemas.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#remote_schemasyaml)
- [ tables.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#tablesyaml)
- [ version.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#versionyaml)


Note

The output of the[ export_metadata ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-export-metadata)metadata
API is a JSON version of the Metadata files.

### actions.graphql​

The `actions.graphql` file contains all the[ actions ](https://hasura.io/docs/latest/actions/overview/)definitions and[ custom type ](https://hasura.io/docs/latest/actions/types/index/)definitions.

 **Example** : A query action called `greet` and two custom types called `SampleInput` and `SampleOutput` .

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

The `actions.yaml` file contains Metadata related to[ Actions ](https://hasura.io/docs/latest/actions/overview/).

 **Example** : An action called `greet` with the `handler` set to `<base_url>/greet` and two custom types called `SampleInput` and `SampleOutput` .

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

 **Example** : Same example as above but with the base URL of the `handler` passed as an environment variable.

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

 **Example** : A query collection called `allowed-queries` set as the allow-list.

`-   collection :  allowed - queries`

### cron_triggers.yaml​

The `cron_triggers.yaml` file contains Metadata related to[ cron triggers ](https://hasura.io/docs/latest/scheduled-triggers/create-cron-trigger/).
The `webhook` can be an HTTP endpoint or an environment variable containing the HTTP endpoint.

 **Example** : A cron trigger called `test-trigger` .

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

### functions.yaml​

Contains the Metadata related to[ custom functions ](https://hasura.io/docs/latest/schema/postgres/custom-functions/).

 **Example** : A custom SQL function called `search_books` .

```
-   function :
   schema :  public
   name :  search_books
```

### query_collections.yaml​

The `query_collections.yaml` file contains Metadata information about[ query collections ](https://hasura.io/docs/latest/api-reference/metadata-api/query-collections/).

 **Example** : A query collection called `sample-collection` which contains two queries `test` and `test2` .

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

 **Example** : A Remote Schema called `my-remote-schema` with URL `<remote-schema-url>` .

```
-   name :  my - remote - schema
   definition :
     url :  <remote - schema - url >
     timeout_seconds :   40
```

 **Example** : A Remote Schema called `my-remote-schema` with URL passed as environment variable.

```
-   name :  my - remote - schema
   definition :
     url_from_env :  REMOTE_SCHEMA
     timeout_seconds :   40
```

### tables.yaml​

The `tables.yaml` file contains Metadata related to[ tables ](https://hasura.io/docs/latest/schema/postgres/tables/).

 **Example** : Two tables called `authors` and `books` including relationships and an Event Trigger defined on the `authors` table.

```
-   table :
     schema :  public
     name :  authors
   insert_permissions :
     -   role :  user
       permission :
         check :
           id :
             _eq :  X - Hasura - User - Id
         columns :
           -  name
         backend_only :   false
   select_permissions :
     -   role :  user
       permission :
         columns :
           -  id
           -  name
         filter :
           id :
             _eq :  X - Hasura - User - Id
   array_relationships :
     -   name :  books
       using :
         foreign_key_constraint_on :
           column :  author_id
           table :
             schema :  public
             name :  books
   event_triggers :
     -   name :  event_test
       definition :
         enable_manual :   false
         insert :
           columns :   '*'
         delete :
           columns :   '*'
         update :
           columns :
             -  id
             -  author_name
       retry_conf :
         num_retries :   1
         interval_sec :   10
         timeout_sec :   60
       webhook :  <webhook_url >
-   table :
     schema :  public
     name :  books
   insert_permissions :
     -   role :  user
       permission :
         check :
           id :
             _eq :  X - Hasura - User - Id
         columns :
           -  author_id
           -  name
         backend_only :   false
   select_permissions :
     -   role :  user
       permission :
         columns :
           -  id
           -  name
         filter :
           id :
             _eq :  X - Hasura - User - Id
   object_relationships :
     -   name :  author
       using :
         foreign_key_constraint_on :  author_id
```

### version.yaml​

The `version.yaml` file contains the Metadata format version.

`version :   2`

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#introduction)
- [ Metadata directory format ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#metadata-directory-format)
    - [ actions.graphql ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#actionsgraphql)

- [ actions.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#actionsyaml)

- [ allow_list.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#allow_listyaml)

- [ cron_triggers.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#cron_triggersyaml)

- [ functions.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#functionsyaml)

- [ query_collections.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#query_collectionsyaml)

- [ remote_schemas.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#remote_schemasyaml)

- [ tables.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#tablesyaml)

- [ version.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/#versionyaml)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)