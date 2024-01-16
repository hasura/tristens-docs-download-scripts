# Metadata API Reference: Observability Options

## Introduction​

The API to manage `Observability` related metadata configurations.

## Logs and metrics configuration​

These are the configurations that govern the metrics and logging output for debugging and analytics.

## set_metrics_config​

 `set_metrics_config` is used to add/update logs and metrics configurations.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "set_metrics_config" ,
     "args" :   {
         "analyze_query_variables" :   false
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| analyze_query_variables | false | boolean | Enables logging of the values of the query variables provided for each request. Default is `false` . |


Please see the corresponding[ feature documentation for the usage of these configurations ](https://hasura.io/docs/latest/observability/cloud-monitoring/operations/#capture-query-variables).

## remove_metrics_config​

 `remove_metrics_config` is used to remove all metrics configurations.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "remove_metrics_config" ,
     "args" :   { }
}
```

## OpenTelemetry Configuration​

The OpenTelemetry configuration enables export of[ distributed traces ](https://hasura.io/docs/latest/observability/cloud-monitoring/tracing/)and[ metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/)to an to an[ OpenTelemetry ](https://opentelemetry.io/)compliant APM receiver.

## set_opentelemetry_config​

 `set_opentelemetry_config` is used to add/update OpenTelemetry configuration.

Supported from

OpenTelemetry traces are supported for Hasura GraphQL Engine versions `v2.18.0` and above.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "set_opentelemetry_config" ,
     "args" :   {
         "status" :   "enabled" ,
         "data_types" :   [
             "traces" ,
             "metrics" ,
             "logs"
         ] ,
         "exporter_otlp" :   {
             "otlp_traces_endpoint" :   "http://localhost:4318/v1/traces" ,
             "otlp_metrics_endpoint" :   "http://localhost:4318/v1/metrics" ,
             "otlp_logs_endpoint" :   "http://localhost:4318/v1/logs" ,
             "protocol" :   "http/protobuf" ,
             "traces_propagators" :   [ "tracecontext" ] ,
             "headers" :   [
                 {
                     "name" :   "x-test-header" ,
                     "value" :   "testing"
                 } ,
                 {
                     "name" :   "x-header-from-env" ,
                     "value_from_env" :   "TEST_ENV_VAR"
                 }
             ] ,
             "resource_attributes" :   [
                 {
                     "name" :   "stage" ,
                     "value" :   "production"
                 } ,
                 {
                     "name" :   "region" ,
                     "value" :   "us-east"
                 }
             ]
         } ,
         "batch_span_processor" :   {
             "max_export_batch_size" :   100
         }
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| status | false |  `String`  | Toggle to enable or disable the export. Allowed values are `enabled` and `disabled` . Default is `disabled` (If status is not explicitely passed, then the configuration gets disabled) |
| data_types | false |  `[String]`  | List of the types of observability data points to be exported. Allowed types: `traces` and `metrics` only |
| exporter_otlp | false | [ OTLPExporter ](https://hasura.io/docs/latest/api-reference/syntax-defs/#otlpexporter). This is required if status is enabled | OpenTelemetry compliant receiver configuration |
| batch_span_processor | false | [ OpenTelemetryBatchSpanProcessor ](https://hasura.io/docs/latest/api-reference/syntax-defs/#opentelemetrybatchspanprocessor) | OpenTelemetry batch export configuration |


## set_opentelemetry_status​

 `set_opentelemetry_status` is used to set just the `status` field of the OpenTelemetry configuration, which
enable/disable the export to the OpenTelemetry receiver. Other configuration settings are preserved.

Supported from

This is supported for versions `v2.18.0` and above.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "set_opentelemetry_status" ,
     "args" :   "enabled"
}
```

Allowed values of `args` are `enabled` and `disabled` 

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/observability/#metadata-set-opentelemetry-config/#introduction)
- [ Logs and metrics configuration ](https://hasura.io/docs/latest/api-reference/metadata-api/observability/#metadata-set-opentelemetry-config/#logs-and-metrics-configuration)
- [ set_metrics_config ](https://hasura.io/docs/latest/api-reference/metadata-api/observability/#metadata-set-opentelemetry-config/#metadata-set-metrics-config)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/observability/#metadata-set-opentelemetry-config/#set-metrics-config-syntax)
- [ remove_metrics_config ](https://hasura.io/docs/latest/api-reference/metadata-api/observability/#metadata-set-opentelemetry-config/#metadata-remove-metrics-config)
- [ OpenTelemetry Configuration ](https://hasura.io/docs/latest/api-reference/metadata-api/observability/#metadata-set-opentelemetry-config/#opentelemetry-configuration)
- [ set_opentelemetry_config ](https://hasura.io/docs/latest/api-reference/metadata-api/observability/#metadata-set-opentelemetry-config/#metadata-set-opentelemetry-config)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/observability/#metadata-set-opentelemetry-config/#set-opentelemetry-config-syntax)
- [ set_opentelemetry_status ](https://hasura.io/docs/latest/api-reference/metadata-api/observability/#metadata-set-opentelemetry-config/#set-opentelemetry-status)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)