# Hasura Data Connectors Developer's Guide

# Sorting

A[ Query ](../../reference/types.html#query)can specify how rows should be sorted in the response.

The requested ordering can be found in the `order_by` field of the[ Query ](../../reference/types.html#query)object.

## Computing the Ordering

To compute the ordering from the `order_by` field, data connectors should implement the following ordering between rows:

- Consider each element of the `order_by.elements` array in turn.
- For each[ OrderByElement ](../../reference/types.html#orderbyelement):
    - If `element.target.type` is `column` , then to compare two rows, compare the value in the selected column. See type `column` below.

- If `element.target.type` is `star_count_aggregate` , compare two rows by comparing the row count of a related collection. See type `star_count_aggregate` below.

- If `element.target.type` is `single_column_aggregate` , compare two rows by comparing a single column aggregate. See type `single_column_aggregate` below.


### Type column

If `element.order_direction` is `asc` , then the row with the smaller column comes first.

If `element.order_direction` is `asc` , then the row with the smaller column comes second.

If the column values are incomparable, continue to the next[ OrderByElement ](../../reference/types.html#orderbyelement).

The data connector should document, for each scalar type, a comparison function to use for any two values of that scalar type.

For example, a data connector might choose to use the obvious ordering for a scalar integer-valued type, but to use the database-given ordering for a string-valued type, based on a certain choice of collation.

For example, the following `query` requests that a collection of articles be ordered by `title` descending:

```
{
"collection"
:
"articles"
,
"arguments"
: {},
"query"
: {
"fields"
: {
"id"
: {
"type"
:
"column"
,
"column"
:
"id"
},
"title"
: {
"type"
:
"column"
,
"column"
:
"title"
}
        },
"order_by"
: {
"elements"
: [
                {
"target"
: {
"type"
:
"column"
,
"name"
:
"title"
,
"path"
: []
                    },
"order_direction"
:
"desc"
}
            ]
        }
    },
"collection_relationships"
: {}
}
```

The selected column can be chosen from a related collection by specifying the `path` property. `path` consists of a list of named[ relationships ](./relationships.html).

For example, this query sorts articles by their author's last names, and then by their first names, by traversing the relationship from articles to authors:

```
{
"collection"
:
"articles"
,
"arguments"
: {},
"query"
: {
"fields"
: {
"id"
: {
"type"
:
"column"
,
"column"
:
"id"
},
"title"
: {
"type"
:
"column"
,
"column"
:
"title"
},
"author"
: {
"type"
:
"relationship"
,
"arguments"
: {},
"relationship"
:
"article_author"
,
"query"
: {
"fields"
: {
"first_name"
: {
"type"
:
"column"
,
"column"
:
"first_name"
},
"last_name"
: {
"type"
:
"column"
,
"column"
:
"last_name"
}
                    }
                }
            }
        },
"order_by"
: {
"elements"
: [
                {
"target"
: {
"type"
:
"column"
,
"name"
:
"last_name"
,
"path"
: [
                            {
"arguments"
: {},
"relationship"
:
"article_author"
,
"predicate"
: {
"type"
:
"and"
,
"expressions"
: []
                                }
                            }
                        ]
                    },
"order_direction"
:
"asc"
},
                {
"target"
: {
"type"
:
"column"
,
"name"
:
"first_name"
,
"path"
: [
                            {
"arguments"
: {},
"relationship"
:
"article_author"
,
"predicate"
: {
"type"
:
"and"
,
"expressions"
: []
                                }
                            }
                        ]
                    },
"order_direction"
:
"asc"
}
            ]
        }
    },
"collection_relationships"
: {
"article_author"
: {
"arguments"
: {},
"column_mapping"
: {
"author_id"
:
"id"
},
"relationship_type"
:
"object"
,
"source_collection_or_type"
:
"article"
,
"target_collection"
:
"authors"
}
    }
}
```

### Type star_count_aggregate

An ordering of type `star_count_aggregate` orders rows by a count of rows in some[ related collection ](./relationships.html). If the respective counts are incomparable, the ordering should continue to the next[ OrderByElement ](../../reference/types.html#orderbyelement).

For example, this query sorts article authors by their total article count:

```
{
"collection"
:
"authors"
,
"arguments"
: {},
"query"
: {
"fields"
: {
"first_name"
: {
"type"
:
"column"
,
"column"
:
"first_name"
},
"last_name"
: {
"type"
:
"column"
,
"column"
:
"last_name"
},
"articles_aggregate"
: {
"type"
:
"relationship"
,
"arguments"
: {},
"relationship"
:
"author_articles"
,
"query"
: {
"aggregates"
: {
"count"
: {
"type"
:
"star_count"
}
                    }
                }
            }
        },
"order_by"
: {
"elements"
: [
                {
"order_direction"
:
"desc"
,
"target"
: {
"type"
:
"star_count_aggregate"
,
"path"
: [
                            {
"arguments"
: {},
"relationship"
:
"author_articles"
,
"predicate"
: {
"type"
:
"and"
,
"expressions"
: []
                                }
                            }
                        ]
                    }
                }
            ]
        }
    },
"collection_relationships"
: {
"author_articles"
: {
"arguments"
: {},
"column_mapping"
: {
"id"
:
"author_id"
},
"relationship_type"
:
"array"
,
"source_collection_or_type"
:
"author"
,
"target_collection"
:
"articles"
}
    }
}
```

### Type single_column_aggregate

An ordering of type `single_column_aggregate` orders rows by an aggregate computed over rows in some[ related collection ](./relationships.html). If the respective aggregates are incomparable, the ordering should continue to the next[ OrderByElement ](../../reference/types.html#orderbyelement).

For example, this query sorts article authors by their maximum article ID:

```
{
"collection"
:
"authors"
,
"arguments"
: {},
"query"
: {
"fields"
: {
"first_name"
: {
"type"
:
"column"
,
"column"
:
"first_name"
},
"last_name"
: {
"type"
:
"column"
,
"column"
:
"last_name"
},
"articles_aggregate"
: {
"type"
:
"relationship"
,
"arguments"
: {},
"relationship"
:
"author_articles"
,
"query"
: {
"aggregates"
: {
"max_id"
: {
"type"
:
"single_column"
,
"column"
:
"id"
,
"function"
:
"max"
}
                    }
                }
            }
        },
"order_by"
: {
"elements"
: [
                {
"order_direction"
:
"asc"
,
"target"
: {
"type"
:
"single_column_aggregate"
,
"column"
:
"id"
,
"function"
:
"max"
,
"path"
: [
                            {
"arguments"
: {},
"relationship"
:
"author_articles"
,
"predicate"
: {
"type"
:
"and"
,
"expressions"
: []
                                }
                            }
                        ]
                    }
                }
            ]
        }
    },
"collection_relationships"
: {
"author_articles"
: {
"arguments"
: {},
"column_mapping"
: {
"id"
:
"author_id"
},
"relationship_type"
:
"array"
,
"source_collection_or_type"
:
"author"
,
"target_collection"
:
"articles"
}
    }
}
```

## Requirements

- Rows in the response should be ordered according to the algorithm described above.
- The `order_by` field should not affect the set of collection which are returned, except for their order.
- If the `order_by` field is not provided then rows should be returned in an unspecified but deterministic order. For example, an implementation might choose to return rows in the order of their primary key or creation timestamp by default.


## See also

- Type[ OrderBy ](../../reference/types.html#orderby)
- Type[ OrderByElement ](../../reference/types.html#orderbyelement)
- Type[ OrderByTarget ](../../reference/types.html#orderbytarget)
