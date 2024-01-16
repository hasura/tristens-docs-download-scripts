# OpenDD Permissions

## Introduction​

The OpenDD Spec lets you define permissions, (also known as access control or authorization rules) on[ object types ](https://hasura.io/docs/3.0/data-domain-modeling/types/),[ models ](https://hasura.io/docs/3.0/data-domain-modeling/models/)and[ commands ](https://hasura.io/docs/3.0/data-domain-modeling/commands/)in your data domain.

The following types of permissions can be defined in the[ OpenDD spec ](https://hasura.io/docs/3.0/data-domain-modeling/overview/):

- `TypePermissions` define which fields are allowed to be accessed by a role. Defining permissions on output types is
useful, as certain fields may be sensitive and should only be accessible to particular roles.
- `ModelPermissions` define which objects or rows within a model are allowed to be accessed by a role.
- `CommandPermissions` defines whether the command is executable by a role.


## Type permissions​

A type permission will need the type and the role(s) for which the permission should be defined. For each role, you will
need to define the fields accessible for that role.

### Metadata Structure​

```
kind :  TypePermissions
version :  v1
definition :
   typeName :  <TypeName >
   permissions :  <TypePermission >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `typeName`  | [ TypeName ](https://hasura.io/docs/3.0/data-domain-modeling/types/) | true | The name of the type for which permissions are to be defined. |
|  `permissions`  | [ [TypePermission] ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#typepermission) | true | The permissions object for this type, one for each role. |


#### TypePermission​

```
permissions :
   -   role :  <RoleName >
     output :  <OutputPermission >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `role`  |  `String`  | true | The name of the role for which permissions are to be defined. |
|  `output`  | [ OutputPermission ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#outputpermission) | true | The type output permission for the role. |


#### OutputPermission​

```
output :
   allowedFields :
     -  <field1 >
     -  <field2 >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `allowedFields`  |  `[String]`  | true | List of fields that are accessible to the role. |


### Examples​

To define permissions on an output type `article` for `admin` and `user` role:

```
kind :  TypePermissions
version :  v1
definition :
   typeName :  article
   permissions :
     -   role :  admin
       output :
         allowedFields :
           -  id
           -  title
           -  author_id
     -   role :  user
       output :
         allowedFields :
           -  id
           -  title
```

Types are inaccessible when undefined for a role

If a role doesn't define any permissions for this type, then none of its fields would be accessible to that role.

## Model Permissions​

A model permission will need the model name and the role(s) for which the permission should be defined. For each role,
you will need to define an optional filter expression. Objects (or rows/documents) that satisfy this filter predicate
will be returned for that role.

### Metadata Structure​

```
kind :  ModelPermissions
version :  v1
definition :
   modelName :  <ModelName >
   permissions :  <ModelPermission >
```

| Field | Type | Required | Description |
|---|---|---|---|
| modelName |  `String`  | true | The name of the model for which permissions are to be defined. |
| permissions | [ [ModelPermission] ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#modelpermission) | true | The permissions object for this model, one for each role. |


#### ModelPermission​

```
permissions :
   -   role :  <RoleName >
     select :  <SelectPermission >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `role`  |  `String`  | true | The name of the role for which permissions are to be defined. |
|  `select`  | [ SelectPermission ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#selectpermission) | true | The model select permission for the role. |


#### SelectPermission​

```
select :
   filter :  <ModelPredicate >
```

| Field | Type | Required | Description |
|---|---|---|---|
| filter | [ ModelPredicate ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#modelpredicate) | false | Optional predicate to satisfy. This predicate can use operators supported by the model’s data connector. If the filter is missing then all rows are accessible. If the filter is present, then only the rows satisfying this filter expression are accessible. |


### Examples​

Below, we're creating a set of `ModelPermissions` on the `Articles` model for the roles `admin` , `user_1` , and `user_2` .

As the `select` object for `admin` role is empty, it will return all rows.

The `user_1` role's `select` object has a filter predicate that will return rows where the `author_id` field is equal to
the `x-hasura-user-id` session variable.

The `user_2` role's `select` object has a filter predicate that will return rows where the `title` field is like the
string `Functional` .

```
kind :  ModelPermissions
version :  v1
definition :
   modelName :  Articles
   permissions :
     -   role :  admin
       select :
         filter :
     -   role :  user_1
       select :
         filter :
           fieldComparison :
             field :  author_id
             operator :  _eq
             value :
               sessionVariable :  x - hasura - user - id
     -   role :  user_2
       select :
         filter :
           and :
             -   fieldComparison :
                 field :  title
                 operator :  _like
                 value :
                   literal :   "%Functional%"
```

Models are inaccessible when undefined for a role

If a role doesn't define any permissions for this model, then the model won't be selectable for that role.

## Command permissions​

A command permission will need the command name and the role(s) for which the permission should be defined.

### Metadata structure​

```
kind :  CommandPermissions
version :  v1
definition :
   commandName :  <CommandName >
   permissions :  <CommandPermission >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `commandName`  |  `String`  | true | The name of the command for which permissions are to be defined. |
|  `permissions`  | [ [CommandPermission] ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#commandpermission) | true | The permissions object for this command, one for each role. |


#### CommandPermission​

```
permissions :
   -   role :  <RoleName >
     allowExecution :  <Boolean >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `role`  |  `String`  | true | The name of the role for which permissions are to be defined. |
|  `allowExecution`  |  `Boolean`  | true | Is the execution of the command allowed for the role |


### Examples​

To define permissions on a command with name `get_article_by_id` for `admin` and `user` role:

```
kind :  CommandPermissions
version :  v1
definition :
   commandName :  get_article_by_id
   permissions :
     -   role :  admin
       allowExecution :   true
     -   role :  user
       allowExecution :   false
```

Commands are inaccessible when undefined for a role

If a role doesn't define any permissions for this command, then it won't be executable by that role.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#introduction)
- [ Type permissions ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#type-permissions)
    - [ Metadata Structure ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#metadata-structure)
        - [ TypePermission ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#typepermission)

- [ OutputPermission ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#outputpermission)

- [ Examples ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#examples)

- [ Metadata Structure ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#metadata-structure)
    - [ TypePermission ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#typepermission)
- [ Model Permissions ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#model-permissions)
    - [ Metadata Structure ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#metadata-structure-1)
        - [ ModelPermission ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#modelpermission)

- [ SelectPermission ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#selectpermission)

- [ Examples ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#examples-1)

- [ Metadata Structure ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#metadata-structure-1)
    - [ ModelPermission ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#modelpermission)
- [ Command permissions ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#command-permissions)
    - [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#metadata-structure-2)
        - [ CommandPermission ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#commandpermission)

- [ Examples ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#examples-2)

- [ Metadata structure ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#metadata-structure-2)
    - [ CommandPermission ](https://hasura.io/docs/3.0/data-domain-modeling/permissions/#command-permissions/#commandpermission)
