# Get all supported locations

## Summary​

 **Description** :

Returns all supported database instance deployment locations.

The three letter codes in the response can be used wherever a "location code" is
accepted by the[ Database instance API ](https://docs.turso.tech/reference/platform-rest-api/instance).

 **Requirements** :

- The caller must provide an[ authentication ](https://docs.turso.tech/reference/platform-rest-api/#authentication)token.


 **Analogous CLI command** : `turso db locations` 

info

The Turso CLI suggests a default location near the user, which is not part of
this API. The CLI uses[ https://region.turso.io/ ](https://region.turso.io/)to get the most most suitable
default.

 **Path** : `/v1/locations` 

 **Method** : `GET` 

## Output​

 **JSON body properties** :

| Property | Description |
|---|---|
|  `locations`  | An object whose properties are locations codes and values are display names of those locations |


## Example​

```
curl   \
  -X GET  \
  -H  "Authorization: Bearer  $TURSO_TOKEN "   \
   " $TURSO_BASE_URL /v1/locations"
```

```
{
   "locations" :   {
     "ams" :   "Amsterdam, Netherlands" ,
     "arn" :   "Stockholm, Sweden" ,
     "bog" :   "Bogotá, Colombia" ,
     "bos" :   "Boston, Massachusetts (US)" ,
     "cdg" :   "Paris, France" ,
     "den" :   "Denver, Colorado (US)" ,
     "dfw" :   "Dallas, Texas (US)" ,
     "ewr" :   "Secaucus, NJ (US)" ,
     "fra" :   "Frankfurt, Germany" ,
     "gdl" :   "Guadalajara, Mexico" ,
     "gig" :   "Rio de Janeiro, Brazil" ,
     "gru" :   "São Paulo, Brazil" ,
     "hkg" :   "Hong Kong, Hong Kong" ,
     "iad" :   "Ashburn, Virginia (US)" ,
     "jnb" :   "Johannesburg, South Africa" ,
     "lax" :   "Los Angeles, California (US)" ,
     "lhr" :   "London, United Kingdom" ,
     "mad" :   "Madrid, Spain" ,
     "mia" :   "Miami, Florida (US)" ,
     "nrt" :   "Tokyo, Japan" ,
     "ord" :   "Chicago, Illinois (US)" ,
     "otp" :   "Bucharest, Romania" ,
     "qro" :   "Querétaro, Mexico" ,
     "scl" :   "Santiago, Chile" ,
     "sea" :   "Seattle, Washington (US)" ,
     "sin" :   "Singapore, Singapore" ,
     "sjc" :   "San Jose, California (US)" ,
     "syd" :   "Sydney, Australia" ,
     "waw" :   "Warsaw, Poland" ,
     "yul" :   "Montreal, Canada" ,
     "yyz" :   "Toronto, Canada"
   }
}
```

- [ Summary ](https://docs.turso.tech//reference/platform-rest-api/location/get-locations#example/#summary)
- [ Output ](https://docs.turso.tech//reference/platform-rest-api/location/get-locations#example/#output)
- [ Example ](https://docs.turso.tech//reference/platform-rest-api/location/get-locations#example/#example)


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