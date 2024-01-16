# Remote Schema Permissions

## Introduction​

Hasura supports[ role-based authorization ](https://hasura.io/docs/latest/auth/authorization/index/)for Remote Schemas.

Remote Schema permissions can be defined to:

1. Expose only certain parts of the Remote Schema to a role
2. Preset arguments with static values or session variables for any field.


Supported from

Remote Schema permissions are supported in Hasura GraphQL Engine versions `v2.0.0` and above.

Enable Remote Schema permissions

Remote Schema permissions are **not** enabled by default.

To enable them, you will have to run the GraphQL Engine either with the server flag `--enable-remote-schema-permissions` or environment variable `HASURA_GRAPHQL_ENABLE_REMOTE_SCHEMA_PERMISSIONS` set to `true` .

When Remote Schema permissions are not enabled, all Remote Schemas are considered to be public entities, i.e. all roles
will have unrestricted access to the Remote Schemas. Once enabled, access to Remote Schemas will be restricted for all
roles (other than `admin` ) unless explicit permissions for the Remote Schema fields are granted to the roles.

## Role based Remote Schemas​

Role based Remote Schemas allow you to expose only certain parts of the Remote Schema . You can choose to remove any
fields from objects, interfaces and input object types, doing this will ensure that these fields are not exposed for the
role and they will not be able to query the fields that have been hidden.

 **For example** , let's say we have the following Remote Schema added to the GraphQL Engine:

```
type   User   {
   id           ID !
   first_name   String !
   last_name    String !
   phone        String !
   email        String !
}
type   Query   {
   user ( id :   ID ! )   :   User
   get_users_by_name   ( first_name :   String ! ,   last_name : String ) :   [ User ]
}
```

Now, we want to expose only certain fields of the `User` object for the `public` role here. The `public` role should not
be allowed to access the `id` , `email` and `phone` fields of the `User` object. Now, since the `public` role doesn't
have access to the `id` field of the `User` object and let's say that the `id` argument of the `user` field defined in
the `Query` object is the same as the `id` field of the `User` object, there will be no way of exposing the `user` field
in the `Query` object, so we'll remove that field as well.

We can accomplish this by specifying the restricted schema (in GraphQL IDL format) for the `public` role. In the above
case, it will be:

```
type   User   {
   first_name   String !
   last_name    String !
}
type   Query   {
   get_users_by_name   ( first_name :   String ! ,   last_name :   String ) :   [ User ]
}
```

We use the above schema document to configure the Remote Schema permissions for the `public` role by using the[ add_remote_schema_permissions ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-schema-permissions/#metadata-add-remote-schema-permissions)Metadata API.

You can modify different[ GraphQL Types ](https://spec.graphql.org/June2018/#sec-Types)in the following manner:

1. Scalar - A scalar definition cannot be modified differently from its corresponding Remote Schema scalar definition.
2. Object - An object can omit some of the fields from its definition.
3. Interface - An interface, like the object type, can omit some of the fields from its definition.
4. Union - A union can be modified to only support a subset of the `possibleTypes` of its original union definition.
5. Enum - An enum can be configured to omit some enum values from its definition.
6. Input object - An input object, just like object type, can omit some of the (input) fields from its definition.


In a[ field definition ](https://spec.graphql.org/June2018/#FieldDefinition)the arguments can be configured to only
expose a subset of the arguments defined.

For example, let's consider the Remote Schema used in the example above, but in this case we want the `public` role to
use the `get_user_by_name` with only the `first_name` argument and the `public` role should not be able to access the `last_name` argument. The schema should look like:

```
type   User   {
   first_name   String !
   last_name    String !
}
type   Query   {
   get_users_by_name   ( first_name :   String ! ) :   [ User ]
}
```

## Argument presets​

The role-based schema only helps in changing the type definitions that are exposed. Argument presets are used to
constrain the input values in fields.

Argument presets automatically inject values from session variables or static values during execution. Arguments which
are preset will not be exposed in the schema. Argument presets are set on an argument value using the `@preset` directive.

Note

A preset value can be defined only at the `INPUT_FIELD_DEFINITION` and `ARGUMENT_DEFINITION` system directive locations
i.e. only at an input object field or an argument field.

For example, let's say we have the following Remote Schema added to the GraphQL Engine:

```
type   User   {
   id           ID !
   first_name   String !
   last_name    String !
   phone        String !
   email        String !
}
type   Activity   {
   name            String !
   activity_type   String !
   created_at      String !
}
type   Query   {
   get_user ( id :   ID ! )   :   User
   get_user_activities ( user_id :   ID ! ,   limit :   Int ! ) :   [ Activity ]
}
```

We want to configure the `user` role to only be able to query their own record. To do this, we need to preset the `id` parameter of the `get_user` field defined in the `Query` object. Let's say we have the value of the `id` argument set in
one of the[ session variables ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables), we can preset the `id` argument with the session variable. Using the above schema, we can do that in the following manner:

```
type   Query   {
   get_user ( id :   ID !   @preset ( value :   "x-hasura-user-id" ) )   :   User
   get_user_activities ( user_id :   ID ! ,   limit :   Int ! )
}
```

Configuring the Remote Schema for the `user` role with the above schema will remove the `id` argument from the schema
and the value of the `id` argument will get injected via the `x-hasura-user-id` session variable, whenever the `user` role executes a query containing the `get_user` field.

Preset values can also be static values.

For example:

Suppose, we want the `user` role to allow to only get 10 of the user activities using the `get_user_activities` field,
we can do that by setting a `preset` value for the `limit` argument of the `get_user_activities` to 10. The schema
implementing this change should look like:

```
type   Query   {
   get_user ( id :   ID !   @preset ( value :   "x-hasura-user-id" ) ) :   User
   get_user_activities ( user_id :   ID ! ,   limit :   Int !   @preset ( value :   10 ) ) :   [ Activity ]
}
```

Note

By default, any preset string value in the format of `x-hasura-*` is assumed to be a[ session variable ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables) `. To override this behaviour i.
e. to treat the value literally, the ` static `argument equal to` true `needs to be added in the` preset `directive. In the following example, the` x-hasura-user-id`
will be treated literally.

`get_user ( id :   ID !   @preset ( value :   "x-hasura-user-id" ,   static :   true ) )   :   User`

## Input object field presets​

Input object fields can also have preset values set. When an input object contains multiple fields and only some of them
have a preset set, the other fields which don't contain a preset can be queried by the user and when the query is
executed, the user provided arguments are merged with the input object field preset arguments.

Let's see an example, to see input object field presets in action.

Suppose, a Remote Schema with the following schema is added to the GraphQL Engine:

```
input   MessageInput   {
   from :   ID !
   to :   ID !
   content :   String !
}
type   Message   {
   from :   ID !
   to :   ID !
   content :   String
}
type   Query   {
   get_user_messages ( user_id :   ID ! ) :   [ Message ]
}
type   Mutation   {
   create_message ( message :   MessageInput ! ) :   Bool
}
```

We want to configure the Remote Schema in a way that when the `user` role creates a new message (using `create_message` ), we want the value of the `from` field of the `MessageInput` to come from the `x-hasura-user-id` session variable and the other fields ( `to` and `content` ) to be set by the user. The schema for the `user` role should
be configured in the following manner:

```
input   MessageInput   {
   from :         ID !   @preset ( value :   "x-hasura-user-id" )
   to :           ID !
   content :      String !
}
type   Message   {
   from :      ID !
   to :        ID !
   content :   String
}
type   Query   {
   get_user_messages ( user_id :   ID ! ) :   [ Message ]
}
type   Mutation   {
   create_message ( message :   MessageInput ! )
}
```

Now, when the `user` role wants to create a new message, they can do it in the following manner:

```
mutation   {
   create_message ( message :   {   to :   "2" ,   content :   "hello world"   } )
}
```

The `from` field will get injected into the input object before the GraphQL Engine queries the remote server. The final
query that will be sent to the remote server will be:

```
mutation   {
   create_message ( message :   {   to :   "2" ,   content :   "hello world" ,   from :   "<x-hasura-user-id>"   } )
}
```

## Add Remote Schema permissions​

### Step 1: Add a Remote Schema​

Add a Remote Schema as described[ here ](https://hasura.io/docs/latest/remote-schemas/adding-schema/), if the schema isn't already added.

### Step 2: Set permissions​

- Console
- CLI
- API


- Head to the `Remote Schemas -> [remote-schema-name] -> Permissions` tab.
- Select an existing role or create a new role by entering a role name (say `user` ) in the `Enter new role` box.
- Click the permissions column next to the role.
- Select the schema fields that the role is allowed to access and set any presets.
- Hit `Save Permissions` .


Image: [ Opening the remote relationship section ](https://hasura.io/docs/assets/images/remote-schemas-user-role-c4c40d5543f748ab6553f3abd764d4f5.png)

You can add a new role or edit the permissions for an existing role by editing the `metadata -> remote_schemas.yaml` file:

Add the subset of the Remote Schema that the role is allowed to access and set any presets.

```
-   name :  countries
   definition :
     url :  https : //countries.trevorblades.com/
     timeout_seconds :   60
   comment :   'remote schema permissions for role: user'
   permissions :
     -   role :  user
       definition :
         schema :   | -
          schema   {   query :  Query  }
          type Continent  {  
             countries :   [ Country ! ] !
             name :  String !
           }
          type Country  {
             name :  String !
             capital :  String
           }   
          type Query  {
             continent(code :   ID!) :  Continent
           }
```

Apply the Metadata by running:

`hasura metadata apply`

You can create Remote Schema permissions by using the[ add_remote_schema_permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-schema-permissions/#metadata-add-remote-schema-permissions):

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "add_remote_schema_permissions" ,
   "args" :   {
     "remote_schema"   :   "countries" ,
     "role"   :   "user" ,
     "definition"   :   {
         "schema"   :   "schema { query: Query } type Continent { countries: [Country!]! name : String!} type Country { name: String! capital: String } type Query { continent(code: ID!): Continent}"
     } ,
     "comment" :   "remote schema permissions for role: user"
   }
}
```

### Step 3: Test and verify the permissions​

Head to the `API` section. Add the session variable `X-Hasura-Role` with the value as the role for which we set
permissions in the previous step.

As we see, the role `user` has access restricted to certain fields of the Remote Schema.

Additional Resources

Data Federation with Hasura -[ Watch Webinar ](https://hasura.io/events/webinar/data-federation-hasura-graphql/?pg=docs&plcmt=body&cta=watch-webinar&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-permissions/#introduction)
- [ Role based Remote Schemas ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-permissions/#role-based-remote-schemas)
- [ Argument presets ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-permissions/#argument-presets)
- [ Input object field presets ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-permissions/#input-object-field-presets)
- [ Add Remote Schema permissions ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-permissions/#add-remote-schema-permissions)
    - [ Step 1: Add a Remote Schema ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-permissions/#step-1-add-a-remote-schema)

- [ Step 2: Set permissions ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-permissions/#step-2-set-permissions)

- [ Step 3: Test and verify the permissions ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-permissions/#step-3-test-and-verify-the-permissions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)