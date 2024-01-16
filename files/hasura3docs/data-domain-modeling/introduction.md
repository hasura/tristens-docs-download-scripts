# Introduction

Hasura v3 introduces the OpenDD specification for constructing a supergraph. The metadata for Hasura v3 is an extension of the OpenDD spec, and adds some Hasura-specific configuration on top of OpenDD.

The OpenDD metadata defines the data model for each subgraph, including the types of the data objects, models and commands used to interact with the data, and access control rules on this data.
This data model is then combined with Native Data Connector agents, which are services to communicate with the raw data sources (like a database) in order to server your API.

## How is this different from Hasura v2 metadata?​

- Hasura V2 metadata was specifically designed for Hasura, whereas OpenDD is a general specification for modeling a data supergraph usable by anyone.
The bits of configuration in Hasura v3 metadata that are specific to Hasura reside outside of the OpenDD spec.
- Functionally, the V2 metadata relied directly on the raw data source for information like columns and fields, whereas
OpenDD metadata is independent of the data source. In OpenDD, all fields and types are explicitly defined within the
metadata itself which eliminates the necessity for data source schema introspection at startup to generate a
GraphQL schema. Also, the v3 metadata is still semantically consistent even if the underlying data source has changed.
- Compared to the v2 metadata, there is a lot more flexibility offered by OpenDD when configuring your GraphQL API.


## The OpenDD spec​

The OpenDD spec lets you define the following to configure your data graph:

- Data Connectors - that will be used to access the raw sources of data.
- Data types - using the OpenDD type system to give strong types to your data.
- Models - collections of data objects that can be queried. These server as the interface for querying your data.
- Commands - opaque functions or procedures that can be used to query or mutate data.
- Relationships - creating edges in your graph from a data type to a model or a command.
- Permissions - access control rules on your types / models / commands.


In this way, your data graph is decoupled from any underlying database, data source or other physical
layer of storage. This is powerful as it enables you to consistently deliver data with the same structure and authorization rules.
This consistency remains intact even when you make significant changes, such as transitioning from MySQL to PostgreSQL,
adopting MongoDB for read operations and MySQL for write operations, altering your transactional email system, or
switching payment providers.

A metadata object is the fundamental building block of OpenDD and Hasura V3 metadata.
Hasura v3 metadata is split into one supergraph configuration and any number of subgraph configurations.

## Supergraph Configuration​

The supergraph configuration is an array of one of the following metadata objects:

```
objects :
   -   kind :  CompatibilityConfig
     # ... (other properties for CompatibilityConfig)
   -   kind :  AuthConfig
     # ... (other properties for AuthConfig)
```

