# Create Group Token

Create an auth token for a group.

The returned token:

- Can't be retrieved again; there is no record kept of it by Turso
- Can't be revoked individually.


## User Groups​

 `POST /v1/groups/:group/auth/tokens` 

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |


### Query String Parameters​

| Parameter | Required | Description |
|---|---|---|
|  `expiration`  | no | Duration of the token until expiration as parsed by[ go-str2duration ](https://github.com/xhit/go-str2duration), or `never` (default); for example: `1w2d6h3ns` (1 week 2 days 6 hours and 3 nanoseconds) |
|  `authorization`  | no | Level of access granted to the bearer of the token; `read-only` or `full-access` (default) |


### Example​

```
curl   \
  --request POST  \
  --location  'https://api.turso.tech/v1/groups/some_group/auth/tokens?expiration=1d&authorization=read-only'   \
  --header  'Authorization: Bearer TOKEN'
```

```
{
   "jwt" :   "TOKEN"
}
```

## Organization Groups​

 `POST /v1/organizations/:organization/groups/:group/auth/tokens` 

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |


### Path Parameters​

| Parameter | Type | Description |
|---|---|---|
|  `organization`  |  `string`  | The organization name. |


### Query String Parameters​

| Parameter | Required | Description |
|---|---|---|
|  `expiration`  | no | Duration of the token until expiration as parsed by[ go-str2duration ](https://github.com/xhit/go-str2duration), or `never` (default); for example: `1w2d6h3ns` (1 week 2 days 6 hours and 3 nanoseconds) |
|  `authorization`  | no | Level of access granted to the bearer of the token; `read-only` or `full-access` (default) |


### Example​

```
curl   \
  --request POST  \
  --location  'https://api.turso.tech/v1/organizations/some_org/groups/some_group/auth/tokens?expiration=1d&authorization=read-only'   \
  --header  'Authorization: Bearer TOKEN'
```

```
{
   "jwt" :   "TOKEN"
}
```

- [ User Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/mint-token/#user-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/mint-token/#headers)

- [ Query String Parameters ](https://docs.turso.tech//reference/platform-rest-api/groups/mint-token/#query-string-parameters)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/mint-token/#example)
- [ Organization Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/mint-token/#organization-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/mint-token/#headers-1)

- [ Path Parameters ](https://docs.turso.tech//reference/platform-rest-api/groups/mint-token/#path-parameters)

- [ Query String Parameters ](https://docs.turso.tech//reference/platform-rest-api/groups/mint-token/#query-string-parameters-1)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/mint-token/#example-1)


- [ 

Sign Up




 ](https://api.turso.tech/?webui=true&type=signup)
- [ 

Star Our Repo






 ](https://github.com/libsql/libsql)


Sign Up

Star Our Repo

- [ About ](https://turso.tech/about-us)
- [ Investors ](https://turso.tech/investors)
- [ Blog ](https://blog.turso.tech)


- [ Turso Discord ](https://discord.com/invite/4B5D7hYwub)
- [ libSQL Discord ](https://discord.gg/VzbXemj6Rg)
- [ Follow us on Twitter ](https://twitter.com/tursodatabase)
- [ Schedule a Zoom ](https://calendly.com/d/gt7-bfd-83n/meet-with-chiselstrike)


- [ Turso GitHub ](https://github.com/tursodatabase/)
- [ Turso extended GitHub ](https://github.com/turso-extended/)
- [ libSQL GitHub ](http://github.com/tursodatabase/libsql)


- [ Privacy Policy ](https://turso.tech/privacy-policy)
- [ Terms of Use ](https://turso.tech/terms-of-use)


Image: [ Turso logo ](https://docs.turso.tech/img/turso.svg)