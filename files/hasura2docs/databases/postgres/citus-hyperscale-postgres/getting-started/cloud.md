# Get Started with Hasura Cloud & Citus - Hyperscale

## Introduction​

### Step 1: Create an account on Hasura Cloud and create a new Hasura Project​

Navigate to[ cloud.hasura.io ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-cloud-hasura-io&tech=default&skip_onboarding=true),
and create a new Hasura Cloud account.

Once you create a project on Hasura Cloud, hit the "Launch Console" button to open the Hasura Console for your project.

Image: [ Connect new or existing database ](https://hasura.io/docs/assets/images/create-project-79b9d7bf1904f9467739017a6dd81666.png)

### Step 2: Add your Citus database as a source to Hasura​

In the `Data > Data Manager > Connect Existing Database` section on the Console, select `Citus` from the `Data Source Driver` dropdown and add the connection string directly or through an environment variable. As Citus speaks
the same protocol as Postgres, the connection string will start with `postgres://` , i.e, there is no difference between
Citus’s connection strings and Postgres’s connection strings.

Image: [ Add source ](https://hasura.io/docs/assets/images/connect-citus-db_console_2.10.1-f42236f1d073a208ec5bbd91663b5e90.png)

Once you add the database, you'll see your database pop up on the sidebar.

### Step 3: Track existing tables or create new tables​

If you have existing tables, head to the database page by clicking on the database name on the sidebar. You should see a
list of tables.

Track tables selectively or all of them so that Hasura can introspect the tables and create the corresponding GraphQL
schema.

If you have foreign keys, you'll also see suggested relationships. Again, you can choose to track them selectively or
all at once.

If you don't have existing tables, go ahead and add new tables and data and try out some queries, just like with a
regular Postgres database.

### Step 4: Try out a GraphQL query​

Head to the `API` tab in the Console and try running a GraphQL query! Use the explorer sidebar on GraphQL to get help in
creating a GraphQL query.

Image: [ Make GraphQL query ](https://hasura.io/docs/assets/images/api-explorer_step-4_console_2.10.1-9b6bd90b02f0f81c53b785a4e67053ba.png)

## Keep up to date​

Hasura supports queries, relationships, permissions, custom functions and mutations on Citus.

Please watch this space to get the latest docs on how you can try these features out via the Console or by manipulating
Metadata in JSON/YAML directly.

If you'd like to stay informed about the status of Citus support, subscribe to our newsletter and join our discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/cloud/#introduction)
    - [ Step 1: Create an account on Hasura Cloud and create a new Hasura Project ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/cloud/#step-1-create-an-account-on-hasura-cloud-and-create-a-new-hasura-project)

- [ Step 2: Add your Citus database as a source to Hasura ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/cloud/#step-2-add-your-citus-database-as-a-source-to-hasura)

- [ Step 3: Track existing tables or create new tables ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/cloud/#step-3-track-existing-tables-or-create-new-tables)

- [ Step 4: Try out a GraphQL query ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/cloud/#step-4-try-out-a-graphql-query)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/cloud/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)