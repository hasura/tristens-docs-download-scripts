# Remove Hasura Data from a Database

Hasura saves two schemas in the database that you have designated to store metadata: `hdb_catalog` and `hdb_views` .
These schemas store metadata and track the state of your database.

If you want to remove Hasura from this database, you can use the following commands to drop these schemas using
either a database-management tool or the SQL editor - accessible in the sidebar of any table in the Hasura Console:

```
drop   schema  hdb_views  cascade ;
drop   schema  hdb_catalog  cascade ;
```

Designated metadata database

Note that the database used to store metadata is designated with the[ HASURA_GRAPHQL_METADATA_DATABASE_URL environment variable or --metadata-database-url startup flag ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#metadata-database-url).
If this is not set, the metadata database will be the same as the database used for data.

### What did you think of this doc?

Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)