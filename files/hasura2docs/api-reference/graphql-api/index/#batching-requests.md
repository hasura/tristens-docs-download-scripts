# GraphQL API Reference

## Introduction​

All GraphQL requests for queries, subscriptions and mutations are made to the GraphQL API.

## Endpoint​

The GraphQL API is available at the `/v1/graphql` (or `/v1alpha1/graphql` ) endpoint of your Hasura GraphQL Engine
instance.

For example, if your GraphQL Engine is running at `https://my-graphql-engine.com` , the GraphQL API will be available at `https://my-graphql-engine.com/v1/graphql` via `POST` requests.

Note

The `/v1/graphql` endpoint returns HTTP 200 status codes for all responses. This is a **breaking** change from the `/v1alpha1/graphql` behavior, where request errors and internal errors were responded with 4xx and 5xx status codes.

## Request types​

The following types of requests can be made using the GraphQL API:

- [ Query / Subscription ](https://hasura.io/docs/latest/api-reference/graphql-api/query/)
- [ Mutation ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/)


## Batching requests​

The GraphQL API provides support for batched requests (which can be a combination of queries and mutations). The
endpoint will accept an array of operations in place of a single operation, and return an array of corresponding
responses.

 **Example:** using a client which supports batching (such as Apollo Client), we can send two query operations in one
request:

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/graphql-api/index/#batching-requests/#introduction)
- [ Endpoint ](https://hasura.io/docs/latest/api-reference/graphql-api/index/#batching-requests/#endpoint)
- [ Request types ](https://hasura.io/docs/latest/api-reference/graphql-api/index/#batching-requests/#request-types)
- [ Batching requests ](https://hasura.io/docs/latest/api-reference/graphql-api/index/#batching-requests/#batching-requests)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)