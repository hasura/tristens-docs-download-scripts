# Hasura Data Connectors Developer's Guide

# Mutations

In this section, we will break down the implementation of the `/mutation` endpoint.

The mutation endpoint is handled by the `post_mutation` function:

```
async
fn   post_mutation
(
    State(state): State<Arc<Mutex<AppState>>>,
    Json(request): Json<models::MutationRequest>,
) ->
Result
<Json<models::MutationResponse>> {
```

This function receives the application state, and the[ MutationRequest ](../../reference/types.html#mutationrequest)structure.

The function iterates over the collection of requested[ MutationOperation ](../../reference/types.html#mutationoperation)structures, and handles each one in turn, adding each result to the `operation_results` field in the response:

```
let
mut
state = state.lock().
await
;
let
mut
operation_results =
vec!
[];
for
operation
in
request.operations.iter() {
let
operation_result =
            execute_mutation_operation(&
mut
state, &request.collection_relationships, operation)?;
        operation_results.push(operation_result);
    }
Ok
(Json(models::MutationResponse { operation_results }))
}
```

The `execute_mutation_operation` function is responsible for executing an individual operation. In the next section, we'll break that function down.