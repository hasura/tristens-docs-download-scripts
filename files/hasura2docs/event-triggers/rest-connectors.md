# REST Connectors for Event Triggers

## Introduction​

REST Connectors for Event Triggers are used to invoke existing or third-party webhooks without needing any middleware or
modifications to the upstream code.

REST Connectors modify the Event Trigger's HTTP request to adapt to your webhook's expected format by adding suitable
transforms.

Note

General information about the templating used in REST Connectors can be found in the[ Kriti templating ](https://hasura.io/docs/latest/api-reference/kriti-templating/)section of the documentation.

Supported from

REST Connectors are supported in Hasura GraphQL Engine versions `v2.1.0` and above.

## Configuring REST Connectors​

REST Connectors can be configured either when creating a new Event Trigger or editing an existing one. See the transform
options[ here ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#event-trigger-transform-types):

- Console
- CLI
- API


Go to the `Events` tab on the Console and create or modify an Event Trigger. Scroll down to `Configure REST Connectors` section:

Image: [ Configure REST Connectors for Event Triggers ](https://hasura.io/docs/assets/images/transform-configure-rest-connectors-1e2a6dd38617ec84291a5df164fe4fc6.png)

Update the `databases > [source-name] > tables > [table-name].yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the Event Trigger:

```
table :
   name :  users
   schema :  public
event_triggers :
   -   name :  insert_trigger_on_users
     definition :
       insert :
         columns :   '*'
     webhook :  https : //api.somedomain.com
     headers :
       -   name :  Authorization
         value :  bearer - xxxx
     request_transform :
       template_engine :  Kriti
       method :  POST
       url :   '{{$base_url}}/api/v3/endpoint'
       query_params :
         query_param :  xxxxx
       content_type :  application/json
       body :
        " { \n  \"table\" :   { \n    \"name\" :   { { $body.table.name } } , \n    \"schema\" :   { { $body.table.schema } } \n   } , \n  \"To\" :
         { \n    \"username\" :   { { $body.event.data.new.name } } , \n    \"email\" :   { { $body.event.data.new.email } } \n   } \n } "
```

Apply the Metadata by running:

`hasura metadata apply`

You can configure REST Connectors for Event Triggers using the[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)Metadata API and adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_event_trigger" ,
   "args" :   {
     "name" :   "insert_trigger_on_users" ,
     "replace" :   true ,
     "source" :   "default" ,
     "table" :   {
       "name" :   "users" ,
       "schema" :   "public"
     } ,
     "webhook" :   "https://api.somedomain.com" ,
     "insert" :   {
       "columns" :   "*"
     } ,
     "headers" :   [
       {
         "name" :   "Authorization" ,
         "value" :   "bearer xxxx"
       }
     ] ,
     "request_transform" :   {
       "template_engine" :   "Kriti" ,
       "method" :   "POST" ,
       "url" :   "{{$base_url}}/api/v3/endpoint" ,
       "query_params" :   {
         "query_param" :   "xxxxx"
       } ,
       "content_type" :   "application/json" ,
       "body" :   "{\n  \"table\": {\n    \"name\": {{$body.table.name}},\n    \"schema\": {{$body.table.schema}}\n  },\n  \"To\": {\n    \"username\": {{$body.event.data.new.name}},\n    \"email\": {{$body.event.data.new.email}}\n  }\n}"
     }
   }
}
```

### Context Variables​

You can use context variables in the transforms to achieve dynamic behavior for each request.

The context variables available in transforms are:

| Context variable | Value |
|---|---|
| $body | Original body of event request |
| $base_url | Original configured webhook URL |
| $session_variables | Session variables |
| $query_params | Query parameters and the values to be sent to the webhook |
| $response.status | HTTP response staus code from the webhook |


#### Console sample context​

The Console allows you to preview your transforms while configuring them. To avoid exposing sensitive information on the
console UI the actual environment variables configured on the server are not resolved while displaying the previews.
Also any session variables used in the transform will not be available at the time of configuration.

Hence, the Console allows you to provide mock env variables and session variables to verify your transforms. If you
configure your transforms without providing the mock env/session variables you might see a UI validation error in the
preview sections.

 **For example:** If your webhook handler is set as an env var as shown below then pass a mock value for that env var in
the sample context:

Image: [ Console Event Trigger webhook handler ](https://hasura.io/docs/assets/images/transform-sample-context-0-083013558f6acae98a89feddce743701.png)

You can enter the mock env/session variables under `Configure REST Connectors > Sample Context` :

Image: [ Add generic sample context ](https://hasura.io/docs/assets/images/transform-sample-context-1-256200e94cd534ab73d43393d2e49798.png)

Note

As the sample context is only used for previews, you can still configure the transforms on the Console without setting
any sample context.

## Types of transforms​

REST Connectors allow you to add different transforms to the default HTTP request. You can also use[ context variables ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#event-trigger-transform-context-variables)in the transforms to achieve dynamic behavior for each
request.

You can transform your:

- [ Request Method ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#request-method)
- [ Request URL ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#request-url)
- [ Request Body ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#request-body)


### Request Method​

You can change the request method to adapt to your API's expected format.

- Console
- CLI
- API


Head to the `Events > [event_trigger_name]` page. Under `Configure REST Connectors` click on `Add Request Options Transform` .

Select the `Request Method` .

Image: [ Change request method ](https://hasura.io/docs/assets/images/transform-request-method-4cc00d5ec3209c3a1fa76fe913bc4a11.png)

Hit `Save Event Trigger` to apply your changes.

Update the `databases > [source-name] > tables > [table-name].yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the Event Trigger:

```
table :
   name :  users
   schema :  public
event_triggers :
   -   name :  insert_trigger_on_users
     definition :
       insert :
         columns :   "*"
     webhook :  https : //api.somedomain.com
   headers :
     -   name :  Authorization
       value :  bearer - xxxx
   request_transform :
     template_engine :  Kriti
     method :  POST
     url :   "{{$base_url}}/api/v3/endpoint"
     query_params :
       query_param :  xxxxx
     content_type :  application/json
     body :   "{\n  \"table\": {\n    \"name\": {{$body.table.name}},\n    \"schema\": {{$body.table.schema}}\n  },\n  \"To\": {\n    \"username\": {{$body.event.data.new.name}},\n    \"email\": {{$body.event.data.new.email}}\n  }\n}"
```

Apply the Metadata by running:

`hasura metadata apply`

You can configure REST Connectors for Event Triggers using the[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)Metadata API and adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_event_trigger" ,
   "args" :   {
     "name" :   "insert_trigger_on_users" ,
     "replace" :   true ,
     "source" :   "default" ,
     "table" :   {
       "name" :   "users" ,
       "schema" :   "public"
     } ,
     "webhook" :   "https://api.somedomain.com" ,
     "insert" :   {
       "columns" :   "*"
     } ,
     "headers" :   [
       {
         "name" :   "Authorization" ,
         "value" :   "bearer xxxx"
       }
     ] ,
     "request_transform" :   {
       "template_engine" :   "Kriti" ,
       "method" :   "POST" ,
       "url" :   "{{$base_url}}/api/v3/endpoint" ,
       "query_params" :   {
         "query_param" :   "xxxxx"
       } ,
       "content_type" :   "application/json" ,
       "body" :   "{\n  \"table\": {\n    \"name\": {{$body.table.name}},\n    \"schema\": {{$body.table.schema}}\n  },\n  \"To\": {\n    \"username\": {{$body.event.data.new.name}},\n    \"email\": {{$body.event.data.new.email}}\n  }\n}"
     }
   }
}
```

### Request URL​

The Request URL template allows you to configure the exact API endpoint to call.

You can use the[ context variables ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#event-trigger-transform-context-variables)to construct the final URL.

- [ Request URL with Query Parmeters (as key-value pairs) ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#request-url-with-query-parmeters-as-key-value-pairs)
- [ Request URL with Query Parmeters (as raw string) ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#request-url-with-query-parmeters-as-raw-string)


##### Request URL with Query Parmeters (as key-value pairs)​

You can provide `Key-Value` type query params to add to the URL.

You can also use the[ Kriti templating language ](https://hasura.io/docs/latest/api-reference/kriti-templating/)to construct any string values here.

- Console
- CLI
- API


Head to the `Events > [event_trigger_name]` page. Under `Configure REST Connectors` click on `Add Request Options Transform` .

Enter the `Request URL Template` and `Query Params` .

Image: [ Console Event Trigger request options transformation ](https://hasura.io/docs/assets/images/transform-key-value-request-options-dca4c151c0dccb10aa1ddd380a3d1b8f.png)

The value of the final url should be reflected in the `Preview` section given all required[ sample context ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#event-trigger-transforms-sample-context)is set.

Hit `Save Event Trigger` to apply your changes.

Update the `databases > [source-name] > tables > [table-name].yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the Event Trigger:

```
table :
   name :  users
   schema :  public
event_triggers :
   -   name :  insert_trigger_on_users
     definition :
       insert :
         columns :   "*"
     webhook :  https : //api.somedomain.com
   headers :
     -   name :  Authorization
       value :  bearer - xxxx
   request_transform :
     template_engine :  Kriti
     method :  POST
     url :   "{{$base_url}}/api/v3/endpoint"
     query_params :
       query_param :  xxxxx
     content_type :  application/json
     body :   "{\n  \"table\": {\n    \"name\": {{$body.table.name}},\n    \"schema\": {{$body.table.schema}}\n  },\n  \"To\": {\n    \"username\": {{$body.event.data.new.name}},\n    \"email\": {{$body.event.data.new.email}}\n  }\n}"
```

Apply the Metadata by running:

`hasura metadata apply`

You can configure REST Connectors for Event Triggers using the[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)Metadata API and adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_event_trigger" ,
   "args" :   {
     "name" :   "insert_trigger_on_users" ,
     "replace" :   true ,
     "source" :   "default" ,
     "table" :   {
       "name" :   "users" ,
       "schema" :   "public"
     } ,
     "webhook" :   "https://api.somedomain.com" ,
     "insert" :   {
       "columns" :   "*"
     } ,
     "headers" :   [
       {
         "name" :   "Authorization" ,
         "value" :   "bearer xxxx"
       }
     ] ,
     "request_transform" :   {
       "template_engine" :   "Kriti" ,
       "method" :   "POST" ,
       "url" :   "{{$base_url}}/api/v3/endpoint" ,
       "query_params" :   {
         "query_param" :   "xxxxx"
       } ,
       "content_type" :   "application/json" ,
       "body" :   "{\n  \"table\": {\n    \"name\": {{$body.table.name}},\n    \"schema\": {{$body.table.schema}}\n  },\n  \"To\": {\n    \"username\": {{$body.event.data.new.name}},\n    \"email\": {{$body.event.data.new.email}}\n  }\n}"
     }
   }
}
```

##### Request URL with Query Parmeters (as raw string)​

You can provide `string` type query params to add to the URL.

You can also use the[ Kriti templating language ](https://hasura.io/docs/latest/api-reference/kriti-templating/)to construct any string values here.

- Console
- CLI
- API


Head to the `Events > [event_trigger_name]` page. Under `Configure REST Connectors` click on `Add Request Options Transform` .

Enter the `Request URL Template` and `Query Params` .

Image: [ Console Event Trigger request options transformation ](https://hasura.io/docs/assets/images/transform-url-string-request-options-5836ae620a2cc0051f8fc3d386a39657.png)

The value of the final url should be reflected in the `Preview` section given all required[ sample context ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#event-trigger-transforms-sample-context)is set.

Hit `Save Event Trigger` to apply your changes.

Update the `databases > [source-name] > tables > [table-name].yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the Event Trigger:

```
table :
   name :  users
   schema :  public
event_triggers :
   -   name :  insert_trigger_on_users
     definition :
       insert :
         columns :   "*"
     webhook :  https : //api.somedomain.com
   headers :
     -   name :  Authorization
       value :  bearer - xxxx
   request_transform :
     template_engine :  Kriti
     method :  POST
     url :   "{{$base_url}}/api/v3/endpoint"
     query_params :  " { { concat( [ "userId=" ,  $session_variables [ "x-hasura-user-id" ] ] ) } } "
     content_type :  application/json
     body :   "{\n  \"table\": {\n    \"name\": {{$body.table.name}},\n    \"schema\": {{$body.table.schema}}\n  },\n  \"To\": {\n    \"username\": {{$body.event.data.new.name}},\n    \"email\": {{$body.event.data.new.email}}\n  }\n}"
```

Apply the Metadata by running:

`hasura metadata apply`

You can configure REST Connectors for Event Triggers using the[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)Metadata API and adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_event_trigger" ,
   "args" :   {
     "name" :   "insert_trigger_on_users" ,
     "replace" :   true ,
     "source" :   "default" ,
     "table" :   {
       "name" :   "users" ,
       "schema" :   "public"
     } ,
     "webhook" :   "https://api.somedomain.com" ,
     "insert" :   {
       "columns" :   "*"
     } ,
     "headers" :   [
       {
         "name" :   "Authorization" ,
         "value" :   "bearer xxxx"
       }
     ] ,
     "request_transform" :   {
       "template_engine" :   "Kriti" ,
       "method" :   "POST" ,
       "url" :   "{{$base_url}}/api/v3/endpoint" ,
       "query_params" :   "{{concat([" userId= ", $session_variables[" x-hasura-user-id "]])}}"
       "content_type" :   "application/json" ,
       "body" :   "{\n  \"table\": {\n    \"name\": {{$body.table.name}},\n    \"schema\": {{$body.table.schema}}\n  },\n  \"To\": {\n    \"username\": {{$body.event.data.new.name}},\n    \"email\": {{$body.event.data.new.email}}\n  }\n}"
     }
   }
}
```

escapeUri

Use the `escapeUri` function to `urlencode` templated values. For example, if you have to use session variables in the
URL and those may contain non-ASCII values, then you should provide the template URL as `{{$base_url}}/{{escapeUri($session_variables['x-hasura-user-id'])}}` .

Optional query params

Query params with key/value pairs which evaluate to `null` are ignored by Hasura while performing the HTTP API call.
Hasura considers such query params optional.

For example, consider a query param value with template `{{$session_variables?['x-hasura-user-id']}}` . If the variable `x-hasura-user-id` is absent in the session variables, then the query param will be omitted from the HTTP API call.

### Request Body​

You can generate a custom request body by configuring a template to transform the default payload to a custom payload.
Request body could be provided using the `body` field as an[ object ](https://hasura.io/docs/latest/api-reference/syntax-defs/#bodytransform),
which additionally gives the ability to disable request body, transform request body to `application/json` , or transform
request body to `x_www_form_urlencoded` formats.

- [ Disabling Request Body ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#disabling-request-body)
- [ Request Body with application/json format ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#request-body-with-applicationjson-format)
- [ Request Body with x_www_form_urlencoded format ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#request-body-with-x_www_form_urlencoded-format)


##### Disabling Request Body​

If you are using a `GET` request, you might want to not send any request body, and additionally not send a `content-type` header to the webhook. You can do that using the disable body feature.

- Console
- CLI
- API


In the `Configure REST Connectors` section, click on `Add Request Options Transform` , and convert the `Request Method` as `GET` .
Then click on `Add Payload Transform` , disable the payload body by using the dropdown next to the `Configure Request Body` section.

Image: [ Disable payload body ](https://hasura.io/docs/assets/images/transform-body-disable-f7f4935b28fafe4571c5a003899d22b5.png)

Hit `Create Event Trigger` to apply your changes.

Update the `databases > [source-name] > tables > [table-name].yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the Event Trigger:

```
table :
   name :  users
   schema :  public
event_triggers :
   -   name :  insert_trigger_on_users
     definition :
       insert :
         columns :   "*"
     webhook :  https : //api.somedomain.com
   headers :
     -   name :  Authorization
       value :  bearer - xxxx
   request_transform :
     template_engine :  Kriti
     version :   2
     method :  GET
     url :   "{{$base_url}}/api/v3/endpoint"
     query_params :
       query_param :  xxxxx
     body :
       action :   'remove'
     request_headers :
       remove_headers :   [ 'content - type ]
```

Apply the Metadata by running:

`hasura metadata apply`

You can configure REST Connectors for Event Triggers using the[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)Metadata API and adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_event_trigger" ,
   "args" :   {
     "name" :   "insert_trigger_on_users" ,
     "replace" :   true ,
     "source" :   "default" ,
     "table" :   {
       "name" :   "users" ,
       "schema" :   "public"
     } ,
     "webhook" :   "https://api.somedomain.com" ,
     "insert" :   {
       "columns" :   "*"
     } ,
     "headers" :   [
       {
         "name" :   "Authorization" ,
         "value" :   "bearer xxxx"
       }
     ] ,
     "request_transform" :   {
       "template_engine" :   "Kriti" ,
       "version" :   2 ,
       "method" :   "GET" ,
       "url" :   "{{$base_url}}/api/v3/endpoint" ,
       "query_params" :   {
         "query_param" :   "xxxxx"
       } ,
       "body" :   {
         "action" :   "remove"
       } ,
       "request_headers" :   {
         "remove_headers" :   [ "content-type" ] ,
       } ,
     }
   }
}
```

##### Request Body with application/json format​

You can transform Request Body to `application/json` format using the following steps:

- Console
- CLI
- API


In the `Configure REST Connectors` section, click on `Add Payload Transform` . By default Console sends the body as `application/json` which can be seen in the dropdown next to the `Configure Request Body` section.

Image: [ payload body application/json ](https://hasura.io/docs/assets/images/transform-body-application-json-60d1ee03ca56c99e3d9d8a9acdaa9525.png)

Hit `Create Event Trigger` to apply your changes.

Update the `databases > [source-name] > tables > [table-name].yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the Event Trigger:

```
table :
   name :  users
   schema :  public
event_triggers :
   -   name :  insert_trigger_on_users
     definition :
       insert :
         columns :   "*"
     webhook :  https : //api.somedomain.com
   headers :
     -   name :  Authorization
       value :  bearer - xxxx
   request_transform :
     template_engine :  Kriti
     version :   2
     method :  POST
     url :   "{{$base_url}}/api/v3/endpoint"
     query_params :
       query_param :  xxxxx
     body :
       action :   'transform'
       template :   '{"username": {{$body.table.username}}}'
```

Apply the Metadata by running:

`hasura metadata apply`

You can configure REST Connectors for Event Triggers using the[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)Metadata API and adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_event_trigger" ,
   "args" :   {
     "name" :   "insert_trigger_on_users" ,
     "replace" :   true ,
     "source" :   "default" ,
     "table" :   {
       "name" :   "users" ,
       "schema" :   "public"
     } ,
     "webhook" :   "https://api.somedomain.com" ,
     "insert" :   {
       "columns" :   "*"
     } ,
     "headers" :   [
       {
         "name" :   "Authorization" ,
         "value" :   "bearer xxxx"
       }
     ] ,
     "request_transform" :   {
       "template_engine" :   "Kriti" ,
       "version" :   2 ,
       "method" :   "POST" ,
       "url" :   "{{$base_url}}/api/v3/endpoint" ,
       "query_params" :   {
         "query_param" :   "xxxxx"
       } ,
       "body" :   {
         "action" :   "transform" ,
         "template" :   "{\"username\": {{$body.table.username}}}"
       } ,
     }
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

Image: [ payload body x_www_form_urlencoded ](https://hasura.io/docs/assets/images/transform-body-xurl-formencoded-b6b127a45c111c779961488f2cdea2c5.png)

Hit `Create Event Trigger` to apply your changes.

Update the `databases > [source-name] > tables > [table-name].yaml` file inside the `metadata` directory and add a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the Event Trigger:

```
table :
   name :  users
   schema :  public
event_triggers :
   -   name :  insert_trigger_on_users
     definition :
       insert :
         columns :   "*"
     webhook :  https : //api.somedomain.com
   headers :
     -   name :  Authorization
       value :  bearer - xxxx
   request_transform :
     template_engine :  Kriti
     version :   2
     method :  POST
     url :   "{{$base_url}}/api/v3/endpoint"
     query_params :
       query_param :  xxxxx
     body :
       action :   'x_www_form_urlencoded'
       form_template :
         username :   '{{$body.table.username}}'
     request_headers :
       remove_headers :   [ 'content-type' ]
       add_headers :
         'content-type' :   'application/x-www-form-urlencoded'
```

Apply the Metadata by running:

`hasura metadata apply`

You can configure REST Connectors for Event Triggers using the[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)Metadata API and adding a[ request_transform ](https://hasura.io/docs/latest/api-reference/syntax-defs/#requesttransformation)field to the args:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_event_trigger" ,
   "args" :   {
     "name" :   "insert_trigger_on_users" ,
     "replace" :   true ,
     "source" :   "default" ,
     "table" :   {
       "name" :   "users" ,
       "schema" :   "public"
     } ,
     "webhook" :   "https://api.somedomain.com" ,
     "insert" :   {
       "columns" :   "*"
     } ,
     "headers" :   [
       {
         "name" :   "Authorization" ,
         "value" :   "bearer xxxx"
       }
     ] ,
     "request_transform" :   {
       "template_engine" :   "Kriti" ,
       "version" :   2 ,
       "method" :   "POST" ,
       "url" :   "{{$base_url}}/api/v3/endpoint" ,
       "query_params" :   {
         "query_param" :   "xxxxx"
       } ,
       "body" :   {
         "action" :   "x_www_form_urlencoded" ,
         "form_template" :   {
           "username" :   "{{$body.table.username}}"
         } ,
       } ,
       "request_headers" :   {
         "remove_headers" :   [ "content-type" ] ,
         "add_headers" :   {
           "content-type" :   "application/x-www-form-urlencoded"
         } ,
       } ,
     }
   }
}
```

## Example: Trigger SendGrid's Mail Send API​

To see the REST Connectors for Event Triggers in action, let's set up an Event Trigger to send an email using the[ SendGrid Mail Send API ](https://docs.sendgrid.com/api-reference/mail-send/mail-send).

Let's say you have a table `users (id int, name text, email text)` and you would like to send the user an email whenever
a new user is inserted into the `users` table.

### Step 1: Configure Event Trigger details​

Head to the `Events` tab on your Console and create a new Event Trigger.

The SendGrid Mail Send API is available at `POST https://api.sendgrid.com/v3/mail/send` and expects an `Authorization` header to be passed with a SendGrid API key for access (see[ docs ](https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api/authentication)).

You can configure env vars, say `SENDGRID_BASE_URL` with the value `https://api.sendgrid.com` and `SENDGRID_API_KEY` with the value `Bearer <sendgrid-api-key>` on the server so that they can be used for this Event Trigger and any other
SendGrid requests we might want to use in the future.

You can now configure the Event Trigger as follows:

 **Table:**  `users` 

 **Operations:**  `Insert` 

 **Webhook:**  `SENDGRID_BASE_URL` 

 **Headers:**  `Authorization: SENDGRID_API_KEY` 

Image: [ Sengrid Event Trigger config ](https://hasura.io/docs/assets/images/transform-sendgrid-def-3321ad2737b0cc096184e7fd6724cff7.png)

### Step 2: Configure REST connector​

#### Step 2.1: Add Sample Context​

Set a mock value for the `SENDGRID_BASE_URL` env var to verify your URL transform that we will be configuring next as
the actual value is not exposed to the Console.

Image: [ Sengrid Event Trigger context ](https://hasura.io/docs/assets/images/transform-sendgrid-context-2858c520c84943ca64d50799864c07a5.png)

#### Step 2.2: Add Request Transforms​

##### Request Method and URL template​

The SendGrid API request uses the `POST` request method so you can choose that.

We need to add `/v3/mail/send` to the SendGrid base URL ( `https://api.sendgrid.com` ) that we configured in the env var.
This can be done by setting the URL template as `{{$base_url}}/v3/mail/send` .

Image: [ Sengrid Event Trigger request options ](https://hasura.io/docs/assets/images/transform-sendgrid-request-475c6bcf3a913813dd276b657d1d2e56.png)

##### Request Body​

Here is the request body template we would need for the SendGrid Mail Send API (see[ docs ](https://docs.sendgrid.com/api-reference/mail-send/mail-send#body)).

We replace the `email` and `name` values from the Event Trigger body:

```
{
  "personalizations":
   [
     {
       "from": { "email": "<from_email>", "name": "<from_name>" },
       "to":
         [
           {
             "email": {{ $body.event.data.new.email }},
             "name": {{ $body.event.data.new.name }}
           }
         ]
     }
   ],
  "from": { "email": "<from_email>", "name": "<from_name>" },
  "reply_to": { "email": "<replyto_email>", "name": "<from_name>" },
  "subject": "Welcome!",
  "content":
    [
      {
        "type": "text/html",
        "value": "<p>Mail from a Hasura Event Trigger!</p>"
      }
    ]
}
```

Image: [ Sengrid Event Trigger payload ](https://hasura.io/docs/assets/images/transform-sendgrid-body-dcc90d2efaf4356c7aa26f9ab4074023.png)

Hit `Create Event Trigger` to complete the Event Trigger set up.

### Step 3: Test the Event Trigger​

Insert a new user to the `users` table to call the SendGrid API.

Navigate to `Data > [database-name] > public > users` and insert a new row.

The `insert` operation triggers the Event Trigger and sends the transformed request to the SendGrid API which should
send an email to the inserted user.

You can view the **Processed Events** and **Invocation Logs** for the Event Trigger to check the SendGrid API response.

Image: [ Event Trigger logs ](https://hasura.io/docs/assets/images/transform-sendgrid-processed-events-6d1e98a5ed0c55786682cc7e36ee9277.png)

Note

Explore the Hasura Data Hub source code for[ Event Connectors ](https://hasura.io/data-hub/event-transforms/)with
different platform integrations.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#introduction)
- [ Configuring REST Connectors ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#configuring-rest-connectors)
    - [ Context Variables ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#event-trigger-transform-context-variables)
- [ Types of transforms ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#event-trigger-transform-types)
    - [ Request Method ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#request-method)

- [ Request URL ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#request-url)

- [ Request Body ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#request-body)
- [ Example: Trigger SendGrid's Mail Send API ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#example-trigger-sendgrids-mail-send-api)
    - [ Step 1: Configure Event Trigger details ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#step-1-configure-event-trigger-details)

- [ Step 2: Configure REST connector ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#step-2-configure-rest-connector)

- [ Step 3: Test the Event Trigger ](https://hasura.io/docs/latest/event-triggers/rest-connectors/#step-3-test-the-event-trigger)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)