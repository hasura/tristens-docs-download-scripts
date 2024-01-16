# Create Group

Create a group for a specific user or organization.

## User Groups​

 `POST /v1/groups` 

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |
|  `Content-Type`  |  `application/json`  | The data sent must be JSON. |


### Request Body​

| Field | Type | Description |
|---|---|---|
|  `name`  |  `string`  | The group name. |
|  `location`  |  `[location]`  | A valid supported location name. |


### Example​

```
curl   \
  --location  'https://api.turso.tech/v1/groups'   \
  --header  'Authorization: Bearer TOKEN'   \
  --header  'Content-Type: application/json'   \
  --data  '{
      "name": "group2",
      "location": "lhr"
  }'
```

```
{
   "group" :   {
     "locations" :   [ "lhr" ] ,
     "name" :   "group2" ,
     "primary" :   "lhr"
   }
}
```

## Organization Groups​

 `POST /v1/organizations/:organization/groups` 

### Headers​

| Header | Example | Description |
|---|---|---|
|  `Authorization`  |  `Bearer TOKEN`  | The platform or user auth `TOKEN` . |
|  `Content-Type`  |  `application/json`  | The data sent must be JSON. |


### Path Parameters​

| Parameter | Type | Description |
|---|---|---|
|  `organization`  |  `string`  | The organization name. |


### Request Body​

| Field | Type | Description |
|---|---|---|
|  `name`  |  `string`  | The group name. |
|  `location`  |  `[location]`  | A valid supported location name. |


### Example​

```
curl   \
  --location  'https://api.turso.tech/v1/organizations/some_org/groups'   \
  --header  'Authorization: Bearer TOKEN'   \
  --header  'Content-Type: application/json'   \
  --data  '{
      "name": "group2",
      "location": "lhr"
  }'
```

```
{
   "group" :   {
     "locations" :   [ "lhr" ] ,
     "name" :   "group2" ,
     "primary" :   "lhr"
   }
}
```

- [ User Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/create-group/#user-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/create-group/#headers)

- [ Request Body ](https://docs.turso.tech//reference/platform-rest-api/groups/create-group/#request-body)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/create-group/#example)
- [ Organization Groups ](https://docs.turso.tech//reference/platform-rest-api/groups/create-group/#organization-groups)
    - [ Headers ](https://docs.turso.tech//reference/platform-rest-api/groups/create-group/#headers-1)

- [ Path Parameters ](https://docs.turso.tech//reference/platform-rest-api/groups/create-group/#path-parameters)

- [ Request Body ](https://docs.turso.tech//reference/platform-rest-api/groups/create-group/#request-body-1)

- [ Example ](https://docs.turso.tech//reference/platform-rest-api/groups/create-group/#example-1)


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