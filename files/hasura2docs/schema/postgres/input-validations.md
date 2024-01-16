# Postgres: Input Validations

## Introduction​

Supported from

Input validations are supported for versions `v2.29.0` and above.

Many times, we need to perform validations on the input arguments of a GraphQL mutation before inserting, deleting or
updating the data.

Hasura provides a way to add input validations to your GraphQL mutations which route the input arguments of a GraphQL
mutation to an HTTP webhook to perform complex validation logic.

### Example​

Consider you have the following GraphQL mutation:

```
mutation   insert_users   {
   insert_users ( objects :   [ {   name :   "John" ,   phone :   "999"   } ] )   {
     affected_rows
   }
}
mutation   update_users   {
   update_users ( where :   {   id :   {   _eq :   1   }   } ,   _set :   {   name :   "John" ,   email :   "random email"   } )   {
     affected_rows
   }
}
```

You can define the input validations for the above mutations to perform the following checks:

1. Check that the `name` field is not empty
2. Check that the `phone` field is a valid phone number
3. Check that the `email` field is a valid email address
4. Do not allow more than 5 insertions in a single insert mutation


## Setting up validation permissions​

- Console
- CLI
- API


You can define the input validations for `insert/update/delete` permissions on the Hasura Console in **Data -> [table]
-> Permissions -> (insert/update/delete)** .

