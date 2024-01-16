# Admin Access

## Introduction​

Hasura will bypass permissions and allow all queries, mutations and subscriptions when you include your `X-Hasura-Admin-Secret` header without other session variables on your request. You can also specify the `admin` role in your authenticated requests to[ bypass permissions ](https://hasura.io/docs/latest/auth/authentication/admin-secret-access/#admin-role).

Admin secret security

The admin secret should **never** be exposed in front-end clients where it could be accessed by a malicious user by
inspecting the request.

## Admin secret in combination with other session variables​

If you include the `X-Hasura-Admin-Secret` header and also add the `X-Hasura-Role` and other user specific
headers such as `X-Hasura-User-Id` ,  Hasura GraphQL Engine will process the request using the defined access-control
rules for that user and role and not as an admin.

Without the `X-Hasura-Admin-Secret` header you will need to authenticate your requests as a user and role with
either the[ JWT ](https://hasura.io/docs/latest/auth/authentication/jwt/)or[ webhook ](https://hasura.io/docs/latest/auth/authentication/webhook/)authentication methods.

Image: [ Pose as a user using the admin secret header ](https://hasura.io/docs/assets/images/authentication_test-permissions-with-admin-secret_2.16.1-19da26c8ee59a6d89feda2a38be4870e.png)

## Using the admin role​

As an alternative to the admin secret header you can also make requests with the default `admin` user role. This
role allows you the user to perform any operation on any table and can be used where full unrestricted permissions
are required.

To use this role, your JWT or webhook token should provide the role as `admin` . You would still verify your request in
the normal way with Hasura Engine in either JWT or webhook authentication modes.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authentication/admin-secret-access/#introduction)
- [ Admin secret in combination with other session variables ](https://hasura.io/docs/latest/auth/authentication/admin-secret-access/#admin-secret)
- [ Using the admin role ](https://hasura.io/docs/latest/auth/authentication/admin-secret-access/#admin-role)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)