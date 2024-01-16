# Revoke a Platform API token for a user

## Summary​

 **Description** :

Revokes (deletes) a Platform API token of the given name for the authenticated
user.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.


 **Analogous CLI command** : `turso auth api-tokens revoke [token_name]` 

 **Path** : `/v1/auth/api-tokens/:token_name` 

 **Method** : `DELETE` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `token_name`  | Name of the token to revoke |


## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `token`  | string | The name of the token that was revoked |


## Example​

```
curl   \
  -X DELETE  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/auth/api-tokens/my-token"
```

```
{
   "token" :   "my-token"
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/auth/revoke-token-for-user/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/auth/revoke-token-for-user/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/auth/revoke-token-for-user/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/auth/revoke-token-for-user/#example)


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