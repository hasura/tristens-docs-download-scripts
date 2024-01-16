# Hasura Cloud Data Usage Calculation

## How do we calculate data usage?​

Hasura Cloud projects are billed based on the amount of data that passes through Hasura Cloud. This data corresponds to
the operations that are performed by you, your apps, or your clients.

The data pass-through is calculated by analyzing the logs that are sent from your project. All data transfer from Hasura
Cloud to external networks - such as your database server, external webhooks for[ Actions ](https://hasura.io/docs/latest/actions/overview/),[ Event Triggers ](https://hasura.io/docs/latest/event-triggers/overview/),[ Scheduled Triggers ](https://hasura.io/docs/latest/scheduled-triggers/overview/)or your[ Remote Schema ](https://hasura.io/docs/latest/remote-schemas/overview/)- is accounted for in Hasura Cloud billing.

We account for the following types of logs in Hasura Cloud data pass-through:

- `http-log` : The data usage is calculated by the request and response sizes of `http-log` . HTTP request size is
dependent on the size of cookies and request headers. Streamlining the response data will help reduce the HTTP
response size and corresponding data usage. Client-side errors like validation, query syntax, and rate-limiting errors
are not accounted for in billing.
- `ws-server` : The volume of data sent and received through a WebSocket connection is considered when calculating your
data usage. WebSocket connections are typically used for subscriptions. You can optimize the amount of data sent via
subscriptions to reduce `ws-server` data usage.
- `action-handler-log` : The sizes of the request and response of `action-handler-log` is taken into account for
calculating your data usage.
- `event-trigger-log` : The sizes of the request and response of `event-trigger-log` is taken into account for
calculating your data usage. This log is generated when Hasura triggers an external webhook.
- `scheduled-trigger-log` : The sizes of the request and response of the `scheduled-trigger-log` are taken into account
for calculating your data usage. The cost incurred by this depends on the frequency of Scheduled Triggers.


 `http-log` : The data usage is calculated by the request and response sizes of `http-log` . HTTP request size is
dependent on the size of cookies and request headers. Streamlining the response data will help reduce the HTTP
response size and corresponding data usage. Client-side errors like validation, query syntax, and rate-limiting errors
are not accounted for in billing.

 `ws-server` : The volume of data sent and received through a WebSocket connection is considered when calculating your
data usage. WebSocket connections are typically used for subscriptions. You can optimize the amount of data sent via
subscriptions to reduce `ws-server` data usage.

 `action-handler-log` : The sizes of the request and response of `action-handler-log` is taken into account for
calculating your data usage.

 `event-trigger-log` : The sizes of the request and response of `event-trigger-log` is taken into account for
calculating your data usage. This log is generated when Hasura triggers an external webhook.

 `scheduled-trigger-log` : The sizes of the request and response of the `scheduled-trigger-log` are taken into account
for calculating your data usage. The cost incurred by this depends on the frequency of Scheduled Triggers.

These logs are used to calculate your data usage in Hasura Cloud, which is then used for generating monthly invoices.
You can find more information about the pricing for data pass-through[ on our pricing page ](https://hasura.io/pricing/).

### What did you think of this doc?

- [ How do we calculate data usage? ](https://hasura.io/docs/latest/hasura-cloud/account-management/billing/billing-data-calculation/#how-do-we-calculate-data-usage)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)