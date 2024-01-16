# Upgrading from Hasura CE to Hasura Enterprise

## Introduction​

Starting from Hasura GraphQL Engine version `v2.12.0` , we have included both open-source and commercial components in
the `hasura/graphql-engine` container image. The open-source portions are licensed under the[ Apache License, Version 2.0 ](https://www.apache.org/licenses/LICENSE-2.0). The proprietary components include features for Hasura Enterprise and they can be enabled through a free trial or with a license key provided by the Hasura team.

Note

If you would
like to use an image with only the open source components, please use Docker images on[ this page ](https://hub.docker.com/r/hasura/graphql-engine/tags?page=1&name=-ce)that contain `-ce` . (example: `hasura/graphql-engine:<VERSION>-ce` )

#### Hasura Enterprise trial​

If you're running Hasura version `v2.23.0` or greater, you can instantly try Hasura Enterprise on your existing Hasura setup by signing up for a[ free 30-day Hasura Enterprise trial ](https://hasura.io/docs/latest/enterprise/try-hasura-enterprise-edition/).

#### Hasura Enterprise Edition license key​

If you have been provided a license key by the Hasura team, set it as the value for the `HASURA_GRAPHQL_EE_LICENSE_KEY` environment variable in your Hasura container.

E.g. if the license key sent by the Hasura team is `ABC1234` , you will set `HASURA_GRAPHQL_EE_LICENSE_KEY=”ABC1234”` .

Restart Hasura to start using the enterprise features.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/enterprise/upgrade-ce-to-ee/#introduction)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)