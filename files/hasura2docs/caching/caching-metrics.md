# Caching Metrics

## Introduction​

Hasura Enterprise Edition exports Prometheus metrics related to caching which
can provide valuable insights into the efficiency and performance of the caching system.
This can help towards monitoring and further optimization of the cache utilization.

## Exposed metrics​

The graphql engine exposes the[ hasura_cache_request_count ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#hasura-cache-request-count)Prometheus metric. It represents a `counter` and is incremented every time a request with `@cached` directive is served.

It has one label `status` , which can have values of either `hit` or `miss` .

| status | description |
|---|---|
|  `hit`  | request served from the cache |
|  `miss`  | request served from the source (not found in cache) |


## Get insights from metrics​

The `hasura_cache_request_count` metric can be used to get insights into the cache utilization by calculating the hit-miss ratio.
The hit-miss ratio is the ratio of the number of requests served from the cache to the total number of requests.

`hit-miss ratio = hit count / (hit count + miss count)`

What does the hit-miss ratio tells us?

- **Cache Efficiency** : The hit-miss ratio reflects how well the caching system can serve requests from its cache. A higher hit ratio indicates more efficient cache usage, as more requests are being served from the cache rather than requiring fetching data from the upstream data source.
- **Cache Performance** : The hit-miss ratio is a measure of cache performance. A higher hit ratio generally indicates better cache performance as it reduces latency and improves overall system performance.


 **Cache Efficiency** : The hit-miss ratio reflects how well the caching system can serve requests from its cache. A higher hit ratio indicates more efficient cache usage, as more requests are being served from the cache rather than requiring fetching data from the upstream data source.

 **Cache Performance** : The hit-miss ratio is a measure of cache performance. A higher hit ratio generally indicates better cache performance as it reduces latency and improves overall system performance.

## Visualize metrics​

The metrics can be visualized using a tool like Grafana.

Image: [ Cache Metrics Grafana Dashboard ](https://hasura.io/docs/assets/images/cache-metrics-grafana-c25466b7b13afb820369a5f612986bca.png)

Sample PromQL Queries

- Total requests per minute with `@cached` directive: `sum(increase(hasura_cache_request_count[1m]))`
- `hit` requests per minute: `increase(hasura_cache_request_count{status="hit"}[1m])`
- `miss` requests per minute: `increase(hasura_cache_request_count{status="miss"}[1m])`
- Hit-Miss ratio over lifetime: `sum(hasura_cache_request_count{status="hit"})/sum(hasura_cache_request_count)`


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/caching/caching-metrics/#introduction)
- [ Exposed metrics ](https://hasura.io/docs/latest/caching/caching-metrics/#exposed-metrics)
- [ Get insights from metrics ](https://hasura.io/docs/latest/caching/caching-metrics/#get-insights-from-metrics)
- [ Visualize metrics ](https://hasura.io/docs/latest/caching/caching-metrics/#visualize-metrics)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)