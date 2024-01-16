# Action Handlers

## Introduction​

Actions need to be backed by custom business logic. This business logic can be defined in a handler which is an HTTP
webhook.

## HTTP handler​

When the action is executed i.e. when the query or the mutation is called, Hasura makes a `POST` request to the handler
with the action arguments and the session variables.

The request payload is of the format:

```
{
   "action" :   {
     "name" :   "<action-name>"
   } ,
   "input" :   {
     "arg1" :   "<value>" ,
     "arg2" :   "<value>"
   } ,
   "session_variables" :   {
     "x-hasura-user-id" :   "<session-user-id>" ,
     "x-hasura-role" :   "<session-user-role>"
   } ,
   "request_query" :   "<request-query>"
}
```

Note

All `session_variables` in the request payload have lowercase keys.

## Returning a success response​

To return a success response, you must send back a response payload of action's response type. The HTTP status code must
be `2xx` for a successful response.

## Returning an error response​

To return an error response, you must send back an error object. An error object looks like:

```
{
   "message" :   "<mandatory-error-message>" ,
   "extensions" :   "<optional-json-object>"
}
```

where `extensions` is an optional JSON value.

If present, `extensions` should be a JSON object, which may have a status code field `code` , along with other data you
may want to add to your errors:

```
{
   "code" :   "<optional-error-code>" ,
   "optionalField1" :   "<custom-data-here>"
}
```

The HTTP status code must be `4xx` in order to indicate an error response.

For backwards compatibility with previous versions of Hasura, the `code` field may also be supplied at the root of the
error object, i.e. at `$.code` . This will be deprecated in a future release, and providing `code` within `extensions` is
preferred.

## Example​

For example, consider the following mutation.

```
extend   type   Mutation   {
   UserLogin ( username :   String ! ,   password :   String ! ) :   UserInfo
}
type   UserInfo   {
   accessToken :   String !
   userId :   Int !
}
```

Let's say, the following mutation is executed:

```
mutation   {
   UserLogin ( username :   "jake" ,   password :   "secretpassword" )   {
     accessToken
     userId
   }
}
```

Hasura will call the handler with the following payload:

```
{
   "action" :   {
     "name" :   "UserLogin"
   } ,
   "input" :   {
     "username" :   "jake" ,
     "password" :   "secretpassword"
   } ,
   "session_variables" :   {
     "x-hasura-user-id" :   "423" ,
     "x-hasura-role" :   "user"
   } ,
   "request_query" :   "mutation {\n  UserLogin (username: \"jake\", password: \"secretpassword\") {\n    accessToken\n    userId\n  }\n}\n"
}
```

To return a success response, you must send the response of the action's output type (in this case, `UserInfo` ) with a
status code `2xx` . So a sample response would be:

```
{
   "accessToken" :   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVC" ,
   "userId" :   423
}
```

To throw an error, you must send a response of the following type while setting the status code as `4xx` .

```
{
   "message" :   "invalid credentials"
}
```

## Restrict access to your action handler​

You might want to restrict access to your action handler in order to ensure that it can only get called by your Hasura
instance and not by third parties.

### Adding an action secret​

One possible way of restricting access to an action handler is by adding a header to the action that is automatically
sent with each request to the webhook, and then adding a check against that in your action handler.

