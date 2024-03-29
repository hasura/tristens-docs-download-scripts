# OpenDD Types

## Introduction​

In the OpenDD spec in Hasura, types serve as the fundamental elements that define the structure of your data.

Being able to define types in your data domain is beneficial because it provides you with the flexibility to define them
separately from the types in your data connector.

The specification employs a concrete type system that includes both primitive types and user-defined types. All
subsequent layers, such as models, commands, and relationships are defined in terms of these types.

The types can be one of the following:

| OpenDD Type | Description |
|---|---|
| Primitive | These are the basic types `ID` , `Int` , `Float` , `Boolean` , or `String`  |
| Custom | These are user-defined types, such as[ ScalarType ](https://hasura.io/docs/3.0/data-domain-modeling/types/#scalar-types)or[ ObjectType ](https://hasura.io/docs/3.0/data-domain-modeling/types/#object-types) |
| Type References | When specifying the types of a field or an argument, you can mark them as required `!` or repeated `[]` . |


The spec also allows you to map existing data connector scalars to types in your data domain.

You can also define custom types by either aliasing existing types (such as primitives or custom), or you can define a
type with fields. In turn, the fields themselves can be a primitive or another custom type.

Type references are types of fields and arguments that refer to other primitive or custom types and which can be marked
as nullable, required or repeated (in the case of arrays).

[ Scalar type representation ](https://hasura.io/docs/3.0/data-domain-modeling/types/#scalar-type-representation)helps in mapping data connector scalars to any of the OpenDD
types.

## Primitive types and type references​

Primitive types supported by the OpenDD spec are `ID` , `Int` , `Float` , `Boolean` and `String` .

Type references in OpenDD follow[ GraphQL type
syntax ](https://spec.graphql.org/June2018/#sec-Combining-List-and-Non-Null). Fields and arguments are nullable by
default. To represent non-nullability, specify a `!` after the type name. Similarly, array fields and arguments are
wrapped in `[]` .

### Examples​

If the field is nullable, it should be defined as

```
name :  category
type :
  ProductCategory
```

If the field is non-nullable, it should be defined as

```
name :  category
type :
  ProductCategory !
```

If the field is a nullable array of nullable type, it should be defined as

```
name :  tags
type :
   [ String ]
```

If the field is a nullable array of non-nullable type, it should be defined as

```
name :  tags
type :
   [ String ! ]
```

If the field is a non-nullable array of nullable type, it should be defined as

```
name :  tags
type :
   [ String ] !
```

If the field is a non-nullable array of non-nullable type, it should be defined as

```
name :  tags
type :
   [ String ! ] !
```

## Scalar types​

In the OpenDD spec, you can create opaque types whose semantics are unknown to OpenDD by defining an object with `kind:
ScalarType` and `version: v1` . These show up as scalars in your GraphQL schema. The object `definition` should include `name` and an optional `graphql` field.

### Metadata structure​

```
kind :  ScalarType
version :  v1
definition :
   name :  <TypeName >
   graphql :  <ScalarTypeGraphQLConfig >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `name`  |  `String`  | true | Name of the type. |
|  `graphql`  | [ ScalarTypeGraphQLConfig ](https://hasura.io/docs/3.0/data-domain-modeling/types/#scalartypegraphqlconfig) | false | Configuration for using this scalar type in the GraphQL API. |


#### ScalarTypeGraphQLConfig​

 `ScalarTypeGraphQLConfig` is an object that defines the configuration for using this scalar type in the GraphQL API.
All scalar types are represented as custom[ GraphQL scalars ](https://graphql.org/learn/schema/#scalar-types)in the resulting GraphQL API.
This object has a field `typeName` that corresponds to the GraphQL type name to use for this scalar type.

```
graphql :
   typeName :  <GraphQLTypeName >
```

### Examples​

Below, we define an `Email` type that is represented as a primitive `String` type:

```
kind :  ScalarType
version :  v1
definition :
   name :  Email
   graphql :
     typeName :  EmailScalar
```

Below, we define an `OpaqueDate` type that is represented as a custom object type:

```
kind :  ScalarType
version :  v1
definition :
   name :  OpaqueDate
```

## Object types​

In the OpenDD spec, completely new types can be created by defining an object with `kind: ObjectType` and `version: v1` .
You need to also define a name and the fields for this type.

### Metadata structure​

```
kind :  ObjectType
version :  v1
definition :
   name :  <TypeName >
   fields :
     -   name :  field1
       type :  <TypeReference >
     -   name :  field2
       type :  <TypeReference >
   globalIdFields :
     -  field1
   graphql :  <ObjectTypeGraphQLConfig >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `name`  |  `String`  | true | Name of the type. |
|  `fields`  | [ [Field] ](https://hasura.io/docs/3.0/data-domain-modeling/types/#field) | true | List of fields. |
|  `globalIdFields`  |  `[String]`  | false | Names of the fields that will form the Global ID associated with the object type. |
|  `graphql`  | [ ObjectTypeGraphQLConfig ](https://hasura.io/docs/3.0/data-domain-modeling/types/#objecttypegraphqlconfig) | false | Configuration for using this object type in the GraphQL API. |


#### Field​

| Field | Type | Required | Description |
|---|---|---|---|
|  `name`  |  `String`  | true | Name of the field. |
|  `type`  |  `String`  | true | Type reference of the field. |


#### ObjectTypeGraphQLConfig​

 `ObjectTypeGraphQLConfig` is config that defines the configuration for using this object type in the GraphQL API.
When used in an output context, a[ GraphQL object type ](https://graphql.org/learn/schema/#object-types-and-fields)is generated for each OpenDD object. `ObjectTypeGraphQLConfig` has a field `typeName` that corresponds to the GraphQL type name to use for this OpenDD object type.
The fields of this generated GraphQL object type will have the same names as the OpenDD field names. The generated GraphQL field types
will also pick the nullability and repeated characteristics based on the OpenDD type reference for the field.

```
graphql :
   typeName :  <GraphQLTypeName >
```

### Examples​

1. Below, we define an `author` type that has three fields: `author_id` , `first_name` , and `last_name` . Each field is
represented as a primitive `Int` or `String` type. The `author_id` field is non-nullable whereas `first_name` and `last_name` fields are nullable.
When used in the GraphQL API in an output context, this will result in a GraphQL object type called `Author` .


```
kind :  ObjectType
version :  v1
definition :
   name :  author
   fields :
     -   name :  author_id
       type :  Int !
     -   name :  first_name
       type :  String
     -   name :  last_name
       type :  String
   graphql :
     typeName :  Author
```

1. Extending the `author` type to also have a Global ID field


```
kind :  ObjectType
version :  v1
definition :
   name :  author
   fields :
     -   name :  author_id
       type :  Int !
     -   name :  first_name
       type :  String
     -   name :  last_name
       type :  String
   graphql :
     typeName :  Author
   globalIdFields :
     -  author_id
```

Now, the `Author` GraphQL type will have an auto-generated `id` field that is a globally
unique ID across your data domain, which will be based on the `author_id` field of `artist` .
The `node` query root field of the Relay API can then be used to retrieve this global ID,
given there is a model whose `objectType` is `artist` and it is set as the `globalIdSource` .

## Scalar type representation for data connectors​

A scalar type from a data connector can be represented as an OpenDD type by defining an object with `kind: DataConnectorScalarRepresentation` and `version: v1` . To define a scalar type representation, you need to
have a data connector name, a data connector scalar type, a type representation and an optional graphql field.

Map scalars for user in your GraphQL API

It is necessary to map **any** available scalar from a data connector that is used in the GraphQL API.

### Metadata structure​

```
kind :  DataConnectorScalarRepresentation
version :  v1
definition :
   dataConnectorName :  <DataSourceName >
   dataConnectorScalarType :  <ScalarTypeName >
   representation :  <TypeName >
   graphql :  <DataConnectorScalarGraphQLConfig >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `dataConnectorName`  |  `String`  | true | Name of the data connector. |
|  `dataConnectorScalarType`  |  `String`  | true | Name of the scalar type from the data connector. |
|  `representation`  |  `String`  | true | Representation of the scalar type in GraphQL schema. |
|  `graphql`  | [ DCScalarGraphQLConfig ](https://hasura.io/docs/3.0/data-domain-modeling/types/#dcscalargraphqlconfig) | false | Configuration for using this data connector scalar type in the GraphQL API. |


#### DCScalarGraphQLConfig​

 `DCScalarGraphQLConfig` is an object that defines the configuration for using this data connector scalar type in the
GraphQL API. This object has a field `comparisonExpressionTypeName` that corresponds to the GraphQL type name to use for
the comparison expression input type that is generated for this data connector scalar type. This comparison expression type
will contain the comparison operators for this scalar as defined by the data connector.

```
graphql :
   comparisonExpressionTypeName :  <GraphQLTypeName >
```

### Examples​

1. Mapping a `text` scalar type from the `my_source` connector to a primitive `String` type and giving its GraphQL comparison expression a type name.


```
kind :  DataConnectorScalarRepresentation
version :  v1
definition :
   dataConnectorName :  my_source
   dataConnectorScalarType :  text
   representation :  String
   graphql :
     comparisonExpressionTypeName :  text_comparison_exp
```

1. Mapping a PostgreSQL scalar `geography` to a custom object type.


```
-   kind :  ObjectType
   version :  v1
   definition :
     name :  Geography
     fields :
       -   name :  type
         type :  String
       -   name :  coordinates
         type :   [ Float ]
-   kind :  DataConnectorScalarRepresentation
   version :  v1
   definition :
     dataConnectorName :  pg_source
     dataConnectorScalarType :  geography
     representation :  Geography
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/data-domain-modeling/types/#introduction)
- [ Primitive types and type references ](https://hasura.io/docs/3.0/data-domain-modeling/types/#primitive-types-and-type-references)
    - [ Examples ](https://hasura.io/docs/3.0/data-domain-modeling/types/#examples)
- [ Scalar types ](https://hasura.io/docs/3.0/data-domain-modeling/types/#scalar-types)
    - [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/types/#metadata-structure)
        - [ ScalarTypeGraphQLConfig ](https://hasura.io/docs/3.0/data-domain-modeling/types/#scalartypegraphqlconfig)

- [ Examples ](https://hasura.io/docs/3.0/data-domain-modeling/types/#examples-1)

- [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/types/#metadata-structure)
    - [ ScalarTypeGraphQLConfig ](https://hasura.io/docs/3.0/data-domain-modeling/types/#scalartypegraphqlconfig)
- [ Object types ](https://hasura.io/docs/3.0/data-domain-modeling/types/#object-types)
    - [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/types/#metadata-structure-1)
        - [ Field ](https://hasura.io/docs/3.0/data-domain-modeling/types/#field)

- [ ObjectTypeGraphQLConfig ](https://hasura.io/docs/3.0/data-domain-modeling/types/#objecttypegraphqlconfig)

- [ Examples ](https://hasura.io/docs/3.0/data-domain-modeling/types/#object-type-examples)

- [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/types/#metadata-structure-1)
    - [ Field ](https://hasura.io/docs/3.0/data-domain-modeling/types/#field)
- [ Scalar type representation for data connectors ](https://hasura.io/docs/3.0/data-domain-modeling/types/#scalar-type-representation)
    - [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/types/#metadata-structure-2)
        - [ DCScalarGraphQLConfig ](https://hasura.io/docs/3.0/data-domain-modeling/types/#dcscalargraphqlconfig)

- [ Examples ](https://hasura.io/docs/3.0/data-domain-modeling/types/#examples-2)

- [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/types/#metadata-structure-2)
    - [ DCScalarGraphQLConfig ](https://hasura.io/docs/3.0/data-domain-modeling/types/#dcscalargraphqlconfig)
