# Postgres: Streaming Subscriptions

## Introduction​

A streaming subscription streams the response according to the cursor provided by the user while making the
subscription. Streaming subscriptions can be used to subscribe only to the data which has been newly added to the result
set.

Supported from

Streaming subscriptions are supported in Hasura GraphQL Engine versions `v2.7.0-beta.1` and above.

## How it works?​

In streaming subscriptions, the server maintains a cursor value with a subscription and after streaming each batch, the
value of the cursor is updated. Ideally, the cursor chosen should represent unique and sortable values so that each row
is sent exactly once to a subscriber. **Hasura does not require sticky sessions for streaming subscriptions** .

Streaming subscriptions work well with other Hasura features like[ permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/)and[ relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/#table-relationships)and also leverage the power of[ subscriptions multiplexing ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/execution/#subscription-multiplexing).

Confguration details

In the case of streaming subscriptions, the multiplexed batch size can be configured via `HASURA_GRAPHQL_STREAMING_QUERIES_MULTIPLEXED_BATCH_SIZE` and the refetch interval can be configured via `HASURA_GRAPHQL_STREAMING_QUERIES_MULTIPLEXED_REFETCH_INTERVAL` .

## Use cases​

- [ Subscribe to the undelivered messages in a chat application ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/use-cases/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/index/#introduction)
- [ How it works? ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/index/#how-it-works)
- [ Use cases ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/index/#use-cases)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)