# Hasura Data Connectors Developer's Guide

# Variables

A[ QueryRequest ](../../reference/types.html#queryrequest)can optionally specify one or more sets of variables which can be referenced throughout the[ Query ](../../reference/types.html#query)object.

Query variables will only be provided if the `query.variables` [ capability ](../capabilities.html)is advertised in the capabilities response.

The intent is that the data connector should attempt to perform multiple versions of the query in parallel - one instance of the query for each set of variables. For each set of variables, each variable value should be substituted wherever it is referenced in the query - for example in a[ ComparisonValue ](../../reference/types.html#comparisonvalue).

## Example

In the following query, we fetch two rowsets of article data. In each rowset, the rows are filtered based on the `author_id` column, and the prescribed `author_id` is determined by a variable. The choice of `author_id` varies between rowsets.

The result contains one rowset containing articles from the author with ID `1` , and a second for the author with ID `2` .

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
"variable"
,
"name"
:
"$article_id"
}
        }
    },
"collection_relationships"
: {},
"variables"
: [
        {
"$article_id"
:
1
},
        {
"$article_id"
:
2
}
    ]
}
```

## Requirements

- If `variables` are provided in the[ QueryRequest ](../../reference/types.html#queryrequest), then the[ QueryResponse ](../../reference/types.html#queryresponse)should contain one[ RowSet ](../../reference/types.html#rowset)for each set of variables.
- If `variables` are not provided, the data connector should return a single[ RowSet ](../../reference/types.html#rowset).