Image: [ Using boolean expressions to build rules ](https://hasura.io/docs/assets/images/input-validation-create-permission-fa7453419abaa5ac06f883f67e1080fe.png)

You can define the input validations in the `metadata -> databases -> [database-name] -> tables -> [table-name].yaml` file, eg:

```
-   table :
     schema :  public
     name :  products
   insert_permissions :
     -   role :  user
       permission :
         columns :   [ ]
         filter :   { }
         validate_input :
           type :  http
           definition :
             url :  http : //www.somedomain.com/validateProducts
             headers :
               -   name :  X - Validate - Input - API - Key
                 value_from_env :  VALIDATION_HOOK_API_KEY
             forward_client_headers :   true
             timeout :   5
```

Apply the Metadata by running:

`hasura metadata apply`

You can define the input validations when using the[ permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/). Example with a Postgres DB:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_(insert|update|delete)_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "products" ,
     "role" :   "user" ,
     "permission" :   {
       "columns" :   "*" ,
       "filter" :   { } ,
       "validate_input" :   {
         "type" :   "http" ,
         "definition" :   {
           "forward_client_headers" :   true ,
           "headers" :   [ ] ,
           "timeout" :   10 ,
           "url" :   "http://www.somedomain.com/validateUser"
         }
       }
     }
   }
}
```

The `type` determines the interface for the input validation, which initially only supports an `http` webhook URL.

The `definition` field provides the necessary context for communicating and submitting the data for input validation. It
is an object with the following fields.

- `url` - *Required* , a[ string value ](https://hasura.io/docs/latest/api-reference/syntax-defs/#webhookurl)which
supports templating environment variables.
- `headers` - *Optional* , a list of headers to be sent to the URL.
- `forward_client_headers` - *Optional* , default is `false` . If set to `true` the client headers are forwarded to the
URL.
- `timeout` - *Optional* , default is `10` . The number of seconds to wait for a response before timing out.


Reduced performance

Mutations that involve input validation **may exhibit slower performance** compared to mutations without validation. The
execution time of the webhook URL can become a bottleneck, potentially reaching the maximum limit specified by the `timeout` configuration value, the default of which is 10 seconds.

## How it works​

Following are the steps that are performed by mutations types ( `insert/update/delete` )

When an mutation arrives with a role, the following steps are performed:

1. First, "collect" all the tables that the mutation targets (because there could be more than one table involved via
nested inserts)
2. If there is a `validate_input` permission defined on a table, then any mutation arguments targeting that table are
sent to the validation URL. This is done for all tables.
3. If all handlers validate the mutation arguments, then the request proceeds. **A transaction with the database will
only be started after the validation is completed and successful.**
4. If any webhook rejects the mutation data, then the request is aborted. An `error` message from the URL can also be
forwarded to the client.


Consider the following sample mutation:

```
mutation   insertAuthorWithArticles ( $name :   String ,   $email :   String ,   $articles_content :   [ article_insert_input ! ] ! )   {
   insert_author ( objects :   {   name :   $name ,   email :   $email ,   articles :   {   data :   $articles_content   }   } )   {
     returning   {
       first_name
       articles   {
         id
       }
     }
   }
}
```

The above mutation targets the `author` and `article` tables, involving a nested insert of an article into the author
model. Assuming that the `validate_input` permission is defined for both tables, the validation process unfolds as
follows:

1. The validation webhook specified for the `author` table is contacted first, including the inserted row with `articles`
2. Subsequently, the validation webhook designated for the `article` table is contacted with `$articles_content` rows.
3. If both of the above webhook calls result in successful validation, a database transaction is started to insert the
rows into the respective tables.


## Webhook specification per mutation type​

### Request​

When a mutation on a table with `validate_input` configuration is executed, before making a database transaction, Hasura
sends the mutation argument data to the validation HTTP webhook using a `POST` request.

The request payload is of the format:

```
{
     "version" :   "<version-integer>" ,
     "role" :   "<role-name>" ,
     "session_variables" :   {
         "x-hasura-user-id" :   "<session-user-id>" ,
         "x-hasura-user-name" :   "<session-user-name>"
     } ,
     "data" :   {
         "input" :  <mutation specific schema>
     }
}
```

- `version` : An integer version serves to indicate the request format. Whenever a breaking update occurs in the request
payload, the version will be incremented. The initial version is set to `1` .
- `role` : Hasura session role on which permissions are enforced.
- `session_variables` : Session variables that aid in enforcing permissions. Session variable names always starts with `x-hasura-*` .
- `data.input` : The schema of `data.input` varies per mutation type. This schema is defined below.


#### Insert Mutations​

```
{
     "version" :   "<version-integer>" ,
     "role" :   "<role-name>" ,
     "session_variables" :   { <session-variables> } ,
     "data" :   {
         "input" :   [ { JSON-fied <model_name>_insert_input! } ]
     }
}
```

- `data.input` : List of rows to be inserted which are specified in the `objects` input field of insert mutation. Also
includes nested data of relationships. The structure of this field will be similar to the JSONified structure of the `<model_name>_insert_input!` graphql type.


Note that, in `data.input` , if the data to be inserted contains nested inserts, then:

1. The `data.input` for the root model will have the type `JSON-fied <model_name>_insert_input!` , i.e: the nested
inserts will be present as `JSON-fied <model_name>_(arr|obj)_rel_insert_input!`
2. The `data.input` for the nested inserts payload will have the type `JSON-fied <nested_model_name>_insert_input!`


#### Update Mutations​

The user may want to validate the input values in the `where` , `_set` , `_inc` etc clause and `pk_columns` . So, the
upstream webhook is expected to receive those values in the payload.

```
{
     "version" :   "<version-integer>" ,
     "role" :   "<role-name>" ,
     "session_variables" :   { <session-variables> } ,
     "data" :   {
       "input" :   [
         {
          JSON-fied <model_name>_updates! ,
           "pk_columns" :  JSON-fied <model_name>_pk_columns_input! (only included for update_<mode_name>_by_pk)
         }
       ]
     }
}
```

- `data.input` : List of the multiple updates to run. The structure of this field will be similar to the JSONified
structure of the `<model_name>_updates!` graphql type. If it is an update mutation by primary key, then it will also
contain the `<model_name>_pk_columns_input!`


#### Delete Mutations​

The user may want to validate the input values in the `where` clause and `pk_columns` . So the upstream webhook is
expected to receive those values in the payload.

```
{
     "version" :   "<version-integer>" ,
     "role" :   "<role-name>" ,
     "session_variables" :   { <session-variables> } ,
     "data" :   {
       "input" :   [
         {
            JSON-fied <model_name>_bool_exp! ,
             "pk_columns" :  JSON-fied <model_name>_pk_columns_input! (only included for delete_<mode_name>_by_pk)
         }
       ]
     }
}
```

- `data.input` : The delete condition. The structure of this field will be similar to the JSONified structure of the `<model_name>_bool_exp!` graphql type. If it is a delete mutation by primary key, then it will also contain the `<model_name>_pk_columns_input!`


### Response​

The following is the expected response from the upstream webhook for all mutation types ( `insert/update/delete` ).

1. **Successful Response**


The HTTP validation URL should return a `200` status code to represent a successful validation.

`200 OK`

1. **Failed Response**


The HTTP validation URL should return an optional JSON object with `400` status code to represent a failed validation.
The object should contain a `message` field whose value is a string and this message is forwarded to client.

If no JSON object is returned then no message is forwarded to client.

```
400 BAD REQUEST
{
    "message": "Phone number invalid"
}
```

 **When an unexpected response format is received, Hasura raises internal exception** 

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/input-validations/#introduction)
    - [ Example ](https://hasura.io/docs/latest/schema/postgres/input-validations/#example)
- [ Setting up validation permissions ](https://hasura.io/docs/latest/schema/postgres/input-validations/#setting-up-validation-permissions)
- [ How it works ](https://hasura.io/docs/latest/schema/postgres/input-validations/#how-it-works)
- [ Webhook specification per mutation type ](https://hasura.io/docs/latest/schema/postgres/input-validations/#webhook-specification-per-mutation-type)
    - [ Request ](https://hasura.io/docs/latest/schema/postgres/input-validations/#request)

- [ Response ](https://hasura.io/docs/latest/schema/postgres/input-validations/#response)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)