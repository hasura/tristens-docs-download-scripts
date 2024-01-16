# Metadata API Reference: Relationships

## Introduction​

When retrieving data from tables, it is very helpful if we can also
fetch the related data alongside the columns. This is where
relationships come in. They can be considered as pseudo columns for a
table to access the related data.

For a simple `article/author` schema, the following relationships exist:

- `author` of an `article`
- `articles` of an `author`


There are two kinds of relationships:

- one-to-one or `object relationships` (e.g. `author` ).
- one-to-many or `array relationships` (e.g. `articles` ).


The above represents the same table relationship from different
perspectives: there is a single `author` for every `article` (one-to-one), but there may be multiple `articles` for every `author` (one-to-many).

A table relationship may be one-to-one from both perspectives. For
example, given tables `author` and `author_details` , if the `author_details` table has a primary key `author_id` which is a foreign
key to the `author` table's primary key `id` . In this case there will be
a single `author` for every `author_details` and a single `details` for
every `author` 

Supported from

The Metadata API is supported for versions `v2.0.0` and above and
replaces the older[ schema/Metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

## pg_create_object_relationship​

 `create_object_relationship` is used to create an object relationship on
a table. There cannot be an existing column or relationship with the
same name.

There are 3 ways in which you can create an object relationship.

### 1. Using foreign key constraint on a column​

Create an `object relationship`  `author` on `article`  *table* , *using* the *foreign_key_constraint_on* the `author_id` column:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_create_object_relationship" ,
     "args" :   {
         "table" :   "article" ,
         "name" :   "author" ,
         "source" :   "default" ,
         "using" :   {
             "foreign_key_constraint_on"   :   [ "author_id" ]
         }
     }
}
```

Note

In the case that the key uses only a single column it is permissible to
give just a string instead of a list, i.e.: `"foreign_key_constraint_on" : "author_id"` .

### 2. Using foreign key constraint on a remote table​

Create an `object relationship`  `details` on `author`  *table* , *using* the *foreign_key_constraint_on* the `author_details`  *table* 's `author_id`  *column* :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "create_object_relationship" ,
     "args" :   {
         "table" :   "author" ,
         "name" :   "details" ,
         "using" :   {
             "foreign_key_constraint_on"   :   {
                 "table" :   "author_details" ,
                 "columns" :   [ "author_id" ]
             }
         }
     }
}
```

Deprecation

For compatibility with previous versions we also support the form of `foreign_key_constraint_on` with a `column` -field, e.g.:

```
{
   "foreign_key_constraint_on" :   {
     "table" :   "author_details" ,
     "column" :   "author_id"
   }
}
```

This form is deprecated in favor of the more general `columns` field.

Supported from

Relationships via remote table are supported for versions `v2.0.0-alpha.3` and above.

### 3. Manual configuration​

This is an advanced feature which is mostly used to define relationships
on or to views. We cannot rely on foreign key constraints as they are
not valid to or from views. So, when using manual configuration, we have
to specify the remote table and how columns in this table are mapped to
the columns of the remote table.

Let's say we have a view called `article_detail` which has three columns `article_id` and `view_count` and `average_rating` . We can now define an
object relationship called `article_detail` on the `article` table as
follows:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_create_object_relationship" ,
     "args" :   {
         "table" :   "article" ,
         "name" :   "article_detail" ,
         "source" :   "default" ,
         "using" :   {
             "manual_configuration"   :   {
                 "remote_table"   :   "article_detail" ,
                 "column_mapping"   :   {
                     "id"   :   "article_id"
                 }
             }
         }
     }
}
```

Note

It is easy to make mistakes while using `manual_configuration` . One
simple check is to ensure that foreign key constraint semantics are
valid on the columns being used in `column_mapping` . In the previous
example, if it was allowed, a foreign key constraint could have been
defined on `article` table's `id` column to `article_detail` view's `article_id` column.

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| name | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | Name of the new relationship |
| using | true | [ ObjRelUsing ](https://hasura.io/docs/latest/api-reference/syntax-defs/#objrelusing) | Use one of the available ways to define an object relationship |
| comment | false | text | comment |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_create_array_relationship​

 `create_array_relationship` is used to create an array relationship on a
table. There cannot be an existing column or relationship with the same name.

There are 2 ways in which you can create an array relationship.

### 1. Using foreign key constraint on a column​

Create an `array relationship`  `articles` on `author`  *table* , *using* the *foreign_key_constraint_on* the `author_id` column of the `article` table:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_create_array_relationship" ,
     "args" :   {
         "table" :   "author" ,
         "name" :   "articles" ,
         "source" :   "default" ,
         "using" :   {
             "foreign_key_constraint_on"   :   {
                 "table"   :   "article" ,
                 "columns"   :   [ "author_id" ]
             }
         }
     }
}
```

