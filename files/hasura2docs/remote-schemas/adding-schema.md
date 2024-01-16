# Add a Remote Schema

## Introduction​

Follow the steps below to merge your remote GraphQL API with the GraphQL Engine's auto-generated API.

## Step 1: Write a custom GraphQL server​

 *You can skip this step if you are using a 3rd party GraphQL API or already have a functional GraphQL server that meets
your requirements.* 

You need to create a custom GraphQL server with a schema and corresponding resolvers that solve your use case.

You can use any language/framework of your choice to author this server and deploy it anywhere. A great way to get
started is to use one of our[ boilerplates ](https://github.com/hasura/graphql-engine/tree/master/community/boilerplates/remote-schemas).

## Step 2: Merge Remote Schema​

The following details need to be specified for merging a Remote Schema:

- **Remote Schema name** : an alias for the Remote Schema that must be unique on an instance of the GraphQL Engine.
- **GraphQL server URL** : the endpoint at which your remote GraphQL server is available. This value can be entered
manually or by specifying an environment variable that contains this information.
- **Headers** : configure the headers to be sent to your custom GraphQL server:
    - Toggle forwarding all headers sent by the client (when making a GraphQL query) to your remote GraphQL server.

- Send additional headers to your remote server - these can be static header name-value pairs; and/or pairs of "header
name-environment variable name". You can specify the value of the header to be picked up from the environment
variable. **Example** : Let's say your remote GraphQL server needs a `X-Api-Key` as a header. As this value contains sensitive
data (like API key in this example), you can configure the name of an environment variable which will hold the
value. This environment variable needs to be present when you start the GraphQL Engine. When Hasura sends requests
to your remote server, it will pick up the value from this environment variable.


 **Remote Schema name** : an alias for the Remote Schema that must be unique on an instance of the GraphQL Engine.

 **GraphQL server URL** : the endpoint at which your remote GraphQL server is available. This value can be entered
manually or by specifying an environment variable that contains this information.

 **Headers** : configure the headers to be sent to your custom GraphQL server:

Toggle forwarding all headers sent by the client (when making a GraphQL query) to your remote GraphQL server.

Send additional headers to your remote server - these can be static header name-value pairs; and/or pairs of "header
name-environment variable name". You can specify the value of the header to be picked up from the environment
variable.

 **Example** : Let's say your remote GraphQL server needs a `X-Api-Key` as a header. As this value contains sensitive
data (like API key in this example), you can configure the name of an environment variable which will hold the
value. This environment variable needs to be present when you start the GraphQL Engine. When Hasura sends requests
to your remote server, it will pick up the value from this environment variable.

- Console
- CLI
- API


Head to the `Remote Schemas` tab of the Console and click on the `Add` button on the left sidebar.

Add the required details and click on the `Add Remote Schema` button to merge the Remote Schema.

Image: [ Merge Remote Schema ](https://hasura.io/docs/assets/images/add-remote-schemas-interface-27e0eaec7186ca0e42015698e4951493.png)

To add a Remote Schema, edit the `remote_schemas.yaml` file in the `metadata` directory as in this example:

```
-   name :  my - remote - schema
   definition :
     url :  https : //graphql - pokemon.now.sh/
     timeout_seconds :   60
     forward_client_headers :   true
```

Apply the Metadata by running:

`hasura metadata apply`

You can add a Remote Schema by using the[ add_remote_schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-schemas/#metadata-add-remote-schema)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "add_remote_schema" ,
     "args" :   {
         "name" :   "my-remote-schema" ,
         "definition" :   {
             "url" :   "https://graphql-pokemon.now.sh/" ,
             "forward_client_headers" :   true ,
             "timeout_seconds" :   60
         }
     }
}
```

Note

If you are running Hasura using Docker, ensure that the Hasura Docker container can reach the server endpoint. See[ this page ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-networking)for Docker networking.

If you are adding the URL using env variable, then run the Hasura docker container with the env variable added during *docker run* . Example `-e REMOTE_SCHEMA_ENDPOINT=http://host.docker.internal:4000/mycustomgraphql` .

Using environment variables

If you are using environment variables in the Remote Schema configuration - either for URL or headers - **the
environment variables need to be present** with valid values when adding the Remote Schema i.e. the GraphQL Engine
should be started with these environment variables.

## Step 3: Make queries to the remote server from Hasura​

- Via Console
- Via API


Now you can head to the `API` tab and make queries to your remote server from Hasura.

You can query your remote server by making requests to the Hasura GraphQL endpoint ( `/v1/graphql` ).

## Points to remember​

### Remote Schema fields nomenclature​

- Top-level field names need to be unique across all merged schemas ( *case-sensitive match* ).
- Types with the *exact same name and structure* will be merged. But types with the *same name but different structure* will result in type conflicts.


### Schema refreshing​

A remote server's GraphQL schema is cached and refreshed only when user explicitly reloads the Remote Schema.

- Console
- API


Head to `Remote Schemas -> [remote_schema_name] -> Details` and click the `Reload` button.

Make a request to the[ reload_remote_schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-schemas/#metadata-reload-remote-schema)Metadata API.

### Current limitations​

- Subscriptions on remote GraphQL servers are not supported.


### Extending the auto-generated GraphQL schema fields​

For some use cases, you may need to extend the GraphQL schema fields exposed by the Hasura GraphQL Engine and not merely
add new fields as we have done here.

To achieve this you can use community tooling to write your own client-facing GraphQL gateway which wraps around and
interacts with the GraphQL Engine API underneath.

Note

 **Adding an additional layer on top of the Hasura GraphQL Engine significantly impacts the performance provided by it
out of the box** ( *by as much as 4x* ). If you need any help with remodeling these kinds of use cases to use the built-in
Remote Schemas feature, please get in touch with us on[ GitHub ](https://github.com/hasura/graphql-engine/discussions).

Additional Resources

Data Federation with Hasura -[ Watch Webinar ](https://hasura.io/events/webinar/data-federation-hasura-graphql/?pg=docs&plcmt=body&cta=watch-webinar&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/remote-schemas/adding-schema/#introduction)
- [ Step 1: Write a custom GraphQL server ](https://hasura.io/docs/latest/remote-schemas/adding-schema/#step-1-write-a-custom-graphql-server)
- [ Step 2: Merge Remote Schema ](https://hasura.io/docs/latest/remote-schemas/adding-schema/#merge-remote-schema)
- [ Step 3: Make queries to the remote server from Hasura ](https://hasura.io/docs/latest/remote-schemas/adding-schema/#step-3-make-queries-to-the-remote-server-from-hasura)
- [ Points to remember ](https://hasura.io/docs/latest/remote-schemas/adding-schema/#points-to-remember)
    - [ Remote Schema fields nomenclature ](https://hasura.io/docs/latest/remote-schemas/adding-schema/#remote-schema-fields-nomenclature)

- [ Schema refreshing ](https://hasura.io/docs/latest/remote-schemas/adding-schema/#schema-refreshing)

- [ Current limitations ](https://hasura.io/docs/latest/remote-schemas/adding-schema/#current-limitations)

- [ Extending the auto-generated GraphQL schema fields ](https://hasura.io/docs/latest/remote-schemas/adding-schema/#extending-the-auto-generated-graphql-schema-fields)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)