# Hasura Data Connectors Developer's Guide

# Field Selection

A[ Query ](../../reference/types.html#query)can specify which fields to fetch. The available fields are either

- the columns on the selected collection (i.e. those advertised in the corresponding[ CollectionInfo ](../../reference/types.html#collectioninfo)structure in the[ schema response ](../schema/collections.html)), or
- fields from[ related collections ](./relationships.html)


The requested fields are specified as a collection of[ Field ](../../reference/types.html#field)structures in the `field` property on the[ Query ](../../reference/types.html#query).

## Example

Here is an example of a query which selects some columns from the `articles` collection of the reference data connector:

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
        }
    },
"collection_relationships"
: {}
}
```

## Requirements

- If the[ QueryRequest ](../../reference/types.html#queryrequest)contains a[ Query ](../../reference/types.html#query)which specifies `fields` , then each[ RowSet ](../../reference/types.html#rowset)in the response should contain the `rows` property, and each row should contain all of the requested fields.


## See also

- Type[ Query ](../../reference/types.html#query)
- Type[ RowFieldValue ](../../reference/types.html#rowfieldvalue)
- Type[ RowSet ](../../reference/types.html#rowset)
