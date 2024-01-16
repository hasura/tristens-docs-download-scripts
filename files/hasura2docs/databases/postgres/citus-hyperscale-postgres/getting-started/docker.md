# Get Started with Docker (Hasura & Citus - Hyperscale)

## Introduction​

### Pre-requisites​

- [ Docker ](https://docs.docker.com/install/)
- [ Docker Compose ](https://docs.docker.com/compose/install/)
- An existing Citus database


### Step 1: Get the docker-compose file​

Get the Hasura docker-compose file:

```
# in a new directory run
wget  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/docker-compose/docker-compose.yaml
# or run
curl  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/docker-compose/docker-compose.yaml -o docker-compose.yaml
```

### Step 2: Run Hasura GraphQL Engine​

The following command will run Hasura along with a Postgres database required for its functioning.

`$  docker  compose up -d`

Check if the containers are running:

```
$  docker   ps
CONTAINER ID IMAGE                  .. . CREATED STATUS PORTS           .. .
097f58433a2b hasura/graphql-engine  .. . 1m ago  Up 1m   8080 - > 8080 /tcp  .. .
b0b1aac0508d postgres               .. . 1m ago  Up 1m   5432 /tcp        .. .
Please  do  note that you will see a Postgres database running,  which  is used by Hasura to store its configuration  ( Hasura Metadata ) .
```

### Step 3: Open the Hasura Console​

Head to `http://localhost:8080/console` to open the Hasura Console.

### Step 4: Add your Citus database as a source to Hasura​

In the `Data > Data Manager > Connect Existing Database` section on the Console, select `Citus` from the `Data Source Driver` dropdown and add the connection string directly or through an environment variable. As Citus speaks
the same protocol as Postgres, the connection string will start with `postgres://` , i.e, there is no difference between
Citus’s connection strings and Postgres’s connection strings.

Image: [ Add source ](https://hasura.io/docs/assets/images/connect-citus-db_console_2.10.1-f42236f1d073a208ec5bbd91663b5e90.png)

If you're testing Hasura with Citus running locally,[ read this guide ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-networking)on Docker networking in case you're not
sure how to make sure that your Citus database is reachable from the Hasura docker container on Linux, Mac or Windows.

Once you add the database, you'll see your database pop up on the sidebar.

### Step 5: Track existing tables or create new tables​

If you have existing tables, head to the database page by clicking on the database name on the sidebar. You should see a
list of tables.

Track tables selectively or all of them so that Hasura can introspect the tables and create the corresponding GraphQL
schema.

If you have foreign keys, you'll also see suggested relationships. Again, you can choose to track them selectively or
all at once.

If you don't have existing tables, go ahead and add new tables and data and try out some queries, just like with a
regular Postgres database.

### Step 6: Try out a GraphQL query​

Head to the `API` tab in the Console and try running a GraphQL query! Use the explorer sidebar on GraphQL to get help in
creating a GraphQL query.

Image: [ Make GraphQL query ](https://hasura.io/docs/assets/images/api-explorer_step-4_console_2.10.1-9b6bd90b02f0f81c53b785a4e67053ba.png)

## Keep up to date​

Hasura supports queries, subscriptions, relationships and permissions on Citus - Hyperscale.

Please watch this space to get the latest docs on how you can try these features out via the Console or by manipulating
Metadata in JSON/YAML directly.

If you'd like to stay informed about the status of Citus support, subscribe to our newsletter and join our discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/docker/#introduction)
    - [ Pre-requisites ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/docker/#pre-requisites)

- [ Step 1: Get the docker-compose file ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/docker/#step-1-get-the-docker-compose-file)

- [ Step 2: Run Hasura GraphQL Engine ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/docker/#step-2-run-hasura-graphql-engine)

- [ Step 3: Open the Hasura Console ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/docker/#step-3-open-the-hasura-console)

- [ Step 4: Add your Citus database as a source to Hasura ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/docker/#step-4-add-your-citus-database-as-a-source-to-hasura)

- [ Step 5: Track existing tables or create new tables ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/docker/#step-5-track-existing-tables-or-create-new-tables)

- [ Step 6: Try out a GraphQL query ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/docker/#step-6-try-out-a-graphql-query)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/postgres/citus-hyperscale-postgres/getting-started/docker/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)