# Get Started with Docker (Hasura & Snowflake)

## Introduction​

Testing is currently underway on the Snowflake connector for use in self-hosted environments. Our suggested installation
method is to use Docker Compose to deploy a working deployment of Hasura with the Snowflake Connector enabled.

In order to do this, follow the instructions for[ Hasura Enterprise Edition ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-docker/), but change out the Docker Compose files
listed in that documentation to these values:

```
# in a new directory run
wget  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/enterprise/snowflake/docker-compose.yaml
# or run
curl  https://raw.githubusercontent.com/hasura/graphql-engine/master/install-manifests/enterprise/snowflake/docker-compose.yaml -o docker-compose.yml
```

When you use these to launch the services, you'll see three containers running instead of two. The third container is
the Snowflake GraphQL Connector agent. By navigating to the Hasura Console after execution, you'll find the Snowflake
data source as a type that can now be added to your Hasura GraphQL Service instance.

### Snowflake Connector Configuration​

You can directly add your JDBC connection string to the Snowflake Connector agent in the Hasura Console, or you can add
it as an environment variable to your project.

Setting the connection string as an environment variable

It's generally accepted that setting the connection string as an environment variable is a better practice as it's more
secure and prevents any secrets from being exposed in your instance's metadata.

An example would be to create a new[ environment variable ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/index/#using-environment-variables)called `SNOWFLAKE_JDBC_URL` and set it equal to your JDBC connection string.

Then, export the metadata - in JSON form - using the Console's `Settings` page or by making a call using the[ metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-export-metadata)and add the following key-value
pair to the `metadata.json` 's `configuration` object:

`"template" :   "{\"fully_qualify_all_names\": false, \"jdbc_url\": \"{{getEnvironmentVariable(\"SNOWFLAKE_JDBC_URL\")}}\"}"`

You can then apply the metadata to your instance by either using the Console's `Settings` page or by making a call using
the[ metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-apply-metadata).

Ensure your password escapes special characters

Due to the potential variations in drivers, it's crucial to escape special characters used in the password of the
connection string. These include `{ } % & #` . To escape a character, use the appropriate escape sequence based on your
database's driver's documentation.

## Keep up to date​

Note

Currently, Hasura supports read-only queries, relationships, and permissions on Snowflake.

Please watch this space to get the latest docs on how you can try these features out via the Console or by manipulating
Metadata in JSON/YAML directly.

If you'd like to stay informed about the status of Snowflake support, subscribe to our newsletter and join our discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/snowflake/getting-started/docker/#introduction)
    - [ Snowflake Connector Configuration ](https://hasura.io/docs/latest/databases/snowflake/getting-started/docker/#snowflake-connector-configuration)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/snowflake/getting-started/docker/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677756408/main-web/Group_11455_1_ziz1fz.png)

### Combining Snowflake and PostgreSQL to build low-latency apps on historical data insights

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)