# Create a Scheduled Trigger

## Introduction​

Scheduled Triggers are used to reliably trigger HTTP endpoints to run custom business logic periodically based on a[ cron schedule ](https://en.wikipedia.org/wiki/Cron). For example, you can create a Scheduled Trigger to generate an
end-of-day sales report every weekday at 10pm.

To add a Scheduled Trigger, follow these steps:

## Step 1: Define the Scheduled Trigger​

The following fields are required to define a Scheduled Trigger:

- **Name** : A name for the Scheduled Trigger.
- **Webhook** : The HTTP endpoint that should be triggered.
- **Cron schedule** : A cron expression defining the schedule for the cron. Cron events are created based on the UTC
timezone. You can use tools like[ crontab guru ](https://crontab.guru/#*_*_*_*_*)to help build a cron expression.
- **Payload** : The JSON payload which will be sent to the webhook.


You can also define a **comment** that helps you identify the Scheduled Trigger.

For example, we can create a Scheduled Trigger called `eod_reports` , to trigger the webhook `https://mywebhook.com/eod` with the cron schedule `0 22 * * 1-5` , which means "At 22:00 on every day-of-week from Monday through Friday" (you can
check this[ here ](https://crontab.guru/#0_22_*_*_1-5)).

- Console
- CLI
- API


Navigate to `Events > Cron Triggers > Create` in your Hasura Console.

Image: [ Adding a Scheduled Trigger ](https://hasura.io/docs/assets/images/create-cron-470787a7abd66c013d27a83a5891c31d.png)

In the form opened, fill out the fields defined above:

You can use the link next to the `Cron Schedule` field to help build a cron expression using[ crontab guru ](https://crontab.guru/#*_*_*_*_*), or use the `Frequently used crons` dropdown as a shortcut.

Image: [ Defining a Scheduled Trigger ](https://hasura.io/docs/assets/images/define-cron-trigger-77ee7dc14cad5697b0a0239672d402a2.png)

You can define a Scheduled Trigger by adding it to the `cron_triggers.yaml` file inside the `metadata` directory:

```
-   name :  eod_reports
   webhook :  https : //mywebhook.com/eod
   schedule :  0 22 * * 1 - 5
   include_in_metadata :   true
   payload :   { }
```

Apply the Metadata by running:

`hasura metadata apply`

You can define a Scheduled Trigger via the[ create_cron_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-create-cron-trigger)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "create_cron_trigger" ,
    "args" :   {
       "name" :   "eod_reports" ,
       "webhook" :   "https://mywebhook.com/eod" ,
       "schedule" :   "0 22 * * 1-5" ,
       "payload" :   { } ,
       "include_in_metadata" :   true
    }
}
```

## Step 2: Define advanced options (Optional)​

If you like, you can also define the following values:

- **Headers** : List of headers to be sent to the webhook.
- **Retry configuration** : In case the call to the webhook fails.
- **Include in metadata** : When set to true, the Scheduled Trigger will be included in the metadata and can be exported
along with it.


- Console
- CLI
- API


Expand the `Advanced` section.

Image: [ Defining advanced options for a Scheduled Trigger ](https://hasura.io/docs/assets/images/advanced-cron-992b9d3553fba15235ddf9014a035f29.png)

You can define advanced options for a crone trigger when adding it to the `cron_triggers.yaml` file inside the `metadata` directory:

```
-   name :  eod_reports
   webhook :  https : //mywebhook.com/eod
   schedule :  0 22 * * 1 - 5
   include_in_metadata :   true
   payload :   { }
   retry_conf :
     num_retries :   3
     timeout_seconds :   120
     tolerance_seconds :   21675
     retry_interval_seconds :   12
   comment :  This is a comment
```

Apply the Metadata by running:

`hasura metadata apply`

You can define advanced options for a Scheduled Trigger when defining it via the[ create_cron_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-create-cron-trigger)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "create_cron_trigger" ,
    "args" :   {
       "name" :   "eod_reports" ,
       "webhook" :   "https://mywebhook.com/eod" ,
       "schedule" :   "0 22 * * 1-5" ,
       "include_in_metadata" :   true ,
       "payload" :   { } ,
       "retry_conf" :   {
             "num_retries" :   3 ,
             "timeout_seconds" :   120 ,
             "tolerance_seconds" :   21675 ,
             "retry_interval_seconds" :   12
       } ,
       "comment" :   "sample_cron comment"
    }
}
```

## Schedule & logs​

Once you've created your Scheduled Trigger, you can see `Pending events` , `Processed events` , and `Invocation logs` in
their respective tabs.

Image: [ Schedule and logs for Scheduled Triggers ](https://hasura.io/docs/assets/images/pending-cron-0cb2990eefbe80cb8ed7982b3f2c1929.png)

## Rest Connectors​

REST Connectors i.e. request and response transformations, for Scheduled Triggers are used to invoke existing or
third-party webhooks without needing any middleware or modifications to the upstream code.

REST Connectors modify the Scheduled Trigger's HTTP request to adapt to your webhook's expected format by adding
suitable transforms.

Rest Connectors for Scheduled Triggers can be configured in the same way as rest connectors for event triggers. You can
read more about it in the[ REST Connectors ](https://hasura.io/docs/latest/event-triggers/rest-connectors/)section.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/scheduled-triggers/create-cron-trigger/#rest-connectors/#introduction)
- [ Step 1: Define the Scheduled Trigger ](https://hasura.io/docs/latest/scheduled-triggers/create-cron-trigger/#rest-connectors/#step-1-define-the-scheduled-trigger)
- [ Step 2: Define advanced options (Optional) ](https://hasura.io/docs/latest/scheduled-triggers/create-cron-trigger/#rest-connectors/#step-2-define-advanced-options-optional)
- [ Schedule & logs ](https://hasura.io/docs/latest/scheduled-triggers/create-cron-trigger/#rest-connectors/#schedule--logs)
- [ Rest Connectors ](https://hasura.io/docs/latest/scheduled-triggers/create-cron-trigger/#rest-connectors/#rest-connectors)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)