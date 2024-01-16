# Forwarding Auth Context to/from Remote Schemas

## Introduction​

This page gives an overview of how Hasura allows you to pass auth context to your Remote Schema server.

## Passing headers from Hasura to your Remote Schema​

Hasura will forward the resolved `x-hasura-*` values as headers to your Remote Schema. You can use this information to apply authorization rules in your server. You don't have to redo authentication in your Remote Schema server.

You can also configure Hasura to have (as shown[ here ](https://hasura.io/docs/latest/remote-schemas/adding-schema/#merge-remote-schema)):

1. static header values that are sent to the remote server
2. forward all headers from the client (like `Authorization` , `Cookie` headers etc.)
3. [ Fine grained access control ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-permissions/)


In case there are multiple headers with same name, the order of precedence is: configuration headers>resolved user ( `x-hasura-*` ) variables>client headers.

So for example, if the client sends an `Authorization` header, and the configuration also has an `Authorization` header, the configuration header value will selected.

Note

The headers from the client behave similarly to the authorization system. If `x-hasura-admin-secret` is sent, then all `x-hasura-*` values from the client are respected, otherwise they are ignored.

## Passing cookie headers from your Remote Schema to the client​

 `Set-Cookie` headers from your Remote Schema servers are sent back to the client over HTTP transport. **Over websocket transport there exists no means of sending headers after a query/mutation and hence the "Set-Cookie" headers are not sent to the client.** Use HTTP transport if your remote servers set cookies.

Additional Resources

Data Federation with Hasura -[ Watch Webinar ](https://hasura.io/events/webinar/data-federation-hasura-graphql/?pg=docs&plcmt=body&cta=watch-webinar&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-forward-auth/#introduction)
- [ Passing headers from Hasura to your Remote Schema ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-forward-auth/#passing-headers-from-hasura-to-your-remote-schema)
- [ Passing cookie headers from your Remote Schema to the client ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-forward-auth/#passing-cookie-headers-from-your-remote-schema-to-the-client)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)