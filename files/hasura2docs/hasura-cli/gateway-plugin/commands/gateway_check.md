# Hasura CLI: gateway check

Check the compatibility of the child Remote Schema configuration with the gateway configuration.

## Synopsis​

This command reads the Remote Schema configuration of the current child Hasura present in the file mentioned by the flag `--gateway-configuration-file` , appends it to the gateway's metadata, and checks for consistency of the final metadata with
the gateway. Please note:

- `gateway-url` , `gateway-configuration-file` , and the gateway's `admin-secret` are required to run this command.


`hasura gateway  [ flags ]  check`

## Usage​

```
# Checking compatibility of the configuration present in gateway-configuration.json with gateway instance
hasura gateway --gateway-url https://gateway-hasura-app.hasura.app --gateway-configuration-file /path/to/gateway-configuration.json --admin-secret myadminsecret check
```

## Options​

```
     --gateway-url  string                  url of the gateway instance
     --gateway-configuration-file  string   path to the current Hasura's configuration
     --admin-secret  string                 admin secret of the gateway
-h, --help                                help for check
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/latest/hasura-cli/gateway-plugin/commands/gateway_check/#synopsis)
- [ Usage ](https://hasura.io/docs/latest/hasura-cli/gateway-plugin/commands/gateway_check/#usage)
- [ Options ](https://hasura.io/docs/latest/hasura-cli/gateway-plugin/commands/gateway_check/#options)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)