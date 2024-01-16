# Create a RESTified Endpoint

## Introduction​

There are two methods to create a RESTified endpoint in Hasura Cloud and EE.

Data source availability

Available for **Postgres, MS SQL Server, Citus, AlloyDB and CockroachDB** databases.

##### DOCS E-COMMERCE SAMPLE APP

This quickstart/recipe is dependent upon the docs e-commerce sample app. If you haven't already deployed the sample app, you can do so with one click below. If you've already deployed the sample app, simply use[ your existing project. ](https://cloud.hasura.io)

Image: [ Deploy to Hasura Cloud ](https://hasura.io/deploy-button.svg)

## Option 1 - Create RESTified endpoints from table​

With a few clicks and no custom code, you can create default CRUD style REST endpoints from your tables.

To create a RESTified endpoint on a table, check out our[ Quickstart guide here ](https://hasura.io/docs/latest/restified/quickstart/).

## Option 2 - Create custom RESTified endpoints from GraphiQL​

### Step 1: Write a query​

In the GraphiQL interface in the `API` tab of the Hasura Console, create a query:

After entering the query, click the `REST` button in the Explorer to configure your endpoint:

Image: [ Create RESTified Endpoint ](https://hasura.io/docs/assets/images/restified-endpoints_click-rest-2_21-cloud_1-c3c2c341d2611020a348baec09ed5cfc.png)

### Step 2: Configure the endpoint​

Enter a name, eg:

`single_product_query`

Followed by a brief description if you wish:

`Retrieve a single product using its id`

Next, we'll provide a route that describes the endpoint's purpose and indicates that we wish to accept a query parameter
of `id` for the product:

`product/:id`

We'll mark `GET` as the allowed method and finish creating the endpoint by clicking `Create` .

Image: [ Create RESTified Endpoint ](https://hasura.io/docs/assets/images/restified-endpoints_click-create-2.21-cloud.1-2e0c870714148fb96bc29e77f7986770.png)

### Step 3: Test the endpoint​

To test this endpoint, run the following curl request in your terminal:

```
curl  --location --request GET  'https://<your-hasura-project>/api/rest/product/7992fdfa-65b5-11ed-8612-6a8b11ef7372'   \
--header  'Content-Type: application/json'   \
--header  'x-hasura-admin-secret: <your-admin-secret>'
```

You should see a response similar to this:

```
{
   "products_by_pk" :   {
     "id" :   "7992fdfa-65b5-11ed-8612-6a8b11ef7372" ,
     "name" :   "The Original Tee" ,
     "description" :   "When you want to keep it simple"
   }
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/restified/create/#introduction)
- [ Option 1 - Create RESTified endpoints from table ](https://hasura.io/docs/latest/restified/create/#create-from-table)
- [ Option 2 - Create custom RESTified endpoints from GraphiQL ](https://hasura.io/docs/latest/restified/create/#create-from-graphiql)
    - [ Step 1: Write a query ](https://hasura.io/docs/latest/restified/create/#step-1-write-a-query)

- [ Step 2: Configure the endpoint ](https://hasura.io/docs/latest/restified/create/#step-2-configure-the-endpoint)

- [ Step 3: Test the endpoint ](https://hasura.io/docs/latest/restified/create/#step-3-test-the-endpoint)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)