# Deploy Hasura GraphQL Engine on Kubernetes with Helm Chart

To help you easily install Hasura GraphQL Engine on Kubernetes, we're happy to provide a[ Helm Chart repository ](https://github.com/hasura/helm-charts)with GraphQL Engine and its ecosystem, including:

- [ GraphQL Engine ](https://github.com/hasura/helm-charts/tree/main/charts/graphql-engine): the chart deploys the
GraphQL Engine service with a Postgres instance for metadata storage.
- [ Hasura Enterprise Stack ](https://github.com/hasura/helm-charts/tree/main/charts/hasura-enterprise-stack): the
complete end-to-end Hasura GraphQL Engine Enterprise ecosystem with Redis, Observability, Dex (SSO middleware), and
Data Connectors.


In this guide, you will get up and running quickly with the Hasura GraphQL Engine and a Postgres database on Kubernetes
using Helm Chart.

### Prerequisites​

- A working[ Kubernetes v1.18+ cluster ](https://kubernetes.io/docs/setup/production-environment/)
- [ Helm v3 installed ](https://helm.sh/docs/intro/install/)on your machine.
- [ Kubectl installed ](https://kubernetes.io/docs/tasks/tools/)and configured to be able to connect to the Kubernetes
cluster.


### Step 1: Configure a Hasura Helm repository​

Run this command to add Hasura Helm repository:

`helm repo  add  hasura https://hasura.github.io/helm-charts`

### Step 2: Install the Helm Chart​

Run the following command to install both the Hasura GraphQL Engine and a Postgres database. We assume that the release
name is `hasura` and the admin secret is `hasura` :

`helm  install  hasura --set secret.adminSecret = hasura hasura/graphql-engine`

Keep your admin secret strong and safe

Remember to set strong admin secrets before going live.

After the GraphQL Engine Helm Chart was installed successfully, print Kubernetes pods with `kubectl` to verify.

```
NAME                                  READY   STATUS    RESTARTS      AGE
hasura-graphql-engine-6cc69694dd-r4dnh    1 /1     Running    1   ( 75s ago )    2m58s
hasura-postgres-5fd95db548-f4vhg          1 /1     Running    0              2m58s
```

By default, the Helm Chart doesn't enable ingress. You need to enable port-forwarding on the `graphql-engine` pod to
localhost.

`kubectl port-forward hasura-graphql-engine-6cc69694dd-r4dnh  8080 :8080`

Hasura ships with a Postgres database

 **Hasura relies on a Postgres database to store its metadata** , and this database can also be used to store your
application data.

If you'd like to connect another type of database for storing application data, check out our list of[ supported databases ](https://hasura.io/docs/latest/databases/overview/).

Open the Hasura Console by navigating to `http://localhost:8080/console` .

### Step 3: Try out Hasura​

#### Create a table and insert some demo data​

On the Hasura Console, navigate to `Data -> Create table` and create a sample table called `profiles` with the following
columns:

```
profiles  (
  id  SERIAL   PRIMARY   KEY ,   -- serial -> auto-incrementing integer
  name  TEXT
)
```

Image: [ Create a table ](https://hasura.io/docs/assets/images/create-profile-table-f93963eda2987dc06c5d2a9377a37f8a.png)

Now, insert some sample data into the table using the `Insert Row` tab of the `profiles` table.

#### Try out a query​

Head to the `API` tab in the Console and try running the following query:

```
query   {
   profiles   {
     id
     name
   }
}
```

You'll see that you get all the inserted data!

Image: [ Try out a query ](https://hasura.io/docs/assets/images/profile-query-5be8a917069f505b215cbf87ea953dfd.png)

### Enable GraphQL Engine Enterprise​

You can set the Enterprise License Key value when installing the Helm chart to enable Enterprise features.

`helm  install  hasura --set secret.adminSecret = hasura --set secret.eeLicenseKey = < license-key >  hasura/graphql-engine`

### Advanced configuration​

You can see full configuration values at[ the Github repository ](https://github.com/hasura/helm-charts/blob/main/charts/graphql-engine/values.yaml)and[ example values ](https://github.com/hasura/helm-charts/tree/main/charts/graphql-engine/examples)to get started.

## Hasura Enterprise Stack​

If you intend to install the all-in-one deployment stack with Hasura Enterprise and its ecosystem you can try the[ hasura-enterprise-stack ](https://github.com/hasura/helm-charts/tree/main/charts/hasura-enterprise-stack)Helm Chart.
The Helm Chart is a collection of sub-charts that includes:

- GraphQL Engine Helm Chart.
- [ Bitnami Redis(R) ](https://github.com/bitnami/charts/tree/main/bitnami/redis)for caching and rate limit.
- [ Kube Prometheus Stack ](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)for observability.
- [ Jeager ](https://github.com/jaegertracing/helm-charts)for trace collector.
- [ Dex ](https://github.com/dexidp/helm-charts/tree/master/charts/dex)for[ Single Sign-on middleware ](https://hasura.io/docs/latest/enterprise/sso/config/#other-protocols).
- Data connector Helm Charts (GraphQL, Mongo, etc...).


Those sub-charts are disabled by default. You can enable desired charts only.

### Prerequisites​

- A working Kubernetes v1.18+ cluster
- [ Helm v3 installed ](https://helm.sh/docs/intro/install/)on your machine.
- [ Kubectl installed ](https://kubernetes.io/docs/tasks/tools/)and configured to be able to connect the Kubernetes cluster.


### Step 1: Configure Hasura Helm repository​

Run this command to add Hasura Helm repository:

`helm repo  add  hasura https://hasura.github.io/helm-charts`

### Step 2: Install the helm chart​

By default, the Helm Chart will start with the basic GraphQL Engine chart above. In this guide, we will enable Hasura
Enterprise with a Redis cache.

Create an extended `values.yaml` file locally with the following values:

```
global :
   redis :
     enabled :   true
     password :  redispassword
graphql-engine :
   secret :
     adminSecret :   'hasura'
     eeLicenseKey :   '<set your license key here>'
```

Then install the Helm Chart with the file.

`helm  install  hasura -f ./values.yaml hasura/hasura-enterprise-stack`

After the Helm Chart was installed successfully, print Kubernetes pods with `kubectl` to verify.

```
NAME                                  READY   STATUS    RESTARTS   AGE
hasura-graphql-engine-65d75f997f-pkwj9    1 /1     Running    0           11s
hasura-postgres-5fd95db548-6x844          1 /1     Running    0           11s
hasura-redis-master-0                     1 /1     Running    0           11s
hasura-redis-replicas-0                   1 /1     Running    0           11s
```

### Advanced configuration​

You can see full configuration values at[ the Github repository ](https://github.com/hasura/helm-charts/blob/main/charts/hasura-enterprise-stack/values.yaml)and[ example values ](https://github.com/hasura/helm-charts/tree/main/charts/hasura-enterprise-stack/examples)to get
started.

### What did you think of this doc?

- [ Prerequisites ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes-helm/#prerequisites)
- [ Step 1: Configure a Hasura Helm repository ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes-helm/#step-1-configure-a-hasura-helm-repository)
- [ Step 2: Install the Helm Chart ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes-helm/#step-2-install-the-helm-chart)
- [ Step 3: Try out Hasura ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes-helm/#step-3-try-out-hasura)
- [ Enable GraphQL Engine Enterprise ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes-helm/#enable-graphql-engine-enterprise)
- [ Advanced configuration ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes-helm/#advanced-configuration)
- [ Hasura Enterprise Stack ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes-helm/#hasura-enterprise-stack)
    - [ Prerequisites ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes-helm/#prerequisites-1)

- [ Step 1: Configure Hasura Helm repository ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes-helm/#step-1-configure-hasura-helm-repository)

- [ Step 2: Install the helm chart ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes-helm/#step-2-install-the-helm-chart-1)

- [ Advanced configuration ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes-helm/#advanced-configuration-1)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)