# Metadata File Format Reference (config v1)

## Introduction​

The Metadata file that is exported from the server is a JSON/YAML
representation of the Hasura Metadata stored in the `hdb_catalog` schema
on the Postgres database.

The top level keys will be the following arrays:

```
functions :   [ ]
remote_schemas :   [ ]
tables :   [ ]
```

Depending on the tables tracked, Remote Schemas and custom functions created,
these keys will have elements inside them.

The `table` will have permission rules, relationships and Event Triggers
defined for each table. Here is an example Metadata file:

## metadata.yaml​

```
functions :
   -  search_articles
remote_schemas :
   -   comment :   null
     definition :
       forward_client_headers :   false
       headers :   [ ]
       url :  https : //graphql - pokemon.now.sh/graphql
       url_from_env :   null
     name :  pokemon
tables :
   -   table :  author
     array_relationships :
       -   comment :   null
         name :  articlesByauthorId
         using :
           foreign_key_constraint_on :
             column :  author_id
             table :  article
     delete_permissions :   [ ]
     event_triggers :   [ ]
     insert_permissions :
       -   comment :   null
         permission :
           check :
             id :
               _eq :  X - Hasura - User - Id
           columns :
             -  name
           set :   { }
         role :  user
     object_relationships :   [ ]
     select_permissions :
       -   comment :   null
         permission :
           allow_aggregations :   false
           columns :
             -  id
             -  name
           filter :
             id :
               _eq :  X - Hasura - User - Id
         role :  user
     update_permissions :   [ ]
   -   table :  article
     array_relationships :   [ ]
     delete_permissions :   [ ]
     event_triggers :
       -   definition :
           delete :
             columns :   '*'
           insert :
             columns :   '*'
           update :
             columns :
               -  id
               -  title
               -  author_id
         headers :   [ ]
         name :  update_article_search_index
         retry_conf :
           interval_sec :   10
           num_retries :   0
           timeout_sec :   60
         webhook :  https : //my - algolia - api.com/update_index
     insert_permissions :
       -   comment :   null
         permission :
           check :
             author_id :
               _eq :  X - Hasura - User - Id
           columns :
             -  title
           set :
             author_id :  x - hasura - user - id
         role :  user
     object_relationships :
       -   comment :   null
         name :  authorByauthorId
         using :
           foreign_key_constraint_on :  author_id
     select_permissions :
       -   comment :   null
         permission :
           allow_aggregations :   true
           columns :
             -  author_id
             -  id
             -  title
           filter :
             author_id :
               _eq :  X - Hasura - User - Id
         role :  user
     update_permissions :   [ ]
```

The schema for this file will mostly correspond to the table structure
of the[ Metadata catalogue ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v1/reference/metadata-schema/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v1/reference/metadata-file-format/#introduction)
- [ metadata.yaml ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v1/reference/metadata-file-format/#metadatayaml)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)