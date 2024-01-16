# Source Health Check

## Introduction​

Hasura enables users to check the health of connected data sources via the Health Check API.[ API reference here ](https://hasura.io/docs/latest/api-reference/source-health/).

## Configuring source Health Check​

A Health Check configuration contains information that Hasura uses to determine the health state of a source. You can
set the time interval for when Hasura will re-perform the check on the source.

Currently, Hasura supports enabling Health Checks on Postgres and MS SQL Server databases. Support for other data
sources will be added soon.

Health Check configurations for Postgres and SQL Server sources are identical and are as follows.

- Console
- CLI
- API


Console support will be added soon.

You can add *health check* for a source by adding the config to the `/metadata/databases/database.yaml` file:

```
-   name :  <db - name >
   kind :  postgres
   health_check :
     test :
       sql :  SELECT 1
     interval :   10
     retries :   3
     retry_interval :   5
     timeout :   5
   configuration :
     connection_info :
       database_url :
         from_env :  <DATABASE_URL_ENV >
       pool_settings :
         idle_timeout :   180
         max_connections :   50
         retries :   1
```

Apply the Metadata by running:

`hasura metadata apply`

You can add/update *health check* for a database using the[ pg_update_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#metadata-pg-update-source)Metadata API.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   {
     "type" :   "pg_update_source" ,
     "args" :   {
       "name" :   "default" ,
       "health_check" :   {
         "test" :   {
           "sql" :   "SELECT 1"
         } ,
         "interval" :   100 ,
         "timeout" :   2 ,
         "retries" :   3 ,
         "retry_interval" :   2
       }
     }
   }
}
```

## Reporting source Health Check​

### API​

Health Check reports of sources can be obtained through a `GET` request from the `/healthz/sources` API, on demand.
Learn more about the API[ here ](https://hasura.io/docs/latest/api-reference/source-health/).

### Logging​

Hasura logs the Health Check status and other information via `health-check-log` type when enabled. Learn more about the
Health Checks logs[ here ](https://hasura.io/docs/latest/deployment/logging/#health-check-log-structure).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/health-checks/source-health-check/#introduction)
- [ Configuring source Health Check ](https://hasura.io/docs/latest/deployment/health-checks/source-health-check/#configuring-source-health-check)
- [ Reporting source Health Check ](https://hasura.io/docs/latest/deployment/health-checks/source-health-check/#reporting-source-health-check)
    - [ API ](https://hasura.io/docs/latest/deployment/health-checks/source-health-check/#api)

- [ Logging ](https://hasura.io/docs/latest/deployment/health-checks/source-health-check/#logging)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)