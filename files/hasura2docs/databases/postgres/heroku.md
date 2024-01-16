# Connecting Hasura to a Heroku Postgres Database

## Introduction​

This guide explains how to connect a new or existing Postgres database hosted on Heroku to a Hasura instance, either on[ Hasura Cloud ](https://cloud.hasura.io?skip_onboarding=true)or[ self-hosted ](https://hasura.io/docs/latest/deployment/deployment-guides/index/).

danger

In August of 2022, Heroku announced the[ deprecation of their free resources ](https://devcenter.heroku.com/changelog-items/2461). Starting November 28th, 2022,
if you have a Hasura Project connected to a free tier Heroku database, you'll need to either upgrade your Heroku account
or migrate your database to a new database provider.

## Connecting to Heroku​

If you are interested in connecting to a Heroku database, our[ Heroku database integration guide ](https://hasura.io/docs/latest/hasura-cloud/heroku-url-sync/)walks you through each step.

## Alternatives to Heroku​

Hasura works well with popular database providers. Most of these providers offer generous free tiers. We have guides you
can use to provision and connect a new database in a matter of minutes. You can check them out[ here ](https://hasura.io/docs/latest/databases/overview/).

If you're interested in migrating away from Heroku, our different cloud database providers have guides and documentation
to help you:

### Heroku-specific migration guides​

- [ Crunchy Postgres ](https://www.crunchydata.com/migrate-from-heroku)
- [ Neon Postgres ](https://neon.tech/docs/how-to-guides/hasura-heroku-migration/)
- [ Railway Postgres ](https://railway.app/heroku)
- [ Render Postgres ](https://render.com/docs/migrate-from-heroku)
- [ Supabase Postgres ](https://supabase.com/docs/guides/migrations/heroku)


### General migration guides​

- [ Aiven Postgres ](https://docs.aiven.io/docs/products/postgresql/howto/migrate-pg-dump-restore.html)
- [ AWS RDS Aurora ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Migrating.html)
- [ AWS RDS Postgres ](https://aws.amazon.com/getting-started/hands-on/move-to-managed/migrate-postgresql-to-amazon-rds/)
- [ Azure Postgres ](https://learn.microsoft.com/en-us/azure/dms/tutorial-postgresql-azure-postgresql-online-portal)
- [ DigitalOcean Postgres ](https://docs.digitalocean.com/products/databases/postgresql/how-to/migrate/)
- [ EnterpriseDB BigAnimal Postgres ](https://www.enterprisedb.com/docs/biganimal/latest/migration/cold_migration/)
- [ Google Cloud SQL Postgres ](https://cloud.google.com/database-migration/docs/postgres)
- [ TimescaleDB ](https://docs.timescale.com/timescaledb/latest/how-to-guides/migrate-data/)
- [ YugabyteDB ](https://docs.yugabyte.com/preview/migrate/migrate-steps/)


### FAQs regarding the deprecation of Heroku free resources​

Note

For more information on which Postgres features we support, check out[ this page ](https://hasura.io/docs/latest/databases/feature-support/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/postgres/heroku/#introduction)
- [ Connecting to Heroku ](https://hasura.io/docs/latest/databases/postgres/heroku/#connecting-to-heroku)
- [ Alternatives to Heroku ](https://hasura.io/docs/latest/databases/postgres/heroku/#alternatives-to-heroku)
    - [ Heroku-specific migration guides ](https://hasura.io/docs/latest/databases/postgres/heroku/#heroku-specific-migration-guides)

- [ General migration guides ](https://hasura.io/docs/latest/databases/postgres/heroku/#general-migration-guides)

- [ FAQs regarding the deprecation of Heroku free resources ](https://hasura.io/docs/latest/databases/postgres/heroku/#heroku-faqs)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)