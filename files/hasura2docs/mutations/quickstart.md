# Quickstart Mutations

This quickstart will help you write your first GraphQL mutation. Mutations are used to modify data in your database.

##### DOCS E-COMMERCE SAMPLE APP

This quickstart/recipe is dependent upon the docs e-commerce sample app. If you haven't already deployed the sample app, you can do so with one click below. If you've already deployed the sample app, simply use[ your existing project. ](https://cloud.hasura.io)

Image: [ Deploy to Hasura Cloud ](https://hasura.io/deploy-button.svg)

## Step 1: Open the API tab​

Open the `API` tab in the Hasura Console:

Image: [ API tab ](https://hasura.io/docs/assets/images/queries_api-tab_cloud2.20.0-767e6b1860ba86bf7fa3a53b944e7283.png)

## Step 2: Write and execute an insert mutation​

In the GraphiQL Explorer, paste the following `InsertReview` mutation and variables. Your API should return a similar
response to the data on the right:

## Step 3: Write and execute an update mutation​

In the GraphiQL Explorer, paste the `UpdateReview` mutation and the following variables. This should return a single,
updated review with new `text` :

## Step 4: Write and execute a delete mutation​

In the GraphiQL Explorer, paste the `DeleteReview` mutation and the following variables. This should return confirmation
that the review was deleted by providing the `id` :

## Recap​

What just happened? Well, you just wrote your first set of GraphQL mutations! They demonstrated the different ways in
which you can modify data in your database using GraphQL. Let's break down each into a bit more detail.

### Insert mutation​

Insertions are used to add new data to your database. In this case, we're adding a new review to the `reviews` table.

The `InsertReview` mutation inserts a new review into the `reviews` table and returns the `id` of the newly inserted
review. It takes the following arguments:

- `rating` : The rating of the review, an integer between 1 and 5.
- `text` : The text of the review, a string.
- `user_id` : The ID of the user who wrote the review, a UUID.
- `product_id` : The ID of the product that the review is for, a UUID.


We made the different arguments required by using the `!` operator. This means that if you try to run the mutation
without providing a value for one of these arguments, the GraphQL Engine will throw an error.

### Update mutation​

Updates are used to modify existing data in your database.

In this case, we're updating the `text` of an existing review. Since we're only updating the `text` of the review, we
don't need to provide the other arguments. However, we do need to provide the `id` of the review we want to update, as
this type uses the primary key of the table to identify which row to update.

### Delete mutation​

Deletions are used to remove existing data from your database.

With this example, we're deleting a review from the `reviews` table. We need to provide the `id` of the review we want
to delete, as this type uses the primary key of the table to identify which row to delete.

### What did you think of this doc?

- [ Step 1: Open the API tab ](https://hasura.io/docs/latest/mutations/quickstart/#step-1-open-the-api-tab)
- [ Step 2: Write and execute an insert mutation ](https://hasura.io/docs/latest/mutations/quickstart/#step-2-write-and-execute-an-insert-mutation)
- [ Step 3: Write and execute an update mutation ](https://hasura.io/docs/latest/mutations/quickstart/#step-3-write-and-execute-an-update-mutation)
- [ Step 4: Write and execute a delete mutation ](https://hasura.io/docs/latest/mutations/quickstart/#step-4-write-and-execute-a-delete-mutation)
- [ Recap ](https://hasura.io/docs/latest/mutations/quickstart/#recap)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)