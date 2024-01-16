# Enable Single Sign-on

## Introduction​

With Hasura Enterprise Edition, you can enable SSO (Single Sign-On) on the Hasura Console with your identity management
system through the[ OAuth 2.0 ](https://oauth.net)/[ OpenID Connect ](https://openid.net/connect)protocol.

Hasura provides full support for OAuth 2.0 as a Single Sign-On (SSO) solution without the need for additional tooling or
services. OAuth 2.0 is an industry-standard protocol that enables secure and delegated access to protected resources.

Hasura SSO can also be extended to use additional providers by leveraging[ Dex ](https://github.com/dexidp/dex).

Supported from

SSO is supported from versions `v2.24.0-beta.1` and above.

Image: [ Console SSO demo ](https://hasura.io/docs/assets/images/sso-animated-demo-c855f7e89531c0f69f9acb3ea7213392.gif)

Note

We only support the[ Proof Key for Code Exchange ](https://oauth.net/2/pkce/)extension to prevent CSRF and authorization
code injection attacks.

## Guides​

To get started, either use our general configuration guide or follow the specific instructions for your identity
provider:

- [ Single Sign-on configuration ](https://hasura.io/docs/latest/enterprise/sso/config/)
- [ Enable ADFS Single Sign-on ](https://hasura.io/docs/latest/enterprise/sso/adfs/)
- [ Enable Auth0 Single Sign-on ](https://hasura.io/docs/latest/enterprise/sso/auth0/)
- [ Enable Azure AD Single Sign-on ](https://hasura.io/docs/latest/enterprise/sso/azure-ad/)
- [ Enable Google Workspace Single Sign-on ](https://hasura.io/docs/latest/enterprise/sso/google-workspace/)
- [ Enable LDAP Single Sign-on ](https://hasura.io/docs/latest/enterprise/sso/ldap/)
- [ Troubleshooting ](https://hasura.io/docs/latest/enterprise/sso/troubleshooting/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/enterprise/sso/index/#introduction)
- [ Guides ](https://hasura.io/docs/latest/enterprise/sso/index/#guides)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)