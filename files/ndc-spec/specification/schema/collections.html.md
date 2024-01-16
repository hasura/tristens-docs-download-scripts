# Hasura Data Connectors Developer's Guide

# Collections

The schema should define the metadata for any *collections* which can be queried using the query endpoint, or mutated using the mutation endpoint.

Each collection is defined by its name, any collection[ arguments ](../queries/arguments.html), the[ object type ](./object-types.html)of its rows, and some additional metadata related to permissions and constraints.

To describe a collection, add a[ CollectionInfo ](../../reference/types.html#collectioninfo)structure to the `collections` field of the schema response.

## Requirements

- The `type` field should name an object type which is defined in the schema response.


## Example

```
{
"collections"
: [
    {
"name"
:
"articles"
,
"description"
:
"A collection of articles"
,
"arguments"
: {},
"type"
:
"article"
,
"deletable"
:
false
,
"uniqueness_constraints"
: {
"ArticleByID"
: {
"unique_columns"
: [
"id"
]
        }
      },
"foreign_keys"
: {}
    },
    {
"name"
:
"authors"
,
"description"
:
"A collection of authors"
,
"arguments"
: {},
"type"
:
"author"
,
"deletable"
:
false
,
"uniqueness_constraints"
: {
"AuthorByID"
: {
"unique_columns"
: [
"id"
]
        }
      },
"foreign_keys"
: {}
    }
  ],
  ...
}
```

## See also

- Type[ CollectionInfo ](../../reference/types.html#collectioninfo)
