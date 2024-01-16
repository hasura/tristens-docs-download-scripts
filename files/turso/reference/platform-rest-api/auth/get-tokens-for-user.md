# Get all Platform API tokens for a user

## Summary​

 **Description** :

Returns a list of all Turso Platform API tokens for the authenticated user. For
security purposes, the list does not contain the actual token values.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.


 **Analogous CLI command** : `turso auth api-tokens list` 

 **Path** : `/v1/auth/api-tokens` 

 **Method** : `GET` 

## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `tokens`  | array | An array of[ Platform API token objects ](https://docs.turso.tech/reference/platform-rest-api/auth#api-token-object)for the user. |


## Example​

```
curl   \
  -X GET  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/auth/api-tokens"
```

```
{
   "tokens" :   [
     {
       "name" :   "token1" ,
       "id" :   "SYzcpe3jEe2We-rqOx4wmQ"
     } ,
     {
       "name" :   "token2" ,
       "id" :   "wPvoKe3qEe2We-rqOx4wmQ"
     }
   ]
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/auth/get-tokens-for-user/#summary)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/auth/get-tokens-for-user/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/auth/get-tokens-for-user/#example)


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