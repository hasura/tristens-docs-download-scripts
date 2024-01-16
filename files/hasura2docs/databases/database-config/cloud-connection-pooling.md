# Elastic Connection Pools

## Introduction​

In Hasura, you get automatic connection pools for your database connections. Apart from the general performance benefits
of using pooled connections, this also ensures that your database remains reliable even during periods of massive load.

Note

Connection pooling is only available for[ PostgreSQL ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgpoolsettings)and[ MSSQL ](https://hasura.io/docs/latest/api-reference/syntax-defs/#mssqlpoolsettings)data sources.

In Hasura Cloud, the connection pool is elastic i.e. shrinks and grows based on usage and also respects a configured max
limit. There are many other tunable parameters for the pool settings which can help you change the behavior of the pool
as required. Read more about these in the[ How connection pooling works ](https://hasura.io/docs/latest/databases/database-config/cloud-connection-pooling/#how-connection-pooling-works)section below.

### Get started​

Connection pooling is always turned on and the size of the pool can be specified via the `total_max_connections` setting. It is always recommended to set an appropriate `total_max_connections` pool setting based on your workload and
database constraints.

In self-hosted deployments

For projects not leveraging Hasura Cloud, the connection pool size can be specified via the `max_connections` setting.
This setting is applicable per server instance and hence the cumulative number of connections across all instances in a
project can be calculated as `number of server instances * max_connections` 

- Console
- CLI
- API


While adding a new database, under `Connection Settings` , set the desired `Total Max Connections` for primary and read
replica pools. To set or update `total_max_connections` for existing sources, head to the `Data > Databases > Manage > [database-name] > Edit` page and scroll down to the `Connection Settings` section.

Image: [ Total max connections ](https://hasura.io/docs/assets/images/total-max-connections-c1d2f57a10cf284222fd32526d3a5806.png)

To set `total_max_connections` , update the `databases > [source-name] > databases.yaml` file inside the metadata
directory as per this example:

```
-   name :  default
   kind :  postgres
   configuration :
     connection_info :
       use_prepared_statements :   false
       database_url :
         from_env :  PG_DATABASE_URL
       isolation_level :  read - committed
       pool_settings :
         total_max_connections :   60
   tables :   '!include default/tables/tables.yaml'
```

Apply the Metadata using the CLI by running:

`hasura metadata apply`

The `total_max_connections` pool setting can be set using the `<backend>_add_source` Metadata API,

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_add_source" ,
   "args" :   {
     "name" :   "pg1" ,
     "configuration" :   {
       "connection_info" :   {
         "database_url" :   {
            "from_env" :   "<DB_URL_ENV_VAR>"
          } ,
         "pool_settings" :   {
           "total_max_connections" :   50 ,
           "idle_timeout" :   180 ,
           "retries" :   1 ,
           "pool_timeout" :   360 ,
           "connection_lifetime" :   600
         } ,
         "use_prepared_statements" :   true ,
         "isolation_level" :   "read-committed" ,
       }
     } ,
     "replace_configuration" :   false
   }
}
```

or can be updated using the `<backend>_update_source` Metadata API.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_update_source" ,
   "args" :   {
     "name" :   "pg1" ,
     "configuration" :   {
       "connection_info" :   {
         "database_url" :   {
            "from_env" :   "<DB_URL_ENV_VAR>"
          } ,
         "pool_settings" :   {
           "total_max_connections" :   50 ,
           "idle_timeout" :   180 ,
           "retries" :   1 ,
           "pool_timeout" :   360 ,
           "connection_lifetime" :   600
         } ,
         "use_prepared_statements" :   true ,
         "isolation_level" :   "read-committed" ,
       }
     }
   }
}
```

## How connection pooling works​

A connection pool starts off empty and as new requests arrive, a connection to the database is established. This
connection stays warm in the pool to be reused by any other waiting request. This ensures that subsequent requests do
not have to reestablish a database connection hence saving time and resources.

After a certain period of connection idleness (specified by `idle_timeout` ) or connection lifetime (specified by `connection_lifetime` ), the connection is released from the pool. This ensures that Hasura is not holding connections
which are not required.

If the connection pool is saturated, then any new request waits for the pool to provide a connection. This ensures that
your database is not bombarded with more connections than it can handle. You can also specify a `pool_timeout` to
timeout any requests that are blocked on the connection pool.

Total max connections is best effort

During heavy load, the number of connections may slightly exceed the `total_max_connections` limit for a brief period of
time during which Hasura Cloud is trying to adjust pools in existing Hasura Server instances. Always set the `total_max_connections` value slightly lower than the database true total maximum limit in order to avoid exceeding your
resource limits.

total_max_connections and max_connections

`total_max_connections`

`max_connections`

If both `total_max_connections` and `max_connections` are set, then `total_max_connections` will take precedence over
the `max_connections` . If neither is set, `total_max_connections` assumes a default value. If only `max_connections` is
set, then Hasura Cloud will not be able to maintain a fixed size of a pool and hence the total number of connections on
the database can be random.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/database-config/cloud-connection-pooling/#introduction)
    - [ Get started ](https://hasura.io/docs/latest/databases/database-config/cloud-connection-pooling/#get-started)
- [ How connection pooling works ](https://hasura.io/docs/latest/databases/database-config/cloud-connection-pooling/#how-connection-pooling-works)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)