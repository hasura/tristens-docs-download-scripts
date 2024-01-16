# Native Data Connector for PostgreSQL

The Native Data Connector for PostgreSQL is our flagship connector, with rich support for all kinds of queries.

Flavors of PostgreSQL

This connector works with most flavors of PostgreSQL — such as Yugabyte and Aurora — but has not been tested with all.
If you are looking for a connector for a specific flavor of PostgreSQL, you can search the[ Connector Hub ](https://hasura.io/connectors)or[ build your own ](https://hasura.io/docs/3.0/connectors/build-your-own-connector/).

## Configuration​

Subject to change

During this active development phase, the configuration structure is subject to change.

The connector will create an empty configuration as follows:

```
---
version :   1
connectionUri :
   uri :   ""
metadata :
   tables :   { }
   nativeQueries :   { }
   aggregateFunctions :   { }
   comparisonOperators :   { }
```

Once you enter your connection string for a PostgreSQL database and refresh your data source using the[ Hasura VS Code extension ](https://marketplace.visualstudio.com/items?itemName=HasuraHQ.hasura), the `"tables"` and `"aggregate_functions"` sections will be auto-populated based on the current state of the database.

These will always be regenerated from scratch.

### PostgreSQL connection URI​

The PostgreSQL database URL should follow the[ PostgreSQL connection URI form ](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING), which looks
like this:

`postgresql://[user[:password]@][host[:port]][/dbname][?param1=value2&param2=value2&...]`

Remember to encode any ambiguous characters using standard URI encoding. For example, if you have an `@` in your
username, it will need to be written as `%40` .

### Native Queries​

Native queries can be defined by adding them to the `"nativeQueries"` section. Each query is specified as SQL. The
return structure of the query must be explicitly specified in the `"columns"` field.

Native queries can take arguments using the `{{argument_name}}` syntax. Arguments must be specified along with their
type. The arguments are not interpolated, but provided to PostgreSQL as parameters, and therefore must be specific
values, not arbitrary SQL.

Here's an example which filters a table called `"Artist"` :

```
---
version :   1
connectionUri :
   uri :  postgresql : //alice@database.host
metadata :
   tables :   { }
   nativeQueries :
     artist_below_id :
       sql :  SELECT * FROM public."Artist" WHERE "ArtistId" <  { { id } }
       columns :
         ArtistId :
           name :  ArtistId
           type :  int4
         Name :
           name :  Name
           type :  varchar
       arguments :
         id :
           name :  id
           type :  int4
```

## Scalar types​

SQL data types are mapped to GraphQL types. The current mappings are as follows:

| SQL data type | GraphQL type |
|---|---|
|  `bool`  |  `Boolean`  |
|  `int2`  |  `Int`  |
|  `int4`  |  `Int`  |
|  `int8`  |  `Int`  |
|  `float4`  |  `Float`  |
|  `float8`  |  `Float`  |
|  `numeric`  |  `Float`  |
|  `char`  |  `String`  |
|  `varchar`  |  `String`  |
|  `text`  |  `String`  |
|  `uuid`  |  `String`  |
|  `date`  |  `String`  |
|  `time`  |  `String`  |
|  `timestamp`  |  `String`  |
|  `timestamptz`  |  `String`  |
|  `timetz`  |  `String`  |


Other SQL scalar types are unsupported, but may still work in certain situations.

Data type aliases

Note that many of these SQL data types have aliases in PostgreSQL, which can be found in the[ PostgreSQL documentation
on data types ](https://www.postgresql.org/docs/current/datatype.html).

## Nested types​

The connector does not currently support nested data structures, such as `array` , `hstore` , `json` , or `jsonb` , though
they may still work in certain situations.

## Queries​

The connector supports all query operations; see the[ query documentation ](https://hasura.io/docs/3.0/graphql-api/queries/)for details.

### Predicates​

The `_is_null` operator checks whether a value is `NULL` .

The following binary operators are supported when filtering:

| Name | GraphQL operator | PostgreSQL operator | GraphQL types |
|---|---|---|---|
| equals |  `_ eq`  |  `=`  | all |
| not equals |  `_ neq`  |  `<>`  | all |
| less than |  `_ lt`  |  `<`  | all |
| less than or equal to |  `_ lte`  |  `<=`  | all |
| greater than |  `_ gt`  |  `>`  | all |
| greater than or equal to |  `_ gte`  |  `>=`  | all |
| like |  `_ like`  |  `LIKE`  |  `String`  |
| not like |  `_ nlike`  |  `NOT LIKE`  |  `String`  |
| case-insensitive like |  `_ ilike`  |  `ILIKE`  |  `String`  |
| not case-insensitive like |  `_ nilike`  |  `NOT ILIKE`  |  `String`  |
| similar |  `_ similar`  |  `SIMILAR TO`  |  `String`  |
| not similar |  `_ nsimilar`  |  `NOT SIMILAR TO`  |  `String`  |
| regex |  `_ regex`  |  `~`  |  `String`  |
| not regex |  `_ nregex`  |  `!~`  |  `String`  |
| case-insensitive regex |  `_ iregex`  |  `~`  |  `String`  |
| not case-insensitive regex |  `_ niregex`  |  `!~`  |  `String`  |


The `_not` , `_and` , and `_or` operators all work as usual.

### What did you think of this doc?

- [ Configuration ](https://hasura.io/docs/3.0/connectors/postgresql/#configuration)
    - [ PostgreSQL connection URI ](https://hasura.io/docs/3.0/connectors/postgresql/#postgresql-connection-uri)

- [ Native Queries ](https://hasura.io/docs/3.0/connectors/postgresql/#native-queries)
- [ Scalar types ](https://hasura.io/docs/3.0/connectors/postgresql/#scalar-types)
- [ Nested types ](https://hasura.io/docs/3.0/connectors/postgresql/#nested-types)
- [ Queries ](https://hasura.io/docs/3.0/connectors/postgresql/#queries)
    - [ Predicates ](https://hasura.io/docs/3.0/connectors/postgresql/#predicates)
