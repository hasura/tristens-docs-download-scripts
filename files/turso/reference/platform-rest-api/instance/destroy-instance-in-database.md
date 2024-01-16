# Destroy an instance in a logical database

## Summary​

 **Description** :

Destroys an instance in a logical database in an organization.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.
- The authenticated user must be a member of the named organization.
- The named logical database must already exist in the named organization.
- The named instance must already exist in the named database.


The organization is identified by the unique slug string it was assigned during
creation. The logical database is identified by the name it was given at
creation. The instance is identified by the name it was assigned by the API at
the time it was created.

 **Analogous CLI command** : `turso db destroy [db_name] --instance [instance_name]` 

info

The CLI allows you to destroy instances by their location with the command `turso db destroy [db_name] --location [location_code]` , but the API does not
offer this function directly. The implementation of the CLI first[ gets a list
of database instances ](https://docs.turso.tech/reference/platform-rest-api/instance/get-instances-in-database), then destroys the individual instances that match the
provided location code.

 **Path** : `/v1/organizations/:org_slug/databases/:db_name/instances/:instance_name` 

 **Method** : `DELETE` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `org_slug`  | Slug of the organization containing the logical database |
|  `db_name`  | Name of the logical database containing the instance |
|  `instance_name`  | Name of the database instance to destroy |


## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `instance`  | string | The name of the destroyed instance |


## Example​

```
curl   \
  -X POST  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations/my-org/databases/my-db/instances/my-instance"
```

```
{
   "instance" :   "my-instance"
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/instance/destroy-instance-in-database/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/instance/destroy-instance-in-database/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/instance/destroy-instance-in-database/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/instance/destroy-instance-in-database/#example)


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