# Clean up Event Data

## Introduction​

Hasura stores event data associated with Event Triggers in **the "hdb_catalog" schema of the database containing the source table** .

If there are many events, the Metadata tables can get huge, and you may want to prune them.

Automatic cleanup

In Cloud/Enterprise editions, you can use the[ Auto cleanup ](https://hasura.io/docs/latest/event-triggers/clean-up/auto-cleanup/)feature
to automatically and efficiently clean up your event logs.

## Tables involved​

Event Triggers have 2 tables managed by Hasura:

1. `hdb_catalog.event_log` : This is the table that stores all captured
events.
2. `hdb_catalog.event_invocation_logs` : This is that table that stores
all HTTP requests and responses.


## Option 1: Clear only HTTP logs​

`DELETE   FROM  hdb_catalog . event_invocation_logs ;`

## Option 2: Clear only processed events​

```
DELETE   FROM  hdb_catalog . event_log
WHERE  delivered  =   true   OR  error  =   true ;
```

## Option 3: Clear all processed events and HTTP logs​

This is the combination of Option 1 and Option 2.

```
DELETE   FROM  hdb_catalog . event_invocation_logs ;
DELETE   FROM  hdb_catalog . event_log
WHERE  delivered  =   true   OR  error  =   true ;
```

## Option 4: Clear all event data for a particular Event Trigger only​

```
DELETE   FROM
hdb_catalog . event_invocation_logs
WHERE  event_id  IN   (
     SELECT  id  FROM  hdb_catalog . event_log
     WHERE  trigger_name  =   '<event_trigger_name>'   ) ;
DELETE   FROM
hdb_catalog . event_log
WHERE  trigger_name  =   '<event_trigger_name>'
AND   ( delivered  =   true   OR  error  =   true ) ;
```

## Option 5: Clear everything​

Warning

This will clear all events including yet to be delivered events.

```
DELETE   FROM  hdb_catalog . event_invocation_logs ;
DELETE   FROM  hdb_catalog . event_log ;
```

## Clearing data before a particular time period​

If you wish to keep recent data and only clear data before a particular
time period you can add the following time clause to your query's where
clause:

```
-- units can be 'minutes', 'hours', 'days', 'months', 'years'
created_at  <   now ( )   -   interval   '<x> <units>'
```

For example: to delete all processed events and HTTP logs older than 3
months:

```
DELETE   FROM  hdb_catalog . event_invocation_logs
WHERE  created_at  <   now ( )   -   interval   '3 months' ;
DELETE   FROM  hdb_catalog . event_log
WHERE   ( delivered  =   true   OR  error  =   true )
  AND  created_at  <   now ( )   -   interval   '3 months' ;
```

See the[ Postgres date/time functions ](https://www.postgresql.org/docs/current/functions-datetime.html)for more details.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/event-triggers/clean-up/index/#introduction)
- [ Tables involved ](https://hasura.io/docs/latest/event-triggers/clean-up/index/#tables-involved)
- [ Option 1: Clear only HTTP logs ](https://hasura.io/docs/latest/event-triggers/clean-up/index/#option-1-clear-only-http-logs)
- [ Option 2: Clear only processed events ](https://hasura.io/docs/latest/event-triggers/clean-up/index/#option-2-clear-only-processed-events)
- [ Option 3: Clear all processed events and HTTP logs ](https://hasura.io/docs/latest/event-triggers/clean-up/index/#option-3-clear-all-processed-events-and-http-logs)
- [ Option 4: Clear all event data for a particular Event Trigger only ](https://hasura.io/docs/latest/event-triggers/clean-up/index/#option-4-clear-all-event-data-for-a-particular-event-trigger-only)
- [ Option 5: Clear everything ](https://hasura.io/docs/latest/event-triggers/clean-up/index/#option-5-clear-everything)
- [ Clearing data before a particular time period ](https://hasura.io/docs/latest/event-triggers/clean-up/index/#clearing-data-before-a-particular-time-period)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)