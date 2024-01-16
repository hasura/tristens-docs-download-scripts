# Auto-Apply Migrations/Metadata when the Server Starts (config v2)

## cli-migrations image​

Hasura ships a special Docker image which can be used to automatically
apply Migrations/Metadata when the server starts:

`hasura/graphql-engine: < version > .cli-migrations-v2`

This container image includes the Hasura CLI at `/bin/hasura-cli` and
can be used for running any other CI/CD scripts in your workflow.

Note

For `config v3` , see[ Auto-apply Migrations/Metadata when the server starts ](https://hasura.io/docs/latest/migrations-metadata-seeds/auto-apply-migrations/).

## Applying Migrations​

The `migrations` and `metadata` directories created by the Hasura CLI in
a Hasura Project can be mounted at the `/hasura-migrations` and `/hasura-metadata` path of this Docker container and the container's
entry point script will apply the Migrations and Metadata before
starting the server. If no directory is mounted at the designated paths,
the server will start ignoring the Migrations and/or metadata.

If you want to mount the Migrations/Metadata directories at some
location other than the above, set the following environment variables:

```
HASURA_GRAPHQL_MIGRATIONS_DIR = /custom-path-for-migrations
HASURA_GRAPHQL_METADATA_DIR = /custom-path-for-metadata
```

Once the Migrations and Metadata are applied, the container resumes
operation as a normal Hasura GraphQL Engine server.

Example:

```
# Start Hasura after applying the Migrations and Metadata present in the Hasura Project
docker  run -p  8080 :8080  \
       -v /home/me/my-project/migrations:/hasura-migrations  \
       -v /home/me/my-project/metadata:/hasura-metadata  \
       -e  HASURA_GRAPHQL_DATABASE_URL = postgres://postgres:@postgres:5432/postgres  \
       hasura/graphql-engine:v1.2.0.cli-migrations-v2
```

## Applying only Metadata​

If you're managing Migrations with a different tool and want to use this
image to apply only the metadata, mount the `metadata` directory of your
Hasura Project at the `/hasura-metadata` path of this Docker container
the container’s entry point script will apply the Metadata before
starting the server.

### What did you think of this doc?

- [ cli-migrations image ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/auto-apply-migrations/#cli-migrations-image)
- [ Applying Migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/auto-apply-migrations/#applying-migrations)
- [ Applying only Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/auto-apply-migrations/#auto-apply-metadata-v2)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)