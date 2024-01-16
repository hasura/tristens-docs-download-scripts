# Postgres: Filter by Hierarchical ltree Data

## Introduction​

Comparison operators on columns with `ltree` , `lquery` or `ltxtquery` types are supported.

Please submit a feature request via[ GitHub ](https://github.com/hasura/graphql-engine)if you want support for more
functions.

For more details on `ltree` operators and Postgres equivalents, refer to the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#ltree-operators).

## _ancestor​

Select ancestors of an *ltree* argument

## _ancestor_any​

## _matches​

Match any label path containing the node `Astronomy` .

## _matches_any​

Select *ltree* paths matching any *lquery* regex in an array

## _descendant​

## _descendant_any​

## _matches_fulltext​

Match any label path containing a node containing the substring `Astro` .

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/queries/postgres/filters/ltree-operators/#introduction)
- [ _ancestor ](https://hasura.io/docs/latest/queries/postgres/filters/ltree-operators/#_ancestor)
- [ _ancestor_any ](https://hasura.io/docs/latest/queries/postgres/filters/ltree-operators/#_ancestor_any)
- [ _matches ](https://hasura.io/docs/latest/queries/postgres/filters/ltree-operators/#_matches)
- [ _matches_any ](https://hasura.io/docs/latest/queries/postgres/filters/ltree-operators/#_matches_any)
- [ _descendant ](https://hasura.io/docs/latest/queries/postgres/filters/ltree-operators/#_descendant)
- [ _descendant_any ](https://hasura.io/docs/latest/queries/postgres/filters/ltree-operators/#_descendant_any)
- [ _matches_fulltext ](https://hasura.io/docs/latest/queries/postgres/filters/ltree-operators/#_matches_fulltext)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)