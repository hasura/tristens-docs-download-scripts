# Commands

## Overview​

The Hasura CLI Gateway plugin utilizes a typical command / flag syntax enabling you to quickly manage your Hasura
federated instances under a parent gateway instance. A typical command structure will follow this pattern:

`hasura gateway -- < flag >   "<flag_value>"   < command >`

A real-world example following this structure would be:

`hasura gateway --gateway-url https://gateway-hasura-app.hasura.app --gateway-configuration-file /path/to/gateway-configuration.json --admin-secret myadminsecret check`

This snippet illustrates the `check` command with three flags and their respective values (i.e., `gateway-url` , `gateway-configuration-file` , and `admin-secret` ).

Gateway configuration file format

A sample gateway configuration, which represents the child Hasura instance's Remote Schema, looks like this:

```
{
   "name" :   "hasura-1" ,
   "definition" :   {
     "url" :   "https://hasura-1.hasura.app/v1/graphql" ,
     "timeout_seconds" :   60 ,
     "customization" :   { } ,
     "headers" :   [
       {
         "name" :   "x-hasura-admin-secret" ,
         "value" :   "hasura-1-admin-secret"
       }
     ] ,
     "forward_client_headers" :   true
   } ,
   "comment" :   "Hasura Child instance 1 for this parent gateway"
}
```

## Getting help​

At any time, you can use the `--help` flag on a certain command. Running `hasura gateway --help` will return information
on available commands and flags:

```
NAME:
   gateway - Manage your gateway Hasura instance
USAGE:
   gateway [global options] command [command options] [arguments...]
COMMANDS:
   build    Append the given remote schema configuration in the gateway metadata and print it to stdout
   check    Check if the configuration of current Hasura project is compatible as remote schema in your gateway Hasura instance
   publish  Add the configuration of current Hasura project as remote schema in your gateway Hasura instance
   help, h  Shows a list of commands or help for one command
GLOBAL OPTIONS:
   --gateway-url value                 The URL of your gateway Hasura instance
   --gateway-headers value             The headers required to access your gateway Hasura instance
   --gateway-configuration-file value  Path to the configuration of your current Hasura instance i.e. the remote-schema configuration that must go into the metadata of the gateway Hasura
   --admin-secret value                The admin secret of Gateway Hasura instance
   --help, -h                          show help
Use "gateway [command] --help" for more information about a command.
```

Support for headers

 `gateway-headers` is not supported currently.

### What did you think of this doc?

- [ Overview ](https://hasura.io/docs/latest/hasura-cli/gateway-plugin/commands/index/#overview)
- [ Getting help ](https://hasura.io/docs/latest/hasura-cli/gateway-plugin/commands/index/#getting-help)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)