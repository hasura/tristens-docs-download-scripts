# MS SQL Server: Filter Query Results / Search Queries

## Introduction​

Hasura provides a powerful yet simple syntax to filter query results on MS SQL Server. This is useful for building
search queries or filtering data based on some criteria. You can utilize arguments and operators to filter results based
on equality, comparison, pattern matching, etc.

## The where argument​

You can use the `where` argument in your queries to filter results based on some field's values (even nested objects'
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
| [ Simple Comparison Operators ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/comparison-operators/) | Utilize comparison operators to selectively filter results by evaluating a field against a specific value. |
| [ Boolean Operators ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/boolean-operators/) | Employ boolean operators to refine result filters based on logical expressions. |
| [ Text Search Operators ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/text-search-operators/) | Apply text search operators to narrow down results according to the presence of text in a field. |
| [ Geospatial Operators ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/geospatial-operators/) | Leverage geospatial operators to narrow results based on geographical location data. |
| [ Nested Objects ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/using-nested-objects/) | Navigate and filter results using nested object structures for advanced filtering. |


## The TRUE expression ( { } )​

The expression `{}` evaluates to `true` if an object exists (even if it's `null` ).

 **For example** :

- any query with the condition `{ where: {} }` will return all objects without applying any filter.
- any query with the condition `{ where: { nested_object: {} } }` will return all objects for which atleast one `nested_object` exists.


## Evaluation of null values in comparison expressions​

If in any comparison expression a `null` value is passed, a type mismatch error will be thrown.

For example, the expression `{ where: {id: { _eq: null }}}` will throw an error.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/index/#introduction)
- [ The where argument ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/index/#the-where-argument)
- [ Filter nested objects ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/index/#ms-sql-server-nested-filter)
- [ Supported operators ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/index/#supported-operators)
- [ The TRUE expression ( { } ) ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/index/#ms-sql-server-true-expression)
- [ Evaluation of null values in comparison expressions ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/index/#ms-sql-server-null-value-evaluation)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)