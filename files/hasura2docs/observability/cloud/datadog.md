# Datadog Integration on Hasura Cloud

## Introduction​

You can export metrics, operation logs and traces of your Hasura Cloud project to your organization's Datadog dashboard.
This can be configured on the integrations tab on the project's setting page.

Note

For Hasura Cloud projects, the Datadog Integration is only available on the `Standard` (pay-as-you-go) tier and above.

More metrics on OpenTelemetry exporter

Try the new[ OpenTelemetry exporter ](https://hasura.io/docs/latest/observability/opentelemetry/)to get advanced metrics and traces to connect
with Datadog. This integration will export the metrics as detailed[ here ](https://hasura.io/docs/latest/observability/cloud/datadog/#view-metrics).

## Configure Datadog integration​

Navigate to the integrations tab on project settings page to find Datadog integration.

Image: [ Configure Datadog Integration ](https://hasura.io/docs/assets/images/integrate-datadog-1a373bdc6a2d22dfc0740c593d2dee1a.png)

Select the Datadog API region and enter the Datadog API key (can be retrieved by navigating to Datadog's settings page
by clicking the `Get API Key` link), host, service name and tags to associate with exported logs, metrics and traces.

| Field | Description |
|---|---|
| Region | Hasura supports all available Datadog regions, namely US1, US3, US5, EU, US1FED. |
| API Key | API keys are unique to your organization. An API key is required by the Datadog agent to submit metrics and events to Datadog. Click on `Read more` above the `API Key` field in the Datadog integration form to get the API key. |
| Host | The name of the originating host of the log and metrics. |
| Tags | Tags associated with your logs and metrics. Default tags `project_ id` and `project_ name` are exported with all logs and metrics. A source tag `hasura-cloud-metrics` is added to all exported logs. |
| Service Name | The name of the application or service generating the log events. |


Image: [ Configure Datadog Integration ](https://hasura.io/docs/assets/images/configure-datadog-4895c191836456618855a586ad96fc5f.png)

After adding appropriate values, click `Save` .

## Checking the status of the integration​

The green/red dot signifies the status of the integration. Green signifies successful exporting of logs to datadog. When
logs are successfully exported, `Last Exported` is continuously updated, indicating the timestamp of the last log line
successfully exported to your Datadog dashboard.

Image: [ Datadog Integration successfully configured ](https://hasura.io/docs/assets/images/configure-datadog-done-e0a3c258bf98a69d67ad500025f83df9.png)

In case there is an error while exporting logs to datadog, the dot is red and the HTTP status code of the error is
displayed right below it.

Image: [ Datadog Integration successfully configured ](https://hasura.io/docs/assets/images/configure-datadog-fail-29daa8bc8ab87cef0a81608f6cb8f0fc.png)

## View logs​

The logs can be viewed in your Datadog dashboard, under the `Logs` tab. To navigate to the same, click `View Logs` .

Image: [ Datadog Integration successfully configured ](https://hasura.io/docs/assets/images/datadog-view-logs-ff80f80950e67f543dddcd728940c2f0.png)

Image: [ Logs successfully exported to Datadog ](https://hasura.io/docs/assets/images/datadog-logs-a45ded2d92733f8dbf3f022be24a5f12.png)

To view only logs exported by Hasura Cloud, filter your logs using `host` and/or `tags` you configured with this
integration.

Note

Datadog allows ingestion of logs with maximum size 256kB for a single log. If a log exceeds this limit, Datadog will
truncate the log at 256kB.

## View metrics​

The integration exports the following five metrics to your Datadog dashboard:

| Metric Exported | Metric Name in Datadog |
|---|---|
| Average number of requests |  `average_ requests_ per_ minute`  |
| Average request execution time |  `average_ execution_ time`  |
| Success rate of requests |  `success_ rate`  |
| Active subscriptions |  `active_ subscriptions`  |
| Number of websockets open |  `websockets_ open`  |


Non zero values of all the above metrics are exported over a one minute time interval. Each metric name is prefixed with `hasura_cloud` .

Graphs for all the above metrics can be viewed in your Datadog dashboard, under the `Metrics` tab. To navigate to the
same, click `View Metrics` .

Image: [ Datadog Integration successfully configured ](https://hasura.io/docs/assets/images/datadog-view-metrics-2763bd5aeb86fb96ca17e095a5a42f00.png)

Select the graphs you want to view from the metrics explorer. Alternatively, select the `host` you configured with this
integration to see all the graphs corresponding to metrics exported by Hasura Cloud.

Image: [ Metrics successfully exported to Datadog ](https://hasura.io/docs/assets/images/datadog-metrics-5114bba730c2b3b89e2b2a810e623a98.png)

## View traces​

Along with the logs and metrics, query tracing is exported to Datadog. From your Datadog metrics page, `APM` > `Traces` will show you a live search of ingested trace data, with each entry of the output table showing the duration of the
operation.

Clicking on an entry from the table will show the details about the trace, including a flame graph, which contains a
visual representation of where the operation spent its execution over time. For example, in this case a query took 2.31
milliseconds in total, of which 758 microseconds was the actual Postgres database processing the query.

Image: [ Flame graph for a trace entry in Datadog ](https://hasura.io/docs/assets/images/datadog-trace-flame-graph-a150248aae5cc54c0b68fe401f51a2be.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/observability/cloud/datadog/#introduction)
- [ Configure Datadog integration ](https://hasura.io/docs/latest/observability/cloud/datadog/#configure-datadog-integration)
- [ Checking the status of the integration ](https://hasura.io/docs/latest/observability/cloud/datadog/#checking-the-status-of-the-integration)
- [ View logs ](https://hasura.io/docs/latest/observability/cloud/datadog/#view-logs)
- [ View metrics ](https://hasura.io/docs/latest/observability/cloud/datadog/#view-metrics)
- [ View traces ](https://hasura.io/docs/latest/observability/cloud/datadog/#view-traces)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)