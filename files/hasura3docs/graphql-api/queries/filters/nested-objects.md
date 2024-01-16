# Filter Based on Fields of Nested Objects

## Introduction​

You can use the fields of nested objects as well to filter your query results.

For example:

```
query   {
   articles ( where :   {   author :   {   name :   {   _eq :   "Sidney"   }   }   } )   {
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

## Fetch if nested object(s) exist/do not exist​

You can filter results based on if they have nested objects by checking if any nested objects exist. This can be
achieved by using the expression `{}` which evaluates to `true` if any object exists.

 **Example where nested object(s) exist:** 

Fetch all authors which have at least one article written by them:

 **Example where nested object(s) do not exist:** 

Fetch all authors which have not written any articles:

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/graphql-api/queries/filters/nested-objects/#introduction)
- [ Fetch if the single nested object defined via an object relationship satisfies a condition ](https://hasura.io/docs/3.0/graphql-api/queries/filters/nested-objects/#fetch-if-the-single-nested-object-defined-via-an-object-relationship-satisfies-a-condition)
- [ Fetch if nested object(s) exist/do not exist ](https://hasura.io/docs/3.0/graphql-api/queries/filters/nested-objects/#fetch-if-nested-objects-existdo-not-exist)
