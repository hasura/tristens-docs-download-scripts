# Postgres Requirements

## Supported Postgres versions​

Hasura GraphQL Engine supports all supported versions of Postgres per the[ public documentation ](https://www.postgresql.org/support/versioning/).

## Postgres permissions​

If you're running in a controlled environment, you might need to configure the Hasura GraphQL Engine to use a specific
Postgres user that your DBA gives you.

The Hasura GraphQL Engine needs access to your Postgres database(s) with the following permissions. You may have a
dedicated Metadata database as described[ here ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#add-metadata-database).

### Metadata Database Permissions​

- (required) Read & write access on the schema `hdb_catalog` .


### User Database Permissions​

- (required) Read access to the `information_schema` and `pg_catalog` schemas, to query for list of tables. Note that
these permissions are usually available by default to all Postgres users via[ PUBLIC ](https://www.postgresql.org/docs/current/sql-grant.html)grant.
- (required) Read access to the schemas ( `public` or otherwise) if you only want to support queries.
- (optional) Write access to the schemas if you want to support mutations as well.
- (optional) To create tables and views via the Hasura Console (the admin UI) you'll need the privilege to create
tables/views. This might not be required when you're working with an existing database.
- (required only if Event Triggers are needed) Read, write & create access on schema: `hdb_catalog` .


## Sample scenarios​

Following are sample SQL blocks that you can run on your database (as a **superuser** ) to create the right credentials
for a sample Hasura user:

### 1. Different roles to manage metadata database and user database​

```
-- We will create separate users to manage the user database
-- and metadata database and grant permissions on hasura-specific
-- schemas and information_schema and pg_catalog.
-- These permissions/grants are required for Hasura to work properly.
-- create a separate user for to manage metadata database
CREATE   USER  hasura_metadata_user  WITH  PASSWORD  'hasura_metadata_user_password' ;
-- create the schemas required by the hasura system
-- NOTE: If you are starting from scratch: drop the below schemas first, if they exist.
CREATE   SCHEMA   IF   NOT   EXISTS  hdb_catalog ;
-- make the user an owner of the schema
ALTER   SCHEMA  hdb_catalog OWNER  TO  hasura_metadata_user ;
ALTER  ROLE hasura_metadata_user  SET  search_path  TO  hdb_catalog ;
-- Hasura needs pgcrypto extension
-- See section below on pgcrypto in PG search path
CREATE  EXTENSION  IF   NOT   EXISTS  pgcrypto ;
------------------------------------------------------------------------------
-- create a separate user for to manage user database
CREATE   USER  hasurauser  WITH  PASSWORD  'hasurauser' ;
-- create pgcrypto extension, required for UUID
-- See section below on pgcrypto in PG search path
CREATE  EXTENSION  IF   NOT   EXISTS  pgcrypto ;
-- The below permissions are optional. This is dependent on what access to your
-- tables/schemas you want give to hasura. If you want expose the public
-- schema for GraphQL query then give permissions on public schema to the
-- hasura user.
-- Be careful to use these in your production db. Consult the Postgres manual or
-- your DBA and give appropriate permissions.
-- grant all privileges on all tables in the public schema. This can be customized:
-- For example, if you only want to use GraphQL regular queries and not mutations,
-- then you can set: GRANT SELECT ON ALL TABLES...
GRANT   USAGE   ON   SCHEMA   public   TO  hasurauser ;
GRANT   ALL   ON   ALL   TABLES   IN   SCHEMA   public   TO  hasurauser ;
GRANT   ALL   ON   ALL  SEQUENCES  IN   SCHEMA   public   TO  hasurauser ;
GRANT   ALL   ON   ALL  FUNCTIONS  IN   SCHEMA   public   TO  hasurauser ;
-- Similarly add these for other schemas as well, if you have any.
-- GRANT USAGE ON SCHEMA <schema-name> TO hasurauser;
-- GRANT ALL ON ALL TABLES IN SCHEMA <schema-name> TO hasurauser;
-- GRANT ALL ON ALL SEQUENCES IN SCHEMA <schema-name> TO hasurauser;
-- GRANT ALL ON ALL FUNCTIONS IN SCHEMA <schema-name> TO hasurauser;
-- By defaults users won't have access to tables they have not created (and thus do not own).
-- You can change these default privileges to grant access to any object created in the future.
ALTER   DEFAULT   PRIVILEGES   IN   SCHEMA   public   GRANT   ALL   ON   TABLES ;
ALTER   DEFAULT   PRIVILEGES   IN   SCHEMA   public   GRANT   ALL   ON  SEQUENCES ;
ALTER   DEFAULT   PRIVILEGES   IN   SCHEMA   public   GRANT   ALL   ON  FUNCTIONS ;
-- Alternatively, you may restrict this to objects created by a specific user
-- ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES TO hasurauser;
-- ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES TO hasurauser;
-- ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS TO hasurauser;
-- grant these privileges to use create and use all Hasura GraphQL Engine functionality
GRANT   USAGE   ON   SCHEMA  hdb_catalog  TO  hasurauser ;
GRANT   CREATE   ON   SCHEMA  hdb_catalog  TO  hasurauser ;
GRANT   ALL   ON   ALL   TABLES   IN   SCHEMA  hdb_catalog  TO  hasurauser ;
GRANT   ALL   ON   ALL  SEQUENCES  IN   SCHEMA  hdb_catalog  TO  hasurauser ;
GRANT   ALL   ON   ALL  FUNCTIONS  IN   SCHEMA  hdb_catalog  TO  hasurauser ;
```

### 2. A single role to manage Metadata and user objects in the same database​

```
-- We will create a separate user to grant permissions on hasura-specific
-- schemas and information_schema and pg_catalog.
-- These permissions/grants are required for Hasura to work properly.
-- create a separate user for to manage metadata database
CREATE   USER  hasurauser  WITH  PASSWORD  'hasurauser' ;
-- create the schemas required by the hasura system
-- NOTE: If you are starting from scratch: drop the below schemas first, if they exist.
CREATE   SCHEMA   IF   NOT   EXISTS  hdb_catalog ;
-- make the user an owner of the schema
ALTER   SCHEMA  hdb_catalog OWNER  TO  hasurauser ;
-- See section below on pgcrypto in PG search path
CREATE  EXTENSION  IF   NOT   EXISTS  pgcrypto ;
-- grant select permissions on information_schema and pg_catalog. This is
-- required for hasura to query the list of available tables.
-- NOTE: these permissions are usually available by default to all users via PUBLIC grant
GRANT   SELECT   ON   ALL   TABLES   IN   SCHEMA  information_schema  TO  hasurauser ;
GRANT   SELECT   ON   ALL   TABLES   IN   SCHEMA  pg_catalog  TO  hasurauser ;
-- The below permissions are optional. This is dependent on what access to your
-- tables/schemas you want give to hasura. If you want expose the public
-- schema for GraphQL query then give permissions on public schema to the
-- hasura user.
-- Be careful to use these in your production db. Consult the Postgres manual or
-- your DBA and give appropriate permissions.
-- grant all privileges on all tables in the public schema. This can be customized:
-- For example, if you only want to use GraphQL regular queries and not mutations,
-- then you can set: GRANT SELECT ON ALL TABLES...
GRANT   USAGE   ON   SCHEMA   public   TO  hasurauser ;
GRANT   ALL   ON   ALL   TABLES   IN   SCHEMA   public   TO  hasurauser ;
GRANT   ALL   ON   ALL  SEQUENCES  IN   SCHEMA   public   TO  hasurauser ;
GRANT   ALL   ON   ALL  FUNCTIONS  IN   SCHEMA   public   TO  hasurauser ;
-- Similarly add these for other schemas as well, if you have any.
-- GRANT USAGE ON SCHEMA <schema-name> TO hasurauser;
-- GRANT ALL ON ALL TABLES IN SCHEMA <schema-name> TO hasurauser;
-- GRANT ALL ON ALL SEQUENCES IN SCHEMA <schema-name> TO hasurauser;
-- GRANT ALL ON ALL FUNCTIONS IN SCHEMA <schema-name> TO hasurauser;
-- By defaults users won't have access to tables they have not created (and thus do not own).
-- You can change these default privileges to grant access to any object created in the future.
ALTER   DEFAULT   PRIVILEGES   IN   SCHEMA   public   GRANT   ALL   ON   TABLES ;
ALTER   DEFAULT   PRIVILEGES   IN   SCHEMA   public   GRANT   ALL   ON  SEQUENCES ;
ALTER   DEFAULT   PRIVILEGES   IN   SCHEMA   public   GRANT   ALL   ON  FUNCTIONS ;
-- Alternatively, you may restrict this to objects created by a specific user
-- ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES TO hasurauser;
-- ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES TO hasurauser;
-- ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS TO hasurauser;
```

### Notes for managed databases (AWS RDS, GCP Cloud SQL, etc.)​

Hasura works out of the box with the default superuser, usually called `postgres` , created by most managed cloud
database providers.

On some cloud providers, like **Google Cloud SQL** , if you are creating a new user and giving the[ above ](https://hasura.io/docs/latest/deployment/postgres-requirements/#postgres-permissions)privileges, then you may notice that the following commands may throw warnings/errors:

```
postgres = >   ALTER   SCHEMA  hdb_catalog OWNER  TO  hasurauser ;
ERROR:  must be member  of  role  "hasurauser"
```

This happens because the superuser created by the cloud provider sometimes has different permissions. To fix this, you
can run the following command first:

```
-- assuming "postgres" is the superuser that you are running the commands with.
postgres = >   GRANT  hasurauser  to  postgres ;
GRANT
postgres = >   ALTER   SCHEMA  hdb_catalog OWNER  TO  hasurauser ;
```

You may also notice the following commands throw warnings/errors:

```
postgres = >   GRANT   SELECT   ON   ALL   TABLES   IN   SCHEMA  information_schema  TO  hasurauser ;
WARNING:   no   privileges  were granted  for   "sql_packages"
WARNING:   no   privileges  were granted  for   "sql_features"
WARNING:   no   privileges  were granted  for   "sql_implementation_info"
ERROR:  permission denied  for   table  sql_parts
postgres = >   GRANT   SELECT   ON   ALL   TABLES   IN   SCHEMA  pg_catalog  TO  hasurauser ;
ERROR:  permission denied  for   table  pg_statistic
```

You can **ignore** these warnings/errors or skip granting these permission as usually all users have relevant access to `information_schema` and `pg_catalog` schemas by default (see keyword[ PUBLIC ](https://www.postgresql.org/docs/current/sql-grant.html)).

## pgcrypto in PG search path​

Hasura GraphQL Engine needs the `pgcrypto` Postgres extension for the following:

- Metadata Database
- User Database (only if Event Triggers are used)


It needs to be ensured that `pgcrypto` is installed in a schema which is in the Postgres[ search path ](https://www.postgresql.org/docs/current/ddl-schemas.html#DDL-SCHEMAS-PATH)for the Postgres user/role that
Hasura connects with.

If `pgcrypto` is installed in a schema that is not in the search path, the schema can be added to the search path by
executing one of the following SQL commands depending on your setup:

```
-- set search path to include schemas for the entire database
ALTER   DATABASE   < database_name >   SET  search_path  TO  schema1 , schema2 ;
-- OR --
-- set search path to include schemas for a particular role
ALTER  ROLE  < hasura_role >   SET  search_path  TO  schema1 , schema2 ;
```

### Metadata Database​

During initialization, Hasura GraphQL Engine attempts to install the `pgcrypto` extension in the `public` schema if
it is not already installed. You may choose to install the Postgres extensions in a different schema by setting that
schema name in the `HASURA_GRAPHQL_METADATA_DATABASE_EXTENSIONS_SCHEMA` environment variable.

### User Database​

Hasura's Event Triggers depend on the Postgres `pgcrypto` extension. Hasura GraphQL Engine creates this extension in
the source database if it hasn't already been installed when the first Event Trigger on the source is created. By
default, the extensions are created in the `public` schema but if you want to install the Postgres extensions in a
custom schema you can achieve this by specifying the schema name in the `extensions_schema` field of the source
configuration.

Image: [ Update extensions schema from Console ](https://hasura.io/docs/assets/images/set-pg-extensions-schema-062c6792204a4220045b17e3bd48dacf.png)

Note

If you're using Heroku Postgres instance for the first time, you will get an error `pgcrypto can only be created in heroku_ext schema` .

For Metadata database, set environment variable `HASURA_GRAPHQL_METADATA_DATABASE_EXTENSIONS_SCHEMA: heroku_ext` and
for user database with Event Triggers, set `extensions_schema: heroku_ext` in source configuration.

## Managed Postgres permissions​

Hasura works out of the box with the default superuser, usually called `postgres` , created by most managed cloud
database providers.

If you use another database user, you will need to make sure that this user has the right Postgres permissions.

## Sample Scenario​

Here's a sample SQL block that you can run on your database (as a **superuser** ) to create the right credentials for a
sample Hasura user called `hasurauser` :

```
-- create a separate user for hasura (if you don't already have one)
CREATE   USER  hasurauser  WITH  PASSWORD  'hasurauser' ;
-- create pgcrypto extension, required for UUID
CREATE  EXTENSION  IF   NOT   EXISTS  pgcrypto ;
-- create the schemas required by the hasura cloud system
CREATE   SCHEMA   IF   NOT   EXISTS  hdb_catalog ;
CREATE   SCHEMA   IF   NOT   EXISTS  hdb_views ;
CREATE   SCHEMA   IF   NOT   EXISTS  hdb_pro_catalog ;
-- make the user an owner of the hasura cloud system schemas
ALTER   SCHEMA  hdb_catalog OWNER  TO  hasurauser ;
ALTER   SCHEMA  hdb_views OWNER  TO  hasurauser ;
ALTER   SCHEMA  hdb_pro_catalog OWNER  TO  hasurauser ;
-- grant select permissions on information_schema and pg_catalog
GRANT   SELECT   ON   ALL   TABLES   IN   SCHEMA  information_schema  TO  hasurauser ;
GRANT   SELECT   ON   ALL   TABLES   IN   SCHEMA  pg_catalog  TO  hasurauser ;
-- grant all privileges on all tables in the public schema (this is optional and can be customized)
GRANT   USAGE   ON   SCHEMA   public   TO  hasurauser ;
GRANT   ALL   ON   ALL   TABLES   IN   SCHEMA   public   TO  hasurauser ;
GRANT   ALL   ON   ALL  SEQUENCES  IN   SCHEMA   public   TO  hasurauser ;
GRANT   ALL   ON   ALL  FUNCTIONS  IN   SCHEMA   public   TO  hasurauser ;
-- Similarly add these for other schemas as well, if you have any
-- GRANT USAGE ON SCHEMA <schema-name> TO hasurauser;
-- GRANT ALL ON ALL TABLES IN SCHEMA <schema-name> TO hasurauser;
-- GRANT ALL ON ALL SEQUENCES IN SCHEMA <schema-name> TO hasurauser;
-- GRANT ALL ON ALL FUNCTIONS IN SCHEMA <schema-name> TO hasurauser;
```

You may notice the following commands throw warnings/errors:

```
postgres = >   GRANT   SELECT   ON   ALL   TABLES   IN   SCHEMA  information_schema  TO  hasurauser ;
WARNING:   no   privileges  were granted  for   "sql_packages"
WARNING:   no   privileges  were granted  for   "sql_features"
WARNING:   no   privileges  were granted  for   "sql_implementation_info"
ERROR:  permission denied  for   table  sql_parts
postgres = >   GRANT   SELECT   ON   ALL   TABLES   IN   SCHEMA  pg_catalog  TO  hasurauser ;
ERROR:  permission denied  for   table  pg_statistic
```

You can **ignore** these warnings/errors or skip granting these permission as usually all users have relevant access to `information_schema` and `pg_catalog` schemas by default (see keyword[ PUBLIC ](https://www.postgresql.org/docs/current/sql-grant.html)).

Note

If you first connect Postgres with the default superuser, and afterwards with another user, you might get an error. You
then need to reset the permissions to the new user.

### Note for GCP​

On Google Cloud SQL, if you are creating a new user and giving the[ above ](https://hasura.io/docs/latest/deployment/postgres-requirements/#postgres-permissions)privileges, then you may notice that the following
commands may throw warnings/errors:

```
postgres = >   ALTER   SCHEMA  hdb_catalog OWNER  TO  hasurauser ;
ERROR:  must be member  of  role  "hasurauser"
```

This happens because the superuser created by the cloud provider sometimes has different permissions. To fix this, you
can run the following command first:

```
-- assuming "postgres" is the superuser that you are running the commands with.
postgres = >   GRANT  hasurauser  to  postgres ;
GRANT
postgres = >   ALTER   SCHEMA  hdb_catalog OWNER  TO  hasurauser ;
```

## Further reading​

For more information and a more detailed explanation on Postgres permissions, refer to the[ Hasura core Postgres requirements ](https://hasura.io/docs/latest/deployment/postgres-requirements/)page.

### What did you think of this doc?

- [ Supported Postgres versions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#postgres-version-support)
- [ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#postgres-permissions)
    - [ Metadata Database Permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#metadata-database-permissions)

- [ User Database Permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#user-database-permissions)
- [ Sample scenarios ](https://hasura.io/docs/latest/deployment/postgres-requirements/#sample-scenarios)
    - [ 1. Different roles to manage metadata database and user database ](https://hasura.io/docs/latest/deployment/postgres-requirements/#1-different-roles-to-manage-metadata-database-and-user-database)

- [ 2. A single role to manage Metadata and user objects in the same database ](https://hasura.io/docs/latest/deployment/postgres-requirements/#2-a-single-role-to-manage-metadata-and-user-objects-in-the-same-database)

- [ Notes for managed databases (AWS RDS, GCP Cloud SQL, etc.) ](https://hasura.io/docs/latest/deployment/postgres-requirements/#notes-for-managed-databases-aws-rds-gcp-cloud-sql-etc)
- [ pgcrypto in PG search path ](https://hasura.io/docs/latest/deployment/postgres-requirements/#pgcrypto-in-pg-search-path)
    - [ Metadata Database ](https://hasura.io/docs/latest/deployment/postgres-requirements/#metadata-database)

- [ User Database ](https://hasura.io/docs/latest/deployment/postgres-requirements/#user-database)
- [ Managed Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#managed-pg-permissions)
- [ Sample Scenario ](https://hasura.io/docs/latest/deployment/postgres-requirements/#sample-scenario)
    - [ Note for GCP ](https://hasura.io/docs/latest/deployment/postgres-requirements/#note-for-gcp)
- [ Further reading ](https://hasura.io/docs/latest/deployment/postgres-requirements/#further-reading)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)