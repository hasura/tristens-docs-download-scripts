# MS SQL Server: Filter Using Geospatial Data

## Introduction​

The `_st_contains` , `_st_crosses` , `_st_equals` , `_st_intersects` , `_st_overlaps` , `_st_touches` , `_st_within` operators
are used to filter based on `geometry` like columns.

_st_intersects usage

```
_
st_intersects
```

 `_st_intersects` can be used on `geography` columns also.

Use JSON representation (see[ GeoJSON ](https://tools.ietf.org/html/rfc7946)) of `geometry` and `geography` values in `variables` as shown in the following examples:

## _st_contains​

Fetch a list of geometry values that are contained within the given `polygon` value:

## _st_crosses​

Fetch a list of geometry values which cross the given `line` value:

## _st_equals​

Fetch a list of geometry values which are equal to the given `polygon` value:

## _st_intersects​

Fetch a list of geometry values which intersect the given `polygon` value:

## _st_overlaps​

Fetch a list of geometry values which overlap with the given `polygon` value:

## _st_touches​

Fetch a list of geometry values which touch the given `polygon` value:

## _st_within​

Fetch a list of geometry values which are within the given `polygon` value:

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/geospatial-operators/#introduction)
- [ _st_contains ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/geospatial-operators/#_st_contains)
- [ _st_crosses ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/geospatial-operators/#_st_crosses)
- [ _st_equals ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/geospatial-operators/#_st_equals)
- [ _st_intersects ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/geospatial-operators/#_st_intersects)
- [ _st_overlaps ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/geospatial-operators/#_st_overlaps)
- [ _st_touches ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/geospatial-operators/#_st_touches)
- [ _st_within ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/geospatial-operators/#_st_within)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)