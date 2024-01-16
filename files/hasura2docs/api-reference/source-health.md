# Source Health Check API Reference

## Introduction​

The Source Health API is an admin-only endpoint which reports the health of sources whose Health Check is configured.[ Documentation here ](https://hasura.io/docs/latest/deployment/health-checks/source-health-check/).

## Endpoint​

All requests are `GET` requests to the `/healthz/sources` endpoint.

## API Spec​

### Request​

```
GET   /healthz/sources   HTTP/1.1
X-Hasura-Role :   admin
```

### Response​

The response is an object with the source name as key and health status as value.

```
{
    "source_1": HealthStatus,
    "source_2": HealthStatus,
     ...        ...
    "source_n": HealthStatus
}
```

The `HealthStatus` is an object with the following members.

| Name | Type | Description |
|---|---|---|
| status |  `string`  | The status of the Health Check |
| error | any `json`  | An additional field whose value varies based on the `status`  |
| timestamp |  `string`  | A[ UTC time ](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)encoded value |


Find the possible values of `status` field in the following along with corresponding `error` field value.

| status | error | Description |
|---|---|---|
| "OK" |  `null`  | Health Check succeeded with configured test; the source is healthy |
| "TIMEOUT" |  `null`  | Health Check timed out |
| "ERROR" |  `HealthCheckError`  | Exceptions occurred after running Health Check; refer `error` for in-depth details |
| "FAILED" |  `String`  | Health Check failed due to bad configuration |


The `HealthCheckError` is an object with the following members.

| Name | Type | Description |
|---|---|---|
| message |  `string`  | A very short description of the error |
| extra | any `json`  | An optional value that contains more details about the error |


### Sample response​

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
   "mssql_source_name" :   {
     "error" :   null ,
     "status" :   "OK" ,
     "timestamp" :   "2022-08-09T09:32:05.235347837Z"
   } ,
   "postgres_source_name" :   {
     "error" :   {
       "message" :   "connection error" ,
       "extra" :   "connection to server at \"localhost\" (::1), port 6432 failed: Connection refused\n\tIs the server running on that host and accepting TCP/IP connections?\nconnection to server at \"localhost\" (127.0.0.1), port 6432 failed: Connection refused\n\tIs the server running on that host and accepting TCP/IP connections?\n"
     } ,
     "status" :   "ERROR" ,
     "timestamp" :   "2022-08-09T09:30:05.235347837Z"
   }
}
```

Note

The `healthz/sources` API endpoint cannot be disabled.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/source-health/#introduction)
- [ Endpoint ](https://hasura.io/docs/latest/api-reference/source-health/#endpoint)
- [ API Spec ](https://hasura.io/docs/latest/api-reference/source-health/#api-spec)
    - [ Request ](https://hasura.io/docs/latest/api-reference/source-health/#request)

- [ Response ](https://hasura.io/docs/latest/api-reference/source-health/#response)

- [ Sample response ](https://hasura.io/docs/latest/api-reference/source-health/#sample-response)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)