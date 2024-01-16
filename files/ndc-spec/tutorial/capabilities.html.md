# Hasura Data Connectors Developer's Guide

# Capabilities

The[ capabilities endpoint ](../specification/capabilities.html)should return data describing which features the data connector can implement, along with a range of versions of this specification that the data connector claims to implement.

The reference implementation returns a static `CapabilitiesResponse` :

```
async
fn   get_capabilities
() -> Json<models::CapabilitiesResponse> {
    Json(models::CapabilitiesResponse {
        versions:
"^0.1.0"
.into(),
        capabilities: models::Capabilities {
            explain:
None
,
            query: models::QueryCapabilities {
                aggregates:
Some
(LeafCapability {}),
                variables:
Some
(LeafCapability {}),
            },
            relationships:
Some
(RelationshipCapabilities {
                order_by_aggregate:
Some
(LeafCapability {}),
                relation_comparisons:
Some
(LeafCapability {}),
            }),
        },
    })
}
```

 *Note* : the reference implementation supports all capabilities with the exception of `explain` . This is because all queries are run in memory by naively interpreting the query request - there is no better description of the query plan than the raw query request itself!