- [ Step 1: Configure your Hasura instance ](https://hasura.io/docs/latest/actions/action-handlers/#configure-your-hasura-instance)
- [ Step 2: Add a header to your action ](https://hasura.io/docs/latest/actions/action-handlers/#add-a-header-to-your-action)
- [ Step 3: Verify the secret in your action handler ](https://hasura.io/docs/latest/actions/action-handlers/#verify-the-secret-in-your-action-handler)


Note

Adding an action secret is a simple way of restricting access to an action handler and will suffice in most use cases.
However, if you have more profound security requirements, you might want to choose advanced security solutions tailored
to your needs.

#### Step 1: Configure your Hasura instance​

In your Hasura server, add the action secret as an environment variable, say `ACTION_SECRET_ENV` .

#### Step 2: Add a header to your action​

For your action, add a header that will act as an action secret.

- Console
- CLI
- API


Head to the `Actions -> [action-name]` tab in the Console and scroll down to `Headers` . You can now configure an action
secret by adding a header:

Image: [ Console action secret ](data:image/png;base64,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)

Then hit `Save` .

Go to `metadata/actions.yaml` in the Hasura Project directory.

Update the definition of your action by adding the action secret as a header:

```
-  actions
   -   name :  actionName
     definition :
        kind :  synchronous
        handler :  http : //localhost : 3000
        forward_client_headers :   true
        headers :
          -   name :  ACTION_SECRET
            value_from_env :  ACTION_SECRET_ENV
```

Save the changes and run `hasura metadata apply` to set the headers.

Headers can be set when[ creating ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action)or[ updating ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-update-action)an action via the Metadata API.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "create_action" ,
   "args" :   {
     "name" :   "addNumbers" ,
     "definition" :   {
       "kind" :   "synchronous" ,
       "type" :   "query" ,
       "headers" :   [
         {
           "name" :   "ACTION_SECRET" ,
           "value_from_env" :   "ACTION_SECRET_ENV"
         }
       ] ,
       "arguments" :   [
         {
           "name" :   "numbers" ,
           "type" :   "[Int]!"
         }
       ] ,
       "output_type" :   "AddResult" ,
       "handler" :   "https://hasura-actions-demo.glitch.me/addNumbers"
     }
   }
}
```

Note

Before creating an action via the[ create_action Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action), all custom types need to
be defined via the[ set_custom_types ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-types/#metadata-set-custom-types)Metadata
API.

This secret is only known by Hasura and is passed to your endpoint with every call, thus making sure only Hasura can
successfully authenticate with the action handler.

Note

The name for the action secret is not defined by Hasura and can be chosen freely.

#### Step 3: Verify the secret in your action handler​

First, load the action secret as an environment variable in your action handler by adding it to your `.env` file (this
file might be a different one depending on your framework).

Second, you need to write some code in your action handler to check that the action secret passed as a header equals to
the one you stored as an environment variable.

The following is an example of a simple authorization middleware with Express which can be included before the request
handler logic:

```
// use authorization for all routes
app . use ( authorizationMiddleware ) ;
// authorize action call
function   authorizationMiddleware ( req ,  res ,  next )   {
   if   ( correctSecretProvided ( req ) )   next ( ) ;
   else  res . sendStatus ( 403 ) ;
}
// check if the secret sent in the header equals to the secret stored as an env variable
function   correctSecretProvided ( req )   {
   const  requiredSecret  =  process . env . ACTION_SECRET_ENV ;
   const  providedSecret  =  req . headers [ 'ACTION_SECRET' ] ;
   return  requiredSecret  ===  providedSecret ;
}
// Request handler
app . post ( '/actionHandler' ,   async   ( req ,  res )   =>   {
   // handler logic
} ) ;
```

Additional Resources

Introduction to Hasura Actions -[ View Recording ](https://hasura.io/events/webinar/hasura-actions/?pg=docs&plcmt=body&cta=view-recording&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/actions/action-handlers/#introduction)
- [ HTTP handler ](https://hasura.io/docs/latest/actions/action-handlers/#http-handler)
- [ Returning a success response ](https://hasura.io/docs/latest/actions/action-handlers/#returning-a-success-response)
- [ Returning an error response ](https://hasura.io/docs/latest/actions/action-handlers/#returning-an-error-response)
- [ Example ](https://hasura.io/docs/latest/actions/action-handlers/#example)
- [ Restrict access to your action handler ](https://hasura.io/docs/latest/actions/action-handlers/#securing-action-handlers)
    - [ Adding an action secret ](https://hasura.io/docs/latest/actions/action-handlers/#adding-an-action-secret)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)