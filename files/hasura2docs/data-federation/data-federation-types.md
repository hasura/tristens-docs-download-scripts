# Data Federation Types

Hasura GraphQL Engine supports the following remote relationships across your various data sources:

## Database to database relationships​

To join data across tables between two different database sources, such as order information stored in a Postgres
database, and user information stored in a separate Postgres or say a SQL Server database.

See[ Database to database relationships ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-source-relationships/).

## Database to Remote Schema relationships​

To join data across tables and remote GraphQL APIs. For example, you can join customer data from your tables with
account data from Stripe, Spotify, or Auth0 via their GraphQL APIs.

See[ Database to Remote Schema relationships ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/).

## Remote Schema to database relationships​

To join data from remote GraphQL schemas to database tables. For example connecting account data from Stripe, Spotify or
Auth0 GraphQL APIs to customer data in your tables.

See[ Remote Schema to database relationships ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-db-relationships/).

## Remote Schema to Remote Schema relationships (a.k.a GraphQL joins)​

To join data between two remote GraphQL schemas. For example connecting customer data from your custom GraphQL API to
account data from Stripe, Spotify or Auth0 GraphQL APIs.

See[ Remote Schema to Remote Schema relationships (a.k.a GraphQL joins) ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-relationships/).

## Action to database relationships​

To join data across tables and Actions (i.e. Rest APIs). For example, you can join user data from your database with
the response from a `createUser` action.

See[ Action to database relationships ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/action-relationships/).

### What did you think of this doc?

- [ Database to database relationships ](https://hasura.io/docs/latest/data-federation/data-federation-types/#database-to-database-relationships)
- [ Database to Remote Schema relationships ](https://hasura.io/docs/latest/data-federation/data-federation-types/#database-to-remote-schema-relationships)
- [ Remote Schema to database relationships ](https://hasura.io/docs/latest/data-federation/data-federation-types/#remote-schema-to-database-relationships)
- [ Remote Schema to Remote Schema relationships (a.k.a GraphQL joins) ](https://hasura.io/docs/latest/data-federation/data-federation-types/#remote-schema-to-remote-schema-relationships-aka-graphql-joins)
- [ Action to database relationships ](https://hasura.io/docs/latest/data-federation/data-federation-types/#action-to-database-relationships)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)