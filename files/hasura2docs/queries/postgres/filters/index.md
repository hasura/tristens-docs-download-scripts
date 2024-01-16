# Postgres: Filter Query Results / Search Queries

## Introduction​

Hasura provides a powerful yet simple syntax to filter query results on Postgres. This is useful for building search
queries or filtering data based on some criteria. You can utilize arguments and operators to filter results based on
equality, comparison, pattern matching, etc.

## The where argument​

You can use the `where` argument in your queries to filter results based on some field’s values (even nested objects'
fields). You can even use multiple filters in the same `where` clause using the `_and` or the `_or` operators.

For example, to fetch data for an author whose name is "Sidney":

```
query   {
   authors ( where :   {   name :   {   _eq :   "Sidney"   }   } )   {
     id
     name
   }
}
```

You can also use nested objects' fields to filter rows from a table and also filter the nested objects as well.

For example, to fetch a list of authors who have articles with a rating greater than 4 along with those articles:

```
query   {
   authors ( where :   {   articles :   {   rating :   {   _gt :   4   }   }   } )   {
     id
     name
     articles ( where :   {   rating :   {   _gt :   4   }   } )   {
       id
       title
       rating
     }
   }
}
```

Here `_eq` and `_gt` are examples of comparison operators that can be used in the `where` argument to filter on
equality.

You can see the complete specification of the `where` argument in the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#whereexp).

## Filter nested objects​

The `where` argument can be used in **array relationships** as well to filter the nested objects. **Object
relationships** have only one nested object and hence they do not expose the `where` argument.

 **Example:** 

Fetch all authors with only their 5 rated articles:

## Supported operators​

| Operator | Use case |
|---|---|
| [ Simple Comparison Operators ](https://hasura.io/docs/latest/queries/postgres/filters/comparison-operators/) | Utilize comparison operators to selectively filter results by evaluating a field against a specific value. |
| [ Boolean Operators ](https://hasura.io/docs/latest/queries/postgres/filters/boolean-operators/) | Employ boolean operators to refine result filters based on logical expressions. |
| [ Text Search Operators ](https://hasura.io/docs/latest/queries/postgres/filters/text-search-operators/) | Apply text search operators to narrow down results according to the presence of text in a field. |
| [ JSONB Operators ](https://hasura.io/docs/latest/queries/postgres/filters/jsonb-operators/) | Utilize JSONB operators to fine-tune result filters using JSONB fields and navigating nested objects. |
| [ PostGIS Operators ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/) | Leverage PostGIS operators to narrow results based on geographical location data. |
| [ ltree Operators ](https://hasura.io/docs/latest/queries/postgres/filters/ltree-operators/) | Utilize ltree operators to filter results using hierarchical ltree data. |
| [ Nested Objects ](https://hasura.io/docs/latest/queries/postgres/filters/using-nested-objects/) | Navigate and filter results using nested object structures for advanced filtering. |
| [ Computed Fields ](https://hasura.io/docs/latest/queries/postgres/filters/using-computed-fields/) | Filter results based on dynamically computed fields that derive from existing data. |


## Cast a field to a different type before filtering (_cast)​

The `_cast` operator can be used to cast a field to a different type, which allows type-specific operators to be used on
fields that otherwise would not support them.

Currently, only the following type casts are supported:

- between PostGIS `geometry` and `geography` types
- from Postgres `jsonb` type to `string` type.


Casting using `_cast` corresponds directly to[ SQL type casts ](https://www.postgresql.org/docs/current/sql-expressions.html#SQL-SYNTAX-TYPE-CASTS).

 **Example: cast jsonb to string** 

Columns of type `jsonb` can be cast to `String` to use[ text operators ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#text-operators)on a `jsonb` field:

 **Example: cast geometry to geography** 

Filtering using `_st_d_within` over large distances can be inaccurate for location data stored in `geometry` columns.
For accurate queries, cast the field to `geography` before comparing:

 **Example: cast geography to geometry** 

Columns of type `geography` are more accurate, but they don’t support as many operations as `geometry` . Cast to `geometry` to use those operations in a filter:

Note

For performant queries that filter on casted fields, create an[ expression index ](https://www.postgresql.org/docs/current/indexes-expressional.html)on the casted column. For example,
if you frequently perform queries on a field `location` of type `geometry` casted to type `geography` , you should create
an index like the following:

`CREATE   INDEX  cities_location_geography  ON  cities  USING  GIST  ( ( location::geography ) ) ;`

## The TRUE expression ( { } )​

The expression `{}` evaluates to `true` if an object exists (even if it's `null` ).

 **For example** :

- any query with the condition `{ where: {} }` will return all objects without applying any filter.
- any query with the condition `{ where: { nested_object: {} } }` will return all objects for which atleast one `nested_object` exists.


## Evaluation of null values in comparison expressions​

In **versions v2.0.0 and above** , if in any comparison expression a `null` value is passed, a type mismatch error will
be thrown.

For example, the expression `{ where: {id: { _eq: null }}}` will throw an error.

In **versions v1.3.3 and below** , if in any comparison expression a `null` value is passed, the expression gets reduced
to `{}` , the[ TRUE expression ](https://hasura.io/docs/latest/queries/postgres/filters/index/#pg-true-expression).

For example, the expression `{ where: { id: {_eq: null }}}` will be reduced to `{ where: {id: {}} }` which will return
all objects for which an `id` is set, i.e. all objects will be returned.

This behavior can be preserved in versions v2.0.0 and above by setting the `HASURA_GRAPHQL_V1_BOOLEAN_NULL_COLLAPSE` env
var to `true` .

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/queries/postgres/filters/index/#introduction)
- [ The where argument ](https://hasura.io/docs/latest/queries/postgres/filters/index/#the-where-argument)
- [ Filter nested objects ](https://hasura.io/docs/latest/queries/postgres/filters/index/#pg-nested-filter)
- [ Supported operators ](https://hasura.io/docs/latest/queries/postgres/filters/index/#supported-operators)
- [ Cast a field to a different type before filtering (_cast) ](https://hasura.io/docs/latest/queries/postgres/filters/index/#cast-a-field-to-a-different-type-before-filtering-_cast)
- [ The TRUE expression ( { } ) ](https://hasura.io/docs/latest/queries/postgres/filters/index/#pg-true-expression)
- [ Evaluation of null values in comparison expressions ](https://hasura.io/docs/latest/queries/postgres/filters/index/#pg-null-value-evaluation)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)