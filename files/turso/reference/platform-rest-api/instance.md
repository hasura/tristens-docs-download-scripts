# Database instance API

## Summary​

The Database instance API allows you to work with Turso database[ instances ](https://docs.turso.tech/concepts#instance).

Before using this API, you must already have a[ logical database ](https://docs.turso.tech/concepts#logical-database)created by the[ Turso CLI ](https://docs.turso.tech/reference/turso-cli)or the[ Logical database API ](https://docs.turso.tech/reference/platform-rest-api/database)

## Operations​

All operations require[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication).

- [ Get all instances in a logical database ](https://docs.turso.tech/reference/platform-rest-api/instance/get-instances-in-database)
- [ Create an instance in a logical database ](https://docs.turso.tech/reference/platform-rest-api/instance/create-instance-in-database)
- [ Destroy an instance in a logical database ](https://docs.turso.tech/reference/platform-rest-api/instance/destroy-instance-in-database)
- [ Wait for an instance to become ready in a logical database ](https://docs.turso.tech/reference/platform-rest-api/instance/wait-instance-ready-in-database)


## Objects​

### Database instance object​

| Property | Type | Description |
|---|---|---|
|  `uuid`  | string | UUID, unique among all instances |
|  `name`  | string | Given name (human readable) |
|  `type`  | string | "primary" or "replica" |
|  `region`  | string | Location code |
|  `hostname`  | string | The DNS hostname used for client connections; used to build libsql and https URLs |


- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/instance/#summary)
- [ Operations ](https://docs.turso.tech//reference/platform-rest-api/instance/#operations)
- [ Objects ](https://docs.turso.tech//reference/platform-rest-api/instance/#objects)
    - [ Database instance object ](https://docs.turso.tech//reference/platform-rest-api/instance/#database-instance-object)


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