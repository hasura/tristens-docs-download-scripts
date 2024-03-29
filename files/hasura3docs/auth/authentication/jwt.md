# Authentication Using JWTs

## Introduction​

This page details how to configure Hasura Engine to use JWT mode in order to authenticate incoming requests.

This process requires that your auth service returns a JWT to the client, which it passes to Hasura GraphQL
Engine in an: `Authorization: Bearer <JWT>` header of the request.

Hasura then verifies and decodes the JWT to extract `x-hasura-*` session variable claim values. The `x-hasura-role` session variable is required, and you will also most likely utilize the user id and any other information which you
need to determine access to your data.

Image: [ Authentication using JWT ](https://hasura.io/docs/3.0/assets/images/auth-jwt-overview-diagram-afcb2de929684d64f9784dc42b9f5ddd.png)

## JWT authentication​

You can enable JWT mode by configuring your metadata appropriately:

### Example​

```
key :
   fixed :
     algorithm :  HS256
     key :
       value :  token
tokenLocation :
   type :  BearerAuthorization
claimsConfig :
   namespace :
     claimsFormat :  Json
     location :   "/https:~1~1hasura.io~1jwt~1claims"
```

### All jwt configuration fields​

```
key :
   # either `fixed` or `jwkFromUrl` is expected.
   fixed :
     algorithm :  required - algorithm - to - be - used - to - decode - the - JWT
     key :  required - key - as - string
   jwkFromUrl :  required - JWK - url
claimsConfig :
   # either `namespace` or `locations` is expected.
   namespace :
     location :  optional - json - pointer - to - the - claims - default - https : //hasura.io/jwt/claims
     claimsFormat :  optional - claims - format - default - Json
   locations :
     # Object with keys as session variables and values as object
     x-hasura-role :
       # either `literal` or `path` is expected.
       literal :  required - string
       path :
         path :  required - json - pointer - to - the - claim
         default :  optional - default
tokenLocation :  required - object - to - indicate - cookie - or - authorization - header - or - custom - header
audience :   "<optional-string-or-list-of-strings-to-verify-audience>"
issuer :   "<optional-string-to-verify-issuer>"
allowedSkew :   "<optional-number-of-seconds-in-integer>"
```

### Metadata structure​

| Field | Type | Required | Description |
|---|---|---|---|
|  `key`  | [ JWT key ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-key) | true | JWT key type to configure the JWT authentication. |
|  `claimsConfig`  | [ Claims Config ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-claims-config) | true | Configuration of the Hasura claims within the JWT. |
|  `tokenLocation`  | [ Object ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-token-location-values) | true | Declares the request header or the cookie (with cookie name) from which to read the JWT. Default: `{"type": "tokenLocationValues"}` . |
|  `audience`  | String | false | When set, verifies the `aud` claims in the JWT to be equal to this value. |
|  `issuer`  | String | false | When set, verifies the `iss` claim in the JWT claim equal to this value. |
|  `allowedSkew`  | Int | false | Optional field to provide some leeway (to account for clock skews) while comparing the JWT expiry time. This field expects an integer value which will be the number of seconds of the skew value. |


#### JWT key​

| Field | Type | Required | Description |
|---|---|---|---|
|  `fixed`  | [ Fixed key ](https://hasura.io/docs/3.0/auth/authentication/jwt/#fixed-jwt-key) | false | Fixed JWT mode, when the `algorithm` and the `key` fields are known and aren't expected to change during runtime. |
|  `jwkFromUrl`  | URL | false | JWK URL from which the graphql-engine will determine the `algorithm` and `key` fields from dynamically. |


Note

Either, the `fixed` or the `jwkFromUrl` is expected.

##### Fixed JWT key​

| Field | Type | Required | Description |
|---|---|---|---|
|  `algorithm`  | String | false | Algorithm used to decode the JWT. Possible values are: `HS256` , `HS384` , `HS512` , `ES256` , `ES384` , `RS256` , `RS384` , `RS512` , `PS256` , `PS384` , `PS512` and `EdDSA` . |
|  `key`  | String | false | Key to decode the JWT. |


#### JWT claims config​

| Field | Type | Required | Description |
|---|---|---|---|
|  `namespace`  | [ Namespace ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-claims-namespace) | false | Used when all of the Hasura claims are present in a single object within the decoded JWT. |
|  `claimsMap`  | [ Claims Map ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-claimsmap) | false | Can be used when Hasura claims are not all present in the single object, but individual claims are either provided a default value or a JSON pointer within the decoded JWT. |


Note

Either, the `namespace` or the `claimsMap` is expected. If neither is present, then the default `namespace` value is used.

##### JWT claims namespace​

| Field | Type | Required | Description |
|---|---|---|---|
|  `path`  | [ JSON Pointer ](https://www.rfc-editor.org/rfc/rfc6901) | true | JSON pointer to the Hasura claims object.  Default: "https:~1~1hasura.io~1jwt~1claims" (JSON Pointer for `https://hasura. io/jwt/claims` ). |
|  `format`  | String | false | Format of the Hasura claims object. Possible values ( `Json` , `StringifiedJson` ). Default value: `Json` . |


##### JWT claims map​

| Field | Type | Required | Description |
|---|---|---|---|
|  `x-hasura-allowed-roles`  | [ Claims Map Object ([String]) ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-claims-map-object) | true | JSON pointer to the Hasura claims object. |
|  `x-hasura-default-role`  | [ Claims Map Object (String) ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-claims-map-object) | true | JSON pointer to the Hasura claims object. |
| Custom claim* | [ Claims Map Object (String) ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-claims-map-object) | false | JSON pointer to the custom Hasura claim. |


Note

Any number of Custom claims can be added to the claims map.

###### JWT claims map object <T>​

`<T>`

| Field | Type | Required | Description |
|---|---|---|---|
|  `literal`  |  `<T>`  | false | Literal value of the Hasura claim. |
|  `path`  | [ JSON claims map path object ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-claims-map-path-object) | false | Get claim value using a JSON pointer to the Hasura claim with a fallback default value, if the value is not present at the JSON pointer. |


###### JWT claims map path object <T>​

`<T>`

| Field | Type | Required | Description |
|---|---|---|---|
|  `path`  | [ JSON Pointer ](https://www.rfc-editor.org/rfc/rfc6901) | false | JSON pointer to the Hasura claim. |
|  `default`  |  `<T>`  | false | Default value of the Hasura claim, if there is no value present at the `path` . |


Note

For `x-hasura-allowed-roles` , `<T>` will be `[String]` and for `x-hasura-default-role` or any other custom claims, `<T>` will be a `String` .

#### JWT token location values​

| Field | Type | Required | Description |
|---|---|---|---|
|  `BearerAuthorization`  | String | false | JWT is provided in the `Authorization` header in the format of `Bearer <JWT>`  |
|  `Header`  | Object | false | Name of the header which will contain the JWT. A JSON object with the name of the custom header is expected like: `{ "Header": "<custom-header-name>" }`  |
|  `Cookie`  | Object | false | JWT is provided in the `Cookie` header. A JSON object with the name of the cookie is expected like: `{ "Cookie": "<custom-cookie-name>" }`  |


### Example Decoded Payload​

```
{
   "sub" :   "1234567890" ,
   "name" :   "John Doe" ,
   "admin" :   true ,
   "iat" :   1516239022 ,
   "https://hasura.io/jwt/claims" :   {
     "x-hasura-default-role" :   "user" ,
     "x-hasura-allowed-roles" :   [ "user" ,   "admin" ] ,
     "x-hasura-user-id" :   "123" ,
     "x-hasura-org-id" :   "456" ,
     "x-hasura-custom" :   "custom-value"
   }
}
```

### Example Encoded JWT​

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjI
zOTAyMiwiaHR0cHM6Ly9oYXN1cmEuaW8vand0L2NsYWltcyI6eyJ4LWhhc3VyYS1kZWZhdWx0LXJvbGUiOiJ1c2VyIiwieC1oYXN1cmEtYWxsb3dlZC1yb2x
lcyI6WyJ1c2VyIiwiYWRtaW4iXSwieC1oYXN1cmEtdXNlci1pZCI6IjEyMyIsIngtaGFzdXJhLW9yZy1pZCI6IjQ1NiIsIngtaGFzdXJhLWN1c3RvbSI6ImN
1c3RvbS12YWx1ZSJ9fQ.07mlUOhH3Oigz_Yyil8EC579Ht6PbZ1yr8fYJfhQ4NE
```

 **Note:**  `x-hasura-default-role` and `x-hasura-allowed-roles` are mandatory, while the rest of the claims are optional.

[ See here for the JWT debugger ](https://jwt.io/#debugger-io?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMiwiaHR0cHM6Ly9oYXN1cmEuaW8vand0L2NsYWltcyI6eyJ4LWhhc3VyYS1kZWZhdWx0LXJvbGUiOiJ1c2VyIiwieC1oYXN1cmEtYWxsb3dlZC1yb2xlcyI6WyJ1c2VyIiwiYWRtaW4iXSwieC1oYXN1cmEtdXNlci1pZCI6IjEyMyIsIngtaGFzdXJhLW9yZy1pZCI6IjQ1NiIsIngtaGFzdXJhLWN1c3RvbSI6ImN1c3RvbS12YWx1ZSJ9fQ.07mlUOhH3Oigz_Yyil8EC579Ht6PbZ1yr8fYJfhQ4NE)of this example JWT token. The signature secret is `ultra-secret-very-secret-super-secret-key` .

### Hasura JWT format​

The `x-hasura-role` value can be sent as a plain **header** in the request to indicate the role which should be used.

When your auth server generates the JWT, the custom claims in the JWT **must contain the following** in a custom
claims namespace:

1. A `x-hasura-allowed-roles` field. A list of allowed roles for the user i.e. acceptable values of the optional `x-hasura-role`  *header* .[ See more ](https://hasura.io/docs/3.0/auth/authentication/jwt/#x-hasura-allowed-roles)
2. A `x-hasura-default-role` field. The role that will be used when the optional `x-hasura-role`  *header* is **not
passed** .[ See more ](https://hasura.io/docs/3.0/auth/authentication/jwt/#x-hasura-default-role)
3. Add any other optional `x-hasura-*` claim fields (required as per your defined permissions) to the custom
namespace.[ See more ](https://hasura.io/docs/3.0/auth/authentication/jwt/#x-hasura-)


The JWT should be sent to Hasura Engine in an: `Authorization: Bearer <JWT>` header. Eg:

```
POST   /v1/graphql   HTTP/1.1
Authorization :   Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWI...
X-Hasura-Role :   editor
...
```

To summarize, `x-hasura-allowed-roles` session variable contains a list of all the roles that the user can assume
and the `x-hasura-role` header tells the Hasura Engine which role to use for the request, and if that is missing
then the `x-hasura-default-role` session variable will be used.

This setup makes it more convenient for a JWT to only need to be issued once with a list of allowed roles for the
user, and then allow the client to decide which of those roles to actually use for a request. This prevents the user
needing to log in again or unnecessary JWT re-issuance.

If, for example, your app will not need to switch user roles and the user only needs one role, for instance: `user` ,
you can just issue a JWT with `x-hasura-default-role` set to `user` and `x-hasura-allowed-roles` set to `["user"]` and not send the `x-hasura-role` header in the request.

This setup is designed so that there is one authoritative way to construct your JWT token for the Hasura Engine which
can cover a wide range of use cases.

### Hasura JWT Claim Description​

#### x-hasura-allowed-roles​

The `x-hasura-allowed-roles` list can contain all the roles which a particular user can assume, eg: `[ "user", "manager", "owner" ]` . Usually, these will have varying degrees of access to your data as specified in
Permissions and by specifying this list it lets the Hasura Engine know that this user
can assume any of them.

#### x-hasura-default-role​

The `x-hasura-default-role` will be the role that the user falls back to when no `x-hasura-role` value is
specified in the header of the request. Usually, this will be the role with the least privileges and can be
overridden by the `x-hasura-role` header when making a request.

#### x-hasura-*​

The JWT can have other user-defined `x-hasura-*` fields and their values can only be strings (they will be converted to
the right type automatically). You can use these `x-hasura-*` values in your permission rules.

The JWT will normally also contain standard ( `sub` , `iat` etc.) and custom ( `name` , `admin` etc.) claims

### JWT Notes​

- JWT claim fields eg: `x-hasura-default-role` are case-insensitive.
- Hasura GraphQL Engine only has access to headers and JWT claims which are prefixed with `x-hasura-` .
- Hasura GraphQL Engine only has access to JWT claims in the `https://hasura.io/jwt/claims` or[ custom defined ](https://hasura.io/docs/3.0/auth/authentication/jwt/#claims-namespace-path)namespace.
- All `x-hasura-*` values should be of type `String` , they will be converted to the right type automatically.


## Hasura JWT configuration options​

### type​

This specifies the cryptographic signing algorithm which is used to sign the JWTs. Valid values are : `HS256` , `HS384` , `HS512` , `RS256` , `RS384` , `RS512` , `Ed25519` , `ES256` , `ES384` , `ES512` . (see[ https://jwt.io ](https://jwt.io/)).

 `HS*` is for HMAC-SHA based algorithms. `RS*` is for RSA based signing. `Ed*` is for Edwards-curve Digital Signature
algorithms. `ES*` is for Elliptic-curve Digital Signature algorithms. For example, if your auth server is using
HMAC-SHA256 for signing the JWTs, then use `HS256` . If it is using RSA with SHA-512, then use `RS512` . If it is using an
EdDSA instance of Edwards25519, then use `Ed25519` . If it is using an ES instance of ECDSA with 256-bit curve, then use `ES256` .

This is an optional field. This is required only if you are using the `key` property in the config.

### key​

- In the case of a symmetric key (i.e. a HMAC-based key), just the key as is. (e.g. -"abcdef..."). The key must be long
enough for the chosen algorithm, (e.g. for HS256 it must be at least 32 characters long).
- In the case of an asymmetric key (RSA, EdDSA, ECDSA etc.), only the **public** key, in a PEM-encoded string or as an
X509 certificate.


This is an optional field. You can also provide a URL to fetch JWKs from using the `jwkUrl` field.

### jwkUrl​

An URL where a provider publishes their JWKs (JSON Web Keys - which are used for signing the JWTs). The URL **must** publish the JWKs in the standard format as described[ here ](https://tools.ietf.org/html/rfc7517).

This is optional as you have the alternative of also providing the key (certificate, PEM-encoded public key) as a
string - in the[ key ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-json-key)field along with the[ type ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-json-type).

### claimsNamespacePath​

This is an optional field. You can specify the key name, inside which the Hasura specific claims will be present, e.g. `https://mydomain.com/claims` . The default value is `https://hasura.io/jwt/claims` .

##### Configure claimsNamespacePath​

`claimsNamespacePath`

An optional JSON path value to the Hasura claims present in the JWT token. Example values are `/hasura/claims` or `/` (i.e. root of the payload).

The JWT token should be in the following format if the `claimsNamespacePath` is set to `/hasura/claims` :

```
{
   "sub" :   "1234567890" ,
   "name" :   "John Doe" ,
   "admin" :   true ,
   "iat" :   1516239022 ,
   "hasura" :   {
     "claims" :   {
       "x-hasura-allowed-roles" :   [ "editor" ,   "user" ,   "mod" ] ,
       "x-hasura-default-role" :   "user" ,
       "x-hasura-user-id" :   "1234567890" ,
       "x-hasura-org-id" :   "123" ,
       "x-hasura-custom" :   "custom-value"
     }
   }
}
```

Claims namespace values

When the `claimsNamespacePath` is not set, the default value is `https:~1~1hasura.io~1jwt~1claims` (JSON pointer
for claims namespace).

### claimsFormat​

This is an optional field, with only the following possible values allowed: `json` , `stringifiedJson` .

The default is `json` .

This is to indicate whether the Hasura-specific claims are a regular JSON object or a stringified JSON.

This is required because providers like AWS Cognito only allow strings in the JWT claims.[ See #1176 ](https://github.com/hasura/graphql-engine/issues/1176).

Example:

If `claimsFormat` is `json` then the JWT claims should look like:

```
{
   "sub" :   "1234567890" ,
   "name" :   "John Doe" ,
   "admin" :   true ,
   "iat" :   1516239022 ,
   "https://hasura.io/jwt/claims" :   {
     "x-hasura-allowed-roles" :   [ "editor" ,   "user" ,   "mod" ] ,
     "x-hasura-default-role" :   "user" ,
     "x-hasura-user-id" :   "1234567890" ,
     "x-hasura-org-id" :   "123" ,
     "x-hasura-custom" :   "custom-value"
   }
}
```

If `claimsFormat` is `stringified_json` then the JWT claims should look like:

```
{
   "sub" :   "1234567890" ,
   "name" :   "John Doe" ,
   "admin" :   true ,
   "iat" :   1516239022 ,
   "https://hasura.io/jwt/claims" :   "{\"x-hasura-allowed-roles\":[\"editor\",\"user\",\"mod\"],\"x-hasura-default-role\":\"user\",\"x-hasura-user-id\":\"1234567890\",\"x-hasura-org-id\":\"123\",\"x-hasura-custom\":\"custom-value\"}"
}
```

### claimsMap​

This is an optional field. Certain providers might not allow adding custom claims. In such a case, you can map Hasura
session variables with existing JWT claims using `claimsMap` . The `claimsMap` is a JSON object where keys are session
variables and values can be a JSON pointer (with a default value option, when the key specified by the JSON pointer doesn't
exist) or a literal value.

The literal values should be of type `String` , except for the `x-hasura-allowed-roles` claim which expects a string
array.

The value of a claim referred by a JSON path must be a string. To use the JSON path value, the path needs to be given
in a JSON object with `path` as the key and the JSON pointer as the value:

```
{
   "path" :   "/user/all_roles"
}
```

```
{
   "path" :   "/roles/default" ,
   "default" :   "user"
}
```

Claims map precedence

If `claimsMap` is provided in the JWT config, `claimsNamespacePath` and `claimsFormat` will be
ignored.

 **Example: JWT config with JSON path values** 

```
{
   "sub" :   "1234567890" ,
   "name" :   "John Doe" ,
   "admin" :   true ,
   "iat" :   1516239022 ,
   "user" :   {
     "id" :   "ujdh739kd"
   } ,
   "hasura" :   {
     "all_roles" :   [ "user" ,   "editor" ]
   }
}
```

The mapping for `x-hasura-allowed-roles` , `x-hasura-default-role` and `x-hasura-user-id` session variables can be
specified in the `claimsMap` configuration as follows:

```
{
   "type" :   "RS512" ,
   "key" :   "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDdlatRjRjogo3WojgGHFHYLugd\nUWAY9iR3fy4arWNA1KoS8kVw33cJibXr8bvwUAUparCwlvdbH6dvEOfou0/gCFQs\nHUfQrSDv+MuSUMAe8jzKE4qW+jK+xQU9a03GUnKHkkle+Q0pX/g6jXZ7r1/xAK5D\no2kQ+X5xK9cipRgEKwIDAQAB\n-----END PUBLIC KEY-----\n" ,
   "claimsMap" :   {
     "x-hasura-allowed-roles" :   {   "path" :   "/hasura/all_roles"   } ,
     "x-hasura-default-role" :   {   "path" :   "/hasura/all_roles[0]"   } ,
     "x-hasura-user-id" :   {   "path" :   "/user/id"   }
   }
}
```

 **Example: JWT config with JSON path values and default values** 

```
{
   "sub" :   "1234567890" ,
   "name" :   "John Doe" ,
   "admin" :   true ,
   "iat" :   1516239022 ,
   "hasura" :   {
     "all_roles" :   [ "user" ,   "editor" ]
   }
}
```

```
{
   "type" :   "RS512" ,
   "key" :   "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDdlatRjRjogo3WojgGHFHYLugd\nUWAY9iR3fy4arWNA1KoS8kVw33cJibXr8bvwUAUparCwlvdbH6dvEOfou0/gCFQs\nHUfQrSDv+MuSUMAe8jzKE4qW+jK+xQU9a03GUnKHkkle+Q0pX/g6jXZ7r1/xAK5D\no2kQ+X5xK9cipRgEKwIDAQAB\n-----END PUBLIC KEY-----\n" ,
   "claimsMap" :   {
     "x-hasura-allowed-roles" :   {   "path" :   "/hasura/all_roles"   } ,
     "x-hasura-default-role" :   {   "path" :   "/hasura/all_roles[0]"   } ,
     "x-hasura-user-id" :   {   "path" :   "/user/id" ,   "default" :   "ujdh739kd"   }
   }
}
```

In the above case, since the `/user/id` doesn't exist in the JWT token, the default value of the `x-hasura-user-id` i.e
"ujdh739kd" will be used

 **Example: JWT config containing literal values** 

```
{
   "sub" :   "1234567890" ,
   "name" :   "John Doe" ,
   "admin" :   true ,
   "iat" :   1516239022 ,
   "user" :   {
     "id" :   "ujdh739kd"
   }
}
```

The corresponding JWT config should be:

```
{
   "type" :   "RS512" ,
   "key" :   "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDdlatRjRjogo3WojgGHFHYLugd\nUWAY9iR3fy4arWNA1KoS8kVw33cJibXr8bvwUAUparCwlvdbH6dvEOfou0/gCFQs\nHUfQrSDv+MuSUMAe8jzKE4qW+jK+xQU9a03GUnKHkkle+Q0pX/g6jXZ7r1/xAK5D\no2kQ+X5xK9cipRgEKwIDAQAB\n-----END PUBLIC KEY-----\n" ,
   "claimsMap" :   {
     "x-hasura-allowed-roles" :   [ "user" ,   "editor" ] ,
     "x-hasura-default-role" :   "user" ,
     "x-hasura-user-id" :   {   "path" :   "/user/id"   }
   }
}
```

In the above example, the `x-hasura-allowed-roles` and `x-hasura-default-role` values are set in the JWT config and the
value of the `x-hasura-user-id` is a JSON path to the value in the JWT token.

### audience​

This is an optional field. Certain providers might set a claim which indicates the intended audience for the JWT. This
can be checked by setting this field.

When this field is set, during the verification process of the JWT, the `aud` claim in the JWT will be checked to
see whether it is equal to the `audience` field given in the configuration. If they are not equal then the JWT will
be rejected.

See the[ RFC ](https://tools.ietf.org/html/rfc7519#section-4.1.3)for more details.

This field can be a string, or a list of strings.

Examples:

```
{
   "jwkUrl" :   "https://......" ,
   "audience" :   "myapp-1234"
}
```

or

```
{
   "jwkUrl" :   "https://......" ,
   "audience" :   [ "myapp-1234" ,   "myapp-6789" ]
}
```

Audience Security Vulnerability

Certain JWT providers share JWKs between multiple tenants. They use the `aud` claim of the JWT to specify the intended
audience. Setting the `audience` field in the Hasura JWT configuration will make sure that the `aud` claim
from the JWT is also checked during verification. Not doing this check will allow JWTs issued for other tenants to be
valid as well.

In these cases, you **MUST** set the `audience` field to the appropriate value. Failing to do so is a **major security
vulnerability** .

### issuer​

This is an optional field. It takes a string value.

When this field is set, during the verification process of the JWT, the `iss` claim in the JWT will be checked to
see whether it is equal to the `issuer` field given in the configuration. If they are not equal then the JWT will be
rejected.

See[ RFC ](https://tools.ietf.org/html/rfc7519#section-4.1.1)for more details.

Examples:

```
{
   "jwkUrl" :   "https://......" ,
   "issuer" :   "https://my-auth-server.com"
}
```

#### Issuer notes​

- Certain providers require you to verify the `iss` claim on the JWT. To do that you can set this field to the
appropriate value.
- A JWT configuration without an issuer will match any issuer field present in an incoming JWT.
- An incoming JWT without an issuer specified will match a configuration even if it specifies an issuer.


### allowedSkew​

 `allowedSkew` is an optional field to provide some leeway (to account for clock skews) while comparing the JWT expiry
time. This field expects an integer value which will be the number of seconds of the skew value.

### header​

This is an optional field, which indicates which request header to read the JWT from. This field is a stringified JSON
object.

The following are the possible values:

- `{"type": "Authorization"}`
- `{"type": "Cookie", "name": "cookie_name" }`
- `{"type": "CustomHeader", "name": "header_name" }`


Default is `{"type": "Authorization"}` .

In the default mode, Hasura expects an `Authorization` header with a `Bearer` token.

In the cookie mode, Hasura will try to parse the cookie header with the given cookie name. The value of the cookie
should be the exact JWT.

In the custom header mode, Hasura expects a `header_name` header with the exact JWT token value.

Example:

If `header` is `{"type": "Authorization"}` then JWT header should look like:

`Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWI...`

If `header` is `{"type": "Cookie", "name": "cookie_name" }` then JWT header should look like:

`Cookie: cookie_name=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWI...`

If `header` is `{"type": "CustomHeader", "name": "header_name" }` then JWT header should look like:

`header_name: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWI...`

## Hasura JWT Config Examples​

#### HMAC-SHA based​

Your auth server is using HMAC-SHA algorithms to sign JWTs, and is using a 256-bit key. In this case, the JWT config
will look like:

```
{
   "type" :   "HS256" ,
   "key" :   "3EK6FD+o0+c7tzBNVfjpMkNDi2yARAAKzQlk8O2IKoxQu4nF7EdAh8s3TwpHwrdWT6R"
}
```

The `key` is the actual shared secret, which is used by Hasura and the external auth server.

#### RSA based​

If your auth server is using the RSA algorithm to sign JWTs, and is using a 512-bit key, the JWT config only needs to
have the public key.

 **Example 1** : public key in PEM format (not OpenSSH format):

```
{
   "type" :   "RS512" ,
   "key" :   "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDdlatRjRjogo3WojgGHFHYLugd\nUWAY9iR3fy4arWNA1KoS8kVw33cJibXr8bvwUAUparCwlvdbH6dvEOfou0/gCFQs\nHUfQrSDv+MuSUMAe8jzKE4qW+jK+xQU9a03GUnKHkkle+Q0pX/g6jXZ7r1/xAK5D\no2kQ+X5xK9cipRgEKwIDAQAB\n-----END PUBLIC KEY-----\n"
}
```

 **Example 2** : public key as X509 certificate:

```
{
   "type" :   "RS512" ,
   "key" :   "-----BEGIN CERTIFICATE-----\nMIIDHDCCAgSgAwIBAgIINw9gva8BPPIwDQYJKoZIhvcNAQEFBQAwMTEvMC0GA1UE\nAxMmc2VjdXJldG9rZW4uc3lzdGVtLmdzZXJ2aWNlYWNjb3VudC5jb20wHhcNMTgQt7dIsMTIU9k1SUrFviZOGnmHWtIAw\nmtYBcM9I0f9/ka45JIRp5Y1NKpAMFSShs7Wv0m1JS1kXQHdJsPSmjmDKcwnBe3R/\nTU3foRRywR/3AJRM15FNjTqvUm7TeaW16LkkRoECAwEAAaM4MDYwDAYDVR0TAQH/\nBAIwADAOBgNVHQ8BAf8EBAMCB4AwFgYDVR0lAQH/BAwwCgYIKwYBBQUHAwIwDQYJ\nKoZIhvcNAQEFBQADggEBADfY2DEmc2gb8/pqMNWHYq/nTYfJPpK4VA9A0lFTNeoq\nzmnbGwhKj24X+Nw8trsvkrKxHvCI1alDgBaCyzjGGvgOrh8X0wLtymp1yj6PWwee\nR2ZPdUaB62TCzO0iRv7W6o39ey+mU/FyYRtxF0ecxG2a0KNsIyFkciXUAeC5UVDo\nBNp678/SDDx9Ltuxc6h56a/hpBGf9Yzhr0RvYy3DmjBs6eopiGFmjnOKNxQrZ5t2\n339JWR+yiGEAtoHqk/fINMf1An6Rung1xYowrm4guhCIVi5unAvQ89fq0I6mzPg6\nLhTpeP0o+mVYrBmtYVpDpv0e71cfYowSJCCkod/9YbY=\n-----END CERTIFICATE-----"
}
```

 **Example 3** : public key published as JWKs:

```
{
   "jwkUrl" :   "https://www.googleapis.com/service_accounts/v1/jwk/securetoken@system.gserviceaccount.com"
}
```

#### EdDSA based​

If your auth server is using EdDSA to sign JWTs, and is using the Ed25519 variant key, the JWT config only needs to have
the public key.

 **Example 1** : public key in PEM format (not OpenSSH format):

```
{
   "type" :   "Ed25519" ,
   "key" :   "-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAG9I+toAAJicilbPt36tiC4wi7E1Dp9rMmfnwdKyVXi0=\n-----END PUBLIC KEY-----"
}
```

 **Example 2** : public key as X509 certificate:

```
{
   "type" : "Ed25519" ,
   "key" :   "-----BEGIN CERTIFICATE REQUEST-----\nMIIBAzCBtgIBADAnMQswCQYDVQQGEwJERTEYMBYGA1UEAwwPd3d3LmV4YW1wbGUu\nY29tMCowBQYDK2VwAyEA/9DV/InajW02Q0tC/tyr9mCSbSnNP1txICXVJrTGKDSg\nXDBaBgkqhkiG9w0BCQ4xTTBLMAsGA1UdDwQEAwIEMDATBgNVHSUEDDAKBggrBgEF\nBQcDATAnBgNVHREEIDAegg93d3cuZXhhbXBsZS5jb22CC2V4YW1wbGUuY29tMAUG\nAytlcANBAKbTqnTyPcf4ZkVuq2tC108pBGY19VgyoI+PP2wD2KaRz4QAO7Bjd+7S\nljyJoN83UDdtdtgb7aFgb611gx9W4go=\n-----END CERTIFICATE REQUEST-----"
}
```

#### EC based​

If your auth server is using ECDSA to sign JWTs, and is using the ES variant with a 256-bit key, the JWT config only
needs to have the public key.

 **Example 1** : public key in PEM format (not OpenSSH format):

```
{
   "type" :   "ES256" ,
   "key" :   "-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEEVs/o5+uQbTjL3chynL4wXgUg2R9\nq9UU8I5mEovUf86QZ7kOBIjJwqnzD1omageEHWwHdBO6B+dFabmdT9POxg==\n-----END PUBLIC KEY-----"
}
```

 **Example 2** : public key as X509 certificate:

```
{
   "type" :   "ES256" ,
   "key" :   "-----BEGIN CERTIFICATE-----\nMIIBbjCCARWgAwIBAgIUGn02F6Y6s88dDGmIfwiNxWxDjhswCgYIKoZIzj0EAwIw\nDTELMAkGA1UEBhMCSU4wHhcNMjMwNTI0MTAzNTI4WhcNMjgwNTIyMTAzNTI4WjAN\nMQswCQYDVQQGEwJJTjBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABBFbP6OfrkG0\n4y93Icpy+MF4FINkfavVFPCOZhKL1H/OkGe5DgSIycKp8w9aJmoHhB1sB3QTugfn\nRWm5nU/TzsajUzBRMB0GA1UdDgQWBBSaqFjzps1qG+x2DPISjaXTWsTOdDAfBgNV\nHSMEGDAWgBSaqFjzps1qG+x2DPISjaXTWsTOdDAPBgNVHRMBAf8EBTADAQH/MAoG\nCCqGSM49BAMCA0cAMEQCIBDHHWa/uLAVdGFEk82auTmw995+MsRwv52VXLw2Z+ji\nAiAXzOWIcGN8p25uhUN/7v9gEcADGIS4yUiv8gsn/Jk2ow==\n-----END CERTIFICATE-----"
}
```

 **Example 3** : public key published as JWKs:

```
{
   "jwkUrl" :   "https://www.gstatic.com/iap/verify/public_key-jwk"
}
```

## Security considerations​

### Setting audience check​

Certain JWT providers share JWKs between multiple tenants (like Firebase). They use the `aud` claim of JWT to specify
the intended tenant for the JWT. Setting the `audience` field in the Hasura JWT configuration will make sure that the `aud` claim from the JWT is also checked during verification. Not doing this check will allow JWTs issued for other
tenants to be valid as well.

In these cases, you **MUST** set the `audience` field to appropriate value. **Failing to do so is a major security
vulnerability** .

## Popular providers and known issues​

### Firebase​

This page of the Firebase[ docs ](https://firebase.google.com/docs/auth/admin/verify-id-tokens#verify_id_tokens_using_a_third-party_jwt_library)mentions that JWKs are published under:

[ https://www.googleapis.com/robot/v1/metadata/x509/securetoken@system.gserviceaccount.com ](https://www.googleapis.com/robot/v1/metadata/x509/securetoken@system.gserviceaccount.com)

But that is a non-standard format. Firebase also publishes the same certificates as the proper JWK format under:

[ https://www.googleapis.com/service_accounts/v1/jwk/securetoken@system.gserviceaccount.com ](https://www.googleapis.com/service_accounts/v1/jwk/securetoken@system.gserviceaccount.com)

If you are using Firebase and Hasura, use this config:

```
{
   "jwkUrl" :   "https://www.googleapis.com/service_accounts/v1/jwk/securetoken@system.gserviceaccount.com" ,
   "audience" :   "<firebase-project-id>" ,
   "issuer" :   "https://securetoken.google.com/<firebase-project-id>"
}
```

### Auth0​

Refer to the[ Auth0 JWT Integration tutorial ](https://hasura.io/learn/graphql/hasura-authentication/integrations/auth0/)for a detailed guide on integrating Auth0 with Hasura.

Auth0 publishes their JWK under:

 `https://<your-auth0-domain>.auth0.com/.well-known/jwks.json` 

But they have a[ bug where the certificate thumbprint does not match ](https://community.auth0.com/t/certificate-thumbprint-is-longer-than-20-bytes/7794/3).
Hence, currently this URL does not work with Hasura.

Current workaround is - download the X590 certificate from:

 `https://<your-auth0-domain>.auth0.com/pem` 

And use it in the `key` field:

```
{
   "type" : "RS512" ,
   "key" :  "-----BEGIN CERTIFICATE-----
MIIDDTCAfWgAwIBAgIJhNlZ11IDrxbMA0GCSqSIb3DQEBCwUAMCQxIjAgBgNV
BAMTGXlc3QtaGdlLWp3C5ldS5hdXRoMC5jb20HhcNMTgwNzMwMTM1MjM1WhcN
MzIwND3MTM1MjM1WjAkSIwIAYDVQQDExl0ZXNLWhnZS1qd3QuZXUuYXV0aDAu
Y29tMIBIjANBgkqhkiGw0BAQEFAAOCAQ8AMIICgKCAQEA13CivdSkNzRnOnR5
ZNiReD+AgbL7BWjRiw3RwjxRp5PYzvAGuj94yR6LRh3QybYtsMFbSg5J7fNq6
Ld6yMpMrUu8CBOnYY456b/2jlf+Vp8vEQuKvPOOw8Ev6x7X3blcuXCELSwyL3
AGHq9OP2RV6V6CIE863zzuYH5HDLzU35oMZqogJVRJM0+6besH6TnSTNiA7xi
BAqFaiRNQRVi1CAUa0bkN1XRp4AFy7d63VldOsM+8QnCNHySdDr1XevVuq6DK
LQyGexFy4niALgHV0Q7A+xP1c2G6rJomZmn4j1avnlBpU87E58JMrRHOCj+5m
Xj22/QDAQABo0IwQDAPgNVHRMBAf8EBTADAQHMB0GA1UdDgQWBBT6FvNkuUgu
tk3OYQi4lo5aOgwazAOgNVHQ8BAf8EBAMCAoQDQYJKoZIhvcNAQELBQADggEB
ADCLj+L22pEKyqaIUlhUJh7DAiDSLafy0fw56CntzPhqiZVVRlhxeAKidkCLV
r9IEbRuxUoXiQSezPqM //9xHegMp0f2VauVCFg7EpUanYwvqFqjy9LWgH+SBz
4uroLSZ5g1EPsHtlArLChA90caTX4e7Z7Xlu8G2kHRJB5nC7ycdbMUvEWBMeI
tn/pcbmZ3/vlgj4UTEnURe2UPmSJpxmPwXqBcvwdKHRMgFXhZxojWCi0z4ftf
f8t8UJIcbEblnkYe7wzYy8tOXoMMHqGSisCdkp/866029rJsKbwd8rVIyKNC5
frGYaw+0cxO6/WvSir0eA=
-----END CERTIFICATE-----
"
}
```

### Clerk​

Clerk integrates with Hasura GraphQL Engine using JWTs.

Clerk publishes their JWK under: `https://<YOUR_CLERK_FRONTEND_API>/.well-known/jwks.json` 

Refer to the[ Clerk authentication guide ](https://hasura.io/learn/graphql/hasura-authentication/integrations/clerk/)to
set up authenticated requests to Hasura with Clerk.

## Generate a JWT Config for Auth0 or Firebase​

The JWT Config to be used in the metadata can be generated using:[ https://hasura.io/jwt-config ](https://hasura.io/jwt-config).

 **Currently, the UI supports generating config for Auth0 and Firebase** .

The config generated from this page can be directly pasted in yaml files and command line arguments as it takes care of
escaping new lines.

Image: [ Generating JWT config ](https://hasura.io/docs/3.0/assets/images/auth_jwt-config-generated-8d727462247674b10067bc14ca8f9838.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/auth/authentication/jwt/#introduction)
- [ JWT authentication ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-auth-config)
    - [ Example ](https://hasura.io/docs/3.0/auth/authentication/jwt/#example)

- [ All jwt configuration fields ](https://hasura.io/docs/3.0/auth/authentication/jwt/#all-jwt-configuration-fields)

- [ Metadata structure ](https://hasura.io/docs/3.0/auth/authentication/jwt/#metadata-structure)

- [ Example Decoded Payload ](https://hasura.io/docs/3.0/auth/authentication/jwt/#example-decoded-payload)

- [ Example Encoded JWT ](https://hasura.io/docs/3.0/auth/authentication/jwt/#example-encoded-jwt)

- [ Hasura JWT format ](https://hasura.io/docs/3.0/auth/authentication/jwt/#hasura-jwt-format)

- [ Hasura JWT Claim Description ](https://hasura.io/docs/3.0/auth/authentication/jwt/#hasura-jwt-claim-description)

- [ JWT Notes ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-notes)
- [ Hasura JWT configuration options ](https://hasura.io/docs/3.0/auth/authentication/jwt/#hasura-jwt-configuration-options)
    - [ type ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-json-type)

- [ key ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-json-key)

- [ jwkUrl ](https://hasura.io/docs/3.0/auth/authentication/jwt/#jwt-json-jwkUrl)

- [ claimsNamespacePath ](https://hasura.io/docs/3.0/auth/authentication/jwt/#claims-namespace-path)

- [ claimsFormat ](https://hasura.io/docs/3.0/auth/authentication/jwt/#claimsformat)

- [ claimsMap ](https://hasura.io/docs/3.0/auth/authentication/jwt/#claimsmap)

- [ audience ](https://hasura.io/docs/3.0/auth/authentication/jwt/#audience)

- [ issuer ](https://hasura.io/docs/3.0/auth/authentication/jwt/#issuer)

- [ allowedSkew ](https://hasura.io/docs/3.0/auth/authentication/jwt/#allowedskew)

- [ header ](https://hasura.io/docs/3.0/auth/authentication/jwt/#header)
- [ Hasura JWT Config Examples ](https://hasura.io/docs/3.0/auth/authentication/jwt/#hasura-jwt-config-examples)
- [ Security considerations ](https://hasura.io/docs/3.0/auth/authentication/jwt/#security-considerations)
    - [ Setting audience check ](https://hasura.io/docs/3.0/auth/authentication/jwt/#setting-audience-check)
- [ Popular providers and known issues ](https://hasura.io/docs/3.0/auth/authentication/jwt/#popular-providers-and-known-issues)
    - [ Firebase ](https://hasura.io/docs/3.0/auth/authentication/jwt/#firebase)

- [ Auth0 ](https://hasura.io/docs/3.0/auth/authentication/jwt/#auth0-issues)

- [ Clerk ](https://hasura.io/docs/3.0/auth/authentication/jwt/#clerk)
- [ Generate a JWT Config for Auth0 or Firebase ](https://hasura.io/docs/3.0/auth/authentication/jwt/#generating-jwt-config)
