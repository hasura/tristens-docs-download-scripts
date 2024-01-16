# Monitoring

Qdrant exposes its metrics in a Prometheus format, so you can integrate them easily
with the compatible tools and monitor Qdrant with your own monitoring system. You can
use the `/metrics` endpoint and configure it as a scrape target.

Metrics endpoint:[ http://localhost:6333/metrics ](http://localhost:6333/metrics)

The integration with Qdrant is easy to[ configure ](https://prometheus.io/docs/prometheus/latest/getting_started/#configure-prometheus-to-monitor-the-sample-targets)with Prometheus and Grafana.

## Exposed metric

Each Qdrant server will expose the following metrics.

| Name | Type | Meaning |
|---|---|---|
| app_info | counter | Information about Qdrant server |
| app_status_recovery_mode | counter | If Qdrant is currently started in recovery mode |
| collections_total | gauge | Number of collections |
| collections_vector_total | gauge | Total number of vectors in all collections |
| collections_full_total | gauge | Number of full collections |
| collections_aggregated_total | gauge | Number of aggregated collections |
| rest_responses_total | counter | Total number of responses through REST API |
| rest_responses_fail_total | counter | Total number of failed responses through REST API |
| rest_responses_avg_duration_seconds | gauge | Average response duration in REST API |
| rest_responses_min_duration_seconds | gauge | Minimum response duration in REST API |
| rest_responses_max_duration_seconds | gauge | Maximum response duration in REST API |
| grpc_responses_total | counter | Total number of responses through gRPC API |
| grpc_responses_fail_total | counter | Total number of failed responses through REST API |
| grpc_responses_avg_duration_seconds | gauge | Average response duration in gRPC API |
| grpc_responses_min_duration_seconds | gauge | Minimum response duration in gRPC API |
| grpc_responses_max_duration_seconds | gauge | Maximum response duration in gRPC API |
| cluster_enabled | gauge | Whether the cluster support is enabled |


### Cluster related metrics

There are also some metrics which are exposed in distributed mode only.

| Name | Type | Meaning |
|---|---|---|
| cluster_peers_total | gauge | Total number of cluster peers |
| cluster_term | counter | Current cluster term |
| cluster_commit | counter | Index of last committed (finalized) operation cluster peer is aware of |
| cluster_pending_operations_total | gauge | Total number of pending operations for cluster peer |
| cluster_voter | gauge | Whether the cluster peer is a voter or learner |


## Kubernetes health endpoints

 *Available as of v1.5.0* 

Qdrant exposes three endpoints, namely[ /healthz ](http://localhost:6333/healthz),[ /livez ](http://localhost:6333/livez)and[ /readyz ](http://localhost:6333/readyz), to indicate the current status of the
Qdrant server.

These currently provide the most basic status response, returning HTTP 200 if
Qdrant is started and ready to be used.

Regardless of whether an[ API key ](../security#authentication)is configured,
the endpoints are always accessible.

You can read more about Kubernetes health endpoints[ here ](https://kubernetes.io/docs/reference/using-api/health-checks/).

##### Table of contents

- [ Exposed metric ](https://qdrant.tech/documentation/guides/monitoring/#exposed-metric)
    - [ Cluster related metrics ](https://qdrant.tech/documentation/guides/monitoring/#cluster-related-metrics)
- [ Kubernetes health endpoints ](https://qdrant.tech/documentation/guides/monitoring/#kubernetes-health-endpoints)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/monitoring.md)
- [ 
 Create an Issue
 ](https://github.com/qdrant/landing_page/issues/new/choose)


#### Product

- [ 
Use cases
 ](https://qdrant.tech/use-cases/)
- [ 
Solutions
 ](https://qdrant.tech/solutions/)
- [ 
Benchmarks
 ](https://qdrant.tech/benchmarks/)
- [ 
Demos
 ](https://qdrant.tech/demo/)
- [ 
Pricing
 ](https://qdrant.tech/pricing/)


#### Community

- [ 
 
Github
 ](https://github.com/qdrant/qdrant)
- [ 
 
Discord
 ](https://qdrant.to/discord)
- [ 
 
Twitter
 ](https://qdrant.to/twitter)
- [ 
 
Newsletter
 ](https://qdrant.tech/subscribe/)
- [ 
 
Contact us
 ](https://qdrant.to/contact-us)


#### Company

- [ 
Jobs
 ](https://qdrant.join.com)
- [ 
Privacy Policy
 ](https://qdrant.tech/legal/privacy-policy/)
- [ 
Terms
 ](https://qdrant.tech/legal/terms_and_conditions/)
- [ 
Impressum
 ](https://qdrant.tech/legal/impressum/)
- [ 
Credits
 ](https://qdrant.tech/legal/credits/)


#### Latest Publications

#### Combining the precision of exact keyword search with NN-based ranking

#### Qdrant 1.7.0 brought a bunch of new features. Let's take a closer look at them!

#### Qdrant 1.6 brings recommendations strategies and more flexibility to the Recommendation API.

- [  ](https://github.com/qdrant/qdrant)
- [  ](https://qdrant.to/linkedin)
- [  ](https://qdrant.to/twitter)
- [  ](https://qdrant.to/discord)
- [  ](https://www.youtube.com/channel/UC6ftm8PwH1RU_LM1jwG0LQA)


##### Thanks for using Qdrant!

Subscribe to our e-mail newsletter if you want to be updated on new features and news regarding
Qdrant.

Like what we are doing? Consider giving us a ⭐[ on Github ](https://github.com/qdrant/qdrant).

We use cookies to learn more about you. At any time you can delete or block cookies through your browser settings.