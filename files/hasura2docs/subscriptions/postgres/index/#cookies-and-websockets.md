# Postgres: GraphQL Subscriptions

## Introduction​

A GraphQL subscription is essentially a query where the client receives an update whenever the value of any field
changes upstream.

Subscriptions are supported for all kinds of queries. All the concepts of[ queries ](https://hasura.io/docs/latest/queries/postgres/index/)hold
true for subscriptions as well.

Postgres Compatibility

Hasura works with most[ Postgres compatible flavours ](https://hasura.io/docs/latest/databases/postgres/index/#postgres-compatible-flavors).

Single subscription in each query caveat

Hasura follows the[ GraphQL spec ](https://graphql.github.io/graphql-spec/June2018/#sec-Single-root-field)which allows
for only one root field in a subscription. You also cannot execute multiple separate subscriptions in one query. To
have multiple subscriptions running at the same time they must be in separate queries.

## Types of subscriptions​

### Live queries​

A live query subscription will return the latest result of the query being made and not necessarily all the individual
events leading up to the result. By default, updates are delivered to clients every **1 sec** .

See more details[ here ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/index/).

### Streaming subscriptions​

A streaming subscription streams the response according to the cursor input by the user. A streaming subscription is
different from a live query as it sends individual rows at a time and not the entire result set.

See more details[ here ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/index/).

### Live query vs streaming subscriptions​

Suppose we need to display the messages of a group chat on a page, this can be done either via live queries or streaming
subscriptions. Let's see how they can be used and how they differ from each other.

1. Using **live query** With live query, we'll make the following query:The initial response for this subscription will be all the messages of the group. Let's say the initial response
contained 100 messages. Now, if there is one more message sent to the group, then all 101 messages will be sent in a
new response.
2. Using **streaming subscriptions** With streaming subscriptions, we'll make the following query:Here, we'll start getting all messages of the group in batches given by `batch_size` with `created_at` greater than `now` .Following the example of the live query, if we have 100 messages corresponding to the group and only 5 messages with `created_at` greater than the current value of the cursor maintained by the cursor, then we will get only the 5
messages.


Using **live query** 

With live query, we'll make the following query:

```
subscription   {
   messages ( where :   {   group_id :   1   } ,   order_by :   {   created_at :   asc   } )   {
     id
     sender
     receiver
     content
     created_at
     edited_at
   }
}
```

The initial response for this subscription will be all the messages of the group. Let's say the initial response
contained 100 messages. Now, if there is one more message sent to the group, then all 101 messages will be sent in a
new response.

Using **streaming subscriptions** 

With streaming subscriptions, we'll make the following query:

```
subscription   {
   messages_stream ( where :   {   group_id :   1   } ,   cursor :   {   initial_value :   {   created_at :   now   }   } ,   batch_size :   10 )   {
     id
     sender
     receiver
     content
     created_at
     edited_at
   }
}
```

Here, we'll start getting all messages of the group in batches given by `batch_size` with `created_at` greater than `now` .

Following the example of the live query, if we have 100 messages corresponding to the group and only 5 messages with `created_at` greater than the current value of the cursor maintained by the cursor, then we will get only the 5
messages.

## Communication protocol​

Hasura GraphQL Engine uses the[ GraphQL over WebSocket Protocol ](https://github.com/apollographql/subscriptions-transport-ws/blob/master/PROTOCOL.md)by the[ apollographql/subscriptions-transport-ws ](https://github.com/apollographql/subscriptions-transport-ws)library
and the[ GraphQL over WebSocket Protocol ](https://github.com/enisdenjo/graphql-ws/blob/master/PROTOCOL.md)by the[ graphql-ws ](https://github.com/enisdenjo/graphql-ws)library for sending and receiving events. The GraphQL Engine uses
the `Sec-WebSocket-Protocol` header to determine the communication protocol that'll be used. By default, the GraphQL
engine will use the `apollographql/subscriptions-transport-ws` protocol.

Setting headers for subscriptions with Apollo client

If you are using Apollo Client, headers can be passed to a subscription by setting `connectionParams` while[ creating the wsLink ](https://www.apollographql.com/docs/react/data/subscriptions/#client-setup):

```
// Create a WebSocket link:
const  wsLink  =   new   WebSocketLink ( {
   uri :   ` <graphql-endpoint> ` ,
   options :   {
     reconnect :   true ,
     connectionParams :   {
       headers :   { headers - object }
     }
   }
} ) ;
```

See[ this ](https://www.apollographql.com/docs/react/data/subscriptions/#authentication-over-websocket)for more info on
using `connectionParams` .

## Cookies and WebSockets​

The Hasura GraphQL Engine will read cookies sent by the browser when initiating a WebSocket connection. The browser will
send the cookie only if it is a secure cookie ( `secure` flag in the cookie) and if the cookie has a `HttpOnly` flag.

Hasura will read this cookie and use it as headers when resolving authorization (i.e. when resolving the auth webhook).

### Cookies, WebSockets and CORS​

As browsers don't enforce Same Origin Policy (SOP) for websockets, the Hasura server enforces the CORS rules when
accepting the websocket connection.

It uses the provided CORS configuration (as per[ Configure CORS ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#configure-cors)).

1. When it is `*` , the cookie is read and the CORS check is not enforced.
2. When there are explicit domains, the cookie will only be read if the request originates from one of the listed
domains.
3. If CORS is disabled, the default behavior is that the cookie won't be read (because of potential security issues).
To override the behavior, you can use the flag `--ws-read-cookie` or the environment variable `HASURA_GRAPHQL_WS_READ_COOKIE` . See[ GraphQL Engine server config reference ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/)for the setting.


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/subscriptions/postgres/index/#cookies-and-websockets/#introduction)
- [ Types of subscriptions ](https://hasura.io/docs/latest/subscriptions/postgres/index/#cookies-and-websockets/#types-of-subscriptions)
    - [ Live queries ](https://hasura.io/docs/latest/subscriptions/postgres/index/#cookies-and-websockets/#live-queries)

- [ Streaming subscriptions ](https://hasura.io/docs/latest/subscriptions/postgres/index/#cookies-and-websockets/#streaming-subscriptions)

- [ Live query vs streaming subscriptions ](https://hasura.io/docs/latest/subscriptions/postgres/index/#cookies-and-websockets/#live-query-vs-streaming-subscriptions)
- [ Communication protocol ](https://hasura.io/docs/latest/subscriptions/postgres/index/#cookies-and-websockets/#communication-protocol)
- [ Cookies and WebSockets ](https://hasura.io/docs/latest/subscriptions/postgres/index/#cookies-and-websockets/#cookies-and-websockets)
    - [ Cookies, WebSockets and CORS ](https://hasura.io/docs/latest/subscriptions/postgres/index/#cookies-and-websockets/#cookies-websockets-and-cors)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)