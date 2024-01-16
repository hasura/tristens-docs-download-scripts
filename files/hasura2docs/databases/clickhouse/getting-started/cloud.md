# Get Started with Hasura Cloud & ClickHouse

## Try it out​

Connecting ClickHouse to Hasura

To connect ClickHouse to Hasura, you'll need to take advantage of[ Hasura Data Connectors ](https://hasura.io/docs/latest/databases/data-connectors/). You can deploy any custom data connector agent to Hasura
Cloud using our CLI plugin. For more information, refer to the[ docs ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/).

If you're curious what other connectors are available, check out our[ NDC Hub ](https://github.com/hasura/ndc-hub).

### Step 1: Create an account on Hasura Cloud and create a new Hasura Project​

Navigate to[ cloud.hasura.io ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-cloud-hasura-io&tech=default&skip_onboarding=true),
and create a new Hasura Cloud account.

Once you create a project on Hasura Cloud, hit the "Launch Console" button to open the Hasura Console for your project.

Image: [ Connect new or existing database ](https://hasura.io/docs/assets/images/create-project-8451135f7ff89b8f6e8fb3d29fd01ade.png)

### Step 2: Deploy a data connector agent​

 **We'll use the Hasura CLI to deploy a custom data connector agent to Hasura Cloud. If you haven't already done so,
install the  data connector plugin .** 

Below, we're using the `create` command and naming our connector `clickhouse-connector:v1` . We're also passing in the
GitHub repo URL for the connector agent using the `--github-repo-url` flag:

`hasura connector create clickhouse-connector:v1 --github-repo-url https://github.com/hasura/clickhouse_gdc_v2/tree/main`

We can check on the progress of the deployment using the `status` command:

`hasura connector status clickhouse-connector:v1`

Once the `DONE` status is returned, we can grab the URL for our data connector agent using the `list` command:

`hasura connector list`

This will return a list of all the custom data connector agents you own. **The second value returned is the URL which
we'll use in the next step; copy it to your clipboard.** 

### Step 3: Add the data connector agent to your Hasura Cloud project​

In your Cloud project, navigate to the `Data` tab and click `Manage` in the left-hand sidebar.

At the bottom of the screen, you'll see an expandable section titled `Data Connector Agents` .

Image: [ Add the agent for a ClickHouse database ](https://hasura.io/docs/assets/images/add-agent-11a552f3b592d1a359b8335f5c88515b.png)

Click this and scroll down to `Add Agent` .

Name this agent `clickhouse` and paste the URL you copied from the CLI into the `URL` field and click `Connect` .

Image: [ Add the agent for a ClickHouse database ](https://hasura.io/docs/assets/images/configure-agent-45a511603b4cfe6aeefeb23123a16906.png)

### Step 4: Add your ClickHouse database as a source to Hasura​

Head to the `Data > Manage databases` section on the Console to add your ClickHouse database as a source to Hasura.

Make sure your ClickHouse service is reachable by Hasura Cloud:

1. **Allow public connections or
 whitelist the Hasura Cloud IP  on your
 Clickhouse firewall :** This is good for testing and will allow you to quickly try out Hasura with your database!
2. **VPC peering:** VPC peering and private network access is available on Hasura Cloud paid tiers and is recommended
for production. Get in touch with us if you'd like to try this out against your existing databases.


#### Step 4.1: Begin by clicking Connect Database​

`Connect Database`

Image: [ Manage databases ](https://hasura.io/docs/assets/images/manage-databases-860d2d8b7b38f56493896034460892f4.png)

#### Step 4.2: Next, choose the Clickhouse driver​

`Clickhouse`

Image: [ temp ](https://hasura.io/docs/assets/images/choose-clickhouse-5f2a4ec2505ae022df8d7deae7c0af58.png)

#### Step 4.3: Enter your ClickHouse JDBC Connection string​

Image: [ Setting the ClickHouse connection details. ](https://hasura.io/docs/assets/images/database-config-dc6d3af3853deab81032833cfb834d2e.png)

You can get create your connection URL by logging in to ClickHouse and selecting `Connect -> View connection string` for
the database to which you want to connect.

Once you add the ClickHouse service, you will find it listed as an available database on the sidebar.

Setting the connection string as an environment variable

It's generally accepted that setting the password as an environment variable is a better practice as it's more secure
and prevents any secrets from being exposed in your instance's metadata.

An example would be to create a new[ environment variable ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/index/#using-environment-variables)called `CLICKHOUSE_PASSWORD` and set it equal to your ClickHouse password.

Then, export the metadata - in JSON form - using the Console's `Settings` page or by making a call using the[ metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-export-metadata)and add the following key-value
pair to the `metadata.json` 's `configuration` object:

`"template" :   "{\"url\": \"your_clickhouse_url_here\", \"user\": \"your_clickhouse_user\", \"password\": \"{{getEnvironmentVariable(\"CLICKHOUSE_PASSWORD\")}}\", \"tables\": null}"`

You can then apply the metadata to your instance by either using the Console's `Settings` page or by making a call using
the[ metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-apply-metadata).

Ensure your password escapes special characters

Due to the potential variations in drivers, it's crucial to escape special characters used in the password of the
connection string. These include `{ } % & #` . To escape a character, use the appropriate escape sequence based on your
database's driver's documentation.

### Step 5: Track existing tables​

To query your ClickHouse service using Hasura, you'll need to have existing tables to select. Those tables will appear
under the database as shown below:

Image: [ Tracking tables. ](https://hasura.io/docs/assets/images/track-tables-1-9d3e9e340360c46908a4000217a4a1e9.png)

You can select all or select individual tables to track. Click `Track Selected` for Hasura to introspect them and create
the corresponding GraphQL schema.

Image: [ Tracking tables selected. ](https://hasura.io/docs/assets/images/track-tables-2-661de38e17204183ead9fafad7fa8a4c.png)

### Step 6: Try out a GraphQL query​

Head to the `API` tab in the Console and try running a GraphQL query! Use the explorer sidebar on GraphiQL to get help
in creating a GraphQL query.

Image: [ Try a GraphQL query ](https://hasura.io/docs/assets/images/query-89b442ba4a4574207ee146a14d1c5dda.png)

## Keep up to date​

Note

Currently, Hasura supports read-only queries, relationships, and permissions on ClickHouse. Column comparison operators
are not supported with permissions on ClickHouse.

If you'd like to stay informed about the status of ClickHouse support, subscribe to our newsletter and join our discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Try it out ](https://hasura.io/docs/latest/databases/clickhouse/getting-started/cloud/#try-it-out)
    - [ Step 1: Create an account on Hasura Cloud and create a new Hasura Project ](https://hasura.io/docs/latest/databases/clickhouse/getting-started/cloud/#step-1-create-an-account-on-hasura-cloud-and-create-a-new-hasura-project)

- [ Step 2: Deploy a data connector agent ](https://hasura.io/docs/latest/databases/clickhouse/getting-started/cloud/#step-2-deploy-a-data-connector-agent)

- [ Step 3: Add the data connector agent to your Hasura Cloud project ](https://hasura.io/docs/latest/databases/clickhouse/getting-started/cloud/#step-3-add-the-data-connector-agent-to-your-hasura-cloud-project)

- [ Step 4: Add your ClickHouse database as a source to Hasura ](https://hasura.io/docs/latest/databases/clickhouse/getting-started/cloud/#step-4-add-your-clickhouse-database-as-a-source-to-hasura)

- [ Step 5: Track existing tables ](https://hasura.io/docs/latest/databases/clickhouse/getting-started/cloud/#step-5-track-existing-tables)

- [ Step 6: Try out a GraphQL query ](https://hasura.io/docs/latest/databases/clickhouse/getting-started/cloud/#step-6-try-out-a-graphql-query)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/clickhouse/getting-started/cloud/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)