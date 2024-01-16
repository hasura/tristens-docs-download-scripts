# Hasura CLI: hasura metadata inconsistency drop

Drop inconsistent objects from the Hasura Metadata.

## Synopsis​

At times, when developing, the Hasura Metadata can become inconsistent. This command can be used to drop inconsistent objects from the Hasura Metadata and bring your project's Metadata back to a consistent state.

Further reading:

- [ https://hasura.io/docs/latest/migrations-metadata-seeds/resetting-migrations-metadata/ ](https://hasura.io/docs/latest/migrations-metadata-seeds/resetting-migrations-metadata/)


`hasura metadata inconsistency drop  [ flags ]`

## Options​

`-h, --help   help for drop`

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

- [ hasura metadata inconsistency ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_inconsistency/)- Manage inconsistent objects in the Hasura Metadata


 *Auto generated by spf13/cobra* 

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_inconsistency_drop/#synopsis)
- [ Options ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_inconsistency_drop/#options)
- [ Options inherited from parent commands ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_inconsistency_drop/#options-inherited-from-parent-commands)
- [ SEE ALSO ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_metadata_inconsistency_drop/#see-also)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)