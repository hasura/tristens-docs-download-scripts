# Relay GraphQL API Reference

## Introduction​

All GraphQL requests for Relay queries are made to the Relay GraphQL API.

## Endpoint​

All requests are `POST` requests to the `/v1beta1/relay` endpoint.

## Request types​

The following types of requests can be made using the Relay GraphQL API:

- [ Query / Subscription ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/)
- [ Mutation ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/mutation/)


## Batching requests​

The Relay GraphQL API provides support for batched requests over the `/v1beta1/relay` endpoint.

 **Example:** using a client which supports batching (such as Apollo
Client), we can send two query operations in one request:

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/index/#introduction)
- [ Endpoint ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/index/#endpoint)
- [ Request types ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/index/#request-types)
- [ Batching requests ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/index/#batching-requests)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)