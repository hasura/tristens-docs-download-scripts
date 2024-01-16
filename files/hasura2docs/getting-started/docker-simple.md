# Quickstart with Docker

## Introduction​

This guide will help you get up and running quickly with the Hasura GraphQL Engine and a Postgres database running as
Docker containers using Docker Compose.

## Prerequisites​

- You have[ Docker ](https://docs.docker.com/install/)and[ Docker Compose version 2.0 or higher ](https://docs.docker.com/compose/install/)working on your machine.


## Step 1: Get the Compose file & start the containers​

Get the Compose file from our repo. If you're using curl, run this command in a new directory:

`curl  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/docker-compose/docker-compose.yaml -o docker-compose.yml`

If you're using wget, run this command in a new directory:

`wget  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/docker-compose/docker-compose.yaml`

Then, run the following command to start both the Hasura GraphQL Engine and the Postgres database in Docker containers:

`docker  compose up -d`

## Step 2: Connect a database​

Hasura ships with a Postgres database

The docker-compose file we used in the previous step starts a Postgres database in a Docker container. **Hasura relies
on this database to store its metadata** , but this can also be used to store your application data.

If you'd like to connect another type of database for storing application data, check out our list of[ supported databases ](https://hasura.io/docs/latest/databases/overview/).

Open the Hasura Console by navigating to `http://localhost:8080/console` . From the Console, click the `Data` tab:

Image: [ Connect database ](https://hasura.io/docs/assets/images/connect-db-console-d08a940e3d5f1f710ba1c83383920b77.png)

Select the `Environment Variable` option and enter `PG_DATABASE_URL` as the environment variable name:

Image: [ Enter URL for existing database ](https://hasura.io/docs/assets/images/connect-db-env-var-57c398c34bae12043547e0ee1596ec8e.png)

Click `Connect Database` .

## Step 3: Try out Hasura​

### Create a table and insert some demo data​

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

Note: The Hasura GraphQL Engine collects anonymous telemetry to understand usage and provide the best experience. Read
more[ here ](https://hasura.io/docs/latest/policies/telemetry/)on what data is collected and the procedure to opt out.

## Recap​

What did we just do? Well, you just created a powerful, full-featured GraphQL API in less than five minutes. 🎉

We started two Docker containers - one for the Hasura GraphQL Engine and one for the Postgres database. In this example,
our Postgres database also contains the[ Hasura Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/); which is how
Hasura records its information about the GraphQL schema, the relationships between tables, and much more. Finally, we
connected our Postgres database to the Hasura GraphQL Engine, which allowed Hasura Engine to automatically create a full
CRUD GraphQL API for our Postgres database which we could then easily query, mutate and subscribe to.

Important: Set up the Hasura CLI

The Hasura CLI is a powerful tool that helps you manage your Hasura project and is recommended for the majority of
development workflows. It helps track and manage your[ Hasura Metadata and Migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/overview/)and commit them to version control and allows
you to quickly move between environments like development and production.

### Database operations​

We omitted the CLI steps in this guide for the sake of simplicity and brevity, but in a typical new project, you would
always include the CLI setup steps.

Every developer working with Hasura should have the[ Hasura CLI installed ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/). You can
quickly get up and running with a new project[ using the CLI quickstart ](https://hasura.io/docs/latest/hasura-cli/quickstart/)and learn more by
checking out our[ Advanced Hasura course ](https://hasura.io/learn/graphql/hasura-advanced/introduction/).

## Next steps​

- If you're interested in taking a deep dive into Hasura, check out our hands-on[ 30-Minute Hasura Basics Tutorial ](https://hasura.io/learn/graphql/hasura/introduction/).
- There are several options for the implementation of business logic, depending on your use case.
    - [ Actions ](https://hasura.io/docs/latest/actions/overview/): Actions can be used if you'd like to extend your GraphQL schema by integrating
with a REST endpoint.

- [ Remote Schemas ](https://hasura.io/docs/latest/remote-schemas/overview/): If you have an existing GraphQL server or if you're comfortable with
implementing one, you can use Remote Schemas.

- [ Event Triggers ](https://hasura.io/docs/latest/event-triggers/overview/): To trigger a serverless function based on a database event, use
Event Triggers.

- [ Scheduled Triggers ](https://hasura.io/docs/latest/scheduled-triggers/overview/): Scheduled Triggers are used to execute custom business logic
at specific points in time.
- If you're new to database modeling, check out these guides:
    - [ Database modeling ](https://hasura.io/docs/latest/schema/postgres/index/): Learn how to model your database schema, as well as how to extend
it.

- [ Querying data ](https://hasura.io/docs/latest/queries/postgres/index/): Use GraphQL queries to query data from your GraphQL API.

- [ Inserting data ](https://hasura.io/docs/latest/mutations/postgres/index/): Use GraphQL mutations to insert data into your GraphQL API.
- **Security Announcements** : Join the[ Hasura Security Announcements ](https://groups.google.com/forum/#!forum/hasura-security-announce)group for emails
about security announcements.
- We release new features every month. Sign up for our newsletter by using the link below. We send newsletters only once
a month.[ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/).


If you're interested in taking a deep dive into Hasura, check out our hands-on[ 30-Minute Hasura Basics Tutorial ](https://hasura.io/learn/graphql/hasura/introduction/).

There are several options for the implementation of business logic, depending on your use case.

If you're new to database modeling, check out these guides:

 **Security Announcements** : Join the[ Hasura Security Announcements ](https://groups.google.com/forum/#!forum/hasura-security-announce)group for emails
about security announcements.

We release new features every month. Sign up for our newsletter by using the link below. We send newsletters only once
a month.[ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/getting-started/docker-simple/#introduction)
- [ Prerequisites ](https://hasura.io/docs/latest/getting-started/docker-simple/#prerequisites)
- [ Step 1: Get the Compose file & start the containers ](https://hasura.io/docs/latest/getting-started/docker-simple/#step-1-get-the-compose-file--start-the-containers)
- [ Step 2: Connect a database ](https://hasura.io/docs/latest/getting-started/docker-simple/#step-2-connect-a-database)
- [ Step 3: Try out Hasura ](https://hasura.io/docs/latest/getting-started/docker-simple/#step-3-try-out-hasura)
    - [ Create a table and insert some demo data ](https://hasura.io/docs/latest/getting-started/docker-simple/#create-a-table-and-insert-some-demo-data)

- [ Try out a query ](https://hasura.io/docs/latest/getting-started/docker-simple/#try-out-a-query)
- [ Recap ](https://hasura.io/docs/latest/getting-started/docker-simple/#recap)
- [ Next steps ](https://hasura.io/docs/latest/getting-started/docker-simple/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)