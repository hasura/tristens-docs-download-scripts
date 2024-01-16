# Streaming Subscriptions Sample Use Cases

## Introduction​

The following are a few use cases for using streaming subscriptions, **all without the need for sticky sessions** :

### Subscribing only to the events that have been changed​

In case you are interested only in the latest events, you can use streaming subscriptions to fetch those events.

### Get the undelivered messages in a chat application​

Consider the following schema:

```
   messages  (
     id  serial   primary   key ,
     from_id uuid  references  users ( id ) ,
     to_id uuid  references  users ,
     content  text ,
      status   text ,
     created_at timestamptz  default   now ( ) ,
    )
   users  (
     id uuid  primary   key ,
     first_name  text ,
     last_name  text ,
     created_at timestamptz  default   current_timestamp
    )
```

and the following messages need to be streamed:

```
[
   {
     "id" :   432432 ,
     "from" :   {
       "first_name" :   "Cindy"
     } ,
     "to" :   {
       "first_name" :   "Michael"
     } ,
     "content" :   "Heyyy" ,
     "created_at" :   "2020-01-01 01:00:00"
   } ,
   {
     "id" :   432433 ,
     "from" :   {
       "first_name" :   "Michael"
     } ,
     "to" :   {
       "first_name" :   "Cindy"
     } ,
     "content" :   "Heyy! How are you?" ,
     "created_at" :   "2020-01-01 01:01:20"
   } ,
   {
     "id" :   432434 ,
     "from" :   {
       "first_name" :   "Cindy"
     } ,
     "to" :   {
       "first_name" :   "Michael"
     } ,
     "content" :   "I'm good! What about you?" ,
     "created_at" :   "2020-01-01 01:01:40"
   } ,
   {
     "id" :   432435 ,
     "from" :   {
       "first_name" :   "Michael"
     } ,
     "to" :   {
       "first_name" :   "Cindy"
     } ,
     "content" :   "All good here too! Thanks" ,
     "created_at" :   "2020-01-01 01:02:00"
   }
]
```

To stream the latest undelivered messages:

```
subscription   getUndeliveredMessages   {
   # will get all the messages that have `created_at > 2022-01-01` in batches of 2 rows
   messages_stream ( cursor :   {   initial_value :   {   created_at :   "2022-01-01"   } ,   ordering :   ASC   } ,   batch_size :   2 )   {
     id
     from   {
       first_name
     }
     to   {
       first_name
     }
     content
     created_at
   }
}
```

The first response sent will be:

```
{
   "data" :   {
     "messages_stream" :   [
       {
         "id" :   432432 ,
         "from" :   {
           "first_name" :   "Cindy"
         } ,
         "to" :   {
           "first_name" :   "Michael"
         } ,
         "content" :   "Heyyy" ,
         "created_at" :   "2020-01-01 01:00:00"
       } ,
       {
         "id" :   432433 ,
         "from" :   {
           "first_name" :   "Michael"
         } ,
         "to" :   {
           "first_name" :   "Cindy"
         } ,
         "content" :   "Heyy! How are you?" ,
         "created_at" :   "2020-01-01 01:01:20"
       }
     ]
   }
}
```

The next response sent will be the following, note that the messages sent have `created_at > 2020-01-01 01:01:20` , the
greatest value of the cursor column sent in the previous response.

```
{
   "data" :   {
     "messages_stream" :   [
       {
         "id" :   432434 ,
         "from" :   {
           "first_name" :   "Cindy"
         } ,
         "to" :   {
           "first_name" :   "Michael"
         } ,
         "content" :   "I'm good! What about you?" ,
         "created_at" :   "2020-01-01 01:01:40"
       } ,
       {
         "id" :   432435 ,
         "from" :   {
           "first_name" :   "Michael"
         } ,
         "to" :   {
           "first_name" :   "Cindy"
         } ,
         "content" :   "All good here too! Thanks" ,
         "created_at" :   "2020-01-01 01:02:00"
       }
     ]
   }
}
```

### Deal with out-of-order events​

Consider the following schema:

```
  cart_items  (
    id  serial   primary   key ,
    cart_id  integer   references  carts ( id ) ,
    product_id  integer   references  products ( id ) ,
    quantity  integer ,
    created_at timestamptz  default   now ( ) ,
   )
   carts  (
     id  serial   primary   key ,
     user_id uuid  references  users ( id ) ,
      status   text ,
     created_at timestamptz  default   now ( ) ,
    )
   users  (
     id uuid  primary   key ,
     first_name  text ,
     last_name  text ,
     created_at timestamptz  default   current_timestamp
    )
```

A user might add an item to their cart, remove it, and then add it again. If the updates are processed out of order, the
item might be removed from the cart even though the user intended to keep it.

To deal with this, you can use the `cursor` argument to stream the events in the order they were created.

```
subscription   getCartItems   {
   cart_items_stream ( cursor :   {   initial_value :   {   created_at :   "2022-01-01"   } ,   ordering :   ASC   } )   {
     id
     cart   {
       id
       user   {
         first_name
       }
     }
     product   {
       name
     }
     quantity
     created_at
   }
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/use-cases/#introduction)
    - [ Subscribing only to the events that have been changed ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/use-cases/#subscribing-only-to-the-events-that-have-been-changed)

- [ Get the undelivered messages in a chat application ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/use-cases/#get-the-undelivered-messages-in-a-chat-application)

- [ Deal with out-of-order events ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/use-cases/#deal-with-out-of-order-events)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)