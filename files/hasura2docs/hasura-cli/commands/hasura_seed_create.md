# Hasura CLI: hasura seed create

Create a new seed file.

## Synopsis​

This will create a new seed file with the name provided as an argument. You can export tables from the database and create a seed file from it by using the `--from-table` flag.

Further reading:

- [ https://hasura.io/docs/latest/migrations-metadata-seeds/manage-seeds/ ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-seeds/)


`hasura seed create seed_name  [ flags ]`

## Examples​

```
# Create a new seed file and use editor to add SQL:
hasura seed create new_table_seed
# Create a new seed by exporting data from tables already present in the database:
hasura seed create table1_seed --from-table table1
# Export data from multiple tables:
hasura seed create tables_seed --from-table table1 --from-table table2
```

## Options​

```
     --from-table  stringArray   name of table from which seed file has to be initialized. e.g. table1 ,  myschema1.table1
-h, --help                     help for create
```

## Options inherited from parent commands​

```
--admin-secret  string            admin secret for Hasura GraphQL Engine  ( env  "HASURA_GRAPHQL_ADMIN_SECRET" )
--certificate-authority  string   path to a cert file for the certificate authority  ( env  "HASURA_GRAPHQL_CERTIFICATE_AUTHORITY" )
--database-name  string           database on which operation should be applied
--disable-interactive             disables interactive prompts  ( default :  false )   ( env  "HASURA_GRAPHQL_DISABLE_INTERACTIVE" )
--endpoint  string                 http ( s )  endpoint for Hasura GraphQL Engine  ( env  "HASURA_GRAPHQL_ENDPOINT" )
--envfile  string                 .env filename to load ENV vars from  ( default  ".env" )
--insecure-skip-tls-verify        skip TLS verification and disable cert checking  ( default :  false )   ( env  "HASURA_GRAPHQL_INSECURE_SKIP_TLS_VERIFY" )
--log-level  string               log level  ( DEBUG ,  INFO ,  WARN ,  ERROR ,  FATAL )   ( default  "INFO" )
--no-color                        do not colorize output  ( default :  false )
--project  string                 directory where commands are executed  ( default :  current dir )
--skip-update-check               skip automatic update check on command execution
```

## SEE ALSO​

- [ hasura seed ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_seed/)- Manage seed data


 *Auto generated by spf13/cobra* 

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_seed_create/#synopsis)
- [ Examples ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_seed_create/#examples)
- [ Options ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_seed_create/#options)
- [ Options inherited from parent commands ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_seed_create/#options-inherited-from-parent-commands)
- [ SEE ALSO ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_seed_create/#see-also)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)