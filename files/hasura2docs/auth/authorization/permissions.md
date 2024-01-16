# Configuring Permission Rules

## Introduction​

Permissions in Hasura are defined with table, role and operation ( *insert, update, select, delete* ) level granularity:

Image: [ Defining permissions in Hasura ](https://hasura.io/docs/assets/images/permission-rule-granularity_2.16.1-f0d4b4a2ab73754a84cefa1a0e032fac.png)

Requests to the Hasura GraphQL Engine should contain the[ reserved session variable ](https://hasura.io/docs/latest/auth/authentication/index/) `X-Hasura-Role` (or `X-Hasura-Allowed-Roles` and `X-Hasura-Default-Role` ) to indicate the requesting user's role.
The table and operation information is inferred from the request itself. This information is then used to determine
the right permission rule to be applied ( *if one has been defined* ) to the incoming request.

Hasura converts incoming GraphQL requests into a single SQL query which includes constraints derived from the
permission rules that is executed on the configured database instance.

Permissions are essentially a combination of **boolean expressions** and **column selections** that impose constraints
on the data being returned or modified.

Let's take a look at the different configuration options available to define a permission rule. Permission rules
can be defined in the Console or the[ metadata APIs for permissions ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/).

## Operation permissions​

### Select permissions​

For `select` operations or for GraphQL queries, you can configure the following:

- [ Row permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/)
- [ Column permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/column-level-permissions/)
- [ Aggregation permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/aggregation-permissions/)
- [ Row fetch limit ](https://hasura.io/docs/latest/auth/authorization/permissions/row-fetch-limit/)
- [ Root field visibility ](https://hasura.io/docs/latest/auth/authorization/permissions/disabling-root-fields/)


### Insert permissions​

For `insert` operations or for GraphQL mutations of the type *insert* , you can configure the following:

- [ Row permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/)
- [ Column permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/column-level-permissions/)
- [ Column presets ](https://hasura.io/docs/latest/auth/authorization/permissions/column-presets/)
- [ Backend-only mutations ](https://hasura.io/docs/latest/auth/authorization/permissions/backend-only/)


### Update permissions​

For `update` operations or for GraphQL mutations of the type *update* , you can configure the following:

- [ Row permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/)including Pre and Post update checks
- [ Column permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/column-level-permissions/)
- [ Column presets ](https://hasura.io/docs/latest/auth/authorization/permissions/column-presets/)
- [ Backend-only mutations ](https://hasura.io/docs/latest/auth/authorization/permissions/backend-only/)


### Delete permissions​

For `delete` operations or for GraphQL mutations of the type *delete* , you can configure the following:

- [ Row permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/)
- [ Backend-only mutations ](https://hasura.io/docs/latest/auth/authorization/permissions/backend-only/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authorization/permissions/#introduction)
- [ Operation permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/#operation-permissions)
    - [ Select permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/#select-permissions)

- [ Insert permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/#insert-permissions)

- [ Update permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/#update-permissions)

- [ Delete permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/#delete-permissions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)