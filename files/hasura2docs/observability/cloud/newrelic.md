# New Relic Integration on Hasura Cloud

## Introduction​

You can export metrics and operation logs of your Hasura Cloud project to[ New Relic ](https://newrelic.com/). This can
be configured on the integrations tab on the project's setting page.

Note

For Hasura Cloud projects, the New Relic Integration is only available on the `Standard` (pay-as-you-go) tier and above.

More metrics on OpenTelemetry exporter

Try the new[ OpenTelemetry exporter ](https://hasura.io/docs/latest/observability/opentelemetry/)to get advanced metrics and traces to connect
with New Relic. This integration will export the metrics as detailed[ here ](https://hasura.io/docs/latest/observability/cloud/newrelic/#view-metrics).

## Configure New Relic integration​

Navigate to the integrations tab on project settings page to find New Relic integration.

Image: [ Configure New Relic Integration ](https://hasura.io/docs/assets/images/integrate-newrelic-6e9ff67d95e1bc96b7853ae1385136a7.png)

Select the New Relic API region and enter the New Relic Insights Insert API key (follow[ New Relic docs to retrieve the API key ](https://docs.newrelic.com/docs/apis/get-started/intro-apis/new-relic-api-keys/#insights-insert-key)),
host, service name and custom attributes to associate with exported logs and metrics.

| Field | Description |
|---|---|
| Region | The region of the datacenter where your New Relic account stores its data.[ Read more about regions on New Relic docs. ](https://docs.newrelic.com/docs/using-new-relic/welcome-new-relic/get-started/our-eu-us-region-data-centers) |
| API Key | API keys are unique to your organization. An API key is required by the New Relic API to submit metrics and events to New Relic. You can get the API key from[ here ](https://one.newrelic.com/launcher/api-keys-ui.api-keys-launcher)if you are in New Relic US region and[ here ](https://one.eu.newrelic.com/launcher/api-keys-ui.api-keys-launcher)if you're in New Relic EU region. |
| Host | The name of the originating host of the log and metrics. |
| Custom Attributes | Custom Attributes associated with your logs and metrics. A default source tag `hasura-cloud-metrics` is added to all exported logs and metrics. Attributes `project_ id` and `project_ name` are added to all exported metrics. |
| Service Name | The name of the application or service generating the log events. |


Image: [ Configure New Relic Integration ](https://hasura.io/docs/assets/images/configure-newrelic-ed5ebdc722c6e78af5c110188b0e87c7.png)

After adding appropriate values, click `Save` .

## Checking the status of the integration​

The green/red dot signifies the status of the integration. Green signifies successful exporting of logs to New Relic.
When logs are successfully exported, `Last Exported` is continuously updated, indicating the timestamp of the last log
line successfully exported to your New Relic account.

Image: [ New Relic Integration successfully configured ](https://hasura.io/docs/assets/images/configure-newrelic-done-0b877bac485055fa4b866fef9d5acf10.png)

In case there is an error while exporting logs to New Relic, the dot is red and the HTTP status code of the error is
displayed right below it.

Image: [ New Relic Integration successfully configured ](https://hasura.io/docs/assets/images/configure-newrelic-fail-94199d2b5bbeb9fe01b4b1bf2659c3c5.png)

## View logs​

The logs can be viewed in your New Relic dashboard, under the `Logs` tab
([ read more on New Relic docs ](https://docs.newrelic.com/docs/logs/log-management/get-started/get-started-log-management/#find-data)).
To navigate to the same, click `View Logs` .

Image: [ New Relic Integration successfully configured ](https://hasura.io/docs/assets/images/newrelic-view-logs-541d5c973599ac87800c26ac83054c48.png)

Image: [ Logs successfully exported to New Relic ](https://hasura.io/docs/assets/images/newrelic-logs-293d1f17e203ef058ae925e066f58927.png)

To view only logs exported by Hasura Cloud, filter your logs using `attributes` you configured with this integration.

## View metrics​

The integration exports the following five metrics to your New Relic account:

| Metric Exported | Metric Name in New Relic |
|---|---|
| Average number of requests |  `average_ requests_ per_ minute`  |
| Average request execution time |  `average_ execution_ time`  |
| Success rate of requests |  `success_ rate`  |
| Active subscriptions |  `active_ subscriptions`  |
| Number of websockets open |  `websockets_ open`  |


Non zero values of all the above metrics are exported over a one minute time interval. Each metric name is prefixed with `hasura_cloud` .

Graphs for all the above metrics can be viewed in your New Relic account. Under `Browse Data` select `Metrics` and
choose the metrics name. To navigate to New Relic dashboard, click `View Metrics` .

Image: [ New Relic Integration successfully configured ](https://hasura.io/docs/assets/images/newrelic-view-metrics-6d33166565f3426f0c7b32a3c6831646.png)

Select the graphs you want to view from the metrics explorer.

Image: [ Metrics successfully exported to New Relic ](https://hasura.io/docs/assets/images/newrerlic-metrics-427c58ccd6cebacdc3ec66afa344e0cc.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/observability/cloud/newrelic/#introduction)
- [ Configure New Relic integration ](https://hasura.io/docs/latest/observability/cloud/newrelic/#configure-new-relic-integration)
- [ Checking the status of the integration ](https://hasura.io/docs/latest/observability/cloud/newrelic/#checking-the-status-of-the-integration)
- [ View logs ](https://hasura.io/docs/latest/observability/cloud/newrelic/#view-logs)
- [ View metrics ](https://hasura.io/docs/latest/observability/cloud/newrelic/#view-metrics)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)