# MS SQL Server: Setting Default Values for Fields

Let's say you want certain fields to have their values set automatically when not explicitly passed. You can do this in
the following ways:

- [ MS SQL Server defaults ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-defaults/): configure default values, using
fixed values or simple SQL functions, for columns in the table definition. E.g. an auto-incrementing `id` , a `created_at` timestamp, etc.
- [ Role based column presets ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-column-presets/): set up presets, using
session variables or fixed values, that are applied when a row is created/updated with a particular[ user role ](https://hasura.io/docs/latest/auth/authorization/roles-variables/). E.g. set a `user_id` field automatically from a session
variable/authorization header.


### What did you think of this doc?

Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)