More details about these can be found[ here ](https://hasura.io/docs/3.0/ci-cd/config/#supergraph).

## Subgraph Configuration​

There can be any number of subgraphs in your supergraph. Each subgraph has a name and a configuration consisting of an array of the following metadata objects:

```
name :  my_subgraph
objects :
   -   kind :  HasuraHubDataConnector
     # ... (other properties for HasuraHubDataConnector)
   -   kind :  DataConnector
     # ... (other properties for DataConnector)
   -   kind :  ScalarType
     # ... (other properties for ScalarType)
   -   kind :  ObjectType
     # ... (other properties for ObjectType)
   -   kind :  DataConnectorScalarRepresentation
     # ... (other properties for DataConnectorScalarRepresentation)
   -   kind :  Model
     # ... (other properties for Model)
   -   kind :  Command
     # ... (other properties for Command)
   -   kind :  Relationship
     # ... (other properties for Relationship)
   -   kind :  TypePermissions
     # ... (other properties for TypePermissions)
   -   kind :  ModelPermissions
     # ... (other properties for ModelPermissions)
   -   kind :  CommandPermissions
     # ... (other properties for CommandPermissions)
```

## Data Connectors​

The[ data connector ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/)will define where the data is coming from. It can be a database, a REST API,
a GraphQL API, etc. The data connector will use the[ Native Data Connector ](https://hasura.io/docs/3.0/connectors/overview/)protocol to
connect to the data source and fetch the data.

### The DataConnector object​

The[ DataConnector ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/)object describes a physical data connector that is hosted at a URL that Hasura can talk to for serving queries.
These data connectors are self-deployed and managed outside of the Hasura metadata.

### The HasuraHubDataConnector object​

The[ HasuraHubDataConnector ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector)object allows you to atomically configure and deploy a data connector available in the[ Connector Hub ](https://hasura.io/connectors/)directly from the metadata.

## Types​

[ Types ](https://hasura.io/docs/3.0/data-domain-modeling/types/)are a fundamental building block of OpenDD metadata with every bit of data in OpenDD having a
type

### The ObjectType object​

The[ ObjectType ](https://hasura.io/docs/3.0/data-domain-modeling/types/#object-types)object allows you to create structured object types with fields.

### The ScalarType object​

The[ ScalarType ](https://hasura.io/docs/3.0/data-domain-modeling/types/#scalar-types)object allows you to create opaque types whose semantics are unknown to OpenDD.

### The DataConnectorScalarRepresentation object​

The[ DataConnectorScalarRepresentation ](https://hasura.io/docs/3.0/data-domain-modeling/types/#scalar-type-representation)object allows you to define how a
scalar type from a data connector (eg: varchar from postgres) is represented in your data graph.

## Models​

[ Models ](https://hasura.io/docs/3.0/data-domain-modeling/models/)are the link between your data sources and the API Hasura generates. A model may be backed by a
database table, an ad-hoc SQL query, a pre-materialized view, a custom REST or GraphQL API server, etc.

### The Model object​

The[ Model ](https://hasura.io/docs/3.0/data-domain-modeling/models/)object represents a collection of data objects (like rows in a SQL table or documents in
collection in a NoSQL database) of a certain[ type ](https://hasura.io/docs/3.0/data-domain-modeling/types/). A Model object also defines how the model and its types
or fields map to entities in the underlying data source. It also defines how it is represented in the GraphQL API.

## Commands​

[ Commands ](https://hasura.io/docs/3.0/data-domain-modeling/commands/)are the other way of accessing data within the OpenDD spec. Commands are functions /
procedures whose implementations are unknown to OpenDD except for their input arguments and output type.

### The Command object​

The[ Command ](https://hasura.io/docs/3.0/data-domain-modeling/commands/)object defines the name of the command, the arguments to the command and the output type
of the command. It also defines any mappings of arguments / types from OpenDD to their corresponding NDC versions.

## Relationships​

[ Relationships ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/)allow you extend[ object types ](https://hasura.io/docs/3.0/data-domain-modeling/types/)with related[ models ](https://hasura.io/docs/3.0/data-domain-modeling/models/)which then allows you to query nested or linked information.

### The Relationship object​

The[ Relationship ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/)object defines a relationship between a source[ type ](https://hasura.io/docs/3.0/data-domain-modeling/types/)and a
target[ models ](https://hasura.io/docs/3.0/data-domain-modeling/models/).

## Permissions​

The OpenDD Spec lets you define[ permissions ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/), (also known as access control or authorization rules)
on[ types ](https://hasura.io/docs/3.0/data-domain-modeling/types/),[ models ](https://hasura.io/docs/3.0/data-domain-modeling/models/)and[ commands ](https://hasura.io/docs/3.0/data-domain-modeling/commands/).

### The TypePermissions object​

[ TypePermissions ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#type-permissions)define which fields are allowed to be accessed by a
role.

### The ModelPermissions object​

[ ModelPermissions ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#model-permissions)define which objects or rows within the model are
allowed to be accessed by a role.

### The CommandPermissions object​

[ CommandPermissions ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions)define which commands are allowed to be executed by a
role.

## Automatic metadata generation​

The new Hasura DDN tooling of Console and the[ VS Code Extension ](https://marketplace.visualstudio.com/items?itemName=HasuraHQ.hasura)have built-in capabilities to
autogenerate the OpenDD spec metadata from your existing data via the GUI console or CLI terminal commands.
Alternatively, you can also author metadata manually.

### What did you think of this doc?

- [ How is this different from Hasura v2 metadata? ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#how-is-this-different-from-hasura-v2-metadata)
- [ The OpenDD spec ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#the-opendd-spec)
- [ Supergraph Configuration ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#supergraph-configuration)
- [ Subgraph Configuration ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#subgraph-configuration)
- [ Data Connectors ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#data-connectors)
    - [ The DataConnector object ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#the-dataconnector-object)

- [ The HasuraHubDataConnector object ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#hasura-hub-data-connector)
- [ Types ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#types)
    - [ The ObjectType object ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#the-objecttype-object)

- [ The ScalarType object ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#the-scalartype-object)

- [ The DataConnectorScalarRepresentation object ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#the-dataconnectorscalarrepresentation-object)
- [ Models ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#models)
    - [ The Model object ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#the-model-object)
- [ Commands ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#commands)
    - [ The Command object ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#the-command-object)
- [ Relationships ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#relationships)
    - [ The Relationship object ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#the-relationship-object)
- [ Permissions ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#permissions)
    - [ The TypePermissions object ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#the-typepermissions-object)

- [ The ModelPermissions object ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#the-modelpermissions-object)

- [ The CommandPermissions object ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#the-commandpermissions-object)
- [ Automatic metadata generation ](https://hasura.io/docs/3.0/data-domain-modeling/introduction/#automatic-metadata-generation)