# Hasura Data Connectors Developer's Guide

# Relationships

Relationships appear in many places in the[ QueryRequest ](../../../reference/types.html#queryrequest), but are always computed using the `eval_path` function.

 `eval_path` accepts a list of[ PathElement ](../../../reference/types.html#pathelement)s, each of which describes the traversal of a single edge of the collection-relationship graph. `eval_path` computes the collection at the final node of this path through the graph.

It does this by successively evaluating each edge in turn using the `eval_path_element` function:

```
fn   eval_path
(
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
    variables: &BTreeMap<
String
, serde_json::Value>,
    state: &AppState,
    path: &[models::PathElement],
    item: &Row,
) ->
Result
<
Vec
<Row>> {
let
mut
result:
Vec
<Row> =
vec!
[item.clone()];
for
path_element
in
path.iter() {
let
relationship_name = path_element.relationship.as_str();
let
relationship = collection_relationships.get(relationship_name).ok_or((
            StatusCode::BAD_REQUEST,
            Json(models::ErrorResponse {
                message:
"invalid relationship name in path"
.into(),
                details: serde_json::Value::Null,
            }),
        ))?;
        result = eval_path_element(
            collection_relationships,
            variables,
            state,
            relationship,
            &path_element.arguments,
            &result,
            &path_element.predicate,
        )?;
    }
Ok
(result)
}
```

The `eval_path_element` function computes a collection from a single relationship, one source row at a time, by evaluating all relationship arguments, computing the target collection using `get_collection_by_name` , and evaluating any column mapping on any resulting rows:

```
fn   eval_path_element
(
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
    variables: &BTreeMap<
String
, serde_json::Value>,
    state: &AppState,
    relationship: &models::Relationship,
    arguments: &BTreeMap<
String
, models::RelationshipArgument>,
    source: &[Row],
    predicate: &models::Expression,
) ->
Result
<
Vec
<Row>> {
let
mut
matching_rows:
Vec
<Row> =
vec!
[];
// Note: Join strategy
//
// Rows can be related in two ways: 1) via a column mapping, and
// 2) via collection arguments. Because collection arguments can be computed
// using the columns on the source side of a relationship, in general
// we need to compute the target collection once for each source row.
// This join strategy can result in some target rows appearing in the
// resulting row set more than once, if two source rows are both related
// to the same target row.
//
// In practice, this is not an issue, either because a) the relationship
// is computed in the course of evaluating a predicate, and all predicates are
// implicitly or explicitly existentially quantified, or b) if the
// relationship is computed in the course of evaluating an ordering, the path
// should consist of all object relationships, and possibly terminated by a
// single array relationship, so there should be no double counting.
for
src_row
in
source.iter() {
let
mut
all_arguments = BTreeMap::new();
for
(argument_name, argument_value)
in
relationship.arguments.iter() {
if
all_arguments
                .insert(
                    argument_name.clone(),
                    eval_relationship_argument(variables, src_row, argument_value)?,
                )
                .is_some()
            {
return
Err
((
                    StatusCode::BAD_REQUEST,
                    Json(models::ErrorResponse {
                        message:
"duplicate argument names"
.into(),
                        details: serde_json::Value::Null,
                    }),
                ));
            }
        }
for
(argument_name, argument_value)
in
arguments.iter() {
if
all_arguments
                .insert(
                    argument_name.clone(),
                    eval_relationship_argument(variables, src_row, argument_value)?,
                )
                .is_some()
            {
return
Err
((
                    StatusCode::BAD_REQUEST,
                    Json(models::ErrorResponse {
                        message:
"duplicate argument names"
.into(),
                        details: serde_json::Value::Null,
                    }),
                ));
            }
        }
let
target = get_collection_by_name(
            relationship.target_collection.as_str(),
            &all_arguments,
            state,
        )?;
for
tgt_row
in
target.iter() {
if
eval_column_mapping(relationship, src_row, tgt_row)?
                && eval_expression(
                    collection_relationships,
                    variables,
                    state,
                    predicate,
                    tgt_row,
                    tgt_row,
                )?
            {
                matching_rows.push(tgt_row.clone());
            }
        }
    }
Ok
(matching_rows)
}
```