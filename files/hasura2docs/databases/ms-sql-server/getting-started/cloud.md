# Get Started with Hasura Cloud & MS SQL Server

## Introduction​

### Step 1: Create an account on Hasura Cloud and create a new Hasura Project​

Navigate to[ cloud.hasura.io ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-cloud-hasura-io&tech=default&skip_onboarding=true),
and create a new Hasura Cloud account.

Once you create a project on Hasura Cloud, hit the "Launch Console" button to open the Hasura Console for your project.

Image: [ Connect new or existing database ](https://hasura.io/docs/assets/images/create-project-79b9d7bf1904f9467739017a6dd81666.png)

### Step 2: Add your SQL Server database as a source to Hasura​

Head to the `Data > Manage databases` section on the Console to add your MS SQL Server as a source to Hasura. You'll
need your ODBC connection string. Make sure that your ODBC driver is set to version 17.

Here's an example of what your connection strings might look like with a SQL server database on Azure SQL Serverless:

`Driver={ODBC Driver 18 for SQL Server};Server=tcp:hasura-test.database.windows.net,1433;Database=db-name;Uid=username;Pwd=password;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;`

Make sure your SQL server database is reachable by Hasura Cloud:

1. Allow public connections or[ whitelist the Hasura Cloud IP ](https://hasura.io/docs/latest/hasura-cloud/projects/create/#cloud-projects-create-allow-nat-ip)on your SQL
Server firewall: This is good for testing and will allow you to try Hasura out with your database quickly!
2. VPC peering: VPC peering and private network access is available on Hasura Cloud paid tiers: Recommended for
production. Get in touch with us if you'd like to try this out against your existing databases!


Image: [ Manage databases ](https://hasura.io/docs/assets/images/manage-databases_console_2.10.1-551bbcec8cdf5510bfe4b40ea977df5b.png)

Image: [ Add source ](https://hasura.io/docs/assets/images/connect-ms-sql-db_console_2.10.1-71fa535096dfffbad524c4431f3ebdd7.png)

Once you add the database, you'll see your database pop up on the sidebar.

### Step 3: Option 1: Track existing tables​

If you have existing tables, head to the database page by clicking on the database name on the sidebar. You should see a
list of tables.

Image: [ Manage my-db ](https://hasura.io/docs/assets/images/manage-db_step-3_console_2.10.1-21825c035d2944e8c56386e7de0dd36c.png)

Track tables selectively or all of them so that Hasura can introspect the tables and create the corresponding GraphQL
schema.

Image: [ Track tables ](https://hasura.io/docs/assets/images/track-tables_step-3_console_2.10.1-4d716ebfd2cd99dc71e00a3d20fd4d28.png)

If you have foreign keys, you'll also see suggested relationships. Again, you can choose to track them selectively or
all at once.

Image: [ Track relationships ](https://hasura.io/docs/assets/images/track-foreign-key-rel_step-3_console_2.10.1-87f74f01fbe37da0d73c423ccb237269.png)

### Step 3: Option 2: Create new tables​

If you don't have existing tables, head to the Run SQL window to run SQL against your SQL Server database and create
tables or hit the Create Table button to create a table.

If you're running raw SQL queries to create your tables, Don't forget to check "track metadata" at the bottom of the Run
SQL window to make sure Hasura tracks your new database objects in its GraphQL schema.

Image: [ Run SQL to create table ](https://hasura.io/docs/assets/images/run-sql_step-3_console_2.10.1-86819d4f3827c3224436def58bc95181.png)

### Step 4: Try out a GraphQL query​

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

- [ Introduction ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/cloud/#introduction)
    - [ Step 1: Create an account on Hasura Cloud and create a new Hasura Project ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/cloud/#step-1-create-an-account-on-hasura-cloud-and-create-a-new-hasura-project)

- [ Step 2: Add your SQL Server database as a source to Hasura ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/cloud/#step-2-add-your-sql-server-database-as-a-source-to-hasura)

- [ Step 3: Option 1: Track existing tables ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/cloud/#step-3-option-1-track-existing-tables)

- [ Step 3: Option 2: Create new tables ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/cloud/#step-3-option-2-create-new-tables)

- [ Step 4: Try out a GraphQL query ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/cloud/#step-4-try-out-a-graphql-query)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/ms-sql-server/getting-started/cloud/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)