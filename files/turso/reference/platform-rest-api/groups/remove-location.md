# Remove location from a group

Remove a location from a group for a specific user or organization.

## User Groups​

 `DELETE /v1/groups/:group/locations/:location` 

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |


### Path Parameters​

| Parameter | Type | Description |
|---|---|---|
|  `group`  |  `string`  | The group name. |
|  `location`  |  `string`  | The three letter location code to be removed from the group. |


### Example​

```
curl   \
  --location --request DELETE  'https://api.turso.tech/v1/groups/default/locations/bos'   \
  --header  'Authorization: Bearer TOKEN'
```

```
{
   "group" :   {
     "name" :   "foo" ,
     "locations" :   [ "fra" ,   "lhr" ] ,
     "primary" :   "fra"
   }
}
```

## Organization Groups​

 `DELETE /v1/organizations/:organization/groups/:group/locations/:location` 

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |


### Path Parameters​

| Parameter | Type | Description |
|---|---|---|
|  `organization`  |  `string`  | The organization name. |
|  `group`  |  `string`  | The group name. |
|  `location`  |  `string`  | The three letter location code to be added to the group. |


### Example​

```
curl   \
  --location --request DELETE  'https://api.turso.tech/v1/organizations/some_org/groups/default/locations/bos'   \
  --header  'Authorization: Bearer TOKEN'
```

```
{
   "group" :   {
     "name" :   "default" ,
     "locations" :   [ "fra" ,   "lhr" ,   "bos" ] ,
     "primary" :   "fra"
   }
}
```

- [ User Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/remove-location/#user-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/remove-location/#headers)

- [ Path Parameters ](https://docs.turso.tech//reference/platform-rest-api/groups/remove-location/#path-parameters)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/remove-location/#example)
- [ Organization Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/remove-location/#organization-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/remove-location/#headers-1)

- [ Path Parameters ](https://docs.turso.tech//reference/platform-rest-api/groups/remove-location/#path-parameters-1)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/remove-location/#example-1)


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