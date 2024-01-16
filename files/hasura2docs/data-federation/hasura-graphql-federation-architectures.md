# Hasura GraphQL Federation Architectures

## Introduction​

In GraphQL, a supergraph is a unified and coherent schema that combines multiple sub-graphs, each representing a
distinct part of the overall data model. The distinctions between supergraphs and a sub-graphs is largely academic and
depends on the boundaries between one or more data sources.

Image: [ Data Federation Layer ](https://hasura.io/docs/assets/images/data-federation_federation-layer-0b5e5a49fd9ad54553efc893aeb97a64.png)

For example:

 ** For an individual team ** A supergraph federates a set of databases and existing GraphQL or REST APIs all owned and
managed by the team.

 ** For an organization or Business unit ** a supergraph federates a set of APIs or other sources (including sub-graphs
like the one above) which are owned and managed by individual teams.

There are four common federation patterns with Hasura which are described in the below sections:

1. Hasura multi-protocol data federation
2. Hasura as a GraphQL gateway to REST services or microservices.
3. Hasura as a federated supergraph gateway
4. Hasura as a sub-graph


## Hasura Multi-Protocol Data Federation​

Hasura works with data from multiple protocols or sources like databases of from differing providers, REST and GraphQL
APIs. Hasura enables federating data across these disparate sources by creating relationships between types agnostic of
their source:

| Source | Database | Existing REST API | Existing GraphQL API |
|---|---|---|---|
|  **Database**  | [ DB to DB relationships ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-source-relationships/) | [ Action relationships ](https://hasura.io/docs/latest/actions/action-relationships/) | [ Database to Remote Schema Relationships ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/) |
|  **Existing REST API**  | [ Action relationships ](https://hasura.io/docs/latest/actions/action-relationships/) | [ Action to Actions relationships ](https://hasura.io/docs/latest/actions/action-relationships/#action-to-action-relationships) | ❌ |
|  **Existing GraphQL API**  | [ Database to Remote Schema Relationships ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/) | ❌ | [ Remote schema to Remote schema relationships ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-relationships/) |


Image: [ Multi-protocol federation with Hasura ](https://hasura.io/docs/assets/images/data-federation_multi-protocol-federation-e3a26f952b7007fc788ad16dabe0f295.png)

### When to use this architecture​

#### Technical standpoint​

- Your team has access to all the sources (databases, REST and GraphQL APIs) and you want to federate these sources into
a unified graph.
- High performance joins across databases are required.


#### Ownership standpoint​

- Your team has access to all the sources (databases, REST and GraphQL APIs) and you want to federate these sources into
a unified graph.


### Comparison to alternatives​

#### GraphQL stitching​

Server-side GraphQL schema stitching requires that your sub-graphs are GraphQL APIs. With Hasura, you can federate
existing REST and GraphQL APIs without adding any middleware.

#### Apollo federation​

Hasura is multi-protocol and doesn't require a custom GraphQL specification as standard GraphQL is acceptable. No
resolvers are needed in Hasura for graph evolution. Hasura also provides API management such as authentication,
authorization, caching, etc.

## Hasura as a GraphQL gateway to REST services or microservices​

Hasura allows you to expose existing REST APIs behind a single GraphQL API by declaratively adding these REST APIs as
Actions in Hasura without any middleware by leveraging request/response transforms. Additionally, you can also create
relationships across types from different REST APIs.

This architecture pattern allows you the flexibility to rapidly evolve this graph by connecting Hasura to the underlying
databases.

Image: [ REST API federation with Hasura ](https://hasura.io/docs/assets/images/data-federation_rest-api-federation-4d55d73af0e8c46f84e38b0ea7b77cfc.png)

### When to use this architecture​

#### Technical standpoint​

- You want to expose a GraphQL API to consumers while leveraging existing REST APIs and/or microservices.
- To accelerate development on this API by connecting Hasura to any underlying databases, the database(s) must be one of
those supported by Hasura like Postgres, SQL Server, MySQL, Oracle, etc.
- You want to query data from multiple REST APIs in a single request from a client application.


#### Ownership standpoint​

- Your team may or may not own or manage the underlying REST APIs but are allowed to consume or expose the APIs.


## Hasura as a federated supergraph gateway​

Hasura can act as a centralized supergraph gateway to multiple multi-protocol (REST and GraphQL) sub-graphs that are
possibly owned and managed by other teams. This architecture allows you to centralize access to these sub-graphs by
providing a unified interface and managing authentication, authorization, caching, and more, centrally.

Image: [ Multi-protocol federation capabilities ](https://hasura.io/docs/assets/images/data-federation_multi-protocol-federation-capabilities-fc0cc541e4b2bb21abd5662377121726.png)

### When to use this architecture​

#### Technical standpoint​

- You want to create a unified/centralized API over multiple sub-graphs owned/maintained by either your teams or other
teams.


#### Ownership standpoint​

- Your team may or may not own or manage the underlying REST APIs but are allowed to consume and expose the APIs.


## Hasura as a sub-graph​

Hasura generates a GraphQL spec compliant schema so Hasura’s API can be included as a sub-graph into any specification
compliant federation tools.

Hasura also works with some proprietary federation tools. Hasura GraphQL Engine supports the Apollo Federation v1 spec,
so you can add Hasura as a sub-graph in your Apollo federated gateway. You can also use Hasura generated table types in
your other sub-graphs by enabling tables for[ Apollo Federation ](https://hasura.io/docs/latest/data-federation/apollo-federation/)explicitly.

Image: [ Third-party federation with Hasura ](https://hasura.io/docs/assets/images/data-federation_third-party-federation-layer-88c4a3105b9c9217a2246560d84449ae.png)

### When to use this architecture​

#### Technical standpoint​

- You have a Hasura-based GraphQL API and you need to make this API part of a Federation layer.


#### Ownership standpoint​

- You own or manage the Hasura-based API and you or another team wants to include this API with others in a single
federated API.


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/data-federation/hasura-graphql-federation-architectures/#introduction)
- [ Hasura Multi-Protocol Data Federation ](https://hasura.io/docs/latest/data-federation/hasura-graphql-federation-architectures/#hasura-multi-protocol-data-federation)
    - [ When to use this architecture ](https://hasura.io/docs/latest/data-federation/hasura-graphql-federation-architectures/#when-to-use-this-architecture)

- [ Comparison to alternatives ](https://hasura.io/docs/latest/data-federation/hasura-graphql-federation-architectures/#comparison-to-alternatives)
- [ Hasura as a GraphQL gateway to REST services or microservices ](https://hasura.io/docs/latest/data-federation/hasura-graphql-federation-architectures/#hasura-as-a-graphql-gateway-to-rest-services-or-microservices)
    - [ When to use this architecture ](https://hasura.io/docs/latest/data-federation/hasura-graphql-federation-architectures/#when-to-use-this-architecture-1)
- [ Hasura as a federated supergraph gateway ](https://hasura.io/docs/latest/data-federation/hasura-graphql-federation-architectures/#hasura-as-a-federated-supergraph-gateway)
    - [ When to use this architecture ](https://hasura.io/docs/latest/data-federation/hasura-graphql-federation-architectures/#when-to-use-this-architecture-2)
- [ Hasura as a sub-graph ](https://hasura.io/docs/latest/data-federation/hasura-graphql-federation-architectures/#hasura-as-a-sub-graph)
    - [ When to use this architecture ](https://hasura.io/docs/latest/data-federation/hasura-graphql-federation-architectures/#when-to-use-this-architecture-3)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)