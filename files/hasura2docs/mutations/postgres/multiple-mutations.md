# Multiple Mutations in a Request

## Execution​

If multiple mutations are part of the same request, they are executed **sequentially** in a single **transaction** . If
any of the mutations fail, all the executed mutations will be rolled back.

Note

In requests where a[ Remote Schema ](https://hasura.io/docs/latest/remote-schemas/overview/)or[ Action ](https://hasura.io/docs/latest/actions/overview/)is present, and a
mutation fails, rollback is not possible. Any mutations executed before the failed mutation will still succeed.

## Run multiple top level mutations in the same request​

 **Example:** Delete all `article` objects written by an author and update the `author` object:

## Insert an object and a nested object in the same mutation​

If you are trying to insert multiple objects which have relationships between them, you can use nested inserts.

 **Example:** Insert a new `article` object with its `author` and return the inserted article object with its author in
the response:

### What did you think of this doc?

- [ Execution ](https://hasura.io/docs/latest/mutations/postgres/multiple-mutations/#execution)
- [ Run multiple top level mutations in the same request ](https://hasura.io/docs/latest/mutations/postgres/multiple-mutations/#run-multiple-top-level-mutations-in-the-same-request)
- [ Insert an object and a nested object in the same mutation ](https://hasura.io/docs/latest/mutations/postgres/multiple-mutations/#insert-an-object-and-a-nested-object-in-the-same-mutation)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)