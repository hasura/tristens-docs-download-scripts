# Upgrading to Hasura Migrations config v2

## What has changed?​

In **config v1** , the PG schema Migrations and Hasura Metadata were both
handled using the same[ migration files ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v1/reference/migration-file-format/)which were in `yaml` format. In **config v2** , these are managed
separately in their own directories in the Hasura Project. Metadata is
managed in its separate[ metadata directory ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/)and PG
schema Migrations are managed via[ migration files ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/migration-file-format/)that are now in `SQL` format.

### Changes needed in existing workflows​

Due to the above mentioned changes, any workflows that involve applying
Migrations have an additional step of applying Metadata as well.

For example,

- any place where the `hasura migrate apply` command is used, it now
needs to be followed by a `hasura metadata apply` command.
- if the `cli-migrations` Docker image is used for[ auto applying migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/auto-apply-migrations/)at server start,
now you will have to use the `cli-migrations-v2` image and the `/metadata` directory will also have to be mounted along with the `/migrations` directory


## Upgrade steps​

### Step 1: Take a backup​

Make sure you take a backup of your Hasura Project before upgrading to `config v2` .

### Step 2: Upgrade to the latest CLI​

Config v2 is available since `v1.2.0` .

Run:

`hasura update-cli`

### Step 3: Upgrade Hasura Project to v2​

In your project directory, run:

`hasura scripts update-project-v2`

Your project directory and `config.yaml` should be updated to v2.

### What did you think of this doc?

- [ What has changed? ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/upgrade-v2/#what-has-changed)
    - [ Changes needed in existing workflows ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/upgrade-v2/#changes-needed-in-existing-workflows)
- [ Upgrade steps ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/upgrade-v2/#upgrade-steps)
    - [ Step 1: Take a backup ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/upgrade-v2/#step-1-take-a-backup)

- [ Step 2: Upgrade to the latest CLI ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/upgrade-v2/#step-2-upgrade-to-the-latest-cli)

- [ Step 3: Upgrade Hasura Project to v2 ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/upgrade-v2/#step-3-upgrade-hasura-project-to-v2)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)