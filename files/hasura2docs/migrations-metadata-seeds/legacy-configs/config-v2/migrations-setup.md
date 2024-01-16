# Set up Hasura Migrations (config v2)

## Introduction​

If you don’t already use any tool to manage your Postgres schema, you can use Hasura to do that for you. Hasura has a
CLI which will help you save each action that you do on the Console, including creating tables/views and schema
modifying SQL statements, as SQL files. These files are called Migrations and they can be applied and rolled back
step-by-step. These files can be version controlled and can be used with your CI/CD system to make incremental updates.

Let's say we have the following two tables in our schema:

```
author  ( id uuid ,  name  text ,  rating  integer )
article  ( id uuid ,  title  text ,  content  text ,  author_id uuid )
```

Now we want to set up Migrations starting with this schema.

## Step 1: Disable the Console on the server​

To use Migrations effectively, the Console on the server (which is served at `/console` ) should be disabled and all
changes must go through the Console served by the CLI. Otherwise, changes could be made through the server Console and
they will not be tracked by Migrations.

So, the first step is to disable the Console served by the GraphQL Engine server. In order to do that, remove the `--enable-console` flag from the command that starts the server or set the following environment variable to `false` :

`HASURA_GRAPHQL_ENABLE_CONSOLE = false`

Note

If this is set in YAML, make sure you quote the word false, i.e. `HASURA_GRAPHQL_ENABLE_CONSOLE: "false"` .

## Step 2: Install the Hasura CLI​

Follow the instructions in[ Installing the Hasura CLI ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/).

## Step 3: Set up a project directory​

For the endpoint referred here, let's say you've deployed the GraphQL Engine on Hasura Cloud, then this endpoint is: `https://my-graphql.hasura.app` . In case you've deployed Hasura using Docker, the URL might be `http://xx.xx.xx.xx:8080` . In any case, the endpoint should **not** contain the `v1/graphql` API path. It should just be
the hostname and any sub-path if it is configured that way.

Let's set up a project directory by executing the following command:

```
hasura init my-project --endpoint http://my-graphql.hasura.app
cd  my-project
```

This will create a new directory called `my-project` with a `config.yaml` file, a `migrations` directory and a `metadata` directory. This directory structure is mandatory to use Hasura Migrations.

Note

In case there is an admin secret set, you can set it as an environment variable `HASURA_GRAPHQL_ADMIN_SECRET=<your-admin-secret>` on your local machine and the CLI will use it. You can also use it as
a flag to CLI commands: `--admin-secret '<your-admin-secret>'` .

### Step 3.1: Set up version control for your project directory​

The project directory created above can be committed to version control.

Set up version control and commit the project status:

```
# in project dir
# initialize version control
git  init
# commit initial project status
git   add   .
git  commit -m  "hasura project init"
```

## Step 4: Initialize the Migrations and Metadata as per your current state​

If you have already set up your database and GraphQL API, you need to initialize your database Migrations and Hasura
Metadata with the current state of the database.

### Step 4.1: Initialize database Migrations​

Create a migration called `init` by exporting the current Postgres schema from the server:

```
# create migration files (note that this will only export the public schema from postgres)
hasura migrate create  "init"  --from-server
# note down the version
# mark the migration as applied on this server
hasura migrate apply --version  "<version>"  --skip-execution
```

This command will create a new directory named `<timestamp>_init` inside the `migrations` directory. In the newly
created directory, there's a file named `up.sql` . This file will contain the required information to reproduce the
current state of the server including the Postgres (public) schema. If you'd like to read more about the format of
migration files, check out the[ Migration file format reference (config v2) ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/migration-file-format/)

The apply command will mark this migration as "applied" on the server.

Note

If you need to export other schemas along with `public` , you can name them using the `--schema` flag.

For example, to export schemas `public` , `schema1` and `schema2` , execute the following command:

`hasura migrate create  "init"  --from-server --schema  "public"  --schema  "schema1"  --schema  "schema2"`

### Step 4.2: Initialize Hasura Metadata​

Export the Hasura Metadata from the server:

```
# export the metadata
hasura metadata  export
```

This command will export the current Hasura Metadata as a bunch of YAML files in the `metadata` directory.

If you'd like to read more about the format of Metadata files, check out the[ Metadata format reference (config v2) ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/reference/metadata-format/)

### Step 4.3: Add a checkpoint to version control​

Commit the current project state to version control:

```
# in project dir
git   add   .
git  commit -m  "initialize migrations and metadata"
```

Note

