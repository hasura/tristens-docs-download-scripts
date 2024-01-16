# BigQuery: Supported Types

## Introduction​

List of BigQuery types supported by the Hasura GraphQL Engine with their equivalent Hasura types:

| Name | Aliases | Description | Hasura Type |
|---|---|---|---|
| BIGDECIMAL | BIGNUMERIC | exact numeric of selectable precision | [ Decimal ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#decimal)or[ bigquery_decimal ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#large-numerical-types) |
| BOOL |  | logical Boolean (true/false) | [ Bool ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#bool) |
| BYTES |  | variable-length bit string | [ Bytes ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#bytes) |
| DATE |  | calendar date (year, month, day) | [ Date ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#date) |
| DATETIME |  | calendar date including time of day | [ Datetime ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#datetime) |
| DECIMAL | NUMERIC | exact numeric of selectable precision | [ Decimal ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#decimal)or[ bigquery_decimal ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#large-numerical-types) |
| FLOAT | FLOAT64 | double (8 bytes) precision floating-point number | [ Float ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#float)or[ bigquery_float ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#large-numerical-types) |
| GEOGRAPHY |  | OpenGIS Geography type | [ Geography ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#geography) |
| INTEGER | INT64 | (8-bytes) signed integer | [ Int ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#integer)or[ bigquery_int ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#large-numerical-types) |
| TIME |  | time of day, excluding time zone | [ Time ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#time) |
| TIMESTAMP |  | date and time, time zone invariant | [ Timestamp ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#timestamp) |


Note

You can learn more about BigQuery data types[ here ](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types).

Note

The BigQuery JSON type is not yet supported

### Length constraints​

BigQuery supports size-constraining the following types:

- STRING
- BYTES
- NUMERIC
- BIGNUMERIC


For example, `STRING(10)` lets you have a string column that contains, at most, 10 characters.

When mapping parametrized BigQuery types to GraphQL types, the Hasura GraphQL Engine ignores the size constraint
parameters.

This, for example, means that `STRING` and `STRING(10)` are both mapped to the GraphQL type `String` and treated alike
in all respects. Mutations that attempt to input data that exceeds the constraints of a column inherit the behavior of
BigQuery, which is to throw an `OUT_OF_RANGE` error.

Reference:[ https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#parameterized_data_types ](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#parameterized_data_types)

### Large numerical types​

In addition to the[ stringify-numeric-types ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#stringify-numeric-types)option,
the BigQuery backend supports an experimental feature[ bigquery_string_numeric_input ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#experimental-features)which extends the support for stringified numbers to input values as well.

Enabling this flag will add a `bigquery_` prefix to the names of numeric types
appearing in the GraphQL schema and use those instead of the builtin scalar
types. This distinction is necessary, as GraphQL mandates that the builtin
numeric types be syntactically represented as numbers only.

## Bool​

GraphQL default Scalar with name **Boolean** . The **Boolean** scalar type represents `true` or `false` .

E.g.

```
objects :   [
   {
     is_published :   true
   }
]
```

## Bytes​

GraphQL custom scalar with name **Bytes** . The **Bytes** scalar type encodes raw binary data, represented as UTF-8
character sequences.

E.g.

```
objects :   [
   {
     bytes :   "Raven"
   }
]
```

Reference:[ https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#bytes_type ](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#bytes_type)

## Date​

GraphQL custom scalar with name **Date** . Date (no time of day). Allowed values are yyyy-mm-dd.

E.g.

```
objects :   [
   {
     date :   "1996-03-15"
   }
]
```

Reference:

- [ https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#date_type ](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#date_type)
- [ https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#date_literals ](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#date_literals)


## Datetime​

GraphQL custom scalar with name **Datetime** , representing date including the time of day. The syntactic format of
Datetime literals is simply a[ Date ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#date)literal followed by a[ Time ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#time)literal, separated by either ` ` (space)
or `t` or `T` .

E.g.

```
objects :   [
   {
     datetime :   "1996-03-15 17:30:15.001"
   }
]
```

Reference:

- [ https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#datetime_type ](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#datetime_type)
- [ https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#datetime_literals ](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#datetime_literals)


## Decimal​

GraphQL custom scalar type with name **Decimal** .

E.g.

```
objects :   [
   {
     decimal_col :   0.8
   }
]
```

Reference:

- [ https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#numeric_literals ](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#numeric_literals)


## Float​

GraphQL builtin scalar type with name **Float** .

E.g.

```
objects :   [
   {
     float_col :   0.8
   }
]
```

## Geography​

GraphQL custom scalar type `geography` is generated for a `GEOGRAPHY` column. Geographical data is represented textually
in the standard OpenGIS format.

```
objects :   [
   {
     point :   " POINT(32 210) "
     polygon :   "POLYGON((0 0, 2 2, 2 0, 0 0), (2 2, 3 4, 2 4))"
   }
]
```

Reference:[ https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#geography_type ](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-types#geography_type)

## Integer​

GraphQL default scalar with name **Int** .

E.g.

```
objects :   [
   {
     int_col :   27
   }
]
```

## String​

GraphQL default scalar with name **String** . The **String** scalar type represents textual data, represented as UTF-8
character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

E.g.

```
objects :   [
   {
     name :   "Raven"
   }
]
```

## Time​

GraphQL custom scalar type with name **Time** . Time of day only, without time zone. Allowed values should be of format `[H]H:[M]M:[S]S[.DDDDDD]` ).

E.g.

```
objects :   [
   {
     time :   "17:30:15.001"
   }
]
```

Reference:

- [ https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#datetime_literals ](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#datetime_literals)
- [ https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#time_literals ](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#time_literals)


## Timestamp​

GraphQL custom scalar type with name **Timestamp** . Semantically, BigQuery timestamps are timezone-invariant, but may
for display and input purposes refer to a timezone.

Their format is the same as that of Datetime, optionally including a timezone (defaulting to UTC).

E.g.

```
objects :   [
   {
     timestamp :   "2016-07-20T17:30:15+05:30"
   }
]
```

```
objects :   [
   {
     timestamp :   "2016-07-20 17:30:15 Europe/Copenhagen"
   }
]
```

Reference:[ https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#timestamp_literals ](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#timestamp_literals)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#types-table)
    - [ Length constraints ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#length-constraints)

- [ Large numerical types ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#large-numerical-types)
- [ Bool ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#bool)
- [ Bytes ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#bytes)
- [ Date ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#date)
- [ Datetime ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#datetime)
- [ Decimal ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#decimal)
- [ Float ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#float)
- [ Geography ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#geography)
- [ Integer ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#integer)
- [ String ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#string)
- [ Time ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#time)
- [ Timestamp ](https://hasura.io/docs/latest/schema/bigquery/bigquery-types/#large-numerical-types/#timestamp)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)