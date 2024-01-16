# Console SSO with Azure Active Directory

## Prerequisites​

This tutorial will help you set up Single Sign-on (SSO) for the Hasura Console with Azure Active Directory. We assume
that the following prerequisites have been met:

- To deploy Hasura EE, you will need a license key.[ Please contact Hasura Sales ](mailto:sales@hasura.io)if you do not
already have one.
- An Azure account and your Azure user has the required permissions to register an Azure AD application.
- You have[ Docker ](https://docs.docker.com/install/)and[ Docker Compose ](https://docs.docker.com/compose/install/)working on your machine.
- Hasura EE service is exposed at `http://localhost:8080`
- Dex service is exposed at `http://localhost:5556`


## Get started​

If you are new to Hasura GraphQL Engine, let's go through the[ Quickstart ](https://hasura.io/docs/latest/getting-started/docker-simple/)to help
you get up and running quickly with the Hasura GraphQL Engine and a Postgres database running as Docker containers using
Docker Compose. You also need to[ configure the EE license key ](https://hasura.io/docs/latest/enterprise/upgrade-ce-to-ee/)to enable Enterprise
features.

## Configuring Azure AD application​

Register an application for both OAuth and SAML SSO login, then add a single-page application with the following
callback URLs:

- `http://localhost:8080/console/oauth2/callback`
- `http://localhost:5556/dex/callback`


Implicit and hybrid flows

The ID tokens (used for implicit and hybrid flows) option must be checked.

Image: [ Register Azure AD application ](https://hasura.io/docs/assets/images/sso-azure-register-app-e26b553b023c47c52a367fda8bec2f7a.jpg)

The authorized user must have the `admin` role in claims. To do this you need to create the role in `App roles` tab.
Head back to `Enterprise applications` -> `<Your app>` -> `Users and groups` and assign the app role to the user.

Image: [ Create admin role ](https://hasura.io/docs/assets/images/sso-azure-create-admin-role-45eb0bf5d7ae5f58870eed1be1181e41.jpg)

Image: [ Azure AD assign role ](https://hasura.io/docs/assets/images/sso-azure-assign-role-85ef75ff06afe62b1b418f4015f909d2.jpg)

Finally, go to `App registrations` -> `<Your app>` -> `Overview` -> `Endpoints` to get the required configuration
endpoints.

Image: [ Azure AD endpoints ](https://hasura.io/docs/assets/images/sso-azure-endpoints-f2237ceb46bbb0ea80d4c75e35d72d9c.jpg)

## OAuth 2.0 configuration​

Hasura EE can handle the OAuth authorization flow directly. You only need to configure via[ --sso-providers ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#single-sign-on-providers)argument
( `HASURA_GRAPHQL_SSO_PROVIDERS` ).

```
[
   {
     "client_id" :   "<Application (client) ID>" ,
     "name" :   "Azure OAuth2 Login" ,
     // OAuth 2.0 authorization endpoint (v2)
     "authorization_url" :   "https://login.microsoftonline.com/<client-id>/oauth2/v2.0/authorize" ,
     // OAuth 2.0 token endpoint (v2)
     "request_token_url" :   "https://login.microsoftonline.com/<client-id>/oauth2/v2.0/token" ,
     "scope" :   "openid offline_access" ,
     "admin_roles" :   [ "admin" ] ,
     "jwt_secret" :   {
       "type" :   "RS256" ,
       // you can get jwt secret information in the OpenID Connect metadata document endpoint
       // https://login.microsoftonline.com/<client-id>/v2.0/.well-known/openid-configuration
       "jwk_url" :   "https://login.microsoftonline.com/<Directory (tenant) ID>/discovery/v2.0/keys" ,
       "issuer" :   "https://login.microsoftonline.com/<Directory (tenant) ID>/v2.0" ,
       "claims_map" :   {
         "x-hasura-allowed-roles" :   {   "path" :   "$.roles"   } ,
         "x-hasura-default-role" :   {   "path" :   "$.roles[0]"   }
       }
     }
   }
]
```

After configuring the variable, reload the Hasura GraphQL Engine service and browse the Console page to verify.

## SAML configuration​

You need to add the[ Dex ](https://github.com/dexidp/dex)service to docker-compose with[ SAML 2.0 ](https://dexidp.io/docs/connectors/saml/)connector configuration to proxy the Azure SAML login connector.

```
# docker-compose.yaml
services :
   dex :
     image :  dexidp/dex
     volumes :
       -  ./dex/config.docker.yaml : /etc/dex/config.docker.yaml
       -  ./dex/saml - ca.pem : /etc/dex/saml - ca.pem : ro
     ports :
       -   '5556:5556'
```

```
# ./dex/config.docker.yaml
issuer :  http : //localhost : 5556/dex
storage :
   type :  memory
web :
   http :  0.0.0.0 : 5556
   allowedOrigins :   [ '*' ]
staticClients :
   -   id :  hasura - app
     redirectURIs :
       -   'http://localhost:8080/console/oauth2/callback'
     name :   'Hasura App'
     public :   true
connectors :
   -   type :  saml
     id :  saml
     name :  SAML
     config :
       # SAML-P sign-on endpoint
       ssoURL :  https : //login.microsoftonline.com/<Directory (tenant) ID > /saml2
       ca :  /path/to/saml - ca.pem
       redirectURI :  http : //localhost : 5556/dex/callback
       usernameAttr :  http : //schemas.xmlsoap.org/ws/2005/05/identity/claims/name
       emailAttr :  http : //schemas.xmlsoap.org/ws/2005/05/identity/claims/name
       groupsAttr :  http : //schemas.microsoft.com/ws/2008/06/identity/claims/role
       entityIssuer :  spn : <client - id >
```

The `saml-ca.pem` file can be downloaded on the Azure portal UI if you create the SAML enterprise application directly.
However, if you create the application through App registrations, you can copy the certificate in the `Federation metadata document` into the `saml-ca.pem` file.

Image: [ Azure AD SAML Certificate ](https://hasura.io/docs/assets/images/sso-azure-saml-ca-23ed2792bc9a2f8216d3e7c9c04324a3.jpg)

```
-----BEGIN PRIVATE KEY-----
<paste here>
-----END PRIVATE KEY-----
```

Finally, add the provider config to the `HASURA_GRAPHQL_SSO_PROVIDERS` variables.

```
[
   {
     "client_id" :   "example-app" ,
     "name" :   "Dex SAML Login" ,
     "authorization_url" :   "http://127.0.0.1:5556/dex/auth" ,
     "request_token_url" :   "http://localhost:5556/dex/token" ,
     "scope" :   "openid offline_access groups" ,
     "admin_roles" :   [ "admin" ] ,
     "jwt_secret" :   {
       "type" :   "RS256" ,
       // use the internal docker service alias of dex
       // because hge fetches the secret inside the docker network
       "jwk_url" :   "http://dex:5556/dex/keys" ,
       "issuer" :   "http://localhost:5556/dex" ,
       "claims_map" :   {
         "x-hasura-allowed-roles" :   {   "path" :   "$.groups"   } ,
         "x-hasura-default-role" :   {   "path" :   "$.groups[0]"   }
       }
     }
   }
]
```

### What did you think of this doc?

- [ Prerequisites ](https://hasura.io/docs/latest/enterprise/sso/azure-ad/#prerequisites)
- [ Get started ](https://hasura.io/docs/latest/enterprise/sso/azure-ad/#get-started)
- [ Configuring Azure AD application ](https://hasura.io/docs/latest/enterprise/sso/azure-ad/#configuring-azure-ad-application)
- [ OAuth 2.0 configuration ](https://hasura.io/docs/latest/enterprise/sso/azure-ad/#oauth-20-configuration)
- [ SAML configuration ](https://hasura.io/docs/latest/enterprise/sso/azure-ad/#saml-configuration)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)