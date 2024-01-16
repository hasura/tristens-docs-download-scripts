# Connect Databases to Hasura GraphQL Engine

## Introduction​

You can quickly and easily connect a new, existing, or demo database to Hasura GraphQL Engine using the Hasura Console,
CLI or API. You can also connect to multiple databases in order to build a unified GraphQL API.

On-the-fly connecting and removing of databases

In versions `v2.0.0` and above, databases can be connected and removed dynamically without having to restart the Hasura
Engine instance.

Connection methods

You can connect to databases by using environment variables, the raw connection string or connection parameters. It is
recommended to use environment variables for better security *(as connection details set via a string will be exposed as
part of the Hasura Metadata)* as well as to allow configuring different databases in different environments *(like
staging or production)* easily.

## On Hasura Cloud​

- Console
- CLI
- API


Hasura Cloud does not host databases, but does provide integrations with which you can connect databases from many 3rd
party managed cloud providers. Check out the[ list of supported databases ](https://hasura.io/docs/latest/databases/overview/).

If you have[ created your project with Hasura Cloud ](https://hasura.io/docs/latest/hasura-cloud/projects/create/), click on the `Launch Console` button to open the Hasura Console in your browser.

Image: [ database setup with new database ](https://hasura.io/docs/assets/images/project_launch-console_2-17-0-f758e64fb9f3e2aa3e82b1d15cd9996c.png)

On the Hasura Console, navigate to `Data -> Manage -> Connect Database` 

### Option 1: Create and connect a new database​

To get started quickly with a Postgres database, choose `Create New Database` :

Image: [ database setup with existing database ](https://hasura.io/docs/assets/images/create-database-neon-2.15-db81649da56f37336859d0a425272740.png)

Click on `Connect Neon Database` to create and connect a new Postgres database to your Hasura Project.

Image: [ Connect Neon database ](https://hasura.io/docs/assets/images/connect_neon_database-20d34cdbe67ad3bdd7dab65e2f0b19cb.png)

### Option 2: Connect an existing database​

To use an existing database, choose `Connect existing database` .

- Give the database a name, say `default`
- Choose the database type from the list of[ supported databases ](https://hasura.io/docs/latest/databases/overview/#supported-databases)
- Enter your database connection details
- Click `Connect Database`


Image: [ Enter URL for existing database ](https://hasura.io/docs/assets/images/connect-db-cloud-aa46779320727922ac336e595a0b2200.png)

Check out[ this section ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#cloud-projects-create-allow-nat-ip)for other steps
required to ensure connectivity to your database from Hasura Cloud if needed.

In your `config v3` project, head to the `/metadata/databases/databases.yaml` file and add the database configuration as
below. If you're using the `HASURA_GRAPHQL_DATABASE_URL` environment variable then the database will get automatically
added and named default.

```
-   name :  <db_name >
   kind :  postgres
   configuration :
     connection_info :
       database_url :
         from_env :  <DB_URL_ENV_VAR >
       pool_settings :
         idle_timeout :   180
         max_connections :   50
         retries :   1
   tables :   [ ]
   functions :   [ ]
```

Apply the Metadata by running:

`hasura metadata apply`

Depending on the type of database, you can add a database using the[ sources Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/source/).

For example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_add_source" ,
   "args" :   {
     "name" :   "<db_name>" ,
     "configuration" :   {
       "connection_info" :   {
         "database_url" :   {
           "from_env" :   "<DB_URL_ENV_VAR>"
         } ,
         "pool_settings" :   {
           "retries" :   1 ,
           "idle_timeout" :   180 ,
           "max_connections" :   50
         }
       }
     }
   }
}
```

### Allow connections from the Hasura Cloud IP​

When using Hasura Cloud, you may need to adjust your connection settings of your database provider to allow connections
from the Hasura Cloud IP address.

You can copy the IP address of your Hasura Engine instance from the copy icon in the `Hasura Cloud IP` field on the
Project's details view which you can shortcut to by clicking on your Project name in the Console.

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/cloud-console_shortcut-to-project-settings_2-17-0-632cea60b50d83ca2e78d9027313b1c5.png)

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/project-general-ip-address_console_2.12-26f7afb546dea5ecf30bd2ff0f1da564.png)

## On Hasura deployed via Docker​

- Console
- CLI
- API


If you've[ spun up the Hasura Engine with Docker ](https://hasura.io/docs/latest/getting-started/docker-simple/), you can access the Hasura Console
by accessing it in a browser at the URL of your Hasura Engine instance, usually `http://localhost:8080` .

Enable Hasura Console

To access the Hasura Console via the URL the `HASURA_GRAPHQL_ENABLE_CONSOLE` [ environment variable ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#database-url)or
the `--enable-console` flag must be set to `true` .

On the Hasura Console, navigate to the `Data` tab, you will see the "Connect Database" screen.

- Give the database a name, say `default`
- Choose the database type from the list of[ supported databases ](https://hasura.io/docs/latest/databases/overview/#supported-databases)
- Enter your database connection details
- Click `Connect Database`


Image: [ database setup with new database ](https://hasura.io/docs/assets/images/databases_connect-database_2-17-0-351c6d81439cc6e76d019077e85a11ea.png)

In your `config v3` project, head to the `/metadata/databases/databases.yaml` file and add the database configuration as
below.

```
-   name :  <db_name >
   kind :  postgres
   configuration :
     connection_info :
       database_url :
         from_env :  <DB_URL_ENV_VAR >
     pool_settings :
       idle_timeout :   180
       max_connections :   50
       retries :   1
   tables :   [ ]
   functions :   [ ]
```

Apply the Metadata by running:

`hasura metadata apply`

Depending on the type of database, you can add a database using the[ sources Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/source/).

For example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_add_source" ,
   "args" :   {
     "name" :   "<db_name>" ,
     "configuration" :   {
       "connection_info" :   {
         "database_url" :   {
           "from_env" :   "<DB_URL_ENV_VAR>"
         } ,
         "pool_settings" :   {
           "retries" :   1 ,
           "idle_timeout" :   180 ,
           "max_connections" :   50
         }
       }
     }
   }
}
```

## Hasura Metadata storage​

When using Hasura Cloud, Metadata is stored for you in separate data storage to your connected database(s). When using
Docker, if you want to[ store the Hasura Metadata on a separate database ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#metadata-database-url),
you can use the `HASURA_GRAPHQL_METADATA_DATABASE_URL` env var to specify which database to use. By default, the Hasura
Metadata is stored on the same database as specified in the `HASURA_GRAPHQL_DATABASE_URL` environment variable.

## Connect different Hasura instances to the same database​

You can connect different Hasura instances (i.e. instances with different Metadata) to the same database as long as
there are no[ Event Triggers ](https://hasura.io/docs/latest/event-triggers/overview/)in any of the Metadata. Event Triggers store their data in
the underlying database and hence different instances acting on the same data can cause undefined behavior during
run-time. This should not be a problem if the Hasura instances have the same Metadata.

To connect multiple Hasura instances to the same database, simply follow the steps above for[ Connect to an existing database ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#connect-to-an-existing-database)for each instance.

## Connecting to a database not exposed over the internet​

[ Contact us ](https://hasura.io/contact-us/)for VPC peering and on-premise solutions.

## More databases​

Support for more databases is coming soon. Stay up to date with[ supported databases here ](https://hasura.io/docs/latest/databases/overview/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#introduction)
- [ On Hasura Cloud ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#on-hasura-cloud)
    - [ Option 1: Create and connect a new database ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#option-1-create-and-connect-a-new-database)

- [ Option 2: Connect an existing database ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#option-2-connect-an-existing-database)

- [ Allow connections from the Hasura Cloud IP ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#cloud-projects-create-allow-nat-ip)
- [ On Hasura deployed via Docker ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#on-hasura-deployed-via-docker)
- [ Hasura Metadata storage ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#hasura-metadata-storage)
- [ Connect different Hasura instances to the same database ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#connect-different-hasura-instances-to-the-same-database)
- [ Connecting to a database not exposed over the internet ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#connecting-to-a-database-not-exposed-over-the-internet)
- [ More databases ](https://hasura.io/docs/latest/databases/quickstart/#cloud-projects-create-allow-nat-ip/#more-databases)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)