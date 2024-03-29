# Hasura CLI: connector list

List all Hasura Cloud Data Connectors owned by the user.

## Synopsis​

This command lists all custom Hasura Data Connector deployments triggered by the current user. It lists the connector names, endpoints to access, whether the connector is deployed and status of the deployment.

To use an endpoint in a Hasura Cloud project, you need to add it to the metadata, this can be done by following these steps:[ https://hasura.io/docs/latest/databases/data-connectors/#adding-hasura-graphql-data-connector-agent-to-metadata ](https://hasura.io/docs/latest/databases/data-connectors/#adding-hasura-graphql-data-connector-agent-to-metadata).

Further Reading:

- [ https://hasura.io/docs/latest/databases/data-connectors/ ](https://hasura.io/docs/latest/databases/data-connectors/)


`hasura connector list  [ flags ]`

## Examples​

```
# list all custom data connectors
hasura connector list
```

## Options​

`-h, --help   help for list`

## SEE ALSO​

- [ hasura connector ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/commands/connector/)- Hasura Data Connector CLI


 *Auto generated by spf13/cobra* 

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/commands/connector_list/#synopsis)
- [ Examples ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/commands/connector_list/#examples)
- [ Options ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/commands/connector_list/#options)
- [ SEE ALSO ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/commands/connector_list/#see-also)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)