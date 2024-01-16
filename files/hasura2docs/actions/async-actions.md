# Async Actions

## Introduction​

Sometimes you may not want to wait for an action to complete before
sending a response back to the client (say if the business logic takes a
long time). In such cases you can create an **asynchronous** action,
which returns an `action_id` immediately to the client before contacting
the handler.

If you mark an action as **asynchronous** , Hasura also generates a `query` and a `subscription` field for the action so that you can
query/subscribe to its status.

Note

Only Actions of type `mutation` can be async. Actions of type query are
always executed synchronously.

For example, let's say `place_order` is an asynchronous action

```
mutation   placeOrderRequest ( $order_input :   place_order_input ! )   {
   place_order ( input :   $order_input )
}
```

Executing this mutation will return a response like:

```
{
   "data" :   {
     "place_order" :   "23b1c256-7aff-4b95-95bd-68220d9f93f2"
   }
}
```

The returned `uuid` is the `action id` of the async action. To get the
actual response of the action, you can `query` or `subscribe` to the
action using this `action id` .

```
subscription   getPlaceOrderResponse   {
   place_order ( id :   "23b1c256-7aff-4b95-95bd-68220d9f93f2" )   {
     output
     errors
   }
}
```

Additional Resources

Introduction to Hasura Actions -[ View
Recording ](https://hasura.io/events/webinar/hasura-actions/?pg=docs&plcmt=body&cta=view-recording&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/actions/async-actions/#introduction)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)