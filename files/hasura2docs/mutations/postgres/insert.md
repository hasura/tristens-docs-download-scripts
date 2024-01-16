# Postgres: Insert Mutation

## Auto-generated insert mutation schema​

 **For example** , the auto-generated schema for the insert mutation field for a table `article` looks like the following:

```
insert_article   (
   objects :   [ article_insert_input ! ] !
   on_conflict :   article_on_conflict
) :   article_mutation_response
# response of any mutation on the table "article"
type   article_mutation_response   {
   # number of affected rows by the mutation
   affected_rows :   Int !
   # data of the affected rows by the mutation
   returning :   [ article ! ] !
}
# single object insert (supported from v1.2.0)
insert_article_one   (
   object :   article_insert_input !
   on_conflict :   article_on_conflict
) :   article
```

As you can see from the schema:

- `objects` argument is necessary and you can pass multiple `objects` to the mutation.
- You can pass an `on_conflict` argument to convert the mutation to an[ upsert mutation ](https://hasura.io/docs/latest/mutations/postgres/upsert/).
- You can return the number of affected rows and the affected objects (with nested objects) in the response.
- You can use the single object insert to get the inserted object directly as the mutation response.


See the[ insert mutation API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#insert-upsert-syntax)for the full
specifications.

Note

If a table is not in the `public` Postgres schema, the insert mutation field will be of the format `insert_<schema_name>_<table_name>` .

## Insert a single object​

 **Example:** Insert a new `article` object and return the inserted article object in the response:

Using variables:

Note

 `insert_<object>_one` will **only** be available if you have select permissions on the table, as it returns the inserted
row.

Supported from

The `insert_<object>_one` mutation is supported in versions `v1.2.0` and above.

## Insert multiple objects of the same type in the same mutation​

 **Example:** Insert 2 new `article` objects and return both the article objects in the response:

Using variables:

## Insert an object and get a nested object in response​

 **Example:** Insert a new `article` object and return the inserted article object with its author in the response:

## Insert an object along with its related objects through relationships​

### One-to-one / One-to-many relationships​

Let's say an `author` has an `object relationship` called `address` to the `addresses` table and an `array relationship` called `articles` to the `articles` table.

 **Example:** Insert an `author` along with their `address` and a few `articles` .

 **How it works** 

A nested insert mutation is processed as follows:

1. The object relationship objects are inserted first, i.e. in this case, the `address` is inserted and its `id` is
collected in this step.
2. The parent object is inserted next. i.e. in this case, the `author` is now inserted with the `address_id` being set
to the `id` of the address that was inserted. Because of this, it is not allowed to pass `address_id` in the author
object if you are also providing data for the address relationship.The `id` of the author is collected in this step.
3. The array relationship objects are inserted at the end. i.e. in this case, the `articles` are now inserted with
their `author_id` set to the author's `id` collected in the step 2. Hence, it's not possible to specify `author_id` in the data for the articles relationship.


The object relationship objects are inserted first, i.e. in this case, the `address` is inserted and its `id` is
collected in this step.

The parent object is inserted next. i.e. in this case, the `author` is now inserted with the `address_id` being set
to the `id` of the address that was inserted. Because of this, it is not allowed to pass `address_id` in the author
object if you are also providing data for the address relationship.

The `id` of the author is collected in this step.

The array relationship objects are inserted at the end. i.e. in this case, the `articles` are now inserted with
their `author_id` set to the author's `id` collected in the step 2. Hence, it's not possible to specify `author_id` in the data for the articles relationship.

Note

The order of object insertion can be controlled using the[ insertion_order ](https://hasura.io/docs/latest/api-reference/syntax-defs/#objrelusingmanualmapping)option while creating a manual relationship.
This is necessary to ensure[ nested inserts ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/one-to-one/#one-to-one-insert)in
one-to-one relationships are possible using either side as the parent which would otherwise error out with a `Not-NULL violation` error in one of the cases.

### Many-to-many relationships​

Let's say the `articles` has a[ many-to-many relationship ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/many-to-many/)with
the `tags` table via a bridge table `article_tags` .

 **Example:** Insert an `article` along with a few `tags` .

 **How it works** 

1. The parent object (from the perspective of `article` ) is inserted first i.e. the `article` is inserted.The `id` of the article is collected in this step.
2. The array relationship objects (from the perspective of `article` ) are inserted next i.e. the `article_tags` are
inserted.
    1. The object relationship objects (from the perspective of `article_tags` ) are inserted now i.e. the `tags` are
now inserted.The `ids` of the tags are collected in this step.

2. The parent object (from the perspective of `article_tags` ) is inserted at the end i.e. the `article_tags` are
now inserted with their `article_id` set to the article's `id` collected in step 1. The `tag_id` is set to the
tag's `id` collected in step 2.1. Hence, it’s not possible to specify `article_id` and `tag_id` in the data for
the *article_tags* relationship.

3. The object relationship objects (from the perspective of `article_tags` ) are inserted now i.e. the `tags` are
now inserted.The `ids` of the tags are collected in this step.

4. The parent object (from the perspective of `article_tags` ) is inserted at the end i.e. the `article_tags` are
now inserted with their `article_id` set to the article's `id` collected in step 1. The `tag_id` is set to the
tag's `id` collected in step 2.1. Hence, it’s not possible to specify `article_id` and `tag_id` in the data for
the *article_tags* relationship.


The parent object (from the perspective of `article` ) is inserted first i.e. the `article` is inserted.

The `id` of the article is collected in this step.

The array relationship objects (from the perspective of `article` ) are inserted next i.e. the `article_tags` are
inserted.

The object relationship objects (from the perspective of `article_tags` ) are inserted now i.e. the `tags` are
now inserted.

The `ids` of the tags are collected in this step.

The parent object (from the perspective of `article_tags` ) is inserted at the end i.e. the `article_tags` are
now inserted with their `article_id` set to the article's `id` collected in step 1. The `tag_id` is set to the
tag's `id` collected in step 2.1. Hence, it’s not possible to specify `article_id` and `tag_id` in the data for
the *article_tags* relationship.

 **on_conflict** 

 `on_conflict` can be passed as an argument in a nested insert statement. In our example, we say that if the unique key
( `label` ) already exists for a tag, we update the `label` of this respective tag (see[ nested upsert caveats ](https://hasura.io/docs/latest/mutations/postgres/upsert/#pg-nested-upsert-caveats)).

## Insert an object with a JSONB field​

 **Example:** Insert a new `author` object with a JSONB `address` field:

## Insert an object with an ARRAY field​

 **Example:** Insert a new `author` with a text array `emails` field:

Using variables:

To insert fields of nested array types, you have to pass them as a[ Postgres array literal ](https://www.postgresql.org/docs/current/arrays.html#ARRAYS-INPUT).

## Set a field to its default value during insert​

To set a field to its `default` value, just omit it from the input object, irrespective of the[ default value configuration ](https://hasura.io/docs/latest/schema/postgres/default-values/postgres-defaults/)i.e. via Postgres defaults or using
column presets.

 **Example:** If the default value of `id` is set to auto-incrementing integer, there's no need to pass the `id` field to
the input object:

## Set a field to NULL during insert​

If a field is `nullable` in the database, to set its value to `null` , either pass its value as `null` or just omit it
from the input object.

 **Example:** If `age` is a nullable field, to set it to `null` , either don't pass the age field to the input object or
pass it as `null` :

OR

### What did you think of this doc?

- [ Auto-generated insert mutation schema ](https://hasura.io/docs/latest/mutations/postgres/insert/#auto-generated-insert-mutation-schema)
- [ Insert a single object ](https://hasura.io/docs/latest/mutations/postgres/insert/#insert-a-single-object)
- [ Insert multiple objects of the same type in the same mutation ](https://hasura.io/docs/latest/mutations/postgres/insert/#insert-multiple-objects-of-the-same-type-in-the-same-mutation)
- [ Insert an object and get a nested object in response ](https://hasura.io/docs/latest/mutations/postgres/insert/#insert-an-object-and-get-a-nested-object-in-response)
- [ Insert an object along with its related objects through relationships ](https://hasura.io/docs/latest/mutations/postgres/insert/#pg-nested-inserts)
    - [ One-to-one / One-to-many relationships ](https://hasura.io/docs/latest/mutations/postgres/insert/#one-to-one--one-to-many-relationships)

- [ Many-to-many relationships ](https://hasura.io/docs/latest/mutations/postgres/insert/#many-to-many-relationships)
- [ Insert an object with a JSONB field ](https://hasura.io/docs/latest/mutations/postgres/insert/#insert-an-object-with-a-jsonb-field)
- [ Insert an object with an ARRAY field ](https://hasura.io/docs/latest/mutations/postgres/insert/#insert-an-object-with-an-array-field)
- [ Set a field to its default value during insert ](https://hasura.io/docs/latest/mutations/postgres/insert/#set-a-field-to-its-default-value-during-insert)
- [ Set a field to NULL during insert ](https://hasura.io/docs/latest/mutations/postgres/insert/#set-a-field-to-null-during-insert)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)