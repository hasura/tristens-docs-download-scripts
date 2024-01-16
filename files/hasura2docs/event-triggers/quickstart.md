# Quickstart Event Triggers

Let's imagine that we want to send a welcome email to every new user who signs up. We can do this by creating an Event
Trigger that calls out to a webhook whenever a new user is inserted into the `users` table. The webhook payload will
contain the user's email address, and we can use this in the endpoint which we create to send them the welcome email.

##### DOCS E-COMMERCE SAMPLE APP

You can use this quickstart with any project, but it pairs well with our docs e-commerce sample app, which you can deploy to Hasura Cloud with one click below. If you've already deployed the sample app,[ access your existing project. ](https://cloud.hasura.io)

Image: [ Deploy to Hasura Cloud ](https://hasura.io/deploy-button.svg)

## Step 1: Navigate to Event Triggers​

To create an Event Trigger, navigate to the `Event` tab in the Console and click the `Create` button while on the `Event Triggers` tab in the left navigation.

Image: [ Click create for new Action ](https://hasura.io/docs/assets/images/event-triggers_main-screen_2-19-0-c87999a3e5ba6da74e6ee26908b54839.png)

## Step 2: Create a new Event Trigger​

On the Event Trigger creation page, input the name of the trigger, `send_welcome_email` , and select the database, schema
and table that the trigger will be listening to. In this case we'll be listening to the `users` table for an INSERT
event.

For the endpoint to call when the event is triggered, we'll use the `https://httpbin.org/post` endpoint. This is a demo
endpoint which will just return a `200` success status code and the data that we initially sent it.

For now, ignore `Auto-cleanup Event Logs` , `Advanced Settings` and `Configure REST Connectors` .

Click `Create Event Trigger` to create the Event Trigger.

Image: [ Click create for new Action ](https://hasura.io/docs/assets/images/event-triggers_create-event-trigger_2-19-0-c3eb0ebbf01b52c458aabb1b80c8bc23.png)

## Step 3: Test the Event Trigger​

Now that we've created the Event Trigger, let's test it out by inserting a new user into the `users` table. To do this,
navigate to the `Data` tab in the Console and click the `Insert Row` tab in the `users` table. Insert some dummy data
and click `Save` .

Image: [ Click create for new Action ](https://hasura.io/docs/assets/images/event-triggers_insert-user-dummy-data_2-19-0-3363c8723cf4c930da81f002efcf608c.png)

## Step 4: Check the Event Logs​

Navigate back to the `send_welcome_email` Event Trigger and click the `Processed Events` tab. You should see a new log
showing a successfully delivered event as it received a `200` status code as the response. You can inspect the `Request` and `Response` tabs to see exactly what data was sent to and received from the `httpbin.org` endpoint.

Image: [ Click create for new Action ](https://hasura.io/docs/assets/images/event-triggers_processed-events_2-19-0-26a7741031637ddb5ce09a5a446c4e48.png)

## Recap​

What just happened? Congrats! You just called a remote endpoint asynchronously when something happened in your database
and your user (theoretically) received a welcome email. 🎉

In a real world scenario, you would create a custom endpoint to send the welcome email, but in this example we showed
you just the mechanics of how to create an Event Trigger and test it out.

You can enable your Event Triggers for any table and event type, INSERT, UPDATE or DELETE, and you can also enable the[ manual invocation of your Event Trigger via a button in the Console ](https://hasura.io/docs/latest/event-triggers/invoke-trigger-manually/).

You can also thoroughly customize your Event Triggers to your needs using the[ Retry Configuration ](https://hasura.io/docs/latest/event-triggers/create-trigger/#retry-logic),[ Advanced Settings ](https://hasura.io/docs/latest/event-triggers/create-trigger/#advanced-settings)and[ Configure REST Connectors ](https://hasura.io/docs/latest/event-triggers/rest-connectors/)options.

### What did you think of this doc?

- [ Step 1: Navigate to Event Triggers ](https://hasura.io/docs/latest/event-triggers/quickstart/#step-2)
- [ Step 2: Create a new Event Trigger ](https://hasura.io/docs/latest/event-triggers/quickstart/#step-3)
- [ Step 3: Test the Event Trigger ](https://hasura.io/docs/latest/event-triggers/quickstart/#step-4)
- [ Step 4: Check the Event Logs ](https://hasura.io/docs/latest/event-triggers/quickstart/#step-5)
- [ Recap ](https://hasura.io/docs/latest/event-triggers/quickstart/#recap)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)