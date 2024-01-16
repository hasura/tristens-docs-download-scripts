# Nested Object Queries

## Introduction​

You can use the object (one-to-one) or array (one-to-many) relationships defined in your metadata to make a nested
queries, i.e. fetch data for one type along with data from a nested or related type.

## Fetch nested object using an object relationship​

The following is an example of a nested object query using the **object relationship** between an article and an author.

 **Example:** Fetch a list of articles and the name of each article’s author:

## Fetch nested objects using an array relationship​

The following is an example of a nested object query using the **array relationship** between an author and articles.

 **Example:** Fetch a list of authors and a related, nested list of each author’s articles:

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/graphql-api/queries/nested-queries/#introduction)
- [ Fetch nested object using an object relationship ](https://hasura.io/docs/3.0/graphql-api/queries/nested-queries/#fetch-nested-object-using-an-object-relationship)
- [ Fetch nested objects using an array relationship ](https://hasura.io/docs/3.0/graphql-api/queries/nested-queries/#fetch-nested-objects-using-an-array-relationship)
