# Get Started with Hasura (Docker) & CockroachDB

## Introduction​

### Pre-requisites​

- [ Docker ](https://docs.docker.com/install/)
- [ Docker Compose ](https://docs.docker.com/compose/install/)
- Optionally, an existing[ CockroachDB database ](https://www.cockroachlabs.com/get-started-cockroachdb/)


### Step 1: Get the docker-compose file​

Get the Hasura docker-compose file:

```
# in a new directory run
wget  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/docker-compose-cockroach/docker-compose.yaml
# or run
curl  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/docker-compose-cockroach/docker-compose.yaml -o docker-compose.yaml
```

### Step 2: Run Hasura GraphQL Engine and a CockroachDB instance​

The following command will run Hasura along with a Postgres database required for its functioning.

`$  docker  compose up -d`

Check that the containers are running:

```
$ docker ps
CONTAINER ID   IMAGE                 ... CREATED        STATUS          PORTS            ...
a6956d1492fd   hasura/graphql-engine ... 1 minute ago   Up 10 seconds   8080->8080/tcp   ...
f0931e41c608   cockroach             ... 1 minute ago   Up 10 seconds   26257->26257/tcp ...
42cd380d6ceb   postgres              ... 1 minute ago   Up 10 seconds   5432/tcp         ...
Please do note that you will see a Postgres database running, which is used by Hasura to store its configuration (Hasura Metadata).
```

### Step 3: Open the Hasura Console​

Head to `http://localhost:8080/console` to open the Hasura Console.

### Step 4: Add your CockroachDB database as a source to Hasura​

In the `Data > Data Manager > Connect Existing Database` section on the Console, select `CockroachDB` from the `Data Source Driver` dropdown and add the connection string directly or through an environment variable. As CockroachDB
speaks the same protocol as Postgres, the connection string will start with `postgres://` , i.e, there is no difference
between CockroachDB's connection strings and Postgres’s connection strings.

Image: [ Add source ](https://hasura.io/docs/assets/images/1-add-source-78a939411918774fe0a98fa59adf02e2.png)

If you're testing Hasura with CockroachDB running locally,[ read this guide ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-networking)on Docker networking if you're not sure
how to reach your CockroachDB database from the Hasura docker container on Linux, Mac or Windows.

Image: [ Add source added with docker-compose ](https://hasura.io/docs/assets/images/2-add-source-03517d4ad8d3a538a0835a4386339237.png)

This example uses the DB url `postgresql://root@cockroach:26257/hasura` , with the service name `cockroach` , as both
Hasura and the CockroachDB services are configured in the above-mentioned `docker-compose.yaml` file.

Once you add the database, you'll see your database pop up on the sidebar.

### Optional: Populate the CockroachDB database​

The following examples use `author` and `articles` tables, which can be set up as follows.

1. Connect to the CockroachDB container and start the `sql` command line tool:


`docker   exec  -it docker-compose-cockroach-cockroach-1 ./cockroach sql --insecure`

1. Once the command line tool has started, execute the following to set up example tables:


```
CREATE   TABLE  author (
    id  serial   PRIMARY   KEY ,
    name  text   UNIQUE ,
     "createdAt"   timestamp
) ;
CREATE   TABLE  article  (
    id  SERIAL   PRIMARY   KEY ,
    title  TEXT ,
    content  TEXT ,
    author_id  INTEGER   REFERENCES  author ( id ) ,
    is_published  BOOLEAN
) ;
-- Inserting sequential ids for demo purposes
-- See https://www.cockroachlabs.com/docs/v22.2/serial.html
INSERT   INTO
    author  ( id ,  name ,   "createdAt" )
VALUES
     ( 1 ,   'Author 3' ,   '2017-09-21T09:39:44' ) ,
     ( 2 ,   'Author 4' ,   '2017-09-21T09:50:44' ) ;
INSERT   INTO
    article  ( title ,  content ,  author_id ,  is_published )
VALUES
     (
         'Article 1' ,
         'Sample article content 1' ,
         1 ,
         false
     ) ,
     (
         'Article 2' ,
         'Sample article content 2' ,
         1 ,
         TRUE
     ) ,
     (
         'Article 3' ,
         'Sample article content 3' ,
         2 ,
         TRUE
     ) ;
```

### Step 5: Track existing tables or create new tables​

If you have existing tables, head to the database page by clicking on the database name on the sidebar. You should see a
list of tables.

Track tables selectively or all of them so that Hasura can introspect the tables and create the corresponding GraphQL
schema.

Image: [ Track tables ](https://hasura.io/docs/assets/images/4-track-tables-c9e8ddb88c5018cde462902f03ac5ca2.png)

If you have foreign keys, you'll also see suggested relationships. Again, you can choose to track them selectively or
all at once.

Image: [ Track foreign-key relationships ](https://hasura.io/docs/assets/images/5-track-rels-5c91f10b7840ad85deb88d56a00f5926.png)

If you don't have existing tables, go ahead and add new tables and data and try out some queries, just like with a
regular Postgres database.

Image: [ Add a new table ](https://hasura.io/docs/assets/images/6-add-tables-905abba9bb1feb68859b368a3f152570.png)

### Step 6: Try out a GraphQL query​

Head to the `API` tab in the Console and try running a GraphQL query! Use the explorer sidebar on GraphQL to get help in
creating a GraphQL query.

Image: [ Make GraphQL query ](https://hasura.io/docs/assets/images/7-make-graphql-query-2de8b8336e323c7f7882ba5b0de061c8.png)

## Keep up to date​

Hasura currently supports[ queries ](https://hasura.io/docs/latest/queries/postgres/index/),[ relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/), and[ mutations ](https://hasura.io/docs/latest/mutations/postgres/index/)on
CockroachDB.

Please refer to the[ Postgres docs ](https://hasura.io/docs/latest/queries/postgres/index/)on how you can try these features out via the Console
or by manipulating Metadata in JSON/YAML directly.

If you'd like to stay informed about the status of CockroachDB support, subscribe to our newsletter and join our
discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/docker/#introduction)
    - [ Pre-requisites ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/docker/#pre-requisites)

- [ Step 1: Get the docker-compose file ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/docker/#step-1-get-the-docker-compose-file)

- [ Step 2: Run Hasura GraphQL Engine and a CockroachDB instance ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/docker/#step-2-run-hasura-graphql-engine-and-a-cockroachdb-instance)

- [ Step 3: Open the Hasura Console ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/docker/#step-3-open-the-hasura-console)

- [ Step 4: Add your CockroachDB database as a source to Hasura ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/docker/#step-4-add-your-cockroachdb-database-as-a-source-to-hasura)

- [ Optional: Populate the CockroachDB database ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/docker/#optional-populate-the-cockroachdb-database)

- [ Step 5: Track existing tables or create new tables ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/docker/#step-5-track-existing-tables-or-create-new-tables)

- [ Step 6: Try out a GraphQL query ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/docker/#step-6-try-out-a-graphql-query)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/docker/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)