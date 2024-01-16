# Hasura - Citus Compatibility

## Introduction​

As Citus is an extension of Postgres, the way it functions with Hasura
is also very similar. Currently the following features are supported
with Citus and Hasura:

## Tables​

Querying from all kinds of tables and views is currently supported. This
includes local, reference and distributed tables. All the tables can be
tracked from the Console.

## Relationships​

The following table describes the supported relationships based on the
supported joins in Citus:

|  | To Local | To Reference | To Distributed |
|---|---|---|---|
|  **From Local**  | Object, Array | Object, Array |  |
|  **From Reference**  | Object, Array | Object, Array |  |
|  **From Distributed**  |  | Object | Object, Array |


The Hasura Console allows you to add all the supported relationships.

## Permissions​

All permissions work like on Postgres without any restrictions.

## Functions​

Citus supported `plpgsql` functions are supported on Hasura with the
following restrictions:

- Fetching relationships as part of the function’s response is
currently not supported


## Mutations​

Mutations are supported in GraphQL Engine with the following
restrictions:

- Fetching relationship data as part of `returning` is not yet
supported


## Subscriptions​

Live Queries and Streaming Subscriptions are supported with Citus.

## Event Triggers​

Citus does not yet support creating triggers ([ See issue ](https://github.com/citusdata/citus/issues/4425)) on reference
tables. Hence this is currently not supported.

## Computed fields​

Computed fields are currently supported on Postgres and BigQuery only.[ Raise a GitHub issue ](https://github.com/hasura/graphql-engine/issues/new?assignees=&labels=k%2Fenhancement&template=02_feature_request.md)to request support for computed fields on Citus sources.

## Naming conventions​

Naming conventions are currently only implemented as an experimental feature on Postgres sources.[ See docs ](https://hasura.io/docs/latest/schema/postgres/naming-convention/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers/#introduction)
- [ Tables ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers/#tables)
- [ Relationships ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers/#relationships)
- [ Permissions ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers/#permissions)
- [ Functions ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers/#functions)
- [ Mutations ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers/#mutations)
- [ Subscriptions ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers/#subscriptions)
- [ Event Triggers ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers/#event-triggers)
- [ Computed fields ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers/#computed-fields)
- [ Naming conventions ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/hasura-citus-compatibility/#event-triggers/#naming-conventions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)