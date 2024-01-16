# Maintenance Mode

## Introduction​

When updates are being rolled out to your Hasura Cloud project which demand no interruptions to your instance's
configuration, maintenance mode is activated for your project.

Note

Currently, cloud maintenance mode will only be activated for your project while you are updating it to Hasura GraphQL
Engine `v2.0` .

Note

This is not to be confused with environment variable `HASURA_GRAPHQL_ENABLE_MAINTENANCE_MODE` . The two are different as
the env var enables the server maintenance mode which disables Metadata APIs (writes) on the project while the cloud
maintenance mode does not. See below for actions disabled by the cloud maintenance mode.

## Check if maintenance mode is activated​

Navigate to your project's settings page, you should see a top banner mentioning if your project is under maintenance.

Image: [ Project with maintenance mode activated ](https://hasura.io/docs/assets/images/maintenance-mode-f51148243c7d125a4875858176ad0d63.png)

If you don't see such a banner, your project is not under maintenance mode.

## Disabled actions when maintenance mode is activated​

All actions that update your project's configurations are not allowed when maintenance mode is activated. The following
actions are disallowed:

- [ Switching pricing plans ](https://hasura.io/docs/latest/hasura-cloud/projects/pricing/)
- [ Adding, updating and deleting an environment variable ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)
- [ Changing project region ](https://hasura.io/docs/latest/hasura-cloud/projects/regions/)
- [ Enabling and disabling Heroku database URL sync ](https://hasura.io/docs/latest/hasura-cloud/heroku-url-sync/)
- [ Deleting project ](https://hasura.io/docs/latest/hasura-cloud/projects/delete/)


If you are trying to apply these changes when maintenance mode is activated, you will encounter an error.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/projects/maintenance-mode/#introduction)
- [ Check if maintenance mode is activated ](https://hasura.io/docs/latest/hasura-cloud/projects/maintenance-mode/#check-if-maintenance-mode-is-activated)
- [ Disabled actions when maintenance mode is activated ](https://hasura.io/docs/latest/hasura-cloud/projects/maintenance-mode/#disabled-actions-when-maintenance-mode-is-activated)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)