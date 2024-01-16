# API Reference | General Info

## Available APIs​

| API | Endpoint | Access |
|---|---|---|
| GraphQL | [ /v1/graphql ](https://hasura.io/docs/latest/api-reference/general-info/#graphql-api) | Permission rules |
| Relay | [ /v1beta1/relay ](https://hasura.io/docs/latest/api-reference/general-info/#relay-api) | Permission rules |
| Legacy GraphQL | [ /v1alpha1/graphql ](https://hasura.io/docs/latest/api-reference/general-info/#graphql-api) | Permission rules |
| Schema *(> v2.0)*  | [ /v2/query ](https://hasura.io/docs/latest/api-reference/general-info/#schema-api) | Admin only |
| Metadata *(> v2.0)*  | [ /v1/metadata ](https://hasura.io/docs/latest/api-reference/general-info/#metadata-api) | Admin only |
| Schema/Metadata *(deprecated)*  | [ /v1/query ](https://hasura.io/docs/latest/api-reference/general-info/#schema-metadata-api) | Admin only |
| Restified GQL | [ /api/rest ](https://hasura.io/docs/latest/api-reference/general-info/#restified-graphql-api) | GQL REST Routes |
| Version | [ /v1/version ](https://hasura.io/docs/latest/api-reference/general-info/#version-api) | Public |
| Health | [ /healthz ](https://hasura.io/docs/latest/api-reference/general-info/#health-check-api) | Public |
| PG Dump | [ /v1alpha1/pg_dump ](https://hasura.io/docs/latest/api-reference/general-info/#pg-dump-api) | Admin only |
| Config | [ /v1alpha1/config ](https://hasura.io/docs/latest/api-reference/general-info/#config-api) | Admin only |
| Explain | [ /v1/graphql/explain ](https://hasura.io/docs/latest/api-reference/general-info/#explain-api) | Admin only |


### GraphQL API​

All GraphQL requests for queries, subscriptions and mutations are made to the GraphQL API.

See details at[ GraphQL API Reference ](https://hasura.io/docs/latest/api-reference/graphql-api/index/).

### Relay API​

Hasura exposes a Relay schema for GraphQL requests for queries, subscriptions and mutations.

See docs at[ Postgres: Relay schema ](https://hasura.io/docs/latest/schema/postgres/relay-schema/).

See details at[ Relay GraphQL API Reference ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/index/).

### Schema API​

Hasura exposes a schema API for directly executing SQL on the underlying Postgres.

This is primarily intended to be used as an `admin` API to manage the Hasura schema.

See details at[ Schema API Reference ](https://hasura.io/docs/latest/api-reference/schema-api/index/).

### Metadata API​

Hasura exposes a Metadata API for managing metadata.

This is primarily intended to be used as an `admin` API to manage the Hasura Metadata.

See details at[ Metadata API Reference ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

### Schema / Metadata API (Deprecated)​

Hasura exposes a schema / Metadata API for managing Metadata for permissions/relationships or for directly executing SQL
on the underlying Postgres.

This is primarily intended to be used as an `admin` API to manage the Hasura schema and metadata.

See details at[ Schema / Metadata API Reference (Deprecated) ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

### RESTified GraphQL API​

Hasura allows saved GraphQL queries and mutations to be accessed through a REST interface.

See details at[ RESTified GraphQL Endpoints API Reference ](https://hasura.io/docs/latest/api-reference/restified/).

### Version API​

The `/v1/version` is a public endpoint that responds with the current server version in JSON format.

See details at[ Version API Reference ](https://hasura.io/docs/latest/api-reference/version/).

### Health Check API​

The `/healthz` is a public endpoint that returns the server health status. There's also `/hasura/healthz` available as
an alternative, which mirrors `/healthz` completely.

See details at[ Health Check API Reference ](https://hasura.io/docs/latest/api-reference/health/).

### pg_dump API​

The `/v1alpha1/pg_dump` is an admin-only endpoint that can be used to execute `pg_dump` on the Postgres instance
connected to Hasura. The `pg_dump` CLI tool's argument can be passed as a POST request body to the API and the response
is sent back to the client.

See details at[ PG Dump API Reference ](https://hasura.io/docs/latest/api-reference/pgdump/).

### Config API​

 `v1alpha1/config` is an admin-only endpoint to get the current server configuration.

See details at[ Config API Reference ](https://hasura.io/docs/latest/api-reference/config/).

### Explain API​

 `v1/graphql/explain` returns the Postgres plan for a query or subscription based on the defined permissions.

See details at[ Explain API Reference ](https://hasura.io/docs/latest/api-reference/explain/).

### What did you think of this doc?

- [ Available APIs ](https://hasura.io/docs/latest/api-reference/general-info/#available-apis)
    - [ GraphQL API ](https://hasura.io/docs/latest/api-reference/general-info/#graphql-api)

- [ Relay API ](https://hasura.io/docs/latest/api-reference/general-info/#relay-api)

- [ Schema API ](https://hasura.io/docs/latest/api-reference/general-info/#schema-api)

- [ Metadata API ](https://hasura.io/docs/latest/api-reference/general-info/#metadata-api)

- [ Schema / Metadata API (Deprecated) ](https://hasura.io/docs/latest/api-reference/general-info/#schema-metadata-api)

- [ RESTified GraphQL API ](https://hasura.io/docs/latest/api-reference/general-info/#restified-graphql-api)

- [ Version API ](https://hasura.io/docs/latest/api-reference/general-info/#version-api)

- [ Health Check API ](https://hasura.io/docs/latest/api-reference/general-info/#health-check-api)

- [ pg_dump API ](https://hasura.io/docs/latest/api-reference/general-info/#pg-dump-api)

- [ Config API ](https://hasura.io/docs/latest/api-reference/general-info/#config-api)

- [ Explain API ](https://hasura.io/docs/latest/api-reference/general-info/#explain-api)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)