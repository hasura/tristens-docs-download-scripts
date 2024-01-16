# Troubleshooting Hasura GraphQL Engine Errors

## Introduction​

This section provides references that can help in troubleshooting errors when developing with Hasura.

## Logs​

In order to find out about the origins of an error, it can be helpful to check the logs.

Metrics and distributed tracing in Hasura Cloud

Hasura Cloud includes metrics and distributed tracing which makes troubleshooting faster. For more information, see[ Metrics ](https://hasura.io/docs/latest/observability/overview/)and[ Tracing ](https://hasura.io/docs/latest/observability/cloud-monitoring/tracing/)in Hasura Cloud.

### Server logs​

For errors that come from the Hasura server, server logs will give you more insights. For details on how you can access
these logs, as well as different log types, visit[ this page ](https://hasura.io/docs/latest/deployment/logging/).

### Console logs​

Should there be any error coming from the Hasura Console UI, they will show up in the Browser dev tools.

### Remote service logs​

Errors can come from a remote service, such as[ Remote Schemas ](https://hasura.io/docs/latest/remote-schemas/overview/),[ Events ](https://hasura.io/docs/latest/event-triggers/overview/)or[ Actions ](https://hasura.io/docs/latest/actions/overview/). In this case, check the errors of the
respective remote service. For Actions, check out this[ debugging page ](https://hasura.io/docs/latest/actions/debugging/).

## GitHub issues​

It's possible that someone with the same problem has created a GitHub issue on the[ Hasura repo ](https://github.com/hasura/graphql-engine/issues). If you don't come across an issue with solution in your
search, feel free to create a[ new issue ](https://github.com/hasura/graphql-engine/issues/new).

## Hasura blog​

The[ Hasura blog ](https://hasura.io/blog/)contains a lot of useful resources including tutorials. You can use the
search functionality to find what you're looking for.

YouTube

If you prefer to watch tutorials in the form of videos, check out the[ Hasura Youtube channel ](https://www.youtube.com/channel/UCZo1ciR8pZvdD3Wxp9aSNhQ).

## Database docs​

If you come across a database error, it will be helpful to check their logs:

- [ Postgres documentation ](https://www.postgresql.org/docs/current/index.html).


## Client-side​

### SSL certificate errors​

SSL certificate errors occur when a web browser can't verify the SSL certificate installed on a site. For SSL errors
such as:

```
ERROR:
{
code: EPROTO,
errno: EPROTO,
message:
request to <graphql-api> failed, reason: write EPROTO <....> alert handshake failure:..<...>: SSL alert number 40
}
```

Follow the steps below to try and resolve the issue:

1. Whitelist the EPROTO error code (in client-side code).
2. Allow the retry logic to be activated.
3. Monitor the system for improvements or changes in the reconciliation process.


## Discord​

If you didn't find a solution in any of the above mentioned sections or if you prefer to troubleshoot with the
community, feel free to join our[ Discord server ](https://hasura.io/discord). Other users might have come across the
same issues, and the Hasura community on Discord is very active and helpful.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/troubleshooting/index/#introduction)
- [ Logs ](https://hasura.io/docs/latest/troubleshooting/index/#logs)
    - [ Server logs ](https://hasura.io/docs/latest/troubleshooting/index/#server-logs)

- [ Console logs ](https://hasura.io/docs/latest/troubleshooting/index/#console-logs)

- [ Remote service logs ](https://hasura.io/docs/latest/troubleshooting/index/#remote-service-logs)
- [ GitHub issues ](https://hasura.io/docs/latest/troubleshooting/index/#github-issues)
- [ Hasura blog ](https://hasura.io/docs/latest/troubleshooting/index/#hasura-blog)
- [ Database docs ](https://hasura.io/docs/latest/troubleshooting/index/#database-docs)
- [ Client-side ](https://hasura.io/docs/latest/troubleshooting/index/#client-side)
    - [ SSL certificate errors ](https://hasura.io/docs/latest/troubleshooting/index/#ssl-certificate-errors)
- [ Discord ](https://hasura.io/docs/latest/troubleshooting/index/#discord)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)