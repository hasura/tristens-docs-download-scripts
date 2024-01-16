# Security Best Practices

## Introduction​

This guide reviews security best practices that should be implemented when working on a Hasura Project. Applying API
security beyond RBAC (role-based access control) permissions is mandatory for any API moving towards a Hasura
deployment. We recommend that all HTTP layer security work be done at the API gateway level and GraphQL-specific
policies be applied at the Hasura level.

Security Announcements

Join the[ Hasura Security Announcements ](https://groups.google.com/forum/#!forum/hasura-security-announce)group for
emails about security announcements.

Image: [ Hasura/API security architecture ](https://hasura.io/docs/assets/images/best-practices-security-apihasura-diagram-4b11861ce823b59c97b5bcd535682c67.png)

Specifics about each security best practice can be found below.

## Hasura GraphQL Engine​

### Restrict Access​

Restrict knowledge of admin secrets to the minimally required team members as an admin secret provides unrestricted
access to the Hasura GraphQL Engine. SSO collaboration should be used to grant project access without sharing an admin
key. Subsequently, implement a plan to rotate admin secrets to limit the exposure of an admin secret being shared too
broadly.

[ Multiple admin secrets ](https://hasura.io/docs/latest/auth/authentication/multiple-admin-secrets/)should be used in situations where admin secrets have
different rotation timelines or when granting temporary access is needed.

Leverage[ allowed operations lists ](https://www.graphql-code-generator.com/plugins/other/hasura-allow-list)whenever
possible to restrict unbounded or unexpected operations from being executed against the GraphQL endpoint. Allow lists[ must be enabled ](https://hasura.io/docs/latest/security/allow-list/#enable-allow-list)via environment variable. These lists can be configured
globally or at the role level which allows for each role to have a differently defined set of permissible operations.
The allow list should include the complete set of expected operations for a given role to restrict the ability for a
user to execute non-permissible operations. Consider using the[ Hasura Allow List ](https://www.graphql-code-generator.com/plugins/other/hasura-allow-list)codegen plugin to
automatically generate allow list Metadata from your application code.

Note

The admin role will bypass the allowed operations list.

### Limit the API​

The allowed operations lists workflow is ideal for private/internal APIs or APIs with well understood and clearly
defined operations. Public APIs or APIs with less defined expected operations should additionally configure[ depth limits ](https://hasura.io/docs/latest/security/api-limits/#depth-limits)and[ node limits ](https://hasura.io/docs/latest/security/api-limits/#node-limits).

- Configure both[ rate limits ](https://hasura.io/docs/latest/security/api-limits/#rate-limits)and[ time limits ](https://hasura.io/docs/latest/security/api-limits/#time-limits)to restrict frequency and duration of operations.
- [ Limit rows ](https://hasura.io/docs/latest/auth/authorization/permissions/row-fetch-limit/)returned by a select operation.


Configure both[ rate limits ](https://hasura.io/docs/latest/security/api-limits/#rate-limits)and[ time limits ](https://hasura.io/docs/latest/security/api-limits/#time-limits)to restrict frequency and duration of operations.

[ Limit rows ](https://hasura.io/docs/latest/auth/authorization/permissions/row-fetch-limit/)returned by a select operation.

### Permissions​

The row-based access control configuration dictates permissions for the GraphQL API. It is critical that these
permissions be configured correctly in order to prevent unauthorized or unintended access to the GraphQL API.

- Review the[ permissions summary ](https://hasura.io/docs/latest/deployment/production-checklist/#review-the-summary)for each schema to verify
permissions are constructed appropriately for your expected data access.
- Configure an[ anonymous default role ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example)in
order to apply global security permissions. This default role should be configured similarly to any other role. This
includes[ RBAC permissions ](https://hasura.io/docs/latest/auth/authorization/quickstart/),[ API limits ](https://hasura.io/docs/latest/security/api-limits/),[ allowed operations lists ](https://www.graphql-code-generator.com/plugins/other/hasura-allow-list)and[ disabling schema introspection ](https://hasura.io/docs/latest/security/disable-graphql-introspection/).


Review the[ permissions summary ](https://hasura.io/docs/latest/deployment/production-checklist/#review-the-summary)for each schema to verify
permissions are constructed appropriately for your expected data access.

Configure an[ anonymous default role ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example)in
order to apply global security permissions. This default role should be configured similarly to any other role. This
includes[ RBAC permissions ](https://hasura.io/docs/latest/auth/authorization/quickstart/),[ API limits ](https://hasura.io/docs/latest/security/api-limits/),[ allowed operations lists ](https://www.graphql-code-generator.com/plugins/other/hasura-allow-list)and[ disabling schema introspection ](https://hasura.io/docs/latest/security/disable-graphql-introspection/).

### Disable development components​

There are several components of Hasura GraphQL Engine that are crucial for development efforts but should be disabled
for a production environment. However, it should be expected that some of these components may need to be temporarily
re-enabled if a situation arises where a production environment specific issue requires troubleshooting.

- [ Disable APIs ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-apis).
- [ Disable the Console ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-console).
- [ Disable dev mode ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode).
- [ Disable schema introspection ](https://hasura.io/docs/latest/security/disable-graphql-introspection/).


[ Disable APIs ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-apis).

[ Disable the Console ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-console).

[ Disable dev mode ](https://hasura.io/docs/latest/deployment/production-checklist/#disable-dev-mode).

[ Disable schema introspection ](https://hasura.io/docs/latest/security/disable-graphql-introspection/).

### Additional environment variables​

There are specific environment variables that should be configured to ensure appropriate communication to the Hasura
GraphQL Engine server.

- [ Allowed CORS requests ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#configure-cors).


## Database connections​

Hasura GraphQL Engine communicates with your data sources(s) via ODBC connection strings. This means Hasura has the same
permissions as the provided credentials in the connection string.

- Use environment variables rather than a hardcoded value when configuring the database connection string. This environment variable can then be reused in the other environments (e.g., staging or production) while containing a reference to the environment-specific database connection string.  Please see[ Metadata Best Practices ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-best-practices/)for more information.
- Review the database permissions allocated via the provided credentials to ensure the level of access granted to Hasura
is appropriate.
- Use database connections strings with the least privileges required for API operations.
- Configure[ read replicas ](https://hasura.io/docs/latest/databases/database-config/read-replicas/)to route read-only operations (queries) to one (or
many) read replicas.


Use environment variables rather than a hardcoded value when configuring the database connection string. This environment variable can then be reused in the other environments (e.g., staging or production) while containing a reference to the environment-specific database connection string.  Please see[ Metadata Best Practices ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-best-practices/)for more information.

Review the database permissions allocated via the provided credentials to ensure the level of access granted to Hasura
is appropriate.

Use database connections strings with the least privileges required for API operations.

Configure[ read replicas ](https://hasura.io/docs/latest/databases/database-config/read-replicas/)to route read-only operations (queries) to one (or
many) read replicas.

## Networking/API gateway​

We recommend the following HTTP layer security policies to be configured at the API gateway:

- [ Configure HTTPS ](https://hasura.io/docs/latest/deployment/enable-https/)on your reverse proxy to ensure encrypted communication between your
client and Hasura.
- Implement request and response size restrictions.
- Restricted allowed connection time to prevent incidents such as slowloris attacks.
- Apply both IP filtering and IP rate limiting.


Consider using a a[ web application firewall ](https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/)(WAF) as the
first line of defense. A firewall can provide extra protection against common attack types such as cross-site request
forgery (CSRF) by filtering and monitoring HTTP traffic between the application and the internet based on a rule set
configured by your team. Common WAF solutions include Cloudflare, Akamai and Imperva.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/security/security-best-practices/#limit-the-api/#introduction)
- [ Hasura GraphQL Engine ](https://hasura.io/docs/latest/security/security-best-practices/#limit-the-api/#hasura-graphql-engine)
    - [ Restrict Access ](https://hasura.io/docs/latest/security/security-best-practices/#limit-the-api/#restrict-access)

- [ Limit the API ](https://hasura.io/docs/latest/security/security-best-practices/#limit-the-api/#limit-the-api)

- [ Permissions ](https://hasura.io/docs/latest/security/security-best-practices/#limit-the-api/#permissions)

- [ Disable development components ](https://hasura.io/docs/latest/security/security-best-practices/#limit-the-api/#disable-development-components)

- [ Additional environment variables ](https://hasura.io/docs/latest/security/security-best-practices/#limit-the-api/#additional-environment-variables)
- [ Database connections ](https://hasura.io/docs/latest/security/security-best-practices/#limit-the-api/#database-connections)
- [ Networking/API gateway ](https://hasura.io/docs/latest/security/security-best-practices/#limit-the-api/#networkingapi-gateway)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759811/main-web/Group_11455_3_azgk7w.png)

### Securing your API with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)