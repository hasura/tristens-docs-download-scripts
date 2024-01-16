# Hasura GraphQL Data Connector SDK

## Introduction​

The Data Connector SDK serves as a pack of documentation and resources for understanding, building, and testing Data
Connector Agent implementations to ensure that they are complete, correct, idiomatic and can be developed rapidly and
with confidence. The workflow that the SDK supports out of the box is powered by Docker Compose in order to reduce the
number of dependencies required, but each component may be run natively if desired. The SDK is versioned with the Hasura
GraphQL Engine.

The SDK including the `docker-compose.yaml` file can be[ found here ](https://github.com/hasura/graphql-engine/tree/master/dc-agents/sdk).

For more details on the SDK, check out the[ SDK repository README.md ](https://github.com/hasura/graphql-engine/blob/master/dc-agents/sdk/README.md).

## Building a new Data Connector with the SDK​

To create a new Data Connector, follow these steps:

1. [ Start the container ](https://github.com/hasura/graphql-engine/blob/master/dc-agents/sdk/docker-compose.yaml)with `docker compose up` .
2. Verify that the tests pass.
3. Review and make changes to the reference connector for your specific database and intended implementation.
4. Or rebuild as required, depending on your stack.
5. Rerun the tests with `docker compose run tests` .
6. Interact with the Agent via Hasura GraphQL Engine at `http://localhost:8080` and view the OpenAPI Schema at `http://localhost:8300` .


## Reference Connector​

The reference connector is located under the `/reference` path within the SDK and serves as a working connector example.
It is written in TypeScript and has several key code snippet examples within the reference itself. For more information
on the reference connector, check out[ README in the reference directory ](https://github.com/hasura/graphql-engine/tree/master/dc-agents/reference).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/data-connectors/data-connector-sdk/#introduction)
- [ Building a new Data Connector with the SDK ](https://hasura.io/docs/latest/databases/data-connectors/data-connector-sdk/#building-a-new-data-connector-with-the-sdk)
- [ Reference Connector ](https://hasura.io/docs/latest/databases/data-connectors/data-connector-sdk/#reference-connector)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)