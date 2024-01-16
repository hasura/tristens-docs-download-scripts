# Quickstart RESTified Endpoints

RESTified endpoints allow you to quickly and easily create REST endpoints without writing custom code. This quickstart
will walk you through the process of creating a REST endpoint from a table.

To see an alternative method of creating a REST endpoint from an query in the GraphiQL IDE, check out the[ Create RESTified endpoints ](https://hasura.io/docs/latest/restified/create/#create-from-graphiql)page.

Data source availability

Available for **Postgres, MS SQL Server, Citus, AlloyDB and CockroachDB** databases.

##### DOCS E-COMMERCE SAMPLE APP

This quickstart/recipe is dependent upon the docs e-commerce sample app. If you haven't already deployed the sample app, you can do so with one click below. If you've already deployed the sample app, simply use[ your existing project. ](https://cloud.hasura.io)

Image: [ Deploy to Hasura Cloud ](https://hasura.io/deploy-button.svg)

### Step 1: Navigate to the products table.​

Navigate to `Data > default > public > products` and click the "Create REST Endpoints" button.

Image: [ Create RESTified Endpoint ](https://hasura.io/docs/assets/images/restified-create-from-table-btn-09044ab07c87a8ce196fd861368c05cf.png)

### Step 2: Choose operations​

After clicking on the "Create REST endpoints" button, you will see a modal list of all REST operations ( `READ` , `READ
 ALL` , `CREATE` , `UPDATE` , `DELETE` ) available on the table. Select `READ` and `CREATE` for this demo. Click the
"Create" button.

Image: [ Create RESTified Endpoint ](https://hasura.io/docs/assets/images/restified-modal-from-table-4ab8f89ed36612c601308504b8e147cd.png)

### Step 3: View all REST endpoints​

You will be able to see the newly created REST endpoints listed in the `API > REST` tab.

Image: [ Create RESTified Endpoint ](https://hasura.io/docs/assets/images/restified-tracked-table-view-2cb6a975a35e84559a23c0930bd25a8d.png)

### Step 4: Test the REST endpoint​

Click on the `products_by_pk` title to get to the details page for that RESTified endpoint. In the "Request
Variables" section for `id` enter the value `7992fdfa-65b5-11ed-8612-6a8b11ef7372` , the UUID for one of the products
already in the `products` table of the docs sample app. Click "Run Request".

Image: [ Create RESTified Endpoint ](https://hasura.io/docs/assets/images/restified-test-16658ebcb7f150dd0795390e7f7375b7.png)

You will see the result returned next to the query.

You can test the other `insert_products_one` endpoint that we created in the same way by providing a new product
object as the request variable.

You can also use your favourite REST client to test the endpoint. For example, using `curl` :

```
curl  --location --request GET  'https://<your-hasura-project>.hasura.app/api/rest/products/7992fdfa-65b5-11ed-8612-6a8b11ef7372'   \
--header  'Content-Type: application/json'   \
--header  'x-hasura-admin-secret: <your-admin-secret>'
```

## Recap​

What just happened? Well, you just created two REST endpoints for reading a single product and inserting a product,
super fast, and without writing a single line of code 🎉

This saves you significant time and effort, as you easily enable REST endpoints on your tables or[ convert any query
or mutation into a REST endpoint ](https://hasura.io/docs/latest/restified/create/)with just a few clicks.

By using RESTified endpoints, you can take advantage of the benefits of both REST and GraphQL, making your Hasura
project even more versatile and powerful. For more details, check out the[ configuration page ](https://hasura.io/docs/latest/restified/restified-config/).

### What did you think of this doc?

- [ Step 1: Navigate to the products table. ](https://hasura.io/docs/latest/restified/quickstart/#step-1-navigate-to-the-products-table)
- [ Step 2: Choose operations ](https://hasura.io/docs/latest/restified/quickstart/#step-2-choose-operations)
- [ Step 3: View all REST endpoints ](https://hasura.io/docs/latest/restified/quickstart/#step-3-view-all-rest-endpoints)
- [ Step 4: Test the REST endpoint ](https://hasura.io/docs/latest/restified/quickstart/#step-4-test-the-rest-endpoint)
- [ Recap ](https://hasura.io/docs/latest/restified/quickstart/#recap)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)