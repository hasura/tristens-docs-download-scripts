# Auto-Apply Migrations and Metadata

## Introduction​

Hasura ships a special `cli-migrations` Docker image which can be used to automatically apply Migrations and Metadata
when the server starts.

### What does it mean to "auto-apply" Migrations and Metadata?​

Auto-applying migrations means that Hasura can automatically apply database schema changes or migrations to your
underlying database without requiring manual intervention. This feature simplifies the process of keeping your database
schema in sync with your GraphQL schema and makes it easier to evolve your application over time.

### How does it work?​

This image is a drop-in place replacement for the standard Hasura GraphQL Engine[ images ](https://hub.docker.com/r/hasura/graphql-engine). This container provides a method to apply[ Migrations and Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/overview/)automatically when the container starts up. It works
by:

- Starting a temporary server securely through `localhost` with the Migrations API allowed.
- The server will then apply the Metadata and Migrations[ mounted to the container automatically ](https://github.com/hasura/graphql-engine/tree/master/packaging/cli-migrations/v3#configuration).
- Finally, it will reboot in a secure mode for consumer GraphQL usage and begin serving GraphQL requests.


This image is intended to assist with automated deployments

We do not intend this to be used as an init container to deploy Metadata and Migrations before shutting down and running
a standard Hasura GraphQL Engine container.

You can use this image in your CI/CD workflows to automatically apply Migrations and Metadata to a Hasura GraphQL Engine
instance like this in a Dockerfile:

```
FROM hasura/graphql-engine: < version > .cli-migrations-v3
CMD graphql-engine  \
  --metadata-database-url  $METADATA_DATABASE_URL   \
  serve  \
  --server-port  $PORT   \
  --enable-console
```

You can find more information about configuring the `cli-migrations` image[ here ](https://github.com/hasura/graphql-engine/blob/master/packaging/cli-migrations/v3/README.md#metadata-directory-optional)and find the image on[ DockerHub for various platforms here ](https://hub.docker.com/r/hasura/graphql-engine/tags?page=1&name=cli-migrations-v3).

This container image also includes the Hasura CLI at `/bin/hasura-cli` and can be used for running any other CI/CD
scripts in your workflow too.

Note

For `config v2` , see[ Auto-apply Migrations/Metadata when the server starts (config v2) ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/auto-apply-migrations/).

## Applying Migrations​

The `migrations` and `metadata` directories created by the Hasura CLI in a Hasura Project can be mounted at the `/hasura-migrations` and `/hasura-metadata` [ paths of this Docker container and the container's entrypoint script ](https://github.com/hasura/graphql-engine/blob/master/packaging/cli-migrations/v3/docker-entrypoint.sh#L12C1-L13)will automatically apply the Migrations and Metadata before starting the server. If no directory is mounted at the
designated paths, the server will start and ignore the Migrations and/or Metadata.

You can also mount the Migrations/Metadata directories at some location other than the above by setting the following
environment variables:

```
HASURA_GRAPHQL_MIGRATIONS_DIR = /custom-path-for-migrations
HASURA_GRAPHQL_METADATA_DIR = /custom-path-for-metadata
```

Once the Migrations and Metadata are applied, the container resumes operation as a normal Hasura GraphQL Engine server.

Example:

```
# Start Hasura after applying the Migrations and Metadata present in the Hasura Project
docker  run -p  8080 :8080  \
       -v /home/me/my-project/migrations:/hasura-migrations  \
       -v /home/me/my-project/metadata:/hasura-metadata  \
       -e  HASURA_GRAPHQL_METADATA_DATABASE_URL = postgres://postgres:@postgres:5432/postgres  \
       hasura/graphql-engine: < version > .cli-migrations-v3
```

## Applying only Metadata​

If you're managing Migrations with a different tool and want to use this image to apply only the metadata, mount the `metadata` directory of your Hasura Project at the `/hasura-metadata` [ path of this Docker container the container's entry point script ](https://github.com/hasura/graphql-engine/blob/master/packaging/cli-migrations/v3/docker-entrypoint.sh#L13)will apply the Metadata before starting the server.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/migrations-metadata-seeds/auto-apply-migrations/#introduction)
    - [ What does it mean to "auto-apply" Migrations and Metadata? ](https://hasura.io/docs/latest/migrations-metadata-seeds/auto-apply-migrations/#what-does-it-mean-to-auto-apply-migrations-and-metadata)

- [ How does it work? ](https://hasura.io/docs/latest/migrations-metadata-seeds/auto-apply-migrations/#how-does-it-work)
- [ Applying Migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/auto-apply-migrations/#applying-migrations)
- [ Applying only Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/auto-apply-migrations/#auto-apply-metadata)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)