# Get Started with Hasura Cloud and Amazon Redshift

## Introduction​

### Step 1: Create an account on Hasura Cloud and create a new Hasura Project​

Navigate to[ cloud.hasura.io ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-cloud-hasura-io&tech=default&skip_onboarding=true),
and create a new Hasura Cloud account.

Once you create a project on Hasura Cloud, hit the "Launch Console" button to open the Hasura Console for your project.

Image: [ Connect new or existing database ](https://hasura.io/docs/assets/images/create-project-8451135f7ff89b8f6e8fb3d29fd01ade.png)

### Step 2: Add your Amazon Redshift database as a source to Hasura​

Head to the `Data > Manage databases` section on the Console to add your Amazon Redshift database as a source to Hasura.

Make sure your Amazon Redshift service is reachable by Hasura Cloud:

1. **Allow public connections or
 whitelist the Hasura Cloud IP  on your Amazon
Redshift firewall:** This is good for testing and will allow you to quickly try Hasura out with your database!
2. **VPC peering:** VPC peering and private network access is available on Hasura Cloud paid tiers: Recommended for
production. Get in touch with us if you'd like to try this out against your existing databases!


First, we need to add the redshift agent:

Image: [ Adding the Amazon Redshift agent ](https://hasura.io/docs/assets/images/redshift-add-agent-0a2f280726e4b73dacf0b3a10ade3c95.png)

Now we need to connect to Redshift by clicking `Connect Database` :

Image: [ Manage databases ](https://hasura.io/docs/assets/images/manage-databases-860d2d8b7b38f56493896034460892f4.png)

Next, choose the `redshift (Beta)` driver:

Image: [ Adding the Amazon Redshift service ](https://hasura.io/docs/assets/images/redshift-add-service1-25b4dbcf479a403948b9caafe229fce2.png)

Finally, enter your Amazon Redshift database URL and[ database schema ](https://docs.aws.amazon.com/athena/latest/ug/creating-tables.html)and click `Connect Database` :

Image: [ Setting the Amazon Redshift connection details. ](https://hasura.io/docs/assets/images/redshift-add-service2-43509a9b6a6597e941d328931a9fd2d3.png)

Once you add the Amazon Redshift service, you'll see it listed as an available database on the sidebar.

### Step 3: Track existing tables​

To query against your Amazon Redshift service using Hasura, you'll need to have existing tables to select. Those tables
will appear under the database as shown.

Image: [ Tracking tables. ](https://hasura.io/docs/assets/images/redshift-tracking-tables1-3c6c7a9b2a94dc90f1fb5bad15cbedb8.png)

Track tables selectively or all so that Hasura can introspect the tables and create the corresponding GraphQL schema.
Once you've selected the tables you'd like to track, click `Track Selected` to finish setup:

Image: [ Tracking tables selected. ](https://hasura.io/docs/assets/images/redshift-tracking-tables2-b99daeee180f5eb6b1ef9cf6b70ecff5.png)

### Step 4: Try out a GraphQL query​

Head to the `API` tab in the Console and try running a GraphQL query! Use the explorer sidebar on GraphQL to get help in
creating a GraphQL query.

Image: [ Try a GraphQL query ](https://hasura.io/docs/assets/images/make-graphql-query-f30826eb11f28095be776ad3259b1543.png)

## Keep up to date​

Note

Currently, Hasura supports read-only queries, subscriptions, relationships, and permissions on Amazon Redshift.

If you'd like to stay informed about the status of Amazon Redshift support, subscribe to our newsletter and join our
discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/redshift/getting-started/cloud/#introduction)
    - [ Step 1: Create an account on Hasura Cloud and create a new Hasura Project ](https://hasura.io/docs/latest/databases/redshift/getting-started/cloud/#step-1-create-an-account-on-hasura-cloud-and-create-a-new-hasura-project)

- [ Step 2: Add your Amazon Redshift database as a source to Hasura ](https://hasura.io/docs/latest/databases/redshift/getting-started/cloud/#step-2-add-your-amazon-redshift-database-as-a-source-to-hasura)

- [ Step 3: Track existing tables ](https://hasura.io/docs/latest/databases/redshift/getting-started/cloud/#step-3-track-existing-tables)

- [ Step 4: Try out a GraphQL query ](https://hasura.io/docs/latest/databases/redshift/getting-started/cloud/#step-4-try-out-a-graphql-query)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/redshift/getting-started/cloud/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)