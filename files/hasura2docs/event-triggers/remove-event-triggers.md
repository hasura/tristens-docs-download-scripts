# Remove Event Triggers

## Removing Event Triggers​

Event Triggers can be removed using the Hasura Console, Hasura CLI, or Metadata APIs.

- Console
- CLI
- API


Open the Hasura Console, head to the `Events` tab, click on the Event Trigger you want to delete, and click on the `Delete Event Trigger` button at the bottom of the page:

Image: [ Delete an Event Trigger ](https://hasura.io/docs/assets/images/event-triggers_delete-event-trigger_2-17-570e605b2f3d5e00294e02a3354aba95.png)

You can remove an Event Trigger for a table by updating the `databases > [source-name] > tables > [table-name].yaml` file
inside the `metadata` directory and removing the event trigger from it:

```
-   table :
    schema :  public
    name :  author
event_triggers :
    -   name :  author_trigger
    definition :
       enable_manual :   false
       insert :
          columns :   "*"
       update :
          columns :   "*"
    webhook :  https : //httpbin.org/post
```

Apply the Metadata by running:

`hasura metadata apply`

You can delete Event Triggers by using the appropriate Metadata API, either:[ pg_delete_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-delete-event-trigger)or[ mssql_delete_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-delete-event-trigger).

To delete an Event Trigger via the the Metadata API, replace `<db_type_delete_event_trigger>` with the following:

- **Postgres** : `pg_delete_event_trigger`
- **MSSQL** : `mssql_delete_event_trigger`


```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type"   :   "<db_type_delete_event_trigger>" ,
    "args"   :   {
         "name" :   "author_trigger" ,
         "source" :   "default"
     }
}
```

Event Triggers for a table or source will also get dropped if the corresponding[ table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-untrack-table)/[ source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#metadata-pg-drop-source)is dropped.

Warning

An Event Trigger can be removed using the above methods (Delete Event Trigger, Drop Table or Drop Source) only when the metadata is consistent.

If the metadata is inconsistent, then an Event Trigger can be dropped using "[ Replace Metadata ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-replace-metadata)" or "[ Clear Metadata ](https://hasura.io/docs/latest/api-reference/metadata-api/manage-metadata/#metadata-clear-metadata)"
methods. This may leave some footprint in the source which can be cleaned manually as described in the following
section.

## Clean up Event Trigger footprints manually​

When an Event Trigger is created, Hasura creates SQL triggers on the table corresponding to each database operation
( `INSERT` / `UPDATE` / `DELETE` ) described in the Event Trigger configuration.

When an inconsistent Table/Event Trigger is removed via the `replace_metadata` API, it may leave orphaned SQL triggers
in the database. The following command can be used to manually delete SQL triggers corresponding to an Event Trigger on
a table:

`DROP   FUNCTION  hdb_catalog . "notify_hasura_<event-trigger-name>_<OPERATION-NAME>"   CASCADE ;`

For example: to delete SQL triggers corresponding to an Event Trigger: `users_all` on a table: `users` with operation: `INSERT` in the Event Trigger configuration:

`DROP   FUNCTION  hdb_catalog . "notify_hasura_users_all_INSERT"   CASCADE ;`

Deleting all triggers

The SQL trigger should be deleted for each operation mentioned in the Event Trigger configuration, i.e. `INSERT` / `UPDATE` / `DELETE` 

## Clean up Hasura footprints from a source manually​

When a source in an inconsistent state is dropped, it may leave Hasura footprints in the database due to Event Triggers.
The following can be used to remove all footprints of Event Triggers present in a source from the database:

### Case 1: When using a different Metadata database to the source database​

In this case, `hdb_metadata` table is not present in `hdb_catalog` schema of the source.

To clean up Hasura footprint completely, drop the `hdb_catalog` schema:

`DROP   SCHEMA   IF   EXISTS  hdb_catalog ;`

### Case 2: When the Metadata database and source database are the same​

In this case, a `hdb_metadata` table is present in the `hdb_catalog` schema of the source. You may want to preserve the
Metadata but remove the remaining Hasura footprint of a few tables for Event Triggers and corresponding SQL triggers.

 **Step 1:** In order to drop the SQL triggers corresponding to Event Triggers created, please refer to the[ clean up Event Trigger footprints manually ](https://hasura.io/docs/latest/event-triggers/remove-event-triggers/#clean-up-event-trigger-footprints-manually)section. Alternatively, the following command can be used to drop all SQL triggers in the source:

```
do  $$
declare  f record ;
begin
   for  f  in   select  trigger_name ,  event_object_table
     from  information_schema . triggers
     where  trigger_name  like   'notify_hasura_%'
   loop
     EXECUTE   'DROP FUNCTION hdb_catalog.'   ||  QUOTE_IDENT ( f . trigger_name )   ||   ' CASCADE' ;
   end   loop ;
end ;
$$ ;
```

 **Step 2:** The following commands can be used to delete Event Triggers tables from `hdb_catalog` :

```
DROP   TABLE   IF   EXISTS  hdb_catalog . hdb_source_catalog_version ;
DROP   FUNCTION   IF   EXISTS  hdb_catalog . insert_event_log ( text ,   text ,   text ,   text ,  json ) ;
DROP   TABLE   IF   EXISTS  hdb_catalog . event_invocation_logs ;
DROP   TABLE   IF   EXISTS  hdb_catalog . event_log ;
DROP   TABLE   IF   EXISTS  hdb_catalog . hdb_event_log_cleanups ;
```

Execute as single transaction

It is recommended to perform the above steps in a single transaction.

### What did you think of this doc?

- [ Removing Event Triggers ](https://hasura.io/docs/latest/event-triggers/remove-event-triggers/#removing-event-triggers)
- [ Clean up Event Trigger footprints manually ](https://hasura.io/docs/latest/event-triggers/remove-event-triggers/#clean-up-event-trigger-footprints-manually)
- [ Clean up Hasura footprints from a source manually ](https://hasura.io/docs/latest/event-triggers/remove-event-triggers/#clean-footprints-manually)
    - [ Case 1: When using a different Metadata database to the source database ](https://hasura.io/docs/latest/event-triggers/remove-event-triggers/#case-1-when-using-a-different-metadata-database-to-the-source-database)

- [ Case 2: When the Metadata database and source database are the same ](https://hasura.io/docs/latest/event-triggers/remove-event-triggers/#case-2-when-the-metadata-database-and-source-database-are-the-same)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)