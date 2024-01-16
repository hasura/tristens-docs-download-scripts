# Postgres: Setting Default Values for Fields Using Postgres Defaults

## Introduction​

You can set values of certain fields automatically when not explicitly passed to a fixed value, e.g. true for a boolean
field, or output of a simple SQL function, e.g. now() for a timestamp field, by setting column default values in the
table definition.

Note

The Postgres default value is ignored when a value is explicitly set to the field.

 **Example:** Say we have a field `created_at` in a table `article` which we want to be set to the current timestamp
whenever a new row is added to the table:

## Step 1: Modify the table​

Edit the `created_at` field and set its default value as the SQL function `now()` .

- Console
- CLI
- API


Open the Console and head to `Data -> [article] -> Modify` .

Click the `Edit` button next to the `created_at` field and add `now()` as a default value.

Image: [ Modify the table in the Console ](https://hasura.io/docs/assets/images/add-default-value-94092ebe2e153fc7128f4c0b9b9803fb.png)

[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
following SQL statement to the `up.sql` file:

`ALTER   TABLE  ONLY  "public" . "article"   ALTER   COLUMN   "created_at"   SET   DEFAULT   now ( ) ;`

Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)the above statement:

`ALTER   TABLE  article  ALTER   COLUMN  created_at  DROP   DEFAULT ;`

Apply the migration by running:

`hasura migrate apply`

You can add a default value by using the[ run_sql ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql)schema API:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "run_sql" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "sql" :   "ALTER TABLE article ALTER COLUMN created_at SET DEFAULT now();"
   }
}
```

To set an auto-incrementing default value

To set a default value as an auto-incrementing integer you first need to set up a `sequence` which will be the source of
our default value.

Let's say we have a field called `roll_number` which we would like to be set by default as an auto-incremented integer.

Run the following SQL command to create a new sequence.

`CREATE  SEQUENCE roll_number_seq ;`

Now set the default value of the `roll_number` field as `nextval('roll_number_seq')` .

## Step 2: Run an insert mutation​

Now if you do not pass the `created_at` field value while running an insert mutation on the `article` table, its value
will be set automatically by Postgres.

## Also see​

- [ Postgres: Setting values of fields using SQL functions ](https://hasura.io/docs/latest/schema/postgres/default-values/sql-functions/)
- [ Postgres: Setting values for fields using role-based column presets ](https://hasura.io/docs/latest/schema/postgres/default-values/column-presets/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/default-values/postgres-defaults/#introduction)
- [ Step 1: Modify the table ](https://hasura.io/docs/latest/schema/postgres/default-values/postgres-defaults/#step-1-modify-the-table)
- [ Step 2: Run an insert mutation ](https://hasura.io/docs/latest/schema/postgres/default-values/postgres-defaults/#step-2-run-an-insert-mutation)
- [ Also see ](https://hasura.io/docs/latest/schema/postgres/default-values/postgres-defaults/#also-see)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)