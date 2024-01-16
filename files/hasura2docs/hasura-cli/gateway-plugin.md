# Hasura Gateway Plugin

This Hasura CLI Gateway Plugin enables publishing and management of Hasura federated instances and enables CI/CD support
for them. Users can `check` , `build` and `publish` the metadata of child Hasura instances added as Remote Schema
configurations to a parent gateway instance.

## Install the Hasura CLI Gateway Plugin​

To start using the Gateway plugin, the following pre-requisites are needed:

1. Install the[ Hasura CLI ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/)
2. Update the plugin index


Install the[ Hasura CLI ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/)

Update the plugin index

`hasura plugins list`

1. Install the `gateway` plugin


`hasura plugins  install  gateway`

1. Verify the installation with the `--help` flag


`hasura gateway --help`

## Uninstall the Hasura CLI Gateway Plugin​

To uninstall the Hasura CLI Gateway Plugin, use the `uninstall` command:

`hasura plugins uninstall gateway`

### What did you think of this doc?

- [ Install the Hasura CLI Gateway Plugin ](https://hasura.io/docs/latest/hasura-cli/gateway-plugin/#install-the-hasura-cli-gateway-plugin)
- [ Uninstall the Hasura CLI Gateway Plugin ](https://hasura.io/docs/latest/hasura-cli/gateway-plugin/#uninstall-the-hasura-cli-gateway-plugin)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)