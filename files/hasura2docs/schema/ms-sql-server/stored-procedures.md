# MS SQL Server: Stored Procedures

## What are stored procedures?​

Supported from

Stored procedures are supported from `v2.26.0` .

Stored procedures can be used to track MS SQL Server[ stored procedures ](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine)and execute them via the Hasura GraphQL Engine.

SQL Server stored procedures are built-in or user-defined Transact-SQL statements that can be used to encapsulate some
custom business logic or extend the built-in SQL functions and operators.

stored procedures support is a Cloud and Enterprise feature of Hasura.

Supported features

Currently, only read-only stored procedures are supported, and Hasura aggregations or relationships are not supported at
this time.

## Example: Execute a built-in stored procedure​

We’ll start with an example. Let’s use this new feature to execute a built-in stored procedure from our Hasura API. If
you’d like some reference documentation, scroll down, and also take a look at the[ Logical Models documentation ](https://hasura.io/docs/latest/schema/ms-sql-server/logical-models/).

For our case, we would like to get some information about our database. Specifically, which tables are currently defined
in the database. On SQL Server we can do that by executing the[ sp_tables ](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-tables-transact-sql)stored procedure.

We can create a Logical Model representing the results set:

- Console
- CLI
- API


Click on the `Logical Models` tab, and on the `Add Logical Model` button.

Image: [ Create Logical Model ](https://hasura.io/docs/assets/images/logical-model-add-0af3fc9409cc5928e2bfc3361ef2cbd7.png)

Once the modal is open, fill in the form.

Image: [ Create Logical Model Form ](https://hasura.io/docs/assets/images/create-logical-model-e9722a4594f41020e034023de133b69a.png)

Add the following to the relevant database definition in the `metadata > databases > databases.yaml` file:

```
logical_models :
   -   name :  tables
     fields :
       TABLE_QUALIFIER :
         type :  sysname
         nullable :   true
       TABLE_OWNER :
         type :  sysname
         nullable :   true
       TABLE_NAME :
         type :  sysname
         nullable :   true
       TABLE_TYPE :
         type :   'varchar(32)'
         nullable :   true
       REMARKS :
         type :   'varchar(254)'
         nullable :   true
```

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_track_logical_model" ,
   "args" :   {
     "source" :   "mssql" ,
     "name" :   "tables" ,
     "fields" :   [
       {
         "name" :   "TABLE_QUALIFIER" ,
         "type" :   "sysname" ,
         "nullable" :   true
       } ,
       {
         "name" :   "TABLE_OWNER" ,
         "type" :   "sysname" ,
         "nullable" :   true
       } ,
       {
         "name" :   "TABLE_NAME" ,
         "type" :   "sysname" ,
         "nullable" :   true
       } ,
       {
         "name" :   "TABLE_TYPE" ,
         "type" :   "varchar(32)" ,
         "nullable" :   true
       } ,
       {
         "name" :   "REMARKS" ,
         "type" :   "varchar(254)" ,
         "nullable" :   true
       }
     ]
   }
}
```

We can then track a stored procedure that returns that result set. Additionally, we can add arguments which can be
passed to the stored procedure from the GraphQL API. We'll include the `table_type` arguments which can be used to
filter tables, system tables, and views.

Validation during tracking is not currently supported

Currently, stored procedures are not checked against the Logical Model to validate that they return the expected result
set or that the arguments match with the stored procedure's arguments. This means that if there's a mismatch between the
database stored procedure and the Logical Model or the arguments, an error will be thrown when running a query.

- Console
- CLI
- API


Click on the `Stored Procedures` tab, and on the `Track Stored Procedures` button.

Image: [ Track Stored Procedure ](https://hasura.io/docs/assets/images/track-stored-procedure-85072465cc5065cde92cb8d1b17148f4.png)

Next, fill in the form, choosing the Logical Model created in the previous step:

Image: [ Stored Procedure Form ](https://hasura.io/docs/assets/images/stored-procedure-form-1530a0c96bd2d1a9b9a985a9d291fbeb.png)

Add the following to the relevant database definition in the `metadata > databases > databases.yaml` file:

```
stored_procedures :
   -   stored_procedure :
       schema :  public
       name :  sp_tables
     configuration :
       exposed_as :  query
     arguments :
       table_type :
         type :  varchar
     returns :  tables
```

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_track_stored_procedure" ,
   "args" :   {
     "source" :   "mssql" ,
     "stored_procedure" :   "sp_tables" ,
     "configuration" :   {
       "exposed_as" :   "query"
     } ,
     "arguments" :   {
       "table_type" :   {
         "type" :   "varchar"
       }
     } ,
     "returns" :   "tables"
   }
}
```

All that’s left is for us to make a GraphQL query to select the tables which are currently defined in the database:

```
query   sp   {
   sp_tables ( args :   {   table_type :   "'TABLE'"   } ,   limit :   3 )   {
     TABLE_QUALIFIER
     TABLE_OWNER
     TABLE_NAME
     TABLE_TYPE
   }
}
```

When we run this GraphQL query, we get the following results:

```
{
   "data" :   {
     "sp_tables" :   [
       {
         "TABLE_QUALIFIER" :   "master" ,
         "TABLE_OWNER" :   "dbo" ,
         "TABLE_NAME" :   "MSreplication_options" ,
         "TABLE_TYPE" :   "TABLE"
       } ,
       {
         "TABLE_QUALIFIER" :   "master" ,
         "TABLE_OWNER" :   "dbo" ,
         "TABLE_NAME" :   "spt_fallback_db" ,
         "TABLE_TYPE" :   "TABLE"
       } ,
       {
         "TABLE_QUALIFIER" :   "master" ,
         "TABLE_OWNER" :   "dbo" ,
         "TABLE_NAME" :   "spt_fallback_dev" ,
         "TABLE_TYPE" :   "TABLE"
       }
     ]
   }
}
```

Next, we'll look at the process of tracking a stored procedure in more detail.

## Tracking a stored procedure​

### Step 1. Create a Logical Model​

In order to represent the structure of the data returned by the query, we first create a Logical Model.

Permissions and Logical Models

Note that this Logical Model has no attached permissions and therefore will only be available to the admin role. See the[ Logical Model documentation ](https://hasura.io/docs/latest/schema/ms-sql-server/logical-models/)for information on attaching permissions.

- Console
- CLI
- API


Click on the `Logical Models` tab, and on the `Add Logical Model` button.

Image: [ Create Logical Model ](https://hasura.io/docs/assets/images/logical-model-add-0af3fc9409cc5928e2bfc3361ef2cbd7.png)

Once the modal is open, fill in the form with the name of the Logical Model and the fields that will be returned by the
stored procedure.

You can create a logical model by adding it to the appropriate database definition in the `metadata > databases > databases.yaml` file:

```
   logical_models :
     -   name :   "<name>"
       fields :
         "<field name>" :
           type :   "<SQL Server field type>"
           nullable :  false  |  true
           description :   "<optional field description>"
         ...
```

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_track_logical_model" ,
   "args" :   {
     "source" :   "default" ,
     "name" :   "<name>" ,
     "fields" :   [
       {
         "name" :   "<field name>" ,
         "type" :   "<SQL Server field type>" ,
         "nullable" :   false  |  true ,
         "description" :   "<optional field description>"
       } ,
      ...
     ]
   }
}
```

### Step 2. Track a stored procedure​

Once the Logical Model is defined, we can use it to define the query:

- Console
- CLI
- API


Click on the `Stored Procedures` tab, and on the `Track Stored Procedures` button.

Image: [ Track Stored Procedure ](https://hasura.io/docs/assets/images/track-stored-procedure-85072465cc5065cde92cb8d1b17148f4.png)

Next, fill in the form, choosing the Logical Model created in the previous step as the return type.

Add the following to the relevant database definition in the `metadata > databases > databases.yaml` file:

```
stored_procedures :
   -   stored_procedure :
       schema :   '<schema name>'
       name :   '<procedure name>'
     configuration :
       exposed_as :  query
       custom_name :   '<custom name>'
     arguments :
       '<argument name>' :
         type :   '<SQL Server field type>'
         nullable :  false  |  true
         description :   '<optional argument description>'
     returns :   '<logical model name>'
```

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_track_stored_procedure" ,
   "args" :   {
     "source" :  <source name> ,
     "stored_procedure" :  <procedure name> |  {   "schema" :  <schema name> ,   "name" :  <procedure name>  } ,
     "arguments" :   {
       "<argument name>" :   {
         "type" :   "<SQL Server field type>" ,
         "nullable" :   false  |  true ,
         "description" :   "<optional argument description>"
       }
     } ,
     "configuration" :   {
       "exposed_as" :   "query" ,
       "custom_name" :  <custom name>
     } ,
     "returns" :  <logical model name>
   }
}
```

#### Arguments​

The stored procedure can take arguments, which are specified in the metadata. When making a GraphQL query, the arguments
are specified using the `args` parameter of the query root field. If the stored procedure does not take arguments, the `args` parameter should be omitted from the GraphQL query.

## Using the stored procedure​

You can make a GraphQL request using the specified root field name just as you would any other GraphQL query. When
making a query, the arguments are specified using the `args` parameter of the query root field.

```
query   {
  < stored   procedure   name > (
     [ args :   { "<argument name>" :  < argument   value > ,   ... } , ]
     [ where :   ... , ]
     [ order_by :   ... ,   distinct_on :   ... , ]
     [ limit :   ... ,   offset :   ... ]
   )   {
    < field   1 >
    < field   2 >
     ...
   }
}
```

Currently running a stored procedure has the following caveats:

- The stored procedure must currently be read-only.
- The return type of the query must match with the Logical Model.


## Query functionality​

Just like tables, stored procedures generate GraphQL types with the ability to further break down the data. You can find
more information in the relevant documentation for[ filtering ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/index/),[ sorting ](https://hasura.io/docs/latest/queries/ms-sql-server/sorting/), and[ pagination ](https://hasura.io/docs/latest/queries/ms-sql-server/pagination/).

## Mutations​

Currently, only read-only stored procedures are supported. All stored procedures are run in a read-only transaction
where supported to enforce this constraint.

A future release will allow mutations to be specified using stored procedures.

## Permissions​

stored procedures will inherit the permissions of the Logical Model that they return. See the[ documentation on Logical Models ](https://hasura.io/docs/latest/schema/ms-sql-server/logical-models/)for an explanation of how to add
permissions.

### What did you think of this doc?

- [ What are stored procedures? ](https://hasura.io/docs/latest/schema/ms-sql-server/stored-procedures/#what-are-stored-procedures)
- [ Example: Execute a built-in stored procedure ](https://hasura.io/docs/latest/schema/ms-sql-server/stored-procedures/#example-execute-a-built-in-stored-procedure)
- [ Tracking a stored procedure ](https://hasura.io/docs/latest/schema/ms-sql-server/stored-procedures/#tracking-a-stored-procedure)
    - [ Step 1. Create a Logical Model ](https://hasura.io/docs/latest/schema/ms-sql-server/stored-procedures/#step-1-create-a-logical-model)

- [ Step 2. Track a stored procedure ](https://hasura.io/docs/latest/schema/ms-sql-server/stored-procedures/#step-2-track-a-stored-procedure)
- [ Using the stored procedure ](https://hasura.io/docs/latest/schema/ms-sql-server/stored-procedures/#using-the-stored-procedure)
- [ Query functionality ](https://hasura.io/docs/latest/schema/ms-sql-server/stored-procedures/#query-functionality)
- [ Mutations ](https://hasura.io/docs/latest/schema/ms-sql-server/stored-procedures/#mutations)
- [ Permissions ](https://hasura.io/docs/latest/schema/ms-sql-server/stored-procedures/#permissions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)