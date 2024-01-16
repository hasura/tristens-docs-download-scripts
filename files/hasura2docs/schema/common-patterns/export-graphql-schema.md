# Export the Hasura GraphQL Schema

## Introduction​

If you need to share, introspect or export the GraphQL schema, you can use community tooling such as[ graphqurl ](https://github.com/hasura/graphqurl),[ Apollo CLI ](https://github.com/apollographql/apollo-tooling),[ get-graphql-schema ](https://github.com/prismagraphql/get-graphql-schema), etc.

## Using graphqurl​

For example, using `graphqurl` , you can get the schema as follows:

Run `npm install -g graphqurl` to install `graphqurl` . Then you can run the following commands to download the GraphQL
schema:

```
# If the GraphQL Engine is running at https://my-graphql-engine.com/v1/graphql,
# without an admin secret
gq https://my-graphql-engine.com/v1/graphql --introspect  >  schema.graphql
# If Hasura GraphQL Engine is running with an admin secret
gq https://my-graphql-engine.com/v1/graphql -H  "X-Hasura-Admin-Secret: adminsecretkey"  --introspect  >  schema.graphql
```

By default, it downloads the schema in `.graphql` format. If you want it in JSON format, you can use an additional flag `--format json` :

```
# Getting the schema in .json format
gq https://my-graphql-engine.com/v1/graphql --introspect --format json  >  schema.json
```

## Using Apollo CLI​

Using Apollo CLI, you can get the schema as follows:

Run `npm install -g apollo` to install the Apollo CLI. You can then run the following command to download the GraphQL
schema:

```
# If the GraphQL Engine is running at https://my-graphql-engine.com/v1/graphql,
# without an admin secret
apollo schema:download --endpoint https://my-graphql-engine.com/v1/graphql
# If Hasura GraphQL Engine is running with an admin secret
apollo schema:download --endpoint https://my-graphql-engine.com/v1/graphql --header  "X-Hasura-Admin-Secret: adminsecretkey"
```

Note that `apollo schema:download` is an alias of the command[ apollo service:download ](https://github.com/apollographql/apollo-tooling#apollo-servicedownload-output).

By default, this downloads the schema to a file called `schema.json` . This command has no other output types.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/common-patterns/export-graphql-schema/#introduction)
- [ Using graphqurl ](https://hasura.io/docs/latest/schema/common-patterns/export-graphql-schema/#using-graphqurl)
- [ Using Apollo CLI ](https://hasura.io/docs/latest/schema/common-patterns/export-graphql-schema/#using-apollo-cli)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)