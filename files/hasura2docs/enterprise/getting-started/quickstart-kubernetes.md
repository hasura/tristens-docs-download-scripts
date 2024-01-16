# Quickstart with Kubernetes

## Introduction​

This tutorial helps you set up Hasura Enterprise Edition on Kubernetes and connect it to your Postgres database.

 **This guide requires HGE versions  v2.12.0  and above.** Installation instructions are below.

`v2.12.0`

## Deploying Hasura Enterprise Edition on Kubernetes​

### Prerequisites​

This tutorial assumes that the following prerequisites have been met:

- A functioning Kubernetes cluster.
- This tutorial uses a container image hosted on the public Docker hub, so your Kubernetes cluster must have internet
access.
- You have a Postgres database for storing Metadata and Redis for caching / rate limiting, preferably a managed service.
- The latest version of[ Kubectl ](https://kubernetes.io/docs/tasks/tools/#kubectl)compatible with your cluster has been
installed and configured.


### Step 1: Get the Kubernetes deployment and service files​

The[ install manifests repo ](https://github.com/hasura/graphql-engine/tree/master/install-manifests)contains all
installation manifests required to deploy Hasura anywhere. Get the Kubernetes deployment and service files from there:

`wget  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/enterprise/kubernetes/deployment.yaml`

### Step 2: Set the Metadata database URL, Redis database URL and the admin secret​

Edit `deployment.yaml` and set the right values:

```
---
env :
   -   name :  HASURA_GRAPHQL_METADATA_DATABASE_URL
     value :  postgres : //<username > : <password > @hostname : <port > /<dbname >
   -   name :  HASURA_GRAPHQL_REDIS_URL
     value :  redis : //redis : 6379
   -   name :  HASURA_GRAPHQL_RATE_LIMIT_REDIS_URL
     value :  redis : //redis : 6379
   -   name :  HASURA_GRAPHQL_ADMIN_SECRET
     value :  adminsecret
```

Examples of `HASURA_GRAPHQL_METADATA_DATABASE_URL` :

- `postgres://admin:password@postgres:5432/my_db`
- `postgres://admin:@postgres:5432/my_db`  *(if there is no password)*


Examples of `HASURA_GRAPHQL_REDIS_URL` and `HASURA_GRAPHQL_RATE_LIMIT_REDIS_URL` :

- `redis://admin:password@redis:6379`
- `redis://redis:6379`  *(if there is no password)*


Note

- If your **password contains special characters** (e.g. #, %, $, @, etc.), you need to URL encode them in the `HASURA_GRAPHQL_METADATA_DATABASE_URL` env var (e.g. %40 for @).You can check the[ logs ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#kubernetes-logs)to see if the database credentials are proper and if Hasura is able to
connect to the database.
- The Hasura GraphQL Engine needs access permissions on your Postgres database as described in[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#postgres-permissions).
- The `HASURA_GRAPHQL_ADMIN_SECRET` should never be passed from the client to the Hasura GraphQL Engine as it would give
the client full admin rights to your Hasura instance. See[ Authentication & Authorization ](https://hasura.io/docs/latest/auth/overview/)for
information on setting up authentication.
- Move confidential environment variables such as Postgres / Redis URLs, admin / metrics secrets to fetch from
kubernetes secrets / vault / your preferred approach.


If your **password contains special characters** (e.g. #, %, $, @, etc.), you need to URL encode them in the `HASURA_GRAPHQL_METADATA_DATABASE_URL` env var (e.g. %40 for @).

You can check the[ logs ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#kubernetes-logs)to see if the database credentials are proper and if Hasura is able to
connect to the database.

The Hasura GraphQL Engine needs access permissions on your Postgres database as described in[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#postgres-permissions).

The `HASURA_GRAPHQL_ADMIN_SECRET` should never be passed from the client to the Hasura GraphQL Engine as it would give
the client full admin rights to your Hasura instance. See[ Authentication & Authorization ](https://hasura.io/docs/latest/auth/overview/)for
information on setting up authentication.

Move confidential environment variables such as Postgres / Redis URLs, admin / metrics secrets to fetch from
kubernetes secrets / vault / your preferred approach.

### Step 3: Set up a license key​

If you don't have a license key, you can skip this step and proceed with this guide to set up Hasura. Once you have the Hasura up and running, you can sign up for a[ free 30 day Enterprise Edition trial ](https://hasura.io/docs/latest/enterprise/try-hasura-enterprise-edition/)from the Hasura console.

If you have been provided a license key by the Hasura team, add it as an environment variable to Hasura. Edit `deployment.yaml` and set the license key as the value for the `HASURA_GRAPHQL_EE_LICENSE_KEY` environment variable.

```
---
env :
   -   name :  HASURA_GRAPHQL_METADATA_DATABASE_URL
     value :  postgres : //<username > : <password > @hostname : <port > /<dbname >
   -   name :  HASURA_GRAPHQL_REDIS_URL
     value :  redis : //redis : 6379
   -   name :  HASURA_GRAPHQL_RATE_LIMIT_REDIS_URL
     value :  redis : //redis : 6379
   -   name :  HASURA_GRAPHQL_ADMIN_SECRET
     value :  adminsecret
   -   name :  HASURA_GRAPHQL_EE_LICENSE_KEY
     value :   '<license key>'
```

### Step 4: Create the Kubernetes deployment and service​

`kubectl create -f deployment.yaml`

### Step 5: Open the Hasura Console​

The above creates a LoadBalancer type service with port 80. So you should be able to access the Console at the external
IP.

For example, using Docker-for-desktop on Mac:

```
kubectl get svc
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT ( S )         AGE
hasura       LoadBalancer    10.96 .214.240   localhost      80 :30303/TCP   4m
kubernetes   ClusterIP       10.96 .0.1        < none >          443 /TCP        8m
```

Head to: `http://localhost` and the Console should load!

### Step 6: Start using Hasura​

Congratulations! You have successfully set up Hasura Enterprise Edition on Docker.[ Start using Hasura Enterprise Edition now ](https://hasura.io/docs/latest/enterprise/getting-started/start-using-hasura-ee/).

## Hasura GraphQL Engine server logs​

You can check the logs of the Hasura GraphQL Engine deployed on Kubernetes by checking the logs of the GraphQL Engine
service, i.e. `hasura` :

```
kubectl logs -f svc/hasura
{ "timestamp" : "2018-10-09T11:20:32.054+0000" ,  "level" : "info" ,  "type" : "http-log" ,  "detail" : { "status" :200,  "query_hash" : "01640c6dd131826cff44308111ed40d7fbd1cbed" ,  "http_version" : "HTTP/1.1" ,  "query_execution_time" :3.0177627e-2,  "request_id" :null,  "url" : "/v1/graphql" ,  "user" : { "x-hasura-role" : "admin" } ,  "ip" : "127.0.0.1" ,  "response_size" :209329,  "method" : "POST" ,  "detail" :null } }
.. .
```

 **See:** 

- [ Kubernetes logs ](https://kubernetes.io/docs/concepts/cluster-administration/logging)for more details on logging in
Kubernetes.
- [ Hasura GraphQL Engine logs ](https://hasura.io/docs/latest/deployment/logging/)for more details on Hasura logs.


## Updating Hasura GraphQL Engine​

This guide will help you update the Hasura GraphQL Engine running on Kubernetes. This guide assumes that you already
have the Hasura GraphQL Engine running on Kubernetes.

### Step 1: Check the latest release version​

The current latest version is:

```
hasura/graphql-engine:
v2.36.0
```

All the versions can be found[ here ](https://github.com/hasura/graphql-engine/releases).

### Step 2: Update the container image​

In the `deployment.yaml` file, update the image tag to this latest version.

For example, if you had:

```
containers :
   -   image :  hasura/graphql - engine : v1.0.0 - alpha01
```

you should change it to:

```
containers:
- image: hasura/graphql-engine:
v2.36.0
```

### Step 3: Roll out the change​

`kubectl replace -f deployment.yaml`

Note

If you are downgrading to an older version of the GraphQL Engine, you might need to downgrade your Metadata catalogue
version as described in[ Downgrading Hasura GraphQL Engine ](https://hasura.io/docs/latest/deployment/downgrading/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#introduction)
- [ Deploying Hasura Enterprise Edition on Kubernetes ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#deploying-hasura-enterprise-edition-on-kubernetes)
    - [ Prerequisites ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#prerequisites)

- [ Step 1: Get the Kubernetes deployment and service files ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#step-1-get-the-kubernetes-deployment-and-service-files)

- [ Step 2: Set the Metadata database URL, Redis database URL and the admin secret ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#step-2-set-the-metadata-database-url-redis-database-url-and-the-admin-secret)

- [ Step 3: Set up a license key ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#step-3-set-up-a-license-key)

- [ Step 4: Create the Kubernetes deployment and service ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#step-4-create-the-kubernetes-deployment-and-service)

- [ Step 5: Open the Hasura Console ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#step-5-open-the-hasura-console)

- [ Step 6: Start using Hasura ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#step-6-start-using-hasura)
- [ Hasura GraphQL Engine server logs ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#kubernetes-logs)
- [ Updating Hasura GraphQL Engine ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#kubernetes-update)
    - [ Step 1: Check the latest release version ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#step-1-check-the-latest-release-version)

- [ Step 2: Update the container image ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#step-2-update-the-container-image)

- [ Step 3: Roll out the change ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-kubernetes/#step-3-roll-out-the-change)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)