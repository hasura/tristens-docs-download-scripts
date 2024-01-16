# Hasura Version Support Policy

## Releases and support​

Hasura releases its software via:

- **Major versions** that may have incompatible or breaking changes from the previous version.
- **Minor versions** that provide new functionality and bug fixes in a backwards-compatible manner.
- **Patch versions** that have backwards-compatible bug fixes.


Hasura provides support for a given major or minor version of our software to eligible customers. Support includes:

1. **Bug fixes** : Critical issues or bugs identified in the software are either provided a workaround or addressed
through minor or patch versions.
2. **Security updates** : Updates are provided via patches to address known security vulnerabilities in the software.
3. **Technical support** : Assistance is provided to users who encounter issues or have questions about the software.


Hasura will support the latest minor version of the previous major version of the GraphQL Engine, including critical
security updates, for up to one year after the release of the current major version.

You can find the latest version — and all changelog entries for each version — of the Hasura GraphQL Engine on the[ Hasura GraphQL Engine releases page ](https://github.com/hasura/graphql-engine/releases).

## Long-term support (LTS) releases​

Hasura also provides long term support (LTS) releases of the Hasura GraphQL Engine (HGE) for Hasura Enterprise Edition
customers. An LTS version is a combination of a major and minor version. *For example: Hasura v2.11* .

`v2.11`

While we recommend our users to be on the latest release, we recognize the need for a long-term support release where
upgrading to a new feature release requires significant effort and planning, and there is a need to be up-to-date on
critical security fixes and critical bug fixes.

- Hasura will support GraphQL Engine LTS releases for versions that are part of the Enterprise Edition packages.
- LTS releases will include critical security fixes, determined by Hasura with input from the customer's IT security
department, that leave the environment vulnerable to external threats.
- LTS releases will include bug fixes that are determined by Hasura to be critical or high priority and are causing the
Hasura GraphQL Engine to be inoperable in production.
- Security and critical bug fixes will be patched to a designated LTS version release. *E.g., v2.x.1 will have the
first set of patches to the LTS version v2.x.0.*
- An LTS release will be supported for two years from the initial release date.
- A new LTS version will be announced annually (at a minimum).


`v2.x.1`

`v2.x.0.`

LTS releases will not include new (or extended) features that are released in future major or minor versions.

## Support and EOL for current LTS versions​

| LTS version | EOL Date |
|---|---|
|  `v2. 11`  | Sep-01-2024 |


### What did you think of this doc?

- [ Releases and support ](https://hasura.io/docs/latest/policies/versioning/#releases-and-support)
- [ Long-term support (LTS) releases ](https://hasura.io/docs/latest/policies/versioning/#long-term-support-lts-releases)
- [ Support and EOL for current LTS versions ](https://hasura.io/docs/latest/policies/versioning/#support-and-eol-for-current-lts-versions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)