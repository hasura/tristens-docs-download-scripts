# Clean up Async Action Logs

## Introduction​

Hasura stores action logs of[ async Actions ](https://hasura.io/docs/latest/actions/async-actions/)in a table
in **the "hdb_catalog" schema of the Hasura Metadata database** .

As the table gets larger, you may want to prune it. You can use any of the following options to prune your logs depending on
your need.

Warning

- Deleting logs is irreversible, so be careful with these Actions.
- Deleting logs while subscriptions for the response might still be
open may result into the loss of data and `null` values been
returned.


## The table involved​

There is a specific table for action logs that is managed by Hasura:

- `hdb_catalog.hdb_action_log` : This table stores all captured action logs.


## Option 1: Delete log of a particular action invocation​

`DELETE   FROM  hdb_catalog . hdb_action_log  WHERE  id  =   '<async-action-id>' ;`

## Option 2: Delete all logs of a specific action​

`DELETE   FROM  hdb_catalog . hdb_action_log  WHERE  action_name  =   '<action-name>' ;`

## Option 3: Delete all logs​

`DELETE   FROM  hdb_catalog . hdb_action_log ;`

## Clearing data before a particular time period​

If you wish to keep recent data and only clear data before a particular time period
you can add the following time clause to your query's where clause:

```
-- units can be 'minutes', 'hours', 'days', 'months', 'years'
created_at  <   now ( )   -   interval   '<x> <units>'
```

For example: to delete all logs older than 3 months:

`DELETE   FROM  hdb_catalog . hdb_action_log  WHERE  created_at  <   NOW ( )   -   INTERVAL   '3 months' ;`

See the[ Postgres date/time functions ](https://www.postgresql.org/docs/current/functions-datetime.html)for more details.

Additional Resources

Introduction to Hasura Actions -[ View Recording ](https://hasura.io/events/webinar/hasura-actions/?pg=docs&plcmt=body&cta=view-recording&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/actions/logs-clean-up/#introduction)
- [ The table involved ](https://hasura.io/docs/latest/actions/logs-clean-up/#the-table-involved)
- [ Option 1: Delete log of a particular action invocation ](https://hasura.io/docs/latest/actions/logs-clean-up/#option-1-delete-log-of-a-particular-action-invocation)
- [ Option 2: Delete all logs of a specific action ](https://hasura.io/docs/latest/actions/logs-clean-up/#option-2-delete-all-logs-of-a-specific-action)
- [ Option 3: Delete all logs ](https://hasura.io/docs/latest/actions/logs-clean-up/#option-3-delete-all-logs)
- [ Clearing data before a particular time period ](https://hasura.io/docs/latest/actions/logs-clean-up/#clearing-data-before-a-particular-time-period)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)