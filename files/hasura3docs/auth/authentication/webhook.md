# Authentication Using a Webhook

## Introduction​

You can configure the Hasura Engine to use webhook mode in order to authenticate incoming requests.

This process of using webhook mode for authentication with Hasura requires specifying a URL - which Hasura calls with
the original request headers - that then returns a body containing the user information in session variables.

Image: [ Authentication using webhooks ](https://hasura.io/docs/3.0/assets/images/auth-webhook-overview-diagram-2cb0cf5d72dc6ecebd9dc4610a15e99c.png)

The webhook service will use your request headers to determine the auth status of the user and return the user role and
any other information as session variables in the response body.

## Configuring webhook mode​

You can configure Hasura to run in webhook mode by running the GraphQL Engine by adding an object endpoint to your
metadata.

### Example​

```
---
kind :  AuthConfig
version :  v1
definition :
   allowRoleEmulationBy :  admin
   webhook :
     webhookUrl :  http : //auth.yourservice.com/validate - request
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `webhookUrl`  | URL | true | URL of the authentication webhook. |
|  `mode`  | String | false | HTTP method to use while making the request to the authentication webhook. Only `Get` and `Post` methods are supported (default: `Get` ). |


Note

If you are running Hasura using Docker, ensure that the Hasura Docker container can reach the webhook.

## Spec for webhook requests​

### GET request Example​

```
GET   https://<your-custom-webhook-url>/   HTTP/1.1
<Header-Key>: <Header-Value>
```

If you configure your webhook to use `Get` , then Hasura **will forward all client headers except** :

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

 `Post` requests will receive **all the client headers** . Given a request like:

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
   }
}
```

Invalid requests

If an invalid JSON request is sent, then the request body is not forwarded to the webhook

## Spec for webhook responses​

### Success​

To allow the GraphQL request to go through, your webhook must return a `200` status code.

You will, at least, need to set the `x-hasura-role` session variable to let the Hasura Engine know which role to use for
this request. Unlike JWT auth mode, you do not have to pass `x-hasura-allowed-roles` or `x-hasura-default-role` session
variables. This is because the webhook is called for each request, allowing the auth service to easily switch the user
role if needed.

In the example below the `x-hasura-is-owner` and `x-hasura-custom` are examples of custom session variables which
will be available to your permission rules in Hasura Engine.

```
HTTP/1.1   200   OK
Content-Type :   application/json
{
     "x-hasura-user-id" :   "25" ,
     "X-hasura-role" :   "user" ,
     "X-hasura-is-owner" :   "true" ,
     "X-hasura-custom" :   "custom value"
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

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/auth/authentication/webhook/#introduction)
- [ Configuring webhook mode ](https://hasura.io/docs/3.0/auth/authentication/webhook/#configuring-webhook-mode)
    - [ Example ](https://hasura.io/docs/3.0/auth/authentication/webhook/#example)
- [ Spec for webhook requests ](https://hasura.io/docs/3.0/auth/authentication/webhook/#webhook-request)
    - [ GET request Example ](https://hasura.io/docs/3.0/auth/authentication/webhook/#get-request-example)
- [ Spec for webhook responses ](https://hasura.io/docs/3.0/auth/authentication/webhook/#webhook-response)
    - [ Success ](https://hasura.io/docs/3.0/auth/authentication/webhook/#success)

- [ Auth denial ](https://hasura.io/docs/3.0/auth/authentication/webhook/#auth-denial)
