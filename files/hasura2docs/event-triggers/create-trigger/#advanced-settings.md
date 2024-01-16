# Create an Event Trigger

## Introduction​

Event Triggers can be created using the Hasura Console, Hasura CLI, or Metadata APIs. Currently, support for event
triggers exists for Postgres and MSSQL databases.

Note

- Event Triggers are supported for **Postgres and MS SQL Server** databases.
- Event webhook notifications will be delivered at least once, and may arrive out of order with respect to the
underlying event.


Caveat on different Hasura instances connected to the same database

Event Triggers store their data in the underlying database and hence different instances acting on the same data can
cause undefined behavior during run-time. This should not be a problem if the Hasura instances have the same metadata.

## Creating triggers​

- Console
- CLI
- API


Open the Hasura Console, head to the `Events` tab and click on the `Create` button to open the page below:

Image: [ Create an Event Trigger ](https://hasura.io/docs/assets/images/create-event-trigger-a0c9b6c15b2edd4e6140fd10fef455bc.png)

You can add an Event Trigger for a table by updating the `databases > [source-name] > tables > [table-name].yaml` file
inside the `metadata` directory:

```
-   table :
    schema :  public
    name :  author
event_triggers :
    -   name :  author_trigger
    definition :
       enable_manual :   false
       insert :
          columns :   "*"
       update :
          columns :   "*"
    webhook :  https : //httpbin.org/post
```

Apply the Metadata by running:

`hasura metadata apply`

You can create Event Triggers by using the appropriate Metadata API, either:[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)or[ mssql_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-create-event-trigger).

To create an Event Trigger via the the Metadata API, replace `<db_type_create_event_trigger>` with the following:

- **Postgres** : `pg_create_event_trigger`
- **MSSQL** : `mssql_create_event_trigger`


```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type"   :   "<db_type_create_event_trigger>" ,
    "args"   :   {
       "name" :   "author_trigger" ,
       "source" :   "<db_name>" ,
       "table" :   {
          "name" :   "author" ,
          "schema" :   "public"
       } ,
       "webhook" :   "https://httpbin.org/post" ,
       "insert" :   {
             "columns" :   "*"
       } ,
       "update" :   {
             "columns" :   "*"
       }
    }
}
```

Note

UPDATE Event Trigger for MSSQL will only work on tables that have a primary key.

### Parameters​

 **Trigger Name** 

Unique name for Event Trigger.

 **Schema/Table** 

The postgres schema and table name on which the Event Trigger needs to be created.

 **Trigger Operations** 

The table operation on which the Event Trigger will be invoked.

 **Webhook URL** 

The HTTP(s) URL which will be called with the event payload on configured operation. Must be a `POST` handler. This URL
can be entered manually or can be picked up from an environment variable ( *the environment variable needs to be set
before using it for this configuration* ).

Note

If you are running Hasura using Docker, ensure that the Hasura Docker container can reach the webhook. See[ this page ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-networking)for Docker networking.

## Advanced Settings​

### Listen columns for update​

Update operations are special because you may want to trigger a webhook only if specific columns have changed in a row.
Choose the columns here which you want the update operation to listen to.

If a column is not selected here, then an update to that column will not trigger the webhook.

- Console
- CLI
- API


Expand the `Advanced Settings` section on the Hasura Console to define advanced settings for an Event Trigger:

Image: [ Listen columns for update Event Triggers ](data:image/png;base64,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)

You can configure advanced settings for Event Triggers in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  author
   event_triggers :
     -   name :  author_trigger
       definition :
         enable_manual :   false
         insert :
           columns :   '*'
         update :
           columns :
             -  name
             -  addr
       webhook :  https : //httpbin.org/post
```

Apply the Metadata by running:

`hasura metadata apply`

You can configure advanced settings via the appropriate Metadata API using either[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)or[ mssql_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-create-event-trigger).

Replace `<db_type_create_event_trigger>` with the following:

- **Postgres** : `pg_create_event_trigger`
- **MSSQL** : `mssql_create_event_trigger`


```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type"   :   "<db_type_create_event_trigger>" ,
    "args" :   {
       "name" :   "author_trigger" ,
       "source" :   "<db_name>" ,
       "table" :   {
          "name" :   "author" ,
          "schema" :   "public"
       } ,
       "webhook" :   "https://httpbin.org/post" ,
       "insert" :   {
          "columns" :   "*"
       } ,
       "update" :   {
          "columns" :   [ "name" ,   "addr" ]
       } ,
       "retry_conf" :   {
          "num_retries" :   0 ,
          "interval_sec" :   10 ,
          "timeout_sec" :   60
       } ,
       "headers" :   [
          {
             "name" :   "X-Hasura-From-Val" ,
             "value" :   "static-value"
          } ,
          {
             "name" :   "X-Hasura-From-Env" ,
             "value_from_env" :   "EVENT_WEBHOOK_HEADER"
          }
       ] ,
       "replace" :   false
    }
}
```

### Retry Logic​

Retry configuration is available in the "Advanced settings" when you create a trigger.

1. `num_retries` : Number of times a failed invocation is retried. Default value is **0** .
2. `interval_sec` : Number of seconds after which a failed invocation is retried. Default value is **10** .
3. `timeout_sec` : Number of seconds before which client closes the connection to the webhook. Default value is **60** .


- Console
- CLI
- API


Expand the `Advanced Settings` section on the Hasura Console to define advanced settings for an Event Trigger:

Image: [ Retry settings for Event Triggers ](data:image/png;base64,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)

You can configure advanced settings for Event Triggers in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
    schema :  public
    name :  author
    event_triggers :
    -   name :  author_trigger
       definition :
          enable_manual :   false
          insert :
          columns :   '*'
          update :
          columns :   [ 'name' ]
       retry_conf :
          num_retries :   0
          interval_sec :   10
          timeout_sec :   60
       headers :
       -   name :  X - Hasura - From - Val
          value :  static - value'
       -   name :  X - Hasura - From - Env
          value_from_env :  EVENT_WEBHOOK_HEADER
       webhook :  https : //httpbin.org/post
```