Deprecation

For compatibility with previous version we also support the form of `foreign_key_constraint_on` with a `column` -field, e.g.:

```
{
   "foreign_key_constraint_on" :   {
     "table" :   "author_details" ,
     "column" :   "author_id"
   }
}
```

This form is deprecated in favor of the more general `columns` field.

### 2. Manual configuration​

This is an advanced feature which is mostly used to define relationships
on or to views. We cannot rely on foreign key constraints as they are
not valid to or from views. So, when using manual configuration, we have
to specify the remote table and how columns in this table are mapped to
the columns of the remote table.

Let's say we have a view called `article_detail` which has four columns `author_id` , `article_id` , `view_count` and `average_rating` . We can now
define an array relationship called `article_details` on the `author` table as follows:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_create_array_relationship" ,
     "args" :   {
         "table" :   "author" ,
         "name" :   "article_details" ,
         "source" :   "default" ,
         "using" :   {
             "manual_configuration"   :   {
                 "remote_table"   :   "article_detail" ,
                 "column_mapping"   :   {
                     "id"   :   "author_id"
                 }
             }
         }
     }
}
```

Note

It is easy to make mistakes while using `manual_configuration` . One
simple check is to ensure that foreign key constraint semantics are
valid on the columns being used in `column_mapping` . In the previous
example, if it was allowed, a foreign key constraint could have been
defined on the `author` table's `id` column to `article_detail` view's `author_id` column.

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| name | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | Name of the new relationship |
| using | true | [ ArrRelUsing ](https://hasura.io/docs/latest/api-reference/syntax-defs/#arrrelusing) | Use one of the available ways to define an array relationship |
| comment | false | text | comment |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_drop_relationship​

 `pg_drop_relationship` is used to drop a relationship (both object and
array) on a table. If there are other objects dependent on this
relationship like permissions and query templates, etc., the request
will fail and report the dependencies unless `cascade` is set to `true` .
If `cascade` is set to `true` , the dependent objects are also dropped.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_drop_relationship" ,
     "args" :   {
         "table" :   "article" ,
         "source" :   "default" ,
         "relationship" :   "article_detail"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| relationship | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | Name of the relationship that needs to be dropped |
| cascade | false | Boolean | When set to `true` , all the dependent items on this relationship are also dropped |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


Note

Be careful when using `cascade` . First, try running the request without `cascade` or `cascade` set to `false` .

## pg_set_relationship_comment​

 `pg_set_relationship_comment` is used to set/update the comment on a
relationship. Setting the comment to `null` removes it.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_set_relationship_comment" ,
     "args" :   {
         "table" :   "article" ,
         "source" :   "default" ,
         "name" :   "article_detail" ,
         "comment"   :   "has extra information about an article like count etc."
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| relationship | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | The relationship |
| comment | false | Text | Comment |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_rename_relationship​

 `pg_rename_relationship` is used to modify the name of an existing relationship.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "pg_rename_relationship" ,
     "args" :   {
         "table" :   "article" ,
         "name" :   "article_details" ,
         "source" :   "default" ,
         "new_name" :   "article_detail"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| name | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | The relationship |
| new_name | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | New relationship name |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## pg_suggest_relationships​

 `pg_suggest_relationships` is used to suggest relationships that can be tracked by the `pg_create_*_relationship` API.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_suggest_relationships" ,
   "version" :   1 ,
   "args" :   {
     "omit_tracked" :   true ,
     "source" :   "chinook" ,
     "tables" :   [ [ "Artist" ] ]
   }
}
```

### Args syntax​

| Key | Required | Default | Schema | Description |
|---|---|---|---|---|
| source | false |  `default`  | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | The source to suggest relationships for |
| tables | false | All Tables | [[ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename)] | List of tables to consider for suggestions |
| omit_tracked | false |  `false`  |  `Boolean`  | Don't re-suggest tracked relationships |


Note

All other source kinds are also supported by using the type `{KIND}_suggest_relationships` .
For example, Snowflake would be: `snowflake_suggest_relationships` , etc.

## mssql_create_object_relationship​

 `create_object_relationship` is used to create an object relationship on
a table. There cannot be an existing column or relationship with the
same name.

There are 3 ways in which you can create an object relationship.

### 1. Using foreign key constraint on a column​

