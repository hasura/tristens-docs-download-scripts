# Wait for an instance to become ready in a logical database

## Summary​

 **Description** :

Waits for an instance to be able to receive a query. Typically invoked
immediately after an instance is created to know when it's ready for use.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.
- The authenticated user must be a member of the named organization.
- The named logical database must already exist in the named organization.


The organization is identified by the unique slug string it was assigned during
creation. The logical database is identified by the name it was given at
creation. The instance is identified by the name it was assigned by the API at
the time it was created.

 **Path** : `/v1/organizations/:org_slug/databases/:db_name/instances/:instance_name/wait` 

 **Method** : `GET` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `org_slug`  | Slug of the organization containing the logical database |
|  `db_name`  | Name of the logical database containing the instance |
|  `instance_name`  | Name of the database instance to wait for |


## Output​

None. The API sends an empty response with HTTP status 200 when the instance is
ready to receive queries.

## Example​

```
curl   \
  -X GET  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations/my-org/databases/my-db/instances/my-instance/wait"
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/instance/wait-instance-ready-in-database/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/instance/wait-instance-ready-in-database/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/instance/wait-instance-ready-in-database/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/instance/wait-instance-ready-in-database/#example)


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