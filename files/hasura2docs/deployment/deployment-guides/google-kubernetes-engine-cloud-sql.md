# Hasura GraphQL Engine on Google Cloud Platform with Kubernetes engine and Cloud SQL

## Introduction​

This is a guide on deploying the Hasura GraphQL Engine on the[ Google
Cloud Platform ](https://cloud.google.com/)using[ Kubernetes
engine ](https://cloud.google.com/kubernetes-engine/)to run Hasura and
PostgreSQL backed by[ Cloud SQL ](https://cloud.google.com/sql/).

## Prerequisites​

- Google Cloud account with billing enabled (or a[ free trial ](https://cloud.google.com/free/))
- `gcloud` CLI ([ install ](https://cloud.google.com/sdk/))
- `kubectl` CLI ([ install ](https://kubernetes.io/docs/tasks/tools/install-kubectl/))


The Actions mentioned below can be done using the Google Cloud Console
and the `gcloud` CLI. But, for the sake of simplicity in documentation,
we are going to use `gcloud` CLI, so that commands can be easily
copy-pasted and executed.

Once the CLI is installed, initialize the SDK:

`gcloud init`

## Create a Google Cloud Project​

A Google Cloud Project is used to group together resources. We'll create
a project called `hasura` for this guide.

`gcloud projects create hasura`

## Create a Google Cloud SQL Postgres instance​

Create a Cloud SQL Postgres instance called `hasura-postgres` in the `us-west2` region.

```
gcloud sql instances create hasura-postgres --database-version POSTGRES_9_6  \
       --cpu  1  --memory 3840MiB --region us-west2 --project hasura
```

Once the instance is created, set a password for the default `postgres` user. Make sure you substitute `[PASSWORD]` with a strong password.

```
gcloud sql  users  set-password postgres --instance hasura-postgres  \
       --password  [ PASSWORD ]  --project hasura
```

## Create a Kubernetes Cluster​

Before creating the cluster, we need to enable the Kubernetes engine
API. Visit the below link in a browser to enable the API. Replace `hasura` at the end of the URL with your project name, in case you're
not using the same name. Note that, you will need a billing account
added to the project to enable the API.

`https://console.cloud.google.com/apis/api/container.googleapis.com/overview?project = hasura`

Once the API is enabled, create a new Kubernetes cluster called `hasura-k8s` in the `us-west2-a` zone with 1 node.

```
gcloud container clusters create hasura-k8s --zone us-west2-a  \
       --num-nodes  1  --project hasura
```

## Set up Cloud SQL Proxy Credentials​

In order to connect to the Cloud SQL instance, we need to set up a proxy
that will forward connections from Hasura to the database instance. For
that purpose, the credentials to access the instance need to be added to
the cluster.

Create a service account and download the JSON key file by following[ this guide ](https://cloud.google.com/sql/docs/postgres/sql-proxy#create-service-account).

Or if you're overwhelmed with that guide, ensure the following:

1. Enable[ Cloud SQL Admin API ](https://console.developers.google.com/apis/api/sqladmin.googleapis.com/overview?project=hasura)for your project.
2. Create a new[ Service Account ](https://console.cloud.google.com/iam-admin/serviceaccounts/?project=hasura).
3. Select `Cloud SQL Admin` as the role.
4. Click `Create Key` to download the JSON file.


Create a Kubernetes secret with this JSON key file; replace `[JSON_KEY_FILE_PATH]` with the filename including the complete path of
the download JSON key file.

```
kubectl create secret generic cloudsql-instance-credentials  \
        --from-file = credentials.json = [ JSON_KEY_FILE_PATH ]
```

Create another secret with the database username and password (use the `[PASSWORD]` used earlier):

```
kubectl create secret generic cloudsql-db-credentials  \
        --from-literal = username = postgres --from-literal = password = [ PASSWORD ]
```

## Deploy the Hasura GraphQL Engine​

Download the `deployment.yaml` file:

`wget  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/google-cloud-k8s-sql/deployment.yaml`

Get the `[INSTANCE_CONNECTION_NAME]` using the following command and
note it down.

```
gcloud sql instances describe hasura-postgres  \
       --format = "value(connectionName)"  --project hasura
```

Edit `deployment.yaml` and replace `[INSTANCE_CONNECTION_NAME]` with
this value. It should look like `hasura:us-west2:hasura-postgres` if
you've followed this guide without modifying any names.

Create the deployment:

`kubectl apply -f deployment.yaml`

Ensure the pods are running:

`kubectl get pods`

If there are any errors, check the logs of the GraphQL Engine:

`kubectl logs deployment/hasura -c graphql-engine`

## Expose GraphQL Engine​

### HTTP​

Now that we have Hasura running, let's expose it on an IP using a
LoadBalancer.

```
kubectl expose deploy/hasura  \
     --port  80  --target-port  8080   \
     --type LoadBalancer
```

#### Open the Hasura Console​

Wait for the external IP to be allocated, check the status using the
command below. It usually takes a couple of minutes.

`kubectl get  service`

Once the IP is allocated, visit the IP in a browser and it should open
the Console.

### HTTPS​

Let's expose Hasura with[ Ingress ](https://cloud.google.com/kubernetes-engine/docs/concepts/ingress/).
Create service:

```
apiVersion :  v1
kind :  Service
metadata :
   labels :
     app :  hasura
   name :  hasura
spec :
   ports :
     -   protocol :  TCP
       port :   80
       targetPort :   8080
   selector :
     app :  hasura
   type :  NodePort
```

Create Managed Certificate:

```
apiVersion :  networking.gke.io/v1beta1
kind :  ManagedCertificate
metadata :
   name :  hasura - cert
spec :
   domains :
     -  example.com
```

Create Ingress:

```
apiVersion :  extensions/v1beta1
kind :  Ingress
metadata :
   name :  basic - ingress
   annotations :
     networking.gke.io/managed-certificates :   'hasura-cert'
spec :
   rules :
     -   host :  example.com
       http :
         paths :
           -   backend :
               serviceName :  hasura
               servicePort :   80
```

## Logs​

Check the status for pods to see if they are running. If there are any
errors, check the logs of the GraphQL Engine:

`kubectl logs deployment/hasura -c graphql-engine`

You might also want to check the logs for cloudsql-proxy:

`kubectl logs deployment/hasura -c cloudsql-proxy`

The username and password used by Hasura to connect to the database
comes from a Kubernetes secret object `cloudsql-db-credentials` that we
created earlier.

## Tearing down​

To clean up the resources created, just delete the Google Cloud Project:

`gcloud projects delete hasura`

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#introduction)
- [ Prerequisites ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#prerequisites)
- [ Create a Google Cloud Project ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#create-a-google-cloud-project)
- [ Create a Google Cloud SQL Postgres instance ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#create-a-google-cloud-sql-postgres-instance)
- [ Create a Kubernetes Cluster ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#create-a-kubernetes-cluster)
- [ Set up Cloud SQL Proxy Credentials ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#set-up-cloud-sql-proxy-credentials)
- [ Deploy the Hasura GraphQL Engine ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#deploy-the-hasura-graphql-engine)
- [ Expose GraphQL Engine ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#expose-graphql-engine)
    - [ HTTP ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#http)

- [ HTTPS ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#https)
- [ Logs ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#gc-kubernetes-logs)
- [ Tearing down ](https://hasura.io/docs/latest/deployment/deployment-guides/google-kubernetes-engine-cloud-sql/#tearing-down)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)