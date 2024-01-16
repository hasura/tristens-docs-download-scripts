# Invalidate all auth tokens for a logical database in an organization

## Summary​

 **Description** :

Invalidates all[ auth tokens ](https://docs.turso.tech/reference/turso-cli#database-client-authentication-tokens)previously[ minted ](https://docs.turso.tech/reference/platform-rest-api/database/mint-token-for-database-in-org)for a logical database in an
organization. This is achieved by randomly changing the signing key for the
database so that tokens signed with the prior key are no longer valid.

caution

This operation cannot be reverted. A short downtime is required to complete the
changes.

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.
- The authenticated user must be a member of the named organization.


The organization is identified by the unique slug string it was assigned during
creation.

 **Analogous CLI command** : `turso db tokens invalidate [db_name]` 

 **Path** : `/v1/organizations/:org_slug/databases/:db_name/auth/rotate` 

 **Method** : `POST` 

## Inputs​

 **Path parameters** :

| Parameter | Description |
|---|---|
|  `org_slug`  | Slug of the organization containing the database |
|  `db_name`  | Name of the logical database |


## Output​

None.

## Example​

```
curl   \
  -X POST  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/organizations/my-org/databases/my-db/auth/rotate"
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/database/invalidate-all-tokens-for-database-in-org/#summary)
- [ Inputs ](https://docs.turso.tech//reference/platform-rest-api/database/invalidate-all-tokens-for-database-in-org/#inputs)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/database/invalidate-all-tokens-for-database-in-org/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/database/invalidate-all-tokens-for-database-in-org/#example)


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