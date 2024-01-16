# Quickstart with Google Cloud Run

## Introduction​

This tutorial will help you run Hasura Enterprise Edition as a Google Cloud Run service using the `gcloud` CLI.

 **This guide requires HGE versions  v2.12.0  and above.** Installation instructions are below.

`v2.12.0`

## Deploying Hasura Enterprise Edition on Cloud Run​

### Prerequisites​

This tutorial assumes that the following prerequisites have been met:

- The latest version of the `gcloud` CLI is installed and configured. For more information about installing or upgrading
your gcloud CLI, see[ Installing the gcloud CLI ](https://cloud.google.com/sdk/docs/install).
- Your `gcloud` user has the[ required permissions ](https://cloud.google.com/run/docs/reference/iam/roles#additional-configuration)to deploy a
cloud run service.
- You have a Postgres database for storing Metadata and Redis for caching / rate limiting, preferably a managed service,
see[ Creating a Cloud SQL PostgresSQL instance ](https://cloud.google.com/sql/docs/postgres/create-instance)and[ Creating a Memorystore for Redis ](https://cloud.google.com/memorystore/docs/redis/create-instance-console).
- You have a Serverless VPC Access Connector to make the Postgres and Redis datastores accessible from Cloud Run, see[ Creating a Serverless VPC Access connector ](https://cloud.google.com/vpc/docs/configure-serverless-vpc-access).


### Step 1: Get the Cloud Run env vars file​

The[ install manifests repo ](https://github.com/hasura/graphql-engine/tree/master/install-manifests)contains all
installation manifests required to deploy Hasura anywhere. Get the Cloud Run env vars file from there:

`wget  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/enterprise/google-cloud-run/env.yaml`

### Step 2: Set the Metadata database URL, Redis database URL and the admin secret​

Edit `env.yaml` and set the right values:

```
HASURA_GRAPHQL_METADATA_DATABASE_URL :  postgres : //postgres : postgrespassword@postgres : 5432/postgres
HASURA_GRAPHQL_REDIS_URL :   'redis://redis:6379'
HASURA_GRAPHQL_RATE_LIMIT_REDIS_URL :   'redis://redis:6379'
HASURA_GRAPHQL_ADMIN_SECRET :  myadminsecretkey
```

Examples of `HASURA_GRAPHQL_METADATA_DATABASE_URL` :

- `postgres://admin:password@db-ip:5432/my_db`
- `postgres://admin:@db-ip:5432/my_db`  *(if there is no password)*


Examples of `HASURA_GRAPHQL_REDIS_URL` and `HASURA_GRAPHQL_RATE_LIMIT_REDIS_URL` :

- `redis://admin:password@redis-ip:6379`
- `redis://redis-ip:6379`  *(if there is no password)*


Note

- If your **password contains special characters** (e.g. #, %, $, @, etc.), you need to URL encode them in the `HASURA_GRAPHQL_METADATA_DATABASE_URL` env var (e.g. %40 for @).
- The Hasura GraphQL Engine needs access permissions on your Postgres database as described in[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#postgres-permissions).
- The `HASURA_GRAPHQL_ADMIN_SECRET` should never be passed from the client to the Hasura GraphQL Engine as it would give
the client full admin rights to your Hasura instance. See[ Authentication & Authorization ](https://hasura.io/docs/latest/auth/overview/)for
information on setting up authentication.
- Convert confidential environment variables such as Postgres / Redis URLs, admin / metrics secrets to fetch them from
secrets,[ see here for more information ](https://cloud.google.com/run/docs/configuring/secrets).


If your **password contains special characters** (e.g. #, %, $, @, etc.), you need to URL encode them in the `HASURA_GRAPHQL_METADATA_DATABASE_URL` env var (e.g. %40 for @).

The Hasura GraphQL Engine needs access permissions on your Postgres database as described in[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#postgres-permissions).

The `HASURA_GRAPHQL_ADMIN_SECRET` should never be passed from the client to the Hasura GraphQL Engine as it would give
the client full admin rights to your Hasura instance. See[ Authentication & Authorization ](https://hasura.io/docs/latest/auth/overview/)for
information on setting up authentication.

Convert confidential environment variables such as Postgres / Redis URLs, admin / metrics secrets to fetch them from
secrets,[ see here for more information ](https://cloud.google.com/run/docs/configuring/secrets).

### Step 3: Set up a license key​

If you don't have a license key, you can skip this step and proceed with this guide to set up Hasura. Once you have Hasura up and running, you can sign up for a[ free 30 day Enterprise Edition trial ](https://hasura.io/docs/latest/enterprise/try-hasura-enterprise-edition/)from the Hasura console.

If you have been provided a license key by the Hasura team, add it as an environment variable to Hasura. Edit `env.yaml` to set the license key as the value for the `HASURA_GRAPHQL_EE_LICENSE_KEY` environment variable.

```
HASURA_GRAPHQL_METADATA_DATABASE_URL :  postgres : //postgres : postgrespassword@postgres : 5432/postgres
HASURA_GRAPHQL_REDIS_URL :   'redis://redis:6379'
HASURA_GRAPHQL_RATE_LIMIT_REDIS_URL :   'redis://redis:6379'
HASURA_GRAPHQL_ADMIN_SECRET :  myadminsecretkey
HASURA_GRAPHQL_EE_LICENSE_KEY :   '<license key>'
```

### Step 4: Copy the Hasura graphql-engine image to the GCR registry​

Cloud Run does not allow using images from Dockerhub. Due to this limitation it's necessary to pull the Hasura
graphql-engine image from Dockerhub and push it to your container registry,[ see here for more information ](https://cloud.google.com/run/docs/deploying#other-registries).

This can be done using the below steps:

```
VERSION=
v2.36.0
docker pull hasura/graphql-engine:$VERSION
docker tag hasura/graphql-engine:$VERSION gcr.io/<MY_PROJECT_ID>/hasura/graphql-engine:$VERSION
docker push gcr.io/<MY_PROJECT_ID>/hasura/graphql-engine:$VERSION
```

### Step 4: Deploy the service​

Update the image and vpc connector values in the below commmand.

```
gcloud run deploy hasura  \
  --image = gcr.io/ < MY_PROJECT_ID > /hasura/graphql-engine:tag  \
  --env-vars-file = env.yaml  \
  --vpc-connector = < vpc-connector-name >   \
  --allow-unauthenticated  \
  --max-instances = 1   \
  --cpu = 1   \
  --memory = 2048Mi  \
  --port = 8080
```

Wait for the deployment to finish. Upon successful completion, a success message is displayed along with the URL of the
deployed service.

Click the displayed URL link to open the unique and stable endpoint of the Hasura service.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-google-cloud-run/#introduction)
- [ Deploying Hasura Enterprise Edition on Cloud Run ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-google-cloud-run/#deploying-hasura-enterprise-edition-on-cloud-run)
    - [ Prerequisites ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-google-cloud-run/#prerequisites)

- [ Step 1: Get the Cloud Run env vars file ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-google-cloud-run/#step-1-get-the-cloud-run-env-vars-file)

- [ Step 2: Set the Metadata database URL, Redis database URL and the admin secret ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-google-cloud-run/#step-2-set-the-metadata-database-url-redis-database-url-and-the-admin-secret)

- [ Step 3: Set up a license key ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-google-cloud-run/#step-3-set-up-a-license-key)

- [ Step 4: Copy the Hasura graphql-engine image to the GCR registry ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-google-cloud-run/#step-4-copy-the-hasura-graphql-engine-image-to-the-gcr-registry)

- [ Step 4: Deploy the service ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-google-cloud-run/#step-4-deploy-the-service)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)