# Unauthenticated / Public Access

## Introduction​

It is a common requirement to have requests which are accessible to all users without the need for authentication or
logging in.

## Enabling authenticated access with an admin secret​

When Hasura GraphQL Engine has a configured[ admin secret ](https://hasura.io/docs/latest/deployment/securing-graphql-endpoint/), by default it
will reject any[ unauthenticated request it receives ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/#configuring-unauthenticated--public-access/#unauthenticated-request-definitions). We need to configure an
unauthorized role in order to handle these requests via the Hasura permissions system.

## Enabling unauthenticated access with a unauthorized role​

You can configure the Hasura Engine to allow access to unauthenticated users by defining a specific role which will be
used for all unauthenticated requests. Once an unauthorized role is configured, unauthenticated requests will not be
rejected and instead will be handled as the unauthenticated user with the relevant authorization permissions for that
role taking effect.

To set the unauthorized role, you can use the env variable[ HASURA_GRAPHQL_UNAUTHORIZED_ROLE or the --unauthorized-role flag ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#unauthorized-role)to define a role name for unauthenticated (non-logged in) users. See[ GraphQL Engine server config reference ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/index/)for more details on setting this
flag or environment variable.

Once that role is set, you can[ configure permissions for it in the usual way ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/).

[ Click here ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example)for a guide on setting up permissions for the unauthorized role.

Risk of session variables with the unauthorized role

You should not use[ session variables ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables)in the permissions for
an unauthorized role because the source of the session variables cannot be trusted.

Since session variables can be passed using request headers and they are not verified through the JWT or webhook
authentication methods or utilize an admin secret, a user can choose to set any values for them and bypass the
permissions.

### Unauthenticated request definitions​

The following situations are considered unauthenticated requests and will default to the unauthorized role:

- When[ JWT ](https://hasura.io/docs/latest/auth/authentication/jwt/)or[ webhook ](https://hasura.io/docs/latest/auth/authentication/webhook/)modes are not configured, and
the request does not contain the admin secret header, then every request is considered an unauthenticated request
no matter the headers supplied.
- When[ JWT ](https://hasura.io/docs/latest/auth/authentication/jwt/)mode is configured, and the request does not contain the admin secret
header, then a request will be considered unauthenticated if it does not have a JWT.
- When[ webhook ](https://hasura.io/docs/latest/auth/authentication/webhook/)mode is configured, and the request does not contain the admin
secret header, then a request will be considered unauthenticated if the webhook returns the following response:To deny the request in webhook mode, a `401` response[ should be returned ](https://hasura.io/docs/latest/auth/authentication/webhook/#auth-denial).
Any response from the webhook which is not a `200` [ response with a valid role ](https://hasura.io/docs/latest/auth/authentication/webhook/#success)or the above `401` response will raise a `500 Internal Server Error` exception in Hasura Engine.


When[ JWT ](https://hasura.io/docs/latest/auth/authentication/jwt/)or[ webhook ](https://hasura.io/docs/latest/auth/authentication/webhook/)modes are not configured, and
the request does not contain the admin secret header, then every request is considered an unauthenticated request
no matter the headers supplied.

When[ JWT ](https://hasura.io/docs/latest/auth/authentication/jwt/)mode is configured, and the request does not contain the admin secret
header, then a request will be considered unauthenticated if it does not have a JWT.

When[ webhook ](https://hasura.io/docs/latest/auth/authentication/webhook/)mode is configured, and the request does not contain the admin
secret header, then a request will be considered unauthenticated if the webhook returns the following response:

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "X-Hasura-Role" :   "your-unauthorized-role-name" ,
}
```

To deny the request in webhook mode, a `401` response[ should be returned ](https://hasura.io/docs/latest/auth/authentication/webhook/#auth-denial).
Any response from the webhook which is not a `200` [ response with a valid role ](https://hasura.io/docs/latest/auth/authentication/webhook/#success)or the above `401` response will raise a `500 Internal Server Error` exception in Hasura Engine.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/#configuring-unauthenticated--public-access/#introduction)
- [ Enabling authenticated access with an admin secret ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/#configuring-unauthenticated--public-access/#enabling-authenticated-access-with-an-admin-secret)
- [ Enabling unauthenticated access with a unauthorized role ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/#configuring-unauthenticated--public-access/#enabling-unauthenticated-access-with-a-unauthorized-role)
    - [ Unauthenticated request definitions ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/#configuring-unauthenticated--public-access/#unauthenticated-request-definitions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)