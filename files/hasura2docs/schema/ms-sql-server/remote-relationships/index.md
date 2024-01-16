# MS SQL Server: Remote Relationships

## Introduction​

Remote relationships (aka "remote joins") allow you to join data across tables and remote data sources. The remote data
source can either be a[ Remote Schema ](https://hasura.io/docs/latest/remote-schemas/overview/)or a table from a second database source. Once you
create relationships between types from your database tables and types created from Remote Schemas, you can then "join"
them by running GraphQL queries.

See the following guides on how to create different types of remote relationships related to MS SQL Server:

- [ Database to database relationships ](https://hasura.io/docs/latest/schema/ms-sql-server/remote-relationships/remote-source-relationships/): To
join data across tables between two different database sources, such as order information stored in a SQL Server
database, and user information stored in a separate SQL Server or say a Postgres database.
- [ Database to Remote Schema relationships ](https://hasura.io/docs/latest/schema/ms-sql-server/remote-relationships/remote-schema-relationships/):
To join data across tables and remote GraphQL APIs. For example, you can join customer data from your tables with
account data from Stripe, Spotify, or Auth0.
- [ Remote Schema to database relationships ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-db-relationships/): To
join data from your Remote Schemas (such as Stripe, Spotify or Auth0) to customer data from your tables.


## Benefits​

Hasura's remote joins architecture provides the following benefits.

- **Security** : Hasura's[ authorization model ](https://hasura.io/docs/latest/auth/authorization/index/)gives you role-based access control. This
extends to Remote Schemas as well. Hasura will[ forward your session variables ](https://hasura.io/docs/latest/remote-schemas/auth/index/)which
can be used to implement custom authorization in your Remote Schemas. Native role-based permissions on Remote Schemas
is in the works.
- **Performance** : Hasura strives for optimal performance. It creates an efficient execution plan which pushes down most
of the heavy-lifting involved to underlying sources. For example, Hasura creates a single efficient query to your
database and batches calls to Remote Schemas to avoid the[ n+1 problem ](https://hasura.io/learn/graphql/intro-graphql/graphql-server/). More improvements to performance are
upcoming.
- **Schema integrity & consistency** : Hasura has Metadata consistency checks at every level. Whenever you add a table or
Remote Schema, Hasura makes sure that the graph that is exposed is consistent, and that all the relationships make
sense at a type level. This helps you in creating robust workflows to test changes in your CI and making safe
deployments of your unified graph.
- **Data federation** : With remote joins, the join, authorization, and consistency checks of added sources all happen at
the Hasura layer via metadata. This allows underlying data sources and APIs to evolve independently. Your applications
have a unified API to query the full data landscape in your org.


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/ms-sql-server/remote-relationships/index/#introduction)
- [ Benefits ](https://hasura.io/docs/latest/schema/ms-sql-server/remote-relationships/index/#benefits)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)