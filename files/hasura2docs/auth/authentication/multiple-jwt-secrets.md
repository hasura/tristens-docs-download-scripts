# Multiple JWT Secrets

## Introduction​

You can configure GraphQL Engine with a list of JWT secrets. This enables you to authenticate with different JWT
issuers.

## How to use​

Multiple JWT secrets can be provided in the env var `HASURA_GRAPHQL_JWT_SECRETS` which takes a list of JWT secret
objects.

For example:

```
[
   {   "jwk_url" :   "https://..." ,   "issuer" :   "myapp"   } ,
   {   "type" :   "HS256" ,   "key" :   "3EK6FD..." ,   "issuer" :   "test"   }
]
```

The structure of an individual JWT secret is described[ here ](https://hasura.io/docs/latest/auth/authentication/jwt/#configuring-jwt-mode).

Note

If both `HASURA_GRAPHQL_JWT_SECRET` and `HASURA_GRAPHQL_JWT_SECRETS` are set, then `HASURA_GRAPHQL_JWT_SECRETS` will be
used.

## Resolution logic​

The authentication is resolved as follows:

1. Bearer tokens are extracted from headers or cookie locations (as configured by each JWT secret)
2. Tokens are filtered to ensure that the **issuer** field matches the configuration, or that the issuer is absent
either from the configuration or the token.
3. If no matching tokens are found then the unauthenticated flow is performed (depends on[ HASURA_GRAPHQL_UNAUTHORIZED_ROLE ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/)).
4. If multiple matching tokens are found then an error is raised as the desired token is ambiguous.
5. If only one matching token is found then it is verified against the corresponding configured secret.


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authentication/multiple-jwt-secrets/#introduction)
- [ How to use ](https://hasura.io/docs/latest/auth/authentication/multiple-jwt-secrets/#how-to-use)
- [ Resolution logic ](https://hasura.io/docs/latest/auth/authentication/multiple-jwt-secrets/#resolution-logic)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)