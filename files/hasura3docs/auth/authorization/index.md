# Hasura Authorization

## Introduction​

 **Authorization determines what a verified user can access.** 

The OpenDD Spec lets you define permissions (also known as access control or authorization rules) on[ output types ](https://hasura.io/docs/3.0/data-domain-modeling/types/),[ models ](https://hasura.io/docs/3.0/data-domain-modeling/models/), and[ commands ](https://hasura.io/docs/3.0/data-domain-modeling/commands/)in your data domain.

There are three forms of permissions in the OpenDD Spec:

- [ Type Permissions ](https://hasura.io/docs/3.0/auth/authorization/index/#type-permissions): Define which fields within a `ScalarType` or `ObjectType` can
be accessed by a particular role.
- [ Model Permissions ](https://hasura.io/docs/3.0/auth/authorization/index/#model-permissions): Define which rows within a[ model ](https://hasura.io/docs/3.0/data-domain-modeling/models/)can be accessed by a specific role.
- [ Command Permissions ](https://hasura.io/docs/3.0/auth/authorization/index/#command-permissions): Define which[ commands ](https://hasura.io/docs/3.0/data-domain-modeling/commands/)can be
executed by a given role.


A role comes into existence when it is defined in one of these three ways.

Every request to Hasura should carry the necessary session variables or roles from your authentication service. The
presence and values of these roles determine which permissions apply to the request. There is no longer the concept
of a built-in, default, super-user `admin` role in Hasura DDN. You can however set up[ role emulation ](https://hasura.io/docs/3.0/auth/authentication/role-emulation/)in order to test your permissions with another role.

Hasura's roles and permissions via the OpenDD Spec are implemented at the Hasura Engine layer. They have no direct
relationship to any data source users and roles.

## Type Permissions​

With the OpenDD Spec, you can specify which fields of a `ScalarType` or `ObjectType` are accessible to specific roles.

### Example​

To define permissions on an output type `product` for `admin` and `customer` roles:

```
kind :  TypePermissions
version :  v1
definition :
   typeName :  product
   permissions :
     -   role :  admin
       output :
         allowedFields :
           -  id
           -  name
           -  price
           -  manufacturer_id
     -   role :  customer
       output :
         allowedFields :
           -  id
           -  name
           -  price
```

No access for undefined roles

If a role doesn't have any permissions defined for a type, it won't have access to it.

## Model Permissions​

You can control which rows or objects within a model a role can access. The syntax for this filter check, known as a `FieldComparison`  `ModelPredicate` , is available in the[ OpenDD Spec ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#modelpredicate).

### Example​

The following defines permissions for the `Users` model:

```
kind :  ModelPermissions
version :  v1
definition :
   modelName :  Users
   permissions :
   -   role :  admin
     select :
       filter :
   -   role :  customer
     select :
     filter :
       fieldComparison :
         field :  id
         operator :  _eq
         value :
           sessionVariable :  x - hasura - user - id
```

In the above example, the `admin` role has no restrictions on the `Users` model. The `customer` role can only access the
row where the `id` field matches the `x-hasura-user-id` session variable ie: themselves.

## Command Permissions​

Command permissions determine which roles can execute specific commands by defining one boolean value of `allowExecution` for each role.

### Example​

For a command named `send_abandoned_cart_email` , the permissions might look like:

```
kind :  CommandPermissions
version :  v1
definition :
   commandName :  send_abandoned_cart_email
   permissions :
   -   role :  admin
     allowExecution :   true
   -   role :  customer
     allowExecution :   false
```

In the above example the `admin` role can execute the `send_abandoned_cart_email` command, but the `customer` role
cannot.

No access for undefined roles

If a role doesn't have any permissions defined for a command, it won't have the ability to execute that command.

## Testing Permissions​

You can test permissions directly in the Hasura Console's API interface:

1. Define the desired permissions for a particular type, model, or command in your metadata.
2. Make a request through the Hasura DDN Console GraphiQL API interface and send the session variables as request
headers (e.g., a role you've defined permissions for).
3. Check the returned data to ensure it adheres to your permission configurations.


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/auth/authorization/index/#introduction)
- [ Type Permissions ](https://hasura.io/docs/3.0/auth/authorization/index/#type-permissions)
    - [ Example ](https://hasura.io/docs/3.0/auth/authorization/index/#example)
- [ Model Permissions ](https://hasura.io/docs/3.0/auth/authorization/index/#model-permissions)
    - [ Example ](https://hasura.io/docs/3.0/auth/authorization/index/#example-1)
- [ Command Permissions ](https://hasura.io/docs/3.0/auth/authorization/index/#command-permissions)
    - [ Example ](https://hasura.io/docs/3.0/auth/authorization/index/#example-2)
- [ Testing Permissions ](https://hasura.io/docs/3.0/auth/authorization/index/#testing-permissions)
