# Update the version of all instances of a logical database in an organization

## Summary​

 **Description** :

Updates the version of libSQL server of all instances of a logical database in
an organization. This operation causes some amount of downtime to occur during
the update process. The version of libSQL server is taken from the latest built
docker image.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.
- The authenticated user must be a member of the named organization.
- The named logical database must already exist in the named organization.


The organization is identified by the unique slug string it was assigned during
creation. The logical database is identified by the name it was given at
creation.

 **Analogous CLI command** : `turso db update [db_name]` 

 **Path** : `/v1/organizations/:org_slug/databases/:db_name/update` 

 **Method** : `POST` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `org_slug`  | Slug of the organization containing the database |
|  `db_name`  | Name of the logical database whose instance to update |


## Output​

None. The API sends an empty response with HTTP status 200 when the
update is complete.

## Example​

```
curl   \
  -X POST  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations/my-org/databases/my-db/update"
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/database/update-database-in-org/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/database/update-database-in-org/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/database/update-database-in-org/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/database/update-database-in-org/#example)


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