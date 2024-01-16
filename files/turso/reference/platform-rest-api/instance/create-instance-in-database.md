# Create an instance in a logical database

## Summary​

 **Description** :

Creates an instance in a logical database in an organization.

The first instance created becomes the primary instance for that database and
can't be destroyed later.

Each instance must be provisioned in a location identified with a location code.
Get a list of location codes using the[ Location API ](https://docs.turso.tech/reference/platform-rest-api/location).

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.
- The authenticated user must be a member of the named organization.
- The named logical database must already exist in the named organization.


The organization is identified by the unique slug string it was assigned during
creation.  The logical database is identified by the name it was given at
creation.

 **Analogous CLI command** : `turso db replicate [db_name] [location]` 

 **Path** : `/v1/organizations/:org_slug/databases/:db_name/instances` 

 **Method** : `POST` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `org_slug`  | Slug of the organization containing the logical database |
|  `db_name`  | Name of the logical database to contain the new instance |


 **JSON body properties** :

| Property | Required | Description |
|---|---|---|
|  `location`  | yes | The location code for the location of the instance |
|  `image`  | no | Type of database image to use; `latest` (default) or `canary`  |


## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `instance`  | object | A[ database instance object ](https://docs.turso.tech/reference/platform-rest-api/instance#database-instance-object)that describes the newly created instance. |


## Example​

```
curl   \
  -X POST  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations/my-org/databases/my-db/instances"   \
  -d  '{"location": "ord", "image": "latest"}'
```

```
{
   "instance" :   {
     "uuid" :   "a3446118-ea9d-11ed-a213-a2c7dbd646dc" ,
     "name" :   "my-instance" ,
     "type" :   "primary" ,
     "region" :   "sjc" ,
     "hostname" :   "3287469dae4185-my-db-my-org.turso.io"
   } ,
   "password" :   "[password]" ,
   "username" :   "[username]"
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/instance/create-instance-in-database/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/instance/create-instance-in-database/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/instance/create-instance-in-database/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/instance/create-instance-in-database/#example)


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