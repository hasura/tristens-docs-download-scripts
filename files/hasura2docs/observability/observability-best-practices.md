# Observability Best Practices

## Introduction​

The purpose of this document is to provide an overview of some of the best practices to follow when you configure
observability for your Hasura-driven product. We will cover the fundamentals of observability and provides general
recommendations on what Hasura considers as observability best practices.

While specifics of your product or system will define your configurations, we have used Hasura Cloud, Postgres,
Prometheus and Grafana to build this guide. Wherever applicable, links are provided to the mentioned product’s
documentation.

We also provide[ pre-built Grafana Dashboards ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/pre-built-dashboards/)for you to replicate.

Image: [ Hasura Overview Dashboard ](https://hasura.io/docs/assets/images/grafana-overview-dashboard-759a66cf0a704891fed8a86c57c4799c.png)

## The basics​

### What is observability?​

The ability to gauge a system's internal conditions by looking at its outputs is known as observability. If the current
state of a system can be determined solely from information from outputs, such as sensor data, then the system is said
to be "observable.”

Without observability, it would be challenging to figure out what is wrong with the system unless you were actively
monitoring the system for issues. Observability means you can:

- Gain insights into the functionality and health of your systems, collect data, visualize them, and set up alerts for
potential problems.
- Have distributed tracing provide end-to-end visibility into actual requests and code, helping you to improve the
performance of your application.
- Audit, debug, and analyze logs from all your services, apps, and platforms at scale.


### Three pillars of observability​

The three pillars of observability are logs, metrics, and traces. Access to logs, metrics, and traces does not
automatically make systems more visible. But in combination, they are potent tools that, when properly understood, allow
the creation of observable systems.

## Observability in Hasura​

### Hasura Cloud​

Hasura Cloud projects include dashboards for observability. You will find your monitoring dashboard under the `Monitoring` tab of your Hasura Cloud project.

The following default observability options are enabled on your Hasura Cloud project:

- [ Stats Overview ](https://hasura.io/docs/latest/observability/overview/)
- [ Errors ](https://hasura.io/docs/latest/observability/cloud-monitoring/errors/)
- [ Usage Summaries ](https://hasura.io/docs/latest/observability/cloud-monitoring/usage/)
- [ Operations ](https://hasura.io/docs/latest/observability/cloud-monitoring/operations/)
- [ Websockets ](https://hasura.io/docs/latest/observability/cloud-monitoring/websockets/)
- [ Subscription Workers ](https://hasura.io/docs/latest/observability/cloud-monitoring/subscription-workers/)
- [ Distributed Tracing ](https://hasura.io/docs/latest/observability/cloud-monitoring/tracing/)
- [ Query Tags ](https://hasura.io/docs/latest/observability/query-tags/)


#### Third-party observability platforms​

If your organization has multiple applications and systems that need to be monitored, the most efficient way to do so is
via an observability platform. Hasura provides first-party integrations with multiple observability platforms and is
fully open-telemetry compliant. You can find a list of third-party observability platforms supported by Hasura[ here ](https://hasura.io/docs/latest/observability/cloud/index/).

### Hasura Enterprise (self-hosted)​

Since your Hasura Enterprise is self-hosted (on-premises or on a third-party cloud), we recommend that you enable
monitoring for your containers and pods. Your organization can make better decisions by knowing what is happening at the
cluster or host level and within the container runtime and application. This level of information allows you to make
decisions like when to scale instances, tasks and pods in or out, as well as which instance types to use.

#### Logs​

Depending on your Hasura Enterprise Edition deployment mode, you may access, export, and process logs from your
deployment using[ this ](https://hasura.io/docs/latest/deployment/logging/#log-types)document. Generally, you should configure your container logs
to be exported to your observability platform using the appropriate log drivers.

#### Metrics via Prometheus​

You can export metrics of your Hasura Enterprise project to Prometheus easily via enabling the `metrics` API. You can find
more information on this[ here ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/integrate-prometheus-grafana/).

For security reasons, the metrics endpoint should not be leaked to the internet. Or if unavoidable, the Prometheus
secret should be confidential to prevent misuse.

[ Pre-built Grafana Dashboards ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/pre-built-dashboards/)are provided to
visualize Golden signal metrics that you will love for real-time monitoring.

#### Metrics via OpenTelemetry​

Hasura Enterprise is open-telemetry compliant and can export metrics to third-party observability
platforms which support OpenTelemetry. Check out[ the OpenTelemetry page ](https://hasura.io/docs/latest/observability/opentelemetry/)for more information.

#### Distributed traces​

Hasura Enterprise also can export distributed traces via OpenTelemetry. Read more at[ here ](https://hasura.io/docs/latest/observability/opentelemetry/)for more information.

## Database observability​

Deeper insight into databases across all of your servers is provided via database monitoring. To understand the
performance and health of your databases and address problems as they develop, we have to dig deeper into:

- Historical query performance
- Host-level metrics


### Enabling observability agents in your database​

You can enable observability for your databases by installing an agent for your observability platform on your database
servers (typically from the observability tool’s marketplace). Hasura recommends the following instrumentations should
be implemented:

- System information
    - CPU Usage

- Memory
- Query Tags


[ Query Tags ](https://hasura.io/docs/latest/observability/query-tags/)are SQL comments that consist of `key=value` pairs that are appended to
generated SQL statements. When you issue a query or mutation with query tags, the generated SQL has some extra
information. Database analytics tools can use that information (metadata) to analyze DB load and track
or monitor performance.

### Using Query Tags and pganalyze​

- Refer to documentation from[ pganalyze ](https://pganalyze.com/docs)for information on how to connect your database to
the analyzer.
- Once connected to your database, test the functionality by:
    - Executing the `run console` option in pganalyze.

- Executing the `collector --test` command in the Console.
- At this point, all queries run from the GraphiQL editor or your Cloud project's Console will appear in the pganalyze
Console.
- Selecting any query from the dashboard will expand to give additional information about the execution.
- To quickly locate operations, you can use the `Request ID` that can be found from the `Metrics` dashboard on Cloud.


## Alerting and alert propagation​

Integrating your observability tools with an incident response platform (IRP) is the recommended method for alert
propagation. Integrating with an IRP allows high visibility and actionable intelligence across the entire incident
lifecycle. Most IRPs enable your organization to respond quickly to incidents, automate responses, and will allow you to
build more reliable services and platforms.

If you use Prometheus for metrics observability, you can also consider using[ Alertmanager ](https://prometheus.io/docs/alerting/latest/alertmanager/)to configure[ common alert rules ](https://github.com/hasura/graphql-engine/blob/master/community/boilerplates/observability/enterprise/prometheus/alert.rules#L22)for performance and error incidents.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/observability/observability-best-practices/#introduction)
- [ The basics ](https://hasura.io/docs/latest/observability/observability-best-practices/#the-basics)
    - [ What is observability? ](https://hasura.io/docs/latest/observability/observability-best-practices/#what-is-observability)

- [ Three pillars of observability ](https://hasura.io/docs/latest/observability/observability-best-practices/#three-pillars-of-observability)
- [ Observability in Hasura ](https://hasura.io/docs/latest/observability/observability-best-practices/#observability-in-hasura)
    - [ Hasura Cloud ](https://hasura.io/docs/latest/observability/observability-best-practices/#hasura-cloud)

- [ Hasura Enterprise (self-hosted) ](https://hasura.io/docs/latest/observability/observability-best-practices/#hasura-enterprise-self-hosted)
- [ Database observability ](https://hasura.io/docs/latest/observability/observability-best-practices/#database-observability)
    - [ Enabling observability agents in your database ](https://hasura.io/docs/latest/observability/observability-best-practices/#enabling-observability-agents-in-your-database)

- [ Using Query Tags and pganalyze ](https://hasura.io/docs/latest/observability/observability-best-practices/#using-query-tags-and-pganalyze)
- [ Alerting and alert propagation ](https://hasura.io/docs/latest/observability/observability-best-practices/#alerting-and-alert-propagation)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)