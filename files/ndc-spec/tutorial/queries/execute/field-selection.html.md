# Hasura Data Connectors Developer's Guide

# Field Selection

In addition to computing aggregates, we can also return fields selected directly from the rows themselves.

This is done by mapping over the computed rows, and using the `eval_field` function to evaluate each selected field in turn:

```
let
rows = query
        .fields
        .as_ref()
        .map(|fields| {
let
mut
rows:
Vec
<IndexMap<
String
, models::RowFieldValue>> =
vec!
[];
for
item
in
paginated.iter() {
let
mut
row = IndexMap::new();
for
(field_name, field)
in
fields.iter() {
                    row.insert(
                        field_name.clone(),
                        eval_field(collection_relationships, variables, state, field, item)?,
                    );
                }
                rows.push(row)
            }
Ok
(rows)
        })
        .transpose()?;
```

The `eval_field` function works by pattern matching on the field type:

- A `column` is selected using the `eval_column` function,
- A `relationship` field is selected by evaluating the related collection using `eval_path_element` (we will cover this in the next section), and then recursively executing a query using `execute_query` :


```
fn   eval_field
(
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
    variables: &BTreeMap<
String
, serde_json::Value>,
    state: &AppState,
    field: &models::Field,
    item: &Row,
) ->
Result
<models::RowFieldValue> {
match
field {
        models::Field::Column { column, .. } => {
Ok
(models::RowFieldValue(eval_column(item, column.as_str())?))
        }
        models::Field::Relationship {
            relationship,
            arguments,
            query,
        } => {
let
relationship = collection_relationships.get(relationship.as_str()).ok_or((
                StatusCode::BAD_REQUEST,
                Json(models::ErrorResponse {
                    message:
" "
.into(),
                    details: serde_json::Value::Null,
                }),
            ))?;
let
source =
vec!
[item.clone()];
let
collection = eval_path_element(
                collection_relationships,
                variables,
                state,
                relationship,
                arguments,
                &source,
                &models::Expression::And {
                    expressions:
vec!
[],
                },
            )?;
let
rows = execute_query(
                collection_relationships,
                variables,
                state,
                query,
                Root::CurrentRow,
                collection,
            )?;
let
rows_json = serde_json::to_value(rows).map_err(|_| {
                (
                    StatusCode::INTERNAL_SERVER_ERROR,
                    Json(models::ErrorResponse {
                        message:
"cannot encode rowset"
.into(),
                        details: serde_json::Value::Null,
                    }),
                )
            })?;
Ok
(models::RowFieldValue(rows_json))
        }
    }
}
```