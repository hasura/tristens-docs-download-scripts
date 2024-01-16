# Roll Back Applied Migrations (config v2)

## Introduction​

If there are any issues with changes made to the DB schema and Hasura
Metadata it is possible to roll back their state to a previous stable
version.

Note

For `config v3` , see[ Rolling back applied Migrations (config v3) ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations).

## Rolling back database schema​

Database schema rollbacks can be achieved via the `down` Migrations
generated every time a schema change is made.

Here are some example scenarios:

To roll back a particular migration version:

`hasura migrate apply --version  1550925483858  --type down`

To roll back the last 2 migration versions:

`hasura migrate apply --down  2`

Note

Rollbacks will only work if there are `down` Migrations defined for a
schema change.

e.g. The Console will not generate `down` Migrations for SQL statements
executed from the `SQL` tab.

## Rolling back Hasura Metadata​

As Hasura Metadata is managed via snapshots of the metadata, to roll
back Hasura Metadata to a particular state you need the metadata
snapshot at that point. This is typically achieved by marking stable
checkpoints of a project in version control via commits.

```
git  checkout  < stable-feature-commit >
hasura metadata apply
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/rolling-back-migrations/#introduction)
- [ Rolling back database schema ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/rolling-back-migrations/#rolling-back-database-schema)
- [ Rolling back Hasura Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/rolling-back-migrations/#rolling-back-hasura-metadata)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)