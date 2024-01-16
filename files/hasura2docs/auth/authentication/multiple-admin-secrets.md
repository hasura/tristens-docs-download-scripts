# Multiple Admin Secrets

## Introduction​

You can specify a list of admin secrets in GraphQL Engine which can be used to :

1. Implement security mechanisms like rotating secrets
2. Have different lifecycles for individual admin secrets e.g. temporarily give admin access to an operator


## How to use​

Multiple admin secrets can be provided in the env var `HASURA_GRAPHQL_ADMIN_SECRETS` which takes a list of admin
secrets,

For example:

`[ "secret-1" ,   "secret-2" ]`

When you launch the Console from the Hasura Cloud or the Hasura Enterprise Edition Control Plane dashboard, you can use
any secret from the admin secrets list to authenticate yourself as an admin. If you want to make API calls as an admin
from outside the console, you need to pass any one of the admin secrets as the `x-hasura-admin-secret` request header.

Note

If both `HASURA_GRAPHQL_ADMIN_SECRET` and `HASURA_GRAPHQL_ADMIN_SECRETS` are set, then only `HASURA_GRAPHQL_ADMIN_SECRETS` will be used.

## Rotating admin secrets​

You can use this feature to implement a secret rotation mechanism without downtime as outlined below:

1. Add a new secret to the list of admin secrets
2. Update applications/services using the old admin secret to use the new secret
3. Remove the old secret from the admin secret list


Note that for self-hosted Hasura, you would need to perform a[ rolling deployment ](https://hasura.io/docs/latest/glossary/index/#rolling-deployment)whenever you are updating the environment variables (to ensure no downtime).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authentication/multiple-admin-secrets/#introduction)
- [ How to use ](https://hasura.io/docs/latest/auth/authentication/multiple-admin-secrets/#how-to-use)
- [ Rotating admin secrets ](https://hasura.io/docs/latest/auth/authentication/multiple-admin-secrets/#rotating-admin-secrets)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)