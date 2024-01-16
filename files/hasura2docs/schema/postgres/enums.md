# Postgres: Enum Type Fields

## Introduction​

Enum type fields are restricted to a fixed set of allowed values.

## Enums in a database​

In a relational database such as Postgres, an enum type field in a table can be defined in two ways:

### Using native Postgres enum types​

While the most obvious solution, native enum types have significant drawbacks: they are not easily mutable. New values
cannot be added to an enum inside a transaction (that is, `ALTER TYPE ... ADD VALUE` is not supported by transactional
DDL), and values cannot be removed from an enum at all without completely dropping and recreating it (which cannot be
done if the enum is in use by *any* tables, views, or functions). Therefore, native enum types should only be used for
enums that are guaranteed to *never* change, such as days of the week.

### Using foreign-key references to a single-column table​

This approach represents an enum using ordinary relational database concepts. The enum type is represented by a table,
and the values of the enum are rows in the table. Columns in other tables that use the enum are ordinary foreign-key
references to the enum table.

For enums with values that are dynamic and may require updates, such as a list of tags or user roles, this approach is
strongly recommended. Modifying an enum defined this way is easy: simply insert, update, or delete rows in the enum
table (and updates or deletes can even be cascaded to references, and they may be done within a transaction).

## Enums in the Hasura GraphQL Engine​

