# Retrieve Group

Returns a single group and its locations by name for a specific user or organization.

## User Groups​

 `GET /v1/groups/:group` 

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Accept`  |  `application/json`  | The data requested should be JSON. |
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |


### Path Parameters​

| Parameter | Type | Description |
|---|---|---|
|  `group`  |  `string`  | The group name. |


### Example​

```
curl   \
  --location  'https://api.turso.tech/v1/groups/default'   \
  --header  'Authorization: Bearer TOKEN'
```

```
{
   "group" :   {
     "name" :   "default" ,
     "locations" :   [ "fra" ] ,
     "primary" :   "fra"
   }
}
```

## Organization Groups​

 `GET /v1/organizations/:organization/groups/:group` 

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Accept`  |  `application/json`  | The data requested should be JSON. |
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |


### Path Parameters​

| Parameter | Type | Description |
|---|---|---|
|  `organization`  |  `string`  | The organization name. |
|  `group`  |  `string`  | The group name. |


### Example​

```
curl   \
  --location --request POST  'https://api.turso.tech/v1/organizations/some_org/groups/default'   \
  --header  'Authorization: Bearer TOKEN'
```

```
{
   "group" :   {
     "name" :   "default" ,
     "locations" :   [ "fra" ] ,
     "primary" :   "fra"
   }
}
```

- [ User Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/retrieve-group/#user-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/retrieve-group/#headers)

- [ Path Parameters ](https://docs.turso.tech//reference/platform-rest-api/groups/retrieve-group/#path-parameters)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/retrieve-group/#example)
- [ Organization Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/retrieve-group/#organization-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/retrieve-group/#headers-1)

- [ Path Parameters ](https://docs.turso.tech//reference/platform-rest-api/groups/retrieve-group/#path-parameters-1)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/retrieve-group/#example-1)


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