Create an `object relationship`  `author` on `article`  *table* , *using* the *foreign_key_constraint_on* the `author_id` column:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_create_object_relationship" ,
     "args" :   {
         "table" :   "article" ,
         "name" :   "author" ,
         "source" :   "default" ,
         "using" :   {
             "foreign_key_constraint_on"   :   [ "author_id" ]
         }
     }
}
```

Note

In the case that the key uses only a single column it is permissible to
give just a string instead of a list, i.e.: `"foreign_key_constraint_on" : "author_id"` .

### 2. Using foreign key constraint on a remote table​

Create an `object relationship`  `details` on `author`  *table* , *using* the *foreign_key_constraint_on* the `author_details`  *table* 's `author_id`  *column* :

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "create_object_relationship" ,
     "args" :   {
         "table" :   "author" ,
         "name" :   "details" ,
         "using" :   {
             "foreign_key_constraint_on"   :   {
                 "table" :   "author_details" ,
                 "columns" :   [ "author_id" ]
             }
         }
     }
}
```

Deprecation

For compatibility with previous versions we also support the form of `foreign_key_constraint_on` with a `column` -field, e.g.:

```
{
   "foreign_key_constraint_on" :   {
     "table" :   "author_details" ,
     "column" :   "author_id"
   }
}
```

This form is deprecated in favor of the more general `columns` field.

Supported from

Relationships via remote table are supported for versions `v2.0.0-alpha.3` and above.

### 3. Manual configuration​

This is an advanced feature which is mostly used to define relationships
on or to views. We cannot rely on foreign key constraints as they are
not valid to or from views. So, when using manual configuration, we have
to specify the remote table and how columns in this table are mapped to
the columns of the remote table.

Let's say we have a view called `article_detail` which has three columns `article_id` and `view_count` and `average_rating` . We can now define an
object relationship called `article_detail` on the `article` table as
follows:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_create_object_relationship" ,
     "args" :   {
         "table" :   "article" ,
         "name" :   "article_detail" ,
         "source" :   "default" ,
         "using" :   {
             "manual_configuration"   :   {
                 "remote_table"   :   "article_detail" ,
                 "column_mapping"   :   {
                     "id"   :   "article_id"
                 }
             }
         }
     }
}
```

Note

It is easy to make mistakes while using `manual_configuration` . One
simple check is to ensure that foreign key constraint semantics are
valid on the columns being used in `column_mapping` . In the previous
example, if it was allowed, a foreign key constraint could have been
defined on `article` table's `id` column to `article_detail` view's `article_id` column.

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| name | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | Name of the new relationship |
| using | true | [ ObjRelUsing ](https://hasura.io/docs/latest/api-reference/syntax-defs/#objrelusing) | Use one of the available ways to define an object relationship |
| comment | false | text | comment |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_create_array_relationship​

 `create_array_relationship` is used to create an array relationship on a
table. There cannot be an existing column or relationship with the same
name.

There are 2 ways in which you can create an array relationship.

### 1. Using foreign key constraint on a column​

Create an `array relationship`  `articles` on `author`  *table* , *using* the *foreign_key_constraint_on* the `author_id` column of the `article` table:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_create_array_relationship" ,
     "args" :   {
         "table" :   "author" ,
         "name" :   "articles" ,
         "source" :   "default" ,
         "using" :   {
             "foreign_key_constraint_on"   :   {
                 "table"   :   "article" ,
                 "columns"   :   [ "author_id" ]
             }
         }
     }
}
```

Deprecation

For compatibility with previous version we also support the form of `foreign_key_constraint_on` with a `column` -field, e.g.:

```
{
   "foreign_key_constraint_on" :   {
     "table" :   "author_details" ,
     "column" :   "author_id"
   }
}
```

This form is deprecated in favor of the more general `columns` field.

### 2. Manual configuration​

This is an advanced feature which is mostly used to define relationships
on or to views. We cannot rely on foreign key constraints as they are
not valid to or from views. So, when using manual configuration, we have
to specify the remote table and how columns in this table are mapped to
the columns of the remote table.

