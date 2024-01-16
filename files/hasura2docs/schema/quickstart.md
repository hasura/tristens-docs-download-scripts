# Quickstart Schema

This quickstart will help you work with the GraphQL Schema. We'll create a table called `coupons` and add some sample
data to it. Then, we'll query for the data using the Hasura Console GUI and the API Explorer.

##### DOCS E-COMMERCE SAMPLE APP

You can use this quickstart with any project, but it pairs well with our docs e-commerce sample app, which you can deploy to Hasura Cloud with one click below. If you've already deployed the sample app,[ access your existing project. ](https://cloud.hasura.io)

Image: [ Deploy to Hasura Cloud ](https://hasura.io/deploy-button.svg)

## Step 1: Navigate to the Data tab​

Once here, click the `Create Table` button at the top of the page:

Image: [ Schema create table ](https://hasura.io/docs/assets/images/schema-create-table_quickstart_cloud2.20.0-38c2f85dcef482b10d06358b97ab60d8.png)

## Step 2: Enter the details​

On this page, we'll begin by naming the table: in the `Table Name` field, enter `coupons` . From there, we'll add all the
necessary columns:

In the `Columns` section, we'll start with the `Column Name` field, enter `id` , with a data type of `integer (auto-increment)` and check the box for `unique` . Leave `nullable` unchecked as this is a required column and
can't be `null` .

Then, we'll repeat the steps for the following columns:

- `amount` (data type: `integer` )
- `code` (data type: `text` )
- `description` (data type: `text` )
- `start_date` (data type: `timestamp` ), defaulting to `now()`
- `end_date` (data type: `timestamp` )


Image: [ Schema create table ](https://hasura.io/docs/assets/images/schema_quickstart_cloud2.20.0-0308d35385b3708cda6b9565b9b192f8.png)

## Step 3: Add a primary key​

In the `Primary Key` section, open the dropdown and select `id` from the list of columns. Then click, `Add table` .

## Step 4: Test it out​

We should have received confirmation that our table was created successfully. Now, let's test it out by adding a new
coupon on the `Insert Row` tab:

Image: [ Schema create table ](https://hasura.io/docs/assets/images/schema-insert-row_quickstart_cloud2.20.0-d8eb3f138b342922d97fb5683e1987c2.png)

We can leave the `id` field blank, since it's auto-incrementing. Then, we'll add the following values:

- `amount` : `50`
- `code` : `HALFOFF`
- `description` : `50% off your next purchase`
- `start_date` : check the `Default` radio button
- `end_date` : `2024-01-04 06:00:00`


Upon clicking `Save` , we should receive confirmation of our new coupon. We can check its details by clicking the `Browse Rows` tab or by running a query in our API Explorer.

## Recap​

What just happened? Well, you just modified your GraphQL API's schema! You can now query for coupons using the `coupons` table. You can also add new coupons using the `insert_coupons` mutation.

You can continue to customize this table and create relationships between it and other tables, such as `products` or `orders` to create a coupon system for your e-commerce store.

### What did you think of this doc?

- [ Step 1: Navigate to the Data tab ](https://hasura.io/docs/latest/schema/quickstart/#step-1-navigate-to-the-data-tab)
- [ Step 2: Enter the details ](https://hasura.io/docs/latest/schema/quickstart/#step-2-enter-the-details)
- [ Step 3: Add a primary key ](https://hasura.io/docs/latest/schema/quickstart/#step-3-add-a-primary-key)
- [ Step 4: Test it out ](https://hasura.io/docs/latest/schema/quickstart/#step-4-test-it-out)
- [ Recap ](https://hasura.io/docs/latest/schema/quickstart/#recap)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)