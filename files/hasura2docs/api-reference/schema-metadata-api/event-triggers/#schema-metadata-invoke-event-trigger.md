# Schema/Metadata API Reference: Event Triggers (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

## Introduction​

Event Triggers are used to capture database changes and send them to a
configured webhook.

## create_event_trigger​

 `create_event_trigger` is used to create a new Event Trigger or replace
an existing Event Trigger.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "create_event_trigger" ,
     "args"   :   {
         "name" :   "sample_trigger" ,
         "table" :   {
            "name" :   "users" ,
            "schema" :   "public"
         } ,
         "webhook" :   "https://httpbin.org/post" ,
         "insert" :   {
             "columns" :   "*" ,
             "payload" :   [ "username" ]
         } ,
         "update" :   {
             "columns" :   [ "username" ,   "real_name" ] ,
             "payload" :   "*"
         } ,
         "delete" :   {
             "columns" :   "*"
         } ,
         "headers" : [
           {
               "name" :   "X-Hasura-From-Val" ,
               "value" :   "myvalue"
           } ,
           {
               "name" :   "X-Hasura-From-Env" ,
               "value_from_env" :   "EVENT_WEBHOOK_HEADER"
           }
         ] ,
         "replace" :   false
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| table | true | [ QualifiedTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#qualifiedtable) | Object with table name and schema |
| webhook | false | String | Full url of webhook (*) |
| webhook_from_env | false | String | Environment variable name of webhook (must exist at boot time) (*) |
| insert | false | [ OperationSpec ](https://hasura.io/docs/latest/api-reference/syntax-defs/#operationspec) | Specification for insert operation |
| update | false | [ OperationSpec ](https://hasura.io/docs/latest/api-reference/syntax-defs/#operationspec) | Specification for update operation |
| delete | false | [ OperationSpec ](https://hasura.io/docs/latest/api-reference/syntax-defs/#operationspec) | Specification for delete operation |
| headers | false | [[ HeaderFromValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#headerfromvalue)|[ HeaderFromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#headerfromenv)] | List of headers to be sent with the webhook |
| retry_conf | false | [ RetryConf ](https://hasura.io/docs/latest/api-reference/syntax-defs/#retryconf) | Retry configuration if event delivery fails |
| replace | false | Boolean | If set to true, the Event Trigger is replaced with the new definition |
| enable_manual | false | Boolean | If set to true, the Event Trigger can be invoked manually |


(*) Either `webhook` or `webhook_from_env` are required.

## delete_event_trigger​

 `delete_event_trigger` is used to delete an Event Trigger.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "delete_event_trigger" ,
     "args"   :   {
         "name" :   "sample_trigger"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |


## redeliver_event​

 `redeliver_event` is used to redeliver an existing event. For example,
if an event is marked as error ( say it did not succeed after retries),
you can redeliver it using this API. Note that this will reset the count
of retries so far. If the event fails to deliver, it will be retried
automatically according to its `retry_conf` .

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "redeliver_event" ,
     "args"   :   {
         "event_id" :   "ad4f698f-a14e-4a6d-a01b-38cd252dd8bf"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| event_id | true | String | UUID of the event |


## invoke_event_trigger​

 `invoke_event_trigger` is used to invoke an Event Trigger with custom payload.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "invoke_event_trigger" ,
     "args"   :   {
         "name" :   "sample_trigger" ,
         "payload" :   { }
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| payload | true | JSON | Some JSON payload to send to trigger |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-invoke-event-trigger/#introduction)
- [ create_event_trigger ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-invoke-event-trigger/#schema-metadata-create-event-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-invoke-event-trigger/#schema-metadata-create-event-trigger-syntax)
- [ delete_event_trigger ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-invoke-event-trigger/#schema-metadata-delete-event-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-invoke-event-trigger/#schema-metadata-delete-event-trigger-syntax)
- [ redeliver_event ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-invoke-event-trigger/#schema-metadata-redeliver-event)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-invoke-event-trigger/#schema-metadata-redeliver-event-syntax)
- [ invoke_event_trigger ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-invoke-event-trigger/#schema-metadata-invoke-event-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-invoke-event-trigger/#schema-metadata-invoke-event-trigger-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)