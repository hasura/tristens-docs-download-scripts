# Quickstart Subscriptions

This quickstart will help you create your first subscription. We're going to subscribe to live updates for a
notification thread.

##### DOCS E-COMMERCE SAMPLE APP

This quickstart/recipe is dependent upon the docs e-commerce sample app. If you haven't already deployed the sample app, you can do so with one click below. If you've already deployed the sample app, simply use[ your existing project. ](https://cloud.hasura.io)

Image: [ Deploy to Hasura Cloud ](https://hasura.io/deploy-button.svg)

## Step 1: Create a Subscription​

Head to the `API` tab of the Hasura Console and paste in this value:

```
subscription   UserNotificationSubscription ( $user_id :   uuid   =   "9bd9d300-65b7-11ed-b908-571fef22d2ba" )   {
   notifications ( where :   {   user_id :   {   _eq :   $user_id   }   } )   {
     id
     created_at
     message
   }
}
```

Once hitting run, you should see the following output:

Image: [ Hasura Scheduled Trigger architecture ](https://hasura.io/docs/assets/images/subscriptions-empty_quickstart-cloud2.20.0-f3e32c5353262554be6544d8a26aa7e0.png)

That's it?

Yep! Remember, you get subscriptions out of the box with Hasura 🔥 You'll see a few notifications in your results
because they're already in the database. To test it — and see new notifications mimicking a client application — let's
ping the server with curl in the next step.

## Step 2: Insert a notification​

To avoid the need for a client application, we'll use curl to insert a notification into the database. You can enter the
curl command below into a terminal window, and replace the `<YOUR_ADMIN_SECRET>` and `<YOUR_HASURA_PROJECT_ENDPOINT>` values with your own:

`curl  -X POST -H  "Content-Type: application/json"  -H  "x-hasura-admin-secret: <YOUR_ADMIN_SECRET>"  -d  '{"query":"mutation InsertNewNotification {\n  insert_notifications_one(object: {user_id: \"9bd9d300-65b7-11ed-b908-571fef22d2ba\", message: \"This is a live-updating subscription!\"}) {\n    id\n  }\n}"}'   < YOUR_PROJECT_GRAPHQL_ENDPOINT >`

After entering the above command hitting `enter` , you should see the following output on your Console's API tab:

Image: [ Hasura Scheduled Trigger architecture ](https://hasura.io/docs/assets/images/subscriptions_quickstart-cloud2.20.0-30a2c9b49ab964e1afc8f33486876f85.gif)

## Recap​

What just happened? Well, you just wrote your first subscription! You can now subscribe to live updates for a
notification thread. Think of the possibilities in a real-world application: you can subscribe to live updates for a
chat thread, a shopping cart, or a live leaderboard.

At the start, you created a subscription using the Hasura Console's API tab. This subscription returns the `id` field
for all notifications with a `user_id` equal to the provided value. This allows us to receive new data, live from the
server, rather than just a single response. So, as new notifications are inserted into the database - like we did with
the curl command - the subscription will return them.

### What did you think of this doc?

- [ Step 1: Create a Subscription ](https://hasura.io/docs/latest/subscriptions/quickstart/#step-1-create-a-subscription)
- [ Step 2: Insert a notification ](https://hasura.io/docs/latest/subscriptions/quickstart/#step-2-insert-a-notification)
- [ Recap ](https://hasura.io/docs/latest/subscriptions/quickstart/#recap)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)