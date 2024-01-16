# Hasura Data Connectors Developer's Guide

# Filtering

A[ Query ](../../reference/types.html#query)can specify a predicate expression which should be used to filter rows in the response.

A predicate expression can be one of

- An application of a *comparison operator* to a column and a value, or
- An `EXISTS` expression, or
- A *conjunction* of other expressions, or
- A *disjunction* of other expressions, or
- A *negation* of another expression


The predicate expression is specified in the `predicate` field of the[ Query ](../../reference/types.html#query)object.

## Comparison Operators

### Unary Operators

Unary comparison operators are denoted by expressions with a `type` field of `unary_comparison_operator` .

The only supported unary operator currently is `is_null` , which return `true` when a column value is `null` :

```
{
"type"
:
"unary_comparison_operator"
,
"operator"
:
"is_null"
,
"column"
: {
"name"
:
"title"
}
}
```

### Binary Operators

Binary comparison operators are denoted by expressions with a `type` field of `binary_comparison_operator` .

The set of available operators depends on the type of the column involved in the expression. The `equal` operator should be implemented for all types of columns.

See type[ BinaryComparisonOperator ](../../reference/types.html#binarycomparisonoperator).

#### equals

 `equals` tests if a column value is equal to a scalar value, another column value, or a variable.

See type[ ComparisonValue ](../../reference/types.html#comparisonvalue)for the valid inhabitants of the `value` field.

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
"id"
,
"path"
: []
            },
"operator"
: {
"type"
:
"equal"
},
"value"
: {
"type"
:
"scalar"
,
"value"
:
1
}
        }
    },
"collection_relationships"
: {}
}
```

### Custom Binary Comparison Operators

Data connectors can also extend the expression grammar by defining comparison operators on each[ scalar type ](../schema/scalar-types.html)in the schema response.

For example, here is an expression which uses a custom `like` operator provided on the `String` type in the reference implementation:

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
    },
"collection_relationships"
: {}
}
```

### Binary Array-Valued Comparison Operators

Binary comparison operators are denoted by expressions with a `type` field of `binary_array_comparison_operator` .

#### in

 `in` tests if a column value is a member of an array of values, each of which can be a scalar value, another column value, or a variable.

See type[ ComparisonValue ](../../reference/types.html#comparisonvalue)for the valid inhabitants of the `value` field.

 *Note* : in general, `PathElement` s in a `ComparisonValue` can refer to *array* relationships. However, in the case of the `in` operator, such requests can be very difficult to implement, and for practical purposes, it is not very useful to express such queries. Therefore, in the case of the `in` operator, connectors can expect `PathElements` in `ComparisonValue` s to always only refer to *object* relationships, and fail with a `Bad Request` error otherwise.

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
"where"
: {
"type"
:
"binary_array_comparison_operator"
,
"column"
: {
"type"
:
"column"
,
"name"
:
"author_id"
,
"path"
: []
            },
"operator"
:
"in"
,
"values"
: [
                {
"type"
:
"scalar"
,
"value"
:
1
},
                {
"type"
:
"scalar"
,
"value"
:
2
}
            ]
        }
    },
"collection_relationships"
: {}
}
```

### Columns in Operators

Comparison operators compare columns to values. The column on the left hand side of any operator is described by a[ ComparisonTarget ](../../reference/types.html#comparisontarget), and the various cases will be explained next.

#### Referencing a column from the same collection

If the `ComparisonTarget` has type `column` , and the `path` property is empty, then the `name` property refers to a column in the current collection.

#### Referencing a column from a related collection

If the `ComparisonTarget` has type `column` , and the `path` property is non-empty, then the `name` property refers to column in a related collection. The path consists of a collection of[ PathElement ](../../reference/types.html#pathelement)s, each of which references a named[ relationship ](./relationships.html), any[ collection arguments ](./arguments.html), and a[ predicate expression ](./filtering.html)to be applied to any relevant rows in the related collection.

When a `PathElement` references an *array* relationship, the enclosing operator should be considered *existentially quantified* over all related rows.

#### Referencing a column from the root collection

If the `ComparisonTarget` has type `root_collection_column` , then the `name` property refers to a column in the *root collection* .

The root collection is defined as the collection in scope at the nearest enclosing[ Query ](../../reference/types.html#query), and the column should be chosen from the *row* in that collection which was in scope when that `Query` was being evaluated.

### Values in Binary Operators

Binary (including array-valued) operators compare columns to *values* , but there are several types of valid values:

- Scalar values, as seen in the examples above, compare the column to a specific value,
- Variable values compare the column to the current value of a[ variable ](./variables.html),
- Column values compare the column to *another* column, possibly selected from a different collection. Column values are also described by a[ ComparisonTarget ](../../reference/types.html#comparisontarget).


## EXISTS expressions

An `EXISTS` expression tests whether a row exists in some possibly-related collection, and is denoted by an expression with a `type` field of `exists` .

 `EXISTS` expressions can query related or unrelated collections.

### Related Collections

Related collections are related to the original collection by a relationship in the `collection_relationships` field of the top-level[ QueryRequest ](../../reference/types.html#queryrequest).

For example, this query fetches authors who have written articles whose titles contain the string `"Functional"` :

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

### Unrelated Collections

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
"unrelated"
,
"arguments"
: {},
"collection"
:
"articles"
},
"where"
: {
"type"
:
"and"
,
"expressions"
: [
                    {
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
"author_id"
,
"path"
: []
                        },
"operator"
: {
"type"
:
"equal"
},
"value"
: {
"type"
:
"column"
,
"column"
: {
"type"
:
"root_collection_column"
,
"name"
:
"id"
}
                        }
                    },
                    {
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
                ]
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

## Conjunction of expressions

To express the conjunction of multiple expressions, specify a `type` field of `and` , and provide the expressions in the `expressions` field.

For example, to test if the `first_name` column is null *and* the `last_name` column is also null:

```
{
"type"
:
"and"
,
"expressions"
: [
        {
"type"
:
"unary_comparison_operator"
,
"operator"
:
"is_null"
,
"column"
: {
"name"
:
"first_name"
}
        },
        {
"type"
:
"unary_comparison_operator"
,
"operator"
:
"is_null"
,
"column"
: {
"name"
:
"last_name"
}
        }
    ]
}
```

## Disjunction of expressions

To express the disjunction of multiple expressions, specify a `type` field of `or` , and provide the expressions in the `expressions` field.

For example, to test if the `first_name` column is null *or* the `last_name` column is also null:

```
{
"type"
:
"or"
,
"expressions"
: [
        {
"type"
:
"unary_comparison_operator"
,
"operator"
:
"is_null"
,
"column"
: {
"name"
:
"first_name"
}
        },
        {
"type"
:
"unary_comparison_operator"
,
"operator"
:
"is_null"
,
"column"
: {
"name"
:
"last_name"
}
        }
    ]
}
```

## Negation

To express the negation of an expressions, specify a `type` field of `not` , and provide that expression in the `expression` field.

For example, to test if the `first_name` column is *not* null:

```
{
"type"
:
"not"
,
"expression"
: {
"type"
:
"unary_comparison_operator"
,
"operator"
:
"is_null"
,
"column"
: {
"name"
:
"first_name"
}
    }
}
```

## See also

- Type[ Expression ](../../reference/types.html#expression)
