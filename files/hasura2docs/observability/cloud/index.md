# Hasura Cloud observability integrations with external services

## Introduction​

To be able to effectively monitor, diagnose and troubleshoot your application stack in production, Hasura Cloud will
export metrics, logs and traces to observability tools / APM vendors.

## Supported integrations​

Check out the following guides on how to export telemetry data from Hasura Cloud to the observability tool of your
choice:

- [ Datadog ](https://hasura.io/docs/latest/observability/cloud/datadog/)
- [ New Relic ](https://hasura.io/docs/latest/observability/cloud/newrelic/)
- [ Azure monitor ](https://hasura.io/docs/latest/observability/cloud/azure-monitor/)
- [ Prometheus ](https://hasura.io/docs/latest/observability/cloud/prometheus/)
- [ OpenTelemetry ](https://hasura.io/docs/latest/observability/opentelemetry/)


More metrics on OpenTelemetry exporter

Try the new[ OpenTelemetry exporter ](https://hasura.io/docs/latest/observability/opentelemetry/)to get advanced metrics and traces to connect
with the tool of your choice. This integration will export the metrics as detailed[ here ](https://hasura.io/docs/latest/observability/cloud/prometheus/#metrics-details).

## Log types​

Hasura Cloud combines various[ Hasura GraphQL Engine server log types ](https://hasura.io/docs/latest/deployment/logging/)into a single log called the **operation log** . This operation log is exported via integrations to your observability tool of choice.

Various Hasura GraphQL Engine server logs are combined to generate an operation log:

- `http_logs`
- `query_logs`
- `websocket_logs`
- `ws_server_logs`
- `ws_connection_init_logs`


```
{
   "operation_type" :   "query" ,
   "request_read_time" :   0.00000776 ,
   "response_size" :   443 ,
   "execution_time" :   0.254919258 ,
   "user_role" :   "admin" ,
   "hostname" :   "hasura-cloud" ,
   "project_id" :   "6450524a-ecc2-4676-9ecb-ba6a90a13c3d" ,
   "is_error" :   false ,
   "operation_id" :   "a456caf866ebcab1a592ade80f07a622652181a9" ,
   "request_size" :   100 ,
   "user_vars" :   {
     "x-hasura-role" :   "admin"
   } ,
   "client_name" :   "" ,
   "ws_operation_id" :   "" ,
   "parameterized_query_hash" :   "a456caf866ebcab1a592ade80f07a622652181a9" ,
   "server_client_id" :   "" ,
   "websocket_id" :   "" ,
   "kind" :   "" ,
   "query" :   {
     "query" :   "query MyQuery {\n author {\n id\n }\n}\n" ,
     "operationName" :   "MyQuery"
   } ,
   "instance_uid" :   "c9e43acf-2e09-41a7-8aa8-ddeff4e64a21" ,
   "transport" :   "http" ,
   "url" :   "/v1/graphql" ,
   "operation_name" :   "MyQuery" ,
   "service" :   "polite-muskox-52" ,
   "request_headers" :   {
     "referer" :   "https://cloud.hasura.io/" ,
     "sec-fetch-site" :   "cross-site" ,
     "origin" :   "https://cloud.hasura.io" ,
     "true-client-ip" :   "106.51.72.39" ,
     "CDN-Loop" :   "cloudflare" ,
     "Accept-Encoding" :   "gzip" ,
     "CF-Connecting-IP" :   "106.51.72.39" ,
     "sec-ch-ua-mobile" :   "?0" ,
     "content-type" :   "application/json" ,
     "Content-Length" :   "100" ,
     "X-Real-IP" :   "106.51.72.39" ,
     "sec-fetch-mode" :   "cors" ,
     "CF-IPCountry" :   "IN" ,
     "CF-RAY" :   "7a08f2590e4cf45e-BOM" ,
     "accept-language" :   "en-US,en;q=0.9" ,
     "X-Request-Id" :   "2f1280a31e31716e4300e84550cc7eb7" ,
     "Connection" :   "close" ,
     "X-Forwarded-Proto" :   "https" ,
     "CF-Visitor" :   "{\"scheme\":\"https\"}" ,
     "Host" :   "polite-muskox-52.hasura.app" ,
     "dnt" :   "1" ,
     "accept" :   "*/*" ,
     "sec-ch-ua" :   "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"" ,
     "sec-ch-ua-platform" :   "\"macOS\"" ,
     "X-Forwarded-For" :   "106.51.72.39" ,
     "X-NginX-Proxy" :   "true" ,
     "sec-fetch-dest" :   "empty" ,
     "user-agent" :   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
   } ,
   "db_uid" :   "" ,
   "error_code" :   "" ,
   "time" :   "2023-02-28T11:51:09.116Z" ,
   "request_id" :   "2f1280a31e31716e4300e84550cc7eb7"
}
```

## Metrics​

Hasura Cloud APM integrations export the following metrics:

| Metric Name | Description |
|---|---|
|  `average_ requests_ per_ minute`  | Average number of requests |
|  `average_ execution_ time`  | Average request execution time |
|  `success_ rate`  | Success rate of requests |
|  `active_ subscriptions`  | Number of Active subscriptions |
|  `websockets_ open`  | Number of open websockets |


## Traces​

Hasura Cloud APM integrations export the same trace logs as Hasura GraphQL Engine. You can find more information about
tracing[ here ](https://hasura.io/docs/latest/observability/cloud-monitoring/tracing/).

Sampling

Hasura samples all trace logs and exports only 5% to your configured APM provider.

```
{
   "resourceSpans" :   [
     {
       "resource" :   {
         "attributes" :   [
           {
             "key" :   "Region" ,
             "value" :   {
               "stringValue" :   "us-west"
             }
           }
         ]
       } ,
       "scopeSpans" :   [
         {
           "scope" :   {
             "name" :   "hasura" ,
             "version" :   "v2.19.0"
           } ,
           "spans" :   [
             {
               "traceId" :   "e44b8c614e0f7434b7b55c914fa71b1c" ,
               "spanId" :   "d3af63b8e6191589" ,
               "parentSpanId" :   "a5648ac5af5faf1f" ,
               "name" :   "Postgres" ,
               "startTimeUnixNano" :   "1676531420905206010" ,
               "endTimeUnixNano" :   "1676531420916114926" ,
               "status" :   {
                 "code" :   "STATUS_CODE_OK"
               }
             } ,
             {
               "traceId" :   "e44b8c614e0f7434b7b55c914fa71b1c" ,
               "spanId" :   "a5648ac5af5faf1f" ,
               "parentSpanId" :   "0d6b602bc5a7b3af" ,
               "name" :   "Postgres Query for root field \"Album\"" ,
               "startTimeUnixNano" :   "1676531420905131593" ,
               "endTimeUnixNano" :   "1676531420916617176" ,
               "status" :   {
                 "code" :   "STATUS_CODE_OK"
               }
             } ,
             {
               "traceId" :   "e44b8c614e0f7434b7b55c914fa71b1c" ,
               "spanId" :   "0d6b602bc5a7b3af" ,
               "parentSpanId" :   "a085bd763f8f72da" ,
               "name" :   "Query" ,
               "startTimeUnixNano" :   "1676531420904690968" ,
               "endTimeUnixNano" :   "1676531420916671343" ,
               "status" :   {
                 "code" :   "STATUS_CODE_OK"
               }
             } ,
             {
               "traceId" :   "e44b8c614e0f7434b7b55c914fa71b1c" ,
               "spanId" :   "a085bd763f8f72da" ,
               "parentSpanId" :   "" ,
               "name" :   "/v1/graphql" ,
               "startTimeUnixNano" :   "1676531420903555760" ,
               "endTimeUnixNano" :   "1676531420919447135" ,
               "status" :   {
                 "code" :   "STATUS_CODE_OK"
               }
             }
           ]
         }
       ]
     }
   ]
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/observability/cloud/index/#introduction)
- [ Supported integrations ](https://hasura.io/docs/latest/observability/cloud/index/#supported-integrations)
- [ Log types ](https://hasura.io/docs/latest/observability/cloud/index/#log-types)
- [ Metrics ](https://hasura.io/docs/latest/observability/cloud/index/#metrics)
- [ Traces ](https://hasura.io/docs/latest/observability/cloud/index/#traces)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)