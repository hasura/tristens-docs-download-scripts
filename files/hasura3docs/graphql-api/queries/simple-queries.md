# Simple Object Queries

## Introduction​

You can fetch a single node or multiple nodes of the same type using a simple object query.

## Fetch a list of objects​

 **Example:** Fetch a list of authors:

## Fetch an object using its primary key​

 **Example:** Fetch an author using their primary key:

## Fetch list of objects with pagination​

 **Example:** Fetch 2 articles after removing the 1st article from the result set.

Warning

Without an `order_by` in `limit` queries, the results may be unpredictable.

## Fetch list of objects with filtering​

 **Example:** Fetch a list of articles whose title contains the word "The":

## Fetch list of objects with sorting​

 **Example:** Fetch a list of articles with `article_id` in descending order:

## Fetch objects using model arguments​

 **Example:** Fetch the articles for the given `author_id` :

Only available for Native Queries

This feature is only available for Native Queries.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/graphql-api/queries/simple-queries/#introduction)
- [ Fetch a list of objects ](https://hasura.io/docs/3.0/graphql-api/queries/simple-queries/#fetch-a-list-of-objects)
- [ Fetch an object using its primary key ](https://hasura.io/docs/3.0/graphql-api/queries/simple-queries/#fetch-an-object-using-its-primary-key)
- [ Fetch list of objects with pagination ](https://hasura.io/docs/3.0/graphql-api/queries/simple-queries/#fetch-list-of-objects-with-pagination)
- [ Fetch list of objects with filtering ](https://hasura.io/docs/3.0/graphql-api/queries/simple-queries/#fetch-list-of-objects-with-filtering)
- [ Fetch list of objects with sorting ](https://hasura.io/docs/3.0/graphql-api/queries/simple-queries/#fetch-list-of-objects-with-sorting)
- [ Fetch objects using model arguments ](https://hasura.io/docs/3.0/graphql-api/queries/simple-queries/#fetch-objects-using-model-arguments)
