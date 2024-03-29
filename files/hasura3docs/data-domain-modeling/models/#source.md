# OpenDD Models

## Introduction​

Models are the link between your data connectors and the API Hasura generates. A model may be backed by a database
table, an ad-hoc SQL query, a pre-materialized view, a custom REST or GraphQL API server, etc.

Once a model is declared it will then often be referenced by `Relationship` and/or `Permissions` objects.

## Description​

To create a model, you need to define an OpenDD object with `kind: Model` and `version: v1` . The object `definition` has the following fields:

### Metadata structure​

```
kind :  Model
version :  v1
definition :
   name :  <ModelName >
   objectType :  <TypeName >
   globalIDSource :  true  |  false
   source :  <SourceConfiguration >
   graphql :  <GraphQLConfiguration >
   arguments :   [ ArgumentDefinition ]
   filterableFields :   [ FilterableFields ]
   orderableFields :   [ OrderableFields ]
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `name`  |  `String`  | true | Name of the model. |
|  `objectType`  |  `String`  | true | [ Type ](https://hasura.io/docs/3.0/data-domain-modeling/types/)of the objects in this model. |
|  `globalIDSource`  |  `Boolean`  | true | If this model should be used as the[ Global ID ](https://hasura.io/docs/3.0/data-domain-modeling/global-id/)source for its `objectType` . |
|  `source`  | [ SourceConfiguration ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source) | false | Source configuration for the model. |
|  `graphql`  | [ ModelGraphQLConfiguration ](https://hasura.io/docs/3.0/data-domain-modeling/models/#graphql) | false | GraphQL configuration for the model. |
|  `arguments`  | [ [ArgumentDefinition] ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#argumentdefinition) | true | The argument definitions for the model. |
|  `filterableFields`  | [ [FilterableFieldDefinition] ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#filterablefielddefinition) | true | Filterable fields for the model. |
|  `orderableFields`  | [ [OrderableFieldDefinition] ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#orderablefielddefinition) | true | Orderable fields for the model. |


Filterable/Orderable Fields support

At the moment, we don't support field level filterable/orderable customizations. So, you will have to provide an
exhaustive list of the fields of your model in `filterableFields` and `orderableFields` .

#### SourceConfiguration​

The source configuration is an object that defines the data source for the model. It has the following fields:

```
source :
   dataConnectorName :  <DataConnectorName >
   collection :  <CollectionName >
   typeMapping :  <TypeMapping >
```

| source Field | Type | Required | Description |
|---|---|---|---|
|  `dataConnector`  |  `String`  | true | Name of the source data connector backing this model. |
|  `collection`  |  `String`  | true | Name of the collection in the source data connector backing this model. |
|  `typeMapping`  | [ TypeMapping ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#typemapping) | true | Type mappings from OpenDD object types used within the model to the corresponding data connector types. |


#### ModelGraphQLConfiguration​

ModelGraphQLConfiguration is an object that defines how the model should be surfaced in the GraphQL API. It has the following fields:

```
graphql :
   selectUniques :  <SelectUniques >
   selectMany :  <SelectMany >
   filterExpressionType :  <FilterExpressionType >
   orderByExpressionType :  <OrderByExpressionType >
   argumentsInputType :  <ArgumentsInputType >
```

| graphql Field | Type | Required | Description |
|---|---|---|---|
|  `selectUniques`  | [ [SelectUniques] ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#selectuniques) | true | Select uniques configuration for the model. |
|  `selectMany`  | [ SelectMany ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#selectmany) | false | Select many configuration for the model. |
|  `filterExpressionType`  |  `String`  | false | GraphQL type name to use for the filter input. |
|  `orderByExpressionType`  |  `String`  | false | GraphQL type name to use for the order by input. |
|  `argumentsInputType`  |  `String`  | false | GraphQL type name to use for the model arguments input. |


##### SelectUniques​

Select uniques is an array of objects that defines the unique identifiers for the model. For each select unique defined here,
a query root field is added to the GraphQL API. For each field defined in the `uniqueIdentifier` , an input argument is added
to the query root field which can be supplied to retrieve the unique identified object from the model.

```
selectUniques :
   queryRootField :  <QueryRootField >
   uniqueIdentifier :  <UniqueIdentifier >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `queryRootField`  |  `String`  | true | Name of the query root field to use in the GraphQL API. |
|  `uniqueIdentifier`  |  `Array`  | true | Set of fields which can uniquely identify a row/object in the model. |


##### SelectMany​

