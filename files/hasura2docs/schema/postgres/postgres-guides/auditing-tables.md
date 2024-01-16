# Auditing Actions on Tables in Postgres

Typically audit logging is added to some tables to comply with various certifications. You may want to capture
the user information (role and the session variables) for every change in Postgres that is done through the GraphQL
engine.

For every mutation, Hasura roughly executes the following transaction:

```
BEGIN ;
SET   local   "hasura.user"   =   '{"x-hasura-role": "role", ... various session variables}'
SQL  related  to  the mutation
COMMIT ;
```

This information can therefore be captured in any trigger on the underlying tables by using the `current_setting` function as follows:

`current_setting ( 'hasura.user' ) ;`

We've set up some utility functions that'll let you quickly get started with auditing in this[ repo ](https://github.com/hasura/audit-trigger).

### What did you think of this doc?

Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)