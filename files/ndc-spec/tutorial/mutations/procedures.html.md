# Hasura Data Connectors Developer's Guide

# Procedures

The `execute_procedure` function is responsible for executing a single procedure:

```
fn   execute_procedure
(
    state: &
mut
AppState,
    name: &
str
,
    arguments: &BTreeMap<
String
, serde_json::Value>,
    fields: &
Option
<IndexMap<
String
, models::Field>>,
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
) -> std::result::
Result
<models::MutationOperationResults, (StatusCode, Json<models::ErrorResponse>)>
```

The function receives the application `state` , along with the `name` of the procedure to invoke, a list of `arguments` , a list of `fields` to return, and a list of `collection_relationships` .

The function matches on the name of the procedure, and fails if the name is not recognized. Currently there is only a single implemented procedure, `upsert_article` , and the function delegates to the `execute_upsert_article` function to handle it.

```
{
match
name {
"upsert_article"
=> {
            execute_upsert_article(state, arguments, fields, collection_relationships)
        }
        _ =>
Err
((
            StatusCode::BAD_REQUEST,
            Json(models::ErrorResponse {
                message:
"unknown procedure"
.into(),
                details: serde_json::Value::Null,
            }),
        )),
    }
}
```

## upsert_article

The `execute_upsert_article` function reads the `article` argument from the `arguments` list, failing if it is not found or invalid.

It then inserts or updates that article in the application state, depending on whether or not an article with that `id` already exists or not.

Finally, it delegates to the `eval_field` function to evaluate each requested field in turn, and returns a single row and column (named `__value` ) containing the result.

 `affected_rows` contains `1` to indicate that one row of data was affected.

```
fn   execute_upsert_article
(
    state: &
mut
AppState,
    arguments: &BTreeMap<
String
, serde_json::Value>,
    fields: &
Option
<IndexMap<
String
, models::Field>>,
    collection_relationships: &BTreeMap<
String
, models::Relationship>,
) -> std::result::
Result
<models::MutationOperationResults, (StatusCode, Json<models::ErrorResponse>)>
{
let
article = arguments.get(
"article"
).ok_or((
        StatusCode::BAD_REQUEST,
        Json(models::ErrorResponse {
            message:
" "
.into(),
            details: serde_json::Value::Null,
        }),
    ))?;
let
article_obj = article.as_object().ok_or((
        StatusCode::BAD_REQUEST,
        Json(models::ErrorResponse {
            message:
" "
.into(),
            details: serde_json::Value::Null,
        }),
    ))?;
let
id = article_obj.get(
"id"
).ok_or((
        StatusCode::BAD_REQUEST,
        Json(models::ErrorResponse {
            message:
" "
.into(),
            details: serde_json::Value::Null,
        }),
    ))?;
let
id_int = id.as_i64().ok_or((
        StatusCode::BAD_REQUEST,
        Json(models::ErrorResponse {
            message:
" "
.into(),
            details: serde_json::Value::Null,
        }),
    ))?;
let
new_row = BTreeMap::from_iter(article_obj.iter().map(|(k, v)| (k.clone(), v.clone())));
let
old_row = state.articles.insert(id_int, new_row);
let
returning = old_row
        .map(|old_row| {
let
mut
row = IndexMap::new();
for
fields
in
fields.iter() {
for
(field_name, field)
in
fields.iter() {
                    row.insert(
                        field_name.clone(),
                        eval_field(
                            collection_relationships,
                            &BTreeMap::new(),
                            state,
                            field,
                            &old_row,
                        )?,
                    );
                }
            }
Ok
(row)
        })
        .transpose()?;
Ok
(models::MutationOperationResults {
        affected_rows:
1
,
        returning:
Some
(
vec!
[IndexMap::from_iter([(
"__value"
.into(),
            models::RowFieldValue(serde_json::to_value(returning).map_err(|_| {
                (
                    StatusCode::INTERNAL_SERVER_ERROR,
                    Json(models::ErrorResponse {
                        message:
"cannot encode response"
.into(),
                        details: serde_json::Value::Null,
                    }),
                )
            })?),
        )])]),
    })
}
```