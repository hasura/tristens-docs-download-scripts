# Healthz Check

## Introduction​

Hasura provides a Health Check endpoint to monitor the status of the GraphQL API. This is available under the `/healthz` endpoint for all Hasura Projects (including the OSS GraphQL Engine).

The endpoint also optionally accepts a `strict` URL parameter whose value should be either `true` or `false` . When
omitted, the `strict` parameter assumes a `false` value.

## Usage​

Make a `GET` request to the `/healthz` endpoint to fetch the status:

`curl  -XGET https://advanced-hasura.hasura.app/healthz?strict = false`

Replace `advanced-hasura` with your project name.

## Response​

The returned status could be one of the following:

- `200, OK` - This requires no action. Everything is working as expected.
- If the Metadata contains any inconsistent objects, the response returned will depend on the provided `strict` parameter.
    - `strict=false` or omitted: `200, WARN, inconsistent objects in schema`

- `strict=true` : `500, ERROR, inconsistent objects in schema`
This requires a review of Metadata since some inconsistent objects have been identified. This usually occurs when
there has been a `metadata apply` [ command which contained inconsistent objects ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/#apply-metadata).
- `500, ERROR` - This means the API is not working and the[ logs need to be checked ](https://hasura.io/docs/latest/deployment/logging/#health-check-log-structure).


 `200, OK` - This requires no action. Everything is working as expected.

If the Metadata contains any inconsistent objects, the response returned will depend on the provided `strict` parameter.

This requires a review of Metadata since some inconsistent objects have been identified. This usually occurs when
there has been a `metadata apply` [ command which contained inconsistent objects ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/#apply-metadata).

 `500, ERROR` - This means the API is not working and the[ logs need to be checked ](https://hasura.io/docs/latest/deployment/logging/#health-check-log-structure).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/health-checks/healthz-check/#introduction)
- [ Usage ](https://hasura.io/docs/latest/deployment/health-checks/healthz-check/#usage)
- [ Response ](https://hasura.io/docs/latest/deployment/health-checks/healthz-check/#response)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)