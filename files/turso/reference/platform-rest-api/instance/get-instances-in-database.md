# Get all instances in a logical database

## Summary​

 **Description** :

Returns all instances in a logical database in an organization.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.
- The authenticated user must be a member of the named organization.
- The named logical database must already exist in the named organization.


The organization is identified by the unique slug string it was assigned during
creation. The logical database is identified by the name it was given at
creation.

 **Analogous CLI command** : `turso db show [db_name]` 

 **Path** : `/v1/organizations/:org_slug/databases/:db_name/instances` 

 **Method** : `GET` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `org_slug`  | Slug of the organization containing the logical database |
|  `db_name`  | Name of the logical database containing the instances |


## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `instances`  | array | An array of[ database instance objects ](https://docs.turso.tech/reference/platform-rest-api/instance#database-instance-object)with all instances. |


## Example​

```
curl   \
  -X GET  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations/my-org/databases/my-db/instances"
```

```
{
   "instances" :   [
     {
       "uuid" :   "424a1738-cef9-11ed-b40d-c68341370672" ,
       "name" :   "my-instance" ,
       "type" :   "primary" ,
       "region" :   "ord" ,
       "hostname" :   "e784ee57c52d83-my-db-my-org.turso.io"
     } ,
     {
       "uuid" :   "cc93f685-1785-11ee-8e67-ee1bce83c37e" ,
       "name" :   "my-replica" ,
       "type" :   "replica" ,
       "region" :   "phx" ,
       "hostname" :   "17811114a90e89-my-db-my-org.turso.io"
     }
   ]
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/instance/get-instances-in-database/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/instance/get-instances-in-database/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/instance/get-instances-in-database/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/instance/get-instances-in-database/#example)


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