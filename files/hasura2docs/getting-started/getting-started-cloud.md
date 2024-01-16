# Quickstart with Hasura Cloud

## Introduction​

Hasura Cloud is a powerful tool that can work with a wide variety of databases. If you have a preferred database, check
out our[ supported databases ](https://hasura.io/docs/latest/databases/overview/)for details on how to connect.

If you're just getting started with Hasura, you can also try out our free Neon Postgres database. We'll walk you through
the setup process in this guide, so you can get started quickly and easily.

Not sure what you want to build?!

If you're not sure what you want to build with Hasura, check out our[ sample use cases ](https://hasura.io/docs/latest/getting-started/use-case/overview/)for inspiration, and we'll walk you through the setup
step-by-step!

## Step 1: Create an account​

Navigate to[ cloud.hasura.io ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-cloud-hasura-io&tech=default&skip_onboarding=true),
and create a new Hasura Cloud account.

## Step 2: Create a project​

On creating a new account, Hasura Cloud automatically creates an initial project for you.

Click `Launch Console` to open the Hasura Console in your browser.

Image: [ Connect new or existing database ](https://hasura.io/docs/assets/images/cloud-initial-project-launch-console-209b8e43a2b99ca84d28c6ececec1a8e.png)

If you already have an account, you can create a new project by clicking the `New Project` link on the[ Projects ](https://cloud.hasura.io/projects)page.

Regardless of tier, you have the choice of either Amazon Web Services (AWS) or Google Cloud Platform (GCP) as hosting
providers.

Image: [ Choose either AWS or GCP ](https://hasura.io/docs/assets/images/getting-started-cloud-aws-and-gcp-emphasis-0d3a39a43d2ef041d075086b9708df6a.png)

Make your selection and then click `Create Free Project` :

Image: [ Create project ](https://hasura.io/docs/assets/images/getting-started-cloud-create-project-9e08e17020f324f6226142006df179f6.png)

## Step 3: Connect a database​

Hit the `Launch console` button to open the Hasura Console and navigate to `Data -> Manage -> Connect Database` :

Image: [ Connect database ](https://hasura.io/docs/assets/images/connect-db-console-d08a940e3d5f1f710ba1c83383920b77.png)

- To try out quickly with a new Postgres database, choose `Create New Database` .
- To use an[ existing database ](https://hasura.io/docs/latest/databases/overview/), choose `Connect existing database` .


Image: [ DB setup ](https://hasura.io/docs/assets/images/db-setup-d68b57e03d089832105feb9a7ab8d177.png)

### Option 3.1: Create and connect a new database​

If you chose `Create New Database` :

Click on `Connect Neon Database` to create and connect a new Postgres database to your Hasura Project.

Image: [ Connect Neon database ](https://hasura.io/docs/assets/images/connect_neon_database-20d34cdbe67ad3bdd7dab65e2f0b19cb.png)

### Option 3.2: Connect an existing database​

If you chose `Connect existing database` :

- Give the database a name, say `default`
- Choose the database type from the list of[ supported databases ](https://hasura.io/docs/latest/databases/overview/#supported-databases)
- Enter your database connection details
- Click `Connect Database` .


Image: [ Enter URL for existing database ](https://hasura.io/docs/assets/images/connect-db-cloud-aa46779320727922ac336e595a0b2200.png)

Check out[ this section ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip)for other steps required to ensure
connectivity to your database from Hasura Cloud if needed.

## Step 4: Try out Hasura​

### Create a table​

On the Hasura Console, navigate to `Data -> Create table` and create a sample table called `profiles` with the following
columns:

```
profiles  (
  id  SERIAL   PRIMARY   KEY ,   -- serial -> auto-incrementing integer
  name  TEXT
)
```

Image: [ Create a table ](https://hasura.io/docs/assets/images/create-profile-table-f93963eda2987dc06c5d2a9377a37f8a.png)

Now, insert some sample data into the table using the `Insert Row` tab of the `profiles` table.

### Try out a query​

Head to the `API` tab in the Console and try running the following query:

```
query   {
   profiles   {
     id
     name
   }
}
```

You'll see that you get all the inserted data!

Image: [ Try out a query ](https://hasura.io/docs/assets/images/profile-query-5be8a917069f505b215cbf87ea953dfd.png)

## Next steps​

### Learn tutorial​

For a full hands-on tour of Hasura, check out our[ 30-Minute Hasura Basics Tutorial ](https://hasura.io/learn/graphql/hasura/introduction/).

### Database operations​

- [ Databases overview ](https://hasura.io/docs/latest/databases/overview/)
- [ Database modeling ](https://hasura.io/docs/latest/schema/postgres/index/): Learn how to model your database schema, as well as how to extend it.
- [ Querying data ](https://hasura.io/docs/latest/queries/postgres/index/): Use GraphQL queries to query data from your GraphQL API.
- [ Inserting data ](https://hasura.io/docs/latest/mutations/postgres/index/): Use GraphQL mutations to insert data into your GraphQL API.
- [ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#managed-pg-permissions)


### Business logic​

There are several options for the implementation of business logic, depending on your use case.

- [ Actions ](https://hasura.io/docs/latest/actions/overview/): Actions can be used if you'd like to extend your GraphQL schema by integrating with
a REST endpoint.
- [ Remote Schemas ](https://hasura.io/docs/latest/remote-schemas/overview/): If you have an existing GraphQL server or if you're comfortable with
implementing one, you can use Remote Schemas.
- [ Event Triggers ](https://hasura.io/docs/latest/event-triggers/overview/): To trigger a serverless function based on a database event, use event
triggers.
- [ Scheduled Triggers ](https://hasura.io/docs/latest/scheduled-triggers/overview/): Scheduled Triggers are used to execute custom business logic
at specific points in time.


### Manage Hasura Cloud project​

You can click the gear icon in the Hasura Cloud dashboard to manage your Hasura Cloud project (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).

Image: [ Project actions ](https://hasura.io/docs/assets/images/project-manage-5b37a214a39b39b6287136606da021c4.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#introduction)
- [ Step 1: Create an account ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#step-1-create-an-account)
- [ Step 2: Create a project ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#step-2-create-a-project)
- [ Step 3: Connect a database ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#cloud-connect-db)
    - [ Option 3.1: Create and connect a new database ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#create-new-db-with-cloud)

- [ Option 3.2: Connect an existing database ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#option-32-connect-an-existing-database)
- [ Step 4: Try out Hasura ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#step-4-try-out-hasura)
    - [ Create a table ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#create-a-table)

- [ Try out a query ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#try-out-a-query)
- [ Next steps ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#next-steps)
    - [ Learn tutorial ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#learn-tutorial)

- [ Database operations ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#database-operations)

- [ Business logic ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#business-logic)

- [ Manage Hasura Cloud project ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/#manage-hasura-cloud-project)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)