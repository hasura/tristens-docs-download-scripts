# Hasura Data Connectors Developer's Guide

# Filtering

The next step is to filter the rows based on the provided predicate expression:

```
let
filtered:
Vec
<Row> = (
match
&query.predicate {
None
=>
Ok
(sorted),
Some
(expr) => {
let
mut
filtered:
Vec
<Row> =
vec!
[];
for
item
in
sorted.into_iter() {
let
root =
match
root {
                    Root::CurrentRow => &item,
                    Root::ExplicitRow(root) => root,
                };
if
eval_expression(
                    collection_relationships,
                    variables,
                    state,
                    expr,
                    root,
                    &item,
                )? {
                    filtered.push(item);
                }
            }
Ok
(filtered)
        }
    })?;
```

As we can see, the function delegates to the `eval_expression` function in order to evaluate the predicate on each row.

## Evaluating expressions

The `eval_expression` function evaluates a predicate by pattern matching on the type of the expression `expr` , and returns a boolean value indicating whether the current row matches the predicate:

```
fn   eval_expression
(
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
    variables: &BTreeMap<
String
, serde_json::Value>,
    state: &AppState,
    expr: &models::Expression,
    root: &Row,
    item: &Row,
) ->
Result
<
bool
> {
```

### Logical expressions

The first category of expression types are the *logical expressions* - *and* (conjunction), *or* (disjunction) and *not* (negation) - whose evaluators are straightforward:

- To evaluate a conjunction/disjunction of subexpressions, we evaluate all of the subexpressions to booleans, and find the conjunction/disjunction of those boolean values respectively.
- To evaluate the negation of a subexpression, we evaluate the subexpression to a boolean value, and negate the boolean.


```
match
expr {
        models::Expression::And { expressions } => {
for
expr
in
expressions.iter() {
if
!eval_expression(collection_relationships, variables, state, expr, root, item)? {
return
Ok
(
false
);
                }
            }
Ok
(
true
)
        }
        models::Expression::Or { expressions } => {
for
expr
in
expressions.iter() {
if
eval_expression(collection_relationships, variables, state, expr, root, item)? {
return
Ok
(
true
);
                }
            }
Ok
(
false
)
        }
        models::Expression::Not { expression } => {
let
b = eval_expression(
                collection_relationships,
                variables,
                state,
                expression,
                root,
                item,
            )?;
Ok
(!b)
        }
```

### Unary Operators

The next category of expressions are the *unary operators* . The only unary operator is the `IsNull` operator, which is evaluated by evaluating the operator's *comparison target* , and then comparing the result to `null` :

```
models::Expression::UnaryComparisonOperator { column, operator } =>
match
operator {
            models::UnaryComparisonOperator::IsNull => {
let
vals = eval_comparison_target(
                    collection_relationships,
                    variables,
                    state,
                    column,
                    root,
                    item,
                )?;
Ok
(vals.iter().any(|val| val.is_null()))
            }
        },
```

To evaluate the comparison target, we delegate to the `eval_comparison_target` function, which pattern matches:

