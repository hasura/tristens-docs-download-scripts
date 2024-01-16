# Schema Registry

## Introduction​

The Schema Registry, as the name suggests, is a registry which stores all the GraphQL schemas that have existed on your
Hasura project. It is aimed at making your Hasura GraphQL schema changes more reliable, prevent breaking changes in the
schema and to make collaboration across large teams, microservices and roles more manageable and predictable. From the `API` tab, you can find the Schema Registry option at the top of the screen.

Image: [ Hasura Cloud Schema Registry Listing ](https://hasura.io/docs/assets/images/schema-registry-tab-af389d0ea4681848c310a2ee4cc9d63f.png)

Note

Schema Registry is available on Hasura Cloud from `v2.26.0-cloud.1` and above.

## How it works​

Whenever there is any operation on the Hasura Engine that could change the GraphQL schema, Hasura sends an event to the

Schema Registry along with the GraphQL schemas for all defined roles. Operations which could change the GraphQL schema
include:

- Applying new metadata
- Reloading metadata
- Hasura version update


Within the Schema Registry tab, you'll find an organized interface to explore schema changes. The layout consists of a
list of schema changes on the left side and an information card on the right, providing in-depth details about each
change.

By default, the Schema Registry showcases the alterations associated with the 'admin' role in the context of the latest
schema change. This default view simplifies the process of staying informed about the most recent schema adjustments for
this specific role.

For instance, below, you can see the changes displayed for the highlighted card, which contains details for both the `admin` and `user` roles.

The right section provides insights into how this specific schema change impacted the `admin` role, which is currently
selected. It reveals that there are the following changes concerning the `admin` role:

- `0` breaking changes
- `7` dangerous changes
- `4` safe changes


These numbers indicate that the schema has been modified in a manner that triggers the warnings and alerts mentioned.

Image: [ Hasura Cloud Schema Registry Role Based Changes ](https://hasura.io/docs/assets/images/schema-registry-change-details-122240048c116889e573295f5bd24ac6.png)

Note

If there was no previous schema to compare against, there will be no changes to present.

## Kind of schema changes​

The changes between subsequent schemas are computed using the open source[ GraphQL Inspector ](https://github.com/kamilkisiela/graphql-inspector).

### Breaking changes​

Breaking changes are typically the changes that could potentially break your GraphQL operations (queries, mutations or
subscriptions) at the GraphQL operation validation layer.

For example, if a field `name` is removed from a GraphQL object type `user` , that counts as a breaking change as it
could potentially fail an existing GraphQL operation that queries the `name` field in the `user` type.

### Dangerous changes​

Sometimes there are changes in your GraphQL schema that might not necessarily break your GraphQL operations at the
validation layer, but might sometimes affect their behaviours.

For example, if a new nullable field is added to an input type, that wouldn't break your GraphQL query but might affect
its execution. These changes are categorised as dangerous changes.

### Safe changes​

The GraphQL schema changes that can not affect your existing GraphQL operations are considered to be safe. These changes
typically include new type definitions and new fields in object types.

## Usage​

While there can be many use cases for the Schema Registry, it can primarily be used for reliable development, auditing,
and ensuring predictability of your GraphQL schema changes.

As new changes are deployed to a staging or pre-production environment, but before moving to production, you are able to
verify whether all the breaking and dangerous have been accounted for in queries made by clients of your GraphQL API.

Also, if you're using Hasura Cloud for development, you can see the schema changes with every change to your GraphQL
schema and update the corresponding GraphQL queries accordingly.

The Schema Registry can also be used to audit the past schemas of your project and observe when and how certain schema
changes took place.

## Alerts​

The Schema Registry provides the following options to configure notifications by clicking the bell icon in the Schema
Registry page:

### Email​

The Schema Registry sends an email to the **owner** of the project whenever there are any changes in the GraphQL schema
of the project.

{' '}

Image: [ Hasura Cloud Schema Registry Alert Config ](https://hasura.io/docs/assets/images/schema-registry-alert-config-8669c21059374825c6c484dcfaf71fed.png)

### Slack​

The Schema Registry sends an aggregate summary of GraphQL schema changes to the configured Slack channel of the
respective workspace. Follow these steps to configure Slack alerts:

1. Click the "Add to Slack" button in the Slack tab.
2. Select the Slack channel in your workspace in which you want alerts to appear. Click **Allow** to authorize.
3. Slack alerts should be configured for the selected channel in your workspace. You can choose to disable the alerts by
clicking on the delete icon.


Click the "Add to Slack" button in the Slack tab.

Image: [ Hasura Cloud Schema Registry Add To Slack ](https://hasura.io/docs/assets/images/add-to-slack-6a7c23bafc1ecb0e411d8caabf69b5b6.png)

Select the Slack channel in your workspace in which you want alerts to appear. Click **Allow** to authorize.

Image: [ Hasura Cloud Schema Registry Select Slack Channel ](https://hasura.io/docs/assets/images/select-slack-channel-8663192ae47fe840bd3736e471a0757a.png)

Slack alerts should be configured for the selected channel in your workspace. You can choose to disable the alerts by
clicking on the delete icon.

Image: [ Hasura Cloud Schema Registry Configured Slack Alerts ](https://hasura.io/docs/assets/images/configured-slack-alerts-43a8152e5db5248f49947aced2e3e42f.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/data-federation/schema-registry/#introduction)
- [ How it works ](https://hasura.io/docs/latest/data-federation/schema-registry/#how-it-works)
- [ Kind of schema changes ](https://hasura.io/docs/latest/data-federation/schema-registry/#kind-of-schema-changes)
    - [ Breaking changes ](https://hasura.io/docs/latest/data-federation/schema-registry/#breaking-changes)

- [ Dangerous changes ](https://hasura.io/docs/latest/data-federation/schema-registry/#dangerous-changes)

- [ Safe changes ](https://hasura.io/docs/latest/data-federation/schema-registry/#safe-changes)
- [ Usage ](https://hasura.io/docs/latest/data-federation/schema-registry/#usage)
- [ Alerts ](https://hasura.io/docs/latest/data-federation/schema-registry/#alerts)
    - [ Email ](https://hasura.io/docs/latest/data-federation/schema-registry/#email)

- [ Slack ](https://hasura.io/docs/latest/data-federation/schema-registry/#slack)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)