Apply the Metadata by running:

`hasura metadata apply`

Again, you can configure advanced settings via the appropriate Metadata API, either:[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)or[ mssql_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-create-event-trigger).

Replace `<db_type_create_event_trigger>` with the following:

- **Postgres** : `pg_create_event_trigger`
- **MSSQL** : `mssql_create_event_trigger`


```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "<db_type_create_event_trigger>" ,
    "args" :   {
       "name" :   "author_trigger" ,
       "source" :   "<db_name>" ,
       "table" :   {
          "name" :   "author" ,
          "schema" :   "public"
       } ,
       "webhook" :   "https://httpbin.org/post" ,
       "insert" :   {
          "columns" :   "*"
       } ,
       "update" :   {
          "columns" :   [ "name" ]
       } ,
       "retry_conf" :   {
          "num_retries" :   0 ,
          "interval_sec" :   10 ,
          "timeout_sec" :   60
       } ,
       "headers" :   [
          {
             "name" :   "X-Hasura-From-Val" ,
             "value" :   "static-value"
          } ,
          {
             "name" :   "X-Hasura-From-Env" ,
             "value_from_env" :   "EVENT_WEBHOOK_HEADER"
          }
       ] ,
       "replace" :   false
    }
}
```

Note

Event Triggers are supported for Postgres and MSSQL databases. To create an Event Trigger via the the Metadata API,
replace `<db_type>` with the following:

- **Postgres** : `pg`
- **MSSQL** : `mssql`


### Headers​

Custom headers can be added to an Event Trigger. Each webhook request will have these headers added.

Each header has 3 parameters:

1. `Key` : Name of the header e.g. Authorization or X-My-Header.
2. `Type` : One of `static` or `from env variable` . `static` means the value provided in the `Value` field is the raw
value of the header. `from env variable` means the value provided in the `Value` field is the name of the environment
variable in the GraphQL Engine which will be resolved before sending the header.
3. `Value` : The value of the header. Either a static value or the name of an environment variable.


- Console
- CLI
- API


Expand the `Advanced Settings` section on the Hasura Console to define advanced settings for an Event Trigger:

Image: [ Headers for Event Triggers ](https://hasura.io/docs/assets/images/create-event-trigger-headers-22311254e9d228c5a4df779c6720aaa8.png)

You can configure advanced settings for Event Triggers in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  author
   event_triggers :
     -   name :  author_trigger
       definition :
         enable_manual :   false
         insert :
           columns :   '*'
         update :
           columns :   [ 'name' ]
       retry_conf :
         num_retries :   0
         interval_sec :   10
         timeout_sec :   60
       headers :
         -   name :  X - Hasura - From - Val
           value :  static - value'
         -   name :  X - Hasura - From - Env
           value_from_env :  EVENT_WEBHOOK_HEADER
       webhook :  https : //httpbin.org/post
```

Apply the Metadata by running:

`hasura metadata apply`

You can configure advanced settings via the appropriate Metadata API, either:[ pg_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-pg-create-event-trigger)or[ mssql_create_event_trigger ](https://hasura.io/docs/latest/api-reference/metadata-api/event-triggers/#metadata-mssql-create-event-trigger).

Replace `<db_type_create_event_trigger>` with the following:

- **Postgres** : `pg_create_event_trigger`
- **MSSQL** : `mssql_create_event_trigger`


```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" :   "<db_type_create_event_trigger>" ,
    "args" :   {
       "name" :   "author_trigger" ,
       "source" :   "<db_name>" ,
       "table" :   {
          "name" :   "author" ,
          "schema" :   "public"
       } ,
       "webhook" :   "https://httpbin.org/post" ,
       "insert" :   {
          "columns" :   "*"
       } ,
       "update" :   {
          "columns" :   [ "name" ]
       } ,
       "retry_conf" :   {
          "num_retries" :   0 ,
          "interval_sec" :   10 ,
          "timeout_sec" :   60
       } ,
       "headers" :   [
          {
             "name" :   "X-Hasura-From-Val" ,
             "value" :   "static-value"
          } ,
          {
             "name" :   "X-Hasura-From-Env" ,
             "value_from_env" :   "EVENT_WEBHOOK_HEADER"
          }
       ] ,
       "replace" :   false
    }
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/event-triggers/create-trigger/#advanced-settings/#introduction)
- [ Creating triggers ](https://hasura.io/docs/latest/event-triggers/create-trigger/#advanced-settings/#creating-triggers)
    - [ Parameters ](https://hasura.io/docs/latest/event-triggers/create-trigger/#advanced-settings/#parameters)
- [ Advanced Settings ](https://hasura.io/docs/latest/event-triggers/create-trigger/#advanced-settings/#advanced-settings)
    - [ Listen columns for update ](https://hasura.io/docs/latest/event-triggers/create-trigger/#advanced-settings/#listen-columns-for-update)

- [ Retry Logic ](https://hasura.io/docs/latest/event-triggers/create-trigger/#advanced-settings/#retry-logic)

- [ Headers ](https://hasura.io/docs/latest/event-triggers/create-trigger/#advanced-settings/#headers)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)