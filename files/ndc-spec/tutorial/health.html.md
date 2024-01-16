# Hasura Data Connectors Developer's Guide

# Health and Metrics

## Service Health

The `/healthz` endpoint has nothing to check, because the reference implementation does not need to connect to any other services. Therefore, once the reference implementation is running, it can always report a healthy status:

```
async
fn   get_healthz
() -> StatusCode {
    StatusCode::NO_CONTENT
}
```

In practice, a connector should make sure that any upstream services can be successfully contacted, and respond accordingly.

## Metrics

The reference implementation maintains some generic access metrics in its application state:

- `metrics.total_requests` counts the number of requests ever served, and
- `metrics.active_requests` counts the number of requests *currently* being served.


The[ metrics endpoint ](../specification/metrics.html)reports these metrics using the Rust[ prometheus ](https://docs.rs/prometheus/latest/prometheus/)crate:

```
async
fn   get_metrics
(State(state): State<Arc<Mutex<AppState>>>) ->
Result
<
String
> {
let
state = state.lock().
await
;
    state.metrics.as_text().ok_or((
        StatusCode::INTERNAL_SERVER_ERROR,
        Json(models::ErrorResponse {
            message:
"cannot encode metrics"
.into(),
            details: serde_json::Value::Null,
        }),
    ))
}
```

To maintain these metrics, it uses a simple metrics middleware:

```
async
fn   metrics_middleware
<T>(
    state: State<Arc<Mutex<AppState>>>,
    request: axum::http::Request<T>,
    next: axum::middleware::Next<T>,
) -> axum::response::Response {
// Don't hold the lock to update metrics, since the
// lock doesn't protect the metrics anyway.
let
metrics = {
let
state = state.lock().
await
;
        state.metrics.clone()
    };

    metrics.total_requests.inc();
    metrics.active_requests.inc();
let
response = next.run(request).
await
;
    metrics.active_requests.dec();
    response
}
```