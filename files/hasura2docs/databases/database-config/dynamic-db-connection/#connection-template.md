# Dynamic Routing for Databases

## Introduction​

Hasura Cloud and Enterprise customers can leverage dynamic routing to implement different kinds of database topology
patterns with Hasura. You can group different databases using a new Metadata configuration object called
'connection-set' and leverage the[ Kriti template ](https://hasura.io/docs/latest/api-reference/kriti-templating/)to define custom 'connection
templates' to route GraphQL requests based on different request parameters such as session variables, headers and tenant
IDs.

Caution

- Dynamic Database Connection Routing is available only for Postgres and Postgres-like backends currently.


Following are some of the top use cases for this feature:

### Connect with different database credentials​

If you are integrating with a vendor IAM or wish to use database RLS, you will want to use different connection
credentials per request. For example, in Hasura, you may use a session variable like `x-hasura-role` and use a specific
connection for that role.

### No-stale reads when read replicas are configured​

If read replicas are configured for a given source, then all query operations are routed to the read replicas, which
sometimes leads to stale reads because of replication lag. You can force certain query operations to the primary
connection by using some operation context variable like an operation name or a special request header.

### Route to a specific shard or node group in a distributed database​

In a distributed database system like YugabyteDB or CockroachDB, sometimes, you may want to route the request to a
specific node. You can achieve this in Hasura using a connection template.

## How it works​

When a request is executed, dynamic routing will use a connection template (in Kriti lang) to resolve a connection from
a connection set. Note that only non-admin roles use the connection template. The admin role will always use the `primary` connection.

There are two configurable parameters in the source configuration useful for dynamic routing:

1. [ Connection set ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#connection-set)
2. [ Connection template ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#connection-template)


### Connection set​

You can define a set of connections that are available for routing. You can refer the members of this connection set in
the[ connection template ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#connection-template)by their unique name using the variable `$.connection_set.<member's name>` .

### Connection template​

The logic for connection routing is defined as a[ Kriti template ](https://hasura.io/docs/latest/api-reference/kriti-templating/). This can resolve
to the following:

1. **A member of the connection set** The connection will be routed to a member of the connection set. **The request will fail if the name is not defined
in the connection set** . To use this, the template should resolve to the following variable:
2. **Predefined connections** The query can also be routed to connections that are already defined:
    1. **Primary source**
The query will be routed to the connection specified under `connection_info` . To use this, the template should
resolve to the following variable: ` $.primary` 
    1. **Read replicas**
The query will be routed to a randomly chosen member from the set of read replicas. **Please note that for mutations,
this will fail.** To use this, the template should resolve to the following variable: ` $.read_replicas` 
    1. **Default**
The connection template resolving to the `$.default` variable directs the query to follow the default behavior. E.g.,
if read replicas are configured, then all queries and subscriptions are routed to read replicas and mutations are
routed to the primary connection. Otherwise, Hasura will execute all GraphQL queries on the primary connection.


 **A member of the connection set** 

The connection will be routed to a member of the connection set. **The request will fail if the name is not defined
in the connection set** . To use this, the template should resolve to the following variable:

`$.connection_set.<name of a member of the connection set>`

 **Predefined connections** 

The query can also be routed to connections that are already defined:

The query will be routed to the connection specified under `connection_info` . To use this, the template should
resolve to the following variable: ` $.primary` 

The query will be routed to a randomly chosen member from the set of read replicas. **Please note that for mutations,
this will fail.** To use this, the template should resolve to the following variable: ` $.read_replicas` 

The connection template resolving to the `$.default` variable directs the query to follow the default behavior. E.g.,
if read replicas are configured, then all queries and subscriptions are routed to read replicas and mutations are
routed to the primary connection. Otherwise, Hasura will execute all GraphQL queries on the primary connection.

The context for the connection template contains the request variables ( `$.request` ). The request variable includes the
following:

1. **HTTP headers** These are client headers associated with the request. Users can refer to the headers in the template using the
variable `$.request.headers` . Header names are case insensitive; hence their names are provided in lowercase in the
template context. An example template using HTTP headers:For this example, if the header `no-stale-read` is set to `true` , then Hasura will route the requests to the `primary` source. Otherwise, it will use the `read_replicas` .
2. **Session variables** These are the key-value pairs returned from your authentication service. They can be referred to in the template
using the variable `$.request.session` . The session variable keys always contain `x-hasura-*` as the prefix. An
example template using session variables:For this example, if the session variable `x-hasura-role` is set to `dev` , then Hasura will route the requests to the `dev_db` in connection_set. Otherwise, Hasura will look up if there is a connection member with the name of `x-hasura-tenant-id` and route to that member if it exists. If not, then it will fall back to the default behavior.
3. **Graphql query parameters** These are the operation type and operation name for the GraphQL query. They can be referred to in the template using
the variable `$.request.query` . This variable can only have two keys:[ operation type ](https://spec.graphql.org/October2021/#OperationType)and[ operation name ](https://spec.graphql.org/October2021/#sec-Named-Operation-Definitions)(optional). An example
template using the query parameters:For this example, Hasura will route to the `primary` database for mutations and `read_replicas` for everything else.


 **HTTP headers** 

These are client headers associated with the request. Users can refer to the headers in the template using the
variable `$.request.headers` . Header names are case insensitive; hence their names are provided in lowercase in the
template context. An example template using HTTP headers:

```
{{ if ($.request.headers?[no-stale-read] == "true")}}
  {{$.primary}}
{{ else }}
  {{$.read_replicas}}
```

For this example, if the header `no-stale-read` is set to `true` , then Hasura will route the requests to the `primary` source. Otherwise, it will use the `read_replicas` .

 **Session variables** 

These are the key-value pairs returned from your authentication service. They can be referred to in the template
using the variable `$.request.session` . The session variable keys always contain `x-hasura-*` as the prefix. An
example template using session variables:

```
{{ if $.request.session?["x-hasura-role"] == "dev" }}
  {{ $.​connection_set.dev_db }}
{{ else }}
  {​{ if ​$.connection_set?[$.request.session.x-hasura-tenant-id] != null }}
    {{ ​$.connection_set[$.request.session.x-hasura-tenant-id] }}
  {{ else }}
    {{ $.default }}
  {{ end }}
{{ end }}
```

For this example, if the session variable `x-hasura-role` is set to `dev` , then Hasura will route the requests to the `dev_db` in connection_set. Otherwise, Hasura will look up if there is a connection member with the name of `x-hasura-tenant-id` and route to that member if it exists. If not, then it will fall back to the default behavior.

 **Graphql query parameters** 

These are the operation type and operation name for the GraphQL query. They can be referred to in the template using
the variable `$.request.query` . This variable can only have two keys:[ operation type ](https://spec.graphql.org/October2021/#OperationType)and[ operation name ](https://spec.graphql.org/October2021/#sec-Named-Operation-Definitions)(optional). An example
template using the query parameters:

```
{{ if ($.request.query.operation_type == "mutation") }}
    {{$.primary}}
{{ else }}
    {{$.read_replicas}}
{{ end }}
```

For this example, Hasura will route to the `primary` database for mutations and `read_replicas` for everything else.

An example of the request context:

```
{
   "headers" :   {
     "x-hasura-role" :   "user" ,
    ...
   } ,
   "session" :   {
     "x-hasura-role" :   "user" ,
     "x-hasura-org" :   "hasura" ,
    ...
   } ,
   "query" :   {
     "operation_type" :   "query" ,
     "operation_name" :   "MyQuery"
   }
}
```

You can build your connection template using these variables. An example of a connection template is given below:

Example:

```
{{ if ($.request.query.operation_type == "query") || ($.request.query.operation_type == "subscription") }}
  {{ if $.request.session?["x-hasura-role"] == "developer" }}
      {{if $.request.headers?["route-to-read-replicas"] == "true"}}
        {{$.read_replicas}}
      {{else}}
        {{$.connection_set.dev_db}}
      {{end}}
  {{else}}
      {{$.default}}
  {{ end }}
{{else}}
    {{ if $.request.session?["x-hasura-role"] == "priority-user" }}
        {{$.connection_set.fast_db}}
    {{else}}
        {{$.primary}}
    {{ end }}
{{ end }}
```

Explanation:

- For query/subscription GraphQL operations, if the `x-hasura-role` is `developer` , then use `read_replicas` if the
header `route-to-read-replicas` is set to `true` . Otherwise, use the `dev_db` from the connection set.
- For query/subscription GraphQL operations, if the `x-hasura-role` is not `developer` , then route using the `default` behavior.
- For mutations, if the `x-hasura-role` is set to `priority-user` , then use the `fast_db` from the connection set; else,
use the `primary` connection.


## Setting up connection set and connection template​

- Console
- CLI
- API


To access Dynamic Routing, navigate to the `Dynamic Routing` tab in the Edit Data Source page.

Select the template you want to use from the list of available templates, or click on `Custom Template` to create your
own template.

Image: [ Dynamic routing ](https://hasura.io/docs/assets/images/edit-connection-template-2f9cf3137599eaf4fdd7cbc321a4af0c.png)

To add a new database connection, click on the `Add Connection` button. Enter the necessary connection details in the
modal that opens up.

You can also edit or delete an existing connection by clicking on the `Edit Connection` or `Remove` button next to the
connection.

Image: [ Dynamic routing ](https://hasura.io/docs/assets/images/add-connection-f03e090a754bc7c1d3ba850065d266b6.png)

Adjust the connection template settings to suit your needs, then click `Update Connection Template` to save the changes.

You can add *connection set* and *connection template* for a database by adding their config to the `/metadata/databases/database.yaml` file:

```
-   name :  <db - name >
   kind :  postgres
   configuration :
     connection_info :
       database_url :
         from_env :  <DATABASE_URL_ENV >
       pool_settings :
         idle_timeout :   180
         max_connections :   50
         retries :   1
     connection_template :
       template :   |
        {{ if $.request.session?["x-hasura-role"] == "user" }}
          {{$.primary}}
        {{else}}
          {{$.connection_set.db_1}}
        {{ end }}
     connection_set :
       -   name :  db_1
         connection_info :
           database_url :
             from_env :  <DATABASE_URL_ENV >
```

Apply the Metadata by running:

`hasura metadata apply`

The *connection set* and *connection template* can be configured via the[ pg_add_source ](https://hasura.io/docs/latest/api-reference/metadata-api/source/#metadata-pg-add-source)Metadata API.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_add_source" ,
   "args" :   {
     "name" :   "db" ,
     "configuration" :   {
       "connection_info" :   {
         "database_url" :   {
           "from_env" :   "<DATABASE_URL_ENV>"
         } ,
         "pool_settings" :   {
           "idle_timeout" :   180 ,
           "max_connections" :   50 ,
           "retries" :   1
         }
       } ,
       "connection_template" :   {
         "template" :   "{{ if $.request.session?[\"x-hasura-role\"] == \"user\" }} {{$.primary}} {{else}} {{$.connection_set.db_1}} {{ end }}"
       } ,
       "connection_set" :   [
         {
           "name" :   "db_1" ,
           "connection_info" :   {
             "database_url" :   {
               "from_env" :   "<DATABASE_URL_ENV>"
             }
           }
         }
       ]
     }
   }
}
```

## Testing connection template​

Hasura offers a convenient way to test the connection template for a source through the Hasura Console, which simulates
an actual GraphQL request without hitting the database. The Hasura Console internally uses the Metadata API
([ pg_test_connection_template ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-test-connection-template)) for
this process. Alternatively, you can also test the connection template directly using the Metadata API.

- Console
- API


1. Navigate to the `Dynamic Routing` tab in the Edit Data Source page.
2. Click on `Validate` button next to the connection template you want to test.


Image: [ Dynamic DB routing ](https://hasura.io/docs/assets/images/validate-connection-template-0e7527d801701837d641ce1698d86e65.png)

1. Fill in the `Headers` , `Session Variables` , `Operation Type and Name` as needed for your test scenario.
2. Click the `Validate` button and the result will be displayed.
3. You can edit the connection template in the validate modal, the modified template will be updated in the previous
screen.


Image: [ Dynamic DB routing ](https://hasura.io/docs/assets/images/validate-connection-template-modal-aad3e888be9c61f09296d003bc570c31.png)

Request:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_test_connection_template" ,
   "args" :   {
     "source_name" :   "source_name" ,
     "request_context" :   {
       "headers" :   {
         "header_name" :   "header_value"
       } ,
       "session" :   {
         "session_var" :   "session_var_value"
       } ,
       "query" :   {
         "operation_type" :   "query" ,
         "operation_name" :   "op_name"
       }
     } ,
     "connection_template" :   {
         "template" :   "{{ if $.request.session?[\"x-hasura-role\"] == \"user\" }} {{$.primary}} {{else}} {{$.connection_set.db_1}} {{ end }}"
       }
   }
}
```

Success Response:

```
{
   "result" :   {
     "routing_to" :   "connection_set" ,
     "value" :   "connection_set_member_name"
   }
}
```

Note

 `connection_template` is an optional argument which has precedence over the connection template present in the source.
If `connection_template` is provided in the API, then the source's connection template will be ignored.

## Limitations​

### Postgres schema of connection set​

Hasura derives the GraphQL schema based on the primary connection only (i.e., `connection_info` ). The Postgres schema of
all members of `connection_set` should be identical to that of the primary connection. **Hasura does not make any checks
to ensure the Postgres schema consistency, and users should guarantee the same.** Also, you can only configure/update
the primary database on the Hasura Console. Other databases are not accessible via the Console.

Caution

A GraphQL request may result in a runtime exception when it is being executed on a member of the connection set that
differs in the Postgres schema from the primary connection.

### Event Triggers​

[ Hasura Event Triggers ](https://hasura.io/docs/latest/event-triggers/overview/)are triggered only for mutations executed on the primary
connection. Mutations routed to the members of the connection set will not trigger Event Triggers.

### Migrations​

Hasura[ CLI Migrations ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/)cannot be applied on a connection set member.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#introduction)
    - [ Connect with different database credentials ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#connect-with-different-database-credentials)

- [ No-stale reads when read replicas are configured ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#no-stale-reads-when-read-replicas-are-configured)

- [ Route to a specific shard or node group in a distributed database ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#route-to-a-specific-shard-or-node-group-in-a-distributed-database)
- [ How it works ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#how-it-works)
    - [ Connection set ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#connection-set)

- [ Connection template ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#connection-template)
- [ Setting up connection set and connection template ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#setting-up-connection-set-and-connection-template)
- [ Testing connection template ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#testing-connection-template)
- [ Limitations ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#limitations)
    - [ Postgres schema of connection set ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#postgres-schema-of-connection-set)

- [ Event Triggers ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#event-triggers)

- [ Migrations ](https://hasura.io/docs/latest/databases/database-config/dynamic-db-connection/#connection-template/#migrations)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)