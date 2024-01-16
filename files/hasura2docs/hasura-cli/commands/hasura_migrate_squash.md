# Hasura CLI: hasura migrate squash

(PREVIEW) Squash multiple migrations into a single one.

## Synopsis​

As you're developing your Hasura GraphQL API, you may find yourself in a situation where you have a lot of migrations that you want to squash into a single one. This command helps you do that. By running this command, you can squash all the iterative migrations you've created into a single file.

`hasura migrate squash  [ flags ]`

## Examples​

```
# NOTE: This command is in PREVIEW. Correctness is not guaranteed and the usage may change.
# squash all migrations from version 123 to the latest one:
hasura migrate squash --from  123
# Add a name for the new squashed migration
hasura migrate squash --name  "<name>"  --from  123
```

## Options​

```
     --delete-source    delete the source files after squashing without any confirmation
     --from  uint       start squashing from this version
-h, --help            help for squash
     --name  string     name for the new squashed migration  ( default  "squashed" )
     --to  int          squash up to this version  ( default  -1 )
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

- [ hasura migrate ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_migrate/)- Manage migrations on the database


 *Auto generated by spf13/cobra* 

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_migrate_squash/#synopsis)
- [ Examples ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_migrate_squash/#examples)
- [ Options ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_migrate_squash/#options)
- [ Options inherited from parent commands ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_migrate_squash/#options-inherited-from-parent-commands)
- [ SEE ALSO ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_migrate_squash/#see-also)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)