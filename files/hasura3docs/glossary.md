# Hasura DDN Glossary

## Data Delivery Network (DDN)​

Hasura DDN is a globally distributed and always-available cloud for APIs and data connectivity which enables
blazingly-fast and secure delivery of real-time data over GraphQL or REST APIs. It is powered by innovations in Hasura
version 3 including a serverless runtime and the new OpenDD metadata specification.

## Serverless Runtime System​

The new runtime engine in Hasura DDN which accesses metadata on a per-request basis, enabling improved isolation and
scalability. The serverless runtime also eliminates shared state and cold start issues for enhanced performance.

## Metadata Authoring​

The process of defining and creating metadata files using the OpenDD and Native Data Connector specifications in Hasura
DDN. It involves specifying data types, models, commands, data source and API configurations. Learn[ more ](https://hasura.io/docs/3.0/data-domain-modeling/overview/).

## Open Data Domain Specification (OpenDD Spec)​

A standardized specification that defines the metadata structure for APIs in Hasura DDN. The OpenDD spec includes typed
metadata objects such as types, models, commands, data sources, functions and API configurations. Learn[ more ](https://hasura.io/docs/3.0/data-domain-modeling/overview/).

## Data Sources​

Any external data source, database, or service that can be connected to Hasura DDN using a Data Connector agent. Every
data source must have connector URL and schema.[ Learn more ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/).

## Native Data Connector Specification (NDC Spec)​

A standardized specification that allows you to extend the functionality of the Hasura server by providing web services
which can resolve new sources of data that defines the metadata structure for APIs in Hasura DDN. All data backends in
Hasura DDN conform to this backend and use types defined by this specification such as collections, functions and
procedures. Learn[ more ](https://hasura.github.io/ndc-spec/).

## Native Data Connector Agents​

Data connector agents that integrate Hasura with various external data sources and services and are based on the native
data connector specification. Native data connectors can be either official Hasura connectors, verified by Hasura or a
non-verified connector.[ Learn more ](https://hasura.io/docs/3.0/connectors/overview/).

## Push-Down Capabilities​

The ability in Hasura DDN to delegate certain query operations including Authorization to the underlying data source.
This can improve query optimization and performance and is the reason why data connectors in Hasura DDN are called
'native'.

## Connector Hub​

Refers to the public site where all Native Data Connectors for Hasura DDN are listed. Users can discover connectors, get
more information about their specific features and find documentation on how to use each connector with Hasura DDN.[ Learn more ](https://hasura.io/connectors/).

## Model​

An OpenDD metadata object that is fundamental to API design in Hasura DDN. The model is the entity that has a direct
mapping to the underlying native data connector schema object or collection.

A model includes reference to the data type and includes configuration details related to API configuration, arguments
and global ids.

It supports select, insert, update and delete operations. Within the select operation the different query operations
include filtering, aggregating, paginating and limiting.[ Learn more ](https://hasura.io/docs/3.0/data-domain-modeling/models/).

## Command​

The Hasura entity that helps encapsulate business logic and represents an action that can be performed which returns
back some type of result. It directly maps to the native data connector object's functions and procedures.[ Learn more ](https://hasura.io/docs/3.0/data-domain-modeling/commands/).

## Relationships​

An OpenDD metadata object in Hasura DDN that defines the relationship between two models or between a model and a
command. This facilitates data interconnection.[ Learn more ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/).

## Permissions​

An OpenDD metadata object in Hasura DDN that defines the access control or authorization rules on models and commands.[ Learn more ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/).

## Global ID​

Refers to the Relay global ID that encodes the type and ID of an object in a single string. In Hasura this is defined
per model and enables fetching any object directly, regardless of what kind of object it is. A result of this is that
you get the node root field in the GraphQL API schema to use with a Relay client.[ Learn more ](https://hasura.io/docs/3.0/data-domain-modeling/global-id/).

## Collection​

A collection is a native data connector spec object that maps one-to-one with the underlying data source object.
Tracking a collection results in the creation of a model OpenDD object in Hasura metadata.

It can be queried or mutated and contains name, arguments and object types.[ Learn more ](https://hasura.github.io/ndc-spec/specification/schema/collections.html).

## Function​

A function is a native data connector specification object and is a special type of collection. It only returns a
single row and a single column, can contain arguments and cannot be mutated.

Tracking a function results in the creation of a `Command` OpenDD object in Hasura metadata.[ Learn more ](https://hasura.github.io/ndc-spec/specification/schema/functions.html).

## Procedure​

A procedure is a native data connector specification object, and it defines an action that the data connector
implements. Each procedure has arguments and a return type.

Tracking a procedure results in the creation of a `Command` OpenDD object in Hasura metadata.[ Learn more ](https://hasura.github.io/ndc-spec/specification/schema/procedures.html).

## Builds​

Each metadata change in Hasura DDN represents an immutable build. Every build has a unique GraphQL Endpoint that can be
tested independently. Builds are tied to projects and there is a one-to-many mapping between projects and builds.[ Learn more ](https://hasura.io/docs/3.0/ci-cd/overview/).

## Subgraphs​

In Hasura DDN, Subgraphs provide autonomy, separation and security to teams for working with project metadata and allow
them to organize and structure metadata as per team and business requirements. There can be multiple subgraphs in a
project.

All subgraphs contribute to one build at any given time, ie: one subgraph can be used create a build only when it does
not introduce a breaking change at the project level.[ Learn more ](https://hasura.io/docs/3.0/data-domain-modeling/overview/).

## Hasura CLI (Command-Line Interface)​

A tool in Hasura DDN that enables developers to interact with Hasura from the command line. It supports various commands
for creating builds, deploying projects, creating tunnels and managing secrets.[ Learn more ](https://hasura.io/docs/3.0/cli/overview/).

## LSP (language server protocol)​

The Hasura Language Server Protocol (LSP) enables the integration of language features such as tracking data source
objects, validation of metadata, providing diagnostics at the time of authoring and helping autocomplete metadata.

It supports `.hml` files which are a Hasura variant of `.yaml` files. We have used the Hasura LSP to build our[ VSCode extension ](https://marketplace.visualstudio.com/items?itemName=HasuraHQ.hasura)which you can download to help
you write metadata. We have plans to provide extensions such as these for other text editors.

## Hasura Secure Connect​

A feature in Hasura DDN that creates secure tunnels to connect with local resources, aiding local development while
ensuring data security. It requires a local daemon to be run via the CLI.

## Hasura Console​

An interface in Hasura DDN that provides tools for metadata visualizing, API testing and deployment, and team
collaboration. It offers tools to validate metadata before creating builds and metrics and traces to determine the usage
and health of the API.

## Secrets​

A secret is an object that contains small amounts of sensitive information such as database connection strings. It is
best practice to first create secrets using the Hasura CLI or Console and then use those secrets in the metadata.

## Cloud PAT​

This refers to a personal authentication token that Hasura Cloud creates automatically for you on every new project
creation. This ensures that your GraphQL API always has a security mechanism. The auto-generated PAT is included in the
API header `cloud_pat` .

### What did you think of this doc?

- [ Data Delivery Network (DDN) ](https://hasura.io/docs/3.0/glossary/#data-delivery-network-ddn)
- [ Serverless Runtime System ](https://hasura.io/docs/3.0/glossary/#serverless-runtime-system)
- [ Metadata Authoring ](https://hasura.io/docs/3.0/glossary/#metadata-authoring)
- [ Open Data Domain Specification (OpenDD Spec) ](https://hasura.io/docs/3.0/glossary/#open-data-domain-specification-opendd-spec)
- [ Data Sources ](https://hasura.io/docs/3.0/glossary/#data-sources)
- [ Native Data Connector Specification (NDC Spec) ](https://hasura.io/docs/3.0/glossary/#native-data-connector-specification-ndc-spec)
- [ Native Data Connector Agents ](https://hasura.io/docs/3.0/glossary/#native-data-connector-agents)
- [ Push-Down Capabilities ](https://hasura.io/docs/3.0/glossary/#push-down-capabilities)
- [ Connector Hub ](https://hasura.io/docs/3.0/glossary/#connector-hub)
- [ Model ](https://hasura.io/docs/3.0/glossary/#model)
- [ Command ](https://hasura.io/docs/3.0/glossary/#command)
- [ Relationships ](https://hasura.io/docs/3.0/glossary/#relationships)
- [ Permissions ](https://hasura.io/docs/3.0/glossary/#permissions)
- [ Global ID ](https://hasura.io/docs/3.0/glossary/#global-id)
- [ Collection ](https://hasura.io/docs/3.0/glossary/#collection)
- [ Function ](https://hasura.io/docs/3.0/glossary/#function)
- [ Procedure ](https://hasura.io/docs/3.0/glossary/#procedure)
- [ Builds ](https://hasura.io/docs/3.0/glossary/#builds)
- [ Subgraphs ](https://hasura.io/docs/3.0/glossary/#subgraphs)
- [ Hasura CLI (Command-Line Interface) ](https://hasura.io/docs/3.0/glossary/#hasura-cli-command-line-interface)
- [ LSP (language server protocol) ](https://hasura.io/docs/3.0/glossary/#lsp-language-server-protocol)
- [ Hasura Secure Connect ](https://hasura.io/docs/3.0/glossary/#hasura-secure-connect)
- [ Hasura Console ](https://hasura.io/docs/3.0/glossary/#hasura-console)
- [ Secrets ](https://hasura.io/docs/3.0/glossary/#secrets)
- [ Cloud PAT ](https://hasura.io/docs/3.0/glossary/#cloud-pat)
