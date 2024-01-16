# Hasura Data Connectors Developer's Guide

# Explain

The `/explain` endpoint is not implemented in the reference implementation, simply because tje `QueryResponse` is interpreted directly in the `/query` endpoint. There is no intermediate representation (such as SQL) which could be described as a "query plan".

The `explain` capability is turned off in the[ capabilities endpoint ](./capabilities.html), and the `/explain` endpoint throws an error:

```
async
fn   post_explain
(
    Json(_request): Json<models::QueryRequest>,
) ->
Result
<Json<models::ExplainResponse>> {
Err
((
        StatusCode::NOT_IMPLEMENTED,
        Json(models::ErrorResponse {
            message:
"explain is not supported"
.into(),
            details: serde_json::Value::Null,
        }),
    ))
}
```