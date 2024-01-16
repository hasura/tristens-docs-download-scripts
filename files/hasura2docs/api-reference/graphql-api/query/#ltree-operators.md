# API Reference - Query / Subscription

## Overview​

The Hasura GraphQL API exposes a set of GraphQL queries so that you can get started with building your application right
away. The queries are[ auto-generated ](https://hasura.io/docs/latest/getting-started/how-it-works/index/#tracking-tables--schema-generation)by
Hasura based on the tables and relationships in your database.

Below, you'll find the overviews and syntax definitions for queries and subscriptions.

## Query / Subscription syntax​

Each query / subscription is a GraphQL object with a set of fields. The fields are auto-generated based on the tables
and relationships in your database. An **object** is - as the name suggests - an object, which can have multiple fields
of its own. Objects can return complex data structures, including nested objects and arrays. Alternatively, **object
fields** are scalar values (e.g., string, integer, boolean, etc.) that do not contain any nested objects or arrays.

```
query|subscription [<op-name>] {
  object [([argument])]{
    object-fields
  }
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
| op-name |  `false`  | Value | The user-generated name of the query / subscription; useful for observability and analyzing operations. |
| object |  `true`  | [ Object ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#object) | The name of the table / object on which to perform the operation. |
| argument |  `false`  | [ Argument ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#argument) | One or more of filter criteria, or instructions for ordering, pagination, etc. |


### Query example​

In the example below, the query retrieves the `id` and `name` fields of all authors whose articles have a rating of 4 or
higher. The results are ordered by the `name` field in ascending order.

```
query   AuthorQuery   {
   author ( where :   {   articles :   {   rating :   {   _gte :   4   }   }   } ,   order_by :   {   name :   asc   } )   {
     id
     name
   }
}
```

Referencing the table above, the author is the object, and `id` and `name` are the object fields. The arguments are `where` and `order_by` .

### Subscription example​

In this example, we're executing the exact same logic as above, but as a subscription. The subscription will re-deliver
all the results of the query whenever there is a change in the data that matches the query criteria.

```
subscription   AuthorSubscription   {
   author ( where :   {   articles :   {   rating :   {   _gte :   4   }   }   } ,   order_by :   {   name :   asc   } )   {
     id
     name
   }
}
```

Note

For more examples and details of usage, please see[ this ](https://hasura.io/docs/latest/queries/postgres/index/).

## By PK syntax​

 `query_by_pk` / `subscription_by_pk` are special queries / subscriptions that can be used to fetch a single row from a
table by its **primary key** . The primary key is specified as an argument to the query / subscription.

```
query|subscription [<op-name>] {
  <query-field-name> (
    column1: value1
    column2: value2
  )
  <object-fields>
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
| op-name |  `false`  | Value | The name of the query / subscription; useful for observability and analyzing operations. |
| query-field-name |  `true`  | Value | The name of the auto-generated query field (e.g. `article_ by_ pk` ). |
| column1 |  `true`  | Value | The argument for the primary key column's name. |


### Query by PK example​

This GraphQL query retrieves the `id` and `title` fields of the article with `id` of `1` . The primary key id is passed
as an argument to the `article_by_pk` field. The desired fields to retrieve from the article record, `id` and `title` ,
are specified in the `object-fields` section of the query.

```
query   GetSingleAuthor   {
   article_by_pk ( id :   1 )   {
     id
     title
   }
}
```

### Subscription by PK example​

In this example, we're executing the exact same logic as above, but as a subscription. The subscription will trigger
whenever there is a change in the data that matches the query criteria.

```
subscription   GetSingleAuthor   {
   article_by_pk ( id :   1 )   {
     id
     title
   }
}
```

## Syntax definitions​

Below, you'll find the syntax definitions for the various components of a query / subscription. The syntax definitions
are grouped by the type of component.

### Object​

An object is a table or a view in your database. Objects can be simple or aggregates. **Simple objects** typically represent a single record in a table. **Aggregate objects** typically represent a group of records in a table grouped by an aggregate
function applied to a specified column.

#### Simple object​

Below, you'll find the syntax definition for a simple object. Simple objects are tables or views in your database that
can have multiple fields of their own. Simple objects can return complex data structures, including nested objects and
arrays.

```
object-name {
  field1
  field2
  json_field[(path: String)]
  ..
  nested object1
  nested object2
  aggregate nested object1
  ..
}
```

Here's a breakdown of some of the key components of the syntax definition:

| Key | Required | Schema | Description |
|---|---|---|---|
| field |  `false`  | Value | The name of the column in the table / view which returns a scalar value. |
| nested object |  `false`  | [ Object ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#object) | A reference to another object via a relationship that contains multiple fields. |
| json_field |  `false`  | Value | The name of the column in the table / view which returns a JSON value. |
| path | false | Value |  `path` argument of `json` / `jsonb` follows simple[ JSONPath specification ](https://github.com/json-path/JsonPath). However, prefix symbol `$.` is optional. |
| aggregate nested object |  `false`  | [ Aggregate object ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#aggregateobject) | A reference to an aggregate object. |


Below, you'll find an example of a simple object based on the definition above:

```
author   {
    id    # scalar integer field
    name    # scalar text field
    address ( path :   "$.city" )   # scalar JSON field -> property
    address ( path :   "$.city.altitude" )   # scalar JSON field -> property -> property
    address ( path :   "city" )   # scalar JSON field -> property; '$.' prefix is optional
    contacts ( path :   "[0]" )   # scalar JSON field -> array_item
    contacts ( path :   "[0].phone" )   # scalar JSON field -> array_item_property
    contacts ( path :   "['Hello world!']" )   # scalar JSON field -> property; used for special characters key
    contacts ( path :   "[\"Hello world!\"]" )   # same as above; the syntax is ugly, but still works
    article   {    # nested object
      title
    }
    article_aggregate   {    # aggregate nested object
      aggregate   {
        count
      }
      nodes   {
        title
      }
    }
}
```

#### Aggregate object​

Aggregate objects represent a group of records in a table grouped by an aggregate function applied to a specified
column. These are useful for performing aggregate queries on your data (e.g. `count` , `sum` , `avg` , etc.) and
simplifying your frontend code. For more details on aggregate functions, refer to the[ Postgres docs ](https://www.postgresql.org/docs/current/functions-aggregate.html#FUNCTIONS-AGGREGATE-STATISTICS-TABLE).

```
object-name_aggregate {
  aggregate {
    count
    sum {
      field
      ..
    }
    avg {
      field
      ..
    }
    stddev {
      field
      ..
    }
    stddev_samp {
      field
      ..
    }
    stddev_pop {
      field
      ..
    }
    variance {
      field
      ..
    }
    var_samp {
      field
      ..
    }
    var_pop {
      field
      ..
    }
    max {
      field
      ..
    }
    min {
      field
      ..
    }
  nodes {
    field1
    field2
    ..
    nested object1
    nested object2
    aggregate nested object1
    ..
  }
}
```

Here's a breakdown of some of the key components of the syntax definition:

| Key | Required | Schema | Description |
|---|---|---|---|
| aggregate |  `true`  | [ Aggregate ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#aggregate) | The aggregate function to apply to the specified column. |
| count |  `false`  | Value | The number of records in the table. |
| sum |  `false`  | Value | The sum of the values in the specified column. |
| avg |  `false`  | Value | The average of the values in the specified column. |
| stddev |  `false`  | Value | The standard deviation of the values in the column. |
| stddev_samp |  `false`  | Value | The sample standard deviation of the values in the column. |
| stddev_pop |  `false`  | Value | The population standard deviation of the values in the column. |
| variance |  `false`  | Value | The variance of the values in the column. |
| var_samp |  `false`  | Value | The sample variance of the values in the column. |
| var_pop |  `false`  | Value | The population variance of the values in the column. |
| max |  `false`  | Value | The maximum value in the column. |
| min |  `false`  | Value | The minimum value in the column. |
| nodes |  `true`  | [ Object ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#object) | A reference to another object via a relationship that contains multiple fields. |


Below, you'll find an example of an aggregate object based on the definition above:

### Argument​

An argument is a value passed to a field. Arguments can be simple or complex. Within Hasura, you can use four types of
arguments:

| Argument type | GraphQL expression | Description |
|---|---|---|
| [ DistinctOnExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#distinctonexp) |  `distinct_ on`  | A distinct on expression that specifies the columns on which to apply the distinct operator |
| [ WhereExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#whereexp) |  `where`  | A where expression that specifies the filter criteria |
| [ OrderByExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#orderbyexp) |  `order_ by`  | An order by expression that specifies the sort order |
| [ PaginationExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#paginationexp) |  `offset: <OFFSET>, limit: <LIMIT>`  | A pagination expression that specifies the limit and offset |


#### DistinctOnExp​

The distinct on expression specifies the columns on which to apply the distinct operator. This is useful for eliminating
duplicate rows in the result set.

```
distinct_on: [
[ TableSelectColumnEnum ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#tableselectcolumnenum)
]
```

 *Example* 

```
query   {
   article ( distinct_on :   title )   {
     title
     content
   }
}
```

In the example above, the `title` column is used to eliminate duplicate rows in the result set. Our query will return
only one row for each unique title.

##### TableSelectColumnEnum​

```
# example table_select_column enum for "article" table
enum   article_select_column   {
   id
   title
   content
   author_id
   is_published
}
```

#### WhereExp​

The where expression specifies the filter criteria. This is useful for filtering the result set to only include records
that match the specified criteria.

```
where:
[ BoolExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#boolexp)
```

 *Example* 

```
query   {
   author ( where :   {   rating :   {   _gt :   4   }   } )   {
     name
     articles   {
       title
     }
   }
}
```

In the example above, the `author` field is filtered to only include authors with a rating greater than 4.

##### BoolExp​

The boolean expression is used to filter the result set by a specified criteria. It can be used in conjunction with
other boolean expressions to create complex filters. Hasura makes the following boolean expressions available:

| Boolean expression | GraphQL expression | Description |
|---|---|---|
| [ AndExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#andexp) |  `_ and`  | A boolean expression that specifies the logical AND operator. |
| [ OrExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#orexp) |  `_ or`  | A boolean expression that specifies the logical OR operator. |
| [ NotExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#notexp) |  `_ not`  | A boolean expression that specifies the logical NOT operator. |
| [ TrueExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#trueexp) |  `Boolean!`  | A boolean expression that specifies the logical TRUE operator. |
| [ ColumnExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#columnexp) |  `<columnName>`  | A boolean expression that specifies a column. |
| [ AggregationExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#aggregationexp) |  `<relationship>_ aggregate`  | A boolean expression that specifies an aggregation on an array relationship. |


###### AndExp​

The `_and` expression specifies the logical AND operator. You can use the `_and` operator to combine multiple boolean
expressions into a single expression where all expressions must evaluate to true.

```
{
  _and: [
[ BoolExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#boolexp)
]
}
```

In the example below, the `article` field is filtered to only include articles with a rating greater than 4 and a
publication date greater than 2018-01-01.

```
query   {
   article ( where :   {   _and :   [ {   rating :   {   _gt :   4   }   } ,   {   published_on :   {   _gt :   "2018-01-01"   }   } ]   } )   {
     title
     content
   }
}
```

Syntactic sugar

You can simplify an `_and` expression by passing the sub-expressions separated by a `,` .

 **First example:  _ and expression with different fields** 

```
{
   _and :   [
     {   rating :   {   _gte :   4   }   } ,
     {   published_on :   {   _gte :   "2018-01-01"   }   }
   ]
}
# can be simplified to:
{
   rating :   {   _gte :   4   } ,
   published_on :   {   _gte :   "2018-01-01"   }
}
```

 **Second example:  _ and expression with same field** 

```
_and :   [
   {
     rating :   {
       _gt :   1
     }
   } ,
   {
     rating :   {
       _lt :   5
     }
   }
]
# can be simplified to:
rating :   {
   _gt :   1 ,
   _lt :   5
}
```

###### OrExp​

The `_or` expression specifies the logical OR operator. You can use the `_or` operator to combine multiple boolean
expressions into a single expression where at least one of the sub-expressions must evaluate to true.

```
{
  _or: [
[ BoolExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#boolexp)
]
}
```

In the example below, the `article` field is filtered to only include articles with a rating greater than 4 or that are
published.

```
query   {
   article ( where :   {   _or :   [ {   rating :   {   _gt :   4   }   } ,   {   is_published :   {   _eq :   true   }   } ]   } )   {
     title
     content
   }
}
```

Note

The `_or` operator expects an array of expressions as input. Passing an object to it will result in the behavior of the `_and` operator due to the way[ GraphQL list input coercion ](https://graphql.github.io/graphql-spec/June2018/#sec-Type-System.List)behaves.

 *Example:* 

```
{
   _or :   {
    rating :   {   _gte :   4   } ,
    published_on :   {   _gte :   "2018-01-01"   }
   }
}
# will be coerced to:
{
   _or :   [
     {
       rating :   {   _gte :   4   } ,
       published_on :   {   _gte :   "2018-01-01"   }
     }
   ]
}
# which is equivalent to:
{
   _or :   [
     _and :   [
       {   rating :   {   _gte :   4   }   } ,
       {   published_on :   {   _gte :   "2018-01-01"   }   }
     ]
   ]
}
```

###### NotExp​

The `_not` expression specifies the logical NOT operator. You can use the `_not` operator to negate a boolean
expression. This is useful when you want to filter out results that match a certain criteria.

```
{
  _not:
[ BoolExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#boolexp)
}
```

In the example below, the `article` field is filtered to only include articles with a title that is not an empty string.
Effectively, this will filter out articles with an empty title.

```
query   {
   article ( where :   {   _not :   {   title :   {   _eq :   ""   }   }   } )   {
     title
     content
   }
}
```

###### TrueExp​

The `_true` expression specifies the logical TRUE operator. You can use the `_true` operator to return all rows in a
table which match the specified criteria.

`{}`

In the example below, the `author` field is filtered to only include authors that have at least one article.
Essentially, we're saying "return all authors if articles is `true` ."

```
query   {
   author ( where :   {   articles :   { }   } )   {
     name
   }
}
```

Note

 `{}` evaluates to true whenever an object exists (even if it's `null` ).

###### ColumnExp​

The `_col` expression specifies a column. You can use the `_col` operator to reference a column in a table. In the
definition below, the `field-name` is the name of the column.

```
{
  field-name: {
[ Operator ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#operator)
: Value }
}
```

In the example below, the `article` field is filtered to only include articles with a title that is equal to "GraphQL
Tutorial".

```
query   {
   article ( where :   {   title :   {   _eq :   "GraphQL Tutorial"   }   } )   {
     title
     content
   }
}
```

###### Operator​

Operators are used to compare a column value with a specified value. The following operators are available:

 **Generic operators (all column types except json, jsonb):** 

| Operator | PostgreSQL equivalent |
|---|---|
|  `_ eq`  |  `=`  |
|  `_ neq`  |  `<>`  |
|  `_ gt`  |  `>`  |
|  `_ lt`  |  `<`  |
|  `_ gte`  |  `>=`  |
|  `_ lte`  |  `<=`  |
|  `_ in`  |  `IN`  |
|  `_ nin`  |  `NOT IN`  |


(For more details, refer to the Postgres docs for[ comparison operators ](https://www.postgresql.org/docs/current/functions-comparison.html)and[ list based search operators ](https://www.postgresql.org/docs/current/functions-comparisons.html).)

 **Text related operators:** 

| Operator | PostgreSQL equivalent |
|---|---|
|  `_ like`  |  `LIKE`  |
|  `_ nlike`  |  `NOT LIKE`  |
|  `_ ilike`  |  `ILIKE`  |
|  `_ nilike`  |  `NOT ILIKE`  |
|  `_ similar`  |  `SIMILAR TO`  |
|  `_ nsimilar`  |  `NOT SIMILAR TO`  |
|  `_ regex`  |  `~`  |
|  `_ iregex`  |  `~*`  |
|  `_ nregex`  |  `!~`  |
|  `_ niregex`  |  `!~*`  |


(For more details on text related operators, refer to the[ Postgres docs ](https://www.postgresql.org/docs/current/functions-matching.html).)

 **Checking for NULL values:** 

| Operator | PostgreSQL equivalent |
|---|---|
|  `_ is_ null` (takes true/false as values) |  `IS NULL`  |


(For more details on the `IS NULL` expression, refer to the[ Postgres docs ](https://www.postgresql.org/docs/current/functions-comparison.html).)

 **Type casting:** 

| Operator | PostgreSQL equivalent |
|---|---|
|  `_ cast` (takes a[ CastExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#castexp)as a value) |  `::`  |


(For more details on type casting, refer to the[ Postgres docs ](https://www.postgresql.org/docs/current/sql-createcast.html).)

 **JSONB operators:** 

| Operator | PostgreSQL equivalent |
|---|---|
|  `_ contains`  |  `@>`  |
|  `_ contained_ in`  |  `<@`  |
|  `_ has_ key`  |  `?`  |
|  `_ has_ keys_ any`  |  `?!`  |
|  `_ has_ keys_ all`  |  `?&`  |


(For more details on JSONB operators, refer to the[ Postgres docs ](https://www.postgresql.org/docs/current/static/functions-json.html#FUNCTIONS-JSONB-OP-TABLE).)

 **PostGIS related operators on GEOMETRY columns:** 

| Operator | PostGIS equivalent |
|---|---|
|  `_ st_ contains`  |  `ST_ Contains(column, input)`  |
|  `_ st_ crosses`  |  `ST_ Crosses(column, input)`  |
|  `_ st_ equals`  |  `ST_ Equals(column, input)`  |
|  `_ st_ intersects`  |  `ST_ Intersects(column, input)`  |
|  `_ st_ overlaps`  |  `ST_ Overlaps(column, input)`  |
|  `_ st_ touches`  |  `ST_ Touches(column, input)`  |
|  `_ st_ within`  |  `ST_ Within(column, input)`  |
|  `_ st_ d_ within`  |  `ST_ DWithin(column, input)`  |


(For more details on spatial relationship operators, refer to the[ PostGIS docs ](http://postgis.net/workshops/postgis-intro/spatial_relationships.html).)

Note

- All operators take a JSON representation of `geometry/geography` values as input value.
- The input value for `_st_d_within` operator is an object:


All operators take a JSON representation of `geometry/geography` values as input value.

The input value for `_st_d_within` operator is an object:

```
{
  field-name : {_st_d_within: {distance: Float, from: Value} }
}
```

 **Intersect Operators on RASTER columns:** 

| Operator | PostgreSQL equivalent | Input object |
|---|---|---|
|  `_ st_ intersects_ rast`  |  `ST_ Intersects(column, value)`  |  `{ _ st_ intersects_ rast: raster }`  |
|  `_ st_ intersects_ nband_ geom`  |  `ST_ Intersects(column, nband, geommin)`  |  `{ _ st_ intersects_ nband_ geom: {nband: Integer! geommin: geometry!}`  |
|  `_ st_ intersects_ geom_ nband`  |  `ST_ Intersects(column, geommin, nband)`  |  `{ _ st_ intersects_ geom_ nband: {geommin: geometry! nband: Integer }`  |


(For more details on intersect operators on `raster` columns refer to the[ PostGIS docs ](https://postgis.net/docs/RT_ST_Intersects.html).)

 **ltree operators:** 

| Operator | PostgreSQL equivalent |
|---|---|
|  `_ ancestor`  |  `@>`  |
|  `_ ancestor_ any`  |  `@>`  |
|  `_ descendant`  |  `<@`  |
|  `_ descendant_ any`  |  `<@`  |
|  `_ matches`  |  `~`  |
|  `_ matches_ any`  |  `?`  |
|  `_ matches_ fulltext`  |  `@`  |


(For more details on operators on `ltree` columns refer to the[ Postgres docs ](https://www.postgresql.org/docs/current/ltree.html).)

###### CastExp​

```
{ type-name: {
[ Operator ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#operator)
: Value} }
```

 *Example* 

```
query   MyQuery ( $coordinate :   geography ! )   {
   postgis_test_table (
     where :   {
       geometry_column :   {
         _cast :   {
           geography :   {   _st_d_within :   {   distance :   1000000 ,   from :   $coordinate   }   }
         }
       }
     }
   )   {
     id
   }
}
Variables :
{
   "coordinate" :   {
     "type" :   "Point" ,
     "coordinates" :   [   2.5559 ,   49.0083   ]
   }
}
```

Note

Currently, only the following type casts are supported:

- between PostGIS `geometry` and `geography` types
- from Postgres `jsonb` type to `string` type.


###### AggregationExp​

The `AggregationExp` type is used to specify aggregation predicates in the `where` clause of a query. This requires an
array relationship.

```
{
  field-name_aggregate: {
[ AggregationPredicate ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#aggregationPredicate)
}
}
```

Note that each `field-name_aggregate` object may refer to only one aggregation predicate. Multiple aggregation
predicates can be specified via the `_and` operator, however.

In the following example, we query for restaurants that have an average review rating greater than 5. The `where` clause
specifies an aggregation predicate on the `reviews` field, which is of type `review_aggregate` .

```
query   RestaurantsWithHighRatings   {
   restaurant ( where :   {   reviews_aggregate :   {   average :   {   arguments :   "rating" ,   predicate :   {   _gt :   5   }   }   }   } )   {
     name
   }
}
```

#### AggregationPredicate​

The `AggregationPredicate` type is used to specify aggregation predicates in the `where` clause of a query. It is
composed of an aggregation function and a predicate.

```
function-name: {
    arguments: (column-name | [column-name] | { argument-name: column-name })
    distinct: true | false
    filter:
[ BoolExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#boolexp)
predicate:
[ Operator ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#operator)
}
```

Aggregation functions may differ in the `arguments` that they support. For instance, `count` may take an arbitrary
number of arguments, while `sum` takes exactly one. Certain functions take named arguments.

The functions supported are specific to each backend.

 *Examples* 

```
   average :   {
     arguments :   "rating" ,
     predicate :   {   _gt :   5   }
   }
```

```
   count :   {
     arguments :   [ ]
     predicate :   {   _gt :   10   }
   }
```

```
   count :   {
     arguments :   [ "name" ,   "id" ]
     predicate :   {   _gt :   10   }
   }
```

```
   corr :   {
     arguments :   {   X :   "age" ,   Y :   "score"   }
     predicate :   {   _gt :   0.6   }
   }
```

#### OrderByExp​

The `OrderByExp` type is used to specify ordering in the `order_by` clause of a query.

```
order_by: (
[ TableOrderBy ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#tableorderby)
| [
[ TableOrderBy ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#tableorderby)
])
```

In the example below, we query for articles, ordered by their rating in descending order.

```
query   ArticlesOrderedByRating   {
   article ( order_by :   {   rating :   desc   } )   {
     name
     rating
   }
}
```

Here, we query for articles, ordered by their rating in descending order, and then by their author's id in ascending
order.

```
query   ArticlesOrderedByRatingAndAuthorId   {
   article ( order_by :   [ {   id :   desc   } ,   {   author :   {   id :   asc   }   } ] )   {
     title
     rating
   }
}
```

##### TableOrderBy​

 `TableOrderBy` is a composite type that consists of one or more fields, each of which specifies the order in which query
results should be sorted.

 **For columns** 

```
{ column:
[ OrderByEnum ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#orderbyenum)
}
```

In the example below, we query for articles, ordered by their rating in ascending order:

```
query   {
   article ( order_by :   {   rating :   asc   } )   {
     title
     content
   }
}
```

 **For object relations** 

```
{ relation-name:
[ TableOrderBy ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#tableorderby)
}
```

Here, we query for articles, ordered by their author's rating in descending order:

```
query   {
   article ( order_by :   {   author :   {   rating :   desc   }   } )   {
     title
     content
   }
}
```

 **For array relations aggregate** 

```
{ relation-name_aggregate:
[ AggregateOrderBy ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#aggregateorderby)
}
```

Below, we query for authors, ordered by the maximum rating of their articles in ascending order:

```
query   {
   author ( order_by :   {   articles_aggregate :   {   max :   {   rating :   asc   }   }   } )   {
     name
   }
}
```

 **For computed fields** 

Returning scalar values:

```
{ computed-field-name:
[ OrderByEnum ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#orderbyenum)
}
```

Returning set of table rows:

```
{ computed-field-name:
[ TableOrderBy ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#tableorderby)
}
```

```
{ computed-field-name_aggregate:
[ AggregateOrderBy ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#aggregateorderby)
}
```

Order by type for `article` table:

```
input   article_order_by   {
   id :   order_by
   title :   order_by
   content :   order_by
   author_id :   order_by
   #order by using "author" object relationship columns
   author :   author_order_by
   #order by using "likes" array relationship aggregates
   likes_aggregate :   likes_aggregate_order_by
}
```

 **For computed fields returning scalar type** 

```
{ computed-field-name:
[ OrderByEnum ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#orderbyenum)
}
```

Consider a table `student` contains integer columns for course subjects to store marks. A computed field with the name `total_marks` defined to calculate sum of all subject marks. We need to fetch `student` rows sorted by `total_marks` .

```
query   StudentsOrderByTotalMarks   {
   student ( order_by :   {   total_marks :   desc   } )   {
     id
     name
     total_marks
   }
}
```

 **For computed fields returning table row type** 

Computed fields returning set of table rows can be used to sort the query by their aggregate fields.

```
{ computed-field-name_aggregate:
[ AggregateOrderBy ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#aggregateorderby)
}
```

A computed field `get_articles` is defined on the `author` table which returns set of `article` table rows. Fetch
authors sorted by the count of their articles.

```
query   AuthorsOrderByArticleCount   {
   author ( order_by :   {   get_articles_aggregate :   {   count :   desc   }   } )   {
     id
     name
     get_articles   {
       id
       title
       content
     }
   }
}
```

###### OrderByEnum​

We can use the `order_by` enum type to specify the order in which query results should be sorted.

```
#the order_by enum type
enum   order_by   {
   #in the ascending order, nulls last
   asc
   #in the ascending order, nulls last
   asc_nulls_last
   #in the ascending order, nulls first
   asc_nulls_first
   #in the descending order, nulls first
   desc
   #in the descending order, nulls first
   desc_nulls_first
   #in the descending order, nulls last
   desc_nulls_last
}
```

In the example below, we query for articles, ordered by their rating in ascending order:

```
query   ArticleOrderByRating   {
   article ( order_by :   {   rating :   asc   } )   {
     title
     content
   }
}
```

###### AggregateOrderBy​

We can use the `aggregate_order_by` enum type to specify the order in which query results should be sorted.

 **Count aggregate** 

```
{ count:
[ OrderByEnum ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#orderbyenum)
}
```

In this example, we query for authors, ordered by the count of their articles in descending order:

```
query   AuthorOrderByArticleCount   {
   author ( order_by :   {   articles_aggregate :   {   count :   desc   }   } )   {
     name
   }
}
```

 **Operation aggregate** 

The `operation` aggregate type is used to specify the order in which query results should be sorted.

```
{ op_name:
[ TableAggOpOrderBy ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#tableaggoporderby)
}
```

Below, we query for authors, ordered by the sum of their article ids in descending order:

```
query   AuthorOrderBySumOfArticles   {
   author ( order_by :   {   articles_aggregate :   {   sum :   {   id :   desc   }   }   } )   {
     id
   }
}
```

Available operations are `sum` , `avg` , `max` , `min` , `stddev` , `stddev_samp` , `stddev_pop` , `variance` , `var_samp` and `var_pop` .

###### TableAggOpOrderBy​

 `table_agg_op_order_by` is a type used to specify the order in which the aggregate query results should be returned. It
is used as an argument to the `order_by` field of an aggregate query.

```
{ column:
[ OrderByEnum ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#orderbyenum)
}
```

In the example below, we query for an `orders_aggregate` , ordered by the sum of their total_price in descending order:

```
query   AggregateOrderBy   {
   orders_aggregate ( order_by :   {   sum_total_price :   desc   } )   {
     aggregate   {
       sum   {
         total_price
       }
     }
     nodes   {
       customer_id
     }
   }
}
```

#### PaginationExp​

Pagination expression is used to paginate the query results. It is used as an argument to the `limit` and `offset` fields of a query.

```
limit: Integer
[offset: Integer]
```

In this final example, we query for articles, limiting the results to 6 rows, and skipping the first 2 rows:

```
query   ArticlesPagination   {
   article ( limit :   6 ,   offset :   2 )   {
     title
     content
   }
}
```

### What did you think of this doc?

- [ Overview ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#overview)
- [ Query / Subscription syntax ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#query--subscription-syntax)
    - [ Query example ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#query-example)

- [ Subscription example ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#subscription-example)
- [ By PK syntax ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#by-pk-syntax)
    - [ Query by PK example ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#query-by-pk-example)

- [ Subscription by PK example ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#subscription-by-pk-example)
- [ Syntax definitions ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#syntax-definitions)
    - [ Object ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#object)

- [ Argument ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators/#argument)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)