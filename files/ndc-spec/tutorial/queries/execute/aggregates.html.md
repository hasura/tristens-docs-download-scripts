# Hasura Data Connectors Developer's Guide

# Aggregates

Now that we have computed the sorted, filtered, and paginated rows of the original collection, we can compute any aggregates over those rows.

Each aggregate is computed in turn by the `eval_aggregate` function, and added to the list of all aggregates to return:

```
let
aggregates = query
        .aggregates
        .as_ref()
        .map(|aggregates| {
let
mut
row: IndexMap<
String
, serde_json::Value> = IndexMap::new();
for
(aggregate_name, aggregate)
in
aggregates.iter() {
                row.insert(
                    aggregate_name.clone(),
                    eval_aggregate(aggregate, &paginated)?,
                );
            }
Ok
(row)
        })
        .transpose()?;
```

The `eval_aggregate` function works by pattern matching on the type of the aggregate being computed:

- A `star_count` aggregate simply counts all rows,
- A `column_count` aggregate computes the subset of rows where the named column is non-null, and returns the count of only those rows,
- A `single_column` aggregate is computed by delegating to the `eval_aggregate_function` function, which computes a custom aggregate operator over the values of the selected column taken from all rows.


```
fn   eval_aggregate
(
    aggregate: &models::Aggregate,
    paginated: &
Vec
<BTreeMap<
String
, serde_json::Value>>,
) ->
Result
<serde_json::Value> {
match
aggregate {
        models::Aggregate::StarCount {} =>
Ok
(serde_json::Value::from(paginated.len())),
        models::Aggregate::ColumnCount { column, distinct } => {
let
values = paginated
                .iter()
                .map(|row| {
                    row.get(column).ok_or((
                        StatusCode::BAD_REQUEST,
                        Json(models::ErrorResponse {
                            message:
"invalid column name"
.into(),
                            details: serde_json::Value::Null,
                        }),
                    ))
                })
                .collect::<
Result
<
Vec
<_>>>()?;
let
non_null_values = values.iter().filter(|value| !value.is_null());
let
agg_value =
if
*distinct {
                non_null_values
                    .map(|value| {
                        serde_json::to_string(value).map_err(|_| {
                            (
                                StatusCode::INTERNAL_SERVER_ERROR,
                                Json(models::ErrorResponse {
                                    message:
"unable to encode value"
.into(),
                                    details: serde_json::Value::Null,
                                }),
                            )
                        })
                    })
                    .collect::<
Result
<HashSet<_>>>()?
                    .len()
            }
else
{
                non_null_values.count()
            };
            serde_json::to_value(agg_value).map_err(|_| {
                (
                    StatusCode::INTERNAL_SERVER_ERROR,
                    Json(models::ErrorResponse {
                        message:
" "
.into(),
                        details: serde_json::Value::Null,
                    }),
                )
            })
        }
        models::Aggregate::SingleColumn { column, function } => {
let
values = paginated
                .iter()
                .map(|row| {
                    row.get(column).ok_or((
                        StatusCode::BAD_REQUEST,
                        Json(models::ErrorResponse {
                            message:
"invalid column name"
.into(),
                            details: serde_json::Value::Null,
                        }),
                    ))
                })
                .collect::<
Result
<
Vec
<_>>>()?;
            eval_aggregate_function(function, values)
        }
    }
}
```

The `eval_aggregate_function` function implements the custom aggregate operators `min` and `max` , which are provided for integer-valued columns:

```
fn   eval_aggregate_function
(
    function: &
str
,
    values:
Vec
<&serde_json::Value>,
) ->
Result
<serde_json::Value> {
let
int_values = values
        .iter()
        .map(|value| {
            value.as_i64().ok_or((
                StatusCode::BAD_REQUEST,
                Json(models::ErrorResponse {
                    message:
"column is not an integer"
.into(),
                    details: serde_json::Value::Null,
                }),
            ))
        })
        .collect::<
Result
<
Vec
<_>>>()?;
let
agg_value =
match
function {
"min"
=>
Ok
(int_values.iter().min()),
"max"
=>
Ok
(int_values.iter().max()),
        _ =>
Err
((
            StatusCode::BAD_REQUEST,
            Json(models::ErrorResponse {
                message:
"invalid aggregation function"
.into(),
                details: serde_json::Value::Null,
            }),
        )),
    }?;
    serde_json::to_value(agg_value).map_err(|_| {
        (
            StatusCode::INTERNAL_SERVER_ERROR,
            Json(models::ErrorResponse {
                message:
" "
.into(),
                details: serde_json::Value::Null,
            }),
        )
    })
}
```