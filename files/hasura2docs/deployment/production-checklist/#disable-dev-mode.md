# Production Checklist

## Introduction​

This guide is a checklist for configuring and securing GraphQL Engine for a production deployment.

Hasura Cloud the fastest way to production

Many of the following steps are pre-configured in a Hasura Cloud instance with integrated logging, API limits, caching
and more. For more information about our hosted Hasura product, see[ Hasura Cloud docs ](https://hasura.io/docs/latest/index/).

## Set an admin secret​

Set an admin secret to protect the API from unauthorized access. It is recommended to keep this as a long string.

```
# set env var
HASURA_GRAPHQL_ADMIN_SECRET = averylongpasswordstring
# or use the flag
graphql-engine --database-url = < database-url >  serve --admin-secret = averylongpasswordstring
```

More details can be found at[ Securing the GraphQL endpoint ](https://hasura.io/docs/latest/deployment/securing-graphql-endpoint/).

## Move secrets to environment variables​

It is recommended to move all secrets to environment variables. On Hasura Cloud, environment variables are stored in a[ Hashicorp Vault ](https://www.vaultproject.io/)instance as secrets which are not directly accessible to Hasura staff.
The Hasura Engine also does not store any copies of your data, except for[ cached query responses ](https://hasura.io/docs/latest/caching/overview/)which have a TTL expiry.

## Verify permissions​

- [ Review the summary ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#review-the-summary)
- [ Limit number of rows returned ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#limit-number-of-rows-returned)


### Review the summary​

Review the authorization/permission rules set on tables. You can make use of the "Schema permissions summary" page to
get a bird's eye view on all the permissions set across all tables and roles. Pay extra attention to roles like
"anonymous" which allow unauthenticated access.

Image: [ Hasura Console - Schema permissions summary ](https://hasura.io/docs/assets/images/schema_permissions_summary-84e8b631713e20e5a1d6b2a6b50dd5af.png)

### Limit number of rows returned​

You should[ limit the number of rows ](https://hasura.io/docs/latest/auth/authorization/permissions/row-fetch-limit/)that can be accessed in one
request, by setting the number in the select permission. This will prevent someone from accidentally or otherwise
querying the entire table in one shot, thus adding load on Postgres.

## Configure max connections​

Hasura utilizes[ connection pooling ](https://hasura.io/docs/latest/databases/database-config/cloud-connection-pooling/)for Postgres and MS SQL Server databases. You should set an appropriate[ total_max_connections ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgpoolsettings)(on Cloud) or[ max_connections ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgpoolsettings)(on Self-hosted) to use the database efficiently.

## Disable APIs​

Hasura exposes many APIs which might not be relevant for a production instance that is only supposed to serve GraphQL.
APIs can be selectively enabled using the corresponding flag or environment variable.

In most production scenarios, you would only need GraphQL API to be enabled.

```
# set this env var to enable only the graphql api
HASURA_GRAPHQL_ENABLED_APIS = graphql
# if you're using flags
graphql-engine --database-url = < database-url >  serve --enabled-apis = graphql
```

By setting the above flag or env var, we are disabling the `metadata` , `pgdump` and `config` APIs. `health` and `version` APIs are public and cannot be disabled.

Read more about all the API types at the[ API reference ](https://hasura.io/docs/latest/api-reference/overview/).

Note

If you're using `cli-migrations` image, prior to `v1.0.0-beta.8` , setting enabled APIs to only `graphql` can cause the
migration apply step to fail. Please update to the latest version if you're facing this issue.

## Disable the Console​

It is recommended that you disable the Console on production deployments to prevent accidental changes to your
production environment. Also, when you disable the Metadata API, Console will stop working.

The Console is disabled by default.

```
# set the env var to false or do not set it at all to disable the Console
HASURA_GRAPHQL_ENABLE_CONSOLE = false
# when using flags, no --enable-console flag implies the Console is disabled
graphql-engine --database-url = < database-url >  serve
```

Note

You can still use the CLI to open a Console connected to this instance. (Provided `metadata` APIs are not disabled).

## Disable dev mode​

It is recommended that you disable the[ dev mode ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#dev-mode)on
production deployments for non-admin roles to avoid leaking internal debugging information to the clients in case of API
errors.

The dev mode is disabled by default.

```
# set the env var to false or do not set it at all to disable dev mode
HASURA_GRAPHQL_DEV_MODE = false
# when using flags, no --dev-mode flag implies dev mode is disabled
graphql-engine --database-url = < database-url >  serve
```

## Set up an allow-list​

An allow-list can be set up to restrict what kind of requests can be made against this particular instance. If your API
is meant to serve a frontend client, you can only allow those requests used by the client to pass through. Every other
request will be rejected without even getting validated.

Read more at[ Allow-list of operations ](https://hasura.io/docs/latest/security/allow-list/).

## Restrict CORS domains​

By default, all cross-origin requests are allowed by Hasura GraphQL Engine. You should restrict them to the domains
which you trust.

```
# set the env var, accept cross-origin requests from https://my-ui.com
HASURA_GRAPHQL_CORS_DOMAIN = https://my-ui.com
# using flags
graphql-engine --database-url = < database-url >  server --cors-domain = "https://my-ui.com"
```

You can read more about this setting at[ Configure CORS ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#configure-cors).

## Enable HTTPS​

Production APIs should be served over HTTPS to be secure over the network.

See[ Enable HTTPS ](https://hasura.io/docs/latest/deployment/enable-https/)for details on achieving this.

## Configure a load balancer​

If you're setting up a load-balancer in front of Hasura, ensure that it's configured appropriately.

- Configure the load balancer health checks to use[ Hasura's health endpoint ](https://hasura.io/docs/latest/api-reference/health/).
- Idle timeout will depend on the `max time` you want to allow an operation to run in Hasura. It should be configured to
a slightly higher number than the maximum time set in Hasura's API Limits.
- Hasura doesn't require sticky sessions.
- The default load-balancing method is usually round-robin and this works well with Hasura. However, you may choose a
different vendor specific algorithm if you find benefits with those. For example, if you have implemented many
subscriptions in your app, the `Least Outstanding Requests` algorithm offered by AWS could be useful in certain
scenarios.


## Configure logging​

The[ logs guide ](https://hasura.io/docs/latest/deployment/logging/)describes different log types and log levels Hasura GraphQL Engine uses. You
can configure the GraphQL Engine to enable/disable certain log-types using the the `--enabled-log-types` flag or the `HASURA_GRAPHQL_ENABLED_LOG_TYPES` env var.

If you are collecting your logs using an agent and you're interested in capturing the request logs along with the SQL
that is generated, you should enable `query-log`  *(it is not enabled by default)* .

```
# enable all log types
HASURA_GRAPHQL_ENABLED_LOG_TYPES = startup,http-log,query-log,websocket-log,webhook-log
# using flags
graphql-engine --database-url = < database-url >
serve --enabled-log-types = "startup,http-log,query-log,websocket-log,webhook-log"
```

## Security Announcements​

Join the[ Hasura Security Announcements ](https://groups.google.com/forum/#!forum/hasura-security-announce)group for
emails about security announcements.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#introduction)
- [ Set an admin secret ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#set-an-admin-secret)
- [ Move secrets to environment variables ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#move-secrets-to-environment-variables)
- [ Verify permissions ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#verify-permissions)
    - [ Review the summary ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#review-the-summary)

- [ Limit number of rows returned ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#limit-number-of-rows-returned)
- [ Configure max connections ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#configure-max-connections)
- [ Disable APIs ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#disable-apis)
- [ Disable the Console ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#disable-the-console)
- [ Disable dev mode ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#disable-dev-mode)
- [ Set up an allow-list ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#set-up-an-allow-list)
- [ Restrict CORS domains ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#restrict-cors-domains)
- [ Enable HTTPS ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#enable-https)
- [ Configure a load balancer ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#configure-a-load-balancer)
- [ Configure logging ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#configure-logging)
- [ Security Announcements ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode/#security-announcements)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)