# REST Connectors for Actions

## Introduction​

REST Connectors for Actions are used to integrate existing REST APIs to the GraphQL API without needing any middleware
or modifications to the upstream code.

REST Connectors modify the default HTTP request made by an action to adapt to your webhook's expected format by adding
suitable transforms.

Note

General information about the templating used in REST Connectors can be found in the[ Kriti templating ](https://hasura.io/docs/latest/api-reference/kriti-templating/)section of the documentation.

Supported from

REST Connectors are supported in Hasura GraphQL Engine versions `v2.1.0` and above

## Configuring REST Connectors​

REST Connectors can be configured either when creating a new action or editing an existing one. See the transform
options[ here ](https://hasura.io/docs/latest/actions/rest-connectors/#action-transform-types):

- Console
- CLI
- API


Go to the `Actions` tab on the Console and create or modify an action. Scroll down to `Configure REST Connectors` section:

Image: [ Configure REST connectors for Actions ](https://hasura.io/docs/assets/images/configure-rest-connectors-5776e56a7742b27994184357bffeb9b2.png)

Update the `actions.yaml` file inside the `metadata` directory and add a [request_transform](RequestTransformation]
field to the action:

```
-   name :  create_user
   definition :
     kind :  synchronous
     handler :  https : //action.my_app.com/create - user
     timeout :   60
     request_transform :
       template_engine :  Kriti
       method :  POST
       content_type :  application/json
       url :   '{{$base_url}}/create_user'
       query_params :
         id :   "{{$session_variables['x-hasura-user-id']}}"
       body :   '{"username": {{$body.input.username}}}'
   comment :  Custom action to create user
```

Apply the Metadata by running:

`hasura metadata apply`

REST Connectors can be configured for Actions using the[ create_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action)or[ update_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-update-action)Metadata APIs by adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to
the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "create_action" ,
   "args" : {
       "name" : "create_user" ,
       "definition" : {
         "kind" : "synchronous" ,
         "arguments" : [
             {
               "name" : "username" ,
               "type" : "String!"
             } ,
             {
               "name" : "email" ,
               "type" : "String!"
             }
         ] ,
         "output_type" : "User" ,
         "handler" : "https://action.my_app.com/create-user" ,
         "timeout" : 60 ,
         "request_transform" :   {
           "template_engine" :   "Kriti" ,
           "method" :   "POST" ,
           "url" :   "{{$base_url}}/create_user" ,
           "query_params" :   {
             "id" :   "{{$session_variables['x-hasura-user-id']}}"
           } ,
           "content_type" :   "application/json" ,
           "body" :   "{\"username\": {{$body.input.username}}}"
         }
       } ,
     "comment" :   "Custom action to create user"
   }
}
```

### Context Variables​

You can use context variables in the transforms to achieve dynamic behavior for each request.

The context variables available in transforms are:

| Context variable | Value |
|---|---|
| $body | Original body of action request |
| $base_url | Original configured webhook handler URL |
| $session_variables | Session variables |
| $response.status | HTTP response staus code from the webhook |


In addition to these variables, the following functions are available in addition to the standard[ Basic Functions ](https://hasura.io/docs/latest/api-reference/kriti-templating/#kriti-function-reference):

| Context variable | Value |
|---|---|
|  `getSessionVariable(NAME)`  | Look up a session variable by name (case-insensitive) |


#### Console sample context​

The Console allows you to preview your transforms while configuring them. To avoid exposing sensitive information on the
console UI the actual environment variables configured on the server are not resolved while displaying the previews.
Also any session variables used in the transform will not be available at the time of configuration.

Hence, the Console allows you to provide mock env variables and session variables to verify your transforms. If you
configure your transforms without providing the mock env/session variables you might see a UI validation error in the
preview sections.

 **For example:** If your webhook handler is set as an env var as shown below then pass a mock value for that env var in
the sample context:

Image: [ Console action webhook handler ](https://hasura.io/docs/assets/images/transform-sample-context-0-82a57db7375894c24d343a0870e15f8e.png)

You can enter the mock env/session variables under `Configure REST Connectors > Sample Context` :

Image: [ Add generic sample context ](https://hasura.io/docs/assets/images/transform-sample-context-1-656f2f69f9e01323d19ef2f619c0295f.png)

Note

As the sample context is only used for previews, you can still configure the transforms on the Console without setting
any sample context.

## Types of transforms​

REST Connectors allow you to add different transforms to the default HTTP request. You can also use[ context variables ](https://hasura.io/docs/latest/actions/rest-connectors/#action-transform-context-variables)in the transforms to achieve dynamic behavior for each request.

You can transform your:

- [ Request Method ](https://hasura.io/docs/latest/actions/rest-connectors/#request-method)
- [ Request URL ](https://hasura.io/docs/latest/actions/rest-connectors/#request-url)
- [ Request Body ](https://hasura.io/docs/latest/actions/rest-connectors/#request-body)
- [ Response Body ](https://hasura.io/docs/latest/actions/rest-connectors/#response-body)


### Request Method​

You can change the request method to adapt to your API's expected format.

- Console
- CLI
- API


In the `Configure REST Connectors` section, click on `Add Request Options Transform` :

Image: [ Change request method ](https://hasura.io/docs/assets/images/transform-method-f76d61dbee34c9f1c77388a6f40fcb70.png)

Update the `actions.yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the action:

```
-   name :  create_user
   definition :
     kind :  synchronous
     handler :  https : //action.my_app.com/create - user
   timeout :   60
   request_transform :
     template_engine :  Kriti
     method :  POST
     content_type :  application/json
     url :   '{{$base_url}}/create_user'
     query_params :
       id :  ' { { $session_variables [ ''x - hasura - user - id'' ] } } '
     body :   '{"username": {{$body.input.username}}}'
comment :  Custom action to create user
```

Apply the Metadata by running:

`hasura metadata apply`

REST Connectors can be configured for Actions using the[ create_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action)or[ update_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-update-action)Metadata APIs by adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to
the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "create_action" ,
   "args" : {
     "name" : "create_user" ,
     "definition" : {
       "kind" : "synchronous" ,
       "arguments" : [
         {
           "name" : "username" ,
           "type" : "String!"
         } ,
         {
           "name" : "email" ,
           "type" : "String!"
         }
       ] ,
       "output_type" : "User" ,
       "handler" : "{{ACTION_BASE_URL}}" ,
       "timeout" : 60 ,
       "request_transform" :   {
         "template_engine" :   "Kriti" ,
         "method" :   "POST" ,
         "url" :   "{{$base_url}}/create_user" ,
         "query_params" :   {
           "id" :   "{{$session_variables['x-hasura-user-id']}}"
         } ,
         "content_type" :   "application/json" ,
         "body" :   "{\"username\": {{$body.input.username}}}"
       }
     } ,
     "comment" :   "Custom action to create user"
   }
}
```

### Request URL​

The Request URL template allows you to configure the exact API endpoint to call.

You can use the[ context variables ](https://hasura.io/docs/latest/actions/rest-connectors/#action-transform-context-variables)to construct the final URL.

- [ Request URL with Query Parmeters (as key-value pairs) ](https://hasura.io/docs/latest/actions/rest-connectors/#request-url-with-query-parmeters-as-key-value-pairs)
- [ Request URL with Query Parmeters (as raw string) ](https://hasura.io/docs/latest/actions/rest-connectors/#request-url-with-query-parmeters-as-raw-string)


##### Request URL with Query Parmeters (as key-value pairs)​

You can provide `Key-Value` type query params to add to the URL.

You can also use the[ Kriti templating language ](https://hasura.io/docs/latest/api-reference/kriti-templating/)to construct any string values here.

- Console
- CLI
- API


In the `Configure REST Connectors` section, click on `Add Request Options Transform` :

Image: [ Change request URL ](https://hasura.io/docs/assets/images/transform-key-value-url-db8fce60c49d2708f36d895ef66d9988.png)

The value of the final url should be reflected in the `Preview` section given all required[ sample context ](https://hasura.io/docs/latest/actions/rest-connectors/#action-transforms-sample-context)is set.

Hit `Save Action` to apply your changes.

Update the `actions.yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the action:

```
-   name :  create_user
   definition :
     kind :  synchronous
     handler :  https : //action.my_app.com/create - user
   timeout :   60
   request_transform :
     template_engine :  Kriti
     method :  POST
     content_type :  application/json
     url :   '{{$base_url}}/create_user'
     query_params :
       id :  ' { { $session_variables [ ''x - hasura - user - id'' ] } } '
     body :   '{"username": {{$body.input.username}}}'
comment :  Custom action to create user
```

Apply the Metadata by running:

`hasura metadata apply`

REST Connectors can be configured for Actions using the[ create_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action)or[ update_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-update-action)Metadata APIs by adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to
the args:

```
POST /v1/metadata HTTP/1.1
Content-Type: application/json
X-Hasura-Role: admin
{
  "type":"create_action",
  "args":{
    "name":"create_user",
    "definition":{
      "kind":"synchronous",
      "arguments":[
        {
          "name":"username",
          "type":"String!"
        },
        {
          "name":"email",
          "type":"String!"
        }
      ],
      "output_type":"User",
      "handler":"{{ACTION_BASE_URL}}",
      "timeout":60,
      "request_transform": {
        "template_engine": "Kriti",
        "method": "POST",
        "url": "{{$base_url}}/create_user",
        "query_params": {
          "id": "{{$session_variables['x-hasura-user-id']}}"
        },
        "content_type": "application/json",
        "body": "{\"username\": {{$body.input.username}}}"
      }
    },
    "comment": "Custom action to create user"
  }
}
```

##### Request URL with Query Parmeters (as raw string)​

You can provide `string` type query params to add to the URL.

You can also use the[ Kriti templating language ](https://hasura.io/docs/latest/api-reference/kriti-templating/)to construct any string values here.

- Console
- CLI
- API


In the `Configure REST Connectors` section, click on `Add Request Options Transform` :

Image: [ Change request URL ](https://hasura.io/docs/assets/images/transform-url-string-url-5836ae620a2cc0051f8fc3d386a39657.png)

The value of the final url should be reflected in the `Preview` section given all required[ sample context ](https://hasura.io/docs/latest/actions/rest-connectors/#action-transforms-sample-context)is set.

Hit `Save Action` to apply your changes.

Update the `actions.yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the action:

```
-   name :  create_user
   definition :
     kind :  synchronous
     handler :  https : //action.my_app.com/create - user
   timeout :   60
   request_transform :
     template_engine :  Kriti
     method :  POST
     content_type :  application/json
     url :   '{{$base_url}}/create_user'
     query_params :  " { { concat( [ "userId=" ,  $session_variables [ "x-hasura-user-id" ] ] ) } } "
     body :   '{"username": {{$body.input.username}}}'
comment :  Custom action to create user
```

Apply the Metadata by running:

`hasura metadata apply`

REST Connectors can be configured for Actions using the[ create_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action)or[ update_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-update-action)Metadata APIs by adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to
the args:

```
POST /v1/metadata HTTP/1.1
Content-Type: application/json
X-Hasura-Role: admin
{
  "type":"create_action",
  "args":{
    "name":"create_user",
    "definition":{
      "kind":"synchronous",
      "arguments":[
        {
          "name":"username",
          "type":"String!"
        },
        {
          "name":"email",
          "type":"String!"
        }
      ],
      "output_type":"User",
      "handler":"{{ACTION_BASE_URL}}",
      "timeout":60,
      "request_transform": {
        "template_engine": "Kriti",
        "method": "POST",
        "url": "{{$base_url}}/create_user",
        "query_params": "{{concat(["userId=", $session_variables["x-hasura-user-id"]])}}"
        "content_type": "application/json",
        "body": "{\"username\": {{$body.input.username}}}"
      }
    },
    "comment": "Custom action to create user"
  }
}
```

escapeUri

Note that you must use the `escapeUri` function to urlencode templated values. For example, if you have to use session
variables in the URL and those may contain non-ASCII values, then you should provide the template URL as `{{$base_url}}/{{escapeUri($session_variables['x-hasura-user-id'])}}` 

Optional query params

Query params with key/value pairs which evaluate to `null` are ignored by Hasura while performing the HTTP API call.
Hasura considers such query params optional.

For example, consider a query param value with template `{{$session_variables?['x-hasura-user-id']}}` . If the variable `x-hasura-user-id` is absent in the session variables, then the query param will be omitted from the HTTP API call.

### Request Body​

You can generate a custom request body by configuring a template to transform the default payload to a custom payload.
Request body could be provided using the `body` field as an[ object ](https://hasura.io/docs/latest/api-reference/syntax-defs/#bodytransform),
which additionally gives the ability to disable request body, transform request body to `application/json` , or transform
request body to `x_www_form_urlencoded` formats.

- [ Disabling Request Body ](https://hasura.io/docs/latest/actions/rest-connectors/#disabling-request-body)
- [ Request Body with application/json format ](https://hasura.io/docs/latest/actions/rest-connectors/#request-body-with-applicationjson-format)
- [ Request Body with x_www_form_urlencoded format ](https://hasura.io/docs/latest/actions/rest-connectors/#request-body-with-x_www_form_urlencoded-format)


##### Disabling Request Body​

If you are using a `GET` request, you might want to not send any request body, and additionally not send a `content-type` header to the webhook. You can do that using the disable body feature.

- Console
- CLI
- API


In the `Configure REST Connectors` section, click on `Add Request Options Transform` , and convert the `Request Method` as `GET` .
Then click on `Add Payload Transform` , disable the payload body by using the dropdown next to the `Configure Request Body` section.

Image: [ Disable payload body ](https://hasura.io/docs/assets/images/transform-body-disable-32084e1b4825aa836a9420ebd4178c17.png)

Hit `Save Action` to apply your changes.

Update the `actions.yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the action:

```
-   name :  create_user
   definition :
     kind :  synchronous
     handler :  https : //action.my_app.com/create - user
   timeout :   60
   request_transform :
     template_engine :  Kriti
     version :   2
     method :  GET
     url :   '{{$base_url}}/create_user'
     query_params :
       id :  ' { { $session_variables [ ''x - hasura - user - id'' ] } } '
     body :
       action :   'remove'
     request_headers :
       remove_headers :   [ 'content - type ]
comment :  Custom action to create user
```

Apply the Metadata by running:

`hasura metadata apply`

REST Connectors can be configured for Actions using the[ create_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action)or[ update_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-update-action)Metadata APIs by adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to
the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "create_action" ,
   "args" : {
     "name" : "create_user" ,
     "definition" : {
       "kind" : "synchronous" ,
       "arguments" : [
         {
           "name" : "username" ,
           "type" : "String!"
         } ,
         {
           "name" : "email" ,
           "type" : "String!"
         }
       ] ,
       "output_type" : "User" ,
       "handler" : "{{ACTION_BASE_URL}}" ,
       "timeout" : 60 ,
       "request_transform" :   {
         "template_engine" :   "Kriti" ,
         "version" :   2 ,
         "method" :   "GET" ,
         "url" :   "{{$base_url}}/create_user" ,
         "query_params" :   {
           "id" :   "{{$session_variables['x-hasura-user-id']}}"
         } ,
         "body" :   {
           "action" :   "remove"
         } ,
         "request_headers" :   {
           "remove_headers" :   [ "content-type" ] ,
         } ,
       }
     } ,
     "comment" :   "Custom action to create user"
   }
}
```

##### Request Body with application/json format​

You can transform Request Body to `application/json` format using the following steps:

- Console
- CLI
- API


In the `Configure REST Connectors` section, click on `Add Payload Transform` . By default, the Console sends the body as `application/json` which can be seen in the dropdown next to the `Configure Request Body` section.

Image: [ payload body application/json ](https://hasura.io/docs/assets/images/transform-body-application-json-36d099304fbf6211d01d158e217af3b2.png)

Hit `Save Action` to apply your changes.

Update the `actions.yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the action:

```
-   name :  create_user
   definition :
     kind :  synchronous
     handler :  https : //action.my_app.com/create - user
   timeout :   60
   request_transform :
     template_engine :  Kriti
     version :   2
     method :  POST
     url :   '{{$base_url}}/create_user'
     query_params :
       id :  ' { { $session_variables [ ''x - hasura - user - id'' ] } } '
     body :
       action :   'transform'
       template :   '{"username": {{$body.input.username}}}'
comment :  Custom action to create user
```

Apply the Metadata by running:

`hasura metadata apply`

REST Connectors can be configured for Actions using the[ create_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action)or[ update_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-update-action)Metadata APIs by adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to
the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "create_action" ,
   "args" : {
     "name" : "create_user" ,
     "definition" : {
       "kind" : "synchronous" ,
       "arguments" : [
         {
           "name" : "username" ,
           "type" : "String!"
         } ,
         {
           "name" : "email" ,
           "type" : "String!"
         }
       ] ,
       "output_type" : "User" ,
       "handler" : "{{ACTION_BASE_URL}}" ,
       "timeout" : 60 ,
       "request_transform" :   {
         "template_engine" :   "Kriti" ,
         "version" :   2 ,
         "method" :   "POST" ,
         "url" :   "{{$base_url}}/create_user" ,
         "query_params" :   {
           "id" :   "{{$session_variables['x-hasura-user-id']}}"
         } ,
         "body" :   {
           "action" :   "transform"
           "template" :   "{\"username\": {{$body.input.username}}}"
         } ,
       }
     } ,
     "comment" :   "Custom action to create user"
   }
}
```

##### Request Body with x_www_form_urlencoded format​

While doing `x_www_form_urlencoded` transformation, please note that as all changes to the request must be made explicit
when calling the API, so you will need to remove the default `application/json` header and add a `application/x-www-form-urlencoded` header.

- Console
- CLI
- API


In the `Configure REST Connectors` section, click on `Add Payload Transform` . Change the dropdown next to `Configure Request Body` section to `x_www_form_urlencoded` . You can see the body transformed body in the `Transformed Request Body` section.

Image: [ payload body x_www_form_urlencoded ](https://hasura.io/docs/assets/images/transform-body-xurl-formencoded-1dc338fb1e48325f11d74551b461d338.png)

Hit `Save Action` to apply your changes.

Update the `actions.yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the action:

```
-   name :  create_user
   definition :
     kind :  synchronous
     handler :  https : //action.my_app.com/create - user
   timeout :   60
   request_transform :
     template_engine :  Kriti
     version :   2
     method :  POST
     url :   '{{$base_url}}/create_user'
     query_params :
       id :  ' { { $session_variables [ ''x - hasura - user - id'' ] } } '
     body :
       action :   'x_www_form_urlencoded'
       form_template :
         username :   '{{$body.input.username}}'
     request_headers :
       remove_headers :   [ 'content-type' ]
       add_headers :
         'content-type' :   'application/x-www-form-urlencoded'
comment :  Custom action to create user
```

Apply the Metadata by running:

`hasura metadata apply`

REST Connectors can be configured for Actions using the[ create_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action)or[ update_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-update-action)Metadata APIs by adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to
the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "create_action" ,
   "args" : {
     "name" : "create_user" ,
     "definition" : {
       "kind" : "synchronous" ,
       "arguments" : [
         {
           "name" : "username" ,
           "type" : "String!"
         } ,
         {
           "name" : "email" ,
           "type" : "String!"
         }
       ] ,
       "output_type" : "User" ,
       "handler" : "{{ACTION_BASE_URL}}" ,
       "timeout" : 60 ,
       "request_transform" :   {
         "template_engine" :   "Kriti" ,
         "version" :   2 ,
         "method" :   "POST" ,
         "url" :   "{{$base_url}}/create_user" ,
         "query_params" :   {
           "id" :   "{{$session_variables['x-hasura-user-id']}}"
         } ,
         "body" :   {
           "action" :   "x_www_form_urlencoded" ,
           "form_template" :   {
             "username" :   "{{$body.input.username}}"
           } ,
         } ,
         "request_headers" :   {
           "remove_headers" :   [ "content-type" ] ,
           "add_headers" :   {
             "content-type" :   "application/x-www-form-urlencoded"
           } ,
         } ,
       }
     } ,
     "comment" :   "Custom action to create user"
   }
}
```

### Response Body​

You can transform the default body of your HTTP API response by configuring a response transform template. This can be
used to match the output types defined in your Action with your HTTP API.

Note

Response transforms are applicable only for JSON responses.

- Console
- CLI
- API


In the `Configure REST Connectors` section, click on `Add Response Transform` :

Image: [ response transform method ](https://hasura.io/docs/assets/images/transform-response_actions_2.13-53ac21633f1f294bbed19f868a7c9b12.png)

Hit `Create Action` to apply your changes.

Update the `actions.yaml` file inside the `metadata` directory and add a[ response_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#responsetransformation)field to the Action:

```
-   name :  create_user
   definition :
     kind :  synchronous
     handler :  https : //action.my_app.com/create - user
   timeout :   60
   response_transform :
     template_engine :  Kriti
     version :   2
     body :   '{"action": "transform", "template": "{\n  \"test\":{{$body.input.arg1.id}}\n}"}'
```

Apply the Metadata by running:

`hasura metadata apply`

REST Connectors can be configured for Actions using the[ create_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action)or[ update_action ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-update-action)Metadata APIs by adding a[ response_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#responsetransformation)field to
the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "create_action" ,
   "args" : {
     "name" : "create_user" ,
     "definition" : {
       "kind" : "synchronous" ,
       "arguments" : [
         {
           "name" : "username" ,
           "type" : "String!"
         } ,
         {
           "name" : "email" ,
           "type" : "String!"
         }
       ] ,
       "output_type" : "User" ,
       "handler" : "{{ACTION_BASE_URL}}" ,
       "timeout" : 60 ,
       "response_transform" :   {
         "template_engine" :   "Kriti" ,
         "version" :   2 ,
         "body" :   { "action" :   "transform" ,   "template" :   "{\n  \"test\":{{$body.input.arg1.id}}\n}" } ,
         "comment" :   "Custom action to create user"
       }
     }
   }
}
```

Note

You can also apply multiple transforms based on the following:

1. HTTP response received from the Action webhook in the response transform template. For example:


```
{{ if $response.status == 200 }}
  {
    "users": {
      "name": {{$body}},
      "password": {{$body}}
    }
  }
{{ elif $response.status == 400 }}
  {
    "message": {{$body.error}}
  }
{{ else }}
  {
    "message" : "internal error"
  }
{{ end }}
```

1. Session Variables. For example:


```
{{ if $session_variables["x-hasura-role"] == "admin" }}
  {
    "users": {
      "name": {{$body}},
      "password": {{$body}}
    }
  }
{{ elif $session_variables["x-hasura-role"] == "user" }}
  {
    "users": {
      "name": {{$body.username}},
      "password": "<redacted password>"
    }
  }
{{ else }}
  {
    "message" : "internal error"
  }
{{ end }}
```

## Example​

Let's integrate Auth0's management API to update the profile of a user:

- Console
- CLI
- API


Go to the `Actions` tab on the Console and create or modify an action. Scroll down to `Configure REST Connectors` section:

Action definition:

Image: [ Example rest connector for actions ](https://hasura.io/docs/assets/images/example-transformation-0-98a8caef7122ebf94543cd3f579ccc33.png)

The transformation is given by:

Image: [ Example rest connector for actions ](https://hasura.io/docs/assets/images/example-transformation-1-6264883debc81574aacece7554b9bf6c.png)

Image: [ Example rest connector for actions ](https://hasura.io/docs/assets/images/example-transformation-2-6289ebe07598c4d44d2fa2e72db76185.png)

To be added

Action definition:

```
type   Mutation   {
   updateProfile ( picture_url :   String ! ) :   ProfileOutput
}
type   ProfileOutput   {
   id :   String !
   user_metadata :   String !
}
```

The transform is given by:

```
{
   "request_transform" :   {
     "body" :   "{\"user_metadata\": {\"picture\": {{$body.input.picture_url}} } }" ,
     "url" :   "{{$base_url}}/{{$session_variables['x-hasura-user-id']}}" ,
     "method" :   "PATCH"
   }
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/actions/rest-connectors/#introduction)
- [ Configuring REST Connectors ](https://hasura.io/docs/latest/actions/rest-connectors/#configuring-rest-connectors)
    - [ Context Variables ](https://hasura.io/docs/latest/actions/rest-connectors/#action-transform-context-variables)
- [ Types of transforms ](https://hasura.io/docs/latest/actions/rest-connectors/#action-transform-types)
    - [ Request Method ](https://hasura.io/docs/latest/actions/rest-connectors/#request-method)

- [ Request URL ](https://hasura.io/docs/latest/actions/rest-connectors/#request-url)

- [ Request Body ](https://hasura.io/docs/latest/actions/rest-connectors/#request-body)

- [ Response Body ](https://hasura.io/docs/latest/actions/rest-connectors/#response-body)
- [ Example ](https://hasura.io/docs/latest/actions/rest-connectors/#example)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)