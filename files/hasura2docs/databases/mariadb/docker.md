# Getting Started with Hasura and MariaDB in Docker

## Introduction​

This guide will help you get set up with the[ Enterprise Edition ](https://hasura.io/docs/latest/enterprise/overview/)of Hasura GraphQL Engine
with our MariaDB integration using Docker Compose. This is the easiest way to set up Hasura Enterprise Edition and the
MariaDB GraphQL Data Connector.

Supported versions:

1. Hasura GraphQL Engine `v2.24.0` onwards
2. Hasura supports most databases with standard implementations of **MariaDB 10.5 and higher** including: Amazon RDS,
Amazon Aurora, Digital Ocean and SkySQL.


Supported features

Hasura currently supports queries, mutations (INSERT, UPDATE, DELETE), table relationships, remote relationships and
permissions on MariaDB.

Note that Hasura doesn't yet support the ability to modify the database schema for MariaDB, so the database you connect
to should already contain tables and data. You should also ideally have access to it outside of Hasura to modify the
schema.

## Deploying Hasura Enterprise with Docker​

### Prerequisites​

This tutorial assumes that the following prerequisites have been met:

- You have[ Docker ](https://docs.docker.com/install/)and[ Docker Compose ](https://docs.docker.com/compose/install/)working on your machine.
- You have access to a MariaDB database for which you would like to create an API.


### Step 1: Get the Docker Compose file​

The[ install manifests repo ](https://github.com/hasura/graphql-engine/tree/master/install-manifests)contains all
installation manifests required to deploy Hasura anywhere. The Docker Compose manifest also contains a Postgres database
in order to store the Hasura metadata and a Redis instance for caching.

```
# in a new directory run
wget  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/enterprise/mariadb/docker-compose.yaml
# or run
curl  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/enterprise/mariadb/docker-compose.yaml -o docker-compose.yaml
```

### Step 2: Set the Hasura Enterprise Edition license key and the admin secret​

Edit the downloaded `docker-compose.yaml` and set the license key and admin secret. If you've been provided a license
key by the Hasura team, you can enter it according to the directions below.

```
---
graphql-engine :
   image :  hasura/graphql - engine : v2.24.0
   environment :
     HASURA_GRAPHQL_EE_LICENSE_KEY :  <license key >
     HASURA_GRAPHQL_ADMIN_SECRET :  <your secretkey >
```

An[ admin secret key ](https://hasura.io/docs/latest/deployment/securing-graphql-endpoint/)is required to make sure that your GraphQL endpoint and
the Hasura Console are not publicly accessible.

I don't have a license key

If you don't already have a license key and are interested in trying out Hasura Enterprise Edition with MariaDB, you can
start a free 30-day trial. Leave the `HASURA_GRAPHQL_EE_LICENSE_KEY` environment variable commented out we'll return to
this in Step 4.

Secure the admin secret

The `HASURA_GRAPHQL_ADMIN_SECRET` should never be passed from the client to the Hasura GraphQL Engine as it would give
the client full admin rights to your Hasura instance. See[ Authentication & Authorization ](https://hasura.io/docs/latest/auth/overview/)for
information on setting up auth in Hasura.

### Step 3: Run Hasura GraphQL Engine​

The following command will create and run the containers in the Docker Compose manifest:

`docker  compose up -d`

Check that the containers are running:

```
docker   ps
CONTAINER ID IMAGE                               .. . CREATED STATUS PORTS           .. .
097f58433a2b hasura/graphql-engine               .. . 1m ago  Up 1m   8080 - > 8080 /tcp  .. .
b0b1aac0508d postgres                            .. . 1m ago  Up 1m   5432 /tcp  .. .
3a29aa348999 redis:7                             .. . 1m ago  Up 1m   6379 /tcp  .. .
7b5b2ee70ece hasura/graphql-data-connector       .. . 1m ago  Up 1m   5005 /tcp  ..
```

### Step 4: Load the Hasura Console​

Open the Hasura Console by navigating to `http://localhost:8080/console` . You will need to input your admin secret key
as set in your Docker Compose file to log in.

30-day free trial

If you don't already have a license key, you can start a 30-day free trial by clicking the `ENTERPRISE` button in the
top navigation. You can read more details[ here ](https://hasura.io/docs/latest/enterprise/try-hasura-enterprise-edition/).

Image: [ Enterprise Edition Trial register button ](https://hasura.io/docs/assets/images/Trials_Register_Button-21f7c94a1f16bc85ed93899268a16ef2.png)

### Step 5: Connect to a MariaDB database​

From the Console, click the `Data` tab:

Image: [ Connect database ](https://hasura.io/docs/assets/images/connect-db-console-d08a940e3d5f1f710ba1c83383920b77.png)

Select the MariaDB data source driver, enter in a display name for the database and set the JDBC Connection URL for your
MariaDB instance.

The JDBC connection URL should look like this:

`jdbc : mariadb : //<hostname > : <port > /<database name > ? user=<username > &password=<password>`

For example:

```
jdbc : mariadb : //myhost.mycompany.com/mariadb ? user=abc &password=pqr    # assuming the default port 3306
jdbc : mariadb : //localhost : 4533/mariadb ? user=abc &password=pqr          # assuming MariaDB is running on port 4533
```

For more information see[ MariaDB Connection URL syntax ](https://mariadb.com/kb/en/about-mariadb-connector-j/#using-the-driver).

Click `Connect Database` .

Ensure your password escapes special characters

Due to the potential variations in drivers, it's crucial to escape special characters used in the password of the
connection string. These include `{ } % & #` . To escape a character, use the appropriate escape sequence based on your
database's driver's documentation.

### Step 6: Track tables and run GraphQL API queries​

Now that you have successfully connected your MariaDB database to Hasura, you can track tables and use Hasura to
automatically build a full-featured GraphQL API for it.

### Step 7 (optional): Use managed PostgreSQL and Redis instances​

The Hasura Enterprise Edition Docker compose files come with containerized open-source versions of PostgreSQL and Redis.

We highly recommend using managed PostgreSQL and Redis instances especially when running in production.

To switch to using your PostgreSQL or Redis instances, set the following environment variables:

`HASURA_GRAPHQL_METADATA_DATABASE_URL HASURA_GRAPHQL_REDIS_URL HASURA_GRAPHQL_RATE_LIMIT_REDIS_URL`

For example:

```
---
graphql-engine :
   image :  hasura/graphql - engine : v2.24.0
   environment :
     HASURA_GRAPHQL_METADATA_DATABASE_URL :  postgres : //postgres : postgrespassword@postgres : 5432/postgres
     HASURA_GRAPHQL_REDIS_URL :   'redis://redis:6379'
     HASURA_GRAPHQL_RATE_LIMIT_REDIS_URL :   'redis://redis:6379'
```

### Resources​

- [ Hasura GraphQL Engine logs ](https://hasura.io/docs/latest/deployment/logging/)for more details on log types.


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/mariadb/docker/#introduction)
- [ Deploying Hasura Enterprise with Docker ](https://hasura.io/docs/latest/databases/mariadb/docker/#deploying-hasura-enterprise-with-docker)
    - [ Prerequisites ](https://hasura.io/docs/latest/databases/mariadb/docker/#prerequisites)

- [ Step 1: Get the Docker Compose file ](https://hasura.io/docs/latest/databases/mariadb/docker/#step-1-get-the-docker-compose-file)

- [ Step 2: Set the Hasura Enterprise Edition license key and the admin secret ](https://hasura.io/docs/latest/databases/mariadb/docker/#step-2-set-the-hasura-enterprise-edition-license-key-and-the-admin-secret)

- [ Step 3: Run Hasura GraphQL Engine ](https://hasura.io/docs/latest/databases/mariadb/docker/#step-3-run-hasura-graphql-engine)

- [ Step 4: Load the Hasura Console ](https://hasura.io/docs/latest/databases/mariadb/docker/#step-4-load-the-hasura-console)

- [ Step 5: Connect to a MariaDB database ](https://hasura.io/docs/latest/databases/mariadb/docker/#step-5-connect-to-a-mariadb-database)

- [ Step 6: Track tables and run GraphQL API queries ](https://hasura.io/docs/latest/databases/mariadb/docker/#step-6-track-tables-and-run-graphql-api-queries)

- [ Step 7 (optional): Use managed PostgreSQL and Redis instances ](https://hasura.io/docs/latest/databases/mariadb/docker/#step-7-optional-use-managed-postgresql-and-redis-instances)

- [ Resources ](https://hasura.io/docs/latest/databases/mariadb/docker/#resources)


Image: [ hasura-webinar ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683628053/main-web/Group_11457_vceb9f.png)

### Ship faster with low-code APIs on MySQL, MariaDB, and Oracle

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)