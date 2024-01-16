# Schema/Metadata API Reference: Relationships (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

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

## create_object_relationship​

 `create_object_relationship` is used to create an object relationship on
a table. There cannot be an existing column or relationship with the
same name.

There are 3 ways in which you can create an object relationship.

### 1. Using foreign key constraint on a column​

Create an `object relationship`  `author` on `article`  *table* , *using* the *foreign_key_constraint_on* the `author_id` column:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "create_object_relationship" ,
     "args" :   {
         "table" :   "article" ,
         "name" :   "author" ,
         "using" :   {
             "foreign_key_constraint_on"   :   "author_id"
         }
     }
}
```

### 2. Using foreign key constraint on a remote table​

Create an `object relationship`  `details` on `author`  *table* , *using* the *foreign_key_constraint_on* the `author_details`  *table* 's `id`  *column* :

```
POST   /v1/query   HTTP/1.1
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
                 "column" :   "author_id"
             }
         }
     }
}
```

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
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "create_object_relationship" ,
     "args" :   {
         "table" :   "article" ,
         "name" :   "article_detail" ,
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


## create_array_relationship​

 `create_array_relationship` is used to create an array relationship on a
table. There cannot be an existing column or relationship with the same
name.

There are 2 ways in which you can create an array relationship.

### 1. Using foreign key constraint on a column​

Create an `array relationship`  `articles` on `author`  *table* , *using* the *foreign_key_constraint_on* the `author_id` column of the `article` table:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "create_array_relationship" ,
     "args" :   {
         "table" :   "author" ,
         "name" :   "articles" ,
         "using" :   {
             "foreign_key_constraint_on"   :   {
                 "table"   :   "article" ,
                 "column"   :   "author_id"
             }
         }
     }
}
```

### 2. Manual configuration​

This is an advanced feature which is mostly used to define relationships
on or to views. We cannot rely on foreign key constraints as they are
not valid to or from views. So, when using manual configuration, we have
to specify the remote table and how columns in this table are mapped to
the columns of the remote table.

Let's say we have a view called `article_detail` which has four columns `author_id` , `article_id` , `view_count` and `average_rating` . We can now
define an array relationship called `article_details` on the `author` table as follows:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "create_array_relationship" ,
     "args" :   {
         "table" :   "author" ,
         "name" :   "article_details" ,
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


## drop_relationship​

 `drop_relationship` is used to drop a relationship (both object and
array) on a table. If there are other objects dependent on this
relationship like permissions and query templates, etc., the request
will fail and report the dependencies unless `cascade` is set to `true` .
If `cascade` is set to `true` , the dependent objects are also dropped.

An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "drop_relationship" ,
     "args" :   {
         "table" :   "article" ,
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


Note

Be careful when using `cascade` . First, try running the request without `cascade` or `cascade` set to `false` .

## set_relationship_comment​

 `set_relationship_comment` is used to set/update the comment on a
relationship. Setting the comment to `null` removes it.

An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "set_relationship_comment" ,
     "args" :   {
         "table" :   "article" ,
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


## rename_relationship​

 `rename_relationship` is used to modify the name of an existing relationship.

An example:

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" :   "rename_relationship" ,
     "args" :   {
         "table" :   "article" ,
         "name" :   "article_details" ,
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


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#introduction)
- [ create_object_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#schema-metadata-create-object-relationship)
    - [ 1. Using foreign key constraint on a column ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#1-using-foreign-key-constraint-on-a-column)

- [ 2. Using foreign key constraint on a remote table ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#2-using-foreign-key-constraint-on-a-remote-table)

- [ 3. Manual configuration ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#schema-metadata-manual-obj-relationship)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#schema-metadata-create-object-relationship-syntax)
- [ create_array_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#schema-metadata-create-array-relationship)
    - [ 1. Using foreign key constraint on a column ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#1-using-foreign-key-constraint-on-a-column-1)

- [ 2. Manual configuration ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#2-manual-configuration)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#schema-metadata-create-array-relationship-syntax)
- [ drop_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#schema-metadata-drop-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#schema-metadata-drop-relationship-syntax)
- [ set_relationship_comment ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#schema-metadata-set-relationship-comment)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#schema-metadata-set-relationship-comment-syntax)
- [ rename_relationship ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#schema-metadata-rename-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/relationship/#schema-metadata-create-array-relationship/#schema-metadata-rename-relationship-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)