The version control set up should typically be done right after[ Step 3 ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#migrations-project-init-v2)

## Step 5: Use the Console from the CLI​

From this point onwards, instead of using the Console at `http://my-graphql.hasura.app/console` you should use the
console from the CLI by running:

```
# in project dir
hasura console
```

## Step 6: Add a new table and see how Migrations and Metadata is updated​

As you use the Hasura Console UI served by the CLI to make changes to your schema, database migration files are
automatically generated in the `migrations/` directory and the Metadata is exported in the `metadata/` directory of your
project.

Let's create the following table `address (id uuid, street text, zip text, city text, country text, author_id int)` and
then create a foreign-key to the `author` table via the `author_id -> id` columns.

In the `migrations` directory, we can find new directories called `<timestamp>_create_table_public_address` and `<timestamp>_set_fk_public_address_author_id` containing an `up.sql` and a `down.sql` migration files for the changes we
made.

You can also go ahead and add permissions and create relationships for the address table. The related Metadata changes
will automatically be exported into the `metadata` directory.

Note

Migrations are only created when using the Console through the CLI.

## Step 7: Squash Migrations and add checkpoints to version control​

As you keep using the Console via the CLI to make changes to the schema, new migration files will keep getting generated
and the Metadata files will keep getting updated automatically.

Typically while adding a feature a lot of incremental migration files get created for each of the small tasks that you
did to achieve the feature. To improve maintainability of the migration files and to ensure you can go back to a
particular version of the metadata, it is recommended that you squash your migration files and commit the project status
in version control whenever you reach a logical checkpoint in your feature development.

The following command will squash all migration files from the given migration to the latest migration into a single
migration file.

```
hasura migrate squash --name  "<feature-name>"  --from  < start-migration-version >
# note down the version
# mark the squashed migration as applied on this server
hasura migrate apply --version  "<squash-migration-version>"  --skip-execution
```

Commit the project status into version control.

```
# in project dir
git   add   .
git  commit -m  "<feature-name>"
```

Note

The version control set up should typically be done right after[ Step 3 ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#migrations-project-init-v2)

## Step 8: Apply the Migrations and Metadata on another instance of the GraphQL Engine​

Apply all Migrations present in the `migrations/` directory and the Metadata present in the `metadata/` directory on a
new instance at `http://another-graphql-instance.hasura.app` :

```
# in project dir
hasura migrate apply --endpoint http://another-graphql-instance.hasura.app
hasura metadata apply --endpoint http://another-graphql-instance.hasura.app
```

In case you need an automated way of applying the Migrations and metadata, take a look at the[ cli-migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/auto-apply-migrations/)Docker image, which can start the GraphQL Engine
after automatically applying the Migrations and Metadata which are mounted onto directories.

If you now open the Console of the new instance, you can see that the three tables have been created and are tracked:

Image: [ Tracked tables from Hasura Migrations ](data:image/png;base64,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)

## Step 9: Check the status of Migrations​

```
# in project dir
hasura migrate status
```

This command will print out each migration version present in the `migrations` directory along with its name, source
status and database status.

For example,

```
$ hasura migrate status
VERSION        NAME                           SOURCE STATUS  DATABASE STATUS
1590493510167   init                           Present        Present
1590497881360   create_table_public_address    Present        Present
```

Such a migration status indicates that there are 2 migration versions in the local directory and both of them are
applied on the database.

If `SOURCE STATUS` indicates `Not Present` , it means that the migration version is present on the server, but not on the
current user's local directory. This typically happens if multiple people are collaborating on a project and one of the
collaborators forgot to pull the latest changes which included the latest migration files, or another collaborator
forgot to push the latest migration files that were applied on the database. Syncing of the files would fix the issue.

If `DATABASE STATUS` indicates `Not Present` , it denotes that there are new migration versions in the local directory
which are not applied on the database yet. Executing `hasura migrate apply` will resolve this.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#introduction)
- [ Step 1: Disable the Console on the server ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#step-1-disable-the-console-on-the-server)
- [ Step 2: Install the Hasura CLI ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#step-2-install-the-hasura-cli)
- [ Step 3: Set up a project directory ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#migrations-project-init-v2)
    - [ Step 3.1: Set up version control for your project directory ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#step-31-set-up-version-control-for-your-project-directory)
- [ Step 4: Initialize the Migrations and Metadata as per your current state ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#migrations-initialize-v2)
    - [ Step 4.1: Initialize database Migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#step-41-initialize-database-migrations)

- [ Step 4.2: Initialize Hasura Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#step-42-initialize-hasura-metadata)

- [ Step 4.3: Add a checkpoint to version control ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#step-43-add-a-checkpoint-to-version-control)
- [ Step 5: Use the Console from the CLI ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#step-5-use-the-console-from-the-cli)
- [ Step 6: Add a new table and see how Migrations and Metadata is updated ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#step-6-add-a-new-table-and-see-how-migrations-and-metadata-is-updated)
- [ Step 7: Squash Migrations and add checkpoints to version control ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#step-7-squash-migrations-and-add-checkpoints-to-version-control)
- [ Step 8: Apply the Migrations and Metadata on another instance of the GraphQL Engine ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#step-8-apply-the-migrations-and-metadata-on-another-instance-of-the-graphql-engine)
- [ Step 9: Check the status of Migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/migrations-setup/#step-9-check-the-status-of-migrations)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)