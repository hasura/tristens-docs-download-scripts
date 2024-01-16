# BigQuery: Filter Based on Fields of Nested Objects

## Introduction​

The `where` argument can be used in **array relationships** as well to filter the nested objects. **Object
relationships** have only one nested object and hence they do not expose the `where` argument.

 **Example:** 

Fetch all authors with only their 5 rated articles:

## Filter based on nested objects' fields​

You can use the fields of nested objects as well to filter your query results.

For example:

```
query   {
   bigquery_articles ( where :   {   author :   {   name :   {   _eq :   "Sidney"   }   }   } )   {
     id
     title
   }
}
```

The behavior of the comparison operators depends on whether the nested objects are a single object related via an object
relationship or an array of objects related via an array relationship.

- In case of an **object relationship** , a row will be returned if the single nested object satisfies the defined
condition.
- In case of an **array relationship** , a row will be returned if **any of the nested objects** satisfy the defined
condition.


Limitations

 **This is only supported for local relationships** , such as relationships between two local database tables. **This is
not supported for remote relationships** , such as remote database relationships or Remote Schema relationships.

Let's look at a few use cases based on the above:

## Fetch if the single nested object defined via an object relationship satisfies a condition​

 **Example:** 

Fetch all articles whose author's name starts with "A":

## Fetch if any of the nested objects defined via an array relationship satisfy a condition​

 **Example:** 

Fetch all authors which have written at least one article which is rated 1:

## Fetch if all of the nested objects defined via an array relationship satisfy a condition​

By default a row is returned if any of the nested objects satisfy a condition. To achieve the above, we need to frame
the `where` expression as `{_not: {inverse-of-condition}}` . This reads as: fetch if not (any of the nested objects
satisfy the inverted condition) i.e. all of the nested objects satisfy the condition.

For example:

| condition | where expression |
|---|---|
|  `{object: {field: {_ eq: "value"}}}`  |  `{_ not: {object: {field: {_ neq: "value"}}}`  |
|  `{object: {field: {_ gt: "value"}}}`  |  `{_ not: {object: {field: {_ lte: "value"}}}`  |


 **Example:** 

Fetch all authors which have all of their articles published i.e. have `{is_published {_eq: true}` .

## Fetch if none of the nested objects defined via an array relationship satisfy a condition​

By default a row is returned if any of the nested objects satisfy a condition. To achieve the above, we need to frame
the `where` expression as `{_not: {condition}}` . This reads as: fetch if not (any of the nested objects satisfy the
condition) i.e. none of the nested objects satisfy the condition.

For example,

| condition | where expression |
|---|---|
|  `{object: {field: {_ eq: "value"}}}`  |  `{_ not: {object: {field: {_ eq: "value"}}}`  |
|  `{object: {field: {_ gt: "value"}}}`  |  `{_ not: {object: {field: {_ gt: "value"}}}`  |


 **Example:** 

Fetch all authors which have none of their articles published i.e. have `{is_published {_eq: true}` :

## Fetch if nested object(s) exist/do not exist​

You can filter results based on if they have nested objects by checking if any nested objects exist. This can be
achieved by using the expression `{}` which evaluates to `true` if any object exists.

 **Example where nested object(s) exist:** 

Fetch all authors which have at least one article written by them:

 **Example where nested object(s) do not exist:** 

Fetch all authors which have not written any articles:

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/queries/bigquery/filters/using-nested-objects/#introduction)
- [ Filter based on nested objects' fields ](https://hasura.io/docs/latest/queries/bigquery/filters/using-nested-objects/#filter-based-on-nested-objects-fields)
- [ Fetch if the single nested object defined via an object relationship satisfies a condition ](https://hasura.io/docs/latest/queries/bigquery/filters/using-nested-objects/#fetch-if-the-single-nested-object-defined-via-an-object-relationship-satisfies-a-condition)
- [ Fetch if any of the nested objects defined via an array relationship satisfy a condition ](https://hasura.io/docs/latest/queries/bigquery/filters/using-nested-objects/#fetch-if-any-of-the-nested-objects-defined-via-an-array-relationship-satisfy-a-condition)
- [ Fetch if all of the nested objects defined via an array relationship satisfy a condition ](https://hasura.io/docs/latest/queries/bigquery/filters/using-nested-objects/#fetch-if-all-of-the-nested-objects-defined-via-an-array-relationship-satisfy-a-condition)
- [ Fetch if none of the nested objects defined via an array relationship satisfy a condition ](https://hasura.io/docs/latest/queries/bigquery/filters/using-nested-objects/#fetch-if-none-of-the-nested-objects-defined-via-an-array-relationship-satisfy-a-condition)
- [ Fetch if nested object(s) exist/do not exist ](https://hasura.io/docs/latest/queries/bigquery/filters/using-nested-objects/#fetch-if-nested-objects-existdo-not-exist)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)