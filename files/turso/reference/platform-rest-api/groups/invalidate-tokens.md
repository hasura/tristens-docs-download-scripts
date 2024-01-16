# Invalidate Group Tokens

Invalidate all auth tokens for a group.

## User Groups​

 `POST /v1/groups/:group/auth/rotate` 

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |


### Example​

```
curl   \
  --request POST
  --location  'https://api.turso.tech/v1/groups/some_group/auth/rotate'   \
  --header  'Authorization: Bearer TOKEN'
```

Note: The response body is empty but returns HTTP status `200` for successful rotations.

## Organization Groups​

 `POST /v1/organizations/:organization/groups/:group/auth/rotate` 

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |


### Path Parameters​

| Parameter | Type | Description |
|---|---|---|
|  `organization`  |  `string`  | The organization name. |


### Example​

```
curl   \
  --request POST  \
  --location  'https://api.turso.tech/v1/organizations/some_org/groups/some_group/auth/rotate'   \
  --header  'Authorization: Bearer TOKEN'
```

Note: The response body is empty but returns HTTP status `200` for successful rotations.

- [ User Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/invalidate-tokens/#user-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/invalidate-tokens/#headers)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/invalidate-tokens/#example)
- [ Organization Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/invalidate-tokens/#organization-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/invalidate-tokens/#headers-1)

- [ Path Parameters ](https://docs.turso.tech//reference/platform-rest-api/groups/invalidate-tokens/#path-parameters)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/invalidate-tokens/#example-1)


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