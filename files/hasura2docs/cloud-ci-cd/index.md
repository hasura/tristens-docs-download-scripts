# Continuous Integration and Continuous Deployment with Hasura Cloud

## Introduction​

Hasura Cloud also enables automatically creating Preview Apps with Migrations and Metadata from a branch on a GitHub
repo by triggering a new deployment. These features are intended to improve the CI/CD experience on Hasura Cloud.

## Hasura Cloud GitHub Integration​

Hasura Cloud can automatically detect Metadata and Migration changes in a linked GitHub repo and deploy these changes to
the linked project. Read more on how to add this integration in your project[ here ](https://hasura.io/docs/latest/cloud-ci-cd/github-integration/).

## Hasura Cloud Preview Apps​

Hasura Cloud enables creating Preview Apps from a branch on GitHub. This allows you to spin up a Hasura Cloud Preview
App on each pull request in order to automatically preview changes.

This can be achieved using either of the following:

- [ Preview App GitHub Action ](https://hasura.io/docs/latest/cloud-ci-cd/preview-apps/#preview-apps-github-action)
- [ Preview App APIs ](https://hasura.io/docs/latest/cloud-ci-cd/preview-apps/#preview-apps-api)


Note

This feature is currently in beta. Please reach out through our support channels with any questions or concerns.

Usage Limit

For users with only `Free` tier projects on Hasura Cloud, usage of the Preview App API is limited to 60 calls per month.
More plans are coming soon.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/cloud-ci-cd/index/#introduction)
- [ Hasura Cloud GitHub Integration ](https://hasura.io/docs/latest/cloud-ci-cd/index/#hasura-cloud-github-integration)
- [ Hasura Cloud Preview Apps ](https://hasura.io/docs/latest/cloud-ci-cd/index/#hasura-cloud-preview-apps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)