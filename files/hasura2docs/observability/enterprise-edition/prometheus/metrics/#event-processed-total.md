# Metrics exported via Prometheus

## Metrics exported​

The following metrics are exported by Hasura GraphQL Engine:

### GraphQL request metrics​

#### Hasura GraphQL execution time seconds​

Execution time of successful GraphQL requests (excluding subscriptions). If more requests are falling in the higher
buckets, you should consider[ tuning the performance ](https://hasura.io/docs/latest/deployment/performance-tuning/).

|  |  |
|---|---|
| Name |  `hasura_ graphql_ execution_ time_ seconds`  |
| Type | Histogram

Buckets: 0.01, 0.03, 0.1, 0.3, 1, 3, 10 |
| Labels |  `operation_ type` : query|mutation |


GraphQL request execution time

- Uses wall-clock time, so it includes time spent waiting on I/O.
- Includes authorization, parsing, validation, planning, and execution (calls to databases, Remote Schemas).


#### Hasura GraphQL requests total​

Number of GraphQL requests received, representing the GraphQL query/mutation traffic on the server.

|  |  |
|---|---|
| Name |  `hasura_ graphql_ requests_ total`  |
| Type | Counter |
| Labels |  `operation_ type` : query|mutation|subscription|unknown |


The `unknown` operation type will be returned for queries that fail authorization, parsing, or certain validations. The `response_status` label will be `success` for successful requests and `failed` for failed requests.

### Hasura Event Triggers metrics​

See more details on Event trigger observability[ here ](https://hasura.io/docs/latest/event-triggers/observability-and-performance/).

#### Event fetch time per batch​

Hasura fetches the events in batches (by default 100) from the Hasura Event tables in the database. This metric
represents the time taken to fetch a batch of events from the database.

A higher metric indicates slower polling of events from the database, you should consider looking into the performance
of your database.

|  |  |
|---|---|
| Name |  `hasura_ event_ fetch_ time_ per_ batch_ seconds`  |
| Type | Histogram

Buckets: 0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10 |
| Labels | none |


#### Event invocations total​

This metric represents the number of HTTP requests that have been made to the webhook server for delivering events.

|  |  |
|---|---|
| Name |  `hasura_ event_ invocations_ total`  |
| Type | Counter |
| Labels |  `status` : success|failed, `trigger_ name` , `source_ name`  |


#### Event processed total​

Total number of events processed. Represents the Event Trigger egress.

|  |  |
|---|---|
| Name |  `hasura_ event_ processed_ total`  |
| Type | Counter |
| Labels |  `status` : success|failed, `trigger_ name` , `source_ name`  |


#### Event processing time​

Time taken for an event to be processed.

|  |  |
|---|---|
| Name |  `hasura_ event_ processing_ time_ seconds`  |
| Type | Histogram

Buckets: 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100 |
| Labels |  `trigger_ name` , `source_ name`  |


The processing of an event involves the following steps:

1. Hasura Engine fetching the event from Hasura Event tables in the database and adding it to the Hasura Events queue
2. An HTTP worker picking up the event from the Hasura Events queue
3. An HTTP worker delivering the event to the webhook


Event delivery failure

Note, if the delivery of the event fails - the delivery of the event is retried based on its `next_retry_at` configuration.

This metric represents the time taken for an event to be delivered since it was created (if the first attempt) or retried
(after the first attempt). **This metric can be considered as the end-to-end processing time for an event.** 

For e.g., say an event was created at `2021-01-01 10:00:30` and it has a `next_retry_at` configuration which says if the
event delivery fails, the event should be retried after 30 seconds.

At `2021-01-01 10:01:30` : the event was fetched from the Hasura Event tables, picked up by the HTTP worker, and the
delivery was attempted. The delivery failed and the `next_retry_at` of `2021-01-01 10:02:00` was set for the event.

Now at `2021-01-01 10:02:00` : the event was fetched again from the Hasura Event tables, picked up by the HTTP worker,
and the delivery was attempted at `2021-01-01 10:03: 30` . This time, the delivery was successful.

The processing time for the second delivery try would be:

Processing Time = event delivery time - event next retried time

Processing Time = `2021-01-01 10:03:30` - `2021-01-01 10:02:00` = `90 seconds` 

#### Event queue time​

Hasura fetches the events from the Hasura Event tables in the database and adds it to the Hasura Events queue. The event
queue time represents the time taken for an event to be picked up by the HTTP worker after it has been added to the
"Events Queue".

Higher value of this metric implies slow event processing. In this case, you can consider increasing the[ HTTP pool size ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#events-http-pool-size)or optimizing the webhook
server.

|  |  |
|---|---|
| Name |  `hasura_ event_ queue_ time_ seconds`  |
| Type | Histogram

Buckets: 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100 |
| Labels |  `trigger_ name` , `source_ name`  |


#### Event Triggers HTTP Workers​

Current number of active Event Trigger HTTP workers. Compare this number to the[ HTTP pool size ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#events-http-pool-size). Consider increasing it if the
metric is near the current configured value.

|  |  |
|---|---|
| Name |  `hasura_ event_ trigger_ http_ workers`  |
| Type | Gauge |
| Labels | none |


#### Event webhook processing time​

The time between when an HTTP worker picks an event for delivery to the time it sends the event payload to the webhook.

A higher processing time indicates slow webhook, you should try to optimize the event webhook.

|  |  |
|---|---|
| Name |  `hasura_ event_ webhook_ processing_ time_ seconds`  |
| Type | Histogram

Buckets: 0.01, 0.03, 0.1, 0.3, 1, 3, 10 |
| Labels |  `trigger_ name` , `source_ name`  |


#### Events fetched per batch​

Number of events fetched from the Hasura Event tables in the database per batch. This number should be equal or less
than the[ events fetch batch size ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#events-fetch-batch-size).

|  |  |
|---|---|
| Name |  `hasura_ events_ fetched_ per_ batch`  |
| Type | Gauge |
| Labels | none |


Since polling the database to continuously check if there are any pending events is an expensive operation, Hasura only
polls the database if there are any pending events. This metric can be used to understand if there are any pending
events in the Hasura Event Tables.

Dependent on pending events

Note that Hasura only fetches events from the Hasura Event tables if there are any pending events. If there are no
pending events, this metric will be 0.

### Subscription metrics​

See more details on subscriptions observability[ here ](https://hasura.io/docs/latest/subscriptions/observability-and-performance/).

#### Active Subscriptions​

Current number of active subscriptions, representing the subscription load on the server.

|  |  |
|---|---|
| Name |  `hasura_ active_ subscriptions`  |
| Type | Gauge |
| Labels |  `subscription_ kind` : streaming|live-query, `operation_ name` , `parameterized_ query_ hash`  |


#### Active Subscription Pollers​

Current number of active subscription pollers. A subscription poller[ multiplexes ](https://github.com/hasura/graphql-engine/blob/master/architecture/live-queries.md#idea-3-batch-multiple-live-queries-into-one-sql-query)similar subscriptions together. The value of this metric should be proportional to the number of uniquely parameterized
subscriptions (i.e., subscriptions with the same selection set, but with different input arguments and session variables
are multiplexed on the same poller). If this metric is high then it may be an indication that there are too many
uniquely parameterized subscriptions which could be optimized for better performance.

|  |  |
|---|---|
| Name |  `hasura_ active_ subscription_ pollers`  |
| Type | Gauge |
| Labels |  `subscription_ kind` : streaming|live-query |


#### Active Subscription Pollers in Error State​

Current number of active subscription pollers that are in the error state. A subscription poller[ multiplexes ](https://github.com/hasura/graphql-engine/blob/master/architecture/live-queries.md#idea-3-batch-multiple-live-queries-into-one-sql-query)similar subscriptions together. A non-zero value of this metric indicates that there are runtime errors in atleast one
of the subscription pollers that are running in Hasura. In most of the cases, runtime errors in subscriptions are caused
due to the changes at the data model layer and fixing the issue at the data model layer should automatically fix the
runtime errors.

|  |  |
|---|---|
| Name |  `hasura_ active_ subscription_ pollers_ in_ error_ state`  |
| Type | Gauge |
| Labels |  `subscription_ kind` : streaming|live-query |


#### Subscription Total Time​

The time taken to complete running of one subscription poller.

A subscription poller[ multiplexes ](https://github.com/hasura/graphql-engine/blob/master/architecture/live-queries.md#idea-3-batch-multiple-live-queries-into-one-sql-query)similar subscriptions together. This subscription poller runs every 1 second by default and queries the database with
the multiplexed query to fetch the latest data. In a polling instance, the poller not only queries the database but does
other operations like splitting similar queries into batches (by default 100) before fetching their data from the
database, etc. **This metric is the total time taken to complete all the operations in a single poll.** 

In a single poll, the subscription poller splits the different variables for the multiplexed query into batches (by
default 100) and executes the batches. We use the `hasura_subscription_db_execution_time_seconds` metric to observe the
time taken for each batch to execute on the database. This means for a single poll there can be multiple values for `hasura_subscription_db_execution_time_seconds` metric.

Let's look at an example to understand these metrics better:

Say we have 650 subscriptions with the same selection set but different input arguments. These 650 subscriptions will be
grouped to form one multiplexed query. A single poller would be created to run this multiplexed query. This poller will
run every 1 second.

The default batch size in hasura is 100, so the 650 subscriptions will be split into 7 batches for execution during a
single poll.

During a single poll:

- Batch 1: `hasura_subscription_db_execution_time_seconds` = 0.002 seconds
- Batch 2: `hasura_subscription_db_execution_time_seconds` = 0.001 seconds
- Batch 3: `hasura_subscription_db_execution_time_seconds` = 0.003 seconds
- Batch 4: `hasura_subscription_db_execution_time_seconds` = 0.001 seconds
- Batch 5: `hasura_subscription_db_execution_time_seconds` = 0.002 seconds
- Batch 6: `hasura_subscription_db_execution_time_seconds` = 0.001 seconds
- Batch 7: `hasura_subscription_db_execution_time_seconds` = 0.002 seconds


The `hasura_subscription_total_time_seconds` would be sum of all the database execution times shown in the batches, plus
some extra process time for other tasks the poller does during a single poll. In this case, it would be approximately
0.013 seconds.

|  |  |
|---|---|
| Name |  `hasura_ subscription_ total_ time_ seconds`  |
| Type | Histogram

Buckets: 0.000001, 0.0001, 0.01, 0.1, 0.3, 1, 3, 10, 30, 100 |
| Labels |  `subscription_ kind` : streaming|live-query, `operation_ name` , `parameterized_ query_ hash`  |


#### Subscription Database Execution Time​

The time taken to run the subscription's multiplexed query in the database for a single batch.

A subscription poller[ multiplexes ](https://github.com/hasura/graphql-engine/blob/master/architecture/live-queries.md#idea-3-batch-multiple-live-queries-into-one-sql-query)similar subscriptions together. During every run (every 1 second by default), the poller splits the different variables
for the multiplexed query into batches (by default 100) and execute the batches. This metric observes the time taken for
each batch to execute on the database.

If this metric is high, then it may be an indication that the database is not performing as expected, you should
consider investigating the subscription query and see if indexes can help improve performance.

|  |  |
|---|---|
| Name |  `hasura_ subscription_ db_ execution_ time_ seconds`  |
| Type | Histogram

Buckets: 0.000001, 0.0001, 0.01, 0.1, 0.3, 1, 3, 10, 30, 100 |
| Labels |  `subscription_ kind` : streaming|live-query, `operation_ name` , `parameterized_ query_ hash`  |


#### WebSocket Egress​

The total size of WebSocket messages sent in bytes.

|  |  |
|---|---|
| Name |  `hasura_ websocket_ messages_ sent_ bytes_ total`  |
| Type | Counter |
| Labels |  `operation_ name` , `parameterized_ query_ hash`  |


#### WebSocket Ingress​

The total size of WebSocket messages received in bytes.

|  |  |
|---|---|
| Name |  `hasura_ websocket_ messages_ received_ bytes_ total`  |
| Type | Counter |
| Labels | none |


#### Websocket Message Queue Time​

The time for which a websocket message remains queued in the GraphQL engine's websocket queue.

|  |  |
|---|---|
| Name |  `hasura_ websocket_ message_ queue_ time`  |
| Type | Histogram

Buckets: 0.000001, 0.0001, 0.01, 0.1, 0.3, 1, 3, 10, 30, 100 |
| Labels | none |


#### Websocket Message Write Time​

The time taken to write a websocket message into the TCP send buffer.

|  |  |
|---|---|
| Name |  `hasura_ websocket_ message_ write_ time`  |
| Type | Histogram

Buckets: 0.000001, 0.0001, 0.01, 0.1, 0.3, 1, 3, 10, 30, 100 |
| Labels | none |


### Cache metrics​

See more details on caching metrics[ here ](https://hasura.io/docs/latest/caching/caching-metrics/)

#### Hasura cache request count​

Tracks cache hit and miss requests, which helps in monitoring and optimizing cache utilization.

|  |  |
|---|---|
| Name |  `hasura_ cache_ request_ count`  |
| Type | Counter |
| Labels |  `status` : hit|miss |


### Cron trigger metrics​

#### Hasura cron events invocation total​

Total number of cron events invoked, representing the number of invocations made for cron events.

|  |  |
|---|---|
| Name |  `hasura_ cron_ events_ invocation_ total`  |
| Type | Counter |
| Labels |  `status` : success|failed |


#### Hasura cron events processed total​

Total number of cron events processed, representing the number of invocations made for cron events. Compare this to `hasura_cron_events_invocation_total` . A high difference between the two metrics indicates high failure rate of the cron
webhook.

|  |  |
|---|---|
| Name |  `hasura_ cron_ events_ processed_ total`  |
| Type | Counter |
| Labels |  `status` : success|failed |


### One-off Scheduled events metrics​

#### Hasura one-off events invocation total​

Total number of one-off events invoked, representing the number of invocations made for one-off events.

|  |  |
|---|---|
| Name |  `hasura_ oneoff_ events_ invocation_ total`  |
| Type | Counter |
| Labels |  `status` : success|failed |


#### Hasura one-off events processed total​

Total number of one-off events processed, representing the number of invocations made for one-off events. Compare this
to `hasura_oneoff_events_invocation_total` . A high difference between the two metrics indicates high failure rate of the
one-off webhook.

|  |  |
|---|---|
| Name |  `hasura_ oneoff_ events_ processed_ total`  |
| Type | Counter |
| Labels |  `status` : success|failed |


### Hasura HTTP connections​

Current number of active HTTP connections (excluding WebSocket connections), representing the HTTP load on the server.

|  |  |
|---|---|
| Name |  `hasura_ http_ connections`  |
| Type | Gauge |
| Labels | none |


### Hasura WebSocket connections​

Current number of active WebSocket connections, representing the WebSocket load on the server.

|  |  |
|---|---|
| Name |  `hasura_ websocket_ connections`  |
| Type | Gauge |
| Labels | none |


### Hasura Postgres connections​

Current number of active PostgreSQL connections. Compare this to[ pool settings ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgpoolsettings).

|  |  |
|---|---|
| Name |  `hasura_ postgres_ connections`  |
| Type | Gauge |
| Labels |  `source_ name` : name of the database
 `conn_ info` : connection url string (password omitted) or name of the connection url environment variable
 `role` : primary|replica |


### Hasura Postgres Connection Initialization Time​

The time taken to establish and initialize a PostgreSQL connection.

|  |  |
|---|---|
| Name |  `hasura_ postgres_ connection_ init_ time`  |
| Type | Histogram

Buckets: 0.000001, 0.0001, 0.01, 0.1, 0.3, 1, 3, 10, 30, 100 |
| Labels |  `source_ name` : name of the database
 `conn_ info` : connection url string (password omitted) or name of the connection url environment variable
 `role` : primary|replica |


### Hasura Postgres Pool Wait Time​

The time taken to acquire a connection from the pool.

|  |  |
|---|---|
| Name |  `hasura_ postgres_ pool_ wait_ time`  |
| Type | Histogram

Buckets: 0.000001, 0.0001, 0.01, 0.1, 0.3, 1, 3, 10, 30, 100 |
| Labels |  `source_ name` : name of the database
 `conn_ info` : connection url string (password omitted) or name of the connection url environment variable
 `role` : primary|replica |


### Hasura source health​

Health check status of a particular data source, corresponding to the output of `/healthz/sources` , with possible values
0 through 3 indicating, respectively: OK, TIMEOUT, FAILED, ERROR. See the[ Source Health Check API Reference ](https://hasura.io/docs/latest/api-reference/source-health/)for details.

|  |  |
|---|---|
| Name |  `hasura_ source_ health`  |
| Type | Gauge |
| Labels |  `source_ name` : name of the database |


### HTTP Egress​

Total size of HTTP response bodies sent via the HTTP server excluding responses from requests to `/healthz` and `/v1/version` endpoints or any other undefined resource/endpoint (for example `/foobar` ).

|  |  |
|---|---|
| Name |  `hasura_ http_ response_ bytes_ total`  |
| Type | Counter |
| Labels | none |


### HTTP Ingress​

Total size of HTTP request bodies received via the HTTP server excluding requests to `/healthz` and `/v1/version` endpoints or any other undefined resource/endpoint (for example `/foobar` ).

|  |  |
|---|---|
| Name |  `hasura_ http_ request_ bytes_ total`  |
| Type | Counter |
| Labels | none |


### OpenTelemetry OTLP Export Metrics​

These metrics allow for monitoring the reliability and performance of OTLP
exports of telemetry data.

#### Hasura OTLP Sent Spans​

Total number of successfully exported trace spans.

|  |  |
|---|---|
| Name |  `hasura_ otel_ sent_ spans`  |
| Type | Counter |
| Labels | none |


#### Hasura OTLP Dropped Spans​

Total number of trace spans dropped due to either high trace volume that filled
the buffer, or errors during send (e.g. a timeout or error response from the
collector).

|  |  |
|---|---|
| Name |  `hasura_ otel_ dropped_ spans`  |
| Type | Counter |
| Labels |  `reason` : buffer_full|send_failed |


### What did you think of this doc?

- [ Metrics exported ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#metrics-exported)
    - [ GraphQL request metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#graphql-request-metrics)
        - [ Hasura GraphQL execution time seconds ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-graphql-execution-time-seconds)

- [ Hasura GraphQL requests total ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-graphql-requests-total)

- [ Hasura Event Triggers metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-event-triggers-metrics)
    - [ Event fetch time per batch ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#event-fetch-time-per-batch)

- [ Event invocations total ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#event-invocations-total)

- [ Event processed total ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#event-processed-total)

- [ Event processing time ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#event-processing-time)

- [ Event queue time ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#event-queue-time)

- [ Event Triggers HTTP Workers ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#event-triggers-http-workers)

- [ Event webhook processing time ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#event-webhook-processing-time)

- [ Events fetched per batch ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#events-fetched-per-batch)

- [ Subscription metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#subscription-metrics)
    - [ Active Subscriptions ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#active-subscriptions)

- [ Active Subscription Pollers ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#active-subscription-pollers)

- [ Active Subscription Pollers in Error State ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#active-subscription-pollers-in-error-state)

- [ Subscription Total Time ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#subscription-total-time)

- [ Subscription Database Execution Time ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#subscription-database-execution-time)

- [ WebSocket Egress ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#websocket-egress)

- [ WebSocket Ingress ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#websocket-ingress)

- [ Websocket Message Queue Time ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#websocket-message-queue-time)

- [ Websocket Message Write Time ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#websocket-message-write-time)

- [ Cache metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#cache-metrics)
    - [ Hasura cache request count ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-cache-request-count)

- [ Cron trigger metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#cron-trigger-metrics)
    - [ Hasura cron events invocation total ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-cron-events-invocation-total)

- [ Hasura cron events processed total ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-cron-events-processed-total)

- [ One-off Scheduled events metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#one-off-scheduled-events-metrics)
    - [ Hasura one-off events invocation total ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-one-off-events-invocation-total)

- [ Hasura one-off events processed total ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-one-off-events-processed-total)

- [ Hasura HTTP connections ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-http-connections)

- [ Hasura WebSocket connections ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-websocket-connections)

- [ Hasura Postgres connections ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-postgres-connections)

- [ Hasura Postgres Connection Initialization Time ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-postgres-connection-initialization-time)

- [ Hasura Postgres Pool Wait Time ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-postgres-pool-wait-time)

- [ Hasura source health ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-source-health)

- [ HTTP Egress ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#http-egress)

- [ HTTP Ingress ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#http-ingress)

- [ OpenTelemetry OTLP Export Metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#opentelemetry-otlp-export-metrics)
    - [ Hasura OTLP Sent Spans ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-otlp-sent-spans)

- [ Hasura OTLP Dropped Spans ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-otlp-dropped-spans)

- [ GraphQL request metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#graphql-request-metrics)
    - [ Hasura GraphQL execution time seconds ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-graphql-execution-time-seconds)

- [ Hasura Event Triggers metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-event-triggers-metrics)
    - [ Event fetch time per batch ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#event-fetch-time-per-batch)

- [ Subscription metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#subscription-metrics)
    - [ Active Subscriptions ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#active-subscriptions)

- [ Cron trigger metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#cron-trigger-metrics)
    - [ Hasura cron events invocation total ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-cron-events-invocation-total)

- [ One-off Scheduled events metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#one-off-scheduled-events-metrics)
    - [ Hasura one-off events invocation total ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-one-off-events-invocation-total)

- [ OpenTelemetry OTLP Export Metrics ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#opentelemetry-otlp-export-metrics)
    - [ Hasura OTLP Sent Spans ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/metrics/#event-processed-total/#hasura-otlp-sent-spans)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)