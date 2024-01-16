# Write Migrations Manually (config v2)

## Introduction​

While the Hasura Console can auto generate Migrations for every action,
sometimes you might want to write the Migrations yourself, by hand.
Using the Hasura CLI, you can bootstrap these migration files and write
the SQL for the Postgres schema.

Note

For `config v3` , see[ Writing Migrations manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations).

## Create migration manually​

1. Set up the migration files:This command will create up and down migration SQL files in the `migrations` directory.
2. Edit the file and add your migration actions. For the file format
and instructions on what actions can be added, refer to[ migration file format ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/migration-file-format/).
3. The corresponding Hasura Metadata changes, if any, can be made
directly in the appropriate Metadata file in the `/metadata` directory, refer to[ Metadata format ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/).
4. Apply the Migration and Metadata:


Set up the migration files:

`hasura migrate create  < name-of-migration >`

This command will create up and down migration SQL files in the `migrations` directory.

Edit the file and add your migration actions. For the file format
and instructions on what actions can be added, refer to[ migration file format ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/migration-file-format/).

The corresponding Hasura Metadata changes, if any, can be made
directly in the appropriate Metadata file in the `/metadata` directory, refer to[ Metadata format ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/).

Apply the Migration and Metadata:

```
hasura migrate apply
hasura metadata apply
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/writing-migrations-manually/#introduction)
- [ Create migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/writing-migrations-manually/#create-migration-manually)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)