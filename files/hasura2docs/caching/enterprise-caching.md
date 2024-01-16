# Enable Caching in Hasura Enterprise Edition

## Introduction​

To start using[ Hasura Caching ](https://hasura.io/docs/latest/caching/overview/)with your Hasura Enterprise Edition GraphQL Engine you will need
a Redis instance that is co-located with the Hasura GraphQL containers.

Once you provision a Redis instance, provide the URL to the Hasura GraphQL Engine docker configuration using the
following environment variable:

`HASURA_GRAPHQL_REDIS_URL=redis://username:password@redishostname:port`

## Enable Redis TLS​

TLS connection information can be specified via the following environment variables:

- `HASURA_GRAPHQL_REDIS_USE_TLS` : Opt-in flag that enables the use of TLS for the caching Redis instance, defaults to
false.
- `HASURA_GRAPHQL_RATE_LIMIT_REDIS_USE_TLS` : Opt-in flag that enables the use of TLS for the rate-limiting Redis
instance, defaults to false.
- `HASURA_GRAPHQL_REDIS_TLS_HOSTNAME` : TLS hostname to use for caching Redis instance.
- `HASURA_GRAPHQL_RATE_LIMIT_REDIS_TLS_HOSTNAME` : TLS hostname to use for rate-limiting Redis instance.
- `HASURA_GRAPHQL_REDIS_TLS_SHARED_CA_STORE_PATH` : path to the shared CA certificate store to use for both the caching
and rate-limiting Redis instances. If unspecified, it defaults to the system CA store if available.


### Example​

```
HASURA_GRAPHQL_REDIS_USE_TLS="true"
HASURA_GRAPHQL_REDIS_URL="redis://username:password@redishostname:port"
HASURA_GRAPHQL_REDIS_TLS_HOSTNAME="redishostname"
```

For rate limit Redis:

```
HASURA_GRAPHQL_RATE_LIMIT_REDIS_USE_TLS="true"
HASURA_GRAPHQL_RATE_LIMIT_REDIS_URL="redis://username:password@redishostname:port"
HASURA_GRAPHQL_RATE_LIMIT_REDIS_TLS_HOSTNAME="redishostname"
```

## Tune caching parameters​

You can tune the various caching parameters according to your use-case. For example, you can configure the maximum
TTL allowed, the max entry size in the cache etc.

| Env var | Flag | Description |
|---|---|---|
|  `HASURA_ GRAPHQL_ CACHE_ MAX_ ENTRY_ TTL`  |  `--query-cache-max-ttl`  | Maximum TTL allowed in seconds. Clients can request TTL via the `@cached` directive. But an upper limit can be set using this setting. Default: 3600 seconds |
|  `HASURA_ GRAPHQL_ CACHE_ MAX_ ENTRY_ SIZE`  |  `--query-cache-max-entry-size`  | Maximum size of the response that is allowed to be cached (in MB). default: 1000 MB |
|  `HASURA_ GRAPHQL_ CACHE_ BUCKET_ RATE`  |  `--query-cache-bucket-rate`  | Recharge rate for the Query Response Cache token bucket. Default: 10,000,000 bytes/second (10 MB/s) |
|  `HASURA_ GRAPHQL_ CACHE_ BUCKET_ SIZE`  |  `--query-cache-bucket-size`  | Maximum capacity in bytes for the Query Response Cache token bucket algorithm. See[ https://hasura.io/docs/latest/queries/response-caching ](https://hasura.io/docs/latest/queries/response-caching)for more info. Default: 1000000000 bytes (1 GB) |


### How to tune these parameters​

- `HASURA_GRAPHQL_CACHE_MAX_ENTRY_TTL` - TTL is the only automatic way of invalidating cache entries in Hasura. Ideally,
you would like to keep the TTL closer to the frequency of your data updates. In some use-cases, if you want to cache
for large amounts of time (in the order of 10s of hours), you may set the max TTL to that, and have some way of
using the[ cache clear APIs ](https://hasura.io/docs/latest/caching/caching-config/#clearing-items-from-the-cache)to invalidate the cache
when you update your data.
- `HASURA_GRAPHQL_CACHE_MAX_ENTRY_SIZE` - The default response size for a single cache entry is 1000MB. If you want to
cache responses larger than 1000MB, configure this parameter accordingly.
- `HASURA_GRAPHQL_CACHE_BUCKET_RATE` - The default bucket recharge rate is 10MB per second. Set this value to the total
or cumulative response sizes across all your data sources during peak traffic. By setting this parameter
appropriately, you guard your data sources, as well as the cache itself, from being overloaded by the caching
mechanism. Changing this parameter is probably mainly important for non-standard workloads, in which case you can
reach out to Hasura Support.
- `HASURA_GRAPHQL_CACHE_BUCKET_SIZE` - Maximum size of the cache store. If your cache store exceeds this size, new items
cannot be stored. So you should tune this such that at peak traffic, given your configured max entry size and TTL, you
should have ample space to store all the items.


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/caching/enterprise-caching/#introduction)
- [ Enable Redis TLS ](https://hasura.io/docs/latest/caching/enterprise-caching/#enable-redis-tls)
    - [ Example ](https://hasura.io/docs/latest/caching/enterprise-caching/#example)
- [ Tune caching parameters ](https://hasura.io/docs/latest/caching/enterprise-caching/#tune-caching-parameters)
    - [ How to tune these parameters ](https://hasura.io/docs/latest/caching/enterprise-caching/#how-to-tune-these-parameters)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)