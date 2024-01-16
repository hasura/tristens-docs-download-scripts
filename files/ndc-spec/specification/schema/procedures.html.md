# Hasura Data Connectors Developer's Guide

# Procedures

The schema should define metadata for each *procedure* which the data connector implements.

Each procedure is defined by its name, any arguments types and a result type.

To describe a procedure, add a[ ProcedureInfo ](../../reference/types.html#procedureinfo)structure to the `procedure` field of the schema response.

## Example

```
{
"procedures"
: [
    {
"name"
:
"upsert_article"
,
"description"
:
"Insert or update an article"
,
"arguments"
: {
"article"
: {
"description"
:
"The article to insert or update"
,
"type"
: {
"type"
:
"named"
,
"name"
:
"article"
}
        }
      },
"result_type"
: {
"type"
:
"named"
,
"name"
:
"article"
}
    }
  ],
  ...
}
```

## See also

- Type[ ProcedureInfo ](../../reference/types.html#procedureinfo)
