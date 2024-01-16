# Connecting Hasura to a Google AlloyDB Postgres Database

## Introduction​

This guide explains how to connect a new or existing[ Google AlloyDB Postgres ](https://cloud.google.com/alloydb)database to a Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or via one of our[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/)solutions. If you're exploring AlloyDB Postgres, check out their[ docs ](https://cloud.google.com/alloydb/docs)before continuing below.

Note

If you plan on using Hasura Cloud, which we recommend, follow steps 1 and 2 below. If you're self-hosting a Hasura
instance and already have a project running, skip to[ step 3 ](https://hasura.io/docs/latest/databases/postgres/alloy/#create-pg-db-alloy).

## Step 1: Sign up or log in to Hasura Cloud​

Navigate to[ Hasura Cloud ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-hasura-cloud&tech=default)and sign up or log in.

## Step 2: Create a Hasura Cloud project​

On the Hasura Cloud dashboard, create a new project:

Image: [ Create Hasura Cloud project ](https://hasura.io/docs/assets/images/create-hasura-cloud-project-3b3f2033182d76a59c7cd12dc90fe02b.png)

After the project is initialized successfully, click on `Launch Console` to open the Hasura Console in your browser.

On the Hasura Console, navigate to the `Data` tab and choose `Connect Existing Database` . Select AlloyDB from the `Data Source Driver` dropdown. Hasura will prompt you for a Postgres Database URL. We'll create this in the next step
and then come back here.

Image: [ Hasura Cloud database setup ](https://hasura.io/docs/assets/images/alloy-existing-db-setup-7731ff8819ecde459005f575826bea8a.png)

## Step 3: Create an AlloyDB database​

Head[ here ](https://cloud.google.com/alloydb)to learn more about and to try AlloyDB. If logged in, click `Go to console` :

Image: [ AlloyDB splash page ](https://hasura.io/docs/assets/images/alloy-splash-a1a28f398e8f09310336328611170a44.png)

You'll be redirected to GCP where you can get started with AlloyDB by clicking `ENABLE` :

Image: [ AlloyDB enable page ](https://hasura.io/docs/assets/images/alloy-enable-dadc592f0d23805eaf29b6888ade8026.png)

To get started, create a cluster by clicking `CREATE CLUSTER` :

Image: [ AlloyDB create cluster ](https://hasura.io/docs/assets/images/alloy-create-cluster-7d73060c38ff7f04b4880798ec0c9e9a.png)

If not already enabled, click, `ENABLE APIS` :

Image: [ AlloyDB enable APIs ](https://hasura.io/docs/assets/images/alloy-enable-apis-bae10025242e0adab48aaed511002170.png)

Choose your cluster type:

Image: [ AlloyDB choose cluster ](https://hasura.io/docs/assets/images/alloy-choose-cluster-42075f1616f609df7775565145110e1d.png)

Note

As GCP states, your selection isn't permanent. At the time of writing this document, only two options are available as
the others are currently in development: `Highly available` and `Highly available with read pools` .

Configure your cluster by providing the information required:

Image: [ AlloyDB configure cluster ](https://hasura.io/docs/assets/images/alloy-configure-cluster-8abb3f0e7d91b4b2760e834ff568ce16.png)

Under the Networking tab, you'll be prompted to set up a list of IP addresses for your services. Click `SET UP CONNECTION` :

Image: [ AlloyDB set up connection ](https://hasura.io/docs/assets/images/alloy-set-up-connection-dac2659566452cc9de2c741e47cd32d0.png)

Note

If you work within a company project, you might need extra permissions to ensure that you can choose a specific network.
Please contact your Google Cloud admin.

Either select an IP range or let GCP automatically allocate a range. After making your selection, click `CONTINUE` and
then `CREATE CONNECTION` :

Image: [ AlloyDB allocate IP ](https://hasura.io/docs/assets/images/alloy-allocate-ip-d22a850c96c42a6331cd1229d576dcd1.png)

With your cluster configured, you now need to configure your primary instance. Fill in the required information before
clicking `CREATE CLUSTER` :

Image: [ AlloyDB cluster created ](https://hasura.io/docs/assets/images/alloy-cluster-created-7bd85d9e0b13745f7a1df2efb15f04ff.png)

## Step 4: Create an AlloyDB auth proxy​

AlloyDB requires an auth proxy to make authorized, encrypted connections to an instance. You can follow GCP's
instructions, found[ here ](https://cloud.google.com/alloydb/docs/auth-proxy/connect), to create your auth proxy and
generate a connection string to use with Hasura. However, we'll also continue below with a Hasura-specific
implementation.

### Create a GCE instance​

Create a Compute Engine VM that can connect to AlloyDB instances using private services access.

Navigate to the **VM Instances page** and click `CREATE INSTANCE` :

Image: [ AlloyDB VM create instance ](https://hasura.io/docs/assets/images/alloy-vm-create-instance-1d8b3a6e62f486aa9d5ed2754a155214.png)

Provide a name for this instance and set the following properties:

- Access scopesSet to Allow full access to all Cloud APIs.
- Network interfacesSet to the VPC network configured for private services access to your AlloyDB instance.


Access scopes

Set to Allow full access to all Cloud APIs.

Network interfaces

Set to the VPC network configured for private services access to your AlloyDB instance.

Tip

For the best performance, select the GCE region as the same or closest to whichever region hosts your Hasura instance.

Click `CREATE` .

### Get the IP address of the AlloyDB instance​

 **From the cluster listing page for your AlloyDB instance** , get the private IP address of the instance. You'll use this
in the next step to run the auth proxy and connect it to the AlloyDB instance:

Image: [ AlloyDB get IP of db ](https://hasura.io/docs/assets/images/alloy-get-db-ip-0b4c553c29f090392f36be6a45154131.png)

 **From your GCE-created VM instance** ,[ download the auth proxy ](https://cloud.google.com/alloydb/docs/auth-proxy/connect)and, per GCP's instructions, make
the file executable.

You can start the auth proxy by running this command:

`./alloydb-auth-proxy  "projects/<project-id>/locations/<region>/clusters/<alloydb-cluster-id>/instances/<alloydb-instance-id>"  --address  "0.0.0.0"`

Note

This starts the auth proxy client and exposes it to the public. **Do note that this setup is an ephemeral one. You
should run the auth proxy in a permanent mode (for example, via
 docker detached mode ).** 

Additionally, you may have to specify a different version of the auth proxy, such as `alloydb-auth-proxy.linux.amd64` .

## Step 5: Add a firewall rule​

With our auth proxy now running, you'll need to create a firewall rule that allows a connection from your Hasura
instance. If using Hasura Cloud, from your project's dashboard, copy the Hasura Cloud IP address:

Image: [ AlloyDB get IP of Hasura Cloud project ](https://hasura.io/docs/assets/images/alloy-hasura-ip-8b274f8154e96c22fefa03a5248f7d9d.png)

Note

If you're using a self-hosted solution, you'll need to determine the IP address manually depending on your hosting
service.

Within the **VPC Firewall settings** , add a new rule by clicking, `CREATE FIREWALL RULE` :

Image: [ AlloyDB create firewall rule ](https://hasura.io/docs/assets/images/alloy-create-firewall-9aab1bc6bb282061d6ecf1b1c78c8aa5.png)

Permit connections to port `5432` and specify the IP address of your Hasura instance in the IPv4 range and click `CREATE` :

Image: [ AlloyDB firewall rule settings ](https://hasura.io/docs/assets/images/alloy-firewall-settings-e1dd23f427f9b1ac3c1d3d52cba3bd0d.png)

## Step 6: Construct the database connection URL and connect the database​

The structure of the database connection URL looks as follows:

`postgresql:// < database-user > : < postgres-password > @ < ip-address-of-gce-instance > :5432/ < database-name >`

- The `database-user` and `database-name` are both `postgres` by default.
- The `postgres-password` is the password you entered when creating the AlloyDB cluster in[ step 3 ](https://hasura.io/docs/latest/databases/postgres/alloy/#create-pg-db-alloy).
- The `ip-address-of-gce-instance` is from[ step 4 ](https://hasura.io/docs/latest/databases/postgres/alloy/#create-gce-instance)when you created a GCE VM instance.


Back on the Hasura Console, enter the database URL:

Image: [ AlloyDB connect db ](https://hasura.io/docs/assets/images/alloy-connect-db-b27535d472e9a6ac66b2d32edff6c74b.png)

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

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/alloy/#introduction)
- [ Step 1: Sign up or log in to Hasura Cloud ](https://hasura.io/docs/latest/databases/postgres/alloy/#step-1-sign-up-or-log-in-to-hasura-cloud)
- [ Step 2: Create a Hasura Cloud project ](https://hasura.io/docs/latest/databases/postgres/alloy/#create-hasura-project-alloy)
- [ Step 3: Create an AlloyDB database ](https://hasura.io/docs/latest/databases/postgres/alloy/#create-pg-db-alloy)
- [ Step 4: Create an AlloyDB auth proxy ](https://hasura.io/docs/latest/databases/postgres/alloy/#create-auth-proxy)
    - [ Create a GCE instance ](https://hasura.io/docs/latest/databases/postgres/alloy/#create-gce-instance)

- [ Get the IP address of the AlloyDB instance ](https://hasura.io/docs/latest/databases/postgres/alloy/#get-the-ip-address-of-the-alloydb-instance)
- [ Step 5: Add a firewall rule ](https://hasura.io/docs/latest/databases/postgres/alloy/#step-5-add-a-firewall-rule)
- [ Step 6: Construct the database connection URL and connect the database ](https://hasura.io/docs/latest/databases/postgres/alloy/#construct-db-url-alloy)
- [ Next steps ](https://hasura.io/docs/latest/databases/postgres/alloy/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)