Select many configuration for a model adds a query root field to the GraphQl API that can be used to retrieve multiple objects from the model.
This field can accept the following arguments:

- `args` , used for supplying the values for the model's arguments. This argument is generated only if the model has arguments and `argumentsInputType` is set in the ModelGraphQlConfiguration.
- `where` , used for filtering the objects to retrieve. This argument is generated only if `filterExpressionType` is set in the ModelGraphQlConfiguration. The filter expression contains all the filterable fields and the `_and` / `_or` / `_not` logical operators.
- `order_by` , used for sorting the retrieved objects. This argument is generated only if `orderByExpressionType` is set in the ModelGraphQlConfiguration. The order by expression contains all the orderable fields.
- `limit` , used for limiting the number of retrieved objects.
- `offset` , used for skipping the first `offset` objects when retrieving.


```
selectMany :
   queryRootField :  <QueryRootField >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `queryRootField`  |  `String`  | true | Name of the query root field to use in the GraphQL API. |


#### FilterableFieldDefinition​

The filterable field definition is an object that lists the allowed operators for a given field.

```
filterableFields :
   -   fieldName :  <String >
     operators :
       enableAll :   true
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `fieldName`  |  `String`  | true | Name of the field. |
|  `operators`  |  `Object`  | true | Allowed operators (at the moment, we only support `enableAll: true` ) |


#### OrderableFieldDefinition​

Orderable field definition is an object that lists down the allowed order by directions for a given field.

```
orderableFields :
   -   fieldName :  <String >
     orderByDirections :
       enableAll :   true
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `fieldName`  |  `String`  | true | Name of the field. |
|  `orderByDirections`  |  `Object`  | true | Allowed order by directions (at the moment, we only support `enableAll: true` ) |


## Examples​

In this example, we're creating a model called `Authors` backed by a database table called `authors` in the `db` data
source:

```
kind :  Model
version :  v1
definition :
   name :  Authors
   objectType :  author
   globalIdSource :   true
   source :
     dataConnectorName :  db
     collection :  authors
     typeMapping :
       author :
         fieldMapping :
           author_id :
             column :  id
           first_name :
             column :  first_name
           last_name :
             column :  last_name
   graphql :
     selectUniques :
       -   queryRootField :  AuthorByID
         uniqueIdentifier :
           -  author_id
     selectMany :
       queryRootField :  AuthorMany
     filterExpressionType :  Author_Where_Exp
     orderByExpressionType :  Author_Order_By
   arguments :   [ ]
   filterableFields :
     -   fieldName :  author_id
       operators :
         enableAll :   true
     -   fieldName :  first_name
       operators :
         enableAll :   true
     -   fieldName :  last_name
       operators :
         enableAll :   true
   orderableFields :
     -   fieldName :  author_id
       orderByDirections :
         enableAll :   true
     -   fieldName :  first_name
       orderByDirections :
         enableAll :   true
     -   fieldName :  last_name
       orderByDirections :
         enableAll :   true
```

Assuming the ObjectType was defined like[ this ](https://hasura.io/docs/3.0/data-domain-modeling/types/#object-type-examples), and the scalar types corresponding to the fields had
appropriate comparison expressions defined, the resulting GraphQl API will be:

```
type   Query   {
   node ( id :   ID ! ) :   Node
   AuthorByID ( author_id :   Int ! ) :   Author
   AuthorMany ( where :   Author_Where_Exp ,   order_by   Author_Order_By ,   limit :   Int ,   offset :   Int ) :   Author
}
type   Author   {
   id :   ID !
   author_id :   Int !
   first_name :   String
   last_name :   String
}
input   Author_Where_Exp :   {
   _and :   [ Author_Where_Exp ! ]
   _or :   [ Author_Where_Exp ! ]
   _not :   [ Author_Where_Exp ! ]
   author_id :   int_comparison_exp
   first_name :   text_comparison_exp
   last_name :   text_comparison_exp
}
input   Author_Order_By   {
   author_id :   order_by
   first_name :   order_by
   last_name :   order_by
}
enum   order_by   {
   Asc ,
   Desc
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#introduction)
- [ Description ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#description)
    - [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#metadata-structure)
        - [ SourceConfiguration ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#source)

- [ ModelGraphQLConfiguration ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#graphql)

- [ FilterableFieldDefinition ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#filterablefielddefinition)

- [ OrderableFieldDefinition ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#orderablefielddefinition)

- [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#metadata-structure)
    - [ SourceConfiguration ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#source)
- [ Examples ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source/#examples)
