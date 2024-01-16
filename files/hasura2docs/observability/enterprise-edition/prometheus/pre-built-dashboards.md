# Pre-built Dashboards

## Grafana Dashboards​

You can download dashboards on the[ Hasura organization ](https://grafana.com/orgs/hasurahq)page on Grafana Cloud, or
from the demo repository below.

## Demo​

### Introduction​

If you're running Hasura EE yourself, you have metrics available over a Prometheus endpoint, Traces available over
OpenTelemetry and Logs available over stdout. We have set up a[ boilerplate folder ](https://github.com/hasura/graphql-engine/tree/master/community/boilerplates/observability/enterprise)where we have configured Hasura along with:

- Prometheus for metrics collector.
- Jaeger for Traces collector.
- Alert Manager and regular alert rules.
- Node Exporter for system metrics.
- Blackbox Exporter for HTTP health checks.
- Grafana with a few sample dashboards.
- Loki and Promtail for logging collector.
- Hasura migrations, metadata examples and enterprise enabled services (Caching, Read Replicas, Data Connectors).


Image: [ Hasura Overview Dashboard ](https://hasura.io/docs/assets/images/grafana-overview-dashboard-759a66cf0a704891fed8a86c57c4799c.png)

The repository helps you quickly start and explore the latest observability feature updates, dashboards, and alert
templates for monitoring in production.

### Get Started​

Clone the repository to your local machine, copy the sample environment file `dotenv` to `.env` , and edit the enterprise
license key ( `HGE_EE_LICENSE_KEY` ) and secrets. The demo uses[ Docker Compose ](https://docs.docker.com/compose/)to
setup container services.

```
git  clone https://github.com/hasura/ee-observability-demo.git
cd  ee-observability-demo
cp  dotenv .env
docker-compose  up -d
```

Explore Grafana Dashboards on `http://localhost:3000` .

### What did you think of this doc?

- [ Grafana Dashboards ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/pre-built-dashboards/#grafana-dashboards)
- [ Demo ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/pre-built-dashboards/#demo)
    - [ Introduction ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/pre-built-dashboards/#introduction)

- [ Get Started ](https://hasura.io/docs/latest/observability/enterprise-edition/prometheus/pre-built-dashboards/#get-started)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)