# Multiple Queries in a Request

## Execution​

If multiple queries are part of the same request, they are executed **sequentially** , the individual responses are collated and returned
together. You can fetch objects of different unrelated types in the same
query.

## Run multiple top level queries in the same request​

 **For example** , fetch a list of `authors` and a list of `articles` :

### What did you think of this doc?

- [ Execution ](https://hasura.io/docs/latest/queries/postgres/multiple-queries/#execution)
- [ Run multiple top level queries in the same request ](https://hasura.io/docs/latest/queries/postgres/multiple-queries/#run-multiple-top-level-queries-in-the-same-request)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)