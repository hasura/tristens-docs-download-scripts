# Get all organizations for the user

## Summary​

 **Description** :

Returns all organizations for which the authenticated user is a member.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.


 **Analogous CLI command** : `turso org list` 

 **Path** : `/v1/organizations` 

 **Method** : `GET` 

## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `organizations`  | array | An array of[ organization objects ](https://docs.turso.tech/reference/platform-rest-api/organization#organization-object) |


## Example​

```
curl   \
  -X GET  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations"
```

```
{
   "organizations" :   [
     {
       "name" :   "personal" ,
       "slug" :   "your-username" ,
       "type" :   "personal"
     } ,
     {
       "name" :   "my-org" ,
       "slug" :   "my-org" ,
       "type" :   "team"
     }
   ]
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/organization/get-organizations-for-user/#summary)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/organization/get-organizations-for-user/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/organization/get-organizations-for-user/#example)


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