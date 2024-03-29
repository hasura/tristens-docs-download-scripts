# Get all logical databases in an organization

## Summary​

 **Description** :

Returns a list of all logical databases in an organization.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.
- The authenticated user must be a member of the named organization.


The organization is identified by the unique slug string it was assigned during
creation.

 **Analogous CLI command** : `turso db list` 

 **Path** : `/v1/organizations/:org_slug/databases` 

 **Method** : `GET` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `org_slug`  | Slug of the organization containing the databases |


## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `databases`  | array | An array of[ logical database objects ](https://docs.turso.tech/reference/platform-rest-api/database#logical-database-object)with all databases. |


## Example​

```
curl   \
  -X GET  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations/my-org/databases"
```

```
{
   "databases" :   [
     {
       "Name" :   "my-db" ,
       "Hostname" :   "my-db-my-org.turso.io" ,
       "IssuedCertLimit" :   0 ,
       "IssuedCertCount" :   0 ,
       "DbId" :   "416756c4-cef9-11ed-b40d-c68341370672" ,
       "regions" :   [
         "ord"
       ] ,
       "primaryRegion" :   "ord" ,
       "type" :   "logical"
     } ,
     {
       "Name" :   "t" ,
       "Hostname" :   "t-my-org.turso.io" ,
       "IssuedCertLimit" :   0 ,
       "IssuedCertCount" :   0 ,
       "DbId" :   "e4a94d21-e2aa-11ed-bb4f-2ae75da7784d" ,
       "regions" :   [
         "ord"
       ] ,
       "primaryRegion" :   "ord" ,
       "type" :   "logical"
     }
   ]
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/database/get-databases-in-org/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/database/get-databases-in-org/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/database/get-databases-in-org/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/database/get-databases-in-org/#example)


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