Given the limitations of native Postgres enum types (as described[ above ](https://hasura.io/docs/latest/schema/postgres/enums/#pg-native-enum)), Hasura currently only
generates GraphQL enum types for enums defined using the[ referenced tables ](https://hasura.io/docs/latest/schema/postgres/enums/#pg-reference-table-enum)approach.

You may use native Postgres enum types in your database schema, but they will essentially be treated like text fields in
the generated GraphQL schema. Therefore, this guide focuses primarily on modeling an enum using a reference table, but
you may still use native Postgres enum types to help maintain data consistency in your database. You can always choose
to create a table with the values of a Postgres enum as shown in the[ section below ](https://hasura.io/docs/latest/schema/postgres/enums/#pg-create-enum-table-from-pg-enum).

 **Example:** Let’s say we have a database that tracks user information, and users may only have one of three specific
roles: user, moderator, or administrator. To represent that, we might have a `users` table with the following schema:

```
CREATE   TABLE  users  (
  id  serial   PRIMARY   KEY ,
  name  text   NOT   NULL ,
  role  text   NOT   NULL
) ;
```

Now we can insert some users into our database:

```
INSERT   INTO  users  ( name ,  role )   VALUES
   ( 'Alyssa' ,   'administrator' ) ,
   ( 'Ben' ,   'moderator' ) ,
   ( 'Gerald' ,   'user' ) ;
```

This works alright, but it doesn’t prevent us from inserting nonsensical values for `role` , such as

```
INSERT   INTO  users  ( name ,  role )   VALUES
   ( 'Hal' ,   'spaghetti' ) ;
```

which we certainly don’t want. Hence we should create an enum to restrict the allowed values.

### Creating an enum compatible table​

To represent an enum, we’re going to create an_ *enum table* , which for Hasura’s purposes is any table that
meets the following restrictions:

1. The table must have a single-column primary key of type `text` . The values of this column are the legal values of
the enum, and they must all be[ valid GraphQL enum value names ](https://graphql.github.io/graphql-spec/June2018/#EnumValue).
2. Optionally, the table may have a second column, also of type `text` , which will be used as a description of each
value in the generated GraphQL schema.
3. The table must not contain any other columns.
4. The table must contain at least 1 row.


 **For example** , to create an enum that represents our user roles, we would create the following table:

```
CREATE   TABLE  user_role  (
   value   text   PRIMARY   KEY ,
   comment   text
) ;
INSERT   INTO  user_role  ( value ,   comment )   VALUES
   ( 'user' ,   'Ordinary users' ) ,
   ( 'moderator' ,   'Users with the privilege to ban users' ) ,
   ( 'administrator' ,   'Users with the privilege to set users’ roles' ) ;
```

Creating an enum table from a native PG enum

You can create a table containing the values of a PG enum by executing the following SQL:

```
CREATE   TABLE   "<my_enum_table>"   ( value   TEXT   PRIMARY   KEY ) ;
INSERT   INTO   "<my_enum_table>"   ( value )   ( SELECT  unnest ( enum_range ( NULL :: "<my_enum>" ) ) :: text ) ;
```

Next, we need to tell Hasura that this table represents an enum.

### Setting a table as an enum table​

Once we have a table which satisfies the conditions for an enum table as described[ above ](https://hasura.io/docs/latest/schema/postgres/enums/#pg-create-enum-table), we
need to tell Hasura that this table represents an enum.

- Console
- CLI
- API


Head to the `Data -> [table-name] -> Modify` tab in the Console and toggle the switch in the `Set table as enum` section:

Image: [ Set table as enum ](data:image/png;base64,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)

```
-   table :
     schema :  public
     name :  user_role
   is_enum :   true
```

Apply the Metadata by running:

`hasura metadata apply`

1. Passing `true` for the `is_enum` option of the[ pg_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-track-table)Metadata API while tracking a
table:
2. Using the[ pg_set_table_is_enum ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-set-table-is-enum)metadata
API to change whether or not an already-tracked table should be used as an enum:


Passing `true` for the `is_enum` option of the[ pg_track_table ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-track-table)Metadata API while tracking a
table:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_track_table" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "schema" :   "public" ,
     "name" :   "user_role" ,
     "is_enum" :   true
   }
}
```

Using the[ pg_set_table_is_enum ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/#metadata-pg-set-table-is-enum)metadata
API to change whether or not an already-tracked table should be used as an enum:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_set_table_is_enum" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   {
       "schema" :   "public" ,
       "name" :   "user_role"
     } ,
     "is_enum" :   true
   }
}
```

### Using an enum table​

To set a field of a table as an enum in the GraphQL schema, we need to set a reference from it to the enum table via a
foreign key.

 **For example** , to update our `users` table to reference the `user_role` enum table:

```
ALTER   TABLE  users  ADD   CONSTRAINT
  users_role_fkey  FOREIGN   KEY   ( role )   REFERENCES  user_role ;
```

### Making queries using enum values​

Once a table has been tracked as an enum, the GraphQL schema will be updated to expose the values of the table as
GraphQL enum values i.e. only the exposed values will be permitted for all fields referencing to it.

 **For example** , the `role` column of the `users` table only permits the values in the `user_role` table:

```
type   users   {
   id :   Int !
   name :   String !
   role :   user_role_enum !
}
enum   user_role_enum   {
   " Users with the privilege to set users’ roles "
   administrator
   " Users with the privilege to ban users "
   moderator
   " Ordinary users "
   user
}
```

When making queries that filter on the `role` column, use the name of the enum value directly rather than providing a
string:

### Enums and Migrations​

As enum tables have a requirement to contain at least 1 row, it is necessary to have a migration which inserts values
into an enum table. Otherwise while applying Migrations an error would be thrown while trying to set the table as an
enum.

The migration which inserts values into an enum table needs to be between the migration creating the table and the
migration setting it as an enum.

This can be achieved via the Console by performing the following steps while setting up an enum table:

1. Create the enum table
2. Use the `RawSQL` tab of the Console to insert the enum values into the table and mark the insert as a migration
3. Set the table as an enum


You can also[ manually create migration files ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)to achieve
this.

### Current limitations​

Currently, Hasura does not automatically detect changes to the contents of enum tables, so the GraphQL schema will only
be updated after[ manually reloading metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/#reload-metadata-manual)after inserting, updating, or deleting rows from an enum table.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/enums/#introduction)
- [ Enums in a database ](https://hasura.io/docs/latest/schema/postgres/enums/#enums-in-a-database)
    - [ Using native Postgres enum types ](https://hasura.io/docs/latest/schema/postgres/enums/#pg-native-enum)

- [ Using foreign-key references to a single-column table ](https://hasura.io/docs/latest/schema/postgres/enums/#pg-reference-table-enum)
- [ Enums in the Hasura GraphQL Engine ](https://hasura.io/docs/latest/schema/postgres/enums/#enums-in-the-hasura-graphql-engine)
    - [ Creating an enum compatible table ](https://hasura.io/docs/latest/schema/postgres/enums/#pg-create-enum-table)

- [ Setting a table as an enum table ](https://hasura.io/docs/latest/schema/postgres/enums/#setting-a-table-as-an-enum-table)

- [ Using an enum table ](https://hasura.io/docs/latest/schema/postgres/enums/#using-an-enum-table)

- [ Making queries using enum values ](https://hasura.io/docs/latest/schema/postgres/enums/#making-queries-using-enum-values)

- [ Enums and Migrations ](https://hasura.io/docs/latest/schema/postgres/enums/#enums-and-migrations)

- [ Current limitations ](https://hasura.io/docs/latest/schema/postgres/enums/#current-limitations)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)