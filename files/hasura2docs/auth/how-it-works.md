# Authentication and Authorization

## Introduction​

 **Authentication  verifies the identity of a user, while  authorization  determines what they can access** .

Hasura provides flexible authentication and role-based access control (RBAC) authorization models.

 **Actual authentication is handled outside Hasura.** Once a user is authenticated with your auth service, you can either
i) provide a JWT to the Hasura GraphQL Engine containing session variables like user role and any other values like
user id, or ii) specify a webhook in order to resolve the variables and send them back.

 **For authorization, Hasura helps you define granular, role and session variable based permission rules to control
access to your data** . These permissions utilize the session variables returned by your authentication service and are
granular enough to control access to every row or column in your database.

Let's take a look at a high-level overview of how this works when Hasura GraphQL Engine receives a request:

Image: [ Authentication and authorization in Hasura flow diagram ](https://hasura.io/docs/assets/images/auth-high-level-overview-diagram-5ac4fad9860da7b4f9732bd5e5eb7f93.png)

Hasura uses the role, session variables and the actual GraphQL query itself to validate against the authorization
permission rules defined by you. If the operation is allowed, it generates an optimized SQL query, which includes
the constraints from the permission rules, and sends it to the database to perform the required operation; fetching
the required rows for queries or inserting, editing or deleting rows for mutations.

Hasura also provides functionality to enable authorization for its[ Actions ](https://hasura.io/docs/latest/actions/action-permissions/)and[ Remote Schema ](https://hasura.io/docs/latest/remote-schemas/auth/index/)features too.

 **More details about setting up authentication and authorization permissions:** 

- [ Authentication ](https://hasura.io/docs/latest/auth/authentication/index/)
- [ Authorization ](https://hasura.io/docs/latest/auth/authorization/index/)


Learn Tutorial

If you'd like to learn about authentication and authorization by following a tutorial, check out our Learn Tutorial,[ Authentication with Hasura ](https://hasura.io/learn/graphql/hasura-auth-slack/introduction/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/how-it-works/#introduction)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)