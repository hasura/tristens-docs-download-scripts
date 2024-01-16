# Hasura Data Connectors Developer's Guide

# Executing Queries

In this section, we will break down the implementation of the `execute_query` function:

```
fn   execute_query
(
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
    variables: &BTreeMap<
String
, serde_json::Value>,
    state: &AppState,
    query: &models::Query,
    root: Root,
    collection:
Vec
<Row>,
) ->
Result
<models::RowSet> {
```

At this point, we have already computed the full collection, which is passed via the `collection` argument. Now, we need to evaluate the[ Query ](../../../reference/types.html#query)in the context of this collection.

The `Query` describes the predicate which should be applied to all rows, the sort order, pagination options, along with any aggregates to compute and fields to return.

The first step is to sort the collection.

 *Note* : we could also start by filtering, and then sort the filtered rows. Which is more efficient depends on the data and the query, and choosing between these approaches would be the job of a *query planner* in a real database engine. However, this is out of scope here, so we make an arbitrary choice, and sort the data first.