# Hasura Data Connectors Developer's Guide

# Capabilities

The capabilities endpoint provides metadata about the features which the data connector (and data source) support.

## Request

`GET /capabilities`

## Response

See[ CapabilitiesResponse ](../reference/types.html#capabilitiesresponse)

### Example

```
{
"versions"
:
"^0.1.0"
,
"capabilities"
: {
"query"
: {
"aggregates"
: {},
"variables"
: {}
    },
"relationships"
: {
"relation_comparisons"
: {},
"order_by_aggregate"
: {}
    }
  }
}
```

## Response Fields

| Name | Description |
|---|---|
|  `versions`  | A[ semantic versioning ](https://semver.org)range of API versions which the data connector |
|  `capabilities.explain`  | Whether the data connector is capable of describing query plans |
|  `capabilities.query.aggregates`  | Whether the data connector supports[ aggregate queries ](queries/aggregates.html) |
|  `capabilities.query.variables`  | Whether the data connector supports[ queries with variables ](queries/variables.html) |
|  `capabilities.relationships`  | Whether the data connector supports[ relationships ](queries/relationships.html) |
|  `capabilities.relationships.order_by_aggregate`  | Whether order by clauses can include aggregates |
|  `capabilities.relationships.relation_comparisons`  | Whether comparisons can include columns reachable via[ relationships ](queries/relationships.html) |


## See also

- Type[ Capabilities ](../reference/types.html#capabilities)
- Type[ CapabilitiesResponse ](../reference/types.html#capabilitiesresponse)
- Type[ QueryCapabilities ](../reference/types.html#querycapabilities)
