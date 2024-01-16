# Validate a token for a user

## Summary​

 **Description** :

Validates a platform token.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.


 **Path** : `/v1/auth/validate` 

 **Method** : `GET` 

## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `exp`  | number | The time of expiration for the provided token in unix epoch seconds, or -1 if there is no expiration |


## Example​

```
curl   \
  -X GET  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/auth/validate"
```

```
{
   "exp" :   999
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/auth/validate-token-for-user/#summary)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/auth/validate-token-for-user/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/auth/validate-token-for-user/#example)


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