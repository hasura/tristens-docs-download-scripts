# GraphQL Engine Server Configuration

## Introduction​

You can customize the configuration of the Hasura GraphQL Engine using either server flags or environment variables.

See the[ Server config reference ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/)for the list of all available flags
and environment variables that can be configured.

## Setting server configurations​

### Using flags​

You can configure self-hosted Hasura GraphQL Engine instances by setting flags on the `graphql-engine` command and the `serve` sub-command.

#### The graphql-engine command​

`graphql-engine`

The `graphql-engine` command has a limited number of flags and environment variables; these pertain directly to the
databases used in your project.

Every `graphql-engine` command is structured as:

`$ graphql-engine  < server-flags >`

As an example, we can set the metadata database url for a project using a flag:

`$ graphql-engine --metadata-database-url  "postgres://<user>:<password>@<host>:<port>/<db-name>"`

#### The serve sub-command​

`serve`

The `serve` sub-command provides opportunities to further customize Hasura's configuration.

Building on the previous example, we can set the port by which Hasura is served by pairing the `serve` sub-command with
the `--port` flag and assigning a value:

`$ graphql-engine --metadata-database-url  "postgres://user:password@host:port/db-name"  serve --port  3000`

Note

The following options can be configured via flags *only* :

```
    --host                      Postgres server host
-p, --port                      Postgres server port
-u, --user                      Database user name
-p, --password                  Password of the user
-d, --dbname                    Database name to connect to
-o, --pg-connection-options     PostgreSQL connection options
```

All other flags can also be passed as environment variables.

### Using environment variables​

You can also use environment variables to configure the Hasura GraphQL Engine. As an example, if you're using[ Docker on a self-hosted instance ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/), you can set these values by modifying your `docker-compose.yaml` file used to run Hasura:

```
# docker-compose.yaml
version :   '3.6'
services :
   postgres :
     image :  postgres : 12
     restart :  always
     volumes :
       -  db_data : /var/lib/postgresql/data
     environment :
       POSTGRES_PASSWORD :  postgrespassword
   graphql-engine :
     image :  hasura/graphql - engine : v2.15.0
     ports :
       -   '8080:8080'
     depends_on :
       -   'postgres'
     restart :  always
     environment :
       ## postgres database to store Hasura metadata
       HASURA_GRAPHQL_METADATA_DATABASE_URL :  postgres : //postgres : postgrespassword@postgres : 5432/postgres
       ## this env var can be used to add the above postgres database to Hasura as a data source. this can be removed/updated based on your needs
       PG_DATABASE_URL :  postgres : //postgres : postgrespassword@postgres : 5432/postgres
       ## enable the console served by server
       HASURA_GRAPHQL_ENABLE_CONSOLE :   'true'   # set to "false" to disable console
       ## enable debugging mode. It is recommended to disable this in production
       HASURA_GRAPHQL_DEV_MODE :   'true'
       HASURA_GRAPHQL_ENABLED_LOG_TYPES :  startup ,  http - log ,  webhook - log ,  websocket - log ,  query - log
       ## uncomment next line to run console offline (i.e load console assets from server instead of CDN)
       # HASURA_GRAPHQL_CONSOLE_ASSETS_DIR: /srv/console-assets
       ## uncomment next line to set an admin secret
       # HASURA_GRAPHQL_ADMIN_SECRET: myadminsecretkey
volumes :
  db_data :
```

Alternatively, if you're using Hasura Cloud, you can set and add environment variables from a project's dashboard:

Image: [ Setting env vars from Cloud ](https://hasura.io/docs/assets/images/cloud-env-var-7defe5a1acbd91e5586371902bf4daba.png)

Flags vs. environment variables

When the equivalent flags for environment variables are used, the flags will take precedence.

Zero downtime environment variable updates

When adding or updating environment variables on[ Hasura Cloud ](https://hasura.io/docs/latest/hasura-cloud/overview/), you will not need to
restart your project and there will be no downtime.

## Use cases​

The following are a few configuration use cases:

- [ Add an admin secret ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#add-admin-secret)
- [ Using CLI commands with admin secret ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#cli-with-admin-secret)
- [ Configure CORS ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#configure-cors)
- [ Run console offline (i.e load console assets from server instead of CDN) ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#console-assets-on-server)
- [ Dev (debugging) mode ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#dev-mode)
- [ Add a metadata database ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#add-metadata-database)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/index/#the-serve-sub-command/#introduction)
- [ Setting server configurations ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/index/#the-serve-sub-command/#setting-server-configurations)
    - [ Using flags ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/index/#the-serve-sub-command/#using-flags)

- [ Using environment variables ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/index/#the-serve-sub-command/#using-environment-variables)
- [ Use cases ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/index/#the-serve-sub-command/#use-cases)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)