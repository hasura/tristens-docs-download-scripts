# Telemetry Guide/FAQ

## Introduction​

The Hasura GraphQL Engine collects anonymous telemetry data that helps the Hasura team in understanding how the product
is being used and in deciding what to focus on next.

The data collected is minimal, statistical in nature and **cannot be used to uniquely identify a user** . Please see the
next section to see what data is collected and sent. Access to collected data is strictly limited to the Hasura team and
not shared with 3rd parties.

As a growing community, we greatly appreciate the usage data users send to us, as it is very valuable in helping us make
the Hasura GraphQL Engine a better product for everyone! However, if you are concerned about sending usage stats, you
can choose to disable telemetry as described[ here ](https://hasura.io/docs/latest/policies/telemetry/#telemetry-optout).

## What data is collected?​

### Server​

The server periodically sends the number of tables, views, relationships, permission rules, custom SQL functions, event
triggers and Remote Schemas tracked by the GraphQL Engine, along with randomly generated UUIDs per database and per
instance. The name of the current continuous integration environment (if any) and the server version is also sent.

```
{
   "id" :   12 ,
   "timestamp" :   "2019-01-21T19:43:33.63838+00:00" ,
   "db_uid" :   "dddff371-dab2-450f-9969-235bca66dab1" ,
   "instance_uid" :   "6799360d-a431-40c5-9f68-24592a9f07df" ,
   "version" :   "v1.0.0-alpha36" ,
   "ci" :   "TRAVIS" ,
   "metrics" :   {
     "views" :   1 ,
     "tables" :   2 ,
     "functions" :   1 ,
     "permissions" :   {
       "roles" :   1 ,
       "delete" :   2 ,
       "insert" :   1 ,
       "select" :   2 ,
       "update" :   2
     } ,
     "relationships" :   {
       "auto" :   2 ,
       "manual" :   0
     } ,
     "event_triggers" :   0 ,
     "remote_schemas" :   1
   }
}
```

### Enterprise Edition server​

The Enterprise Edition server collects and sends additional types of telemetry.

Here are samples of all the types of telemetry sent by the Enterprise Edition server:

```
{
   "license_jti" :   "e86e5a54-ad3b-49e6-98ca-ab34b0a50f8f" ,
   "client_id" :   null ,
   "metadata_db_uid" :   "4492082b-a2d6-4d4c-81e5-f481b2aea669" ,
   "instance_uid" :   "f6d67a85-4a4f-4897-a767-89a86253b59c" ,
   "sample_uid" :   "2a18421a-baff-466b-bf34-b7fd6a5c76c8" ,
   "hasura_version" :   "v2.23.0" ,
   "metrics" :   {
     "api_limits_enabled" :   true ,
     "api_limits_roles_with_limits" :   0 ,
     "api_limits_rate_limits" :   0 ,
     "api_limits_depth_limits" :   0 ,
     "api_limits_node_limits" :   0 ,
     "api_limits_time_limits" :   0 ,
     "api_limits_batch_limits" :   0 ,
     "prometheus_endpoint_enabled" :   false ,
     "prometheus_secret_enabled" :   false ,
     "otel_enabled" :   false ,
     "otel_traces_enabled" :   false ,
     "allow_list_roles" :   0 ,
     "logs_http_response_log_enabled" :   false ,
     "logs_api_limit_log_enabled" :   false ,
     "logs_live_query_poller_log_enabled" :   false ,
     "logs_caching_log_enabled" :   false ,
     "logs_tracing_log_enabled" :   true ,
     "logs_metrics_log_enabled" :   false ,
     "logs_health_check_log_enabled" :   false ,
     "rate_limiting_enabled" :   false ,
     "caching_enabled" :   false ,
     "remote_schemas" :   0 ,
     "actions_synchronous" :   0 ,
     "actions_asynchronous" :   0 ,
     "actions_query" :   0 ,
     "actions_type_relationships" :   0 ,
     "actions_custom_types" :   0 ,
     "resource_cpu" :   2048 ,
     "resource_memory" :   0 ,
     "resource_checker_error_code" :   "CPU_MEMORY_INCONCLUSIVE" ,
     "jwt_secrets_configured" :   2 ,
     "admin_secrets_configured" :   2
   }
}
```

```
{
   "license_jti" :   "e86e5a54-ad3b-49e6-98ca-ab34b0a50f8f" ,
   "client_id" :   null ,
   "metadata_db_uid" :   "4492082b-a2d6-4d4c-81e5-f481b2aea669" ,
   "instance_uid" :   "f6d67a85-4a4f-4897-a767-89a86253b59c" ,
   "sample_uid" :   "2a18421a-baff-466b-bf34-b7fd6a5c76c8" ,
   "hasura_version" :   "12345" ,
   "metrics" :   {
     "backend_type" :   "postgres" ,
     "read_replicas" :   0 ,
     "health_check_enabled" :   false ,
     "tables" :   0 ,
     "views" :   0 ,
     "enum_tables" :   0 ,
     "relationships_manual" :   0 ,
     "relationships_auto" :   0 ,
     "permissions_select" :   0 ,
     "permissions_insert" :   0 ,
     "permissions_update" :   0 ,
     "permissions_delete" :   0 ,
     "permissions_roles" :   0 ,
     "event_triggers" :   0 ,
     "functions" :   0 ,
     "native_queries" :   0 ,
     "query_tags_enabled" :   false ,
     "connection_templates_enabled" :   false
   }
}
```

```
{    "license_jti" :   "e86e5a54-ad3b-49e6-98ca-ab34b0a50f8f" ,
   "client_id" :   null ,
   "metadata_db_uid" :   "4492082b-a2d6-4d4c-81e5-f481b2aea669" ,
   "instance_uid" :   "f6d67a85-4a4f-4897-a767-89a86253b59c" ,
   "sample_uid" :   "2a18421a-baff-466b-bf34-b7fd6a5c76c8" ,
   "hasura_version" :   "12345" ,
   "metrics" :   {
     "hasura_action_request_bytes_total" :   [   {   "value" :   0   }   ] ,
     "hasura_action_response_bytes_total" :   [   {   "value" :   0   }   ] ,
     "hasura_active_subscriptions" :   [   {   "value" :   0   }   ] ,
     "hasura_cron_events_invocation_total" :   [ { "status" :   "success" , "value" :   0 } ] ,
     "hasura_event_invocations_total" :   [ { "status" :   "success" , "value" :   0 } ] ,
     "hasura_event_trigger_http_workers" :   [   {   "value" :   0   }   ] ,
     "hasura_events_fetched_per_batch" :   [   {   "value" :   0   }   ] ,
     "hasura_event_trigger_request_bytes_total" :   [   {   "value" :   0   }   ] ,
     "hasura_event_trigger_response_bytes_total" :   [   {   "value" :   0   }   ] ,
     "hasura_graphql_requests_total" :   [ { "operation_type" :   "query" , "response_status" :   "failed" , "value" :   0 } ]
     "hasura_http_connections" :   [   {   "value" :   0   }   ] ,
     "hasura_http_request_bytes_total" :   [   {   "value" :   0   }   ] ,
     "hasura_http_response_bytes_total" :   [   {   "value" :   0   }   ] ,
     "hasura_metadata_resource_version" :   [   {   "value" :   1   }   ] ,
     "hasura_postgres_connections" :   [ { "role" :   "primary" , "source_name" :   "default" , "value" :   1 } ] ,
     "hasura_scheduled_trigger_request_bytes_total" :   [   {   "value" :   0   }   ] ,
     "hasura_scheduled_trigger_response_bytes_total" :   [   {   "value" :   0   }   ] ,
     "hasura_websocket_connections" :   [   {   "value" :   0   }   ] ,
     "hasura_websocket_messages_received_bytes_total" :   [   {   "value" :   0   }   ] ,
     "hasura_websocket_messages_sent_bytes_total" :   [   {   "value" :   0   }   ]
   }
}
```

### Console​

The Console collects runtime errors along with anonymized route names are sent without any identifiable information or
payload. The Console also records the UUID of the server/CLI that it is connected to.

Sample data:

```
{
   "server_version" :   "2.0.0" ,
   "event_type" :   "Main/RUN_TIME_ERROR" ,
   "url" :   "/data/schema/SCHEMA_NAME/tables/TABLE_NAME/modify" ,
   "console_mode" :   "cli" ,
   "cli_uuid" :   "0e4e2e9b-7fc9-44b8-9d5c-955673e20e0b" ,
   "server_uuid" :   "015a8f49-2fbd-4c41-8066-23f48d9c620a" ,
   "data" :   {   "message" :   "Uncaught TypeError: something is not a function" ,   "stack" :   [ " at main.js:1:3" ]   }
}
```

Please note that `TABLE_NAME` and `SCHEMA_NAME` are not placeholders. The actual names of the tables, schemas,
remote-schemas and event-triggers that are a part of the URL are not sent.

### CLI​

The CLI collects each execution event, along with a randomly generated UUID. The execution event contains the command
name, timestamp and whether the execution resulted in an error or not. **Error messages, arguments and flags are not
recorded** . The CLI also collects the server version and UUID that it is talking to. The operating system platform and
architecture is also noted along with the CLI version.

Sample data:

```
{
   "id" :   115 ,
   "timestamp" :   "2019-01-21T11:36:07.86783+00:00" ,
   "uuid" :   "e462ce20-42dd-40fd-9549-edfb92f80455" ,
   "execution_id" :   "ddfa9c33-0693-457d-9026-c7f456c43322" ,
   "version" :   "v0.4.27" ,
   "command" :   "hasura version" ,
   "is_error" :   false ,
   "os_platform" :   "linux" ,
   "os_arch" :   "amd64" ,
   "server_uuid" :   "a4d66fb2-f88d-457b-8db1-ea7a0b57921d" ,
   "server_version" :   "v1.0.0-alpha36" ,
   "payload" :   null
}
```

## Where is the data sent?​

The data is sent to Hasura's servers addressed by `telemetry.hasura.io` .

## How do I turn off telemetry (opt-out)?​

### Disable server telemetry​

You can turn off telemetry on **the server and on the Console hosted by the server** by setting the env variable `HASURA_GRAPHQL_ENABLE_TELEMETRY=false` or the flag `--enable-telemetry=false` on the server.

### Disable CLI telemetry​

You can turn off telemetry on **the CLI and on the Console served by the CLI** by setting the env variable `HASURA_GRAPHQL_ENABLE_TELEMETRY=false` on the machine running the CLI. You can also set `"enable_telemetry": false` in
the JSON config file created by the CLI at `~/.hasura/config.json` to persist the setting.

## Privacy Policy​

You can check out our privacy policy[ here ](https://hasura.io/legal/hasura-privacy-policy).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/policies/telemetry/#introduction)
- [ What data is collected? ](https://hasura.io/docs/latest/policies/telemetry/#what-data-is-collected)
    - [ Server ](https://hasura.io/docs/latest/policies/telemetry/#server)

- [ Enterprise Edition server ](https://hasura.io/docs/latest/policies/telemetry/#enterprise-edition-server)

- [ Console ](https://hasura.io/docs/latest/policies/telemetry/#console)

- [ CLI ](https://hasura.io/docs/latest/policies/telemetry/#cli)
- [ Where is the data sent? ](https://hasura.io/docs/latest/policies/telemetry/#where-is-the-data-sent)
- [ How do I turn off telemetry (opt-out)? ](https://hasura.io/docs/latest/policies/telemetry/#telemetry-optout)
    - [ Disable server telemetry ](https://hasura.io/docs/latest/policies/telemetry/#disable-server-telemetry)

- [ Disable CLI telemetry ](https://hasura.io/docs/latest/policies/telemetry/#disable-cli-telemetry)
- [ Privacy Policy ](https://hasura.io/docs/latest/policies/telemetry/#privacy-policy)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)