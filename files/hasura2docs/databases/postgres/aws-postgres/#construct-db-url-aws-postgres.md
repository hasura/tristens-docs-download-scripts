# Connecting Hasura to an AWS RDS Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ AWS RDS Postgres ](https://aws.amazon.com/rds/)database to a
Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring AWS RDS Postgres and are
interested in migrating an existing Postgres database - such as from Heroku - check out their[ docs ](https://aws.amazon.com/getting-started/hands-on/move-to-managed/migrate-postgresql-to-amazon-rds/)before
continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#construct-db-url-aws-postgres/#create-hasura-project-aws-rds-postgres).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Hasura will prompt you for a
Postgres Database URL. We'll create this in the next step and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/existing-db-setup-0c5807a4a16836b8789e886baee94d37.png)

## Step 3: Create a Postgres DB on AWS​

Note

If you have an existing Postgres database on AWS, you can skip this step and move on to[ step 4 ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#construct-db-url-aws-postgres/#connect-hasura-aws-pg).

Log into the[ AWS console ](https://console.aws.amazon.com//).

On the top left, click on `Services` and type "RDS" into the search field. Then click on `RDS` :

Image: [ Navigate to RDS in AWS ](https://hasura.io/docs/assets/images/search-for-rds-748f2b54a96f41ecc63deaed3d8f96f3.png)

Click the `Create database` button:

Image: [ Create database in AWS ](https://hasura.io/docs/assets/images/create-database-324a0374c3e53254b3dd84b1fd58d08b.png)

In `Engine options` , select `Postgres` as `Engine type` :

Image: [ Select Postgres for RDS instance on AWS ](https://hasura.io/docs/assets/images/rds-select-postgres-e28d6296549bb97373c608739826d14e.png)

Scroll down to `Settings` . Now you can choose a `DB instance identifier` as a name for your database. The `Master username` is `postgres` by default. You can change that if you have to. As for the password, you can click the
checkbox for AWS to auto-generate one for you, or you can type in a password of your choice.

Image: [ Settings for RDS instance on AWS ](https://hasura.io/docs/assets/images/rds-settings-152cd54f3b0b922613db6ca642e1e99a.png)

Scroll down and customize other database options such as `DB instance size` and `Storage` , based on your requirements.

In the `Connectivity` section, expand the `Additional connectivity configuration` . Then set `Public access` to `Yes` and
choose or add a new security group:

Image: [ Connectivity for RDS instance on AWS ](https://hasura.io/docs/assets/images/rds-connectivity-8944046b6e1064dd5c3cd8a996ea0c90.png)

When you're done, at the bottom, click the `Create database` button:

Image: [ Create RDS instance on AWS ](https://hasura.io/docs/assets/images/rds-click-create-c5758c41bfbea304ba0beada94ee3bc4.png)

Note

If you're using a database user other than the default one, make sure to give it the right[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#managed-pg-permissions).

## Step 4: Allow connections to your DB from Hasura​

On the database dashboard, click on `Connectivity & security` . On the right, click on the security group that you
selected or added in[ step 3 ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#create-aws-rds-postgres-db).

Image: [ Find the security group on AWS RDS ](https://hasura.io/docs/assets/images/find-security-group-f15233c1d23b09567e4d4c6f922c99ac.png)

Click on the security group:

Image: [ Click on the security group ](https://hasura.io/docs/assets/images/select-security-group-f631dd08d3f1b910630f59eec43289ca.png)

Click on `Edit inbound rules` :

Image: [ Edit inbound rules for AWS RDS database ](https://hasura.io/docs/assets/images/inbound-rules-b32e2e1aac008a99f949a8c62cbe36bf.png)

Click on `Add rule` :

Image: [ Add an inbound rule for AWS RDS database ](https://hasura.io/docs/assets/images/add-inbound-rule-d756c5ef35869289d8e0b3824da7b8cf.png)

If using Hasura Cloud, from your project's dashboard, copy the Hasura Cloud IP address:

Image: [ Hasura Cloud IP field ](https://hasura.io/docs/assets/images/hasura-cloud-ip-86181dcc16cbac471b8a2c5237a23b24.png)

Note

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

Add the Hasura IP address that you copied:

Image: [ Add the Hasura IP for AWS RDS database ](https://hasura.io/docs/assets/images/add-hasura-ip-6c5348dd912501abe6b8958ea662bcc2.png)

Then click `Save rules` .

## Step 5: Construct the database connection URL​

The structure of the database connection URL looks as follows:

`postgresql:// < user-name > : < password > @ < public-ip > : < postgres-port > / < db >`

On the database dashboard, click on `Connectivity & security` :

Image: [ Construct the database connection string for AWS RDS ](https://hasura.io/docs/assets/images/get-db-connection-string-6a1aa55a7074d7e71758e184c6eec4d2.png)

- `user-name` : If you have a separate database user the user name will be their name. If you didn't specify a user, the
default user name is `postgres` .
- `password` : If you have a separate database user, use their password. Otherwise, use the password that you chose when
creating the database.
- `public-ip` : On the screenshot above, the `Endpoint` is the public IP.
- `postgres-port` : On the screenshot above you can find it under `Port` . The default port for Postgres is `5432` .
- `db` : The DB is `postgres` by default unless otherwise specified.


## Step 6: Finish connecting the database​

Back on the Hasura Console, enter the database URL that we retrieved in[ step 5 ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#construct-db-url-aws-postgres):

Image: [ Database setup ](https://hasura.io/docs/assets/images/connect-db-cloud-aa46779320727922ac336e595a0b2200.png)

Then click `Connect Database` .

Note

For security reasons, it is recommended to set database URLs as[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)and
using the env vars to connect to the databases in place of the raw database URLs.

Voilà. You are ready to start developing.

Image: [ Hasura Console ](https://hasura.io/docs/assets/images/hasura-console-5685707ef939a6ca7cc2c5fb6ed7dda8.png)

## Next steps​

- You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.
- If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).


You can check out our[ 30-Minute Hasura Basics Course ](https://hasura.io/learn/graphql/hasura/introduction/)and other[ GraphQL & Hasura Courses ](https://hasura.io/learn/)for a more detailed introduction to Hasura.

If using Hasura Cloud, you can also click the gear icon to manage your Hasura Cloud project. (e.g. add[ collaborators ](https://hasura.io/docs/latest/hasura-cloud/projects/collaborators/),[ env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/env-vars/)or[ custom domains ](https://hasura.io/docs/latest/hasura-cloud/domains/)).

Image: [ Project actions ](https://hasura.io/docs/assets/images/project-manage-5b37a214a39b39b6287136606da021c4.png)

Note

For more information on which Postgres features we support, check out[ this page ](https://hasura.io/docs/latest/databases/feature-support/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#construct-db-url-aws-postgres/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#construct-db-url-aws-postgres/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#construct-db-url-aws-postgres/#create-hasura-project-aws-rds-postgres)
- [ Step 3: Create a Postgres DB on AWS ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#construct-db-url-aws-postgres/#create-aws-rds-postgres-db)
- [ Step 4: Allow connections to your DB from Hasura ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#construct-db-url-aws-postgres/#connect-hasura-aws-pg)
- [ Step 5: Construct the database connection URL ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#construct-db-url-aws-postgres/#construct-db-url-aws-postgres)
- [ Step 6: Finish connecting the database ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#construct-db-url-aws-postgres/#step-6-finish-connecting-the-database)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/aws-postgres/#construct-db-url-aws-postgres/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)