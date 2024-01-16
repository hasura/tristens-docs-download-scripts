# Subscriptions Sample Use Cases

## Introduction​

The following are a few use cases for using subscriptions:

## Subscribe to the latest value of a particular field​

In case you are interested only in the latest value of a particular field, you can use subscriptions to fetch the field
and get updated with its latest value whenever it changes.

### Example: Live location tracking​

Use subscriptions to show the current location of a vehicle on a map.

Let's say we have the following database schema:

```
vehicle  (
  id  INT   PRIMARY   KEY ,
  vehicle_number  TEXT
)
vehicle_location  (
  id  INT   PRIMARY   KEY ,
  location  TEXT ,
   timestamp   TIMESTAMP ,
   /* used to create relationship 'locations' for vehicle */
  vehicle_id  INT   FOREIGN   KEY   REFERENCES  vehicle ( id )
)
```

Now we can use the following subscription to fetch the latest location of a vehicle to display it on a map:

## Subscribe to changes to a table's entries​

In case you are interested in all the additions/changes to a table's entries, you can use subscriptions to fetch the
table rows and get updates whenever there are any additions/changes to the table.

### Example: Chat app​

Use subscriptions to show new messages in a chatroom.

Let's say we have the following database schema:

```
user   (
  id  INT   PRIMARY   KEY ,
  username  TEXT   UNIQUE
)
message  (
  id  INT   PRIMARY   KEY ,
   text   TEXT ,
   timestamp   TIMESTAMP ,
   /* used to create relationship 'author' for message */
  user_id  INT   FOREIGN   KEY   REFERENCES   user ( id )
)
```

Now we can use the following subscription to display the latest messages in a chatroom:

## Subscribe to the latest value of some derived data​

In case you are interested in the latest value of some derived data, you can[ create a view to query the derived data ](https://hasura.io/docs/latest/schema/ms-sql-server/views/)and then use subscriptions to fetch the
derived value and get its latest value whenever it updates.

### Example: A poll dashboard​

Use subscriptions to show the result of a poll.

Let's say we have the following database schema:

```
poll  (
  id  INT   PRIMARY   KEY ,
  question  TEXT
)
option   (
  id  INT   PRIMARY   KEY
  poll_id  INT   FOREIGN   KEY   REFERENCES  poll ( id )
   text   TEXT
)
user   (
  id  INT   PRIMARY   KEY
  name  TEXT
)
vote  (
  id  INT   PRIMARY   KEY ,
  option_id  INT   FOREIGN   KEY   REFERENCES   option ( id ) ,
  user_id  INT   FOREIGN   KEY   REFERENCES   user ( id ) ,
   timestamp   TIMESTAMP
)
```

First, create a view `poll_results` to give the result of the poll:

```
CREATE   OR   REPLACE   VIEW   public . "poll_results"   AS
   SELECT  poll . id  AS  poll_id ,
         o . option_id ,
          count ( * )   AS  votes
     FROM   (
       (
         SELECT  vote . option_id ,
                option . poll_id ,
                option . text
           FROM   (
            vote
               LEFT   JOIN   option   ON   ( ( option . id  =  vote . option_id ) )
           )
         )  o
             LEFT   JOIN  poll  ON   ( ( poll . id  =  o . poll_id ) )
       )
   GROUP   BY  poll . question ,  o . option_id ,  poll . id ;
```

This view will have the following fields: `poll_id` , `option_id` and `votes` , i.e. it gives the number of votes received
by each option for a poll.

Next,[ set up relationships ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/index/) `poll` and `option` between the `poll_results` view and the `poll` and `option` tables using the `poll_id` and `option_id` fields respectively.

Now we can use the following subscription to display the latest poll result:

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/subscriptions/ms-sql-server/use-cases/#ms-sql-server-subscribe-field/#introduction)
- [ Subscribe to the latest value of a particular field ](https://hasura.io/docs/latest/subscriptions/ms-sql-server/use-cases/#ms-sql-server-subscribe-field/#ms-sql-server-subscribe-field)
    - [ Example: Live location tracking ](https://hasura.io/docs/latest/subscriptions/ms-sql-server/use-cases/#ms-sql-server-subscribe-field/#example-live-location-tracking)
- [ Subscribe to changes to a table's entries ](https://hasura.io/docs/latest/subscriptions/ms-sql-server/use-cases/#ms-sql-server-subscribe-field/#ms-sql-server-subscribe-table)
    - [ Example: Chat app ](https://hasura.io/docs/latest/subscriptions/ms-sql-server/use-cases/#ms-sql-server-subscribe-field/#example-chat-app)
- [ Subscribe to the latest value of some derived data ](https://hasura.io/docs/latest/subscriptions/ms-sql-server/use-cases/#ms-sql-server-subscribe-field/#ms-sql-server-subscribe-derived)
    - [ Example: A poll dashboard ](https://hasura.io/docs/latest/subscriptions/ms-sql-server/use-cases/#ms-sql-server-subscribe-field/#example-a-poll-dashboard)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)