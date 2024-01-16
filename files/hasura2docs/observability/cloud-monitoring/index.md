# Built-in Monitoring in Hasura Cloud

## Introduction​

Observability is a critical aspect of any application, and Hasura Cloud provides developers with a powerful set of tools
to monitor and debug their applications. In this document, we'll explore the observability features available in Hasura
Cloud and how they can help you build better applications.

## Alerts​

Hasura Cloud provides[ alerts ](https://hasura.io/docs/latest/observability/cloud-monitoring/alerting/)that can be used to notify you when
certain events occur in your application. These can be configured to send notifications via email, Slack, or other
channels, allowing you to stay informed about the health of your application.

## Error Reporting​

Hasura Cloud provides detailed[ error reporting ](https://hasura.io/docs/latest/observability/cloud-monitoring/errors/)for GraphQL queries and mutations. Whenever an error
occurs, Hasura Cloud captures the error message, query, and other relevant information, allowing you to quickly identify
and fix the issue. This feature is particularly useful when debugging complex GraphQL queries and mutations.

## Usage Summaries​

Hasura Cloud provides[ usage summaries ](https://hasura.io/docs/latest/observability/cloud-monitoring/usage/)for your GraphQL operations, allowing you to monitor the performance
of your application and identify any performance bottlenecks. The usage summaries can be filtered by time range,
operation type, and other parameters, making it easy to pinpoint performance issues.

## GraphQL Operations​

Hasura Cloud provides detailed metrics for your[ GraphQL operations ](https://hasura.io/docs/latest/observability/cloud-monitoring/operations/), including query latency, request
count, and error rate. This information can be used to monitor the performance of your application and identify any
issues that may be impacting your users.

## Websockets​

Hasura Cloud supports[ WebSockets ](https://hasura.io/docs/latest/observability/cloud-monitoring/websockets/), allowing you to build real-time applications that can push data
updates to the client in real-time without having to continuously poll the server. Hasura Cloud provides detailed
metrics for your WebSocket connections, including connection count, message count, and error rate.

## Subscription Workers​

Hasura Cloud provides[ subscription workers ](https://hasura.io/docs/latest/observability/cloud-monitoring/subscription-workers/)that can be used to process subscriptions and
deliver real-time updates to your clients. The subscription workers are fully managed and can be scaled up or down based
on your application's needs.

## Distributed Tracing​

Hasura Cloud provides[ distributed tracing ](https://hasura.io/docs/latest/observability/cloud-monitoring/tracing/)capabilities, allowing you to
trace requests across multiple services and identify any performance bottlenecks. The tracing information can be used to
optimize your application's performance and ensure that it is running smoothly.

## Query Tags​

Hasura Cloud provides[ query tags ](https://hasura.io/docs/latest/observability/query-tags/), which can be used to tag your GraphQL queries and
mutations with metadata. This metadata can be used to filter and group your usage summaries and metrics, making it easy
to identify trends and patterns in your application's usage.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/observability/cloud-monitoring/index/#introduction)
- [ Alerts ](https://hasura.io/docs/latest/observability/cloud-monitoring/index/#alerts)
- [ Error Reporting ](https://hasura.io/docs/latest/observability/cloud-monitoring/index/#error-reporting)
- [ Usage Summaries ](https://hasura.io/docs/latest/observability/cloud-monitoring/index/#usage-summaries)
- [ GraphQL Operations ](https://hasura.io/docs/latest/observability/cloud-monitoring/index/#graphql-operations)
- [ Websockets ](https://hasura.io/docs/latest/observability/cloud-monitoring/index/#websockets)
- [ Subscription Workers ](https://hasura.io/docs/latest/observability/cloud-monitoring/index/#subscription-workers)
- [ Distributed Tracing ](https://hasura.io/docs/latest/observability/cloud-monitoring/index/#distributed-tracing)
- [ Query Tags ](https://hasura.io/docs/latest/observability/cloud-monitoring/index/#query-tags)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)