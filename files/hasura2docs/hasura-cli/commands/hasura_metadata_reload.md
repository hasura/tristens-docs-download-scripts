# Hasura CLI: hasura metadata reload

Reload Hasura GraphQL Engine schema to pick up changes in any underlying data sources (database or remote schema).

## Synopsis​

hasura metadata reload should be used when there is a change in the underlying data sources (database or remote schema) that Hasura should be aware of.
Example:
A new column is added to a table and this column should now be added to the GraphQL schema.

`hasura metadata reload  [ flags ]`

## Examples​

```
# Reload all the metadata information from database:
hasura metadata reload
# Use with admin secret:
hasura metadata reload --admin-secret  "<admin-secret>"
# Use with a specific endpoint:
hasura metadata reload --endpoint  "<endpoint>"
```

## Options​

`-h, --help   help for reload`

## Options inherited from parent commands​

```
--admin-secret  string            admin secret for Hasura GraphQL Engine  ( env  "HASURA_GRAPHQL_ADMIN_SECRET" )
--certificate-authority  string   path to a cert file for the certificate authority  ( env  "HASURA_GRAPHQL_CERTIFICATE_AUTHORITY" )
--endpoint  string                 http ( s )  endpoint for Hasura GraphQL Engine  ( env  "HASURA_GRAPHQL_ENDPOINT" )
--envfile  string                 .env filename to load ENV vars from  ( default  ".env" )
--insecure-skip-tls-verify        skip TLS verification and disable cert checking  ( default :  false )   ( env  "HASURA_GRAPHQL_INSECURE_SKIP_TLS_VERIFY" )
--log-level  string               log level  ( DEBUG ,  INFO ,  WARN ,  ERROR ,  FATAL )   ( default  "INFO" )
--no-color                        do not colorize output  ( default :  false )
--project  string                 directory where commands are executed  ( default :  current dir )
--skip-update-check               skip automatic update check on command execution
```

## SEE ALSO​

- [ hasura metadata ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata/)- Manage Hasura GraphQL Engine Metadata saved in the database


 *Auto generated by spf13/cobra* 

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_reload/#synopsis)
- [ Examples ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_reload/#examples)
- [ Options ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_reload/#options)
- [ Options inherited from parent commands ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_reload/#options-inherited-from-parent-commands)
- [ SEE ALSO ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_reload/#see-also)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)