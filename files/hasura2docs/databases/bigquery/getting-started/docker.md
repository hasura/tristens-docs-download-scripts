# Get Started with Docker (Hasura and BigQuery)

Get the Hasura docker-compose file:

```
# in a new directory run
wget  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/docker-compose/docker-compose.yaml
# or run
curl  https://raw.githubusercontent.com/hasura/graphql-engine/stable/install-manifests/docker-compose/docker-compose.yaml -o docker-compose.yaml
```

The following command will run Hasura along with a Postgres database required for its functioning.

`$  docker  compose up -d`

Check if the containers are running:

```
$  docker   ps
CONTAINER ID IMAGE                  .. . CREATED STATUS PORTS           .. .
097f58433a2b hasura/graphql-engine  .. . 1m ago  Up 1m   8080 - > 8080 /tcp  .. .
b0b1aac0508d postgres               .. . 1m ago  Up 1m   5432 /tcp        .. .
Please  do  note that you will see a Postgres database running,  which  is used by Hasura to store its configuration  ( Hasura Metadata ) .
```

Head to `http://localhost:8080/console` to open the Hasura Console.

## Connecting to a BigQuery project​

### Pre-requisites​

Hasura GraphQL Engine requires the following to connect to a BigQuery project:

- The[ project Id ](https://support.google.com/googleapi/answer/7014113?hl=en)
- The[ datasets ](https://cloud.google.com/bigquery/docs/datasets-intro)that can be exposed over graphql have to be
explicitly listed.
- A[ Service Account ](https://cloud.google.com/iam/docs/service-accounts)to query the project.


### Creating a Service Account​

- In Google Cloud's console, head to your BigQuery project.
- Go to `IAM & Admin > Service Accounts > Create Service Account`


In Google Cloud's console, head to your BigQuery project.

Go to `IAM & Admin > Service Accounts > Create Service Account` 

Image: [ Create a service account on GCP ](https://hasura.io/docs/assets/images/1-service-account-885cfcecd0ae792ecbcce920266f2c43.png)

- Give it a name, and under roles, and grant these 3 roles:
    - `BigQuery Metadata Viewer`

- `BigQuery Data Viewer`

- `BigQuery Job User`


Image: [ Add roles to service account on GCP ](https://hasura.io/docs/assets/images/2-service-account-details-8fea0aa79db2e56eed270c33d589a62a.png)

- Click on the created service account, `Keys > ADD KEY > Create New Key > JSON > Create` . This will download a service
account file on your computer.


### Connect BigQuery to Hasura​

- Update Graphql engine with an environment variable set to the contents of the service account.


For example, this could be done as follows if you are using Docker:

`docker  run -e  BIGQUERY_SA_ACCOUNT = $( cat  /path/to/the/service-account.json )   < rest-of-the-flags >`

- Head to the Console, in the `Connect Existing Database` page, choose `Environment Variable` under `Connect Via` , and
fill in the necessary details:


Image: [ Connect existing BigQuery database in Hasura Cloud ](https://hasura.io/docs/assets/images/bigquery-add-service-account_console_2.12.1-d320ec71a03ddd7b66d86c47ac35f1fe.png)

Image: [ Connect existing BigQuery database in Console ](https://hasura.io/docs/assets/images/connect-big-query-db_console_2.10.1-189535627b354c9a6f6330b491636859.png)

You should now be able to track the tables that are part of the specified tables and configure relationships between
them. As BigQuery lacks foreign key constraints, the Hasura Console cannot suggest relationships, so all relationships between
BigQuery tables have to be manually configured.

## Try out a GraphQL query​

Head to the `API` tab in the Console and try running a GraphQL query! Use the explorer sidebar on GraphQL to get help in
creating a GraphQL query.

Image: [ Make GraphQL query in Hasura ](https://hasura.io/docs/assets/images/bigquery_api-query_2.12-9fbef7bc50041416df45501da1b8de68.png)

### What did you think of this doc?

- [ Connecting to a BigQuery project ](https://hasura.io/docs/latest/databases/bigquery/getting-started/docker/#connecting-to-a-bigquery-project)
    - [ Pre-requisites ](https://hasura.io/docs/latest/databases/bigquery/getting-started/docker/#pre-requisites)

- [ Creating a Service Account ](https://hasura.io/docs/latest/databases/bigquery/getting-started/docker/#creating-a-service-account)

- [ Connect BigQuery to Hasura ](https://hasura.io/docs/latest/databases/bigquery/getting-started/docker/#connect-bigquery-to-hasura)
- [ Try out a GraphQL query ](https://hasura.io/docs/latest/databases/bigquery/getting-started/docker/#try-out-a-graphql-query)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)