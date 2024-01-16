# Mint an auth token for a logical database in an organization

## Summary​

 **Description** :

Mints an[ auth token for client access ](https://docs.turso.tech/reference/turso-cli#database-client-authentication-tokens)to a logical database in an
organization.

The returned token:

- Can't be retrieved again; there is no record kept of it by Turso
- Can't be revoked individually.


All previously minted tokens can be[ invalidated ](https://docs.turso.tech/reference/platform-rest-api/database/invalidate-all-tokens-for-database-in-org).

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.
- The authenticated user must be a member of the named organization.


The organization is identified by the unique slug string it was assigned during
creation.

 **Analogous CLI command** : `turso db tokens create [db_name]` 

 **Path** : `/v1/organizations/:org_slug/databases/:db_name/auth/tokens` 

 **Method** : `POST` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `org_slug`  | Slug of the organization containing the database |
|  `db_name`  | Name of the logical database |


 **Query string parameters** :

| Parameter | Required | Description |
|---|---|---|
|  `expiration`  | no | Duration of the token until expiration as parsed by[ go-str2duration ](https://github.com/xhit/go-str2duration), or `never` (default); for example: "1w2d6h3ns" (1 week 2 days 6 hours and 3 nanoseconds) |
|  `authorization`  | no | Level of access granted to the bearer of the token; `read-only` or `full-access` (default) |


## Output​

 **JSON body properties** :

| Property | Type | Description |
|---|---|---|
|  `jwt`  | string | An auth token with the requested access to the logical database |


## Example​

```
curl   \
  -X POST  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations/my-org/databases/my-db/auth/tokens?expiration=1d&authorization=read-only"
```

```
{
   "jwt" :   "AUTH-TOKEN-STRING"
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/database/mint-token-for-database-in-org/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/database/mint-token-for-database-in-org/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/database/mint-token-for-database-in-org/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/database/mint-token-for-database-in-org/#example)


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