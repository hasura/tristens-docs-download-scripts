# Hasura Data Connectors Developer's Guide

# Query Variables

The first step in `post_query` is to reduce the problem from a query with multiple sets of[ query variables ](../../specification/queries/variables.html)to only a single set.

The `post_query` function iterates over all variable sets, and for each one, produces a[ RowSet ](../../reference/types.html#rowset)of rows corresponding to that set of variables. Each `RowSet` is then added to the final `QueryResponse` :

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
let
state = state.lock().
await
;
let
variable_sets = request.variables.unwrap_or(
vec!
[BTreeMap::new()]);
let
mut
row_sets =
vec!
[];
for
variables
in
variable_sets.iter() {
let
row_set = execute_query_with_variables(
            &request.collection,
            &request.arguments,
            &request.collection_relationships,
            &request.query,
            variables,
            &state,
        )?;
        row_sets.push(row_set);
    }
Ok
(Json(models::QueryResponse(row_sets)))
}
```

In order to compute the `RowSet` for a given set of variables, the function delegates to a function named `execute_query_with_variables` :

```
fn   execute_query_with_variables
(
    collection: &
str
,
    arguments: &BTreeMap<
String
, models::Argument>,
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
    query: &models::Query,
    variables: &BTreeMap<
String
, serde_json::Value>,
    state: &AppState,
) ->
Result
<models::RowSet> {
```

In the next section, we will break down the implementation of this function.