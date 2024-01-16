# Postgres: Adding created_at / updated_at Timestamps

## Introduction​

We often need `created_at` and `updated_at` timestamp fields in our tables in order to indicate when an object was
created or last updated. This page explains how to add these.

## Add a created_at timestamp​

- Console
- CLI
- API


On the Hasura Console, click on the `Modify` tab of a table. When clicking on the `+Frequently used columns` button,
choose `created_at` :

Image: [ Add a created_at time on the Hasura Console ](https://hasura.io/docs/assets/images/created-at-4292ed6a70ce2905e0bffb07629c90b9.png)

Click the `Add column` button.

[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
following SQL statement to the `up.sql` file:

`ALTER   TABLE   ONLY   "public" . "article"   ADD  COLUMN  "created_at"   TIMESTAMP   DEFAULT   NOW ( ) ;`

Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)the above statement:

`ALTER   TABLE  article  DROP  COLUMN created_at ;`

Apply the migration and reload the metadata:

```
hasura migrate apply
hasura metadata reload
```

You can add a `created_at` timestamp by using the[ run_sql ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql)schema
API:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "run_sql" ,
   "args" :   {
       "source" :   "<db_name>" ,
       "sql" :   "ALTER TABLE ONLY \"article\" ADD COLUMN \"created_at\" TIMESTAMP DEFAULT NOW();"
   }
}
```

## Add an updated_at timestamp​

- Console
- CLI
- API


On the Hasura Console, click on the `Modify` tab of a table. When clicking on the `+Frequently used columns` button,
choose `updated_at` :

Image: [ Add an updated_at time on the Hasura Console ](https://hasura.io/docs/assets/images/updated-at-d0a9b63c74349877d911ca49d06a16a3.png)

Click the `Add column` button.

[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
below SQL statement to the `up.sql` file:

1. Add an `updated_at` timestamp field to the `article` table.
2. Define a[ Postgres function ](https://www.postgresql.org/docs/current/sql-createfunction.html)to set the `updated_at` field to `NOW()` .
3. Create a[ Postgres trigger ](https://www.postgresql.org/docs/current/sql-createtrigger.html)to call the defined
function whenever an article is updated.


```
ALTER   TABLE   ONLY   "public" . "article"
ADD  COLUMN  "updated_at"   TIMESTAMP   DEFAULT   NOW ( ) ;
CREATE   FUNCTION  trigger_set_timestamp ( )
RETURNS TRIGGER  AS  $$
BEGIN
   NEW . updated_at  =   NOW ( ) ;
RETURN   NEW ;
END ;
$$  LANGUAGE  plpgsql ;
CREATE  TRIGGER set_timestamp
BEFORE
UPDATE   ON  article
FOR  EACH  ROW
EXECUTE   PROCEDURE  trigger_set_timestamp ( ) ;
```

Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)the above statement:

```
DROP  trigger set_timestamp  on  article ;
DROP   function  trigger_set_timestamp ( ) ;
ALTER   TABLE  article  DROP  COLUMN updated_at ;
```

Apply the migration and reload the metadata:

```
hasura migrate apply
hasura metadata reload
```

You can add an `updated_at` timestamp by using the[ run_sql ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql)schema API.

The below SQL statement will achieve the following:

1. Add an `updated_at` timestamp field to the `article` table.
2. Define a[ Postgres function ](https://www.postgresql.org/docs/current/sql-createfunction.html)to set the `updated_at` field to `NOW()` .
3. Create a[ Postgres trigger ](https://www.postgresql.org/docs/current/sql-createtrigger.html)to call the defined
function whenever an article is updated.


```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "run_sql" ,
   "args" :   {
       "source" :   "<db_name>" ,
       "sql" :
        "ALTER TABLE ONLY \"public\".\"article\"
        ADD COLUMN \"updated_at\" TIMESTAMP DEFAULT NOW();
        CREATE FUNCTION trigger_set_timestamp()
        RETURNS TRIGGER AS $$
        BEGIN
          NEW.updated_at = NOW();
        RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        CREATE TRIGGER set_timestamp
        BEFORE
        UPDATE ON article
        FOR EACH ROW
        EXECUTE PROCEDURE trigger_set_timestamp();"
   }
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/default-values/created-updated-timestamps/#introduction)
- [ Add a created_at timestamp ](https://hasura.io/docs/latest/schema/postgres/default-values/created-updated-timestamps/#add-a-created_at-timestamp)
- [ Add an updated_at timestamp ](https://hasura.io/docs/latest/schema/postgres/default-values/created-updated-timestamps/#add-an-updated_at-timestamp)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)