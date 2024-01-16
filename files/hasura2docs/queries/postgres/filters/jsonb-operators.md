# Postgres: Filter Using JSONB Objects

## Introduction​

The `_contains` , `_contained_in` , `_has_key` , `_has_keys_any` and `_has_keys_all` operators are used to filter based on `JSONB` columns.

For more details on JSONB operators and Postgres equivalents, refer to the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#jsonb-operators).

## _contains​

Fetch all authors living within a particular pincode (present in `address` JSONB column):

## _contained_in​

This example fetches all items where the "Tags" property contains the value "tag1" and is also contained in the list `["tag1", "tag2"]` .

## _has_key​

Fetch authors if the `phone` key is present in their JSONB `address` column:

## _has_keys_any​

Fetch users who have either "admin" or "editor" permissions:

## _has_keys_all​

Fetch user, where their id is "123", and check if the address has all the fields "street", "city", "state", "zip":

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/queries/postgres/filters/jsonb-operators/#introduction)
- [ _contains ](https://hasura.io/docs/latest/queries/postgres/filters/jsonb-operators/#_contains)
- [ _contained_in ](https://hasura.io/docs/latest/queries/postgres/filters/jsonb-operators/#_contained_in)
- [ _has_key ](https://hasura.io/docs/latest/queries/postgres/filters/jsonb-operators/#_has_key)
- [ _has_keys_any ](https://hasura.io/docs/latest/queries/postgres/filters/jsonb-operators/#_has_keys_any)
- [ _has_keys_all ](https://hasura.io/docs/latest/queries/postgres/filters/jsonb-operators/#_has_keys_all)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)