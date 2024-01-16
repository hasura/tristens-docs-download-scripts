# Hasura CLI: hasura migrate apply

Apply migrations on the database.

## Synopsis​

Migrations represent the modifications needed to reach the desired state of a database schema. Running this command will apply the migrations on the database.

Further reading:

- [ https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/ ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/)


`hasura migrate apply  [ flags ]`

## Examples​

```
# Apply all migrations
hasura migrate apply
# Use with admin secret:
hasura migrate apply --admin-secret  "<admin-secret>"
# Apply migrations on another Hasura instance:
hasura migrate apply --endpoint  "<endpoint>"
# Mark migration as applied on the server and skip execution:
hasura migrate apply --skip-execution --version  "<version>"
# Mark migrations as applied on the server and skip execution:
hasura migrate apply --skip-execution --up all
# Mark migrations as rollbacked on the server and skip execution:
hasura migrate apply --skip-execution --down all
# Apply a particular migration version only:
hasura migrate apply --version  "<version>"
# Apply last 2 down migrations:
hasura migrate apply --down  2
# Apply only 2 up migrations:
hasura migrate apply --up  2
# Apply only a particular version
hasura migrate apply --type up --version  "<version>"
# Apply all up migrations upto version 125, last applied is 100
hasura migrate apply --goto  125
# Apply all down migrations upto version 125, last applied is 150
hasura migrate apply --goto  125
# Rollback a particular version:
hasura migrate apply --type down --version  "<version>"
# Rollback all migrations:
hasura migrate apply --down all
```

## Options​

```
     --up  string        apply all or N up migration steps
     --down  string      apply all or N down migration steps
     --goto  string      apply migration chain up to to the version specified
     --version  string   only apply this particular migration
     --skip-execution    skip executing the migration action ,  but mark them as applied
     --type  string      type of migration  ( up ,  down )  to be used with version flag  ( default  "up" )
     --dry-run           print the names of migrations which are going to be applied
     --all-databases     set this flag to attempt to apply migrations on all databases present on server
-h, --help             help for apply
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

- [ Synopsis ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_migrate_apply/#synopsis)
- [ Examples ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_migrate_apply/#examples)
- [ Options ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_migrate_apply/#options)
- [ Options inherited from parent commands ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_migrate_apply/#options-inherited-from-parent-commands)
- [ SEE ALSO ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_migrate_apply/#see-also)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)