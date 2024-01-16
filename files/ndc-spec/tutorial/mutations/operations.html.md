# Hasura Data Connectors Developer's Guide

# Handling Operations

The `execute_mutation_operation` function is responsible for handling a single[ MutationOperation ](../../reference/types.html#mutationoperation), and returning the corresponding[ MutationOperationResults ](../../reference/types.html#mutationoperationresults):

```
fn   execute_mutation_operation
(
    state: &
mut
AppState,
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
    operation: &models::MutationOperation,
) ->
Result
<models::MutationOperationResults> {
match
operation {
        models::MutationOperation::Procedure {
            name,
            arguments,
            fields,
        } => execute_procedure(state, name, arguments, fields, collection_relationships),
    }
}
```

The function matches on the type of the operation, and delegates to the appropriate function. Currently, the only type of operation is `Procedure` , so the function delegates to the `execute_procedure` function. In the next section, we will break down the implementation of that function.