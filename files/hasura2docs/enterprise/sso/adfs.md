# Console SSO with Active Directory Federation Services (ADFS)

## Introduction​

SSO can be configured with ADFS SAML by setting up[ Dex ](https://dexidp.io/docs/)as an OAuth2 proxy. Access can be
configured for all users of a domain or only for members of certain groups.

This guide assumes you have a Hasura GraphQL Engine instance running with a valid license key. If you don't have one,
you can get a license key via a[ 30-day free trial ](https://hasura.io/docs/latest/enterprise/try-hasura-enterprise-edition/)or by contacting the[ Hasura team ](mailto:sales@hasura.io).

Supported from

SSO for ADFS is supported from versions `v2.25.0` and above.

## Step 1: Configure ADFS​

We assume that you have deployed the[ ADFS service ](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/ad-fs-deployment-guide). To
configure SAML for ADFS, you need to create a[ Relying party trust ](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/create-a-relying-party-trust)and make sure that:

- The `Enable support for the SAML 2.0 WebSSO protocol` checkbox is checked.
- The Dex callback URL is entered in the `Relying party SAML 2.0 SSO service URL` textbox.
- On the `Configure Identifiers page` , add a `Relying party trust identifier`


The `Enable support for the SAML 2.0 WebSSO protocol` checkbox is checked.

The Dex callback URL is entered in the `Relying party SAML 2.0 SSO service URL` textbox.

Image: [ Relying party SAML 2.0 SSO service URL ](https://hasura.io/docs/assets/images/sso-adfs-trust-party-url-93efee2291f22820d632bce34f3aa9e9.png)

On the `Configure Identifiers page` , add a `Relying party trust identifier` 

You'll need this later

You'll need the `Relying party trust identifier` to configure Dex's `entityIssuer` . Note this value.

### Add Claims​

After creating the Relying Party Trust, select the `Relying Party Trusts` folder from AD FS Management, and choose `Edit Claim Rules` from the Actions sidebar to add claims.

- To pass attributes of a user from LDAP, create a rule with the `Send LDAP Attributes as Claims` as a template.
- Choose `Active Directory` as your Attribute Store.
- Map your LDAP attributes to ongoing claim types. Dex only requires the `username` , `mail` , and role-equivalent fields.
- Click on the `View Rule Language` button to get the attribute name. These were the attribute names that were mapped in
the previous step.
- Click `Finish` and `Apply` the change in the `Edit Claim Issuance Policy` window.


To pass attributes of a user from LDAP, create a rule with the `Send LDAP Attributes as Claims` as a template.

Choose `Active Directory` as your Attribute Store.

Map your LDAP attributes to ongoing claim types. Dex only requires the `username` , `mail` , and role-equivalent fields.

Image: [ Add claims for SSO ADFS ](data:image/png;base64,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)

Click on the `View Rule Language` button to get the attribute name. These were the attribute names that were mapped in
the previous step.

Image: [ View XML attribute names ](https://hasura.io/docs/assets/images/sso-adfs-view-rule-04467c3c735710cd6a02ad520cede10a.png)

Click `Finish` and `Apply` the change in the `Edit Claim Issuance Policy` window.

### Export Signing Certificate​

Finally, you'll need to export the signing certificate from the ADFS console to mount it to Dex.

Image: [ ADFS SSO Certificates ](https://hasura.io/docs/assets/images/sso-adfs-certificates-b270c805254164f2c0ec6f9cf695d1aa.png)

1. Go to `ADFS > Service > Certificates` . Select the `Token-signing` certificate, and right-click to select `View Certificate` .
2. On the `Details tab` , click `Copy to File...` . This launches the Certificate Export Wizard. Click `Next` .
3. Choose `Base-64 encoded X.509 (.CER)` as the format you'd like to use. Click Next.
4. Download to the location where Dex is deployed.


## Step 2: Configure Hasura​

The table below describes the configuration options for ADFS SSO. Hasura GraphQL Engine will expect these values to be
set as the value of the[ HASURA_GRAPHQL_SSO_PROVIDERS ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#single-sign-on-providers)environment
variable:

| Key | Example | Description |
|---|---|---|
|  `client_ id`  |  `dex-login`  | Any name identifying the Dex client |
|  `admin_ roles`  |  `["admin"]`  | X-hasura-roles that should be given admin access to Console |
|  `name`  | Dex Login | A display name for this login method on the Console |
|  `authorization_ url`  |  `http://dex-endpoint-from-browser:port/dex/auth`  | Endpoint of Dex for auth request, should be reachable from browser |
|  `request_ token_ url`  |  `http://dex-endpoint-from-browser:port/dex/token`  | Endpoint of Dex for token request, should be reachable from browser |
|  `scope`  |  `openid offline_ access groups`  | Oauth2 scopes to be used against Dex |
|  `jwt_ secret. type`  |  `RS256`  | Key type Dex is configured with |
|  `jwt_ secret. jwk_ url`  |  `http://dex-endpoint-from-hasura:port/dex/keys`  | JWK URL that is published by dex |
|  `jwt_ secret. issuer`  |  `http://dex-endpoint-from-browser:port/dex`  | Issuer that is configured with Dex, same as issuer in Dex configuration, this is typically the endpoint at which Dex can be reached at |
|  `jwt_ secret. claims_ map`  |  `{"x-hasura-allowed-roles": {"path": "$. groups"},"x-hasura-default-role": {"path": "$. groups[0]"}}`  | Mapping groups parsed by Dex to roles on Hasura |


Using the information above as an example, you can configure the `HASURA_GRAPHQL_SSO_PROVIDERS` environment variable as
follows:

```
[
   {
     "client_id" :   "dex-login" ,
     "admin_roles" :   [ "admin" ] ,
     "name" :   "Dex Login" ,
     "authorization_url" :   "http://localhost:5556/dex/auth" ,
     "request_token_url" :   "http://localhost:5556/dex/token" ,
     "scope" :   "openid offline_access groups" ,
     "jwt_secret" :   {
       "type" :   "RS256" ,
       "jwk_url" :   "http://localhost:5556/dex/keys" ,
       "issuer" :   "http://localhost:5556:5556/dex" ,
       "claims_map" :   {
         "x-hasura-allowed-roles" :   {
           "path" :   "$.groups"
         } ,
         "x-hasura-default-role" :   {
           "path" :   "$.groups[0]"
         }
       }
     }
   }
]
```

Setting environment variables

For guidance on setting environment variables or flags for Hasura GraphQL Engine, see[ server configuration ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/index/).

## Step 3: Configure Dex​

Your Dex configuration will need the following fields set to enable ADFS SAML SSO. You can find a sample configuration
file below. This file should be saved in the `/dex` directory of your container.

### Issuer​

The base path of Dex and the external name of the OpenID Connect service. This is the canonical URL that all clients **must** use to refer to Dex. If a path is provided, Dex's HTTP service will listen at a non-root URL. This is the
public URL at which Dex is available.

Example:

`http://dex-domain:5556/dex`

### Static clients​

This contains the `id` and `redirectURIs` . The `id` will reference the `client_id` in the Hasura configuration. The `redirectURIs` will be the oauth callback URL of Hasura Console, which is at `http(s)://<hasura-endpoint>/console/oauth2/callback` .

Example:

```
staticClients :
   -   id :  dex - login
     redirectURIs :
       -   'http://localhost:8080/console/oauth2/callback'
     name :   'Dex Login'
     public :   true
```

### Connectors​

The connectors field is an array of objects that define the various connectors being used in the Dex configuration. Each
object in the array contains a type field that specifies the type of connector being used. Here, we'll use `type: saml` along with a series of fields that are specific to the SAML connector.

```
connectors :
   -   type :  saml
     id :  saml - auth0
     name :  Auth0 SAML
     config :
       ssoURL :  https : //sts.example.local/adfs/ls/
       ca :  /etc/dex/saml - ca.pem
       # insecureSkipSignatureValidation: true
       redirectURI :  http : //localhost : 5556/dex/callback
       usernameAttr :  http : //schemas.xmlsoap.org/ws/2005/05/identity/claims/name
       emailAttr :  http : //schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
       groupsAttr :  http : //schemas.xmlsoap.org/ws/2005/05/identity/claims/role
       entityIssuer :  https : //sts.example.local/adfs/ls/
```

### Sample configuration file for Dex​

```
# The base path of dex and the external name of the OpenID Connect service.
# This is the canonical URL that all clients MUST use to refer to dex. If a
# path is provided, dex's HTTP service will listen at a non-root URL.
# Public URL that dex is available at
issuer :  http : //localhost : 5556/dex
# The storage configuration determines where dex stores its state. Supported
# options include SQL flavors and Kubernetes third party resources.
#
# See the documentation (https://dexidp.io/docs/storage/) for further information.
storage :
   type :  sqlite3
   config :
     file :  /var/dex/dex.db
# Configuration for the HTTP endpoints.
web :
   http :  0.0.0.0 : 5556
   allowedOrigins :   [ '*' ]
   # Uncomment for HTTPS options.
   # https: 127.0.0.1:5554
   # tlsCert: /etc/dex/tls.crt
   # tlsKey: /etc/dex/tls.key
# Uncomment this block to enable configuration for the expiration time durations.
# Is possible to specify units using only s, m and h suffixes.
# expiry:
#   deviceRequests: "5m"
#   signingKeys: "6h"
#   idTokens: "24h"
#   refreshTokens:
#     reuseInterval: "3s"
#     validIfNotUsedFor: "2160h" # 90 days
#     absoluteLifetime: "3960h" # 165 days
# Options for controlling the logger.
# logger:
#   level: "debug"
#   format: "text" # can also be "json"
oauth2 :
   responseTypes :   [ 'code' ]   # also allowed are "token" and "id_token"
   skipApprovalScreen :   true
#
staticClients :
   -   id :  dex - login
     redirectURIs :
       -   'http://localhost:8080/console/oauth2/callback'
     name :   'Dex Login'
     public :   true
connectors :
   -   type :  saml
     id :  saml - auth0
     name :  Auth0 SAML
     config :
       ssoURL :  https : //sts.example.local/adfs/ls/
       ca :  /etc/dex/adfs - saml.cer
       # insecureSkipSignatureValidation: true
       redirectURI :  http : //localhost : 5556/dex/callback
       usernameAttr :  http : //schemas.xmlsoap.org/ws/2005/05/identity/claims/name
       emailAttr :  http : //schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
       groupsAttr :  http : //schemas.xmlsoap.org/ws/2005/05/identity/claims/role
       entityIssuer :  https : //sts.example.local/adfs/ls/
```

## Step 4: Update your deployment​

Finally, you'll need to configure your deployment with these changes. Here is a Docker Compose example, with the
configuration:

```
version :   '3.8'
services :
   postgres :
     image :  postgres : 15
     restart :  always
     volumes :
       -  postgres_data : /var/lib/postgresql/data
     ports :
       -   '5432'
     environment :
       POSTGRES_PASSWORD :  postgrespassword
   hasura-pro :
     image :  hasura/graphql - engine : v2.25.0
     ports :
       -   '8080:8080'
     depends_on :
       -  postgres
     restart :  always
     environment :
       HASURA_GRAPHQL_EE_LICENSE_KEY :  <YOUR_EE_LICENSE_KEY >
       HASURA_GRAPHQL_ADMIN_SECRET :  <YOUR_ADMIN_SECRET >
       HASURA_GRAPHQL_DATABASE_URL :  postgres : //postgres : postgrespassword@postgres : 5432/postgres ? sslmode=disable
       HASURA_GRAPHQL_ENABLE_CONSOLE :   'true'
       HASURA_GRAPHQL_DEV_MODE :   'true'
       HASURA_GRAPHQL_ENABLED_LOG_TYPES :  startup , http - log , webhook - log , websocket - log , query - log
       HASURA_GRAPHQL_ENABLED_APIS :  metadata , graphql , config , metrics
       HASURA_GRAPHQL_METRICS_SECRET :  <YOUR_METRICS_SECRET >
       HASURA_GRAPHQL_CONSOLE_ASSETS_DIR :  /srv/console - assets
       HASURA_GRAPHQL_SSO_PROVIDERS :
        ' [ { "client_id" :   "dex-login" , "admin_roles" :   [ "hasura-admin@company.com" ] ,   "name" :  "Dex
        Login" , "authorization_url" :   "http://127.0.0.1:5556/dex/auth" , "request_token_url" :
         "http://127.0.0.1:5556/dex/token" , "scope" :   "openid offline_access groups" , "jwt_secret" :   { "type" :
         "RS256" , "jwk_url" :   "http://dex:5556/dex/keys" , "issuer" :   "http://127.0.0.1:5556/dex" , "claims_map" :
         { "x-hasura-allowed-roles" :   {   "path" :   "$.groups"   } , "x-hasura-default-role" :   {   "path" :   "$.groups[0]"   } } } } ] '
   dex :
     image :  dexidp/dex
     restart :  always
     volumes :
       -  ./dex/config.docker.yaml : /etc/dex/config.docker.yaml
       -  ./dex/adfs - saml.cer : /dex/adfs - saml.cer
     ports :
       -   '5556:5556'
volumes :
  postgres_data :
```

## Step 5: Log in​

At this point, you should see a `Dex Login` option on the Hasura Console. Now, you're ready to log in with your ADFS
account 🎉

Image: [ Dex on Hasura Console ](https://hasura.io/docs/assets/images/Dex-sso-b323db7bc347ff95ac0f7dc88664ed3b.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/enterprise/sso/adfs/#introduction)
- [ Step 1: Configure ADFS ](https://hasura.io/docs/latest/enterprise/sso/adfs/#step-1-configure-adfs)
- [ Step 2: Configure Hasura ](https://hasura.io/docs/latest/enterprise/sso/adfs/#step-2-configure-hasura)
- [ Step 3: Configure Dex ](https://hasura.io/docs/latest/enterprise/sso/adfs/#step-3-configure-dex)
- [ Step 4: Update your deployment ](https://hasura.io/docs/latest/enterprise/sso/adfs/#step-4-update-your-deployment)
- [ Step 5: Log in ](https://hasura.io/docs/latest/enterprise/sso/adfs/#step-5-log-in)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)