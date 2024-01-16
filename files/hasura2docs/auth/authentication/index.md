# Authentication

## Introduction​

 **Authentication verifies the identity of a user.** 

Hasura GraphQL Engine utilizes **session variables** , with specific user, role, organization and any other information
you may need to determine the data access rights of the user.

With these session variables you are able to construct permission rules which are added per **table** , **role** , and **database operation** in order to provide extremely granular access control.

 **Actual authentication is handled outside Hasura** . Ie: the responsibility for generating session variables is
delegated to your (new or existing) authentication service in order to provide you with the greatest flexibility and
range of options for your authentication needs.

Hasura authentication can be configured via JSON web tokens (JWT) or a webhook service and can be integrated with any
other provider you choose (e.g.[ Auth0 ](https://auth0.com/),[ Firebase Auth ](https://firebase.google.com/products/auth),[ AWS Cognito ](https://aws.amazon.com/cognito/), a custom solution, etc) in order to verify the user and set
session variables that then control access to data.

Full[ admin level ](https://hasura.io/docs/latest/auth/authentication/admin-secret-access/)and[ unauthenticated access ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/)can also be configured.

In[ JWT mode ](https://hasura.io/docs/latest/auth/authentication/jwt/), session variables are provided to Hasura Engine in the payload of the
JWT token. In[ webhook mode ](https://hasura.io/docs/latest/auth/authentication/webhook/), the session variables are provided in JSON format
back to Hasura Engine in the body of a successful request to the webhook endpoint.

Your authentication service is required to pass, at least, a **user's role information** in the form of the session
variable `X-Hasura-Role` . More often than not, you'll also need to pass other information for your particular access
control use cases, like `X-Hasura-User-Id` or `X-Hasura-Org-Id` , in order to build your permission rules.

The specific content of the GraphQL request is then processed with the session variables against the permissions
defined by you in the Hasura Engine to build a single optimized query to the database with restricted access for that
user role.

## The two Hasura authentication options​

Hasura supports two options for authentication configuration:

### 1. JWT​

Your auth service issues JWTs (JSON Web Tokens) to your client app, which, when sent as part of the request are then
verified and decoded by the Hasura Engine to get session variables to use when evaluating permissions.

Here's how a GraphQL query is processed in JWT mode:

Image: [ Authentication using JWT ](https://hasura.io/docs/assets/images/auth-jwt-overview-diagram-1bc36ac6c078e8138c6932512e70f610.png)

### 2. Webhook​

Your auth service exposes a webhook endpoint that is used to authenticate all incoming requests and to respond with
session variables to use when evaluating permissions on Hasura Engine.

Here's how a GraphQL request is processed in webhook mode:

Image: [ Authentication using webhooks ](https://hasura.io/docs/assets/images/auth-webhook-overview-b29e5afc166191c7369055f0d1574e35.png)

## Other access levels​

- [ Admin secret access ](https://hasura.io/docs/latest/auth/authentication/admin-secret-access/)
- [ Unauthenticated / Public access ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/)


## Next Steps​

- [ Quickstart 3rd party integration tutorials ](https://hasura.io/docs/latest/auth/authentication/quickstart/)
- [ See here for info on using JWT mode ](https://hasura.io/docs/latest/auth/authentication/jwt/).
- [ See here for info on using webhook mode ](https://hasura.io/docs/latest/auth/authentication/webhook/).


JWT and webhook Tutorials

- Webhooks Basics -[ Learn Tutorial ](https://hasura.io/learn/graphql/hasura-authentication/webhook-mode/)
- JWT Basics -[ Learn Tutorial ](https://hasura.io/learn/graphql/hasura-authentication/jwt-basics/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authentication/index/#introduction)
- [ The two Hasura authentication options ](https://hasura.io/docs/latest/auth/authentication/index/#the-two-hasura-authentication-options)
    - [ 1. JWT ](https://hasura.io/docs/latest/auth/authentication/index/#1-jwt)

- [ 2. Webhook ](https://hasura.io/docs/latest/auth/authentication/index/#2-webhook)
- [ Other access levels ](https://hasura.io/docs/latest/auth/authentication/index/#other-access-levels)
- [ Next Steps ](https://hasura.io/docs/latest/auth/authentication/index/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)