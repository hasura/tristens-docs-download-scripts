# Server Config Examples

## Introduction​

The following are a few configuration use cases:

## Add an admin secret​

To add an admin secret to Hasura, pass the `--admin-secret` flag with a
secret generated by you.

Run server in this mode using following docker command:

```
docker  run -P -d hasura/graphql-engine:latest graphql-engine  \
           --database-url postgres://username:password@host:5432/dbname  \
             serve  \
             --admin-secret XXXXXXXXXXXXXXXX
```

Typically, you will also have a webhook for authentication:

```
docker  run -P -d hasura/graphql-engine:latest graphql-engine  \
           --database-url postgres://username:password@host:5432/dbname  \
             serve  \
             --admin-secret XXXXXXXXXXXXXXXX
             --auth-hook https://myauth.mywebsite.com/user/session-info
```

In addition to flags, the GraphQL Engine also accepts environment
variables.

In the above case, for adding an admin secret you will use the `HASURA_GRAPHQL_ADMIN_SECRET` and for the webhook, you will use the `HASURA_GRAPHQL_AUTH_HOOK` environment variables.

## Using CLI commands with admin secret​

When you start the GraphQL Engine with an admin secret key, CLI commands
will also need this admin secret to contact APIs. It can be set in `config.yaml` or as an environment variable or as a flag to the command.
For example, let's look at the case of the `console` command:

In the `my-project/config.yaml` file, set a new key `admin_secret` :

```
# config.yaml
endpoint :  https : //my - graphql - endpoint.com
admin_secret :  XXXXXXXXXXXXXXXX
```

The Console can now contact the GraphQL APIs with the specified admin
secret.

Note

If you're setting an `admin_secret` in `config.yaml` please make sure
you do not check this file into a public repository.

An alternate and safe way is to pass the admin secret value to the
command as an environment variable:

```
export   HASURA_GRAPHQL_ADMIN_SECRET = xxxxx
hasura console
# OR in a single line
HASURA_GRAPHQL_ADMIN_SECRET = xxxxx hasura console
```

You can also set the admin secret using a flag to the command:

`hasura console --admin-secret = XXXXXXXXXXXX`

Note

The order of precedence for admin secret and endpoint is as follows:

CLI flag > Environment variable > Config file

## Configure CORS​

By default, all CORS requests to the Hasura GraphQL Engine are allowed.
To run with more restrictive CORS settings, use the `--cors-domain` flag
or the `HASURA_GRAPHQL_CORS_DOMAIN` ENV variable. The default value is `*` , which means CORS headers are sent for all domains.

The scheme + host with optional wildcard + optional port have to be
mentioned.

Examples:

```
# Accepts from https://app.foo.bar.com , https://api.foo.bar.com etc.
HASURA_GRAPHQL_CORS_DOMAIN = "https://*.foo.bar.com"
# Accepts from https://app.foo.bar.com:8080 , http://api.foo.bar.com:8080,
# http://app.localhost, http://api.localhost, http://localhost:3000,
# http://example.com etc.
HASURA_GRAPHQL_CORS_DOMAIN = "https://*.foo.bar.com:8080, http://*.localhost, http://localhost:3000, http://example.com"
# Accepts from all domain
HASURA_GRAPHQL_CORS_DOMAIN = "*"
# Accepts only from http://example.com
HASURA_GRAPHQL_CORS_DOMAIN = "http://example.com"
```

Note

Top-level domains are not considered as part of wildcard domains. You
have to add them separately. E.g. `https://*.foo.com` doesn't include `https://foo.com` .

