# Metadata API Reference: Event Triggers

## Introduction​

Event Triggers are used to capture database changes and send them to a configured webhook.

Supported from

The Metadata API is supported for versions `v2.0.0` and above and replaces the older[ schema/Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

## pg_create_event_trigger​

 `pg_create_event_trigger` is used to create a new Event Trigger or replace an existing Event Trigger.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_create_event_trigger" ,
     "args"   :   {
         "name" :   "sample_trigger" ,
         "table" :   {
            "name" :   "users" ,
            "schema" :   "public"
         } ,
         "source" :   "default" ,
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
         "cleanup_config" :   {
             "schedule" :   "0 0 * * *" ,
             "batch_size" :   10000 ,
             "clear_older_than" :   168 ,
             "timeout" :   60 ,
             "clean_invocation_logs" :   false ,
             "paused" :   false
         } ,
         "replace" :   false
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| table | true | [ QualifiedTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#qualifiedtable) | Object with table name and schema |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| webhook | false | [ WebhookURL ](https://hasura.io/docs/latest/api-reference/syntax-defs/#webhookurl) | Event Trigger webhook URL |
| webhook_from_env | false | String | Environment variable name of webhook (Deprecated in favour of[ WebhookURL ](https://hasura.io/docs/latest/api-reference/syntax-defs/#webhookurl)) |
| insert | false | [ OperationSpec ](https://hasura.io/docs/latest/api-reference/syntax-defs/#operationspec) | Specification for insert operation |
| update | false | [ OperationSpec ](https://hasura.io/docs/latest/api-reference/syntax-defs/#operationspec) | Specification for update operation |
| delete | false | [ OperationSpec ](https://hasura.io/docs/latest/api-reference/syntax-defs/#operationspec) | Specification for delete operation |
| headers | false | [[ HeaderFromValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#headerfromvalue)|[ HeaderFromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#headerfromenv)] | List of headers to be sent with the webhook |
| retry_conf | false | [ RetryConf ](https://hasura.io/docs/latest/api-reference/syntax-defs/#retryconf) | Retry configuration if event delivery fails |
| replace | false | Boolean | If set to true, the Event Trigger is replaced with the new definition |
| enable_manual | false | Boolean | If set to true, the Event Trigger can be invoked manually |
| request_transform | false | [ RequestTransformation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation) | Attaches a Request Transformation to the Event Trigger. |
| response_transform | false | [ ResponseTransformation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#responsetransformation) | Attaches a Request Transformation to the Event Trigger. |
| cleanup_config | false | [ AutoEventTriggerCleanupConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#autoeventtriggercleanupconfig) | Cleanup config for the auto cleanup process (Enterprise Edition/Cloud only). |
| trigger_on_replication | false | Boolean | Specification for enabling/disabling the Event Trigger during logical replication |


(*) Either `webhook` or `webhook_from_env` are required.

Note

The default value of the `trigger_on_replication` parameter for Postgres sources will be `false` , which means that the
trigger will not fire during logical replication of data.

## pg_delete_event_trigger​

 `pg_delete_event_trigger` is used to delete an Event Trigger.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_delete_event_trigger" ,
     "args"   :   {
         "name" :   "sample_trigger" ,
         "source" :   "default"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the trigger (default: `default` ) |


## pg_redeliver_event​

 `redeliver_event` is used to redeliver an existing event. For example, if an event is marked as error ( say it did not
succeed after retries), you can redeliver it using this API. Note that this will reset the count of retries so far. If
the event fails to deliver, it will be retried automatically according to its `retry_conf` .

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_redeliver_event" ,
     "args"   :   {
         "event_id" :   "ad4f698f-a14e-4a6d-a01b-38cd252dd8bf"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| event_id | true | String | UUID of the event |


## pg_invoke_event_trigger​

 `invoke_event_trigger` is used to invoke an Event Trigger with custom payload.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_invoke_event_trigger" ,
     "args"   :   {
         "name" :   "sample_trigger" ,
         "source" :   "default" ,
         "payload" :   { }
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| payload | true | JSON | Some JSON payload to send to trigger |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the trigger (default: `default` ) |


## pg_get_event_logs​

 `pg_get_event_logs` is used to fetch the event logs for a given event trigger.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_get_event_logs" ,
   "args" :   {
     "name" :   "sample_trigger" ,
     "source" :   "default" ,
     "status" :   "processed" ,
     "limit" :   10 ,
     "offset" :   0
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the trigger (default: `default` ) |
| status | false | [ `pending` | `processed` ] | Type of event logs to be fetched. If `status` is not provided then all types of status are included |
| limit | false | Integer | Maximum number of event logs to be returned in one API call (default: `100` ) |
| offset | false | Integer | Starting point from where the event logs need to be returned (default: `0` ) |


## pg_get_event_invocation_logs​

 `pg_get_event_invocation_logs` is used to fetch the invocation logs for a given event trigger.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_get_event_invocation_logs" ,
   "args" :   {
     "name" :   "sample_trigger" ,
     "source" :   "default" ,
     "limit" :   10 ,
     "offset" :   0
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the trigger (default: `default` ) |
| limit | false | Integer | Maximum number of invocation logs to be returned in one API call (default: `100` ) |
| offset | false | Integer | Starting point from where the invocation logs need to be returned (default: `0` ) |


## pg_get_event_by_id​

 `pg_get_event_by_id` is used to fetch the event and invocation logs for a given `event_id` .

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_get_event_by_id" ,
   "args" :   {
     "source"   :   "default" ,
     "event_id"   :   "009335c9-7b01-4ea5-b790-66a112e165f9" ,
     "invocation_log_limit"   :   100 ,
     "invocation_log_offset"   :   0
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the trigger (default: `default` ) |
| event_id | true | String | UUID of the event |
| invocation_log_limit | false | Integer | Maximum number of invocation logs to be returned in one API call (default: `100` ) |
| invocation_log_offset | false | Integer | Starting point from where the invocation logs need to be returned (default: `0` ) |


## mssql_create_event_trigger​

 `mssql_create_event_trigger` is used to create a new Event Trigger or replace an existing Event Trigger.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_create_event_trigger" ,
     "args"   :   {
         "name" :   "sample_trigger" ,
         "table" :   {
            "name" :   "users" ,
            "schema" :   "public"
         } ,
         "source" :   "default" ,
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
         "cleanup_config" :   {
             "schedule" :   "0 0 * * *" ,
             "batch_size" :   10000 ,
             "clear_older_than" :   168 ,
             "timeout" :   60 ,
             "clean_invocation_logs" :   false ,
             "paused" :   false
         } ,
         "replace" :   false
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| table | true | [ QualifiedTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#qualifiedtable) | Object with table name and schema |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| webhook | false | String | Full url of webhook (*) |
| webhook_from_env | false | String | Environment variable name of webhook (must exist at boot time) (*) |
| insert | false | [ OperationSpec ](https://hasura.io/docs/latest/api-reference/syntax-defs/#operationspec) | Specification for insert operation |
| update | false | [ OperationSpec ](https://hasura.io/docs/latest/api-reference/syntax-defs/#operationspec) | Specification for update operation |
| delete | false | [ OperationSpec ](https://hasura.io/docs/latest/api-reference/syntax-defs/#operationspec) | Specification for delete operation |
| headers | false | [[ HeaderFromValue ](https://hasura.io/docs/latest/api-reference/syntax-defs/#headerfromvalue)|[ HeaderFromEnv ](https://hasura.io/docs/latest/api-reference/syntax-defs/#headerfromenv)] | List of headers to be sent with the webhook |
| retry_conf | false | [ RetryConf ](https://hasura.io/docs/latest/api-reference/syntax-defs/#retryconf) | Retry configuration if event delivery fails |
| replace | false | Boolean | If set to true, the Event Trigger is replaced with the new definition |
| enable_manual | false | Boolean | If set to true, the Event Trigger can be invoked manually |
| request_transform | false | [ RequestTransformation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation) | Attaches a Request Transformation to the Event Trigger. |
| response_transform | false | [ ResponseTransformation ](https://hasura.io/docs/latest/api-reference/syntax-defs/#responsetransformation) | Attaches a Request Transformation to the Event Trigger. |
| cleanup_config | false | [ AutoEventTriggerCleanupConfig ](https://hasura.io/docs/latest/api-reference/syntax-defs/#autoeventtriggercleanupconfig) | Cleanup config for the auto cleanup process (Enterprise Edition/Cloud only). |
| trigger_on_replication | false | Boolean | Specification for enabling/disabling the Event Trigger during logical replication |


(*) Either `webhook` or `webhook_from_env` are required.

Note

The default value of the `trigger_on_replication` parameter for MSSQL sources will be `true` , which means that the
trigger will be fired during logical replication of data.

## mssql_delete_event_trigger​

 `mssql_delete_event_trigger` is used to delete an Event Trigger.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_delete_event_trigger" ,
     "args"   :   {
         "name" :   "sample_trigger" ,
         "source" :   "default"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the Event Trigger (default: `default` ) |


## mssql_redeliver_event​

 `mssql_redeliver_event` is used to redeliver an existing event. For example, if an event is marked as error (say it did
not succeed after retries), you can redeliver it using this API. Note that this will reset the count of retries so far.
If the event fails to deliver, it will be retried automatically according to its `retry_conf` .

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_redeliver_event" ,
     "args"   :   {
         "event_id" :   "ad4f698f-a14e-4a6d-a01b-38cd252dd8bf"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| event_id | true | String | UUID of the event |


## mssql_invoke_event_trigger​

 `invoke_event_trigger` is used to invoke an Event Trigger with custom payload.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_invoke_event_trigger" ,
     "args"   :   {
         "name" :   "sample_trigger" ,
         "source" :   "default" ,
         "payload" :   { }
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| payload | true | JSON | Some JSON payload to send to trigger |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the trigger (default: `default` ) |


## mssql_get_event_logs​

 `mssql_get_event_logs` is used to fetch the event logs for a given event trigger.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_get_event_logs" ,
   "args" :   {
     "name" :   "sample_trigger" ,
     "source" :   "default" ,
     "status" :   "processed" ,
     "limit" :   10 ,
     "offset" :   0
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the trigger (default: `default` ) |
| status | false | [ `pending` | `processed` ] | Type of event logs to be fetched. If `status` is not provided then all types of status are included |
| limit | false | Integer | Maximum number of event logs to be returned in one API call (default: `100` ) |
| offset | false | Integer | Starting point from where the event logs need to be returned (default: `0` ) |


## mssql_get_event_invocation_logs​

 `mssql_get_event_invocation_logs` is used to fetch the invocation logs for a given event trigger.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_get_event_invocation_logs" ,
   "args" :   {
     "name" :   "sample_trigger" ,
     "source" :   "default" ,
     "limit" :   10 ,
     "offset" :   0
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ TriggerName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggername) | Name of the Event Trigger |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the trigger (default: `default` ) |
| limit | false | Integer | Maximum number of invocation logs to be returned in one API call (default: `100` ) |
| offset | false | Integer | Starting point from where the invocation logs need to be returned (default: `0` ) |


## mssql_get_event_by_id​

 `mssql_get_event_by_id` is used to fetch the event and invocation logs for a given `event_id` .

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_get_event_by_id" ,
   "args" :   {
     "source"   :   "default" ,
     "event_id"   :   "81531A4C-AED7-4EFE-964D-D115A77B05C2" ,
     "invocation_log_limit"   :   100 ,
     "invocation_log_offset"   :   0
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the trigger (default: `default` ) |
| event_id | true | String | UUID of the event |
| invocation_log_limit | false | Integer | Maximum number of invocation logs to be returned in one API call (default: `100` ) |
| invocation_log_offset | false | Integer | Starting point from where the invocation logs need to be returned (default: `0` ) |


## cleanup_event_trigger_logs​

 `cleanup_event_trigger_logs` is used to manually delete the event logs for a given Event Trigger.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type"   :   "cleanup_event_trigger_logs" ,
   "args" :   {
     "event_trigger_name" :   "sample_trigger" ,
     "source" :   "default" ,
     "batch_size" :   10000 ,
     "clear_older_than" :   168 ,
     "timeout" :   60 ,
     "clean_invocation_logs" :   false
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| event_trigger_name | true | String | Name of the Event Trigger whose logs needs to be cleaned up |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Source to which the Event Trigger belong. Default `default`  |
| batch_size | false | Int | Maximum number of logs to delete in a single statement during the cleanup action. If there are more events to be cleaned than the `batch_ size` then the cleanup action will execute multiple statements sequentially until all old event logs are cleared. Default 10000 |
| clear_older_than | true | Int | Event logs retention period (in hours). |
| timeout | false | Int | Maximum time (in seconds) that a batch can take during the cleanup process. If a batch times out, the cleanup process is halted. Default: 60 |
| clean_invocation_logs | false | Boolean | Should corresponding invocation logs be cleaned. Default `false`  |


## resume_event_trigger_cleanups​

 `resume_event_trigger_cleanups` is used to resume the paused log cleaner for Event Triggers.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "resume_event_trigger_cleanups" ,
   "args" :   {
     "event_triggers" :   [
       {
         "source_name" :   "default" ,
         "event_triggers" :   [ "sample_trigger" ]
       }
     ]
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| event_triggers | true | [ TriggerLogCleanupSources ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggerlogcleanupsources)|[ [EventTriggerQualifier] ](https://hasura.io/docs/latest/api-reference/syntax-defs/#eventtriggerqualifier) | Event Triggers for which to start the cleanup process |


## pause_event_trigger_cleanups​

- `pause_event_trigger_cleanups` is used to pause the log cleaner for event triggers which already have a cleaner
installed.


```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pause_event_trigger_cleanups" ,
   "args" :   {
     "event_triggers" :   [
       {
         "source_name" :   "default" ,
         "event_triggers" :   [ "sample_trigger" ]
       }
     ]
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| event_triggers | true | [ TriggerLogCleanupSources ](https://hasura.io/docs/latest/api-reference/syntax-defs/#triggerlogcleanupsources)|[ [EventTriggerQualifier] ](https://hasura.io/docs/latest/api-reference/syntax-defs/#eventtriggerqualifier) | Event Triggers for which to pause the cleanup process |


Note

The start and pause APIs for Event Trigger cleanup work only for Event Triggers that have a cleanup configuration
defined.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#introduction)
- [ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-create-event-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-create-event-trigger-syntax)
- [ pg_delete_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-delete-event-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-delete-event-trigger-syntax)
- [ pg_redeliver_event ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-redeliver-event)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-redeliver-event-syntax)
- [ pg_invoke_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-invoke-event-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-invoke-event-trigger-syntax)
- [ pg_get_event_logs ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-get-event-logs)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-get-event-logs-syntax)
- [ pg_get_event_invocation_logs ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-get-event-invocation-logs)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-get-event-invocation-logs-syntax)
- [ pg_get_event_by_id ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-get-event-by-id)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pg-get-event-by-id-syntax)
- [ mssql_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-create-event-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-create-event-trigger-syntax)
- [ mssql_delete_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-delete-event-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-delete-event-trigger-syntax)
- [ mssql_redeliver_event ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-redeliver-event)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-redeliver-event-syntax)
- [ mssql_invoke_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-invoke-event-trigger)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-invoke-event-trigger-syntax)
- [ mssql_get_event_logs ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-get-event-logs)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-get-event-logs-syntax)
- [ mssql_get_event_invocation_logs ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-get-event-invocation-logs)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-get-event-invocation-logs-syntax)
- [ mssql_get_event_by_id ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-get-event-by-id)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-mssql-get-event-by-id-syntax)
- [ cleanup_event_trigger_logs ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-cleanup-event-trigger-logs)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-cleanup-event-trigger-logs-syntax)
- [ resume_event_trigger_cleanups ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-resume-event-trigger-cleanups)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-resume-event-trigger-cleanups-syntax)
- [ pause_event_trigger_cleanups ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pause-event-trigger-cleanups)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger/#metadata-pause-event-trigger-cleanups-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)