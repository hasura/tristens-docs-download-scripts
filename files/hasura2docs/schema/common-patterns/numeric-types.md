# Wide Numeric Types

Databases often support numerical types which accommodate a wider range of numbers than the Number type in JavaScript
(and in programming languages broadly). Parsing JSON payloads containing such numbers naively suffers from numerical
overflow issues.

For example, The JSON object `{ "value" : 9223372036854775807}` , is still a valid[ RFC4627 ](https://www.ietf.org/rfc/rfc4627.txt)JSON string, but in most JS runtimes, the result of `JSON.parse` is the
object `{ value: 9223372036854776000 }` , where the last 4 digits have been rounded.

In order to deal with this you will need to ensure that clients issuing queries containing large numbers are adequately
equipped to handle those. For Javascript, this could mean using a package such as[ json-bigint ](https://www.npmjs.com/package/json-bigint).

The Hasura GraphQL Engine also supports optionally representing large number types as strings. You can do this using
Hasura Community Edition, Hasura Cloud, and Hasura Enterprise Edition by setting the[ stringify-numeric-types environment variable ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#stringify-numeric-types).

When this option is set, all values of large numerical type appearing in query results will be represented as strings.
It's then up to the caller to interpret these strings numerically as needed.

Note

This only affects the JSON format of query results. Query *input fields* still use JSON and GraphQL number types, though
the[ BigQuery ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types)backend also supports an extra flag to affect
input fields.

Using the json-bigint package

`json-bigint`

The `json-bigint` package can be used to parse JSON strings containing large numbers:

```
var   JSONbig   =   require ( 'json-bigint' ) ;
var  json  =   '{ "value" : 9223372036854775807, "v2": 123 }' ;
// Built-in JSON parsing:
var  r  =   JSON . parse ( json ) ;
console . log ( r . value . toString ( ) ) ;
// Prints: 9223372036854776000
console . log ( JSON . stringify ( r ) ) ;
// Prints: {"value":9223372036854776000,"v2":123}
// Big number JSON parsing:
var  r1  =   JSONbig . parse ( json ) ;
console . log ( r1 . value . toString ( ) ) ;
// Prints: 9223372036854775807
console . log ( JSONbig . stringify ( r1 ) ) ;
// Prints: {"value":9223372036854775807,"v2":123}
```

[ Source: json-bigint homepage ](https://www.npmjs.com/package/json-bigint).

### What did you think of this doc?

Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)