You can tell Hasura to disable handling CORS entirely via the `--disable-cors` flag or the `HASURA_GRAPHQL_DISABLE_CORS` [ environment variable ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#disable-cors).
Hasura will not respond with CORS headers. You can use this
option if you're already handling CORS on a reverse proxy etc.

## Run the Console offline (i.e load console assets from server instead of CDN)​

Normally the static assets (js, css, fonts, img etc.) required by the
console are loaded from a CDN. Starting with `v1.0.0-beta.1` , these
assets are bundled with the Docker image published by Hasura. These
files can be found at `/srv/console-assets` .

If you're working in an environment with Hasura running locally and have
no access to internet, you can configure the GraphQL Engine to load
assets from the Docker image itself, instead of the CDN.

Set the following env var or flag on the server:

```
# env var
HASURA_GRAPHQL_CONSOLE_ASSETS_DIR = /srv/console-assets
# flag
--console-assets-dir = /srv/console-assets
```

Once the flag is set, all files in the `/srv/console-assets` directory
of the Docker image will be served at the `/console/assets` endpoint on
the server with the right content-type headers.

Note

Hasura follows a rolling update pattern for Console releases where
assets for a `major.minor` version is updated continuously across all
patches. If you're using the assets on the server with a Docker image,
it might not be the latest version of the Console.

## Dev (debugging) mode​

The Hasura GraphQL Engine may provide additional information for each
object in the `extensions` key of `errors` . The `internal` key contains
error information including the generated SQL statement, exception
information from Postgres and, if applicable, resolved[ connection template ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template)information. This can be highly useful, especially in the case of
debugging errors in[ Action ](https://hasura.io/docs/latest/actions/debugging/)requests.

By default the `internal` key is not sent in the `extensions` response
(except for `admin` roles). To enable this, start the GraphQL Engine
server in debugging mode with the following configuration:

```
# env var
HASURA_GRAPHQL_DEV_MODE = true
# flag
--dev-mode
```

The `internal` key is sent for `admin` role requests by default. To
disable them, configure as follows:

```
# env var
HASURA_GRAPHQL_ADMIN_INTERNAL_ERRORS = false
# flag
--admin-internal-errors  false
```

Note

It is highly recommended to enable debugging only for the `admin` role
in production.

## Add a Metadata database​

The Hasura GraphQL Engine when initialized, creates a schema called `hdb_catalog` in the Postgres database and initializes a few tables
under it. This schema and the internal tables are generally termed as
the `metadata catalogue` and is responsible to manage the internal state
of the Hasura GraphQL Engine.

By default, the `metadata_catalogue` is created inside the primary
database provided by the user. But sometimes it might be more
advantageous to segregate the primary database and the metadata
database.

Hasura GraphQL Engine provides a way to the users to provide an entirely
separate database to store the `metadata catalogue` .

To add a Metadata database, set the following environment variable or
add the flag to the server executable

```
# env var
HASURA_GRAPHQL_METADATA_DATABASE_URL = postgres:// < user > : < password > @ < host > : < port > / < metadata-db-name >
# flag
--metadata-database-url = postgres:// < user > : < password > @ < host > : < port > / < metadata-db-name >
```

Caveat for Hasura Cloud

The Metadata for Hasura Cloud projects is stored in dedicated metadata
DBs managed by Hasura Cloud. Hence the `HASURA_GRAPHQL_METADATA_DATABASE_URL` cannot be configured on Hasura
Cloud as its value is controlled by Hasura Cloud itself.

### Possible configurations:​

 **1. Both the**  `primary database`  **and**  `metadata database`  **are
provided to the server** 

```
# env var
HASURA_GRAPHQL_METADATA_DATABASE_URL = postgres:// < user > : < password > @ < host > : < port > / < metadata-db-name >
HASURA_GRAPHQL_DATABASE_URL = postgres:// < user > : < password > @ < host > : < port > / < db-name >
# flag
--metadata-database-url = postgres:// < user > : < password > @ < host > : < port > / < metadata-db-name >
--database-url = postgres:// < user > : < password > @ < host > : < port > / < db-name >
```

In this case, Hasura GraphQL Engine will use the `HASURA_GRAPHQL_METADATA_DATABASE_URL` to store the `metadata catalogue` and starts the server with the database provided in the `HASURA_GRAPHQL_DATABASE_URL` .

 **2. Only**  `metadata database`  **is provided to the server** 

```
# env var
HASURA_GRAPHQL_METADATA_DATABASE_URL = postgres:// < user > : < password > @ < host > : < port > / < metadata-db-name >
# flag
--metadata-database-url = postgres:// < user > : < password > @ < host > : < port > / < metadata-db-name >
```

In this case, Hasura GraphQL Engine will use the `HASURA_GRAPHQL_METADATA_DATABASE_URL` to store the `metadata catalogue` and starts the server without tracking/managing any database. *i.e* a
Hasura GraphQL server will be started with no database. The user could
then manually track/manage databases at a later time.

 **3. Only**  `primary database`  **is provided to the server** 

```
# env var
HASURA_GRAPHQL_DATABASE_URL = postgres:// < user > : < password > @ < host > : < port > / < db-name >
# flag
--database-url = postgres:// < user > : < password > @ < host > : < port > / < db-name >
```

In this case, Hasura GraphQL Engine server will start with the database
provided in the `HASURA_GRAPHQL_DATABASE_URL` and will also use the *same database* to store the `metadata catalogue` .

 **4. Neither**  `primary database`  **nor**  `metadata database`  **is
provided to the server** 

Hasura GraphQL Engine will fail to startup and will throw an error

`Fatal Error: Either of --metadata-database-url or --database-url option expected`

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#add-metadata-database/#introduction)
- [ Add an admin secret ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#add-metadata-database/#add-admin-secret)
- [ Using CLI commands with admin secret ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#add-metadata-database/#cli-with-admin-secret)
- [ Configure CORS ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#add-metadata-database/#configure-cors)
- [ Run the Console offline (i.e load console assets from server instead of CDN) ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#add-metadata-database/#console-assets-on-server)
- [ Dev (debugging) mode ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#add-metadata-database/#dev-mode)
- [ Add a Metadata database ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#add-metadata-database/#add-metadata-database)
    - [ Possible configurations: ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#add-metadata-database/#possible-configurations)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)