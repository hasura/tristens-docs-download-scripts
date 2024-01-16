# Manage Development Environments

## Introduction​

This guide is designed to teach you how to set up and modify Hasura in a local Docker environment, and then transfer
those changes to your Cloud project.

## Moving from Hasura Cloud to local development​

### Step 1: Setup local development of Hasura with Docker​

In this step, you'll establish a self-hosted version of Hasura. **Please note: if you intend to utilize Hasura EE for
local development, please secure a license by either registering for a
 30-day free trial  or filing a ticket with
 Hasura support .** 

Follow the guide[ here ](https://hasura.io/docs/latest/getting-started/docker-simple/)to get up and running with Hasura GraphQL Engine and
Postgres as Docker containers in your local system. You can skip the steps involving connecting a database, as you'll be
applying Metadata from your cloud database in a later step. Make sure that the ENV variable name for database connection
in your local setup is the same as that in your Cloud project so that your database connection Metadata will still work
and not need to be updated. The value of this variable will be updated to point to your local database. Also add any
other ENV variables that you might have set on the Cloud project.

### Step 2: Install Hasura CLI​

Follow the instructions in[ install_hasura_cli ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/)

### Step 3: Initialize a Hasura CLI project locally​

`hasura init  < project-name >`

### Step 4: Initialize the migration files​

This will get your database schema from the cloud project to your local setup

```
hasura migrate create init --from-server --endpoint  < hasura-cloud-project-url >  --admin-secret  < admin-secret >  --database-name  < database-name >
# note down the version
# mark the migration as applied on the cloud project
hasura migrate apply --endpoint  < hasura-cloud-project-url >  --admin-secret  < admin-secret >  --version  < version-number >  --skip-execution
```

When using a non-Postgres database

Please note that when using the `migrate create init --from-server` command, Hasura only supports Postgres databases.
Should you wish to use a different database, you will need to manually create the migration files. For more information,
please see this section of the[ Migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)documentation.

It is important to mark the migration as applied on the Cloud project to ensure that the schema that is already created
on Hasura Cloud project is not attempted to be recreated again, which would end in an error state.

### Step 5: Export metadata​

`hasura metadata  export  --endpoint  < hasura-project-url >  --admin-secret  < admin-secret >`

We have successfully synced our state from Cloud to the Hasura CLI local dev environment.

Next, we apply all these changes to our local Hasura with Docker setup.

### Step 6: Apply Metadata and Migrations to your local Hasura instance​

```
hasura metadata apply
hasura migrate apply --all-databases
hasura metadata reload
```

By default the Metadata and Migrations are applied to `http://localhost:8080` which is the endpoint specified in the `config.yaml` file of your CLI project. If you want to apply the Metadata and Migrations to any other endpoint, you
could go ahead and change the endpoint in the `config.yaml` file or use the `--endpoint` flag along with the commands
above.

And you're all set now! Go ahead and setup version control for your project for further ease of integration.

## Moving from local development to Hasura Cloud​

If you have been using the OSS version of Hasura GraphQL Engine locally using Docker and want to move to a Hasura Cloud
project, start by creating a project at[ https://cloud.hasura.io/signup ](https://cloud.hasura.io/signup)

Once the project is created, launch Console and connect your database. Make sure that the name of the database is same
as that in your local setup. Do refer this[ Get started guide ](https://hasura.io/docs/latest/getting-started/getting-started-cloud/)for a
step-by-step guide.

Also ensure the database is connected using the same ENV var in your local setup and the Cloud project. You might have
drop and create a new ENV var containing the database URL on your Cloud project if required.

Also add any other ENV vars that you might have set on your local project.

### Setting up a Git repo for your Hasura Project​

In order to easily apply your local changes to your new Cloud project, we'll use the Hasura[ GitHub deployment ](https://hasura.io/docs/latest/cloud-ci-cd/github-integration/)feature. But before we do that, we need to setup Metadata &
Migrations of your local setup that you can apply to your Cloud project. For a lowdown on Hasura Metadata & Migrations
refer the guide[ here ](https://hasura.io/docs/latest/migrations-metadata-seeds/overview/)

### Step 1: Install Hasura CLI​

Follow the instructions in[ install_hasura_cli ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/)

### Step 2: Setup a project directory​

`hasura init  < project-name >  --endpoint  < local-project-endpoint >`

Your local project endpoint might be `http://localhost:8080` (based on how it was setup initially). This creates a
project directory with `migrations` and `metadata` directories and a `config.yaml` file.

### Step 3: Initialize the migration files​

This will get your database schema from your local setup into the project folder.

```
hasura migrate create init --from-server --admin-secret  < admin-secret >  --database-name  < database-name >
# note down the version
# mark the migration as already applied on the local server
hasura migrate apply --admin-secret  < admin-secret >  --version  < version-number >  --skip-execution
```

When using a non-Postgres database

Please note that when using the `migrate create init --from-server` command, Hasura only supports Postgres databases.
Should you wish to use a different database, you will need to manually create the migration files. For more information,
please see this section of the[ Migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)documentation.

### Step 4: Initialize Hasura Metadata​

`hasura metadata  export`

This command will export the current Hasura Metadata as a bunch of YAML files in the `metadata` directory.

### Step 5: Setup version control & Git Deploy​

```
# in the project directory
git  init
git   add   .
git  commit -m  "initialize metadata and migrations"
```

Push these changes to GitHub repo of your choice.

Now we're all set to see the magic of our GitHub integration to deploy the Metadata and Migrations to your Cloud project
by following the steps[ here ](https://hasura.io/docs/latest/cloud-ci-cd/github-integration/)!

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/environments/#introduction)
- [ Moving from Hasura Cloud to local development ](https://hasura.io/docs/latest/hasura-cloud/environments/#moving-from-hasura-cloud-to-local-development)
    - [ Step 1: Setup local development of Hasura with Docker ](https://hasura.io/docs/latest/hasura-cloud/environments/#step-1-setup-local-development-of-hasura-with-docker)

- [ Step 2: Install Hasura CLI ](https://hasura.io/docs/latest/hasura-cloud/environments/#step-2-install-hasura-cli)

- [ Step 3: Initialize a Hasura CLI project locally ](https://hasura.io/docs/latest/hasura-cloud/environments/#step-3-initialize-a-hasura-cli-project-locally)

- [ Step 4: Initialize the migration files ](https://hasura.io/docs/latest/hasura-cloud/environments/#step-4-initialize-the-migration-files)

- [ Step 5: Export metadata ](https://hasura.io/docs/latest/hasura-cloud/environments/#step-5-export-metadata)

- [ Step 6: Apply Metadata and Migrations to your local Hasura instance ](https://hasura.io/docs/latest/hasura-cloud/environments/#step-6-apply-metadata-and-migrations-to-your-local-hasura-instance)
- [ Moving from local development to Hasura Cloud ](https://hasura.io/docs/latest/hasura-cloud/environments/#moving-from-local-development-to-hasura-cloud)
    - [ Setting up a Git repo for your Hasura Project ](https://hasura.io/docs/latest/hasura-cloud/environments/#setting-up-a-git-repo-for-your-hasura-project)

- [ Step 1: Install Hasura CLI ](https://hasura.io/docs/latest/hasura-cloud/environments/#step-1-install-hasura-cli)

- [ Step 2: Setup a project directory ](https://hasura.io/docs/latest/hasura-cloud/environments/#step-2-setup-a-project-directory)

- [ Step 3: Initialize the migration files ](https://hasura.io/docs/latest/hasura-cloud/environments/#step-3-initialize-the-migration-files)

- [ Step 4: Initialize Hasura Metadata ](https://hasura.io/docs/latest/hasura-cloud/environments/#step-4-initialize-hasura-metadata)

- [ Step 5: Setup version control & Git Deploy ](https://hasura.io/docs/latest/hasura-cloud/environments/#step-5-setup-version-control--git-deploy)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)