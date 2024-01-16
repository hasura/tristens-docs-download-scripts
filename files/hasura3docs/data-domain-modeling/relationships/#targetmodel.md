# OpenDD Relationships

## Introduction​

A relationship allows you to query nested or linked information, for example from `Manufacturers` to `Products` . A
relationship defined in the OpenDD spec allows you extend[ type ](https://hasura.io/docs/3.0/data-domain-modeling/types/)objects with related[ models ](https://hasura.io/docs/3.0/data-domain-modeling/models/).

To create a relationship, you will need to define an object with `kind: Relationship` and `version: v1` . The object `definition` has a `name` , the `source` type, a `target` model and the `mapping` between the two.

### Metadata structure​

```
kind :  Relationship
version :  v1
definition :
   source :  <String >
   name :  <String >
   target :  <TargetConfiguration >
   mapping :  <RelationshipMapping >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `source`  |  `String`  | true | The source[ type ](https://hasura.io/docs/3.0/data-domain-modeling/types/)of the relationship. |
|  `name`  |  `String`  | true | The name of the relationship. |
|  `target`  | [ TargetConfiguration ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#targetconfiguration) | true | The target of the relationship. |
|  `mapping`  | [ [RelationshipMapping] ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#relationshipmapping) | true | Defines how the `Source` and `Target` should be connected. This field expects a list of objects. |


#### TargetConfiguration​

```
target :
   model :  <TargetModel >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `model`  | [ TargetModel ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#targetmodel) | true | The target[ model ](https://hasura.io/docs/3.0/data-domain-modeling/models/)for the relationship. |


#### TargetModel​

```
model :
   name :  <String >
   subgraph :  <String >
   relationshipType :  <RelationshipType >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `name`  |  `String`  | true | The name of the target model. |
|  `subgraph`  |  `String`  | false | The subgraph of the target model. Defaults to the subgraph of the relationship metadata object. |
|  `relationshipType`  | [ RelationshipType ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#relationshiptype) | true | The type of the relationship: either `Object` or `Array` . |


#### RelationshipType​

`relationshipType :  Object  |  Array`

| Value | Description |
|---|---|
|  `Object`  | The relationship is a one-to-one relationship. |
|  `Array`  | The relationship is a one-to-many relationship. |


#### RelationshipMapping​

Defines how the source type maps to the target model in this relationship. The mapping can have multiple links.

```
mapping :
   -   source :  <RelationshipMappingSource >
     target :  <RelationshipMappingTarget >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `source`  | [ RelationshipMappingSource ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#relationshipmappingsource) | true | The source link of this mapping. |
|  `target`  | [ RelationshipMappingTarget ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#relationshipmappingtarget) | true | The target link of this mapping. |


#### RelationshipMappingSource​

```
source :
   fieldPath :
     -  <FieldAccess >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `fieldPath`  | [ [FieldAccess] ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#fieldaccess) | true | The field path of the source link. |


#### RelationshipMappingTarget​

```
target :
   modelField :
     -  <FieldAccess >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `modelField`  | [ [FieldAccess] ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#fieldaccess) | true | The field path of the target model the source link maps to. |


#### FieldAccess​

Defines a single element of a field path.

`fieldName :  <FieldName >`

| Field | Type | Required | Description |
|---|---|---|---|
|  `fieldName`  |  `String`  | true | The name of the field for this path element. |


## Example​

### Basic relationship​

Let's add the following relationships to the above types.

1. `Array` relationship where `author` has many `Articles` :


```
kind :  Relationship
version :
definition :
   source :  author
   name :  articles
   target :
     model :
       name :  Articles
       relationshipType :  Array
   mappings :
     -   source :
         fieldPath :
           -   fieldName :  id
       target :
         modelField :
           -   fieldName :  author_id
```

1. `Object` relationship where `article` has one `Author` :


```
kind :  Relationship
version :  v1
definition :
   source :  article
   name :  author
   target :
     model :
       name :  Authors
       relationshipType :  Object
   mappings :
     -   source :
         fieldPath :
           -   fieldName :  author_id
       target :
         modelField :
           -   fieldName :  id
```

The resulting GraphQL schema will appear as:

```
type   Authors   {
   author_id :   Int !
   first_name :   String !
   last_name :   String !
   articles :   [ Article ! ] !
}
type   Articles   {
   id :   Int !
   author_id :   Int !
   title :   String !
   author :   Author
}
```

Local and Remote Relationships

Syntactically, there are no differences between local (e.g., a relationship between two columns in the same datasource,
or an existing foreign-key relationship) or remote (a relationship across two different data sources) relationships.
Hasura DDN will automatically detect the type of relationship and make the optimal query plan accordingly.

### Relationship across subgraphs​

Now, imagine if the `Article` model is defined in a **different subgraph** called `subgraph_articles` and the `Author` type
and the following array relationship are part of the `default` subgraph.

We will now need to specify the **target** subgraph in the `target` section of the relationship definition as `subgraph: subgraph_articles` as shown below:

```
kind :  Relationship
version :
definition :
   source :  author
   name :  articles
   target :
     model :
       name :  Articles
       relationshipType :  Array
       subgraph :  subgraph_articles
   mappings :
     -   source :
         fieldPath :
           -   fieldName :  id
       target :
         modelField :
           -   fieldName :  author_id
```

Next, imagine you want to query the author from the `Article` model, which is specified in the `subgraph_articles` subgraph. You will need to specify where the `Authors` can be queried from by specifying the **subgraph** in the `target` section of the relationship.

In this case, by specifying the subgraph as `subgraph: default` as shown below:

```
kind :  Relationship
version :  v1
definition :
   source :  article
   name :  author
   target :
     model :
       name :  Authors
       relationshipType :  Object
       subgraph :  default
   mapping :
     -   source :
         fieldPath :
           -   fieldName :  author_id
       target :
         modelField :
           -   fieldName :  id
```

Current limitations

1. Only types to top-level model types relationships are supported.
2. Simple top-level type field to top-level model field mapping are supported.


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#introduction)
    - [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#metadata-structure)
        - [ TargetConfiguration ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#targetconfiguration)

- [ TargetModel ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#targetmodel)

- [ RelationshipType ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#relationshiptype)

- [ RelationshipMapping ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#relationshipmapping)

- [ RelationshipMappingSource ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#relationshipmappingsource)

- [ RelationshipMappingTarget ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#relationshipmappingtarget)

- [ FieldAccess ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#fieldaccess)

- [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#metadata-structure)
    - [ TargetConfiguration ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#targetconfiguration)
- [ Example ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#example)
    - [ Basic relationship ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#basic-relationship)

- [ Relationship across subgraphs ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/#targetmodel/#relationship-across-subgraphs)
