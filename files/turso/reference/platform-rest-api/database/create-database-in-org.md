# Create a logical database in an organization

## Summary​

 **Description** :

Creates a logical database in an organization. Returns a[ logical database
object ](https://docs.turso.tech/reference/platform-rest-api/database#logical-database-object)that describes the newly created database.

The result of this operation is an empty logical database with no instances. The
database is not useful until an instance is created with the[ Database instance
API ](https://docs.turso.tech/reference/platform-rest-api/instance/). The first created instance becomes the primary for the logical database.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.
- The authenticated user must be a member of the named organization.


The organization is identified by the unique slug string it was assigned during
creation.

 **Analogous CLI command** : `turso db create [db_name]` 

info

 `turso db create` automatically creates the primary instance using the closest
(or specified location) after creating the logical database. This function is
not provided by the API, and you must use the[ Database instance API ](https://docs.turso.tech/reference/platform-rest-api/instance/)to create
the first instance yourself in the location you specify.

info

 `turso db create` with no arguments creates a database with a random name, but
the API does not offer this function. The CLI is randomly generating the name
itself and passing that to the API in the request body using the `name` property.

 **Path** : `/v1/organizations/:org_slug/databases` 

 **Method** : `POST` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `org_slug`  | Slug of the organization to contain the database |


 **JSON body properties** :

| Property | Required | Description |
|---|---|---|
|  `name`  | yes | Slug of the logical database to create; must be unique among all of the user's databases |
|  `image`  | no | Type of database image to use; `latest` (default) or `canary`  |
|  `group`  | no | The name of the group to add this database to. Defaults to `default`  |


## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `database`  | object | A[ logical database object ](https://docs.turso.tech/reference/platform-rest-api/database#logical-database-object)describing the newly created database. |


## Example​

```
curl   \
  -X POST  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations/my-org/databases"   \
  -d  '{"name": "my-db", "image": "latest"}'
```

```
{
   "database" :   {
     "Name" :   "my-db" ,
     "Hostname" :   "my-db-my-org.turso.io" ,
     "IssuedCertLimit" :   0 ,
     "IssuedCertCount" :   0 ,
     "DbId" :   "444f7e33-ea1d-11ed-afb4-d228a44fc89f"
   } ,
   "password" :   "[password]" ,
   "username" :   "[username]"
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/database/create-database-in-org/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/database/create-database-in-org/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/database/create-database-in-org/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/database/create-database-in-org/#example)


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