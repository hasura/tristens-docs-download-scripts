# Hasura Data Connectors Developer's Guide

# Evaluating Arguments

Now that we have reduced the problem to a single set of query variables, we must evaluate any[ collection arguments ](../../specification/queries/arguments.html), and in turn, evaluate the *collection* of rows that we will be working with.

From there, we will be able to apply predicates, sort and paginate rows. But one step at a time!

The first step is to evaluate each argument, which the `execute_query_with_variables` function does by delegating to the `eval_argument` function:

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
let
mut
argument_values = BTreeMap::new();
for
(argument_name, argument_value)
in
arguments.iter() {
if
argument_values
            .insert(
                argument_name.clone(),
                eval_argument(variables, argument_value)?,
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
collection = get_collection_by_name(collection, &argument_values, state)?;

    execute_query(
        collection_relationships,
        variables,
        state,
        query,
        Root::CurrentRow,
        collection,
    )
}
```

Once this is complete, and we have a collection of evaluated `argument_values` , we can delegate to the `get_collection_by_name` function. This function peforms the work of computing the full collection, by pattern matching on the name of the collection:

```
fn   get_collection_by_name
(
    collection_name: &
str
,
    arguments: &BTreeMap<
String
, serde_json::Value>,
    state: &AppState,
) ->
Result
<
Vec
<Row>> {
match
collection_name {
"articles"
=>
Ok
(state.articles.values().cloned().collect()),
"authors"
=>
Ok
(state.authors.values().cloned().collect()),
"articles_by_author"
=> {
let
author_id = arguments.get(
"author_id"
).ok_or((
                StatusCode::BAD_REQUEST,
                Json(models::ErrorResponse {
                    message:
"missing argument author_id"
.into(),
                    details: serde_json::Value::Null,
                }),
            ))?;
let
author_id_int = author_id.as_i64().ok_or((
                StatusCode::BAD_REQUEST,
                Json(models::ErrorResponse {
                    message:
"author_id must be a string"
.into(),
                    details: serde_json::Value::Null,
                }),
            ))?;
let
mut
articles_by_author =
vec!
[];
for
(_id, article)
in
state.articles.iter() {
let
article_author_id = article.get(
"author_id"
).ok_or((
                    StatusCode::INTERNAL_SERVER_ERROR,
                    Json(models::ErrorResponse {
                        message:
"author_id not found"
.into(),
                        details: serde_json::Value::Null,
                    }),
                ))?;
let
article_author_id_int = article_author_id.as_i64().ok_or((
                    StatusCode::INTERNAL_SERVER_ERROR,
                    Json(models::ErrorResponse {
                        message:
" "
.into(),
                        details: serde_json::Value::Null,
                    }),
                ))?;
if
article_author_id_int == author_id_int {
                    articles_by_author.push(article.clone())
                }
            }
Ok
(articles_by_author)
        }
"latest_article_id"
=> {
let
latest_id = state
                .articles
                .iter()
                .filter_map(|(_id, a)| a.get(
"id"
).and_then(|v| v.as_i64()))
                .max();
let
latest_id_value = serde_json::to_value(latest_id).map_err(|_| {
                (
                    StatusCode::INTERNAL_SERVER_ERROR,
                    Json(models::ErrorResponse {
                        message:
" "
.into(),
                        details: serde_json::Value::Null,
                    }),
                )
            })?;
Ok
(
vec!
[BTreeMap::from_iter([(
"__value"
.into(),
                latest_id_value,
            )])])
        }
        _ =>
Err
((
            StatusCode::BAD_REQUEST,
            Json(models::ErrorResponse {
                message:
"invalid collection name"
.into(),
                details: serde_json::Value::Null,
            }),
        )),
    }
}
```

 *Note 1* : the `articles_by_author` collection is the only example here which has to apply any arguments. It is provided as an example of a collection which accepts an `author_id` argument, and it must validate that the argument is present, and that it is an integer.

 *Note 2* : the `latest_article_id` collection is provided as an example of a[ function ](../../specification/schema/functions.html). It is a collection like all the others, but must follow the rules for functions: it must consist of a single row, with a single column named `__value` .

In the next section, we will break down the implementation of `execute_query` .
Once we have computed the full collection, we can move onto evaluating the query in the context of that collection, using the `execute_query` function:

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

In the next section, we will break down the implementation of `execute_query` .