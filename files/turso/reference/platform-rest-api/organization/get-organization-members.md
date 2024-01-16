# Get all organization members

## Summary​

 **Description** :

Returns all of the members of an organization.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.
- The authenticated user must be the owner of the named organization.


The organization is identified by the unique slug string it was assigned during
creation.

 **Analogous CLI command** : `turso org list members` 

 **Path** : `/v1/organizations/:org_slug/members` 

 **Method** : `GET` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `org_slug`  | Slug of the organization from which to get members |


## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `members`  | array | An array of[ organization member objects ](https://docs.turso.tech/reference/platform-rest-api/organization#organization-member-object) |


## Example​

```
curl   \
  -X GET  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations/my-org/members"
```

```
{
   "members" :   [
     {
       "role" :   "owner" ,
       "username" :   "MyGitHubName"
     } ,
     {
       "role" :   "member" ,
       "username" :   "OthersGitHubName"
     }
   ]
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/organization/get-organization-members/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/organization/get-organization-members/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/organization/get-organization-members/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/organization/get-organization-members/#example)


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