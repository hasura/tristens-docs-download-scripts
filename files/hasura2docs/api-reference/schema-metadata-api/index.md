# Schema / Metadata API Reference (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

## Introduction​

The schema / Metadata API provides the following features:

1. Execute SQL on the underlying Postgres database, supports schema
modifying actions.
2. Modify Hasura Metadata (permission rules and relationships).


This is primarily intended to be used as an `admin` API to manage the
Hasura schema and metadata.

## Endpoint​

All requests are `POST` requests to the `/v1/query` endpoint.

## Request structure​

```
POST   /v1/query   HTTP/1.1
{
   "type": "<query-type>",
   "args": <args-object>
}
```

### Request body​

`[ Query ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/#schema-metadata-api-query)`

#### Query​

| Key | Required | Schema | Description |
|---|---|---|---|
| type | true | String | Type of the query |
| args | true | JSON Value | The arguments to the query |
| version | false | Integer | Version of the API (default: 1) |


## Request types​

The various types of queries are listed in the following table:

| type | args | version | Synopsis |
|---|---|---|---|
|  **bulk**  | [ Query ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/#schema-metadata-api-query)array | 1 | Execute multiple operations in a single query |
| [ run_sql ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/run-sql/#schema-metadata-run-sql) | [ run_sql_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/run-sql/#schema-metadata-run-sql-syntax) | 1 | Run SQL directly on Postgres |
| [ track_table ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-track-table) | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | 1 | Add a table/view |
| [ track_table ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-track-table-v2) | [ track_table_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-track-table-syntax-v2) | 2 | Add a table/view with configuration |
| [ set_table_customization ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-customization) | [ set_table_customization_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-customization-syntax) | 1 | Set table customization of an already tracked table |
| [ set_table_custom_fields (deprecated) ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-custom-fields) | [ set_table_custom_fields_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-custom-fields-syntax) | 2 | Set custom fields of an already tracked table (deprecated) |
| [ untrack_table ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-untrack-table) | [ untrack_table_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-untrack-table-syntax) | 1 | Remove a table/view |
| [ set_table_is_enum ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum) | [ set_table_is_enum_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/#schema-metadata-set-table-is-enum-syntax) | 1 | Set a tracked table as an enum table |
| [ track_function ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-functions/#schema-metadata-track-function) | [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#functionname) | 1 | Add an SQL function |
| [ track_function ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-functions/#schema-metadata-track-function-v2) | [ track_function_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-functions/#schema-metadata-track-function-syntax-v2) | 2 | Add an SQL function with configuration |
| [ untrack_function ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-functions/#schema-metadata-untrack-function) | [ FunctionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#functionname) | 1 | Remove an SQL function |
| [ create_object_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-object-relationship) | [ create_object_relationship_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-object-relationship-syntax) | 1 | Define a new object relationship |
| [ create_array_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship) | [ create_array_relationship_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship-syntax) | 1 | Define a new array relationship |
| [ drop_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-drop-relationship) | [ drop_relationship_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-drop-relationship-syntax) | 1 | Drop an existing relationship |
| [ rename_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-rename-relationship) | [ rename_relationship_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-rename-relationship-syntax) | 1 | Modify name of an existing relationship |
| [ set_relationship_comment ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-set-relationship-comment) | [ set_relationship_comment_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-set-relationship-comment-syntax) | 1 | Set comment on an existing relationship |
| [ add_computed_field ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/computed-field/#schema-metadata-add-computed-field) | [ add_computed_field_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/computed-field/#schema-metadata-add-computed-field-syntax) | 1 | Add a computed field |
| [ drop_computed_field ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/computed-field/#schema-metadata-drop-computed-field) | [ drop_computed_field_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/computed-field/#schema-metadata-drop-computed-field-syntax) | 1 | Drop a computed field |
| [ create_insert_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-create-insert-permission) | [ create_insert_permission_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-create-insert-permission-syntax) | 1 | Specify insert permission |
| [ drop_insert_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-insert-permission) | [ drop_insert_permission_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-insert-permission-syntax) | 1 | Remove existing insert permission |
| [ create_select_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-create-select-permission) | [ create_select_permission_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-create-select-permission-syntax) | 1 | Specify select permission |
| [ drop_select_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-select-permission) | [ drop_select_permission_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-select-permission-syntax) | 1 | Remove existing select permission |
| [ create_update_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-create-update-permission) | [ create_update_permission_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-create-update-permission-syntax) | 1 | Specify update permission |
| [ drop_update_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-update-permission) | [ drop_update_permission_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-update-permission-syntax) | 1 | Remove existing update permission |
| [ create_delete_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-create-delete-permission) | [ create_delete_permission_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-create-delete-permission-syntax) | 1 | Specify delete permission |
| [ drop_delete_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission) | [ drop_delete_permission_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-drop-delete-permission-syntax) | 1 | Remove existing delete permission |
| [ set_permission_comment ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-set-permission-comment) | [ set_permission_comment_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/#schema-metadata-set-permission-comment-syntax) | 1 | Set comment on an existing permission |
| [ create_event_trigger ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-create-event-trigger) | [ create_event_trigger_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-create-event-trigger-syntax) | 1 | Create or replace an Event Trigger |
| [ delete_event_trigger ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-delete-event-trigger) | [ delete_event_trigger_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-delete-event-trigger-syntax) | 1 | Delete an existing Event Trigger |
| [ redeliver_event ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-redeliver-event) | [ redeliver_event_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-redeliver-event-syntax) | 1 | Redeliver an existing event |
| [ invoke_event_trigger ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-invoke-event-trigger) | [ invoke_event_trigger_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/#schema-metadata-invoke-event-trigger-syntax) | 1 | Invoke a trigger with custom payload |
| [ create_cron_trigger ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-create-cron-trigger) | [ create_cron_trigger_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-create-cron-trigger-syntax) | 1 | Create a cron trigger |
| [ delete_cron_trigger ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-delete-cron-trigger) | [ delete_cron_trigger_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-delete-cron-trigger-syntax) | 1 | Delete an existing cron trigger |
| [ get_cron_triggers ](https://hasura.io/docs/latest/api-reference/metadata-api/scheduled-triggers/#metadata-get-cron-triggers) | [ Empty Object ](https://hasura.io/docs/latest/api-reference/syntax-defs/#empty-object) | 1 | Fetch all the cron triggers |
| [ create_scheduled_event ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-create-scheduled-event) | [ create_scheduled_event_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/scheduled-triggers/#schema-metadata-create-scheduled-event-syntax) | 1 | Create a new scheduled event |
| [ add_remote_schema ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-add-remote-schema) | [ add_remote_schema_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-add-remote-schema-syntax) | 1 | Add a remote GraphQL server as a Remote Schema |
| [ update_remote_schema ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-update-remote-schema) | [ update_remote_schema_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-update-remote-schema-syntax) | 1 | Update the details for a Remote Schema |
| [ remove_remote_schema ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-remove-remote-schema) | [ remove_remote_schema_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-remove-remote-schema-syntax) | 1 | Remove an existing Remote Schema |
| [ reload_remote_schema ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-reload-remote-schema) | [ reload_remote_schema_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/#schema-metadata-reload-remote-schema-syntax) | 1 | Reload schema of an existing Remote Schema |
| [ add_remote_schema_permissions ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schema-permissions/#schema-metadata-add-remote-schema-permissions) | [ add_remote_schema_permissions ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schema-permissions/#schema-metadata-add-remote-schema-permissions-syntax) | 1 | Add permissions to a role of an existing Remote Schema |
| [ drop_remote_schema_permissions ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schema-permissions/#schema-metadata-drop-remote-schema-permissions) | [ drop_remote_schema_permissions ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schema-permissions/#schema-metadata-drop-remote-schema-permissions-syntax) | 1 | Drop existing permissions defined for a role for a Remote Schema |
| [ create_remote_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-create-remote-relationship) | [ create_remote_relationship_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-create-remote-relationship-syntax) | 1 | Create a remote relationship with an existing Remote Schema |
| [ update_remote_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-update-remote-relationship) | [ update_remote_relationship_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-update-remote-relationship-syntax) | 1 | Update an existing remote relationship |
| [ delete_remote_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-delete-remote-relationship) | [ delete_remote_relationship_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-relationships/#schema-metadata-delete-remote-relationship-syntax) | 1 | Delete an existing remote relationship |
| [ export_metadata ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/manage-metadata/#schema-metadata-export-metadata) | [ Empty Object ](https://hasura.io/docs/latest/api-reference/syntax-defs/#empty-object) | 1 | Export the current Metadata |
| [ replace_metadata ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/manage-metadata/#schema-metadata-replace-metadata) | [ replace_metadata_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/manage-metadata/#schema-metadata-replace-metadata-syntax) | 1 | Import and replace existing Metadata |
| [ reload_metadata ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/manage-metadata/#schema-metadata-reload-metadata) | [ reload_metadata_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/manage-metadata/#schema-metadata-reload-metadata-syntax) | 1 | Reload changes to the underlying Postgres DB |
| [ clear_metadata ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/manage-metadata/#schema-metadata-clear-metadata) | [ Empty Object ](https://hasura.io/docs/latest/api-reference/syntax-defs/#empty-object) | 1 | Clear/wipe-out the current Metadata state form server |
| [ get_inconsistent_metadata ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/manage-metadata/#schema-metadata-get-inconsistent-metadata) | [ Empty Object ](https://hasura.io/docs/latest/api-reference/syntax-defs/#empty-object) | 1 | List all inconsistent Metadata objects |
| [ drop_inconsistent_metadata ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/manage-metadata/#schema-metadata-drop-inconsistent-metadata) | [ Empty Object ](https://hasura.io/docs/latest/api-reference/syntax-defs/#empty-object) | 1 | Drop all inconsistent Metadata objects |
| [ create_query_collection ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-create-query-collection) | [ create_query_collection_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-create-query-collection-syntax) | 1 | Create a query collection |
| [ rename_query_collection ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection) | [ rename_query_collection_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax) | 1 | Rename a query collection |
| [ drop_query_collection ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-drop-query-collection) | [ drop_query_collection_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-drop-query-collection-syntax) | 1 | Drop a query collection |
| [ add_query_to_collection ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-add-query-to-collection) | [ add_query_to_collection_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-add-query-to-collection-syntax) | 1 | Add a query to a given collection |
| [ drop_query_from_collection ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-drop-query-from-collection) | [ drop_query_from_collection_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-drop-query-from-collection-syntax) | 1 | Drop a query from a given collection |
| [ add_collection_to_allowlist ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-add-collection-to-allowlist) | [ add_collection_to_allowlist_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-add-collection-to-allowlist-syntax) | 1 | Add a collection to the allow-list |
| [ drop_collection_from_allowlist ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-drop-collection-from-allowlist) | [ drop_collection_from_allowlist_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-drop-collection-from-allowlist-syntax) | 1 | Drop a collection from the allow-list |
| [ set_custom_types ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-types/#schema-metadata-set-custom-types) | [ set_custom_types_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-types/#schema-metadata-set-custom-types-syntax) | 1 | Set custom GraphQL types |
| [ create_action ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action) | [ create_action_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-syntax) | 1 | Create an action |
| [ drop_action ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-drop-action) | [ drop_action_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-drop-action-syntax) | 1 | Drop an action |
| [ update_action ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-update-action) | [ update_action_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-update-action-syntax) | 1 | Update an action |
| [ create_action_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission) | [ create_action_permission_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-create-action-permission-syntax) | 1 | Create an action permission |
| [ drop_action_permission ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-drop-action-permission) | [ drop_action_permission_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/#schema-metadata-drop-action-permission-syntax) | 1 | Drop an action permission |
| [ create_rest_endpoint ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/restified-endpoints/#schema-metadata-create-rest-endpoint) | [ create_rest_endpoint_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/restified-endpoints/#schema-metadata-create-rest-endpoint-syntax) | 3 | Create a RESTified GraphQL Endpoint |
| [ drop_rest_endpoint ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/restified-endpoints/#schema-metadata-drop-rest-endpoint) | [ drop_rest_endpoint_args ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/restified-endpoints/#schema-metadata-drop-rest-endpoint-syntax) | 3 | Drop a RESTified GraphQL Endpoint |


 **See:** 

- [ Run SQL ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/run-sql/)
- [ Tables/Views ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/table-view/)
- [ Custom SQL Functions ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-functions/)
- [ Relationships ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/)
- [ Computed Fields ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/computed-field/)
- [ Permissions ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/permission/)
- [ Remote Schema Permissions ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schema-permissions/)
- [ Event Triggers ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/event-triggers/)
- [ Remote Schemas ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/remote-schemas/)
- [ Query Collections ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/)
- [ Custom Types ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/custom-types/)
- [ Actions ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/actions/)
- [ Manage Metadata ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/manage-metadata/)


## Response structure​

| Status code | Description | Response structure |
|---|---|---|
| 200 | Success | Request specific |
| 400 | Bad request |  `{"path" : String, "error" : String}`  |
| 401 | Unauthorized |  `{"error" : String}`  |
| 500 | Internal server error |  `{"error" : String}`  |


## Error codes​

| Status Code | Code | Error |
|---|---|---|
| 400 | postgres-error | Not-NULL violation. null value in column `<column-name>` violates not-null constraint |
| 400 | permission-denied | select on `<column/table>` for role `<role-name>` is not allowed. |
| 400 | not-exists | table `<table-name>` does not exist |
| 400 | not-exists | no such table/view exists in source: `<table-name>`  |
| 400 | not-exists |  `<field-name>` does not exist |
| 400 | already-tracked | view/table already tracked: `<table-name>`  |
| 400 | access-denied | restricted access: admin only |
| 400 | not-supported | table renames are not yet supported: `<table-name>`  |
| 400 | not-exists |  `<column-name>` does not exist |
| 400 | already-exists | cannot add column `<column-name>` in table `<table-name>` as a relationship with the name already exists |
| 400 | invalid-json | invalid json |
| 400 | not-supported | column renames are not yet supported: `<table-name>` . `<column-name>`  |
| 400 | invalid-headers | missing header: `<header-name>`  |
| 400 | dependency-error | cannot change type of column `<column-name>` in table `<table-name>` because of the following dependencies: `<dependencies>`  |
| 400 | invalid-headers | X-Hasura-User-Id should be an integer |
| 400 | dependency-error | cannot drop due to the following dependent objects: `<dependencies>`  |
| 400 | access-denied | You have to be admin to access this endpoint |
| 400 | parse-failed | parsing dotted table failed: `<table-name>`  |
| 400 | access-denied | not authorized to access this tx |
| 400 | already-exists | multiple declarations exist for the following `<table-name>` : `<duplicates>`  |
| 400 | not-exists | tx does not exists |
| 400 | already-exists | column/relationship of table `<table-name>` already exists |
| 400 | already-initialized | the state seems to be initialized already. \ \ you may need to migrate from this version: `<catalog-version>`  |
| 400 | constraint-error | no foreign constraint exists on the given column |
| 400 | not-supported | unsupported version: `<catalog-version>`  |
| 400 | constraint-error | more than one foreign key constraint exists on the given column |
| 400 | already-exists | the query template already exists `<template-name>`  |
| 400 | permission-error |  `<permission-type>` ' permission on `<table-name>` for role `<role-name>` already exists |
| 400 | permission-error |  `<permission-type>` ' permission on `<table-name>` for role `<role-name>` does not exist |
| 400 | unexpected-payload | Unknown operator: `<operator-type>`  |
| 400 | unexpected-payload | expecting a string for column operator |
| 400 | unexpected-payload | incompatible column types: ' `<column-name>` ', ' `<column-name>` ' |
| 400 | unexpected-payload | Expecting 'constraint' or 'constraint_on' when the 'action' is 'update' |
| 400 | unexpected-payload | constraint' and 'constraint_on' cannot be set at a time |
| 400 | unexpected-payload | upsert is not allowed for role ' `<role-name>` ' |
| 400 | unexpected-payload | objects should not be empty |
| 400 | invalid-params | missing parameter: `<param-name>`  |
| 400 | unexpected-payload | can't be empty |
| 400 |  |  `<col-name>` is a relationship and should be expanded |
| 400 | unexpected-payload |  `<column-name>` ' should be included in 'columns' |
| 400 | unexpected-payload |  `<column-name>` ' is an array relationship and can't be used in 'order_by' |
| 400 |  |  `<column-name>` ' is a Postgres column and cannot be chained further |
| 400 | unexpected-payload | order_by array should not be empty |
| 400 | unexpected-payload | when selecting an 'obj_relationship' 'where', 'order_by', 'limit' and 'offset' can't be used |
| 400 | unexpected-payload | atleast one of $set, $inc, $mul has to be present |
| 400 | permission-denied |  `<permission-type>` on `<table-name>` for role `<role-name>` is not allowed |
| 400 | not-exists | no such column exists: `<column-name>`  |
| 400 | permission-denied | role `<role-name>` does not have permission to `<permission-type>` column `<column-name>`  |
| 400 |  | expecting a postgres column; but, `<name>` is relationship |
| 400 | unexpected-payload | JSON column can not be part of where clause |
| 400 | unexpected-payload | is of type `<type-name>` ; this operator works only on column of types `<[types]>`  |
| 400 | postgres-error | query execution failed |
| 500 | unexpected | unexpected dependency of relationship: `<dependency>`  |
| 500 | unexpected | unexpected dependent object: `<dependency>`  |
| 500 | unexpected | field already exists |
| 500 | unexpected | field does not exist |
| 500 | unexpected | permission does not exist |
| 500 | postgres-error | postgres transaction error |
| 500 | postgres-error | connection error |
| 500 | postgres-error | postgres query error |
| 404 | not-found | No such resource exists |


## Disabling schema / Metadata API​

Since this API can be used to make changes to the GraphQL schema, it can
be disabled, especially in production deployments.

The `enabled-apis` flag or the `HASURA_GRAPHQL_ENABLED_APIS` env var can
be used to enable/disable this API. By default, the schema/Metadata API
is enabled. To disable it, you need to explicitly state that this API is
not enabled i.e. remove it from the list of enabled APIs.

```
# enable only graphql api, disable Metadata and pgdump
--enabled-apis = "graphql"
HASURA_GRAPHQL_ENABLED_APIS = "graphql"
```

See[ GraphQL Engine server config reference ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/)for info on setting the above flag/env var.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/#introduction)
- [ Endpoint ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/#endpoint)
- [ Request structure ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/#request-structure)
    - [ Request body ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/#request-body)
- [ Request types ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/#request-types)
- [ Response structure ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/#response-structure)
- [ Error codes ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/#error-codes)
- [ Disabling schema / Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/#disabling-schema--metadata-api)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)