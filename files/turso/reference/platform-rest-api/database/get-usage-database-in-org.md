# Get the current month's usage for a logical database in an organization

## Summary​

 **Description** :

Returns usage statistics for the current calendar month that are used for
purpose of billing and monthly limits.

Usage is reported per individual database instance. Any instance that
contributed to the usage for the calendar month is present in the output, even
if that instance was deleted.

To get more information about each instance, given their IDs in the output, make
another request to[ get the logical database ](https://docs.turso.tech/reference/platform-rest-api/database/get-database-in-org).

To learn more about how usage is measured, read the[ technical billing
documentation ](https://docs.turso.tech/billing-details).

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.
- The authenticated user must be a member of the named organization.
- The named logical database must already exist in the named organization.


The organization is identified by the unique slug string it was assigned during
creation.

 **Analogous CLI command** : `turso db inspect [db_name]` 

 **Path** : `/v1/organizations/:org_slug/databases/:db_name/usage` 

 **Method** : `GET` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `org_slug`  | Slug of the organization containing the databases |
|  `db_name`  | Name of the logical database to get |


## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `database`  | object | A[ logical database usage object ](https://docs.turso.tech/reference/platform-rest-api/database#logical-database-usage-object) |
|  `instances`  | object | Deprecated - do not use |
|  `total`  | object | Deprecated - do not use |


## Example​

```
curl   \
  -X GET  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations/my-org/databases/my-db/usage"
```

```
{
   "database" :   {
     "uuid" :   "0c3b1c40-04a5-11ee-897e-ea9ebfc69781" ,
     "instances" :   [
       {
         "uuid" :   "0d2a4482-04a5-11ee-897e-ea9ebfc69781" ,
         "usage" :   {
           "rows_read" :   11 ,
           "rows_written" :   1 ,
           "storage_bytes" :   28672
         }
       } ,
       {
         "uuid" :   "b1d366e4-08ad-11ee-b472-02aae2e52fd2" ,
         "usage" :   {
           "rows_read" :   0 ,
           "rows_written" :   0 ,
           "storage_bytes" :   20480
         }
       }
     ] ,
     "usage" :   {
       "rows_read" :   11 ,
       "rows_written" :   1 ,
       "storage_bytes" :   53248
     }
   }
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/database/get-usage-database-in-org/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/database/get-usage-database-in-org/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/database/get-usage-database-in-org/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/database/get-usage-database-in-org/#example)


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