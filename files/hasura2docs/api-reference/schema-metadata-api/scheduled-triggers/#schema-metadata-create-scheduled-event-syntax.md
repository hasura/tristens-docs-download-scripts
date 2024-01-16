# Schema/Metadata API Reference: Scheduled Triggers (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

## Introduction​

Scheduled Triggers are used to invoke webhooks based on a timestamp or
cron.

## create_cron_trigger​

 `create_cron_trigger` is used to create a new cron trigger.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "create_cron_trigger" ,
     "args"   :   {
         "name" :   "sample_cron" ,
         "webhook" :   "https://httpbin.org/post" ,
         "schedule" :    "* * * * *" ,
         "payload" :   {
             "key1" :   "value1" ,
             "key2" :   "value2"
         } ,
         "include_in_metadata" : false ,
         "comment" : "sample_cron comment"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the cron trigger |
| webhook | true | [ WebhookURL ](https://hasura.io/docs/latest/api-reference/syntax-defs/#webhookurl) | URL of the webhook |
| schedule | true | Cron Expression | Cron expression at which the trigger should be invoked. |
| payload | false | JSON | Any JSON payload which will be sent when the webhook is invoked. |
| headers | false | [[ HeaderFromValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#headerfromvalue)|[ HeaderFromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#headerfromenv)] | List of headers to be sent with the webhook |
| retry_conf | false | [ RetryConfST ](https://hasura.io/docs/latest/api-reference/syntax-defs/#retryconfst) | Retry configuration if scheduled invocation delivery fails |
| include_in_metadata | true | Boolean | Flag to indicate whether a trigger should be included in the metadata. When a cron trigger is included in the metadata, the user will be able to export it when the Metadata of the graphql-engine is exported. |
| comment | false | Text | Custom comment. |
| replace | false | Bool | When replace is set to `true` , the cron trigger will be updated(if exists) and when it's `false` or the field is omitted, then a new cron trigger will be created. |


Supported from

Scheduled Triggers are supported from versions `v1.3.0` and above.

## delete_cron_trigger​

 `delete_cron_trigger` is used to delete an existing cron trigger. The
scheduled events associated with the cron trigger will also be deleted.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "delete_cron_trigger" ,
     "args"   :   {
         "name" :   "sample_cron"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the cron trigger |


Supported from

Scheduled Triggers are supported from versions `v1.3.0` and above.

## create_scheduled_event​

 `create_scheduled_event` is used to create a scheduled event.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "create_scheduled_event" ,
     "args"   :   {
         "webhook" :   "https://httpbin.org/post" ,
         "schedule_at" :   "2019-09-09T22:00:00Z" ,
         "payload" :   {
             "key1" :   "value1" ,
             "key2" :   "value2"
         } ,
         "headers"   :   [ {
             "name" : "header-key" ,
             "value" : "header-value"
         } ] ,
         "comment" : "sample scheduled event comment"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| webhook | true | [ WebhookURL ](https://hasura.io/docs/latest/api-reference/syntax-defs/#webhookurl) | URL of the webhook |
| schedule_at | true | Timestamp (ISO8601 format) | The time at which the invocation should be invoked. |
| payload | false | JSON | Any JSON payload which will be sent when the webhook is invoked. |
| headers | false | [[ HeaderFromValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#headerfromvalue)|[ HeaderFromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#headerfromenv)] | List of headers to be sent with the webhook |
| retry_conf | false | [ RetryConfST ](https://hasura.io/docs/latest/api-reference/syntax-defs/#retryconfst) | Retry configuration if scheduled event delivery fails |
| comment | false | Text | Custom comment. |


Supported from

Scheduled Triggers are supported from versions `v1.3.0` and above.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-create-scheduled-event-syntax/#introduction)
- [ create_cron_trigger ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-create-scheduled-event-syntax/#schema-metadata-create-cron-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-create-scheduled-event-syntax/#schema-metadata-create-cron-trigger-syntax)
- [ delete_cron_trigger ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-create-scheduled-event-syntax/#schema-metadata-delete-cron-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-create-scheduled-event-syntax/#schema-metadata-delete-cron-trigger-syntax)
- [ create_scheduled_event ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-create-scheduled-event-syntax/#schema-metadata-create-scheduled-event)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-create-scheduled-event-syntax/#schema-metadata-create-scheduled-event-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)