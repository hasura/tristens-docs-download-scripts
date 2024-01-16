# Invoke Event Trigger Manually

- Console
- API


You can select the `Via Console` trigger operation while[ creating an Event Trigger ](https://hasura.io/docs/latest/event-triggers/create-trigger/)to allow invoking the Event Trigger on rows manually using the Hasura Console.

In the `Data -> [table-name] -> Browse Rows` tab, clicking the `invoke trigger` button next to any row lets you invoke
"manual Event Triggers" configured on the table with that row as payload *(the button will be shown only if you have any
triggers configured)* :

Image: [ Invoke Event Trigger on the Console ](https://hasura.io/docs/assets/images/select-manual-trigger-428a7e07ad5eaa5626c68f337b698514.png)

Click on the Event Trigger you want to run and a modal will pop up with the request and response.

Image: [ Request and response of Event Trigger ](https://hasura.io/docs/assets/images/run-manual-trigger-5e8430e32e1773280f7349e07c374915.png)

When creating an Event Trigger over the[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)Metadata API,
you can set the argument `enable_manual` to true.

Then you can use the[ pg_invoke_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-invoke-event-trigger)Metadata API
to invoke triggers manually:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type"   :   "pg_invoke_event_trigger" ,
    "args"   :   {
       "source" :   "<db_name>" ,
       "name" :   "send_email" ,
       "payload" :   { }
    }
}
```

### What did you think of this doc?

Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)