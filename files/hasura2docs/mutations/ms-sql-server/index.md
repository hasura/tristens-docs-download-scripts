# MS SQL Server: GraphQL Mutations

## Introduction​

GraphQL mutations are used to modify data on the server (i.e. write, update or delete data).

Hasura GraphQL Engine auto-generates mutations as part of the GraphQL schema from your MS SQL Server schema model.

Data of all tables in the database tracked by the GraphQL Engine can be modified over the GraphQL endpoint. If you have
a tracked table in your database, its insert/update/delete mutation fields are added as nested fields under the `mutation_root` root level type.

## Types of mutation requests​

The following types of mutation requests are possible:

- [ Insert ](https://hasura.io/docs/latest/mutations/ms-sql-server/insert/)
- [ Upsert ](https://hasura.io/docs/latest/mutations/ms-sql-server/upsert/)
- [ Update ](https://hasura.io/docs/latest/mutations/ms-sql-server/update/)
- [ Delete ](https://hasura.io/docs/latest/mutations/ms-sql-server/delete/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/mutations/ms-sql-server/index/#introduction)
- [ Types of mutation requests ](https://hasura.io/docs/latest/mutations/ms-sql-server/index/#types-of-mutation-requests)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)