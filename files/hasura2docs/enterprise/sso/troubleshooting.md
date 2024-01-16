# Troubleshooting Console SSO Errors

## Introduction​

This section provides references that can help in troubleshooting errors when integrating Console SSO.

## Troubleshooting​

### Could not verify JWT: JWTNotInIssuer.​

Make sure that the `issuer` config of Dex matches the `issuer` value in the `jwt_secret` value.

### Login Failed: user doesn't have permission​

Role values in the JWT token don't contain any role in the `admin_roles` config. If the structure of the JWT payload
doesn't follow the Hasura claim specification, you need to set the claim map JSON path to select the equivalent field
for role.

```
{
   "client_id" :   "example-app" ,
   // ...
   "jwt_secret" :   {
     "type" :   "RS256" ,
     "jwk_url" :   "http://dex:5556/dex/keys" ,
     "issuer" :   "http://localhost:5556/dex" ,
     "claims_map" :   {
       "x-hasura-allowed-roles" :   {   "path" :   "$.groups"   } ,
       "x-hasura-default-role" :   {   "path" :   "$.groups[0]"   }
     }
   }
}
```

If there isn't any equivalent field for the role, or you just want to test the authentication flow, you can hard-code
the `admin` role.

```
{
   // ...
   "admin_roles" :   [ "admin" ] ,
   "jwt_secret" :   {
     // ...
     "claims_map" :   {
       "x-hasura-allowed-roles" :   [ "admin" ] ,
       "x-hasura-default-role" :   "admin"
     }
   }
}
```

### Error fetching JWK: ConnectionFailure​

GraphQL Engine will fail to start if it can't fetch the JWK secret information from the remote Identity Provider. You
should verify if the IdP service is online and accepts connections.

If both services are in the same internal network - such as Docker or Kubernetes - and the GraphQL Engine instance is
unable to resolve the public DNS of the IdP service, you should change the domain of the JWK URL to the internal DNS
domain.

For example, in the SSO configuration of Dex IdP in the docker-compose stack, the `jwk_url` is set to `http://dex:5556` instead of `http://localhost:5556` .

```
{
   "client_id" :   "example-app" ,
   "authorization_url" :   "http://localhost:5556/dex/auth" ,   // public: the web browser can redirect to public dns only
   "request_token_url" :   "http://localhost:5556/dex/token" ,   // public: the web browser can request to public dns only
   "jwt_secret" :   {
     "type" :   "RS256" ,
     "jwk_url" :   "http://dex:5556/dex/keys"   // private dns: graphql engine connects to dex internally
   }
}
```

### Error fetching JWK: certificate rejected (CertificateUnknown)​

SSL certificate of the IdP service is a self-signed cert, and GraphQL Engine doesn't trust it. You need to either mount
the certificate file to the `/etc/ssl/certs/` folder, use the `HASURA_GRAPHQL_CERTIFICATE_AUTHORITY=<cert/path>` environment variable via the CLI, or disable CA verification through the TLS Allowlist feature.

If both GraphQL Engine and the IdP service are in the same internal network, you can consider using HTTP URL to the
private DNS domain of the IdP service.

### Debug the JWT​

Open the Network tab in the Developer Tool's panel to track HTTP requests. Find a `/v1/metadata` request which includes
a `Hasura-Sso-Token` request header and copy the token body. Finally, go to[ https://jwt.io/ ](https://jwt.io/)and paste the token to debug
the JSON content.

### Can I verify the authentication flow between Dex and Hasura EE without IdP?​

Dex supports mock connector and basic password authentication that you can use to verify the authentication flow between
Dex and Hasura EE first. The default role of the mock connector is `authors` , so make sure to add that role to the `admin_roles` list.

```
# dex/config.docker.yaml
connectors :
   -   type :  mockCallback
     id :  mock
     name :  Mock
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/enterprise/sso/troubleshooting/#introduction)
- [ Troubleshooting ](https://hasura.io/docs/latest/enterprise/sso/troubleshooting/#troubleshooting)
    - [ Could not verify JWT: JWTNotInIssuer. ](https://hasura.io/docs/latest/enterprise/sso/troubleshooting/#could-not-verify-jwt-jwtnotinissuer)

- [ Login Failed: user doesn't have permission ](https://hasura.io/docs/latest/enterprise/sso/troubleshooting/#login-failed-user-doesnt-have-permission)

- [ Error fetching JWK: ConnectionFailure ](https://hasura.io/docs/latest/enterprise/sso/troubleshooting/#error-fetching-jwk-connectionfailure)

- [ Error fetching JWK: certificate rejected (CertificateUnknown) ](https://hasura.io/docs/latest/enterprise/sso/troubleshooting/#error-fetching-jwk-certificate-rejected-certificateunknown)

- [ Debug the JWT ](https://hasura.io/docs/latest/enterprise/sso/troubleshooting/#debug-the-jwt)

- [ Can I verify the authentication flow between Dex and Hasura EE without IdP? ](https://hasura.io/docs/latest/enterprise/sso/troubleshooting/#can-i-verify-the-authentication-flow-between-dex-and-hasura-ee-without-idp)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)