# Get Started with Hasura Cloud & CockroachDB

## Introduction​

### Step 1: Create an account on Hasura Cloud and create a new Hasura Project​

Navigate to[ cloud.hasura.io ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-cloud-hasura-io&tech=default&skip_onboarding=true),
and create a new Hasura Cloud account.

Once you create a project on Hasura Cloud, hit the "Launch Console" button to open the Hasura Console for your project.

Image: [ Connect new or existing database ](https://hasura.io/docs/assets/images/create-project-79b9d7bf1904f9467739017a6dd81666.png)

### Step 2: Add your CockroachDB database as a source to Hasura​

In the `Data > Data Manager > Connect Existing Database` section on the Console, select `CockroachDB` from the `Data Source Driver` dropdown and add the connection string. As CockroachDB speaks the same protocol as Postgres, the
connection string will start with `postgres://` , i.e, there is no difference between CockroachDB's connection strings
and Postgres’s connection strings.

CockroachDB requires an SSL root certificate by default. To use this, you must set an environment variable for your
Hasura GraphQL Engine instance with the contents of the certificate as the value, and then specify the name of the
environment variable as the `SSL Root Certificate` .

Note

Pay extra notice that if you use one of CockroachDB's serverless databases, you will be prompted with a connection
string that contains the parameter `sslverify` . You must add this parameter manually via the "SSL Certificates Settings"
section.

Depending on how you have configured[ Network Authorization ](https://www.cockroachlabs.com/docs/cockroachcloud/network-authorization.html)on your
CockroachDB Serverless database, you will also need to either add the Hasura IP (which can be found on the `General` tab
of your Hasura Project details page) to the allowlist, or setup a[ dedicated VPC ](https://hasura.io/docs/latest/hasura-cloud/dedicated-vpc/).

Image: [ Add source ](https://hasura.io/docs/assets/images/1-add-source-cloud-89cc1beb76ee33cf4ba07ed4d40d2b9d.png)

Once you add the database, you'll see your database pop up on the sidebar.

### Step 3: Track existing tables or create new tables​

If you have existing tables, head to the database page by clicking on the database name on the sidebar. You should see a
list of tables.

Track tables selectively or all of them so that Hasura can introspect the tables and create the corresponding GraphQL
schema.

Image: [ Track tables ](https://hasura.io/docs/assets/images/4-track-tables-c9e8ddb88c5018cde462902f03ac5ca2.png)

If you have foreign keys, you'll also see suggested relationships. Again, you can choose to track them selectively or
all at once.

Image: [ Track foreign-key relationships ](https://hasura.io/docs/assets/images/5-track-rels-5c91f10b7840ad85deb88d56a00f5926.png)

If you don't have existing tables, go ahead and add new tables and data and try out some queries, just like with a
regular Postgres database.

Image: [ Add a new table ](https://hasura.io/docs/assets/images/6-add-tables-905abba9bb1feb68859b368a3f152570.png)

### Step 4: Try out a GraphQL query​

Head to the `API` tab in the Console and try running a GraphQL query! Use the explorer sidebar on GraphQL to get help in
creating a GraphQL query.

Image: [ Make GraphQL query ](https://hasura.io/docs/assets/images/7-make-graphql-query-2de8b8336e323c7f7882ba5b0de061c8.png)

## Keep up to date​

Hasura currently supports[ queries ](https://hasura.io/docs/latest/queries/postgres/index/),[ relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/), and[ mutations ](https://hasura.io/docs/latest/mutations/postgres/index/)on
CockroachDB.

Please refer to the[ Postgres docs ](https://hasura.io/docs/latest/queries/postgres/index/)on how you can try these features out via the Console
or by manipulating Metadata in JSON/YAML directly.

If you'd like to stay informed about the status of CockroachDB support, subscribe to our newsletter and join our
discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/cloud/#introduction)
    - [ Step 1: Create an account on Hasura Cloud and create a new Hasura Project ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/cloud/#step-1-create-an-account-on-hasura-cloud-and-create-a-new-hasura-project)

- [ Step 2: Add your CockroachDB database as a source to Hasura ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/cloud/#step-2-add-your-cockroachdb-database-as-a-source-to-hasura)

- [ Step 3: Track existing tables or create new tables ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/cloud/#step-3-track-existing-tables-or-create-new-tables)

- [ Step 4: Try out a GraphQL query ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/cloud/#step-4-try-out-a-graphql-query)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/postgres/cockroachdb/getting-started/cloud/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)