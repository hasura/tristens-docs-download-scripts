# Postgres: Supported Types

## Introduction​

List of PostgreSQL types supported by the Hasura GraphQL Engine with their equivalent Hasura types:

| Name | Aliases | Description | Hasura Type |
|---|---|---|---|
| bigint | int8 | signed eight-byte integer | [ Numeric ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#numeric)or[ String ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#string)([ flag ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#stringify-numeric-types)) |
| bigserial | serial8 | autoincrementing eight-byte integer | [ Numeric ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#numeric)or[ String ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#string)([ flag ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#stringify-numeric-types)) |
| bit[ (n) ] |  | fixed-length bit string | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| bit varying[ (n) ] | varbit[ (n) ] | variable-length bit string | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| boolean | bool | logical Boolean (true/false) | [ Bool ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#bool) |
| box |  | rectangular box on a plane | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| bytea |  | binary data (“byte array”) | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| character[ (n) ] | char[ (n) ] | fixed-length character string | [ Char ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#char) |
| character varying[ (n) ] | varchar[ (n) ] | variable-length character string | [ String ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#string) |
| cidr |  | IPv4 or IPv6 network address | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| circle |  | circle on a plane | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| date |  | calendar date (year, month, day) | [ Date ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#date) |
| double precision | float8 | double precision floating-point number (8 bytes) | [ Float ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#float)or[ String ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#string)([ flag ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#stringify-numeric-types)) |
| inet |  | IPv4 or IPv6 host address | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| integer | int, int4 | signed four-byte integer | [ Int ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#int) |
| interval[ fields ][ (p) ] |  | time span | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| json |  | textual JSON data | [ JSON ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#json) |
| jsonb |  | binary JSON data, decomposed | [ JSONB ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#jsonb) |
| line |  | infinite line on a plane | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| lseg |  | line segment on a plane | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| ltree |  | labels of data stored in a hierarchical tree-like structure | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| geometry |  | PostGIS Geometry type | [ Geometry ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#geometry) |
| geography |  | PostGIS Geography type | [ Geography ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#geography) |
| macaddr |  | MAC (Media Access Control) address | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| macaddr8 |  | MAC (Media Access Control) address (EUI-64 format) | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| money |  | currency amount | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| numeric[ (p, s) ] | decimal[ (p, s) ] | exact numeric of selectable precision | [ Numeric ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#numeric)or[ String ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#string)([ flag ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#stringify-numeric-types)) |
| path |  | geometric path on a plane | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| pg_lsn |  | PostgreSQL Log Sequence Number | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| point |  | geometric point on a plane | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| polygon |  | closed geometric path on a plane | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| real | float4 | single precision floating-point number (4 bytes) | [ Float ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#float) |
| smallint | int2 | signed two-byte integer | [ Int ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#int) |
| smallserial | serial2 | autoincrementing two-byte integer | [ Int ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#int) |
| serial | serial4 | autoincrementing four-byte integer | [ Int ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#int) |
| text |  | variable-length character string | [ String ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#string) |
| time[ (p) ][ without time zone ] |  | time of day (no time zone) | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| time[ (p) ]with time zone | timetz | time of day, including time zone | [ Timetz ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#timetz) |
| timestamp[ (p) ][ without time zone ] |  | date and time (no time zone) | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| timestamp[ (p) ]with time zone | timestamptz | date and time, including time zone | [ Timestamptz ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#timestamptz) |
| tsquery |  | text search query | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| tsvector |  | text search document | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| txid_snapshot |  | user-level transaction ID snapshot | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| uuid |  | universally unique identifier | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |
| xml |  | XML data | [ Implicit ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit) |


## Int​

GraphQL default scalar with name **Int** .

E.g.

```
objects :   [
   {
     int_col :   27
   }
]
```

## Float​

GraphQL custom scalar type with name **float8** .

E.g.

```
objects :   [
   {
     float_col :   0.8
   }
]
```

Note

To avoid loss of data when retrieving IEEE 754 style data from the database, please refer to the[ GraphQL Engine server config reference ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/)for instructions on setting the `extra_float_digits` parameter, which has a bad default value in PostgreSQL 11 and older.

## Numeric​

GraphQL custom scalar type with name **numeric** .

E.g.

```
objects :   [
   {
     numeric_col :   0.00000008
   }
]
```

Note

When using a[ numeric ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#numeric)value in an[ Action ](https://hasura.io/docs/latest/actions/overview/), the
value is[ coerced ](https://spec.graphql.org/October2021/#sec-Scalars.Input-Coercion)to its expected scalar type based
on type of the input value supplied (from the Action payload). As stated in the spec, a GraphQL service (such as Hasura)
will attempt to coerce numeric values to `Int` , `Float` , or `String` types, so long as its reasonable and doesn't result
in the loss of data. Otherwise, the service will throw an error.

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

## Char​

GraphQL custom scalar with name **character** . It is a `String` with single character.

E.g.

```
objects :   [
   {
     char_column :   "a"
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

## Date​

GraphQL custom scalar with name **date** . Date (no time of day). Allowed values are yyyy-mm-dd.

E.g.

```
objects :   [
   {
     date :   "1996-03-15"
   }
]
```

## Time with time zone​

GraphQL custom scalar type with name **timetz** . Time of day only, with time zone. Allowed values should be of ISO8601
format (e.g. 17:30:15Z, 17:30:15+05:30, 17:30:15.234890+05:30).

E.g.

```
objects :   [
   {
     time :   "17:30:15+05:30"
   }
]
```

## Timestamp with time zone​

GraphQL custom scalar type with name **timestamptz** . Both date and time, with time zone. Allowed values should be of
ISO8601 format (e.g. 2016-07-20T17:30:15Z, 2016-07-20T17:30:15+05:30, 2016-07-20T17:30:15.234890+05:30).

E.g.

```
objects :   [
   {
     timestamptz_col :   "2016-07-20T17:30:15+05:30"
   }
]
```

## JSON​

GraphQL custom scalar type with name **json** . It is a stringified json value.

E.g.

```
objects :   [
   {
     json_col :   "{ \"name\": \"raven\" }"
   }
]
```

## JSONB​

GraphQL custom scalar type with name **jsonb** . Value should be given through a variable of type **jsonb** .

E.g.

```
mutation   insert_test ( $value :   jsonb )   {
   insert_test ( objects :   [ {   jsonb_col :   $value   } ] )   {
     affected_rows
     returning   {
       jsonb_col
     }
   }
}
```

variables:

```
{
   "value" :   {
     "name" :   "raven"
   }
}
```

## Geometry​

GraphQL custom scalar type `geometry` is generated for a `GEOMETRY` column on a PostGIS enabled Postgres instance. Value
should be given as GeoJSON.

E.g.

```
mutation   insertGeometry ( $point :   geometry ! )   {
   insert_test ( objects :   [ {   geometry_col :   $point   } ] )   {
     affected_rows
     returning   {
       geometry_col
     }
   }
}
```

variables:

```
{
   "point" :   {
     "type" :   "Point" ,
     "coordinates" :   [ 0 ,   0 ]
   }
}
```

## Geography​

GraphQL custom scalar type `geography` is generated for a `GEOGRAPHY` column on a PostGIS enabled Postgres instance.
Value should be given as GeoJSON.

E.g.

```
mutation   insertGeography ( $point :   geography ! )   {
   insert_test ( objects :   [ {   geography_col :   $point   } ] )   {
     affected_rows
     returning   {
       geography_col
     }
   }
}
```

variables:

```
{
   "point" :   {
     "type" :   "Point" ,
     "coordinates" :   [ 0 ,   0 ]
   }
}
```

## Implicitly supported types​

All `Implicit` types in the[ above table ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#types-table)are implicitly supported by the GraphQL Engine. You have to
provide the value as a **String** .

E.g. For time without time zone type

In ISO 8601 format

```
objects :   [
   {
     time_col :   "04:05:06.789"
   }
]
```

E.g. For macaddr type

```
objects :   [
   {
     macaddr_col :   "08:00:2b:01:02:03"
   }
]
```

Typically, implicit types only support reading and writing, but not more complex operations such as boolean comparisons
(except for equality) or aggregations.

Note

You can learn more about PostgreSQL data types[ here ](https://www.postgresql.org/docs/current/static/datatype.html).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#types-table)
- [ Int ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#int)
- [ Float ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#float)
- [ Numeric ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#numeric)
- [ Bool ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#bool)
- [ Char ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#char)
- [ String ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#string)
- [ Date ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#date)
- [ Time with time zone ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#timetz)
- [ Timestamp with time zone ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#timestamptz)
- [ JSON ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#json)
- [ JSONB ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#jsonb)
- [ Geometry ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#geometry)
- [ Geography ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#geography)
- [ Implicitly supported types ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#string/#implicit)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)