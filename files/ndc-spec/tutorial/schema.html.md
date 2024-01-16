# Hasura Data Connectors Developer's Guide

# Schema

The schema endpoint should return data describing the data connector's scalar and object types, along with any collections, functions and procedures which are exposed.

```
async
fn   get_schema
() -> Json<models::SchemaResponse> {
// ...
Json(models::SchemaResponse {
        scalar_types,
        object_types,
        collections,
        functions,
        procedures,
    })
}
```

## Scalar Types

We define two scalar types: `String` and `Int` .

 `String` supports a custom `like` comparison operator, and `Int` supports custom aggregation operators `min` and `max` .

```
let
scalar_types = BTreeMap::from_iter([
        (
"String"
.into(),
            models::ScalarType {
                aggregate_functions: BTreeMap::new(),
                comparison_operators: BTreeMap::from_iter([(
"like"
.into(),
                    models::ComparisonOperatorDefinition {
                        argument_type: models::Type::Named {
                            name:
"String"
.into(),
                        },
                    },
                )]),
            },
        ),
        (
"Int"
.into(),
            models::ScalarType {
                aggregate_functions: BTreeMap::from_iter([
                    (
"max"
.into(),
                        models::AggregateFunctionDefinition {
                            result_type: models::Type::Nullable {
                                underlying_type:
Box
::new(models::Type::Named {
                                    name:
"Int"
.into(),
                                }),
                            },
                        },
                    ),
                    (
"min"
.into(),
                        models::AggregateFunctionDefinition {
                            result_type: models::Type::Nullable {
                                underlying_type:
Box
::new(models::Type::Named {
                                    name:
"Int"
.into(),
                                }),
                            },
                        },
                    ),
                ]),
                comparison_operators: BTreeMap::from_iter([]),
            },
        ),
    ]);
```

## Object Types

For each collection, we define an object type for its rows:

```
let
object_types = BTreeMap::from_iter([
        (
"article"
.into(), article_type),
        (
"author"
.into(), author_type),
    ]);
```

### Author

```
let
author_type = models::ObjectType {
        description:
Some
(
"An author"
.into()),
        fields: BTreeMap::from_iter([
            (
"id"
.into(),
                models::ObjectField {
                    description:
Some
(
"The author's primary key"
.into()),
                    r#
type :  models
::Type::Named { name:
"Int"
.into() },
                },
            ),
            (
"first_name"
.into(),
                models::ObjectField {
                    description:
Some
(
"The author's first name"
.into()),
                    r#
type :  models
::Type::Named {
                        name:
"String"
.into(),
                    },
                },
            ),
            (
"last_name"
.into(),
                models::ObjectField {
                    description:
Some
(
"The author's last name"
.into()),
                    r#
type :  models
::Type::Named {
                        name:
"String"
.into(),
                    },
                },
            ),
        ]),
    };
```

### Article

```
let
article_type = models::ObjectType {
        description:
Some
(
"An article"
.into()),
        fields: BTreeMap::from_iter([
            (
"id"
.into(),
                models::ObjectField {
                    description:
Some
(
"The article's primary key"
.into()),
                    r#
type :  models
::Type::Named { name:
"Int"
.into() },
                },
            ),
            (
"title"
.into(),
                models::ObjectField {
                    description:
Some
(
"The article's title"
.into()),
                    r#
type :  models
::Type::Named {
                        name:
"String"
.into(),
                    },
                },
            ),
            (
"author_id"
.into(),
                models::ObjectField {
                    description:
Some
(
"The article's author ID"
.into()),
                    r#
type :  models
::Type::Named { name:
"Int"
.into() },
                },
            ),
        ]),
    };
```

## Collections

We define each collection's schema using the type information defined above:

```
let
collections =
vec!
[
        articles_collection,
        authors_collection,
        articles_by_author_collection,
    ];
```

### Author

```
let
authors_collection = models::CollectionInfo {
        name:
"authors"
.into(),
        description:
Some
(
"A collection of authors"
.into()),
        collection_type:
"author"
.into(),
        arguments: BTreeMap::new(),
        foreign_keys: BTreeMap::new(),
        uniqueness_constraints: BTreeMap::from_iter([(
"AuthorByID"
.into(),
            models::UniquenessConstraint {
                unique_columns:
vec!
[
"id"
.into()],
            },
        )]),
    };
```

### Article

```
let
articles_collection = models::CollectionInfo {
        name:
"articles"
.into(),
        description:
Some
(
"A collection of articles"
.into()),
        collection_type:
"article"
.into(),
        arguments: BTreeMap::new(),
        foreign_keys: BTreeMap::from_iter([(
"Article_AuthorID"
.into(),
            models::ForeignKeyConstraint {
                foreign_collection:
"authors"
.into(),
                column_mapping: BTreeMap::from_iter([(
"author_id"
.into(),
"id"
.into())]),
            },
        )]),
        uniqueness_constraints: BTreeMap::from_iter([(
"ArticleByID"
.into(),
            models::UniquenessConstraint {
                unique_columns:
vec!
[
"id"
.into()],
            },
        )]),
    };
```

### articles_by_author

We define one additional collection, `articles_by_author` , which is provided as an example of a collection with an argument:

```
let
articles_by_author_collection = models::CollectionInfo {
        name:
"articles_by_author"
.into(),
        description:
Some
(
"Articles parameterized by author"
.into()),
        collection_type:
"article"
.into(),
        arguments: BTreeMap::from_iter([(
"author_id"
.into(),
            models::ArgumentInfo {
                argument_type: models::Type::Named { name:
"Int"
.into() },
                description:
None
,
            },
        )]),
        foreign_keys: BTreeMap::new(),
        uniqueness_constraints: BTreeMap::new(),
    };
```

## Functions

The schema defines a list of[ functions ](../specification/schema/functions.html), each including its input and output[ types ](../specification/types.html).

### Get Latest Article

As an example, we define a `latest_article_id` function, which returns a single integer representing the maximum article ID.

```
let
latest_article_id_function = models::FunctionInfo {
        name:
"latest_article_id"
.into(),
        description:
Some
(
"Get the ID of the most recent article"
.into()),
        result_type: models::Type::Nullable {
            underlying_type:
Box
::new(models::Type::Named { name:
"Int"
.into() }),
        },
        arguments: BTreeMap::new(),
    };
```

## Procedures

The schema defines a list of[ procedures ](../specification/schema/procedures.html), each including its input and output[ types ](../specification/types.html).

### Upsert Article

As an example, we define an *upsert* procedure for the article collection defined above. The procedure will accept an input argument of type `article` , and returns a nulcollection `article` , representing the state of the article before the update, if it were already present.

```
let
upsert_article = models::ProcedureInfo {
        name:
"upsert_article"
.into(),
        description:
Some
(
"Insert or update an article"
.into()),
        arguments: BTreeMap::from_iter([(
"article"
.into(),
            models::ArgumentInfo {
                description:
Some
(
"The article to insert or update"
.into()),
                argument_type: models::Type::Named {
                    name:
"article"
.into(),
                },
            },
        )]),
        result_type: models::Type::Nullable {
            underlying_type:
Box
::new(models::Type::Named {
                name:
"article"
.into(),
            }),
        },
    };
```