# Postgres: Live Query Subscriptions

## Introduction​

A Live query subscription will return the latest result of the query being made and not necessarily all the individual
events leading up to the result.

By default, updates are delivered to clients every **1 sec** .

See more details on[ subscriptions execution ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/execution/).

## Convert a query to a subscription​

You can turn any query into a subscription by simply replacing `query` with `subscription` as the operation type.

Single subscription in each query caveat

Hasura follows the[ GraphQL spec ](https://graphql.github.io/graphql-spec/June2018/#sec-Single-root-field)which allows
for only one root field in a subscription. You also cannot execute multiple separate subscriptions in one query. To
have multiple subscriptions running at the same time they must be in separate queries.

## Use cases​

- [ Subscribe to the latest value of a particular field ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-field)
- [ Subscribe to changes to a table’s entries ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-table)
- [ Subscribe to the latest value of some derived data ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/use-cases/#pg-subscribe-derived)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/index/#introduction)
- [ Convert a query to a subscription ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/index/#convert-a-query-to-a-subscription)
- [ Use cases ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/index/#use-cases)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)