# Logical database API

## Summary​

The Logical database API allows you to work with Turso[ logical databases ](https://docs.turso.tech/concepts#logical-database)within an organization.

Each database must be contained within an organization. Every GitHub account has
a personal organization with a name based on the GitHub account name. Team
organizations are created and managed with the Turso CLI or the[ Organization
API ](https://docs.turso.tech/reference/platform-rest-api/organization).

After creating a logical database, use the[ Database instance API ](https://docs.turso.tech/reference/platform-rest-api/instance)to add and
remove[ instances ](https://docs.turso.tech/concepts#instance)within that logical database.

## Operations​

All operations require[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication).

- [ Get all logical databases in an organization ](https://docs.turso.tech/reference/platform-rest-api/database/get-databases-in-org)
- [ Create a logical database in an organization ](https://docs.turso.tech/reference/platform-rest-api/database/create-database-in-org)
- [ Destroy a logical database in an organization ](https://docs.turso.tech/reference/platform-rest-api/database/destroy-database-in-org)
- [ Mint an auth token for a logical database in an organization ](https://docs.turso.tech/reference/platform-rest-api/database/mint-token-for-database-in-org)
- [ Invalidate all auth tokens for a logical database in an organization ](https://docs.turso.tech/reference/platform-rest-api/database/invalidate-all-tokens-for-database-in-org)


## Objects​

### Logical database object​

| Property | Type | Description |
|---|---|---|
|  `Name`  | string | Name of the logical database, unique among all databases in an organization |
|  `Hostname`  | string | The DNS hostname used for client connections; used to build libsql and https URLs |
|  `IssuedCertLimit`  | number |  |
|  `IssuedCertCount`  | number |  |
|  `DbId`  | string | UUID of the logical database |
|  `regions`  | string array | List of location codes for all instances of this logical database |
|  `primaryRegion`  | string | Location code for the primary instance |
|  `type`  | string | "logical" |


Any `username` and `password` values associated with a database are deprecated
and should not be used by consumers of this API.

### Logical database usage object​

| Property | Type | Description |
|---|---|---|
|  `uuid`  | string | UUID of the logical database |
|  `instances`  | array | List of[ database instance usage objects ](https://docs.turso.tech//reference/platform-rest-api/database#logical-database-object/#database-instance-usage-object)of instances contributing usage for the current month |


### Database instance usage object​

| Property | Type | Description |
|---|---|---|
|  `uuid`  | string | UUID of the database instance |
|  `usage`  | object | [ Usage object ](https://docs.turso.tech//reference/platform-rest-api/database#logical-database-object/#usage-object)describing the usage of this instance for the current month |


### Usage object​

| Property | Type | Description |
|---|---|---|
|  `rows_read`  | number | The number of row reads incurred during a monthly billing period |
|  `rows_written`  | number | The number of row writes incurred during a monthly billing period |
|  `storage_bytes`  | number | The total amount of storage used |


- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/database#logical-database-object/#summary)
- [ Operations ](https://docs.turso.tech//reference/platform-rest-api/database#logical-database-object/#operations)
- [ Objects ](https://docs.turso.tech//reference/platform-rest-api/database#logical-database-object/#objects)
    - [ Logical database object ](https://docs.turso.tech//reference/platform-rest-api/database#logical-database-object/#logical-database-object)

- [ Logical database usage object ](https://docs.turso.tech//reference/platform-rest-api/database#logical-database-object/#logical-database-usage-object)

- [ Database instance usage object ](https://docs.turso.tech//reference/platform-rest-api/database#logical-database-object/#database-instance-usage-object)

- [ Usage object ](https://docs.turso.tech//reference/platform-rest-api/database#logical-database-object/#usage-object)


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