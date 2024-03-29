# Mint a Platform API token for a user

## Summary​

 **Description** :

Mints (creates) a new Platform API token for the authenticated user. Returns a[ Platform API token object ](https://docs.turso.tech/reference/platform-rest-api/auth#platform-api-token-object)that describes the newly created token.

caution

The response of this call contains the token value to use in future API calls.
Once you receive this value, save it somewhere secure. For security reasons, the
Authentication API will not give back the token value when[ listing tokens for
the user ](https://docs.turso.tech/reference/platform-rest-api/auth/get-tokens-for-user).

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.


 **Analogous CLI command** : `turso auth api-tokens mint [token_name]` 

 **Path** : `/v1/auth/api-tokens/:token_name` 

 **Method** : `POST` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `token_name`  | Name of the token to mint; must be unique among all tokens for the user |


## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `token`  | object | A[ Platform API token object ](https://docs.turso.tech/reference/platform-rest-api/auth#platform-api-token-object)describing the newly created token. |


## Example​

```
curl   \
  -X POST  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/auth/api-tokens/my-token"
```

```
{
   "id" :   "6FnEr-6fEe2rsyLfpvsWuA" ,
   "name" :   "my-token" ,
   "token" :   "token-value"
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/auth/mint-token-for-user/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/auth/mint-token-for-user/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/auth/mint-token-for-user/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/auth/mint-token-for-user/#example)


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