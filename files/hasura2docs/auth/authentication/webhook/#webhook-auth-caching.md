# Authentication Using a Webhook

## Introduction​

You can configure the Hasura Engine to use webhook mode in order to authenticate incoming requests.

This process of using webhook mode for authentication with Hasura requires specifying a URL - which Hasura calls with
the original request headers - that then returns a body containing the user information in session variables.

Image: [ Authentication using webhooks ](https://hasura.io/docs/assets/images/auth-webhook-overview-b29e5afc166191c7369055f0d1574e35.png)

The webhook service will use your request headers to determine the auth status of the user and return the user role and
any other information as session variables in the response body.

Prerequisite

It is mandatory to first[ secure your GraphQL endpoint ](https://hasura.io/docs/latest/deployment/securing-graphql-endpoint/)for the webhook mode
to take effect.

## Configuring webhook mode​

- You can configure Hasura to run in webhook mode by running the GraphQL Engine with the `--auth-hook` flag or the `HASURA_GRAPHQL_AUTH_HOOK` environment variable (see[ GraphQL Engine server options ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/)), the value of which is the webhook
endpoint.
- You can configure Hasura to send either a `GET` or a `POST` request to your auth webhook. The default configuration is `GET` and you can override this with `POST` by using the `--auth-hook-mode` flag or the `HASURA_GRAPHQL_AUTH_HOOK_MODE` environment variable ( *in addition to those specified above; see* [ GraphQL Engine server options ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/)).


Note

If you are running Hasura using Docker, ensure that the Hasura Docker container can reach the webhook. See[ this page ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-networking)for Docker networking.

Note

The configured webhook is **ignored** when the `X-Hasura-Admin-Secret` header is found in the request and admin access
is granted.

## Spec for webhook requests​

### GET request Example​

```
GET   https://<your-custom-webhook-url>/   HTTP/1.1
<Header-Key>: <Header-Value>
```

If you configure your webhook to use `GET` , then Hasura **will forward all client headers except** :

- `Content-Length`
- `Content-Type`
- `Content-MD5`
- `User-Agent`
- `Host`
- `Origin`
- `Referer`
- `Accept`
- `Accept-Encoding`
- `Accept-Language`
- `Accept-Datetime`
- `Cache-Control`
- `Connection`
- `DNT`


#### POST request Example​

 `POST` requests will receive the contents of the request body in addition to **all client headers** . Given a request
like:

```
query   UserQuery ( $a :   Int )   {
   users ( where :   {   id :   {   _eq :   $a   }   } )   {
     id
   }
}
```

with variables `{"a": 1}` , the webhook will receive a request in the following form:

```
POST   https://<your-custom-webhook>/   HTTP/1.1
Content-Type :   application/json
{
   "headers" :   {
     "header-key1" :   "header-value1" ,
     "header-key2" :   "header-value2"
   } ,
   "request" :   {
     "variables" :   {
       "a" :   1
     } ,
     "operationName" :   "UserQuery" ,
     "query" :   "query UserQuery($a:  Int) {\n  users(where:  {id:  {_eq:  $a}}){\n    id\n  }\n}\n"
   }
}
```

Invalid requests

If an invalid JSON request is sent, then the request body is not forwarded to the webhook

## Spec for webhook responses​

### Success​

To allow the GraphQL request to go through, your webhook must return a `200` status code. You should respond with
session variables beginning with `X-Hasura-*` in the body of your response. These will be available to your permission
rules in Hasura Engine.

You will, at least, need to set the `X-Hasura-Role` session variable to let the Hasura Engine know which role to use for
this request. Unlike JWT auth mode, you do not have to pass `X-Hasura-Allowed-Roles` or `X-Hasura-Default-Role` session
variables. This is because the webhook is called for each request, allowing the auth service to easily switch the user
role if needed.

In the example below the `X-Hasura-Is-Owner` and `X-Hasura-Custom` are examples of custom session variables which
will be available to your permission rules in Hasura Engine.

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "X-Hasura-User-Id" :   "25" ,
     "X-Hasura-Role" :   "user" ,
     "X-Hasura-Is-Owner" :   "true" ,
     "X-Hasura-Custom" :   "custom value"
}
```

Value types

All values should be `String` . They will be converted to the right type automatically upon receipt.

Set-Cookie headers

If `Set-Cookie` HTTP headers are set by the auth webhook, they are forwarded by Hasura Engine as response headers for
both GET/POST request methods.

### Auth denial​

If you want to deny the GraphQL request, return a `401 Unauthorized` exception.

`HTTP/1.1   401   Unauthorized`

### Unauthorized role​

In order to use the defined[ unauthorized (anonymous or public) role ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/),
the webhook should respond with a `200` status code and specify the `X-Hasura-Role` session variable with the name of
the unauthorized role. Eg:

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "X-Hasura-Role" :   "anonymous" ,
}
```

Only 200 or 401 responses are accepted

Anything other than a `200` or `401` response from webhook will make Hasura Engine raise a `500 Internal Server Error` exception.

## Refreshing Websocket Connections​

There is no default timeout on an authorized websocket connection (for[ live queries ](https://hasura.io/docs/latest/subscriptions/postgres/livequery/index/)or[ streaming subscriptions ](https://hasura.io/docs/latest/subscriptions/postgres/streaming/index/)) and you can optionally add one. To do so, you
need to return either:

- a `Cache-Control` variable, modeled on the[ Cache-Control HTTP Header ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control), to specify a **relative** expiration time, in seconds.


```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "X-Hasura-User-Id" :   "26" ,
     "X-Hasura-Role" :   "user" ,
     "X-Hasura-Is-Owner" :   "false" ,
     "Cache-Control" :   "max-age=600"
}
```

- an `Expires` variable, modeled on the[ Expires HTTP Header ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expires), to specify an **absolute** expiration time. The expected format is `"%a, %d %b %Y %T GMT"` .


```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "X-Hasura-User-Id" :   "27" ,
     "X-Hasura-Role" :   "user" ,
     "X-Hasura-Is-Owner" :   "false" ,
     "Expires" :   "Mon, 30 Mar 2020 13:25:18 GMT"
}
```

Websocket timeouts

For websockets, if the `Cache-Control` or `Expires` fields are present in the response then a new request to the
auth-webhook is made after the time specified in those fields and a new websocket connection is established.

## Webhook Auth Caching​

Session variables from a webhook token can be cached to improve the performance of the request.

Note

- This feature is available for version `v2.22.0` and higher.
- Webhook auth caching is available on Hasura Cloud without any configuration.
- For self-hosted EE, it requires a[ Redis instance
to be configured ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#redis-url). If the Redis instance is not configured or
inaccessible, then the request will skip the cache.


For caching, you need to return either:

- a `Cache-Control` variable, modeled on the[ Cache-Control HTTP Header ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control), to specify a **relative** expiration time, in seconds.


```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "X-Hasura-User-Id" :   "26" ,
     "X-Hasura-Role" :   "user" ,
     "X-Hasura-Is-Owner" :   "false" ,
     "Cache-Control" :   "max-age=60"
}
```

- an `Expires` variable, modeled on the[ Expires HTTP Header ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expires), to specify an **absolute** expiration time. The expected format is `"%a, %d %b %Y %T GMT"` .


```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "X-Hasura-User-Id" :   "27" ,
     "X-Hasura-Role" :   "user" ,
     "X-Hasura-Is-Owner" :   "false" ,
     "Expires" :   "Mon, 30 Mar 2020 13:25:18 GMT"
}
```

Tip

The cache key is based on the information that is sent to the auth webhook, namely the following:

- Client headers
- Graphql request


Note that the cache key will change if the GraphQL request changes even if the client headers are same. If you want to
cache auth token based on client headers only, you should disable sending GraphQL request to the auth webhook using[ Send Request Body to Auth Hook ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#send-request-body-to-auth-hook)server
configuration.

## Webhook with the WebSocket protocol​

When executing a subscription (or query or mutation) over the WebSocket protocol, the authentication step is executed on `connection_init` when the websocket is connected to Hasura GraphQL Engine and is valid until the expiry as per the `expires` header set on the webhook response, when in webhook mode.

Once authenticated, all operations are allowed without further check, until the authentication expires.

## Auth webhook samples​

We have put together a[ GitHub Node.js repo ](https://github.com/hasura/graphql-engine/tree/master/community/boilerplates/auth-webhooks/nodejs-express)that has some sample auth webhooks configured.

You can deploy these samples using[ glitch ](https://glitch.com/):

[  ](http://glitch.com/edit/#!/import/github/hasura/sample-auth-webhook)

Image: [ deploy_auth_webhook_with_glitch ](https://raw.githubusercontent.com/hasura/sample-auth-webhook/master/assets/deploy-glitch.png)

Once deployed, you can use any of the following endpoints as your auth webhook in the GraphQL Engine:

- `/simple/webhook` ([ View source ](https://github.com/hasura/graphql-engine/blob/master/community/boilerplates/auth-webhooks/nodejs-express/server.js))
- `/firebase/webhook` ([ View source ](https://github.com/hasura/graphql-engine/blob/master/community/boilerplates/auth-webhooks/nodejs-firebase/firebase/firebaseHandler.js))


Firebase environment variables

If you are using `Firebase` , you will need to set the associated environment variables.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#introduction)
- [ Configuring webhook mode ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#configuring-webhook-mode)
- [ Spec for webhook requests ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#webhook-request)
    - [ GET request Example ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#get-request-example)
- [ Spec for webhook responses ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#webhook-response)
    - [ Success ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#success)

- [ Auth denial ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#auth-denial)

- [ Unauthorized role ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#unauthorized-role)
- [ Refreshing Websocket Connections ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#refreshing-websocket-connections)
- [ Webhook Auth Caching ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#webhook-auth-caching)
- [ Webhook with the WebSocket protocol ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#webhook-with-the-websocket-protocol)
- [ Auth webhook samples ](https://hasura.io/docs/latest/auth/authentication/webhook/#webhook-auth-caching/#auth-webhook-samples)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)