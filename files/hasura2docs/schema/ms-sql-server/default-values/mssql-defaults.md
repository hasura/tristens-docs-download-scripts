# MS SQL Server: Setting Default Values for Fields Using MS SQL Server Defaults

## Introduction​

You can set values of certain fields automatically when not explicitly passed to a fixed value, e.g. true for a boolean
field, or output of a simple SQL function, e.g. GETDATE() for a timestamp field, by setting column default values in the
table definition.

Note

The MS SQL Server default value is ignored when a value is explicitly set to the field.

 **Example:** Say we have a field `created_at` in a table `article` which we want to be set to the current timestamp
whenever a new row is added to the table:

## Step 1: Modify the table​

Edit the `created_at` field and set its default value as the SQL function `GETDATE()` .

- Console
- API


Open the Console and head to `Data -> [article] -> Modify` .

Click the `Edit` button next to the `created_at` field and add `GETDATE()` as a default value.

Image: [ Modify the table in the Console ](https://hasura.io/docs/assets/images/mssql-add-default-value-15a9d9d89d09c3ddfb153d96e19c235b.png)

You can add a default value by using the mssql_run_sql schema API:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_run_sql" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "sql" :   "ALTER TABLE article ADD CONSTRAINT DF_article DEFAULT GETDATE() FOR created_at;"
   }
}
```

To set an auto-incrementing default value

To set a default value as an auto-incrementing integer you first need to set up a `sequence` which will be the source of
our default value.

Let's say we have a field called `roll_number` which we would like to be set by default as an auto-incremented integer.

Run the following SQL command to create a new sequence.

`CREATE  SEQUENCE roll_number_seq  AS   INT   START   WITH   0  INCREMENT  BY   1 ;`

Now set the default value of the `roll_number` field as `DEFAULT (NEXT VALUE FOR roll_number_seq)` .

## Step 2: Run an insert mutation​

Now if you do not pass the `created_at` field value while running an insert mutation on the `article` table, its value
will be set automatically by MS SQL Server.

## Also see​

- [ MS SQL Server: Setting values for fields using role-based column presets ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-column-presets/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-defaults/#introduction)
- [ Step 1: Modify the table ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-defaults/#step-1-modify-the-table)
- [ Step 2: Run an insert mutation ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-defaults/#step-2-run-an-insert-mutation)
- [ Also see ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-defaults/#also-see)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)