Let's say we have a view called `article_detail` which has four columns `author_id` , `article_id` , `view_count` and `average_rating` . We can now
define an array relationship called `article_details` on the `author` table as follows:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_create_array_relationship" ,
     "args" :   {
         "table" :   "author" ,
         "name" :   "article_details" ,
         "source" :   "default" ,
         "using" :   {
             "manual_configuration"   :   {
                 "remote_table"   :   "article_detail" ,
                 "column_mapping"   :   {
                     "id"   :   "author_id"
                 }
             }
         }
     }
}
```

Note

It is easy to make mistakes while using `manual_configuration` . One
simple check is to ensure that foreign key constraint semantics are
valid on the columns being used in `column_mapping` . In the previous
example, if it was allowed, a foreign key constraint could have been
defined on the `author` table's `id` column to `article_detail` view's `author_id` column.

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| name | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | Name of the new relationship |
| using | true | [ ArrRelUsing ](https://hasura.io/docs/latest/api-reference/syntax-defs/#arrrelusing) | Use one of the available ways to define an array relationship |
| comment | false | text | comment |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_drop_relationship​

 `mssql_drop_relationship` is used to drop a relationship (both object
and array) on a table. If there are other objects dependent on this
relationship like permissions and query templates, etc., the request
will fail and report the dependencies unless `cascade` is set to `true` .
If `cascade` is set to `true` , the dependent objects are also dropped.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_drop_relationship" ,
     "args" :   {
         "table" :   "article" ,
         "source" :   "default" ,
         "relationship" :   "article_detail"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| relationship | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | Name of the relationship that needs to be dropped |
| cascade | false | Boolean | When set to `true` , all the dependent items on this relationship are also dropped |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


Note

Be careful when using `cascade` . First, try running the request without `cascade` or `cascade` set to `false` .

## mssql_set_relationship_comment​

 `mssql_set_relationship_comment` is used to set/update the comment on a
relationship. Setting the comment to `null` removes it.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_set_relationship_comment" ,
     "args" :   {
         "table" :   "article" ,
         "source" :   "default" ,
         "name" :   "article_detail" ,
         "comment"   :   "has extra information about an article like count etc."
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| relationship | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | The relationship |
| comment | false | Text | Comment |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_rename_relationship​

 `mssql_rename_relationship` is used to modify the name of an existing relationship.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "mssql_rename_relationship" ,
     "args" :   {
         "table" :   "article" ,
         "name" :   "article_details" ,
         "source" :   "default" ,
         "new_name" :   "article_detail"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| name | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | The relationship |
| new_name | true | [ RelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#relationshipname) | New relationship name |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |


## mssql_suggest_relationships​

 `mssql_suggest_relationships` is used to suggest relationships that can be tracked by the `mssql_create_*_relationship` API.

An example:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_suggest_relationships" ,
   "version" :   1 ,
   "args" :   {
     "omit_tracked" :   true ,
     "source" :   "chinook" ,
     "tables" :   [ [ "Artist" ] ]
   }
}
```

### Args syntax​

| Key | Required | Default | Schema | Description |
|---|---|---|---|---|
| source | false |  `default`  | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | The source to suggest relationships for |
| tables | false | All Tables | [[ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename)] | List of tables to consider for suggestions |
| omit_tracked | false |  `false`  |  `Boolean`  | Don't re-suggest tracked relationships |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#introduction)
- [ pg_create_object_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#metadata-pg-create-object-relationship)
    - [ 1. Using foreign key constraint on a column ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#1-using-foreign-key-constraint-on-a-column)

- [ 2. Using foreign key constraint on a remote table ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#2-using-foreign-key-constraint-on-a-remote-table)

- [ 3. Manual configuration ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#metadata-pg-manual-obj-relationship)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#metadata-pg-create-object-relationship-syntax)
- [ pg_create_array_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#metadata-pg-create-array-relationship)
    - [ 1. Using foreign key constraint on a column ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#1-using-foreign-key-constraint-on-a-column-1)

- [ 2. Manual configuration ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#2-manual-configuration)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#metadata-pg-create-array-relationship-syntax)
- [ pg_drop_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#metadata-pg-drop-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#metadata-pg-drop-relationship-syntax)
- [ pg_set_relationship_comment ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#metadata-pg-set-relationship-comment)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#metadata-pg-set-relationship-comment-syntax)
- [ pg_rename_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#metadata-pg-rename-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#metadata-pg-rename-relationship-syntax)
- [ pg_suggest_relationships ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#pg-suggest-relationships)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#pg-suggest-relationship-syntax)
- [ mssql_create_object_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-create-object-relationship)
    - [ 1. Using foreign key constraint on a column ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#1-using-foreign-key-constraint-on-a-column-2)

- [ 2. Using foreign key constraint on a remote table ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#2-using-foreign-key-constraint-on-a-remote-table-1)

- [ 3. Manual configuration ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-manual-obj-relationship)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-create-object-relationship-syntax)
- [ mssql_create_array_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-create-array-relationship)
    - [ 1. Using foreign key constraint on a column ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#1-using-foreign-key-constraint-on-a-column-3)

- [ 2. Manual configuration ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#2-manual-configuration-1)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-create-array-relationship-syntax)
- [ mssql_drop_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-drop-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-drop-relationship-syntax)
- [ mssql_set_relationship_comment ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-set-relationship-comment)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-set-relationship-comment-syntax)
- [ mssql_rename_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-rename-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-rename-relationship-syntax)
- [ mssql_suggest_relationships ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-suggest-relationships)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-pg-rename-relationship/#mssql-suggest-relationship-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)