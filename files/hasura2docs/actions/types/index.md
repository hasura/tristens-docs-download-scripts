# Custom GraphQL Types

## Introduction​

You can add custom GraphQL types in Hasura that you can utilize for defining your actions.

Limitations

It is currently not possible to define `Interfaces` and `Union types` as custom types

## Object types​

The most basic components of a GraphQL schema are object types, which just represent a kind of object a GraphQL query
can return, and what fields it has. In the GraphQL SDL, we might represent it like this:

```
type   UserInfo   {
   accessToken :   String !
   userId :   Int !
}
```

This is an object type called `UserInfo` that has two fields:

- `accessToken` : This field is of type `String!` (non-nullable `String` )
- `userId` : This field is of type `Int!` (non-nullable `Int` )


From version `v2.2.0` onwards, Hasura GraphQL Engine supports nested objects.

For example, you can define a type like the following:

```
type   UserInfo   {
   accessToken :   String !
   userId :   Int !
   user :   UserObj !
}
type   UserObj   {
   name :   String !
   favFood :   String !
   isAdmin :   Boolean !
}
```

Recursive nested objects are also supported.

For example, you can use the following type:

```
type   UserObj   {
   name :   String !
   favFood :   String !
   isAdmin :   Boolean !
   friends :   [ UserObj ] !
}
```

[ See reference ](https://graphql.org/learn/schema/#object-types-and-fields)

### Relationships​

Custom object types can be connected to the rest of the graph by setting up[ action relationships ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/action-relationships/)with tables/views.

 **For example** , given the object type:

```
type   UserInfo   {
   accessToken :   String !
   userId :   Int !
}
```

and tables:

```
user   ( id  int ,  name  text )
order   ( id  int ,  user_id  int ,   . . . )
```

We can create:

- an **object relationship** called `loggedInUser` between the `UserInfo` object type and the `user` table via the `UserInfo.userId` and `user.id` fields.
- an **array relationship** called `userOrders` between the `UserInfo` object type and the `order` table via the `UserInfo.userId` and `order.user_id` fields.


The object type will now be modified as:

```
type   UserInfo   {
   accessToken :   String !
   userId :   Int !
   loggedInUser :   user
   userOrders :   [ order ]
}
```

Note

Only fields with non-list scalar types (e.g. `Int` , `String` ) can be used to define relationships

Limitations

Hasura has the following limitations for relationship in nested object types:

1. For nested objects, relationships can only be defined for top-level fields. For example, for the following type
definition:relationships can only be defined using `accessToken` and `userID` , you cannot use `name` , `favFood` or `isAdmin` fields in a relationship definition.
2. For `async` actions, you cannot have nested object types and relationships in the same action.


For nested objects, relationships can only be defined for top-level fields. For example, for the following type
definition:

```
type   UserInfo   {
   accessToken :   String !
   userId :   Int !
   user :   UserObj !
}
type   UserObj   {
   name :   String !
   favFood :   String !
   isAdmin :   Boolean !
}
```

relationships can only be defined using `accessToken` and `userID` , you cannot use `name` , `favFood` or `isAdmin` fields in a relationship definition.

For `async` actions, you cannot have nested object types and relationships in the same action.

## Input types​

You can pass complex objects as arguments to queries and mutations. This is particularly valuable in cases where you
might want to pass in a whole object to be created. In the GraphQL SDL, input types look exactly the same as regular
object types, but with the keyword input instead of type:

```
input   LoginInfo   {
   username :   String !
   password :   String !
}
```

A field of an input type could be a `scalar` , an `enum` or another input type.

[ See reference ](https://graphql.org/learn/schema/#input-types)

## Scalar types​

A GraphQL object type has a name and fields, but at some point those fields have to resolve to some concrete data.
That's where the scalar types come in: they represent the leaves of the query.

### Inbuilt scalars​

Hasura comes with some default GraphQL scalars that you can directly start using while defining your actions:

- `Int` : A signed 32‐bit integer.
- `Float` : A signed double-precision floating-point value.
- `String` : A UTF‐8 character sequence.
- `Boolean` : true or false.
- `ID` : The ID scalar type represents a unique identifier, often used to refetch an object or as the key for a cache.
The ID type is serialized in the same way as a String; however, defining it as an ID signifies that it is not intended
to be human‐readable.


[ See reference ](https://graphql.org/learn/schema/#scalar-types)

### Custom scalars​

Hasura allows you to define custom scalars. For example, if you want to define a scalar called `Date` , you can define it
like.

`scalar   Date`

These scalars can be used as arguments of queries and mutations or as fields of object types and input types.

Postgres scalars

Postgres base types are implicitly made available as GraphQL scalars; there is no need to declare them separately. For
example, in the definition

```
type   User   {
   id :   uuid !
   name :   String !
   location :   geography
}
```

the `uuid` and `geography` types are assumed to refer to Postgres scalars (assuming no other definition for them is
provided).

## List types​

You can define a list of objects or scalars as the response type for an action.

The action definition for list (of objects) response type looks something like this:

```
type   Mutation   {
   userLogin ( username :   String ! ,   password :   String ! ) :   [ UserInfo ]
}
```

For corresponding custom object type definition of `UserInfo` , refer to[ Object Types ](https://hasura.io/docs/latest/actions/types/index/#object-types)

In case the response type is a list of scalars (let's say, `Int` ), the output type in the above action definition can be `[Int]` .

## Enum types​

Enums are a special kind of scalar that is restricted to a particular set of allowed values. This allows you to:

- Validate that any arguments of this type are one of the allowed values
- Communicate through the type system that a field will always be one of a finite set of values


Here's what an enum definition might look like in the GraphQL schema language:

```
enum   Color   {
   RED
   GREEN
   BLUE
}
```

This means that wherever we use the type `Color` in our schema, we expect it to be exactly one of RED, GREEN, or BLUE.

[ See reference ](https://graphql.org/learn/schema/#enumeration-types)

Additional Resources

Introduction to Hasura Actions -[ View Recording ](https://hasura.io/events/webinar/hasura-actions/?pg=docs&plcmt=body&cta=view-recording&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/actions/types/index/#introduction)
- [ Object types ](https://hasura.io/docs/latest/actions/types/index/#object-types)
    - [ Relationships ](https://hasura.io/docs/latest/actions/types/index/#relationships)
- [ Input types ](https://hasura.io/docs/latest/actions/types/index/#input-types)
- [ Scalar types ](https://hasura.io/docs/latest/actions/types/index/#scalar-types)
    - [ Inbuilt scalars ](https://hasura.io/docs/latest/actions/types/index/#inbuilt-scalars)

- [ Custom scalars ](https://hasura.io/docs/latest/actions/types/index/#custom-scalars)
- [ List types ](https://hasura.io/docs/latest/actions/types/index/#list-types)
- [ Enum types ](https://hasura.io/docs/latest/actions/types/index/#enum-types)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)