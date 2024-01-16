# Create Actions

## Introduction​

An action is a GraphQL query or mutation. You have to define the GraphQL type of the arguments that the query or
mutation accepts and the GraphQL type of its response.

To create an action, you have to:

1. Define the query or mutation
2. Define the required types
3. Create a handler


Let's look at **examples** for mutation and query type Actions.

## Setup​

- Console
- CLI
- API


There is no setup required for defining Actions via the Console.

[ Install ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/)or[ update to ](https://hasura.io/docs/latest/hasura-cli/commands/hasura_update-cli/)the latest
version of Hasura CLI.

You can either get started with an existing project or create a new project.

 **For a new project** 

`hasura init`

This will create a new project. You can set up your GraphQL Engine endpoint (and admin secret if it exists) in the `config.yaml` .

Run `hasura metadata export` so that you get server's Metadata into the `metadata/` directory.

 **For existing projects** 

Actions are supported only in the v2 config of the CLI. Check the `config.yaml` of your Hasura Project for the `version` key.

If you see `version: 1` (or do not see a version key), upgrade to version 2 by running:

`hasura scripts update-config-v2`

Run `hasura metadata export` so that you get server's Metadata into the `metadata/` directory.

There is no setup required for defining Actions via the[ Actions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/).

## Mutation type action​

Let's start with a mutation that accepts a username and password, and returns an access token. We'll call this mutation `login` .

- [ Step 1: Define your mutation and associated types ](https://hasura.io/docs/latest/actions/create/#step-1-define-your-mutation-and-associated-types)
- [ Step 2: Create the action handler ](https://hasura.io/docs/latest/actions/create/#step-2-create-the-action-handler)
- [ Step 3: Finish action creation ](https://hasura.io/docs/latest/actions/create/#step-3-finish-action-creation)
- [ Step 4: Try it out ](https://hasura.io/docs/latest/actions/create/#step-4-try-it-out)


### Step 1: Define your mutation and associated types​

Start with defining the mutation and the required types. These types will reflect in the GraphQL schema.

- Console
- CLI
- API


Go to the `Actions` tab on the Console and click on `Create` . This will take you to a page like this:

Image: [ Console Action create ](https://hasura.io/docs/assets/images/mutation-action-create-04d2a073b48455e14cbcdb54bf2284c5.png)

Define the Action as follows in the `Action Definition` editor.

```
type   Mutation   {
   login ( username :   String ! ,   password :   String ! ) :   LoginResponse
}
```

In the above action, we called the returning object type to be `LoginResponse` . Define it in the `New types definition` as:

```
type   LoginResponse   {
   accessToken :   String !
}
```

To create an action, run

`hasura actions create login`

This will open up an editor with `metadata/actions.graphql` . You can enter the action's mutation definition and the
required types in this file. For your `login` mutation, replace the content of this file with the following and save:

```
type   Mutation   {
   login ( username :   String ! ,   password :   String ! ) :   LoginResponse
}
type   LoginResponse   {
   accessToken :   String !
}
```

It is essential that the custom types used in the action are defined *beforehand* via the[ set_custom_types ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-types/#metadata-set-custom-types)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "set_custom_types" ,
   "args" :   {
     "scalars" :   [ ] ,
     "enums" :   [ ] ,
     "input_objects" :   [ ] ,
     "objects" :   [
       {
         "name" :   "LoginResponse" ,
         "fields" :   [
           {
             "name" :   "accessToken" ,
             "type" :   "String!"
           }
         ]
       }
     ]
   }
}
```

Once the custom types are defined, we can create an action via the[ create_action Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action):

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "create_action" ,
   "args" :   {
     "name" :   "Login" ,
     "definition" :   {
       "kind" :   "synchronous" ,
       "type" :   "mutation" ,
       "arguments" :   [
         {
           "name" :   "username" ,
           "type" :   "String!"
         } ,
         {
           "name" :   "password" ,
           "type" :   "String!"
         }
       ] ,
       "output_type" :   "LoginResponse" ,
       "handler" :   "https://hasura-actions-demo.glitch.me/login"
     }
   }
}
```

The above definition means:

- This action will be available in your GraphQL schema as a mutation called `login` .
- It accepts two arguments called `username` and `password` of type `String!` .
- It returns an output type called `LoginResponse` .
- `LoginResponse` is a simple object type with a field called `accessToken` of type `String!` .


Note

When using a[ numeric ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#numeric)value in an[ Action ](https://hasura.io/docs/latest/actions/overview/), the
value is[ coerced ](https://spec.graphql.org/October2021/#sec-Scalars.Input-Coercion)to its expected scalar type based
on type of the input value supplied (from the Action payload). As stated in the spec, a GraphQL service (such as Hasura)
will attempt to coerce numeric values to `Int` , `Float` , or `String` types, so long as its reasonable and doesn't result
in the loss of data. Otherwise, the service will throw an error.

### Step 2: Create the action handler​

A handler is an HTTP webhook where you can perform the custom logic for the action.

In this case, we will just return an access token, but typically you would want to run all the business logic that the
action demands. NodeJS/Express code for this handler would look something like:

```
const   handler   =   ( req ,  resp )   =>   {
   // You can access their arguments input at req.body.input
   const   {  username ,  password  }   =  req . body . input ;
   // perform your custom business logic
   // check if the username and password are valid and login the user
   // return the response
   return  resp . json ( {
     accessToken :   'Ew8jkGCNDGAo7p35RV72e0Lk3RGJoJKB' ,
   } ) ;
} ;
```

You can deploy this code somewhere and get the URI. For getting started quickly, we also have this handler ready at `https://hasura-actions-demo.glitch.me/login` .

 **Set the handler** 

Now, set the handler for the action:

- Console
- CLI
- API


Set the value of the `handler` field to the above endpoint.

Go to `metadata/actions.yaml` . You must see a handler like `http://localhost:3000` or `http://host.docker.internal:3000` under the action named `login` . This is a default value taken from `config.yaml` . Update the `handler` to the above
endpoint.

The action handler must be set when creating an action via the[ create_action Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action).

It can be updated later by using the[ update_action Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-update-action).

URL templating

To manage handler endpoints across environments it is possible to template the endpoints using ENV variables.

e.g. `https://my-handler-endpoint/addNumbers` can be templated to `{{ACTION_BASE_ENDPOINT}}/addNumbers` where `ACTION_BASE_ENDPOINT` is an ENV variable whose value is set to `https://my-handler-endpoint` 

Note

If you are running Hasura using Docker, ensure that the Hasura Docker container can reach the handler endpoint. See[ this page ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-networking)for Docker networking.

### Step 3: Finish action creation​

Finally, to save the action:

- Console
- CLI
- API


Hit `Create` .

Run `hasura metadata apply` .

An action will be created when sending a request to the[ create_action Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action).

### Step 4: Try it out​

In the Hasura Console, head to the `API` tab and try out the new action.

And that's it. You have extended your Hasura schema with a new mutation.

## Query type action​

Let's start with a basic query that accepts a list of numbers and returns their sum. We'll call this query `addNumbers` .

- [ Step 1: Define your query and associated types ](https://hasura.io/docs/latest/actions/create/#step-1-define-your-query-and-associated-types)
- [ Step 2: Create the action handler ](https://hasura.io/docs/latest/actions/create/#step-2-create-the-action-handler-1)
- [ Step 3: Finish action creation ](https://hasura.io/docs/latest/actions/create/#step-3-finish-action-creation-1)
- [ Step 4: Try it out ](https://hasura.io/docs/latest/actions/create/#step-4-try-it-out-1)


### Step 1: Define your query and associated types​

Start with defining the query and the required types. These types will reflect in the GraphQL schema.

- Console
- CLI
- API


Go to the `Actions` tab on the Console and click on `Create` . This will take you to a page like this:

Image: [ Console action create ](https://hasura.io/docs/assets/images/query-action-create-7c21d3c68bafe136d255f6f7d23191ad.png)

Define the Action as follows in the `Action Definition` editor.

```
type   Query   {
   addNumbers ( numbers :   [ Int ] ) :   AddResult
}
```

In the above action, we called the returning object type to be `AddResult` . Define it in the `New types definition` as:

```
type   AddResult   {
   sum :   Int
}
```

To create an action, run

`hasura actions create addNumbers`

This will open up an editor with `metadata/actions.graphql` . You can enter the action's query definition and the
required types in this file. For your `addNumbers` query, replace the content of this file with the following and save:

```
type   Query   {
   addNumbers ( numbers :   [ Int ] ) :   AddResult
}
type   AddResult   {
   sum :   Int
}
```

It is essential that the custom types used in the action are defined *beforehand* via the[ set_custom_types ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-types/#metadata-set-custom-types)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "set_custom_types" ,
   "args" :   {
     "scalars" :   [ ] ,
     "enums" :   [ ] ,
     "input_objects" :   [ ] ,
     "objects" :   [
       {
         "name" :   "AddResult" ,
         "fields" :   [
           {
             "name" :   "sum" ,
             "type" :   "Int!"
           }
         ]
       }
     ]
   }
}
```

Once the custom types are defined, we can create an action via the[ create_action Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action):

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "create_action" ,
     "args" :   {
       "name" : "addNumbers" ,
       "definition" :   {
         "kind" : "synchronous" ,
         "type" :   "query" ,
         "arguments" : [
           {
             "name" : "numbers" ,
             "type" : "[Int]!"
           }
         ] ,
         "output_type" : "AddResult" ,
         "handler" : "https://hasura-actions-demo.glitch.me/addNumbers"
     }
   }
}
```

The above definition means:

- This action will be available in your GraphQL schema as a query called `addNumbers`
- It accepts an argument called `numbers` which is a list of integers.
- It returns an output type called `AddResult` .
- `AddResult` is a simple object type with a field called `sum` of type integer.


Note

When using a[ numeric ](https://hasura.io/docs/latest/schema/postgres/postgresql-types/#numeric)value in an[ Action ](https://hasura.io/docs/latest/actions/overview/), the
value is[ coerced ](https://spec.graphql.org/October2021/#sec-Scalars.Input-Coercion)to its expected scalar type based
on type of the input value supplied (from the Action payload). As stated in the spec, a GraphQL service (such as Hasura)
will attempt to coerce numeric values to `Int` , `Float` , or `String` types, so long as its reasonable and doesn't result
in the loss of data. Otherwise, the service will throw an error.

You can also use Type Generator feature to generate the types for your Action:

Image: [ Console Action create ](https://hasura.io/docs/assets/images/type-generator-d230f7fd55deb579131c5f29c78e6cc8.png)

Insert JSON samples for the request and the response, click "Insert Types" and Hasura generates the GraphQL types for
you.

### Step 2: Create the action handler​

A handler is an HTTP webhook where you can perform the custom logic for the action.

In this case, it is the addition of the numbers. NodeJS/Express code for this handler would look something like:

```
const   handler   =   ( req ,  resp )   =>   {
   // You can access their arguments input at req.body.input
   const   {  numbers  }   =  req . body . input ;
   // perform your custom business logic
   // return an error or response
   try   {
     return  resp . json ( {
       sum :  numbers . reduce ( ( s ,  n )   =>  s  +  n ,   0 ) ,
     } ) ;
   }   catch   ( e )   {
     console . error ( e ) ;
     return  resp . status ( 500 ) . json ( {
       message :   'unexpected' ,
     } ) ;
   }
} ;
```

You can deploy this code somewhere and get the URI. For getting started quickly, we also have this handler ready at `https://hasura-actions-demo.glitch.me/addNumbers` .

 **Set the handler** 

Now, set the handler for the action:

- Console
- CLI
- API


Set the value of the `handler` field to the above endpoint.

Go to `metadata/actions.yaml` . You must see a handler like `http://localhost:3000` or `http://host.docker.internal:3000` under the action named `addNumbers` . This is a default value taken from `config.yaml` .

Update the `handler` to the above endpoint.

The action handler must be set when creating an action via the Once the custom types are defined, we can create an
action via the[ create_action Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action).

It can be updated later by using the[ update_action Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-update-action).

URL templating

To manage handler endpoints across environments it is possible to template the endpoints using ENV variables.

e.g. `https://my-handler-endpoint/addNumbers` can be templated to `{{ACTION_BASE_ENDPOINT}}/addNumbers` where `ACTION_BASE_ENDPOINT` is an ENV variable whose value is set to `https://my-handler-endpoint` 

### Step 3: Finish action creation​

Finally, to save the action:

- Console
- CLI
- API


Hit `Create` .

Run `hasura metadata apply` .

An action will be created when sending a request to the[ create_action Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action).

### Step 4: Try it out​

In the Hasura Console, head to the `API` tab and try out the new action.

And that's it. You have extended your Hasura schema with a new query.

Additional Resources

Introduction to Hasura Actions -[ View Recording ](https://hasura.io/events/webinar/hasura-actions/?pg=docs&plcmt=body&cta=view-recording&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/actions/create/#introduction)
- [ Setup ](https://hasura.io/docs/latest/actions/create/#setup)
- [ Mutation type action ](https://hasura.io/docs/latest/actions/create/#mutation-type-action)
    - [ Step 1: Define your mutation and associated types ](https://hasura.io/docs/latest/actions/create/#step-1-define-your-mutation-and-associated-types)

- [ Step 2: Create the action handler ](https://hasura.io/docs/latest/actions/create/#step-2-create-the-action-handler)

- [ Step 3: Finish action creation ](https://hasura.io/docs/latest/actions/create/#step-3-finish-action-creation)

- [ Step 4: Try it out ](https://hasura.io/docs/latest/actions/create/#step-4-try-it-out)
- [ Query type action ](https://hasura.io/docs/latest/actions/create/#query-type-action)
    - [ Step 1: Define your query and associated types ](https://hasura.io/docs/latest/actions/create/#step-1-define-your-query-and-associated-types)

- [ Step 2: Create the action handler ](https://hasura.io/docs/latest/actions/create/#step-2-create-the-action-handler-1)

- [ Step 3: Finish action creation ](https://hasura.io/docs/latest/actions/create/#step-3-finish-action-creation-1)

- [ Step 4: Try it out ](https://hasura.io/docs/latest/actions/create/#step-4-try-it-out-1)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)