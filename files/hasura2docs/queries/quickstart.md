# Quickstart Queries

This quickstart will help you write your first GraphQL query. Queries are the most common operation type in GraphQL.
They are used to fetch data from your database.

##### DOCS E-COMMERCE SAMPLE APP

This quickstart/recipe is dependent upon the docs e-commerce sample app. If you haven't already deployed the sample app, you can do so with one click below. If you've already deployed the sample app, simply use[ your existing project. ](https://cloud.hasura.io)

Image: [ Deploy to Hasura Cloud ](https://hasura.io/deploy-button.svg)

## Step 1: Open the API tab​

Open the `API` tab in the Hasura Console:

Image: [ API tab ](https://hasura.io/docs/assets/images/queries_api-tab_cloud2.20.0-767e6b1860ba86bf7fa3a53b944e7283.png)

## Step 2: Write and execute a simple query​

In the GraphiQL Explorer, paste the following `AllProducts` query. Your API should return the response on the right:

## Step 3: Write and execute a query with variables​

In the GraphiQL Explorer, paste the `ProductByID` query in the query field, and the following variables in the variables
field. This should return a single product from your database:

## Step 4: Write and execute a query with a relationship​

In the GraphiQL Explorer, paste the `ManufacturersAndProducts` query in the query field. This should return all
manufacturers and their products:

## Recap​

What just happened? Well, you just wrote your first set of GraphQL queries! They increased in complexity as you went
along, and you learned how to use variables and relationships in your queries. Let's break down each into a bit more
detail.

### Simple queries​

A simple query is a query that returns a single field without any filtering or special adjustments. In the `AllProducts` query, you queried the `products` field, which returns a list of products. As this is GraphQL, you have the option to
query only the fields you need. In this case, you only queried the `id` , `name` , and `manufacturer` fields. This is a
good practice to follow, as it reduces the amount of data you need to transfer over the network.

### Queries with variables​

A query with variables is a query that uses variables to filter the results. In the `ProductByID` query, you used the `$id` variable to filter the results to a single product. This allows you to reuse the same query with different
variables.

### Queries with relationships​

A query with[ relationships ](https://hasura.io/docs/latest/data-federation/data-federation-types/)is a query that uses relationships to filter
the results. In the `ManufacturersAndProducts` query, you used the `manufacturers` field to get a list of manufacturers.
You then used the `products` field to get a list of products for each manufacturer. Because of this, you can fetch
related data in a single query.

Naming Operation Types

It's helpful to name your operations so that you can easily identify them in the GraphiQL Explorer and in your
application. Hasura offers a robust set of[ observability tools ](https://hasura.io/docs/latest/observability/overview/)that you can use to
monitor your GraphQL API, namely by examining which queries are being executed, how often, and how long they take to
execute.

### What did you think of this doc?

- [ Step 1: Open the API tab ](https://hasura.io/docs/latest/queries/quickstart/#step-1-open-the-api-tab)
- [ Step 2: Write and execute a simple query ](https://hasura.io/docs/latest/queries/quickstart/#step-2-write-and-execute-a-simple-query)
- [ Step 3: Write and execute a query with variables ](https://hasura.io/docs/latest/queries/quickstart/#step-3-write-and-execute-a-query-with-variables)
- [ Step 4: Write and execute a query with a relationship ](https://hasura.io/docs/latest/queries/quickstart/#step-4-write-and-execute-a-query-with-a-relationship)
- [ Recap ](https://hasura.io/docs/latest/queries/quickstart/#recap)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)