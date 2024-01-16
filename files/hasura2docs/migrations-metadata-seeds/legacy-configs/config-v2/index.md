# Migrations & Metadata (config v2)

## Introduction​

It is a typical requirement to export an existing Hasura "setup" so that you can apply it on another instance to
reproduce the same setup. For example, to achieve a dev -> staging -> production environment promotion scenario.

Note

This documentation is for Hasura Migrations `config v2` . For `config v3` , see[ Migrations & Metadata (CI/CD) ](https://hasura.io/docs/latest/migrations-metadata-seeds/overview/).

## How is Hasura state managed?​

Hasura needs 2 pieces of information to recreate your GraphQL API, the underlying PG database schema and the Hasura
Metadata which is used to describe the exposed GraphQL API.

The[ Hasura CLI ](https://hasura.io/docs/latest/hasura-cli/overview/)lets you manage these pieces of information as you build your project via:

### Database migration files​

The state of your PG database is managed via incremental SQL migration files. These migration files can be applied one
after the other to achieve the final DB schema.

DB migration files can be generated incrementally and can by applied in parts to reach particular checkpoints. They can
be used to roll-back the DB schema as well.

Note

You can choose to manage database Migrations using external tools like knex, TypeORM, Django/Rails migrations, etc. as
well.

### Hasura Metadata files​

The state of Hasura Metadata is managed via snapshots of the metadata. These snapshots can be applied as a whole to
configure Hasura to a state represented in the snapshot.

Hasura Metadata can be exported and imported as a whole.

## Setting up Migrations​

See[ Setting up Hasura Migrations (config v2) ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/).

## Advanced use cases​

- [ Auto-apply Migrations/Metadata when the server starts (config v2) ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/auto-apply-migrations/)
- [ Writing Migrations manually (config v2) ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/writing-migrations-manually/)
- [ Rolling back applied Migrations (config v2) ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/rolling-back-migrations/)
- [ Creating a seed data migration (config v2) ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/seed-data-migration/)


## Reference documentation​

- [ How Hasura Migrations work (config v2) ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/how-it-works/)
- [ Migration file format ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/migration-file-format/)
- [ Metadata format ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/index/#introduction)
- [ How is Hasura state managed? ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/index/#how-is-hasura-state-managed)
    - [ Database migration files ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/index/#database-migration-files)

- [ Hasura Metadata files ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/index/#hasura-metadata-files)
- [ Setting up Migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/index/#setting-up-migrations)
- [ Advanced use cases ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/index/#advanced-use-cases)
- [ Reference documentation ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/index/#reference-documentation)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)