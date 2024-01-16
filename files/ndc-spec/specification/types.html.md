# Hasura Data Connectors Developer's Guide

# Types

Several definitions in this specification make mention of *types* . Types are used to categorize the sorts of data returned and accepted by a data connector.

Scalar and named object types are defined in the[ schema response
 ](./schema/README.html), and referred to by name at the point of use.

Array types and nullable types are constructed at the point of use.

## Named Types

To refer to a named (scalar or object) type, use the type `named` , and provide the name:

```
{
"type"
:
"named"
,
"name"
:
"String"
}
```

## Array Types

To refer to an array type, use the type `array` , and refer to the type of the elements of the array in the `element_type` field:

```
{
"type"
:
"array"
,
"element_type"
: {
"type"
:
"named"
,
"name"
:
"String"
}
}
```

## Nullable Types

To refer to a nullable type, use the type `nullable` , and refer to the type of the underlying (non-null) inhabitants in the `underlying_type` field:

```
{
"type"
:
"nullable"
,
"underlying_type"
: {
"type"
:
"named"
,
"name"
:
"String"
}
}
```

Nullable and array types can be nested. For example, to refer to a nullable array of nullable strings:

```
{
"type"
:
"nullable"
,
"underlying_type"
: {
"type"
:
"array"
,
"element_type"
: {
"type"
:
"nullable"
,
"underlying_type"
: {
"type"
:
"named"
,
"name"
:
"String"
}
    }
  }
}
```

## See also

- Type[ Type
 ](../reference/types.html#type)
- [ Scalar types
 ](./schema/scalar-types.html)
- [ Object types
 ](./schema/object-types.html)
