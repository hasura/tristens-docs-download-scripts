# Postgres: Filter Using Text Values

## Introduction​

The `_like` , `_nlike` , `_ilike` , `_nilike` , `_similar` , `_nsimilar` , `_regex` , `_nregex` , `_iregex` , `_niregex` operators are used for pattern matching on string/text fields.

For more details on text search operators and Postgres equivalents, refer to the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#text-operators).

## _like​

Fetch a list of articles whose titles contain the word “amet”:

## _ilike​

This query will return all users whose name contains the string "john", regardless of case.

## _nilike​

This query would return all users whose name does not contain the string "John".

Note

 `_like` is case-sensitive. Use `_ilike` for case-insensitive search.

## _similar​

Fetch a list of authors whose names begin with A or C:

## _nsimilar​

Fetch a list of authors whose names do not begin with A or C:

Note

 `_similar` and `_nsimilar` are case-sensitive.

## _regex​

Fetch a list of articles whose titles match the regex `[ae]met` :

## _iregex​

This query will return all users whose name matches the regular expression `/^joh?n$/i` , which matches "John" and "Jon".

## _nregex​

The_nregex operator in this GraphQL query is a negated regular expression filter that matches all users whose names do
not start with the letter "J".

Note

 `_regex` is case-sensitive. Use `_iregex` for case-insensitive search.

Note

 `regex` operators are supported in in `v2.0.0` and above

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/queries/postgres/filters/text-search-operators/#introduction)
- [ _like ](https://hasura.io/docs/latest/queries/postgres/filters/text-search-operators/#_like)
- [ _ilike ](https://hasura.io/docs/latest/queries/postgres/filters/text-search-operators/#_ilike)
- [ _nilike ](https://hasura.io/docs/latest/queries/postgres/filters/text-search-operators/#_nilike)
- [ _similar ](https://hasura.io/docs/latest/queries/postgres/filters/text-search-operators/#_similar)
- [ _nsimilar ](https://hasura.io/docs/latest/queries/postgres/filters/text-search-operators/#_nsimilar)
- [ _regex ](https://hasura.io/docs/latest/queries/postgres/filters/text-search-operators/#_regex)
- [ _iregex ](https://hasura.io/docs/latest/queries/postgres/filters/text-search-operators/#_iregex)
- [ _nregex ](https://hasura.io/docs/latest/queries/postgres/filters/text-search-operators/#_nregex)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)