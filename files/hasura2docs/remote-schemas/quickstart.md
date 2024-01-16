# Quickstart

## Overview​

This quickstart will help you connect your first Remote Schema.

##### DOCS E-COMMERCE SAMPLE APP

You can use this quickstart with any project, but it pairs well with our docs e-commerce sample app, which you can deploy to Hasura Cloud with one click below. If you've already deployed the sample app,[ access your existing project. ](https://cloud.hasura.io)

Image: [ Deploy to Hasura Cloud ](https://hasura.io/deploy-button.svg)

## Step 1: Click Add​

From the Console, navigate to the `Remote Schemas` page. At the top of the page, click `Add` :

Image: [ API Explorer Landing Page ](https://hasura.io/docs/assets/images/remote-schema_getting-started-guide_2.18.0_click-add-7eec4a17b6a2f71251c09f8ce354e757.png)

## Step 2: Enter the basics​

Name this remote schema `countries_api` and enter the following value in the `GraphQL Service URL` field:

`https://countries.trevorblades.com/graphql`

Image: [ API Explorer Landing Page ](https://hasura.io/docs/assets/images/remote-schema_getting-started-guide_2.18.0_enter-basics-946c6a2f718f05ff9e0d7d916302f6f1.png)

Scroll to the bottom of the page and click `Add Remote Schema` .

After clicking this button, you'll see the details of your newly connected API:

Image: [ API Explorer Landing Page ](https://hasura.io/docs/assets/images/remote-schema_getting-started-guide_2.18.0_newly-connected-result-f9bdac5dd4272a1b932ae4a39532cbf6.png)

That's it?!

Yep, that's it! You've just joined a remote GraphQL service with your Hasura GraphQL API 🔥

You could head to the API tab and query data from this new API, but keep reading if you're using the docs sample app to
see the power of a unified schema by creating a relationship with our existing data model.

## Step 3: Add a relationship​

Click the `Data` tab at the top of the page, select the `Products` table from the left-hand side navigation, and click `Relationships` . Scroll to the bottom of this page to find the `Remote Schema Relationships` and then click `Add a remote schema relationship` :

Image: [ API Explorer Landing Page ](https://hasura.io/docs/assets/images/remote-schema_getting-started-guide_2.18.0_click-add-remote-schema-relationship-a234aeead340a49b63177019d0fa3abb.png)

## Step 4: Configure the relationship​

Call the relationship `countryInfo` and select `countries_api` from the `Remote Schema` dropdown.

Then, under `Configuration` , check `countries` . Nested within `countries` , check the `filter` option and select `code` ,
then `eq` . We'll use the `country_of_origin` column as the foreign key for this relationship. When you've completed
these steps, scroll down and click `Save` .

Image: [ API Explorer Landing Page ](https://hasura.io/docs/assets/images/remote-schema_getting-started-guide_2.18.0_configure-relationship-c774dd8ab742d5c17274c9cd83ad11e8.png)

## Step 5: Test it out​

Head to the `API` tab and try this query; you should see a response similar to this:

Since our `products` table has a `country_of_origin` field, each product has a country code as its value. We can use
this to filter by this value and return the data we want - in this case, a flag emoji - for our front end.

## Recap​

What did we just do? Well, you just connected a remote GraphQL API to your Hasura GraphQL API and created a[ relationship between your existing data model and the new API ](https://hasura.io/docs/latest/data-federation/data-federation-types/#database-to-remote-schema-relationships).
This means you can query data from both APIs in a single query, and also use the data from the remote API to filter or
augment your existing data model 🎉

In our example, we used the data from the remote API to filter our existing data model by a country code, and then
return the data we want for that country. Common use cases include filtering for an id or a name.

All Hasura needs is a GraphQL endpoint to connect to, and it will automatically generate a GraphQL schema for you. This
means you can connect to any GraphQL API - or even multiple APIs - and access all your data in a single query from your
Hasura GraphQL API.

### What did you think of this doc?

- [ Overview ](https://hasura.io/docs/latest/remote-schemas/quickstart/#overview)
- [ Step 1: Click Add ](https://hasura.io/docs/latest/remote-schemas/quickstart/#step-1-click-add)
- [ Step 2: Enter the basics ](https://hasura.io/docs/latest/remote-schemas/quickstart/#step-2-enter-the-basics)
- [ Step 3: Add a relationship ](https://hasura.io/docs/latest/remote-schemas/quickstart/#step-3-add-a-relationship)
- [ Step 4: Configure the relationship ](https://hasura.io/docs/latest/remote-schemas/quickstart/#step-4-configure-the-relationship)
- [ Step 5: Test it out ](https://hasura.io/docs/latest/remote-schemas/quickstart/#step-5-test-it-out)
- [ Recap ](https://hasura.io/docs/latest/remote-schemas/quickstart/#recap)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)