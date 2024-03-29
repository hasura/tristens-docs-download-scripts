# Build Your Own Connector

You can build your own connector using one of our SDKs. Currently, we have the following available:

- [ Rust Data Connector SDK ](https://github.com/hasura/ndc-hub#rust-sdk)
- [ TypeScript Data Connector SDK ](https://github.com/hasura/ndc-sdk-typescript)


Alternatively, you can implement the NDC spec directly, or use the[ TypeScript connector ](https://github.com/hasura/ndc-typescript-deno)for simple functions and procedures.

## Create a Connector tutorial​

If you are interested in creating a connector, we have a series of video tutorials that walk you through the
process. We have these available in a repo you can[ check out here ](https://github.com/hasura/ndc-learn/tree/main).

## Examples​

### CSV Connector - Direct NDC Spec Implementation​

The NDC Specification documentation can be found[ here ](https://hasura.github.io/ndc-spec/overview.html)and a guide,
based on developing a connector for CSVs, can be found[ here ](https://hasura.github.io/ndc-spec/tutorial/index.html).
You can use this guide as a reference to build your own connector.

Limitations

Complex input types in procedures are not supported yet.

### Sendgrid Connector - Rust SDK​

An example of implementing the Sendgrid API can be found[ on GitHub here ](https://github.com/hasura/ndc-sendgrid/).

The architecture can be summarized as follows:

- The connector is designed to work via the[ hasura3 connector plugin ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/)deployment method.
- As with all connector-plugin connectors, the connector is built and run as defined in its[ Dockerfile ](https://github.com/hasura/ndc-sendgrid/blob/main/Dockerfile)
    - The `Dockerfile` :
        - Installs system dependencies

- Builds the Rust Cargo project

- Copies the release build

- Starts the server reading the configuration from `/config.json`

- The `Dockerfile` :
    - Installs system dependencies
- The connector is implemented using the[ Rust Data Connector SDK ](https://github.com/hasura/ndc-hub#rust-sdk)
    - The[ main entrypoint ](https://github.com/hasura/ndc-sendgrid/blob/main/crates/ndc-sendgrid/src/main.rs)uses the
SDK's `default_main` method invoked with our `SendGridConnector` implementation of the `Connector` trait.

- The most important aspects of this implementation are
    - Defining its `SendGridConfiguration` that includes its API Key.

- Exposing its `/schema`

- Providing a `/query` to list email templates

- Providing a `/mutation` to send emails

- The[ SendGrid API interactions ](https://github.com/hasura/ndc-sendgrid/blob/main/crates/ndc-sendgrid/src/sendgrid_api.rs)expose
    - `invoke_list_function_templates` , and

- `invoke_send_mail`

- The most important aspects of this implementation are
    - Defining its `SendGridConfiguration` that includes its API Key.

- The[ SendGrid API interactions ](https://github.com/hasura/ndc-sendgrid/blob/main/crates/ndc-sendgrid/src/sendgrid_api.rs)expose
    - `invoke_list_function_templates` , and
- With all this in place the connector can be used by referencing[ the repository ](https://github.com/hasura/ndc-sendgrid)and running the following command:
- The running connector can then:
    - Be referenced in Hasura v3 metadata

- Leveraged by the LSP

- Targeted by the engine

- Receive Translated GraphQL Queries


The connector is designed to work via the[ hasura3 connector plugin ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/)deployment method.

As with all connector-plugin connectors, the connector is built and run as defined in its[ Dockerfile ](https://github.com/hasura/ndc-sendgrid/blob/main/Dockerfile)

The connector is implemented using the[ Rust Data Connector SDK ](https://github.com/hasura/ndc-hub#rust-sdk)

With all this in place the connector can be used by referencing[ the repository ](https://github.com/hasura/ndc-sendgrid)and running the following command:

`hasura3 connector create sendgrid:v1 --github-repo-url https://github.com/hasura/ndc-sendgrid/tree/main --config-file config.json`

The running connector can then:

### Sendgrid Connector - Typescript Connector​

The[ TypeScript Connector ](https://github.com/hasura/ndc-typescript-deno/)provides a simple way to deploy TypeScript
functions as data connectors. **There is no need to implement an API, use an SDK, or write a Dockerfile.** Simply
provide a Typescript function to the Typescript Connector, and it will be deployed and executed within the[ Deno ](https://deno.com/)runtime.

As an example, we can write a Sendgrid connector consisting of the following two files:

 `functions/sendgrid.ts` :

```
import   {  sendSimpleMail ,  IResult  }   from   "https://deno.land/x/sendgrid@0.0.3/mod.ts" ;
export   async   function   send ( subject :   string ,  to :   string ,  from :   string ,  plain :   string ,  html :   string ) :   Promise < IResult >   {
   const   API_KEY   =  Deno . env . get ( "SENDGRID_API_KEY" ) ;
   if   ( ! API_KEY )   {
     throw   new   Error ( "Error: SENDGRID_API_KEY environment variable must be set." ) ;
   }
   const  response  =   await   sendSimpleMail (
     {
      subject ,
      to :   [ {  email :  to  } ] ,
      from :   {  email :  from  } ,
      content :   [
         {  type :   "text/plain" ,  value :  plain  } ,
         {  type :   "text/html" ,  value :  html  } ,
       ] ,
     } ,
     {
      apiKey :   API_KEY ,
     }
   ) ;
   return  response ;
}
```

 `config.json` :

```
{
   "typescript_source" :   "/functions/sendgrid.ts"
}
```

The file `config.json` tells the Typescript Connector where to find our Typescript function. The file `functions/sendgrid.ts` contains the function itself.

To deploy the connector you can use the command:

`hasura3 connector create sendgrid:deno:v1 --github-repo-url https://github.com/hasura/ndc-typescript-deno/tree/main --config-file config.json --volume ./functions:/functions --env  SENDGRID_API_KEY = 'YOUR_SENDGRID_API_KEY'`

The example code shown here can be found[ on GitHub ](https://github.com/hasura/ndc-sendgrid-deno).

### What did you think of this doc?

- [ Create a Connector tutorial ](https://hasura.io/docs/3.0/connectors/build-your-own-connector/#create-a-connector-tutorial)
- [ Examples ](https://hasura.io/docs/3.0/connectors/build-your-own-connector/#examples)
    - [ CSV Connector - Direct NDC Spec Implementation ](https://hasura.io/docs/3.0/connectors/build-your-own-connector/#csv-connector---direct-ndc-spec-implementation)

- [ Sendgrid Connector - Rust SDK ](https://hasura.io/docs/3.0/connectors/build-your-own-connector/#sendgrid-connector---rust-sdk)

- [ Sendgrid Connector - Typescript Connector ](https://hasura.io/docs/3.0/connectors/build-your-own-connector/#sendgrid-connector---typescript-connector)
