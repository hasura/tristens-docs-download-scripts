# Postgres: Setting Values of Fields Using SQL Functions

## Introduction​

Let's say you want to set the value of some fields as the output of some[ custom SQL functions ](https://www.postgresql.org/docs/current/sql-createfunction.html)(a.k.a. stored procedures). This
is useful to set values of fields which depend on other fields passed in the input. E.g. set `submission_time` of an
online quiz as 1 hour from the `start_time` .

This can be achieved by:

1. Modifying the table to allow the columns we want to be set by the SQL functions to be nullable (to allow the initial
insert before the SQL function is run).
2. Creating an insert/update trigger on the table that calls your SQL function and sets the output values in the output
columns.
3. Making your mutation requests without setting the SQL function output columns.


Note

This approach enforces the value set in the field to always be the result of the defined SQL function even if a value is
explicitly passed in the insert object.

 **For example** , say we have a table `sql_function_table` with columns `input` and `output` and we would like to set the
value of the `output` column as the uppercased value of the string received in the `input` field.

## Step 1: Modify the table​

Modify the table `sql_function_table` and make its `output` column nullable.

- Console
- CLI
- API


Open the Console and head to `Data -> [sql_function_table] -> Modify` :

Image: [ Modify the table ](https://hasura.io/docs/assets/images/modify-sql-fn-table-9a0a71b3d642fd61faa375ea3e4a4295.png)

[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
following SQL statement to the `up.sql` file:

`ALTER   TABLE   "public" . "sql_function_table"   ALTER   COLUMN   "output"   DROP   NOT   NULL ;`

Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)the above statement:

`ALTER   TABLE   "public" . "sql_function_table"   ALTER   COLUMN   "output"   SET   NOT   NULL ;`

Apply the migration by running:

`hasura migrate apply`

You can modify a table column by using the[ run_sql ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql)schema API:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "run_sql" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "sql" :   "ALTER TABLE sql_function_table ALTER COLUMN output DROP NOT NULL;"
   }
}
```

## Step 2: Create a trigger​

The below SQL defines a `trigger` which will simply uppercase the value passed in the `input` field and set it to the `output` field whenever an insert or update is made to the `sql_function_table` :

```
CREATE   FUNCTION  test_func ( )  RETURNS trigger  AS  $emp_stamp$
       BEGIN
           NEW . output  :=  UPPER ( NEW . input ) ;
           RETURN   NEW ;
       END ;
  $emp_stamp$  LANGUAGE  plpgsql ;
   CREATE  TRIGGER test_trigger BEFORE  INSERT   OR   UPDATE   ON  sql_function_table
       FOR  EACH  ROW   EXECUTE   PROCEDURE  test_func ( ) ;
```

- Console
- CLI
- API


Head to `Data -> SQL` and run the above SQL:

Image: [ Create a trigger with SQL ](https://hasura.io/docs/assets/images/create-trigger-7d0a5b5bba3d7135a4a3468cd3e0c54c.png)

[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
above SQL to the `up.sql` file. Also, add a statement to revert the previous statement to the `down.sql` .

Apply the migration by running:

`hasura migrate apply`

You can create a trigger by using the[ run_sql ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql)schema API:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "run_sql" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "sql" :   "<above SQL>"
   }
}
```

## Step 3: Run an insert mutation​

Run a mutation to insert an object with (input = "yabba dabba doo!", output=null) and you'll see the output value
(output="YABBA DABBA DOO!") will be set automatically.

## Also see​

- [ Postgres: Setting default values for fields using Postgres defaults ](https://hasura.io/docs/latest/schema/postgres/default-values/postgres-defaults/)
- [ Postgres: Setting values for fields using role-based column presets ](https://hasura.io/docs/latest/schema/postgres/default-values/column-presets/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/default-values/sql-functions/#introduction)
- [ Step 1: Modify the table ](https://hasura.io/docs/latest/schema/postgres/default-values/sql-functions/#step-1-modify-the-table)
- [ Step 2: Create a trigger ](https://hasura.io/docs/latest/schema/postgres/default-values/sql-functions/#step-2-create-a-trigger)
- [ Step 3: Run an insert mutation ](https://hasura.io/docs/latest/schema/postgres/default-values/sql-functions/#step-3-run-an-insert-mutation)
- [ Also see ](https://hasura.io/docs/latest/schema/postgres/default-values/sql-functions/#also-see)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)