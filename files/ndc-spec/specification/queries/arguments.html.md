# Hasura Data Connectors Developer's Guide

# Arguments

 *Collection arguments* parameterize an entire collection, and must be provided in queries wherever the collection is referenced, either directly, or via relationships,

## Collection Arguments

Collection arguments should be provided in the `QueryRequest` anywhere a collection is referenced. The set of provided arguments should be compatible with the list of arguments required by the corresponding[ collection in the schema response ](../schema/collections.html).

### Specifying arguments to the top-level collection

Collection arguments should be provided as key-value pairs in the `arguments` property of the top-level `QueryRequest` object:

```
{
"collection"
:
"articles_by_author"
,
"arguments"
: {
"author_id"
: {
"type"
:
"literal"
,
"value"
:
1
}
    },
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
        }
    },
"collection_relationships"
: {}
}
```

### Relationships

[ Relationships ](./relationships.html)can specify values for arguments on their target collection:

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
"articles"
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
                    }
                }
            }
        }
    },
"collection_relationships"
: {
"author_articles"
: {
"arguments"
: {
"author_id"
: {
"type"
:
"column"
,
"name"
:
"id"
}
            },
"column_mapping"
: {
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
"articles_by_author"
}
    }
}
```

Any arguments which are not defined by the relationship itself should be specified where the relationship is used. For example, here the `author_id` argument can be moved from the relationship definition to the field which uses it:

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
"articles"
: {
"type"
:
"relationship"
,
"arguments"
: {
"author_id"
: {
"type"
:
"column"
,
"name"
:
"id"
}
                },
"relationship"
:
"author_articles"
,
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
                    }
                }
            }
        }
    },
"collection_relationships"
: {
"author_articles"
: {
"arguments"
: {},
"column_mapping"
: {},
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
"articles_by_author"
}
    }
}
```

### Collection arguments in predicates

Arguments must be specified in predicates whenever a reference to a secondary collection is required.

For example, in an `EXISTS` expression, if the target collection has arguments:

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
"id"
: {
"type"
:
"column"
,
"column"
:
"id"
}
        },
"where"
: {
"type"
:
"exists"
,
"in_collection"
: {
"type"
:
"related"
,
"arguments"
: {
"author_id"
: {
"type"
:
"column"
,
"name"
:
"id"
}
                },
"relationship"
:
"author_articles"
},
"where"
: {
"type"
:
"binary_comparison_operator"
,
"column"
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
"operator"
: {
"type"
:
"other"
,
"name"
:
"like"
},
"value"
: {
"type"
:
"scalar"
,
"value"
:
"Functional"
}
            }
        }
    },
"collection_relationships"
: {
"author_articles"
: {
"arguments"
: {},
"column_mapping"
: {},
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
"articles_by_author"
}
    }
}
```

Or when a predicate expression matches a column from a related collection:

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
"id"
: {
"type"
:
"column"
,
"column"
:
"id"
}
        },
"where"
: {
"type"
:
"binary_comparison_operator"
,
"column"
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
: [
                    {
"arguments"
: {
"author_id"
: {
"type"
:
"column"
,
"name"
:
"id"
}
                        },
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
            },
"operator"
: {
"type"
:
"other"
,
"name"
:
"like"
},
"value"
: {
"type"
:
"scalar"
,
"value"
:
"Functional"
}
        }
    },
"collection_relationships"
: {
"author_articles"
: {
"arguments"
: {},
"column_mapping"
: {},
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
"articles_by_author"
}
    }
}
```

### Collection arguments in order_by

Arguments must be specified when an `OrderByElement` references a related collection.

For example, when ordering by an aggregate of rows in a related collection, and that collection has arguments:

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
"id"
: {
"type"
:
"column"
,
"column"
:
"id"
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
: {
"author_id"
: {
"type"
:
"column"
,
"name"
:
"id"
}
                                },
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
: {},
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
"articles_by_author"
}
    }
}
```