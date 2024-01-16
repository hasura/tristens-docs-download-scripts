# Clean Up Scheduled Triggers Data

## Introduction​

Hasura stores event data associated with Scheduled Triggers in **the "hdb_catalog" schema of the Hasura Metadata
database** .

If there are lots of events, the events tables can get huge and you may want to prune them. You can use any of the
following options to prune your event data depending on your need.

Note

For each project in Hasura Cloud the retention period for cron events and invocation logs for cron triggers is 1 month.

## Tables involved​

Cron triggers have two tables managed by Hasura:

1. `hdb_catalog.hdb_cron_events` : Table that stores all the cron events.
2. `hdb_catalog.hdb_cron_event_invocation_logs` : Table that stores all the HTTP requests and their responses of the cron
events invocations.


Similarly, scheduled events also have two tables managed by Hasura:

1. `hdb_catalog.hdb_scheduled_events` : Table that stores all the scheduled events.
2. `hdb_catalog.hdb_scheduled_event_invocation_logs` : Table that stores all the HTTP requests and their responses of the
scheduled events invocations.


## Option 1: Clear only HTTP logs​

1. Cron event invocation logs


`DELETE   FROM  hdb_catalog . hdb_cron_event_invocation_logs ;`

1. Scheduled event invocation logs


`DELETE   FROM  hdb_catalog . hdb_scheduled_event_invocation_logs ;`

## Option 2: Clear processed events​

1. Cron events


```
DELETE   FROM  hdb_catalog . hdb_cron_events
WHERE   status   IN   ( 'delivered' ,   'error' ,   'dead' ) ;
```

1. Scheduled events


```
DELETE   FROM  hdb_catalog . hdb_scheduled_events
WHERE   status   IN   ( 'delivered' ,   'error' ,   'dead' ) ;
```

Note

Deleting a cron/scheduled event will also delete the invocations related to that event.

Warning

The below options will clear all events including yet to be delivered events. If the cron trigger exists in the
metadata, then new events will be generated automatically by the graphql-engine, but this step can take upto a minute.

## Option 3: Clear all data for a particular cron trigger only​

```
DELETE   FROM  hdb_catalog . hdb_cron_events
WHERE  trigger_name  =   '<trigger_name>' ;
```

## Option 4: Clear everything​

1. Cron triggers


`DELETE   FROM  hdb_catalog . hdb_cron_events ;`

1. Scheduled events


`DELETE   FROM  hdb_catalog . hdb_scheduled_events ;`

## Clearing data before a particular time period​

If you wish to keep recent data and only clear data before a particular time period you can add the following time
clause to your query's where clause:

```
-- units can be 'minutes', 'hours', 'days', 'months', 'years'
scheduled_time  <   now ( )   -   interval   '<x> <units>'
```

For example: to delete all processed events and HTTP logs older than 3 months:

1. Cron triggers


```
DELETE   FROM  hdb_catalog . hdb_cron_events
WHERE   status   IN   ( 'delivered' ,   'error' ,   'dead' )
   AND  scheduled_time  <   now ( )   -   interval   '3 months' ;
```

1. Scheduled events


```
DELETE   FROM  hdb_catalog . hdb_scheduled_events
WHERE   status   IN   ( 'delivered' ,   'error' ,   'dead' )
  AND  scheduled_time  <   now ( )   -   interval   '3 months' ;
```

See the[ Postgres date/time functions ](https://www.postgresql.org/docs/current/functions-datetime.html)for more
details.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/scheduled-triggers/clean-up/#introduction)
- [ Tables involved ](https://hasura.io/docs/latest/scheduled-triggers/clean-up/#tables-involved)
- [ Option 1: Clear only HTTP logs ](https://hasura.io/docs/latest/scheduled-triggers/clean-up/#option-1-clear-only-http-logs)
- [ Option 2: Clear processed events ](https://hasura.io/docs/latest/scheduled-triggers/clean-up/#option-2-clear-processed-events)
- [ Option 3: Clear all data for a particular cron trigger only ](https://hasura.io/docs/latest/scheduled-triggers/clean-up/#option-3-clear-all-data-for-a-particular-cron-trigger-only)
- [ Option 4: Clear everything ](https://hasura.io/docs/latest/scheduled-triggers/clean-up/#option-4-clear-everything)
- [ Clearing data before a particular time period ](https://hasura.io/docs/latest/scheduled-triggers/clean-up/#clearing-data-before-a-particular-time-period)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)