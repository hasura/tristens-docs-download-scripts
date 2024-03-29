# Subgraphs

## Introduction​

For a multi-team organization working on a Hasura project, it can make sense for any one team to not have access to all
metadata objects. Subgraphs introduces the notion of a module system for your Hasura metadata.

A project can have a collection of subgraphs and the project becomes the 'union' of metadata objects across all
subgraphs of the project. Each subgraph can then be accessed and updated independently.

A build profile file with subgraphs looks something like the following:

```
version :   2
spec :
   environment :  staging
   mode :  replace
   supergraph :
     resources :
       -  supergraph/*
   subgraphs :
     -   name :  default
       resources :
         -  subgraphs/default/ **/*.hml
     -   name :  billing
       resources :
         -  subgraphs/fulfillment/ **/*.hml
     -   name :  stripe
       resources :
         -  subgraphs/stripe/ **/*.hml
```

## Subgraph Lifecycle​

### Create​

You can create a subgraph for a project on Hasura DDN using the CLI:

`hasura3 subgraph create -n  < SUBGRAPH_NAME >`

Within the `subgraphs` directory of your local project, create a directory with the name of the subgraph. For example,
if you created a subgraph named `billing` , then create a directory named `billing` within the `subgraphs` directory. You
can use the `default` subgraph as a template for your subgraph.

### Manage​

You can easily list all the available subgraphs for a project using the CLI:

`hasura3 subgraph list`

You can connect new data sources, add new types, etc. to a subgraph. Any files you add to the subgraph directory will be
picked up by the metadata build and associated with the subgraph.

### Delete​

Delete a subgraph by running:

`hasura3 subgraph delete -n  < SUBGRAPH_NAME >`

## Ownership Rules​

The metadata objects in subgraphs must follow the ownership rules for metadata objects as outlined below.

### DataConnector/ HasuraHubDataConnector​

The data source metadata object ( `DataConnector` / `HasuraHubDataConnector` ) doesn't depend on (or reference) any other
metadata object. Hence, any subgraph can define a data source.

Subgraph ownership

The subgraph that defines a data source then owns it. This means that no other subgraph can reference this data source
in their type representations, model, etc.

Violating this rule will result in the metadata build failing with the error, `unable to build schema: subgraph is not consistent: the following data source is defined more than once: <data source name>` .

### ObjectType​

The `ObjectType` metadata object also doesn't reference any other metadata object. Thus, any subgraph can define an `ObjectType` .

### DataConnectorScalarRepresentation​

The `DataConnectorScalarRepresentation` metadata object references the data connector metadata object and the scalar
type object. Thus, the data source in a `DataConnectorScalarRepresentation` should be owned by the **same** subgraph.

### ScalarType​

The `ScalarType` metadata object also doesn't reference any other metadata object. Thus, **any** subgraph can define a `ScalarType` .

### Model​

A `Model` metadata object references a data type. Also, the model's `source` references a data source and some data
types in type mappings. **Thus, the same subgraph should own the types and the data source.** 

### Command​

A `Command` metadata object references an output data type. Thus, the subgraph defining the `Command` metadata object
should also define the output data type.

### Relationship​

The `Relationship` metadata object references a source type and a target model. The source type used in the `Relationship` should be owned by the subgraph defining the `Relationship` .

Target model ownership

The target model can be from any subgraph. This allows us to define relationships across subgraphs. To use a model from
another subgraph as the target, you will need to reference the subgraph in the target model definition. Please refer to
the[ TargetModel ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel)for syntax.

### TypePermissions​

The `TypePermissions` metadata object references a type (for which the permission is being defined). Thus, the subgraph
defining the `TypePermissions` should own the type referenced.

### ModelPermissions​

Similar to `TypePermissions` , the subgraph should also own the model referenced in the `ModelPermissions` metadata
object.

### CommandPermissions​

The `CommandPermissions` metadata object references a command, which should be defined in the same subgraph.

### AuthConfig​

This is defined in the supergraph.

Only one auth config allowed per project

There can be only one `AuthConfig` in the project's metadata. If there is more than one `AuthConfig` , then the metadata
build will fail with the error `Found duplicate authentication config` .

## Other Rules​

Apart from ownership rules, metadata with subgraphs should also follow the following rules:

### Duplicate Subgraphs​

Metadata should not define two subgraphs with same name.

### Duplicate Metadata Objects​

Metadata should also not define the same subgraph object twice (either in the same subgraph or in different subgraphs).
If you violate this rule, then the metadata build will fail with the error `subgraph constraints violated - found multiple subgraphs with the same name` .

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#introduction)
- [ Subgraph Lifecycle ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#subgraph-lifecycle)
    - [ Create ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#create)

- [ Manage ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#manage)

- [ Delete ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#delete)
- [ Ownership Rules ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#ownership-rules)
    - [ DataConnector/ HasuraHubDataConnector ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#dataconnector-hasurahubdataconnector)

- [ ObjectType ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#objecttype)

- [ DataConnectorScalarRepresentation ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#dataconnectorscalarrepresentation)

- [ ScalarType ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#scalartype)

- [ Model ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#model)

- [ Command ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#command)

- [ Relationship ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#relationship)

- [ TypePermissions ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#typepermissions)

- [ ModelPermissions ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#modelpermissions)

- [ CommandPermissions ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#commandpermissions)

- [ AuthConfig ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#authconfig)
- [ Other Rules ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#other-rules)
    - [ Duplicate Subgraphs ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#duplicate-subgraphs)

- [ Duplicate Metadata Objects ](https://hasura.io/docs/3.0/ci-cd/subgraphs/#duplicate-metadata-objects)
