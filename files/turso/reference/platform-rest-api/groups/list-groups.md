# List Groups

Returns a list of groups and the assigned locations.

## User Groups​

 `GET /v1/groups` 

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Accept`  |  `application/json`  | The data requested should be JSON. |
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |


### Example​

```
curl   \
  --location  'https://api.turso.tech/v1/groups'   \
  --header  'Authorization: Bearer TOKEN'
```

```
{
   "groups" :   [
     {
       "locations" :   [ "bos" ,   "lhr" ] ,
       "name" :   "default" ,
       "primary" :   "lhr"
     }
   ]
}
```

## Organization Groups​

 `GET /v1/organizations/:organization/groups` 

This endpoint retrieves groups that are specific to an organization.

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Accept`  |  `application/json`  | The data requested should be JSON. |
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |


### Path Parameters​

| Header | Type | Description |
|---|---|---|
|  `organization`  |  `string`  | The organization name. |


### Example​

```
curl   \
  --location  'https://api.turso.tech/v1/organizations/some_org/groups'   \
  --header  'Authorization: Bearer TOKEN'
```

```
{
   "groups" :   [
     {
       "locations" :   [ "lhr" ] ,
       "name" :   "default" ,
       "primary" :   "lhr"
     }
   ]
}
```

- [ User Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/list-groups/#user-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/list-groups/#headers)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/list-groups/#example)
- [ Organization Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/list-groups/#organization-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/list-groups/#headers-1)

- [ Path Parameters ](https://docs.turso.tech//reference/platform-rest-api/groups/list-groups/#path-parameters)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/list-groups/#example-1)


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