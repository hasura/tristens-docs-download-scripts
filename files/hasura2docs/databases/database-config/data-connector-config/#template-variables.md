# Data Connector Config

## Introduction​

The configuration of[ data connectors ](https://hasura.io/docs/latest/databases/data-connectors/)depends on the specific data connector
you are connecting to. But, two options are available that are common amongst all data
connectors. Those two options are:

1. [ Timeout ](https://hasura.io/docs/latest/databases/database-config/data-connector-config/#template-variables/#timeout)
2. [ Template ](https://hasura.io/docs/latest/databases/database-config/data-connector-config/#template-variables/#template)


This configuration only applies to Hasura Data Connector Agents

Please note that this only applies to[ data connectors ](https://hasura.io/docs/latest/databases/data-connectors/). If you are using a
native database connection then this configuration does not apply. You can learn more about connecting to a
native database[ here ](https://hasura.io/docs/latest/databases/overview/#supported-databases).

### Timeout​

The timeout setting is related to how long the graphql engine will wait for a response from the
data connector agent before throwing an error. This value defaults to 30 seconds.

As an example, if it takes more than 30 seconds to introspect the schema of a data connector, then it
is likely you may be connecting to a slow or latent data source. In this case, you may want to increase
the timeout value to allow for the introspection to complete.

Timeout has three available setting options:

1. Seconds `seconds`  `{ "seconds": 60 }`
2. Milliseconds `milliseconds`  `{ "milliseconds": 60000 }`
3. Microseconds `microseconds`  `{ "microseconds": 60000000 }`


- Console
- CLI
- API


Console only supports seconds timeout

`seconds`

The Console only gives you the option to use `seconds` . If you need to use `milliseconds` or `microseconds` you
will need to use CLI or the API.

In the Console, navigate to the `Data` tab and select your data connector. Then, under the `Advanced` tab you
will can set the timeout value.

Image: [ Data connector advanced config ](https://hasura.io/docs/assets/images/data-connector-config-e333a2072d089626498f73f8f7bacfa0.png)

You can add a *timeout* for a data connector database by adding their config to the `/metadata/databases/database.yaml` file. In the example below, we're using
Snowflake:

```
-   name :  snowflake
   kind :  snowflake
   configuration :
     template :   null
     timeout :   {   "seconds" :   120   }
     value :   {
       "jdbc_url" :   "jdbc:snowflake://url.snowflakecomputing.com/?user=user&password=password&warehouse=warehouse&db=db&role=role&schema=schema"
     }
```

The *timeout* via the[ {{connector_name}}_add_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/)Metadata API. In the example below, we're using
Snowflake:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "snowflake_add_source" ,
   "args" :   {
     "name" :   "db" ,
     "configuration" :   {
       "template" :   null ,
       "timeout" :   {   "seconds" :   120   } ,
       "value" :   {
         "jdbc_url" :   "jdbc:snowflake://url.snowflakecomputing.com/?user=user&password=password&warehouse=warehouse&db=db&role=role&schema=schema"
       }
     }
   }
}
```

### Template​

You can use the template field to either set connection strings from `ENV` variables or implement more complex logic
for a connection string based on some other available variables. Currently, the template for data connectors
has access to:

- [ Environment variables ](https://hasura.io/docs/latest/databases/database-config/data-connector-config/#template-variables/#environment-variables)
- [ Session variables ](https://hasura.io/docs/latest/databases/database-config/data-connector-config/#template-variables/#session-variables)
- [ Configuration variables ](https://hasura.io/docs/latest/databases/database-config/data-connector-config/#template-variables/#configuration-variables)
- [ Template variables ](https://hasura.io/docs/latest/databases/database-config/data-connector-config/#template-variables/#template-variables)


Templates are written using the[ Kriti templating language ](https://hasura.io/docs/latest/api-reference/kriti-templating/).

- Console
- CLI
- API


In the Console, navigate to the `Data` tab and select your data connector. Then, under the `Advanced` tab you
will can set the template value.

Image: [ Data connector advanced config ](https://hasura.io/docs/assets/images/data-connector-config-e333a2072d089626498f73f8f7bacfa0.png)

You can add a *template* for a data connector database by adding their config to the `/metadata/databases/database.yaml` file:

```
-   name :  snowflake
   kind :  snowflake
   configuration :
     template :   |
      {"jdbc_url": "jdbc:snowflake://url.snowflakecomputing.com/?password={{$vars['snowflake_password']}}&user={{$env['SNOWFLAKE_USER']}}&warehouse=warehouse&db=db&role=role&schema=schema"}
     template_variables :
       snowflake_password :
         type :  dynamic_from_file
         filepath :  /var/secrets/snowflake_password.txt
     timeout :   null
     value :   { }
```

Apply the Metadata by running:

`hasura metadata apply`

The *template* via the[ {{:connector_name}}_add_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/)Metadata API.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "snowflake_add_source" ,
   "args" :   {
     "name" :   "db" ,
     "configuration" :   {
       "template" :   "{\"jdbc_url\": \"jdbc:snowflake://url.snowflakecomputing.com/?password={{$vars['snowflake_password']}}&user={{$env['SNOWFLAKE_USER']}}&warehouse=warehouse&db=db&role=role&schema=schema}" ,
       "template_variables" :   {
         "snowflake_password" :   {
           "type" :   "dynamic_from_file" ,
           "filepath: " /var/secrets/snowflake_password.txt"
         }
       }
       "timeout" :   null ,
       "value" :   { }
     }
   }
}
```

#### Environment variables​

Environment variables can be accessed using the variable `$env` or using the function `getEnvironmentVariable` in your Kriti templating. A simple example would be to use the environment variable `SNOWFLAKE_JDBC_URL` to set
the connection string for a Snowflake data connector:

```
{"jdbc_url": "$env["SNOWFLAKE_JDBC_URL"]"}
{"jdbc_url": "getEnvironmentVariable("SNOWFLAKE_JDBC_URL")"}
```

#### Session variables​

You can refer to session variables in the template using the variable `$session` . The session variable keys always contain `x-hasura-*` as the prefix:

```
{{if (empty($session?['x-hasura-role'])) && (empty($session?['x-hasura-user-id']))}}
  {"jdbc_url": "jdbc:snowflake://url.snowflakecomputing.com/?user=getEnvironmentVariable("DEFAULT_USER")&password=getEnvironmentVariable("DEFAULT_PASS")&warehouse=warehouse&db=db&role=role&schema=schema"}
{{else}}
  {"jdbc_url": "jdbc:snowflake://url.snowflakecomputing.com/?user={{$session['x-hasura-role']}}&password={{$session['x-hasura-user-id']}}&warehouse=warehouse&db=db&role=role&schema=schema"}
{{end}}
```

In this example, if the session variables `x-hasura-role` and `x-hasura-user-id` are both empty, then the graphql engine will use
the connection string with the `DEFAULT_USER` and the `DEFAULT_PASS` from our environment variables.
Otherwise, the graphql engine will use the values of `x-hasura-role` and `x-hasura-user-id` to generate the
connection string dynamically.

#### Configuration variables​

Config variables can be accessed using the variable `$config` . This allows you to access any field from the
data connector's configuration fields. As a simple example, you could set up your template to check the value
of the JDBC url configuration field as environment variable or fallback to using the value as the JDBC url.

`{"jdbc_url":{{$env?[$config.jdbc_url] ?? $config.jdbc_url}}}`

#### Template variables​

Supported versions

Template variables are supported on Hasura GraphQL Engine from v2.35.0 onwards.
However, they are not supported on Hasura Cloud.

Template variables allow you to define variables that can be referred to in your template using the variable `$vars` .
The values of these variables can be dynamically loaded on a per-query basis from a file on disk.

`{"jdbc_url": "jdbc:snowflake://url.snowflakecomputing.com/?password={{$vars['snowflakePassword']}}&user={{$env['SNOWFLAKE_USER']}}&warehouse=warehouse&db=db&role=role&schema=schema"}`

This can be useful in scenarios where you need to rotate credentials regularly and you want to avoid restarting Hasura
in order to update environment variables. Instead, you can write the credentials to a file and load the file contents
as a template variable to incorporate it in your configuration Kriti template. The file could be updated with new
credentials when they change, and the new credentials will be used by all requests following the file update.

Configuration

This feature requires the environment variable `HASURA_GRAPHQL_DYNAMIC_SECRETS_ALLOWED_PATH_PREFIX` to be set to the path
that you will locate your files in. For example, you could use `/var/secrets/` . Only file paths that have this prefix
will be allowed to be accessed as a template variable.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/database-config/data-connector-config/#template-variables/#introduction)
    - [ Timeout ](https://hasura.io/docs/latest/databases/database-config/data-connector-config/#template-variables/#timeout)

- [ Template ](https://hasura.io/docs/latest/databases/database-config/data-connector-config/#template-variables/#template)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)