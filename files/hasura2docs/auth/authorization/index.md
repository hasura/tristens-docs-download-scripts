# Authorization

## Introduction​

 **Authorization determines what a verified user can access.** 

Hasura supports **role-based** authorization where access control over data is achieved by creating **permissions** based on the **user role** and **database operation** on the **table** .

Every authenticated request to Hasura Engine should contain dynamic[ session variables ](https://hasura.io/docs/latest/auth/authorization/roles-variables/)from your[ authentication service ](https://hasura.io/docs/latest/auth/authentication/index/)of **at least**  `X-Hasura-Role` as well as any others you may
need to use in your authorization rules.

Authorization rules, or "Permissions", are defined by you in Hasura Engine. To control access to data, you create
permissions per role and table for each of the `select` , `insert` , `update` and `delete` database operations.

Permissions can also be defined for[ Actions ](https://hasura.io/docs/latest/actions/action-permissions/)and[ Remote Schemas ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-permissions/).

### Example​

If we wanted to create a Permission which allowed users to only view their own data on the `user` table for a `select` database operation, we would create a row `select` Permission for the table like this:

```
{
  “id”: {
    “_eq”: “X-Hasura-User-Id”
  }
}
```

This would check that the `X-Hasura-User-Id` session variable matches the `id` value in the `user` table of the user
which is being selected. This is a simple yet effective example and many more complex rules can be created as per
your needs.

Note

Hasura roles and permissions are implemented at the Hasura Engine layer. They have no relationship to database users
and roles.

## Easily test permissions​

If you just want to see permissions in action, you don't need to first set up or integrate your auth service with
GraphQL Engine. You can just do the following:

- [ Define permission rules ](https://hasura.io/docs/latest/auth/authorization/permissions/)for a table, role and operation. eg: `user` table, `user` role and `select` operation.
- Use the API GraphiQL interface in the Console to make a request and send the session variables as request headers
(send a `X-Hasura-Role` key, with its value as the name of the role you've defined rules for). The data in the
response will be restricted as per your configuration.


Image: [ Pose as a user using the admin secret header ](https://hasura.io/docs/assets/images/authentication_test-permissions-with-admin-secret_2.16.1-19da26c8ee59a6d89feda2a38be4870e.png)

API limits and access controls in Hasura Cloud

Additional access controls and API limits like maximum query depth are available in Hasura Cloud and Enterprise. See
more at[ API limits with Hasura Cloud ](https://hasura.io/docs/latest/security/api-limits/).

Additional authorization tutorial

- Authorization Patterns with Hasura -[ Check out this tutorial ](https://hasura.io/learn/graphql/hasura-auth-slack/introduction/).


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authorization/index/#introduction)
    - [ Example ](https://hasura.io/docs/latest/auth/authorization/index/#example)
- [ Easily test permissions ](https://hasura.io/docs/latest/auth/authorization/index/#easily-test-permissions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)