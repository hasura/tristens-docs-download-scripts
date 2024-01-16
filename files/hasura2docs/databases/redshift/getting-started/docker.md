# Get Started with Docker and Amazon Redshift

## Introduction​

Currently, testing continues on the Amazon Redshift connector for use in self-hosted environments. Our suggested
installation method is to use Docker Compose to deploy a working deployment of Hasura with the Amazon Redshift connector
enabled.

In order to do this, follow the instructions for[ Hasura Enterprise Edition ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-docker/), but change out the Docker Compose files
listed in that documentation with these values:

```
# in a new directory run
wget  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/enterprise/redshift/docker-compose.yaml
# or run
curl  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/enterprise/redshift/docker-compose.yaml -o docker-compose.yml
```

When you use these to launch the services, you'll see three containers running instead of two. The third container is
the Amazon Redshift GraphQL Connector agent. By navigating to the Hasura Console after execution, you'll find the Amazon
Redshift data source as a type that can now be added to your Hasura GraphQL Service instance.

## Keep up to date​

Note

Currently, Hasura supports read-only queries, subscriptions, relationships, and permissions on Amazon Redshift.

Please watch this space to get the latest docs on how you can try these features out via the Console or by manipulating
Metadata in JSON/YAML directly.

If you'd like to stay informed about the status of Amazon Redshift support, subscribe to our newsletter and join our
discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/redshift/getting-started/docker/#introduction)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/redshift/getting-started/docker/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)