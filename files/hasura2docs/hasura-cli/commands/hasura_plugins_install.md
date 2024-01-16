# Hasura CLI: hasura plugins install

Install a plugin from the index.

## Synopsis​

To install plugins that extend the functionality of the Hasura CLI, you can use the install command. This command will install the plugin from the index and add it to your configuration file.

`hasura plugins  install   [ plugin-name ]   [ flags ]`

## Examples​

```
# Install a plugin:
hasura plugins  install   [ plugin-name ]
```

## Options​

```
-h, --help             help for install
     --version  string   version to be installed
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

- [ hasura plugins ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_plugins/)- Manage plugins for the CLI


 *Auto generated by spf13/cobra* 

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_plugins_install/#synopsis)
- [ Examples ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_plugins_install/#examples)
- [ Options ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_plugins_install/#options)
- [ Options inherited from parent commands ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_plugins_install/#options-inherited-from-parent-commands)
- [ SEE ALSO ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_plugins_install/#see-also)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)