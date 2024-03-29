# Hasura CLI: hasura actions

Manage Hasura Actions.

## Synopsis​

Running this command enables the use of additional sub-commands to create, modify, and export code related to a project's Actions.

Further Reading:

- [ https://hasura.io/docs/latest/actions/index/ ](https://hasura.io/docs/latest/actions/index/)
- [ https://hasura.io/docs/latest/actions/create/ ](https://hasura.io/docs/latest/actions/create/)
- [ https://hasura.io/docs/latest/actions/derive/ ](https://hasura.io/docs/latest/actions/derive/)


## Options​

```
     --admin-secret  string            admin secret for Hasura GraphQL Engine  ( env  "HASURA_GRAPHQL_ADMIN_SECRET" )
     --certificate-authority  string   path to a cert file for the certificate authority  ( env  "HASURA_GRAPHQL_CERTIFICATE_AUTHORITY" )
     --endpoint  string                 http ( s )  endpoint for Hasura GraphQL Engine  ( env  "HASURA_GRAPHQL_ENDPOINT" )
-h, --help                           help for actions
     --insecure-skip-tls-verify        skip TLS verification and disable cert checking  ( default :  false )   ( env  "HASURA_GRAPHQL_INSECURE_SKIP_TLS_VERIFY" )
```

## Options inherited from parent commands​

```
--envfile  string      .env filename to load ENV vars from  ( default  ".env" )
--log-level  string    log level  ( DEBUG ,  INFO ,  WARN ,  ERROR ,  FATAL )   ( default  "INFO" )
--no-color             do not colorize output  ( default :  false )
--project  string      directory where commands are executed  ( default :  current dir )
--skip-update-check    skip automatic update check on command execution
```

## SEE ALSO​

- [ hasura ](https://hasura.io/docs/latest/hasura-cli/commands/hasura/)- Hasura GraphQL Engine command line tool
- [ hasura actions codegen ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_actions_codegen/)- Generate code for Actions
- [ hasura actions create ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_actions_create/)- Create a Hasura Action
- [ hasura actions use-codegen ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_actions_use-codegen/)- Use the codegen to generate code for Hasura Actions


 *Auto generated by spf13/cobra* 

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_actions/#synopsis)
- [ Options ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_actions/#options)
- [ Options inherited from parent commands ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_actions/#options-inherited-from-parent-commands)
- [ SEE ALSO ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_actions/#see-also)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)