# Get Started with Docker (Hasura & MS SQL Server)

## Introduction​

### Pre-requisites​

- [ Docker ](https://docs.docker.com/install/)
- [ Docker Compose ](https://docs.docker.com/compose/install/)
- An existing SQL Server database


Note

Support for MS SQL Server on M1/M2 Macs was added in version `v2.15.0` .

### Step 1: Get the docker-compose file​

Get the Hasura MS SQL Server docker compose file:

```
# in a new directory run
wget  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/docker-compose-ms-sql-server/docker-compose.yaml
# or run
curl  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/docker-compose-ms-sql-server/docker-compose.yaml -o docker-compose.yaml
```

Note

This docker compose file utilizes the `tempdb mssql` database which is primarily used for testing. While this is a quick
way to get up and running using MS SQL with the Hasura GraphQL Engine, other solutions should be utilized for production
databases.

### Step 2: Run Hasura GraphQL Engine​

The following command will run:

- The Hasura GraphQL Engine
- The MS SQL Server to act as your local database
- A Postgres database responsible for Hasura's metadata


`$  docker  compose up -d`

Check if the containers are running:

```
$  docker   ps
CONTAINER ID   IMAGE                                        COMMAND                  CREATED         STATUS         PORTS                    NAMES
1bbfb6c6311d   hasura/graphql-engine:v2.8.4                  "graphql-engine serve"     4  seconds ago   Up  2  seconds    0.0 .0.0:8080- > 8080 /tcp   hasura-graphql-engine-1
1ce5806438bb   mcr.microsoft.com/mssql/server:2022-latest    "/opt/mssql/bin/perm…"     4  seconds ago   Up  3  seconds    1433 /tcp                 hasura-mssql-1
0e09d1f31c0e   postgres:14                                   "docker-entrypoint.s…"     4  seconds ago   Up  3  seconds    5432 /tcp                 hasura-postgres-1
```

### Step 3: Open the Hasura Console​

Head to `http://localhost:8080/console` to open the Hasura Console.

### Step 4: Add your SQL Server database as a source to Hasura​

Head to the `Data > Manage databases` section on the Console to add your MS SQL Server as a source to Hasura. You'll
need your ODBC connection string. Make sure that your ODBC driver is set to version 17.

Here are 2 examples of what your connection strings might look like:

- Testing with SQL Server running locally on Mac: `Driver={ODBC Driver 18 for SQL Server};Server=tcp:host.docker.internal,1433;Database=tempdb;Uid=sa;Pwd=Password123;Encrypt=optional`
- A SQL Server instance on Azure SQL Serverless: `Driver={ODBC Driver 18 for SQL Server};Server=tcp:db.<hostname>.com,1433;Database=<db-name>;Uid=<username>;Pwd=<password>;Encrypt=yes;TrustServerCertificate=no;ConnectionTimeout=30;`


Testing with SQL Server running locally on Mac:

 `Driver={ODBC Driver 18 for SQL Server};Server=tcp:host.docker.internal,1433;Database=tempdb;Uid=sa;Pwd=Password123;Encrypt=optional` 

A SQL Server instance on Azure SQL Serverless:

 `Driver={ODBC Driver 18 for SQL Server};Server=tcp:db.<hostname>.com,1433;Database=<db-name>;Uid=<username>;Pwd=<password>;Encrypt=yes;TrustServerCertificate=no;ConnectionTimeout=30;` 

If you're testing Hasura with SQL Server running locally,[ read this guide ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-networking)on Docker networking in case you're not
sure how to make sure that your SQL Server database is reachable from the Hasura docker container on Linux, Mac or
Windows.

Image: [ Manage databases ](https://hasura.io/docs/assets/images/manage-databases_console_2.10.1-551bbcec8cdf5510bfe4b40ea977df5b.png)

Image: [ Add source ](https://hasura.io/docs/assets/images/connect-ms-sql-db_console_2.10.1-71fa535096dfffbad524c4431f3ebdd7.png)

Once you add the database, you'll see your database pop up on the sidebar.

### Step 5: Option 1: Track existing tables​

If you have existing tables, head to the database page by clicking on the database name on the sidebar. You should see a
list of tables.

Image: [ Manage my-db ](https://hasura.io/docs/assets/images/manage-db_step-3_console_2.10.1-21825c035d2944e8c56386e7de0dd36c.png)

Track tables selectively or all of them so that Hasura can introspect the tables and create the corresponding GraphQL
schema.

Image: [ Track tables ](https://hasura.io/docs/assets/images/track-tables_step-3_console_2.10.1-4d716ebfd2cd99dc71e00a3d20fd4d28.png)

If you have foreign keys, you'll also see suggested relationships. Again, you can choose to track them selectively or
all at once.

Image: [ Track relationships ](https://hasura.io/docs/assets/images/track-foreign-key-rel_step-3_console_2.10.1-87f74f01fbe37da0d73c423ccb237269.png)

### Step 5: Option 2: Create new tables​

If you don't have existing tables, head to the Run SQL window to run SQL against your SQL Server database and create
tables or hit the Create Table button to create a table.

If you're running raw SQL queries to create your tables, Don't forget to check "track metadata" at the bottom of the Run
SQL window to make sure Hasura tracks your new database objects in its GraphQL schema.

Image: [ Run SQL to create table ](https://hasura.io/docs/assets/images/run-sql_step-3_console_2.10.1-86819d4f3827c3224436def58bc95181.png)

### Step 6: Try out a GraphQL query​

Head to the `API` tab in the Console and try running a GraphQL query! Use the explorer sidebar on GraphQL to get help in
creating a GraphQL query.

Image: [ Make GraphQL query ](https://hasura.io/docs/assets/images/api-explorer_step-4_console_2.10.1-9b6bd90b02f0f81c53b785a4e67053ba.png)

## Keep up to date​

Hasura supports queries, subscriptions, relationships and permissions on MS SQL Server.

Please watch this space to get the latest docs on how you can try these features out via the Console or by manipulating
Metadata in JSON/YAML directly.

If you'd like to stay informed about the status of SQL Server support, subscribe to our newsletter and join our discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


Additional Resources

This Hands-on Demo walks you through Getting Started with Hasura on SQL Server & common use cases. -[ View Recording here ](https://hasura.io/events/webinar/hasura-sql-server/?pg=docs&plcmt=body&cta=view-recording&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/docker/#introduction)
    - [ Pre-requisites ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/docker/#pre-requisites)

- [ Step 1: Get the docker-compose file ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/docker/#step-1-get-the-docker-compose-file)

- [ Step 2: Run Hasura GraphQL Engine ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/docker/#step-2-run-hasura-graphql-engine)

- [ Step 3: Open the Hasura Console ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/docker/#step-3-open-the-hasura-console)

- [ Step 4: Add your SQL Server database as a source to Hasura ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/docker/#step-4-add-your-sql-server-database-as-a-source-to-hasura)

- [ Step 5: Option 1: Track existing tables ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/docker/#step-5-option-1-track-existing-tables)

- [ Step 5: Option 2: Create new tables ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/docker/#step-5-option-2-create-new-tables)

- [ Step 6: Try out a GraphQL query ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/docker/#step-6-try-out-a-graphql-query)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/docker/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)