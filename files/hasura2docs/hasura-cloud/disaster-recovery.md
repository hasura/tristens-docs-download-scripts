# Disaster Recovery and Passive Standby Config for Hasura Cloud

## Introduction​

If you're designing your system to be fault tolerant enough to account for a full region-wide outage, we recommend
enabling a backup region on Hasura Cloud too.

## Step 1: Create a secondary Hasura Cloud Project​

In addition to your primary region on Hasura Cloud, create a new project in a convenient secondary region of your choice
and within a new VPC - we will call this the secondary Hasura Cloud project.

Note

This guide assumes that you use a custom domain for the primary Hasura Project so that in the event of a failover you
can switch the DNS for the custom domain to point to the secondary Hasura Project.

## Step 2: Peer the VPC and configure​

Peer this new VPC with your disaster recovery region on AWS or GCP where your secondary database is present.

Create all the required configurations and environment variables for the secondary Hasura Project. Connect this project
with your secondary database.

## Step 3: Keep Metadata in-sync​

Depending on when and how you keep the secondary database schema and data synced with the primary database, you should
also keep the Hasura Metadata on the secondary project up-to-date and in-sync with the primary project. You can use our[ Github Integration ](https://hasura.io/docs/latest/cloud-ci-cd/github-integration/)features to keep your secondary project in-sync by
deploying each commit to both projects. Care should be taken in the config of databases and ENV variables in this
regard.

## Step 4: Redirect traffic on failover​

When you actually need to failover to the secondary database and the secondary Hasura Project, point your custom domain
to the secondary project by changing the DNS entry on your side. This will send all traffic through to the secondary
project into your secondary database.

Note

Scheduled events (which are not part of Metadata), pending events deliveries, as well as the events history, will not be
migrated in the event of a failover.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/disaster-recovery/#introduction)
- [ Step 1: Create a secondary Hasura Cloud Project ](https://hasura.io/docs/latest/hasura-cloud/disaster-recovery/#step-1-create-a-secondary-hasura-cloud-project)
- [ Step 2: Peer the VPC and configure ](https://hasura.io/docs/latest/hasura-cloud/disaster-recovery/#step-2-peer-the-vpc-and-configure)
- [ Step 3: Keep Metadata in-sync ](https://hasura.io/docs/latest/hasura-cloud/disaster-recovery/#step-3-keep-metadata-in-sync)
- [ Step 4: Redirect traffic on failover ](https://hasura.io/docs/latest/hasura-cloud/disaster-recovery/#step-4-redirect-traffic-on-failover)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)