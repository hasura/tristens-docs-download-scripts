# Hasura Data Connectors Developer's Guide

# Queries

The reference implementation of the `/query` endpoint may seem complicated, because there is a lot of functionality packed into a single endpoint. However, we will break the implementation down into small sections, each of which should be easily understood.

We start by looking at the type signature of the `post_query` function, which is the top-level function implementing the query endpoint:

```
pub
async
fn   post_query
(
    State(state): State<Arc<Mutex<AppState>>>,
    Json(request): Json<models::QueryRequest>,
) ->
Result
<Json<models::QueryResponse>> {
```

This function accepts a[ QueryRequest ](../../reference/types.html#queryrequest)and must produce a[ QueryResponse ](../../reference/types.html#queryresponse).

In the next section, we will start to break down this problem step-by-step.