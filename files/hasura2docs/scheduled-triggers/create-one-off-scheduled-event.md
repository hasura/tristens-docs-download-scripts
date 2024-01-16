# Create a One-off Scheduled Event

## Introduction​

One-off scheduled events are used to reliably trigger an HTTP webhook to run custom business logic at a particular point
in time. For example, you can create a scheduled event to send a reminder email two weeks after a user signs up.

To add a one-off scheduled event, follow these steps:

## Step 1: Define the scheduled event​

The following fields for required to define a scheduled event:

- **Webhook** : The HTTP endpoint that should be triggered.
- **Time** : The time to trigger the event.
- **Payload** : The JSON payload which will be sent to the webhook.


- Console
- CLI
- API


Navigate to `Events > One-off Scheduled Events > Schedule an event` in your Hasura Console.

Image: [ Adding a one-off scheduled event ](https://hasura.io/docs/assets/images/one-off-200260624f20f323725ee906ee23aac1.png)

In the form opened by the above step, fill out the fields defined above:

Image: [ Defining the scheduled event ](https://hasura.io/docs/assets/images/define-one-off-event-c2cee7ea799ca61e287ac7392b5e4d7c.png)

One-off scheduled events cannot be set using the CLI as they are not tracked as a part of Hasura Metadata.

You can define a scheduled event via the[ create_scheduled_event ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-create-scheduled-event)metadata
API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "create_scheduled_event" ,
    "args" :   {
       "webhook" :   "https://send-email.com" ,
       "schedule_at" :   "2022-06-18T18:45:00Z" ,
       "payload" :   {   "email" :   "bob@ross.com"   }
    }
}
```

## Step 2: Define advanced options (Optional)​

If you like, you can also define advanced values:

- **Headers** : List of headers to be sent to the webhook.
- **Retry configuration** : In case the call to the webhook fails.
- **Comment** : Custom description of the Scheduled Trigger.


- Console
- CLI
- API


Expand the `Advanced` section.

Image: [ Defining advanced options for a scheduled event ](https://hasura.io/docs/assets/images/advanced-one-off-cce5a16cff08798509751e10e1cb02dd.png)

One-off scheduled events cannot be set using the CLI as they are not tracked as a part of Hasura Metadata.

You can define advanced options when defining a scheduled event via the[ create_scheduled_event ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-create-scheduled-event)metadata
API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "create_scheduled_event" ,
    "args" :   {
       "webhook" :   "https://send-email.com" ,
       "schedule_at" :   "2022-06-18T18:45:00Z" ,
       "payload" :   {
             "email" :   "bob@ross.com"
       } ,
       "headers" :   [
             {
                "name" :   "key" ,
                "value" :   "value"
             }
       ] ,
       "retry_conf" :   {
             "num_retries" :   3 ,
             "timeout_seconds" :   120 ,
             "tolerance_seconds" :   21675 ,
             "retry_interval_seconds" :   12
       } ,
       "comment" :   "sample scheduled event comment"
    }
}
```

## Schedule & logs​

Once you've created your Scheduled Trigger, you can see `Pending events` , `Processed events` , and `Invocation logs` in
their respective tabs.

Image: [ Schedule and logs for scheduled events ](https://hasura.io/docs/assets/images/pending-one-off-9551debb67c89eb38a44a30f95b93030.png)

Note

A scheduled event will be delivered within ten seconds of when it's scheduled. For example, if you schedule an event at `09:24:10` , it will be delivered between `09:24:10` and `09:24:20` .

This is because Hasura currently checks for events to be delivered at 10 second intervals. This interval will be made
configurable soon.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/scheduled-triggers/create-one-off-scheduled-event/#introduction)
- [ Step 1: Define the scheduled event ](https://hasura.io/docs/latest/scheduled-triggers/create-one-off-scheduled-event/#step-1-define-the-scheduled-event)
- [ Step 2: Define advanced options (Optional) ](https://hasura.io/docs/latest/scheduled-triggers/create-one-off-scheduled-event/#step-2-define-advanced-options-optional)
- [ Schedule & logs ](https://hasura.io/docs/latest/scheduled-triggers/create-one-off-scheduled-event/#schedule--logs)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)