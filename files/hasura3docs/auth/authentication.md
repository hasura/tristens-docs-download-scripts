# Hasura Authentication

## Introduction​

 **Authentication verifies the identity of a user.** 

Hasura GraphQL Engine utilizes "session variables", with specific user, role, organization and any other information you
may need to determine the data access rights of the user.

With these session variables you are able to define permission rules on your data domain to provide fine-grained access
control to resources.

Actual authentication is handled outside of Hasura i.e. the responsibility for generating session variables is delegated
to your (new or existing) authentication service in order to provide you with the greatest flexibility and range of
options for your authentication needs.

Hasura's authentication can be configured via JSON web tokens (JWT) or a webhook service and can be integrated with any
other provider you choose (e.g.[ Auth0 ](https://auth0.com/),[ Firebase Auth ](https://firebase.google.com/products/auth),[ AWS Cognito ](https://aws.amazon.com/cognito/), a custom solution, etc.) in order to verify the user and set session
variables that then control access to data.

This document details the `AuthConfig` metadata object used to set up authentication for incoming requests in Hasura.

## Auth Config​

Only a single `AuthConfig` object can be defined in the metadata. It has the following structure:

| Field | Type | Required | Description |
|---|---|---|---|
|  `allowRoleEmulationBy`  | String | false | Name of the role which allows role emulation. Read more about role emulation[ here ](https://hasura.io/docs/3.0/auth/authentication/role-emulation/). |
|  `webhook`  | Object | false | Configuration of the authentication webhook. |
|  `jwt`  | Object | false | Configuration of the JWT secret. |


You must select one of the supported authentication modes

In the object, only one of the supported authentication modes ( `jwt` or `webhook` ) is expected.

## JWT authentication​

### Example​

```
kind :  AuthConfig
version :  v1
definition :
   jwt :
     key :
       fixed :
         algorithm :  HS256
         key :
           value :  token
     tokenLocation :
       type :  BearerAuthorization
     claimsConfig :
       namespace :
         claimsFormat :  Json
         location :   "/https:~1~1hasura.io~1jwt~1claims"
```

For a full description of JWT mode[ see here ](https://hasura.io/docs/3.0/auth/authentication/jwt/).

## Webhook authentication​

### Example​

```
---
kind :  AuthConfig
version :  v1
definition :
   allowRoleEmulationBy :  admin
   webhook :
     url :  http : //auth.yourservice.com/validate - request
     method :  Get
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `url`  | URL | true | URL of the authentication webhook. |
|  `method`  | String | false | HTTP method to use while making the request to the authentication webhook. Only `Get` and `Post` methods are supported. |


For a full description of webhook mode[ see here ](https://hasura.io/docs/3.0/auth/authentication/webhook/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/auth/authentication/#introduction)
- [ Auth Config ](https://hasura.io/docs/3.0/auth/authentication/#auth-config)
- [ JWT authentication ](https://hasura.io/docs/3.0/auth/authentication/#jwt-auth-config)
    - [ Example ](https://hasura.io/docs/3.0/auth/authentication/#example)
- [ Webhook authentication ](https://hasura.io/docs/3.0/auth/authentication/#webhook-auth-config)
    - [ Example ](https://hasura.io/docs/3.0/auth/authentication/#example-1)