- A column is evaluated using the `eval_path` function, which we will cover when we talk about[ relationships ](./relationships.html).
- A *root collection* column (that is, a column from the *root collection* , or collection used by the nearest enclosing[ Query ](../../../reference/types.html#query)) is evaluated using `eval_column` . You may have noticed the additional argument, `root` , which has been passed down through every function call so far - this is to track the root collection for exactly this case.


```
fn   eval_comparison_target
(
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
    variables: &BTreeMap<
String
, serde_json::Value>,
    state: &AppState,
    target: &models::ComparisonTarget,
    root: &Row,
    item: &Row,
) ->
Result
<
Vec
<serde_json::Value>> {
match
target {
        models::ComparisonTarget::Column { name, path } => {
let
rows = eval_path(collection_relationships, variables, state, path, item)?;
let
mut
values =
vec!
[];
for
row
in
rows.iter() {
let
value = eval_column(row, name.as_str())?;
                values.push(value);
            }
Ok
(values)
        }
        models::ComparisonTarget::RootCollectionColumn { name } => {
let
value = eval_column(root, name.as_str())?;
Ok
(
vec!
[value])
        }
    }
}
```

### Binary Operators

The next category of expressions are the *binary operators* . Binary operators can be *standard* or *custom* .

The only standard binary operators are the `equal` and `in` operators.

 `equal` evaluated by evaluating its *comparison target* and *comparison value* , and comparing them for equality:

```
models::Expression::BinaryComparisonOperator {
            column,
            operator,
            value,
        } =>
match
operator {
            models::BinaryComparisonOperator::Equal => {
let
left_vals = eval_comparison_target(
                    collection_relationships,
                    variables,
                    state,
                    column,
                    root,
                    item,
                )?;
let
right_vals = eval_comparison_value(
                    collection_relationships,
                    variables,
                    state,
                    value,
                    root,
                    item,
                )?;
for
left_val
in
left_vals.iter() {
for
right_val
in
right_vals.iter() {
if
left_val == right_val {
return
Ok
(
true
);
                        }
                    }
                }
Ok
(
false
)
            }
```

The `in` operator is evaluated by evaluating its comparison target, and all of its comparison values, and testing whether the evaluated target appears in the list of evaluated values:

```
models::Expression::BinaryArrayComparisonOperator {
            column,
            operator,
            values,
        } =>
match
operator {
            models::BinaryArrayComparisonOperator::In => {
let
left_vals = eval_comparison_target(
                    collection_relationships,
                    variables,
                    state,
                    column,
                    root,
                    item,
                )?;
for
comparison_value
in
values.iter() {
let
right_vals = eval_comparison_value(
                        collection_relationships,
                        variables,
                        state,
                        comparison_value,
                        root,
                        item,
                    )?;
for
left_val
in
left_vals.iter() {
for
right_val
in
right_vals.iter() {
if
left_val == right_val {
return
Ok
(
true
);
                            }
                        }
                    }
                }
Ok
(
false
)
            }
        },
```

The reference implementation provides a single custom binary operator as an example, which is the `like` operator on strings:

```
models::BinaryComparisonOperator::Other { name } =>
match
name.as_str() {
"like"
=> {
let
column_vals = eval_comparison_target(
                        collection_relationships,
                        variables,
                        state,
                        column,
                        root,
                        item,
                    )?;
let
regex_vals = eval_comparison_value(
                        collection_relationships,
                        variables,
                        state,
                        value,
                        root,
                        item,
                    )?;
for
column_val
in
column_vals.iter() {
for
regex_val
in
regex_vals.iter() {
let
column_str = column_val.as_str().ok_or((
                                StatusCode::BAD_REQUEST,
                                Json(models::ErrorResponse {
                                    message:
"column is not a string"
.into(),
                                    details: serde_json::Value::Null,
                                }),
                            ))?;
let
regex_str = regex_val.as_str().ok_or((
                                StatusCode::BAD_REQUEST,
                                Json(models::ErrorResponse {
                                    message:
" "
.into(),
                                    details: serde_json::Value::Null,
                                }),
                            ))?;
let
regex = Regex::new(regex_str).map_err(|_| {
                                (
                                    StatusCode::BAD_REQUEST,
                                    Json(models::ErrorResponse {
                                        message:
"invalid regular expression"
.into(),
                                        details: serde_json::Value::Null,
                                    }),
                                )
                            })?;
if
regex.is_match(column_str) {
return
Ok
(
true
);
                            }
                        }
                    }
Ok
(
false
)
                }
                _ =>
Err
((
                    StatusCode::BAD_REQUEST,
                    Json(models::ErrorResponse {
                        message:
" "
.into(),
                        details: serde_json::Value::Null,
                    }),
                )),
            },
```

### EXISTS expressions

An `EXISTS` expression is evaluated by recursively evaluating a `Query` on a related collection, and testing to see whether the resulting `RowSet` contains any rows:

```
models::Expression::Exists {
            in_collection,
            predicate,
        } => {
let
query = models::Query {
                aggregates:
None
,
                fields:
Some
(IndexMap::new()),
                limit:
None
,
                offset:
None
,
                order_by:
None
,
                predicate:
Some
(*predicate.clone()),
            };
let
collection = eval_in_collection(
                collection_relationships,
                item,
                variables,
                state,
                in_collection,
            )?;
let
row_set = execute_query(
                collection_relationships,
                variables,
                state,
                &query,
                Root::ExplicitRow(root),
                collection,
            )?;
let
rows:
Vec
<IndexMap<_, _>> = row_set.rows.ok_or((
                StatusCode::INTERNAL_SERVER_ERROR,
                Json(models::ErrorResponse {
                    message:
" "
.into(),
                    details: serde_json::Value::Null,
                }),
            ))?;
Ok
(!rows.is_empty())
```