# Hasura Data Connectors Developer's Guide

# Sorting

The first step is to sort the rows in the full collection:

```
let
sorted = sort(
        collection_relationships,
        variables,
        state,
        collection,
        &query.order_by,
    )?;
```

The[ Query ](../../../reference/types.html#query)object defines the sort order in terms of a list of[ OrderByElement ](../../../reference/types.html#orderbyelement)s. See the[ sorting specification ](../../../specification/queries/sorting.html)for details on how this ought to be interpreted.

## The sort function

The `sort` function implements a simple insertion sort, computing the ordering for each pair of rows, and inserting each row at the correct place:

```
fn   sort
(
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
    variables: &BTreeMap<
String
, serde_json::Value>,
    state: &AppState,
    collection:
Vec
<Row>,
    order_by: &
Option
<models::OrderBy>,
) ->
Result
<
Vec
<Row>> {
match
order_by {
None
=>
Ok
(collection),
Some
(order_by) => {
let
mut
copy =
vec!
[];
for
item_to_insert
in
collection.into_iter() {
let
mut
index =
0
;
for
other
in
copy.iter() {
if
let
Ordering::Greater = eval_order_by(
                        collection_relationships,
                        variables,
                        state,
                        order_by,
                        other,
                        &item_to_insert,
                    )? {
break
;
                    }
else
{
                        index +=
1
;
                    }
                }
                copy.insert(index, item_to_insert);
            }
Ok
(copy)
        }
    }
}
```

 `sort` delegates to the `eval_order_by` function to compute the ordering between two rows:

## Evaluating the Ordering

To compare two rows, the `eval_order_by` computes each `OrderByElement` in turn, and compares the rows in order, or in reverse order, depending on whether the ordering is *ascending* or *descending* .

The function returns the first `Ordering` which makes the two rows distinct (if any):

```
fn   eval_order_by
(
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
    variables: &BTreeMap<
String
, serde_json::Value>,
    state: &AppState,
    order_by: &models::OrderBy,
    t1: &Row,
    t2: &Row,
) ->
Result
<Ordering> {
let
mut
result = Ordering::Equal;
for
element
in
order_by.elements.iter() {
let
v1 = eval_order_by_element(collection_relationships, variables, state, element, t1)?;
let
v2 = eval_order_by_element(collection_relationships, variables, state, element, t2)?;
let
x =
match
element.order_direction {
            models::OrderDirection::Asc => compare(v1, v2)?,
            models::OrderDirection::Desc => compare(v2, v1)?,
        };
        result = result.then(x);
    }
Ok
(result)
}
```

The ordering for a single `OrderByElement` is computed by the `eval_order_by_element` function.

We won't cover every branch of this function in detail here, but it works by pattern matching on the type of ordering being used.

### Ordering by a column

As an example, here is the function `eval_order_by_column` which evaluates *ordering by a column* :

```
fn   eval_order_by_column
(
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
    variables: &BTreeMap<
String
, serde_json::Value>,
    state: &AppState,
    item: &BTreeMap<
String
, serde_json::Value>,
    path:
Vec
<models::PathElement>,
    name:
String
,
) ->
Result
<serde_json::Value> {
let
rows:
Vec
<Row> = eval_path(collection_relationships, variables, state, &path, item)?;
if
rows.len() >
1
{
return
Err
((
            StatusCode::BAD_REQUEST,
            Json(models::ErrorResponse {
                message:
" "
.into(),
                details: serde_json::Value::Null,
            }),
        ));
    }
match
rows.first() {
Some
(row) => eval_column(row, name.as_str()),
None
=>
Ok
(serde_json::Value::Null),
    }
}
```

This code computes the target table, possibly by traversing relationships using `eval_path` (we will cover this function later when we cover relationships), and validates that we computed a single row before selecting the value of the chosen column.

Now that we have sorted the full collection, we can apply the predicate to filter down the collection of rows. We will cover this in the next section.