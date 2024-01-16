# Get Started with Hasura Cloud & Snowflake

## Try it out​

### Step 1: Create an account on Hasura Cloud and create a new Hasura Project​

Navigate to[ cloud.hasura.io ](https://cloud.hasura.io/signup/?pg=docs&plcmt=body&cta=navigate-to-cloud-hasura-io&tech=default&skip_onboarding=true),
and create a new Hasura Cloud account.

Once you create a project on Hasura Cloud, hit the "Launch Console" button to open the Hasura Console for your project.

Image: [ Connect new or existing database ](https://hasura.io/docs/assets/images/create-project-8451135f7ff89b8f6e8fb3d29fd01ade.png)

### Step 2: Add your Snowflake database as a source to Hasura​

Head to the `Data > Manage databases` section on the Console to add your Snowflake database as a source to Hasura.

Make sure your Snowflake service is reachable by Hasura Cloud:

1. **Allow public connections or
 whitelist the Hasura Cloud IP  on your
 Snowflake firewall :** This is good for testing and
will allow you to quickly try out Hasura with your database!
2. **VPC peering:** VPC peering and private network access is available on Hasura Cloud paid tiers and is recommended
for production. Get in touch with us if you'd like to try this out against your existing databases.


#### Step 2.1: Begin by clicking "Connect Database"​

Image: [ Manage databases ](https://hasura.io/docs/assets/images/manage-databases-860d2d8b7b38f56493896034460892f4.png)

#### Step 2.2: Next, choose the snowflake driver​

`snowflake`

Image: [ temp ](https://hasura.io/docs/assets/images/choose-snowflake-af9ba058f9967f937ea77275e86e9a05.png)

#### Step 2.3: Enter your Snowflake JDBC Connection string​

Image: [ Setting the Snowflake connection details. ](https://hasura.io/docs/assets/images/database-config-ed2cd6543825a6423d783cff7a8c22dd.png)

Snowflake JDBC connection strings have the[ following formats ](https://docs.snowflake.com/en/user-guide/jdbc-configure.html#examples):

- `jdbc:snowflake://myorganization-myaccount.snowflakecomputing.com/?user=peter&warehouse=mywh&db=mydb&schema=public`
- `jdbc:snowflake://xy12345.snowflakecomputing.com/?user=peter&warehouse=mywh&db=mydb&schema=public`


You can get your `account id` for the second syntax by logging in to Snowflake and navigating to `Admin -> Accounts` .

You can find more info on Snowflake's[ JDBC Connection docs ](https://docs.snowflake.com/en/user-guide/jdbc-configure.html#jdbc-driver-connection-string)here.

Once you add the Snowflake service, you will find it listed as an available database on the sidebar.

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

### Step 3: Track existing tables​

To query your Snowflake service using Hasura, you'll need to have existing tables to select. Those tables will appear
under the database as shown.

Image: [ Tracking tables. ](https://hasura.io/docs/assets/images/track-tables-1-138adbcb36c1d3de36ee3ccda3de577d.png)

You can select all or select individual tables to track. Click "Track Selected" for Hasura to introspect them and create
the corresponding GraphQL schema.

Image: [ Tracking tables selected. ](https://hasura.io/docs/assets/images/track-tables-2-5fdda57c36b69b37bdaef100808d12a0.png)

### Step 4: Try out a GraphQL query​

Head to the `API` tab in the Console and try running a GraphQL query! Use the explorer sidebar on GraphQL to get help in
creating a GraphQL query.

Image: [ Try a GraphQL query ](https://hasura.io/docs/assets/images/query-5b76e7318d7a02e3e8d514d789741c5c.png)

## Keep up to date​

Note

Currently, Hasura supports read-only queries, relationships, and permissions on Snowflake.

If you'd like to stay informed about the status of Snowflake support, subscribe to our newsletter and join our discord!

- [ https://hasura.io/newsletter/ ](https://hasura.io/newsletter/)
- [ https://discord.com/invite/hasura ](https://discord.com/invite/hasura)


### What did you think of this doc?

- [ Try it out ](https://hasura.io/docs/latest/databases/snowflake/getting-started/cloud/#try-it-out)
    - [ Step 1: Create an account on Hasura Cloud and create a new Hasura Project ](https://hasura.io/docs/latest/databases/snowflake/getting-started/cloud/#step-1-create-an-account-on-hasura-cloud-and-create-a-new-hasura-project)

- [ Step 2: Add your Snowflake database as a source to Hasura ](https://hasura.io/docs/latest/databases/snowflake/getting-started/cloud/#step-2-add-your-snowflake-database-as-a-source-to-hasura)

- [ Step 3: Track existing tables ](https://hasura.io/docs/latest/databases/snowflake/getting-started/cloud/#step-3-track-existing-tables)

- [ Step 4: Try out a GraphQL query ](https://hasura.io/docs/latest/databases/snowflake/getting-started/cloud/#step-4-try-out-a-graphql-query)
- [ Keep up to date ](https://hasura.io/docs/latest/databases/snowflake/getting-started/cloud/#keep-up-to-date)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677756408/main-web/Group_11455_1_ziz1fz.png)

### Combining Snowflake and PostgreSQL to build low-latency apps on historical data insights

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)