# Run Hasura GraphQL Engine Using Docker

## Introduction​

This guide will help you deploy the Hasura GraphQL Engine and a Postgres database to store its Metadata using Docker
Compose.

## Deploying Hasura using Docker​

### Prerequisites​

- [ Docker ](https://docs.docker.com/install/)
- [ Docker Compose ](https://docs.docker.com/compose/install/)


### Step 1: Get the docker-compose file​

The[ hasura/graphql-engine/install-manifests ](https://github.com/hasura/graphql-engine/tree/stable/install-manifests)repo contains all installation manifests required to deploy Hasura anywhere. Get the docker compose file from there:

```
# in a new directory run
wget  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/docker-compose/docker-compose.yaml
# or run
curl  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/docker-compose/docker-compose.yaml -o docker-compose.yml
```

### Step 2: Run Hasura GraphQL Engine​

The following command will run Hasura GraphQL Engine along with a Postgres database to store its Metadata.

`$  docker  compose up -d`

Check if the containers are running:

```
$  docker   ps
CONTAINER ID IMAGE                  .. . CREATED STATUS PORTS           .. .
097f58433a2b hasura/graphql-engine  .. . 1m ago  Up 1m   8080 - > 8080 /tcp  .. .
b0b1aac0508d postgres               .. . 1m ago  Up 1m   5432 /tcp        .. .
```

## Securing the GraphQL endpoint​

To make sure that your GraphQL endpoint and the Hasura Console are not publicly accessible, you need to configure an
admin secret key.

### Run the Docker container with an admin-secret env var​

```
graphql-engine :
   image :  hasura/graphql - engine : v2.0.0
   environment :
     HASURA_GRAPHQL_METADATA_DATABASE_URL :  postgres : //postgres : postgrespassword@postgres : 5432/postgres
     HASURA_GRAPHQL_ADMIN_SECRET :  myadminsecretkey
   ...
```

Note

The `HASURA_GRAPHQL_ADMIN_SECRET` should never be passed from the client to the Hasura GraphQL Engine as it would give
the client full admin rights to your Hasura instance. See[ Authentication & Authorization ](https://hasura.io/docs/latest/auth/overview/)for
information on setting up authentication.

## Hasura GraphQL Engine server logs​

You can check the logs of the Hasura GraphQL Engine deployed using Docker by checking the logs of the GraphQL Engine
container:

```
$  docker   ps
CONTAINER ID IMAGE                  .. . CREATED STATUS PORTS           .. .
097f58433a2b hasura/graphql-engine  .. . 1m ago  Up 1m   8080 - > 8080 /tcp  .. .
b0b1aac0508d postgres               .. . 1m ago  Up 1m   5432 /tcp        .. .
$  docker  logs 097f58433a2b
{ "timestamp" : "2018-10-09T11:20:32.054+0000" ,  "level" : "info" ,  "type" : "http-log" ,  "detail" : { "status" :200,  "query_hash" : "01640c6dd131826cff44308111ed40d7fbd1cbed" ,  "http_version" : "HTTP/1.1" ,  "query_execution_time" :3.0177627e-2,  "request_id" :null,  "url" : "/v1/graphql" ,  "user" : { "x-hasura-role" : "admin" } ,  "ip" : "127.0.0.1" ,  "response_size" :209329,  "method" : "POST" ,  "detail" :null } }
.. .
```

 **See:** 

- [ https://docs.docker.com/config/containers/logging ](https://docs.docker.com/config/containers/logging)for more
details on logging in Docker.
- [ Hasura GraphQL Engine logs ](https://hasura.io/docs/latest/deployment/logging/)for more details on Hasura logs.


## Updating Hasura GraphQL Engine​

This guide will help you update the Hasura GraphQL Engine running with Docker. This guide assumes that you already have
Hasura GraphQL Engine running with Docker.

### Step 1: Check the latest release version​

The current latest version is:

```
hasura/graphql-engine:
v2.36.0
```

All the versions can be found at:[ https://github.com/hasura/graphql-engine/releases ](https://github.com/hasura/graphql-engine/releases)

### Step 2: Update the Docker image​

In the `docker compose` command that you're running, update the image tag to this latest version.

For example, if you had:

```
graphql-engine :
   image :  hasura/graphql - engine : v1.2.0
```

you should change it to:

```
graphql-engine:
image: hasura/graphql-engine:
v2.36.0
```

Note

If you are downgrading to an older version of the GraphQL Engine you might need to downgrade your Metadata catalogue
version as described in[ Downgrading Hasura GraphQL Engine ](https://hasura.io/docs/latest/deployment/downgrading/)

## Docker networking​

Sometimes you might want to connect Hasura running in Docker with APIs (e.g. auth webhooks, Event Triggers, Remote
Schemas) that are either running outside of Docker or in a different Docker container. Depending on the setting, the
network config is different. This section shows how to connect in each of these use cases.

### Network config​

- Linux
- Mac
- Windows


| Connection | Config | Comment |
|---|---|---|
|  **Hasura to API (outside Docker)**  |     1. With `--net=host` , `localhost:3000`
    2. Otherwise, `<docker-bridge-ip>:3000` , e.g. `172.17.0.1:3000`
 |     1. Assuming the API is running on port `3000`
    2. The Docker bridge IP can be found via `ifconfig`
 |
|  **API (outside Docker) to Hasura**  |  `localhost:8080`  | Hasura runs on port `8080` by default |
|  **Hasura to API (both in docker-compose)**  | service name, e.g.: `api:3000`  | Assuming the API is running on port `3000`  |
|  **API to Hasura (both in docker-compose)**  | service name, e.g.: `hasura:8080`  | Hasura runs on port `8080` by default |
|  **Hasura to API (both running with separate docker run)**  | Docker internal IP address | Can be obtained with `docker inspect`  |
|  **API to Hasura (both running with separate docker run)**  | Docker internal IP address | Can be obtained with `docker inspect`  |


1. With `--net=host` , `localhost:3000`
2. Otherwise, `<docker-bridge-ip>:3000` , e.g. `172.17.0.1:3000`


1. Assuming the API is running on port `3000`
2. The Docker bridge IP can be found via `ifconfig`


| Connection | Config | Comment |
|---|---|---|
|  **Hasura to API (outside Docker)**  |  `host.docker.internal:3000`  | Assuming the API is running on port `3000`  |
|  **API (outside Docker) to Hasura**  |  `localhost:8080`  | Hasura runs on port `8080` by default |
|  **Hasura to API (both in docker-compose)**  | service name, e.g.: `api:3000`  | Assuming the API is running on port `3000`  |
|  **API to Hasura (both in docker-compose)**  | service name, e.g.: `hasura:8080`  | Hasura runs on port `8080` by default |
|  **Hasura to API (both running with separate docker run)**  | Docker internal IP address | Can be obtained with `docker inspect`  |
|  **API to Hasura (both running with separate docker run)**  | Docker internal IP address | Can be obtained with `docker inspect`  |


| Connection | Config | Comment |
|---|---|---|
|  **Hasura to API (outside Docker)**  |  `host.docker.internal:3000`  | Assuming the API is running on port `3000`  |
|  **API (outside Docker) to Hasura**  |  `localhost:8080`  | Hasura runs on port `8080` by default |
|  **Hasura to API (both in docker-compose)**  | service name, e.g.: `api:3000`  | Assuming the API is running on port `3000`  |
|  **API to Hasura (both in docker-compose)**  | service name, e.g.: `hasura:8080`  | Hasura runs on port `8080` by default |
|  **Hasura to API (both running with separate docker run)**  | Docker internal IP address | Can be obtained with `docker inspect`  |
|  **API to Hasura (both running with separate docker run)**  | Docker internal IP address | Can be obtained with `docker inspect`  |


### Advanced​

Learn more about Docker specific networking in the[ Docker documentation ](https://docs.docker.com/network/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#introduction)
- [ Deploying Hasura using Docker ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#deploying-hasura-using-docker)
    - [ Prerequisites ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#prerequisites)

- [ Step 1: Get the docker-compose file ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#step-1-get-the-docker-compose-file)

- [ Step 2: Run Hasura GraphQL Engine ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#step-2-run-hasura-graphql-engine)
- [ Securing the GraphQL endpoint ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#docker-secure)
    - [ Run the Docker container with an admin-secret env var ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#run-the-docker-container-with-an-admin-secret-env-var)
- [ Hasura GraphQL Engine server logs ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#docker-logs)
- [ Updating Hasura GraphQL Engine ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#docker-update)
    - [ Step 1: Check the latest release version ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#step-1-check-the-latest-release-version)

- [ Step 2: Update the Docker image ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#step-2-update-the-docker-image)
- [ Docker networking ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#docker-networking)
    - [ Network config ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#network-config)

- [ Advanced ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-logs/#advanced)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)