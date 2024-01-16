# MS SQL Server: Nested Object Queries

## Introduction​

You can use the object (one-to-one) or array (one-to-many)[ relationships ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/index/)defined in your schema to make a nested query i.e.
fetch data for a type along with data from a nested or related type.

The **name of the nested object** is the same as the name of the object/array relationship configured in the Console.

You can also filter, sort, aggregate and paginate nested objects in case of array relationships. These are not exposed
for object relationships as they have only one nested object.

## Fetch nested object using an object relationship​

The following is an example of a nested object query using the **object relationship** between an article and an author.

 **Example:** Fetch a list of articles and the name of each article’s author:

## Fetch nested objects using an array relationship​

The following is an example of a nested object query using the **array relationship** between an author and articles.

 **Example:** Fetch a list of authors and a nested list of each author’s articles:

Note

You can also[ filter ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/index/#ms-sql-server-nested-filter),[ sort ](https://hasura.io/docs/latest/queries/ms-sql-server/sorting/#ms-sql-server-nested-sort),[ aggregate ](https://hasura.io/docs/latest/queries/ms-sql-server/aggregation-queries/#ms-sql-server-nested-aggregate)and[ paginate ](https://hasura.io/docs/latest/queries/ms-sql-server/pagination/#ms-sql-server-nested-paginate)nested objects in case of array
relationships.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/queries/ms-sql-server/nested-object-queries/#introduction)
- [ Fetch nested object using an object relationship ](https://hasura.io/docs/latest/queries/ms-sql-server/nested-object-queries/#fetch-nested-object-using-an-object-relationship)
- [ Fetch nested objects using an array relationship ](https://hasura.io/docs/latest/queries/ms-sql-server/nested-object-queries/#fetch-nested-objects-using-an-array-relationship)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)