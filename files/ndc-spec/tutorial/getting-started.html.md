# Hasura Data Connectors Developer's Guide

# Getting Started

The reference implementation will serve queries and mutations based on in-memory data read from CSV files.

First, we will define some types to represent the data in the CSV files. Rows of CSV data will be stored in memory as ordered maps:

```
type   Row
= BTreeMap<
String
, serde_json::Value>;
```

Our application state will consist of collections of various types of rows:

```
#[derive(Debug, Clone)]
pub
struct   AppState
{
pub
articles: BTreeMap<
i64
, Row>,
pub
authors: BTreeMap<
i64
, Row>,
pub
metrics: Metrics,
}
```

In our `main` function, the data connector reads the initial data from the CSV files, and creates the `AppState` :

```
fn   init_app_state
() -> AppState {
// Read the CSV data files
let
articles = read_csv(
"articles.csv"
).unwrap();
let
authors = read_csv(
"authors.csv"
).unwrap();
let
metrics = Metrics::new().unwrap();

    AppState {
        articles,
        authors,
        metrics,
    }
}
```

Finally, we start a web server with the endpoints which are required by this specification:

```
#[tokio::main]
async
fn   main
() {
let
app_state = Arc::new(Mutex::new(init_app_state()));
let
app = Router::new()
        .route(
"/healthz"
, get(get_healthz))
        .route(
"/metrics"
, get(get_metrics))
        .route(
"/capabilities"
, get(get_capabilities))
        .route(
"/schema"
, get(get_schema))
        .route(
"/query"
, post(post_query))
        .route(
"/mutation"
, post(post_mutation))
        .route(
"/explain"
, post(post_explain))
        .layer(axum::middleware::from_fn_with_state(
            app_state.clone(),
            metrics_middleware,
        ))
        .with_state(app_state);
// run it with hyper on localhost:8100
axum::Server::bind(&
"0.0.0.0:8100"
.parse().unwrap())
        .serve(app.into_make_service())
        .
await
.unwrap();
}
```

 *Note* : the application state is stored in an `Arc<Mutex<_>>` , so that we can perform locking reads and writes in multiple threads.

In the next chapters, we will look at the implementation of each of these endpoints in turn.