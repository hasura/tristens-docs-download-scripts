# Prometheus Integration for Hasura Cloud

## Introduction​

You can export metrics of your Hasura Cloud project to[ Prometheus ](https://prometheus.io/). This can be configured on
the integrations tab on the project's setting page.

Note

For Hasura Cloud projects, the Prometheus Integration is only available on the `Standard` (pay-as-you-go) tier and
above.

More metrics on OpenTelemetry exporter

Try the new[ OpenTelemetry exporter ](https://hasura.io/docs/latest/observability/opentelemetry/)to get advanced metrics and traces to connect
with Prometheus. This integration will export the metrics as detailed[ here ](https://hasura.io/docs/latest/observability/cloud/prometheus/#metrics-details).

## Configure Prometheus integration​

Navigate to the integrations tab on project settings page to find Prometheus integration.

Image: [ Configure Prometheus Integration ](https://hasura.io/docs/assets/images/integrate-prometheus-8a9fc1c1cb0645c0ffe38f6c0a1a8b7e.png)

Enter the Namespace and label values to be associated to the exported metrics and click on *Connect Integration* .

| Field | Description |
|---|---|
| Namespace (Optional) | The single word prefix relevant to the domain the metrics belong to.[ Read more about namespace on Prometheus docs. ](https://prometheus.io/docs/practices/naming/#metric-names) |
| Labels (Optional) | [ Labels ](https://prometheus.io/docs/practices/naming/#labels)are key-value pairs associated with your metrics used to differentiate the characteristics of the metric that is being measured. |


Image: [ Configure Prometheus Integration ](https://hasura.io/docs/assets/images/configure-prometheus-6d104f0906f09a1a0fd4e825985fcfde.png)

## Prometheus instance configuration​

The Prometheus instance(Agent) needs to be configured with Basic Auth mode with Project ID as username and the generated
Access token as Password. The Connection URL is needed to configure the Scrape Target rule.

### Access Token​

The Access Token is generated once the Integration is created. The token is showed only once and cannot be retrieved
again. Access token is used as the password for Basic Authentication by the Prometheus Agent.

Image: [ Prometheus Access Token ](https://hasura.io/docs/assets/images/prometheus-access-token-329fafc40b150ad7948c4ba5d20535e9.png)

The token can be re-generated from the Configuration Panel of the Integration. This action is permanent and cannot be
reversed.

Image: [ Prometheus Access Token Regeneration ](https://hasura.io/docs/assets/images/prometheus-regenerate-token-acd9a9ea33d47dde48004919cbee94cb.png)

### Connection URL​

This is the secured webhook URL which exposes the Project Metrics in the prometheus compatible format. It has 3 parts
namely scheme, host name and metrics_path. For example, if the connection URL is `https://prometheus-exporter.pro.hasura.io/metrics` , then the scheme is `https` , host name (This includes sub-domains as
well) is `prometheus-exporter.pro.hasura.io` and metrics_path is `/metrics` .

Image: [ Prometheus Connection URL ](https://hasura.io/docs/assets/images/prometheus-connection-url-aa056f23b35b409132e2c6eaf2b2f1cc.png)

### Project ID​

The Project ID is used as the Username for the Basic Authentication by the Prometheus agent.

Image: [ Prometheus Copy Project ID ](https://hasura.io/docs/assets/images/prometheus-project-id-copy-792a96c6438b873a22118d426538595f.png)

The following YAML template can be used as the[ config file ](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)to establish connectivity with
the exposed Integration.

```
global :
   scrape_interval :  60s
scrape_configs :
   -   job_name :   'hasura_prometheus_exporter'
     scrape_interval :  60s  ## Recommended scrape interval is 60s
     metrics_path :   '/metrics'   ## Replace with metrics Path of the connection URL
     scheme :   'https'   ## Replace with the scheme of the connection URL
     basic_auth :
       username :   'd01c60e1-1b11-564d-bb09-0a39e3e41b05'   ## Replace with project ID
       password :   'IrhO3GlR8oXTfsdfdsNs8Nj'   ## Replace with Access Token
     static_configs :
       -   targets :   [ 'prometheus-exporter.pro.hasura.io' ]   ## Replace with the host name of the connection URL
```

## Checking the status of the integration​

The green/red dot signifies the status of the integration. Green signifies successful exporting of metrics to
Prometheus. When metrics are successfully exported, `Last Exported` is continuously updated, indicating the timestamp of
the last metric successfully exported to your Prometheus Instance.

Image: [ Prometheus Integration successfully configured ](https://hasura.io/docs/assets/images/prometheus-configure-done-c184b380e43e56ecdcb3c935a52df78d.png)

In case there is an error while exporting metrics to Prometheus, the dot is red and the error message is displayed right
below it.

Image: [ Prometheus integration Pull failed ](https://hasura.io/docs/assets/images/prometheus-configure-fail-9a162ba874fcc042a1ca31fe92f8bc62.png)

## Metrics details​

The integration exports the following five metrics to your Prometheus Instance:

| Metric Exported | Metric Name in Prometheus |
|---|---|
| Average number of requests |  `average_ requests_ per_ minute`  |
| Average request execution time |  `average_ execution_ time`  |
| Success rate of requests |  `success_ rate`  |
| Active subscriptions |  `active_ subscriptions`  |
| Number of websockets open |  `websockets_ open`  |


Note

If `average_requests_per_minute` is `0` (Which means no incoming requests in the Last one minute), `average_execution_time` is reported as `0` and `success_rate` is reported as 1 to avoid `NaN` values in Prometheus.

Note

If `Namespace` and `Labels` are configured (Optional), the format of the metric identifier is `namespace_metricName{key1=value1, key2=value2}` 

## View metrics​

The metrics can be queried from the Prometheus Dashboard (or using tools like[ Grafana ](https://prometheus.io/docs/visualization/grafana/))

Image: [ Prometheus view Metrics ](https://hasura.io/docs/assets/images/prometheus-view-metrics-b785b13c467eb0e57979833aff9e06a0.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/observability/cloud/prometheus/#metrics-details/#introduction)
- [ Configure Prometheus integration ](https://hasura.io/docs/latest/observability/cloud/prometheus/#metrics-details/#configure-prometheus-integration)
- [ Prometheus instance configuration ](https://hasura.io/docs/latest/observability/cloud/prometheus/#metrics-details/#prometheus-instance-configuration)
    - [ Access Token ](https://hasura.io/docs/latest/observability/cloud/prometheus/#metrics-details/#access-token)

- [ Connection URL ](https://hasura.io/docs/latest/observability/cloud/prometheus/#metrics-details/#connection-url)

- [ Project ID ](https://hasura.io/docs/latest/observability/cloud/prometheus/#metrics-details/#project-id)
- [ Checking the status of the integration ](https://hasura.io/docs/latest/observability/cloud/prometheus/#metrics-details/#checking-the-status-of-the-integration)
- [ Metrics details ](https://hasura.io/docs/latest/observability/cloud/prometheus/#metrics-details/#metrics-details)
- [ View metrics ](https://hasura.io/docs/latest/observability/cloud/prometheus/#metrics-details/#view-metrics)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)