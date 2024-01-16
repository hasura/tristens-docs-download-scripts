# Console SSO with LDAP

## Introduction​

SSO can be configured with LDAP by setting up[ Dex ](https://dexidp.io/docs/)as an OAuth2 proxy. Access can be
configured for all users of a domain or only for members of certain groups.

This guide assumes you have a Hasura GraphQL Engine instance running with a valid license key. If you don't have one,
you can get a license key via a[ 30-day free trial ](https://hasura.io/docs/latest/enterprise/try-hasura-enterprise-edition/)or by contacting the[ Hasura team ](mailto:sales@hasura.io).

Supported from

SSO for LDAP is supported from versions `v2.25.0` and above.

## Get started​

You can try the SSO configuration with[ this demo ](https://github.com/hasura/ee-sso-demo). The demo uses[ OpenLDAP ](https://www.openldap.org/)to integrate with Dex. You can clone the repository, edit the EE License Key
environment variable, and start up Docker Compose services.

```
git  clone https://github.com/hasura/ee-sso-demo.git
cd  ee-sso-demo
cp  dotenv .env
docker-compose  up -d
```

Finally, browse `http://localhost:8080` and try the SSO login.

## Walkthrough​

### Step 1: Configure Hasura​

The table below describes the configuration options for LDAP SSO. Hasura GraphQL Engine will expect these values to be
set as the value of the[ HASURA_GRAPHQL_SSO_PROVIDERS environment variable ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#single-sign-on-providers):

| Key | Example | Description |
|---|---|---|
|  `client_ id`  |  `dex-login`  | Any name identifying the Dex client |
|  `admin_ roles`  |  `["admin", "admins"]`  | X-hasura-roles that should be given admin access to Console |
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
     "admin_roles" :   [ "admin" ,   "admins" ] ,
     "name" :   "Dex Login" ,
     "authorization_url" :   "http://localhost:5556/dex/auth" ,
     "request_token_url" :   "http://localhost:5556/dex/token" ,
     "scope" :   "openid offline_access groups" ,
     "jwt_secret" :   {
       "type" :   "RS256" ,
       "jwk_url" :   "http://dex:5556/dex/keys" ,
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

### Step 2: Configure Dex​

Your Dex configuration will need the following fields set to enable LDAP SSO. You can find a sample configuration file
below. This file should be saved in the `/dex` directory of your container.

#### Issuer​

The base path of Dex and the external name of the OpenID Connect service. This is the canonical URL that all clients **must** use to refer to Dex. If a path is provided, Dex's HTTP service will listen at a non-root URL. This is the
public URL at which Dex is available.

Example:

`http://dex-domain:5556/dex`

#### Static clients​

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

#### Connectors​

The connectors field is an array of objects that define the various connectors being used in the Dex configuration. Each
object in the array contains a `type` field that specifies the type of connector being used. Here, we'll use `type: ldap` along with a series of fields that are specific to the LDAP connector.

```
connectors :
   -   type :  ldap
     name :  OpenLDAP
     id :  ldap
     config :
       # The following configurations seem to work with OpenLDAP:
       #
       # 1) Plain LDAP, without TLS:
       host :  ldap : 389
       insecureNoSSL :   true
       #
       # 2) LDAPS without certificate validation:
       #host: localhost:636
       #insecureNoSSL: false
       #insecureSkipVerify: true
       #
       # 3) LDAPS with certificate validation:
       #host: YOUR-HOSTNAME:636
       #insecureNoSSL: false
       #insecureSkipVerify: false
       #rootCAData: 'CERT'
       # ...where CERT="$( base64 -w 0 your-cert.crt )"
       # This would normally be a read-only user.
       bindDN :  cn=admin , dc=example , dc=org
       bindPW :  admin
       usernamePrompt :  Email Address
       userSearch :
         baseDN :  ou=People , dc=example , dc=org
         filter :   '(objectClass=person)'
         username :  mail
         # "DN" (case sensitive) is a special attribute name. It indicates that
         # this value should be taken from the entity's DN not an attribute on
         # the entity.
         idAttr :  DN
         emailAttr :  mail
         nameAttr :  cn
       groupSearch :
         baseDN :  ou=Groups , dc=example , dc=org
         filter :   '(objectClass=groupOfNames)'
         userMatchers :
           # A user is a member of a group when their DN matches
           # the value of a "member" attribute on the group entity.
           -   userAttr :  DN
             groupAttr :  member
         # The group name should be the "cn" value.
         nameAttr :  cn
```

You need to configure mappings for the login form, user and groups attributes. For instance with the LDAP configuration:

```
# User definitions
dn: ou=People,dc=example,dc=org
objectClass: organizationalUnit
ou: People
dn: cn=jane,ou=People,dc=example,dc=org
objectClass: person
objectClass: inetOrgPerson
sn: doe
cn: jane
mail: janedoe@example.com
userpassword: foo
# Group definitions.
dn: ou=Groups,dc=example,dc=org
objectClass: organizationalUnit
ou: Groups
dn: cn=admins,ou=Groups,dc=example,dc=org
objectClass: groupOfNames
cn: admins
member: cn=jane,ou=People,dc=example,dc=org
```

The attribute mappings configuration of Dex should be:

```
usernamePrompt :  Email Address
userSearch :
   baseDN :  ou=People , dc=example , dc=org
   filter :   '(objectClass=person)'
   # we want the user using email to login
   username :  mail
   # "DN" (case sensitive) is a special attribute name. It indicates that
   # this value should be taken from the entity's DN not an attribute on
   # the entity.
   idAttr :  DN
   emailAttr :  mail
   nameAttr :  cn
groupSearch :
   baseDN :  ou=Groups , dc=example , dc=org
   filter :   '(objectClass=groupOfNames)'
   userMatchers :
     # A user is a member of a group when their DN matches
     # the value of a "member" attribute on the group entity.
     -   userAttr :  DN
       groupAttr :  member
   # The group name should be the "cn" value.
   nameAttr :  cn
```

#### Sample configuration file for Dex​

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
   -   type :  ldap
     name :  OpenLDAP
     id :  ldap
     config :
       # The following configurations seem to work with OpenLDAP:
       #
       # 1) Plain LDAP, without TLS:
       host :  ldap : 389
       insecureNoSSL :   true
       #
       # 2) LDAPS without certificate validation:
       #host: localhost:636
       #insecureNoSSL: false
       #insecureSkipVerify: true
       #
       # 3) LDAPS with certificate validation:
       #host: YOUR-HOSTNAME:636
       #insecureNoSSL: false
       #insecureSkipVerify: false
       #rootCAData: 'CERT'
       # ...where CERT="$( base64 -w 0 your-cert.crt )"
       # This would normally be a read-only user.
       bindDN :  cn=admin , dc=example , dc=org
       bindPW :  admin
       usernamePrompt :  Email Address
       userSearch :
         baseDN :  ou=People , dc=example , dc=org
         filter :   '(objectClass=person)'
         username :  mail
         # "DN" (case sensitive) is a special attribute name. It indicates that
         # this value should be taken from the entity's DN not an attribute on
         # the entity.
         idAttr :  DN
         emailAttr :  mail
         nameAttr :  cn
       groupSearch :
         baseDN :  ou=Groups , dc=example , dc=org
         filter :   '(objectClass=groupOfNames)'
         userMatchers :
           # A user is a member of a group when their DN matches
           # the value of a "member" attribute on the group entity.
           -   userAttr :  DN
             groupAttr :  member
         # The group name should be the "cn" value.
         nameAttr :  cn
```

### Step 3: Update your deployment​

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
        ' [ { "client_id" :   "dex-login" , "admin_roles" :   [ "admin" ,   "authors" ] ,   "name" :   "Dex Login" , "authorization_url" :
         "http://127.0.0.1:5556/dex/auth" , "request_token_url" :   "http://127.0.0.1:5556/dex/token" , "scope" :  "openid
        offline_access groups" , "jwt_secret" :   { "type" :   "RS256" , "jwk_url" :   "http://dex:5556/dex/keys" , "issuer" :
         "http://127.0.0.1:5556/dex" , "claims_map" :   { "x-hasura-allowed-roles" :   {   "path" :   "$.groups"
         } , "x-hasura-default-role" :   {   "path" :   "$.groups[0]"   } } } } ] '
   dex :
     image :  dexidp/dex
     restart :  always
     volumes :
       -  ./dex/config.docker.yaml : /etc/dex/config.docker.yaml
     ports :
       -   '5556:5556'
volumes :
  postgres_data :
```

### Step 4: Log in​

At this point, you should see a `Dex Login` option on the Hasura Console. Now, you're ready to log in with your LDAP
account 🎉

Image: [ Dex on Hasura Console ](https://hasura.io/docs/assets/images/Dex-sso-b323db7bc347ff95ac0f7dc88664ed3b.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/enterprise/sso/ldap/#introduction)
- [ Get started ](https://hasura.io/docs/latest/enterprise/sso/ldap/#get-started)
- [ Walkthrough ](https://hasura.io/docs/latest/enterprise/sso/ldap/#walkthrough)
    - [ Step 1: Configure Hasura ](https://hasura.io/docs/latest/enterprise/sso/ldap/#step-1-configure-hasura)

- [ Step 2: Configure Dex ](https://hasura.io/docs/latest/enterprise/sso/ldap/#step-2-configure-dex)

- [ Step 3: Update your deployment ](https://hasura.io/docs/latest/enterprise/sso/ldap/#step-3-update-your-deployment)

- [ Step 4: Log in ](https://hasura.io/docs/latest/enterprise/sso/ldap/#step-4-log-in)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)