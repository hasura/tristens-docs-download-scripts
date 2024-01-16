# Metadata API Reference: Scheduled Triggers

## Introduction​

Scheduled Triggers are used to invoke webhooks based on a timestamp or
cron.

Supported from

The Metadata API is supported for versions `v2.0.0` and above and
replaces the older[ schema/Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

## create_cron_trigger​

 `create_cron_trigger` is used to create a new cron trigger.

```
POST   /v1/metadata   HTTP/1.1
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
| request_transform | false | [ RequestTransformation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation) | Attaches a Request Transformation to the cron trigger. |
| response_transform | false | [ ResponseTransformation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#responsetransformation) | Attaches a Request Transformation to the cron trigger. |


Supported from

Scheduled Triggers are supported from versions `v1.3.0` and above.

## delete_cron_trigger​

 `delete_cron_trigger` is used to delete an existing cron trigger. The
scheduled events associated with the cron trigger will also be deleted.

```
POST   /v1/metadata   HTTP/1.1
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
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "create_scheduled_event" ,
     "args" :   {
         "webhook" :   "https://httpbin.org/post" ,
         "schedule_at" :   "2019-09-09T22:00:00Z" ,
         "payload" :   {
             "key1" :   "value1" ,
             "key2" :   "value2"
         } ,
         "headers" :   [ {
             "name" : "header-key" ,
             "value" : "header-value"
         } ] ,
         "comment" :   "sample scheduled event comment"
     }
}
```

Upon creating a scheduled event successfully, this API will return the `event_id` in the response.

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "message" :   "success" ,
     "event_id" :   "b918cd10-8853-4e66-91b8-81b5cd16e44b"
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

## delete_scheduled_event​

 `delete_scheduled_event` is used to delete an existing scheduled event
(one-off or cron).

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "delete_scheduled_event" ,
     "args"   :   {
         "type" :   "one_off" ,
         "event_id" :   "b918cd10-8853-4e66-91b8-81b5cd16e44b"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| type | true |  `one_ off` | `cron`  | Type of the Event Trigger. |
| event_id | true | UUID | The `id` of the scheduled event. |


Supported from

Scheduled Triggers are supported from versions `v1.3.0` and above.

## get_cron_triggers​

 `get_cron_triggers` fetches all the cron triggers from the metadata.
This API also returns the cron triggers which have `include_in_metadata` set to `false` , and thus are not exported in the `export_metadata` API.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "get_cron_triggers" ,
     "args"   :   { }
}
```

## get_scheduled_events​

 `get_scheduled_events` provides a way to retrieve cron/one-off scheduled
events present in the graphql-engine.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "get_scheduled_events" ,
     "args"   :   {
       "type" :   "cron" ,
       "trigger_name" :   "daily_trigger" ,
       "limit" :   10 ,
       "offset" :   0 ,
       "status" :   [
         "scheduled" ,
         "delivered"
       ] ,
       "get_rows_count" :   false
     }
}
```

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "get_scheduled_events" ,
     "args"   :   {
       "type" :   "one_off" ,
       "limit" :   10 ,
       "offset" :   0 ,
       "get_rows_count" :   true
     }
}
```

### Args Syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| type | true |  `one_ off` | `cron`  | Type of the Scheduled Trigger. |
| trigger_name | only when `type` is `cron`  | String | Name of the cron trigger |
| limit | false | Integer | Maximum number of events to be returned in one API call. |
| offset | false | Integer | Starting point from where the rows need to be returned. |
| get_rows_count | false | Boolean | Flag to indicate whether number of rows returned should be included in the response. |
| status | false | [ [ScheduledEventStatus] ](https://hasura.io/docs/latest/api-reference/syntax-defs/#scheduledEventStatus) | Filter scheduled events by the status |


## get_scheduled_event_invocations​

 `get_scheduled_event_invocations` provides a way to retrieve the scheduled
event invocations of a specific scheduled event or a cron trigger.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "get_scheduled_event_invocations" ,
     "args" :   {
         "type" :   "cron" ,
         "trigger_name" :   "daily_trigger" ,
         "limit" :   10 ,
         "offset" :   0
     }
}
```

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "get_scheduled_event_invocations" ,
     "args"   :   {
       "type" :   "one_off" ,
       "limit" :   10 ,
       "offset" :   0 ,
       "get_rows_count" :   true
     }
}
```

### Args Syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| type | true |  `one_ off` | `cron`  | Type of the Scheduled Trigger. |
| trigger_name | only when `type` is `cron`  | String | Name of the cron trigger |
| event_id | false | String | Getting invocations of the specified event |
| limit | false | Integer | Maximum number of events to be returned in one API call. |
| offset | false | Integer | Starting point from where the rows need to be returned. |
| get_rows_count | false | Boolean | Flag to indicate whether number of rows returned should be included in the response. |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#introduction)
- [ create_cron_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-create-cron-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-create-cron-trigger-syntax)
- [ delete_cron_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-delete-cron-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-delete-cron-trigger-syntax)
- [ create_scheduled_event ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-create-scheduled-event)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-create-scheduled-event-syntax)
- [ delete_scheduled_event ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-delete-scheduled-event)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-delete-scheduled-event-syntax)
- [ get_cron_triggers ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-get-cron-triggers)
- [ get_scheduled_events ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-get-scheduled-events)
    - [ Args Syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-get-scheduled-events-syntax)
- [ get_scheduled_event_invocations ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-get-scheduled-event-invocations)
    - [ Args Syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-scheduled-event-invocations/#metadata-get-scheduled-event-invocations-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)