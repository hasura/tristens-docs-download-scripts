# BigQuery: Filter Using Text Values

## Introdution​

The `_like` , `_nlike` , `_ilike` , `_nilike` operators are used for pattern matching on string/text fields.

## _like​

Fetch a list of articles whose titles contain the word “amet”:

Note

 `_like` is case-sensitive. Use `_ilike` for case-insensitive search.

## _nlike​

Retrieve a list of articles whose titles do not contain the word "Lorem":

## _ilike​

Retrieve a list of articles whose titles contain the case-insensitive word "lorem":

## _nilike​

Retrieve a list of articles whose titles do not contain the case-insensitive word "ipsum":

### What did you think of this doc?

- [ Introdution ](https://hasura.io/docs/latest/queries/bigquery/filters/text-search-operators/#introdution)
- [ _like ](https://hasura.io/docs/latest/queries/bigquery/filters/text-search-operators/#_like)
- [ _nlike ](https://hasura.io/docs/latest/queries/bigquery/filters/text-search-operators/#_nlike)
- [ _ilike ](https://hasura.io/docs/latest/queries/bigquery/filters/text-search-operators/#_ilike)
- [ _nilike ](https://hasura.io/docs/latest/queries/bigquery/filters/text-search-operators/#_nilike)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)