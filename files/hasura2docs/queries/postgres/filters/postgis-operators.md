# Postgres: Filter Using Geospatial Data

## PostGIS spatial relationship operators​

The `_st_contains` , `_st_crosses` , `_st_equals` , `_st_intersects` , `_st_3d_intersects` , `_st_overlaps` , `_st_touches` , `_st_within` , `_st_d_within` , and `_st_3d_d_within` operators are used to filter based on `geometry` like columns.

 `_st_d_within` and `_st_intersects` can be used on `geography` columns also (but their 3D variations are for `geometry` only).

For more details on spatial relationship operators and Postgres equivalents, refer to the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#geometry-operators).

Use JSON representation (see[ GeoJSON ](https://tools.ietf.org/html/rfc7946)) of `geometry` and `geography` values in `variables` as shown in the following examples:

### _st_contains​

 `_st_contains` is a spatial operator that checks whether one geometry contains another. It returns values if the first
geometry completely contains the second geometry.

### _st_crosses​

 `_st_crosses` is a spatial operator that checks whether two geometries cross each other. It returns values if the two
geometries cross one another.

### _st_equals​

 `_st_equals` is a spatial operator that checks whether two geometries are equal. It returns values if the two geometries
have the same shape and size.

### _st_intersects​

In this example, the `getPointsWithinPolygon` query takes in a polygon argument that defines a rectangular area on a
map. The location field returns the latitude and longitude of points that intersect with the given polygon using the `_st_intersects` operator.

### _st_within​

 `_st_within` is a spatial operator that checks whether one geometry is completely contained within another geometry. It
returns values if the first geometry is completely contained within the second geometry.

### _st_d_within​

Fetch a list of `geometry` values which are within a 3-unit buffer from a given `point` value:

### _st_3d_d_within​

This is completely analogous to the `_st_d_within` example above, the only difference being that our coordinates now
contain a z-value.

### _st_3d_intersects​

Fetch a list of (3D) `geometry` values which intersect a given `polygon` value:

### _st_overlaps​

 `_st_overlaps` is a spatial operator that checks whether two geometries overlap each other and that their two compared
geometries are of the same dimension. It returns values if the two geometries share some, but not all, points.

### _st_touches​

 `_st_touches` is a spatial operator that checks whether two geometries share a boundary, but do not overlap. It returns
values if the two geometries share one or more points on their boundaries.

## Intersect operators on RASTER columns​

Intersect operators on columns with `raster` type are supported. Please submit a feature request via[ GitHub ](https://github.com/hasura/graphql-engine)if you want support for more functions.

For more details on intersect operators on raster columns and Postgres equivalents, refer to the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#intersect-operators).

### _st_intersects_rast​

Filter the raster values which intersect the input raster value.

Executes the following SQL function:

`boolean  ST_Intersects (  raster  < raster - col >   ,  raster  < raster - value >   ) ;`

### _st_intersects_geom_nband​

Filter the raster values which intersect the input geometry value and optional band number.

Executes the following SQL function:

`boolean  ST_Intersects (  raster  < raster - col >   ,   geometry  geommin  ,   integer  nband = NULL   ) ;`

### _st_intersects_nband_geom​

Filter the raster values (with specified band number) which intersect the input geometry value.

Executes the following SQL function:

`boolean  ST_Intersects (  raster  < raster - col >   ,   integer  nband  ,   geometry  geommin  ) ;`

### What did you think of this doc?

- [ PostGIS spatial relationship operators ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#postgis-spatial-relationship-operators)
    - [ _st_contains ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_contains)

- [ _st_crosses ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_crosses)

- [ _st_equals ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_equals)

- [ _st_intersects ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_intersects)

- [ _st_within ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_within)

- [ _st_d_within ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_d_within)

- [ _st_3d_d_within ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_3d_d_within)

- [ _st_3d_intersects ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_3d_intersects)

- [ _st_overlaps ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_overlaps)

- [ _st_touches ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_touches)
- [ Intersect operators on RASTER columns ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#intersect-operators-on-raster-columns)
    - [ _st_intersects_rast ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_intersects_rast)

- [ _st_intersects_geom_nband ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_intersects_geom_nband)

- [ _st_intersects_nband_geom ](https://hasura.io/docs/latest/queries/postgres/filters/postgis-operators/#_st_intersects_nband_geom)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)