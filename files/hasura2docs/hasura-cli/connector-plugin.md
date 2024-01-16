# Hasura Data Connector plugin on Hasura Cloud

This Hasura CLI plugin enables deployment and management of custom[ Hasura Data Connector ](https://hasura.io/docs/latest/databases/data-connectors/)agents to Hasura Cloud.

Want to build your own Data Connector?

If you're ready to build your own Data Connector, or want to see what community-built connectors you can deploy today,
check out the[ Native Data Connector Hub ](https://github.com/hasura/ndc-hub).

## Install the Hasura CLI Data Connector plugin​

To start deploying Data Connectors using the Data Connector plugin, the following pre-requisites need to be in place:

1. Install[ Hasura CLI ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/)
2. Update plugin index


Install[ Hasura CLI ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/)

Update plugin index

`hasura plugins list`

1. Install `cloud` plugin


`hasura plugins  install  cloud`

1. Authenticate the CLI with Hasura Cloud


`hasura cloud login`

1. Install `connector` plugin


`hasura plugins  install  connector`

1. Verify installation with the `--help` flag


`hasura connector --help`

## Uninstall the Hasura CLI Data Connector plugin​

To uninstall the Hasura CLI Data Connector plugin, use the `uninstall` command:

`hasura plugins uninstall connector`

### What did you think of this doc?

- [ Install the Hasura CLI Data Connector plugin ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/#install-the-hasura-cli-data-connector-plugin)
- [ Uninstall the Hasura CLI Data Connector plugin ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/#uninstall-the-hasura-cli-data-connector-plugin)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)