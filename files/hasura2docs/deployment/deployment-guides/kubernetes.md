# Run Hasura GraphQL Engine on Kubernetes

## Introduction​

This guide assumes that you already have Postgres running and helps you set up the Hasura GraphQL Engine on Kubernetes
and connect it to your Postgres database.

## Deploying Hasura using Kubernetes​

### Step 1: Get the Kubernetes deployment and service files​

The[ hasura/graphql-engine/install-manifests ](https://github.com/hasura/graphql-engine/tree/stable/install-manifests)repo contains all installation manifests required to deploy Hasura anywhere. Get the Kubernetes deployment and service
files from there:

```
$  wget  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/kubernetes/deployment.yaml
$  wget  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/kubernetes/svc.yaml
```

### Step 2: Set the Postgres database url​

Edit `deployment.yaml` and set the right database url:

```
env :
   -   name :  HASURA_GRAPHQL_DATABASE_URL
     value :  postgres : //<username > : <password > @hostname : <port > /<dbname >
```

Examples of `HASURA_GRAPHQL_DATABASE_URL` :

- `postgres://admin:password@localhost:5432/my-db`
- `postgres://admin:@localhost:5432/my-db`  *(if there is no password)*


Note

- If your **password contains special characters** (e.g. #, %, $, @, etc.), you need to URL encode them in the `HASURA_GRAPHQL_DATABASE_URL` env var (e.g. %40 for @).You can check the[ logs ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#kubernetes-logs)to see if the database credentials are proper and if Hasura is able to
connect to the database.
- The Hasura GraphQL Engine needs access permissions on your Postgres database as described in[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#postgres-permissions).


If your **password contains special characters** (e.g. #, %, $, @, etc.), you need to URL encode them in the `HASURA_GRAPHQL_DATABASE_URL` env var (e.g. %40 for @).

You can check the[ logs ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#kubernetes-logs)to see if the database credentials are proper and if Hasura is able to
connect to the database.

The Hasura GraphQL Engine needs access permissions on your Postgres database as described in[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#postgres-permissions).

### Step 3: Create the Kubernetes deployment and service​

```
$ kubectl create -f deployment.yaml
$ kubectl create -f svc.yaml
```

### Step 4: Open the Hasura Console​

The above creates a LoadBalancer type service with port 80. So you should be able to access the Console at the external
IP.

For example, using Docker-for-desktop on Mac:

```
$ kubectl get svc
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT ( S )         AGE
hasura       LoadBalancer    10.96 .214.240   localhost      80 :30303/TCP   4m
kubernetes   ClusterIP       10.96 .0.1        < none >          443 /TCP        8m
```

Head to: `http://localhost` and the Console should load!

### Step 5: Track existing tables and relationships​

See[ Setting up a GraphQL schema using an existing Postgres database ](https://hasura.io/docs/latest/schema/postgres/using-existing-database/)to
enable GraphQL over the database.

## Securing the GraphQL endpoint​

To make sure that your GraphQL endpoint and the Hasura Console are not publicly accessible, you need to configure an
admin secret key.

### Add the HASURA_GRAPHQL_ADMIN_SECRET env var​

Update the `deployment.yaml` to set the `HASURA_GRAPHQL_ADMIN_SECRET` environment variable.

```
...
spec :
    containers :
      ...
      command :   [ "graphql-engine" ]
      args :   [ "serve" ,   "--enable-console" ]
      env :
      -   name :  HASURA_GRAPHQL_DATABASE_URL
        value :  postgres : //<username > : <password > @hostname : <port > /<dbname >
      -   name :  HASURA_GRAPHQL_ADMIN_SECRET
        value :  mysecretkey
      ports :
      -   containerPort :   8080
        protocol :  TCP
      resources :   { }
```

Note

The `HASURA_GRAPHQL_ADMIN_SECRET` should never be passed from the client to the Hasura GraphQL Engine as it would give
the client full admin rights to your Hasura instance. See[ Authentication & Authorization ](https://hasura.io/docs/latest/auth/overview/)for
information on setting up authentication.

### (optional) Use the admin secret key with the CLI​

In case you're using the CLI to open the Hasura Console, use the `admin-secret` flag when you open the Console:

`hasura console --admin-secret = < myadminsecretkey >`

## Hasura GraphQL Engine server logs​

You can check the logs of the Hasura GraphQL Engine deployed on Kubernetes by checking the logs of the GraphQL Engine
service, i.e. `hasura` :

```
$ kubectl logs -f svc/hasura
{ "timestamp" : "2018-10-09T11:20:32.054+0000" ,  "level" : "info" ,  "type" : "http-log" ,  "detail" : { "status" :200,  "query_hash" : "01640c6dd131826cff44308111ed40d7fbd1cbed" ,  "http_version" : "HTTP/1.1" ,  "query_execution_time" :3.0177627e-2,  "request_id" :null,  "url" : "/v1/graphql" ,  "user" : { "x-hasura-role" : "admin" } ,  "ip" : "127.0.0.1" ,  "response_size" :209329,  "method" : "POST" ,  "detail" :null } }
.. .
```

 **See:** 

- [ https://kubernetes.io/docs/concepts/cluster-administration/logging ](https://kubernetes.io/docs/concepts/cluster-administration/logging)for more details on logging in Kubernetes.
- [ Hasura GraphQL Engine logs ](https://hasura.io/docs/latest/deployment/logging/)for more details on Hasura logs


## Updating Hasura GraphQL Engine​

This guide will help you update the Hasura GraphQL Engine running on Kubernetes. This guide assumes that you already
have the Hasura GraphQL Engine running on Kubernetes.

### Step 1: Check the latest release version​

The current latest version is:

```
hasura/graphql-engine:
v2.36.0
```

All the versions can be found at:[ https://github.com/hasura/graphql-engine/releases ](https://github.com/hasura/graphql-engine/releases).

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

### Step 3: Rollout the change​

`$ kubectl replace -f deployment.yaml`

Note

If you are downgrading to an older version of the GraphQL Engine you might need to downgrade your Metadata catalogue
version as described in[ Downgrading Hasura GraphQL Engine ](https://hasura.io/docs/latest/deployment/downgrading/)

## Advanced​

- [ Setting up Migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/migrations-metadata-setup/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#introduction)
- [ Deploying Hasura using Kubernetes ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#deploying-hasura-using-kubernetes)
    - [ Step 1: Get the Kubernetes deployment and service files ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#step-1-get-the-kubernetes-deployment-and-service-files)

- [ Step 2: Set the Postgres database url ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#step-2-set-the-postgres-database-url)

- [ Step 3: Create the Kubernetes deployment and service ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#step-3-create-the-kubernetes-deployment-and-service)

- [ Step 4: Open the Hasura Console ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#step-4-open-the-hasura-console)

- [ Step 5: Track existing tables and relationships ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#step-5-track-existing-tables-and-relationships)
- [ Securing the GraphQL endpoint ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#kubernetes-secure)
    - [ Add the HASURA_GRAPHQL_ADMIN_SECRET env var ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#add-the-hasura_graphql_admin_secret-env-var)

- [ (optional) Use the admin secret key with the CLI ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#optional-use-the-admin-secret-key-with-the-cli)
- [ Hasura GraphQL Engine server logs ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#kubernetes-logs)
- [ Updating Hasura GraphQL Engine ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#kubernetes-update)
    - [ Step 1: Check the latest release version ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#step-1-check-the-latest-release-version)

- [ Step 2: Update the container image ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#step-2-update-the-container-image)

- [ Step 3: Rollout the change ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#step-3-rollout-the-change)
- [ Advanced ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#advanced)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)