# Auto Cleanup of Event Trigger Logs

Supported from

Auto cleanup for Event Triggers is available from Hasura version `v2.13` and above.

## Introduction​

Hasura provides a way to automate the cleanup of the Event Trigger logs based on the following parameters:

| Name of the parameter | Description | Default | Example |
|---|---|---|---|
| clear_older_than | Minimum age (in hours) of the event logs that need to be cleared from when the cleanup action is invoked. | - |  `clear_ older_ than: 168` means logs older than 168 hours (7 days) will be deleted. |
| schedule | Cron expression at which the cleanup should be invoked. | - | A `0 0 * * *` schedule means that the cleanup will be invoked every day at 00:00 (UTC time). |
| clean_invocation_logs | Option to indicate whether the corresponding invocation logs are also to be cleaned. | false |  `clean_ invocation_ logs: false` means that invocation logs will not be cleaned. |
| batch_size | Maximum number of logs to delete in a single statement during the cleanup action. If there are more events to be cleaned than the `batch_ size` then the cleanup action will execute multiple statements sequentially until all old event logs are cleared. | 10000 | Suppose there are 10000 events pending deletion and a `batch_ size` of 1000 then the cleanup will be performed in 10 batches sequentially. |
| timeout | Maximum time (in seconds) that a batch can take during the cleanup process. If a batch times out, the cleanup process is halted. | 60 | A timeout of 60 means a batch of cleanup should not take more than 60 seconds. If a batch takes more than the `timeout` , then all the subsequent batches for the cleanup action will be cancelled. |
| paused | Indicates if the auto-cleanup process is paused. | false |  `paused: true` means cleanup is paused, hence no logs will be deleted. |


## Auto cleanup​

For automatic cleanup, you can provide a cleanup config while[ adding the event trigger ](https://hasura.io/docs/latest/event-triggers/create-trigger/)and Hasura will clean up the logs according to the
provided config.

- Console
- CLI
- API


For an existing Event Trigger, head to the `Modify` tab of the Event Trigger and scroll down to the `Auto-cleanup Event Logs` section.

Image: [ Auto cleanup ](https://hasura.io/docs/assets/images/auto-cleanup-4d0a84ceaf9b71b4c4a14a20448d007c.png)

To add an auto cleanup config, update the `databases > [source-name] > tables > [table-name].yaml` file inside the
Metadata directory as in this example:

```
table :
   name :  users
   schema :  public
event_triggers :
   -   name :  send_email
     definition :
       enable_manual :   true
       insert :
         columns :   '*'
     retry_conf :
       interval_sec :   10
       num_retries :   0
       timeout_sec :   60
     webhook :  https : //send.email
     cleanup_config :
       batch_size :   10000
       clean_invocation_logs :   true
       clear_older_than :   168
       paused :   false
       schedule :   '0 0 * * *'
       timeout :   60
```

Apply the Metadata by running:

`hasura metadata apply`

You can add a auto cleanup config using the `<backend>_create_event_trigger` Metadata API.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type"   :   "pg_create_event_trigger" ,
   "args" :   {
     "name" :   "send_email" ,
     "source" :   "default" ,
     "table" :   "users" ,
     "insert" :   {
       "columns" :   "*"
     } ,
     "webhook" :   "https://send.email" ,
     "cleanup_config" :   {
       "batch_size" :   10000 ,
       "clean_invocation_logs" :   true ,
       "clear_older_than" :   168 ,
       "paused" :   false ,
       "schedule" :   "0 0 * * *" ,
       "timeout" :   60
     }
}
```

Warning

If you initially choose not to delete `invocation_logs` , but later they need to be deleted, you will need to delete the
retained logs manually.

## Manual APIs​

For cleaning up the Event Trigger logs using an API, Hasura provides the[ cleanup_event_trigger_logs ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-cleanup-event-trigger-logs)API.

## Managing automatic cleaners​

For the ease of managing automated cleanups, Hasura provides few Metadata APIs such as:

- [ resume_event_trigger_cleanups ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-start-event-trigger-cleanups):
This API resumes the cleanup process (sets `paused` to `false` ).
- [ pause_event_trigger_cleanups ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pause-event-trigger-cleanups):
This API pauses the cleanup process (sets `paused` to `true` ).


Tip

While applying Migrations, you may pause all the installed cleaners for better performance.

### API usage examples​

- Activate the cleaners on all the triggers defined on all the event-trigger-supported sources


```
POST /v1/metadata HTTP/ 1.1
Content-Type :  application/json
X-Hasura-Role :  admin
{
   "type"   :   "resume_event_trigger_cleanups" ,
   "args" :   {
     "event_triggers" :   {
       "sources" :   "*"
     }
   }
}
```

- Activate the cleaners on all the triggers defined on the sources: `source_1` , `source_2`


```
POST /v1/metadata HTTP/ 1.1
Content-Type :  application/json
X-Hasura-Role :  admin
{
   "type"   :   "resume_event_trigger_cleanups" ,
   "args" :   {
     "event_triggers" :   {
       "sources" :   [ "source_1" ,   "source_2" ]
     }
   }
}
```

- Activate the cleaners on triggers: `sample_trigger_1` , `sample_trigger_2` defined on source `default`


```
POST /v1/metadata HTTP/ 1.1
Content-Type :  application/json
X-Hasura-Role :  admin
{
   "type" :   "resume_event_trigger_cleanups" ,
   "args" :   {
     "event_triggers" :   [
       {
         "source_name" :   "default" ,
         "event_triggers" :   [ "sample_trigger_1" ,   "sample_trigger_2" ]
       }
     ]
   }
}
```

Note

The management APIs will only affect the Event Trigger log cleaners if the Event Triggers have cleaners configured.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/event-triggers/clean-up/auto-cleanup/#introduction)
- [ Auto cleanup ](https://hasura.io/docs/latest/event-triggers/clean-up/auto-cleanup/#auto-cleanup)
- [ Manual APIs ](https://hasura.io/docs/latest/event-triggers/clean-up/auto-cleanup/#manual-apis)
- [ Managing automatic cleaners ](https://hasura.io/docs/latest/event-triggers/clean-up/auto-cleanup/#managing-automatic-cleaners)
    - [ API usage examples ](https://hasura.io/docs/latest/event-triggers/clean-up/auto-cleanup/#api-usage-examples)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)