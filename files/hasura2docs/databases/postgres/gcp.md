# Connecting Hasura to a Google Cloud SQL Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ Google Cloud SQL Postgres database ](https://cloud.google.com/sql)to a Hasura
instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring Google Cloud SQL Postgres and are interested in
migrating an existing Postgres database - such as from Heroku - check out their[ docs ](https://cloud.google.com/database-migration/docs/postgres)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/gcp/#create-pg-db-gcp).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
Postgres Database URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Postgres DB on GCP​

Note

If you have an existing Postgres database on GCP, you can skip this step and move on to[ step 4 ](https://hasura.io/docs/latest/databases/postgres/gcp/#allow-connections).

Log into the[ GCP console ](https://console.cloud.google.com/).

On the left-side navigation, scroll down to `Storage` and click on `SQL` :

Image: [ Navigate to SQL in GCP ](https://hasura.io/docs/assets/images/navigate-to-sql-b51fa2f423b5367b08f746c5fc8626a7.png)

On the top, click on `Create instance` :

Image: [ Create database instance in GCP ](https://hasura.io/docs/assets/images/create-instance-eccce009582ef540ea272255dcb01c2c.png)

Select Postgres:

Image: [ Select Postgres database instance in GCP ](https://hasura.io/docs/assets/images/select-postgres-57e23647e4f55d532f9cc0294b57ba0b.png)

Select an instance ID, as well as a default user password. If required, choose a specific region and zone.

Image: [ Configure database instance in GCP ](https://hasura.io/docs/assets/images/configure-instance-b9f05c6da0bea05c7c850ed428210683.png)

Then click `Create` .

## Step 4: Allow connections to your DB from Hasura​

On the dashboard of your GCP database instance, on the left sidebar, click on `Connections` . Then scroll down to the
checkbox `Public IP` , and click `+ Add network` :

Image: [ Navigate to connections in GCP ](https://hasura.io/docs/assets/images/connections-9d857907436dc1828e0a536921a0d4fd.png)

You can choose an optional name (e.g. "Hasura").

If using Hasura Cloud, from your project's dashboard, copy the Hasura Cloud IP address:

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/hasura-cloud-ip-86181dcc16cbac471b8a2c5237a23b24.png)

Note

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

Enter the Hasura IP address that you copied:

Image: [ Add a new network in GCP ](https://hasura.io/docs/assets/images/add-network-ca7fa284d18aac4b4e2baf24024b2ec0.png)

Then click `Save` .

Note

If you're using a database user other than the default one, make sure to give it the right[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#managed-pg-permissions).

## Step 5: Construct the database connection URL​

The structure of the database connection URL looks as follows:

`postgresql:// < user-name > : < password > @ < public-ip > : < postgres-port > /`

- `user-name` : If you have a separate database user, the user name will be their name. If you didn't specify a user, the
default user name is `postgres` .
- `password` : If you have a separate database user, use their password. Otherwise, use the password that you chose when
creating the database.
- `public-ip` : The public IP can be obtained by clicking on `Overview` on the left-side navigation and then scrolling
down to `Connect to this instance` :


Image: [ Find the public IP for a Google Cloud SQL Postgres database ](https://hasura.io/docs/assets/images/public-ip-fb46bb7a20ecba34f6fb96ee0b464d84.png)

- `postgres-port` : The default port for Postgres is `5432` if not specified otherwise.
- `db` : The DB is `postgres` by default unless otherwise specified.


## Step 6: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in[ step 5 ](https://hasura.io/docs/latest/databases/postgres/gcp/#construct-db-url-gcp):

Image: [ Database setup ](https://hasura.io/docs/assets/images/GCP-complete-4a8127b097084b1f1f6fdad322aa196f.png)

Then click `Connect Database` .

Note

For security reasons, it is recommended to set database URLs as[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)and
using the env vars to connect to the databases in place of the raw database URLs.

Voilà. You are ready to start developing.

Image: [ Hasura Console ](https://hasura.io/docs/assets/images/hasura-console-5685707ef939a6ca7cc2c5fb6ed7dda8.png)

## Step 7 (optional): Enable SSL connection​

### Step 7.1 Get GCP SSL Certs​

Google Cloud (GCP) SQL makes the following SSL/TLS certificates available for download:

- A server certificate saved as `server-ca.pem`
- A client public key certificate saved as `client-cert.pem`
- A client private key saved as `client-key.pem`


Note Please refer to the

[ Google Cloud Documentation ](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance?&_ga=2.87107544.-1769733723.1651179247#server-certs)for detailed information about the different certs.

Download these certs to your local drive.

### Step 7.2: Add env vars​

If using Hasura Cloud, go to your project and add the following env vars:

(Open the cert files using your favorite text editor, select all the contents and copy them to the clipboard)

| Env Var Name | Value |
|---|---|
|  `SSL_ ROOTCERT_ GCP`  | Contents from `server-ca. pem`  |
|  `SSL_ CERT_ GCP`  | Contents from `client-cert. pem`  |
|  `SSL_ KEY_ GCP`  | Contents from `client-key. pem`  |


Here is how your Hasura Cloud env vars setup should look like:

Image: [ Hasura Cloud Env Vars ](https://hasura.io/docs/assets/images/cloud-gcp-env-vars-7281e056f22e96da5eeddd17b9ad3f14.png)

Note

If you're using a self-hosted solution, you can set these env vars in your `docker-compose.yml` file.

### Step 7.3: Configure SSL settings​

Open the Console of your Hasura Project, go to the `Data -> Manage -> [db-name] -> Edit` page.

Under `Connection Settings` add the following SSL certificate settings:

| Field Name | Value |
|---|---|
|  `SSL Mode`  |  `verify-ca` (select from dropdown) |
|  `SSL Root Certificate`  |  `SSL_ ROOTCERT_ GCP`  |
|  `SSL Certificate`  |  `SSL_ CERT_ GCP`  |
|  `SSL Key`  |  `SSL_ KEY_ GCP`  |


Here is how the setup should look like:

Image: [ Hasura Console SSL Config Setup ](https://hasura.io/docs/assets/images/ssl-config-setup-204885ea561b80045ccf8a88ea8a8406.png)

Finally, click on the `Update Connection` button to apply the SSL settings.

Image: [ Update Connection Button ](https://hasura.io/docs/assets/images/update-connection-button-66041e2c3b1ffb6aaec1ea9a2e271635.png)

## Next steps​

- You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.
- If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).


You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.

If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).

Image: [ Project actions ](https://hasura.io/docs/assets/images/project-manage-5b37a214a39b39b6287136606da021c4.png)

Note

For more information on which Postgres features we support, check out[ this page ](https://hasura.io/docs/latest/databases/feature-support/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/gcp/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/gcp/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/gcp/#create-hasura-project-gcp)
- [ Step 3: Create a Postgres DB on GCP ](https://hasura.io/docs/latest/databases/postgres/gcp/#create-pg-db-gcp)
- [ Step 4: Allow connections to your DB from Hasura ](https://hasura.io/docs/latest/databases/postgres/gcp/#allow-connections)
- [ Step 5: Construct the database connection URL ](https://hasura.io/docs/latest/databases/postgres/gcp/#construct-db-url-gcp)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/gcp/#step-6-finish-connecting-the-database)
- [ Step 7 (optional): Enable SSL connection ](https://hasura.io/docs/latest/databases/postgres/gcp/#step-7-optional-enable-ssl-connection)
    - [ Step 7.1 Get GCP SSL Certs ](https://hasura.io/docs/latest/databases/postgres/gcp/#step-71-get-gcp-ssl-certs)

- [ Step 7.2: Add env vars ](https://hasura.io/docs/latest/databases/postgres/gcp/#step-72-add-env-vars)

- [ Step 7.3: Configure SSL settings ](https://hasura.io/docs/latest/databases/postgres/gcp/#step-73-configure-ssl-settings)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/gcp/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)