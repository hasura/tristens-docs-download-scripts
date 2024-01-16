# Metadata Catalogue

## What is the Metadata catalogue?​

The Hasura Metadata catalogue is a set of internal tables used to manage the state of the database and the GraphQL schema.
Hasura GraphQL Engine uses the data in the catalogue to generate the GraphQL API which then can be accessed from different clients.

The Hasura GraphQL Engine stores this catalogue in a Postgres Metadata database *(which is by default the same database from which data is served over the GraphQL API if it is Postgres)* .
When initialized, the Hasura GraphQL Engine creates a schema called `hdb_catalog` in the Metadata database and initializes a few tables under it as described below.

## hdb_catalog schema​

This schema is created by the Hasura GraphQL Engine to manage its internal state. Whenever a table/permission/relationship is created/updated using the Hasura Console or the Metadata API, the Hasura GraphQL Engine captures that information and stores it in the corresponding tables.

## Exploring the catalogue​

You can check the current schema and contents of the catalogue by exploring the `hdb_catalog` schema in the Metadata database through a Postgres client.

Hasura Cloud

The Metadata for Hasura Cloud projects is stored in dedicated databases managed by Hasura Cloud itself,
hence the Metadata catalogue will not be set up on the user's connected database(s). *(Though note that if any Event Triggers are defined on a database, then their invocation logs will be stored in the "hdb_catalog" schema of that database).* 

## Catalogue versioning​

Whenever the schema of the catalogue is modified *(typically to support new features)* a new version of the catalogue is generated.

The catalogue version is upgraded automatically on startup if a new version is available during Hasura GraphQL Engine updates.

### What did you think of this doc?

- [ What is the Metadata catalogue? ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v1/reference/metadata-schema/#what-is-the-metadata-catalogue)
- [ hdb_catalog schema ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v1/reference/metadata-schema/#hdb_catalog-schema)
- [ Exploring the catalogue ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v1/reference/metadata-schema/#exploring-the-catalogue)
- [ Catalogue versioning ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v1/reference/metadata-schema/#catalogue-versioning)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)