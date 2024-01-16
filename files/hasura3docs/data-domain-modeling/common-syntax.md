# Common OpenDD Syntax

## ModelPredicate​

A `ModelPredicate` is used to define the boolean expression for filtering the objects within a model, and is typically used when defining permissions.

```
[ FieldComparison ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#fieldcomparison)
|
[ RelationshipPredicate ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#relationship)
|
[ AndExp ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#andexp)
|
[ OrExp ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#orexp)
|
[ NotExp ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#notexp)
```

### FieldComparison​

This predicate filters objects where the particular `field` of the object returns true when the specified comparison operator `operator` is applied with the `value` as input.

```
fieldComparison :
   field :  <FieldName >
   operator :  <Operator >
   value :  <ValueExpression >
```

| Field | Type | Required | Description |
|---|---|---|---|
| field |  `String`  | true | Name of the field of the model to compare. |
| operator |  `String`  | true | Name of the operator. Either the built-in operators `_ eq` or `_ is_ null` , or any of the operators available from the data connector. |
| value | [ ValueExpression ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#valueexpression) | false | The value to compare. Can be a literal value or a a value from session variables. This can be omitted in case of `_ is_ null` operator. |


### RelationshipPredicate​

This predicate evaluates to true if any of the corresponding target objects of the relationship of the source model's object type with `name` meet the nested `predicate` .

```
relationship :
   name :  <RelationshipName >
   predicate :  <ModelPredicate >
```

| Field | Type | Required | Description |
|---|---|---|---|
| name |  `String`  | true | Name of relationship of the model to compare. |
| predicate | [ ModelPredicate ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#modelpredicate) | false | The filter or predicate expression. |


### AndExp​

This predicates evaluates to true if all sub-predicates of `and` evaluate to true.

```
{
  "and" : [
[ ModelPredicate ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#modelpredicate)
]
}
```

### OrExp​

This predicates evaluates to true if any of the sub-predicates of `or` evaluate to true.

```
{
  "or" : [
[ ModelPredicate ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#modelpredicate)
]
}
```

### NotExp​

This predicates evaluates to true if the sub-predicates of `not` evaluates to false.

```
{
  "not" :
[ ModelPredicate ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#modelpredicate)
}
```

## ValueExpression​

An expression which evaluates to a value that can be used in comparison expressions, etc.
This expression can either be a literal value or a reference to a session variable.

```
[ Literal ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#literal)
|
[ SessionVariable ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#sessionvariable)
```

### Literal​

```
{
   "literal" :  <any JSON value>
}
```

#### Examples​

`literal :  some string`

### SessionVariable​

`sessionVariable :  String`

#### Examples​

`sessionVariable :  x - hasura - user - id`

## TypeMapping​

The `typemapping` is used by[ models ](https://hasura.io/docs/3.0/data-domain-modeling/models/)and[ commands ](https://hasura.io/docs/3.0/data-domain-modeling/commands/)to define the mapping between the fields of the OpenDD types used in the model/command and
the fields of the corresponding types in the data connector. It has the following fields:

```
<OpenDDTypeName> :
   fieldMapping :  <FieldMapping >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `OpenDDTypeName`  |  `String`  | true | Name of the OpenDD object type which is being mapped. |
|  `fieldMapping`  | [ FieldMapping ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#fieldmapping) | true | The field mapping between the OpenDD object type and the corresponding NDC object type. |


## FieldMapping​

The `fieldMapping` is used by[ typemapping ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#typemapping)to define mapping for the fields of the `OpenDDTypeName` .

It has the following fields:

```
<OpenDDFieldName> :
   column :  <String >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `OpenDDFieldName`  |  `String`  | true | Name of the field in the OpenDD object type. |
|  `column`  |  `String`  | true | The name of the field in the NDC object type. |


## ArgumentDefinition​

Arguments is a list of objects that defines the arguments for the[ model ](https://hasura.io/docs/3.0/data-domain-modeling/models/#metadata-structure)or a[ command ](https://hasura.io/docs/3.0/data-domain-modeling/commands/#metadata-structure). An argument object has the following fields:

```
name :  <String > ,
type :  <TypeReference >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `name`  |  `String`  | true | Name of the argument. |
|  `type`  |  `Type`  | true | [ TypeReference ](https://hasura.io/docs/3.0/data-domain-modeling/types/#primitive-types-and-type-references)of the argument as a string. |


## Secret references​

Instead of embedding sensitive values in the metadata, certain fields can be set using[ secrets ](https://hasura.io/docs/3.0/ci-cd/secrets/)stored in DDN.

To embed a value directly without using a secret:

`value: <your value>`

To use a value via a secret:

`stringValueFromSecret: <secret name>`

### What did you think of this doc?

- [ ModelPredicate ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#modelpredicate)
    - [ FieldComparison ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#fieldcomparison)

- [ RelationshipPredicate ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#relationshippredicate)

- [ AndExp ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#andexp)

- [ OrExp ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#orexp)

- [ NotExp ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#notexp)
- [ ValueExpression ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#valueexpression)
    - [ Literal ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#literal)
        - [ Examples ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#examples)

- [ SessionVariable ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#sessionvariable)
    - [ Examples ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#examples-1)

- [ Literal ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#literal)
    - [ Examples ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#examples)
- [ TypeMapping ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#typemapping)
- [ FieldMapping ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#fieldmapping)
- [ ArgumentDefinition ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#argumentdefinition)
- [ Secret references ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#secret)
