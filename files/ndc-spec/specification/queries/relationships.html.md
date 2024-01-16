# Hasura Data Connectors Developer's Guide

# Relationships

Queries can request data from other collections via relationships. A relationship identifies rows in one collection (the "source collection") with possibly-many related rows in a second collection (the "target collection") in two ways:

- Columns in the two collections can be related via *column mappings* , and
- [ Collection arguments ](./arguments.html)to the target collection can be computed via the row of the source collection.


## Defining Relationships

Relationships are defined (and given names) in the top-level `QueryRequest` object, and then referred to by name everywhere they are used. To define a relationship, add a[ Relationship ](../../reference/types.html#relationship)object to the `collection_relationships` property of the `QueryRequest` object.

## Column Mappings

A column mapping is a set of pairs of columns - each consisting of one column from the source collection and one column from the target collection - which must be pairwise equal in order for a pair of rows to be considered equal.

For example, we can fetch each `author` with its list of related `articles` by establishing a column mapping between the author's primary key and the article's `author_id` column:

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

## Collection Arguments

See[ collection arguments ](./arguments.html)for examples.

## Advanced relationship use cases

Relationships are not used only for fetching data - they are used in practically all features of data connectors, as we will see below.

### Relationships in predicates

Filters can reference columns across relationships. For example, here we fetch all authors who have written articles with the word `"Functional"` in the title:

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
: [{
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
                }]
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

 `EXISTS` expressions in predicates can query related collections. Here we find all authors who have written any article with `"Functional"` in the title:

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
: {},
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

### Relationships in order_by

Sorting can be defined in terms of row counts and aggregates over related collections.

For example, here we order authors by the number of articles they have written:

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

We can also order by custom aggregate functions applied to related collections. For example, here we order authors by their most recent (maximum) article ID:

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