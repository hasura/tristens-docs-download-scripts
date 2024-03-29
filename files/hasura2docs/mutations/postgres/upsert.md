# Postgres: Upsert Mutation

## Introduction​

An upsert query will insert an object into the database in case there is no conflict with another row in the table. In
case there is a conflict with one or more rows, it will either update the fields of the conflicted rows or ignore the
request.

## Convert insert mutation to upsert​

Note

Only tables with **update** permissions are **upsertable** . i.e. a table's update permissions are respected before
updating an existing row in case of a conflict.

To convert an[ insert mutation ](https://hasura.io/docs/latest/mutations/postgres/insert/)into an upsert, you need to use the `on_conflict` argument to specify:

- a **unique or primary key constraint** using the `constraint` field, and
- the **columns to be updated** in the case of a violation of that constraint using the `update_columns` field.


The value of the `update_columns` field determines the behavior of the upsert request as shown via the use cases below.

Note

Partial unique indexes cannot be used in the `constraint` field.

Fetching Postgres constraint names

You can fetch details of unique or primary key constraints on a table by running the following SQL:

`SELECT   *   FROM   "information_schema" . "table_constraints"   WHERE  table_name = '<table>'   AND  table_schema = '<schema>' ;`

GraphQL Engine will automatically generate constraint names as enum values for the `constraint` field *(try
autocompleting in GraphiQL)* . Typically, the constraint is automatically named as `<table-name>_<column-name>_key` .

## Upsert is not a substitute for update​

The upsert functionality is sometimes confused with the update functionality. However, they work slightly differently.
An upsert mutation is used in the case when it's not clear if the respective row is already present in the database. If
it's known that the row is present in the database, `update` is the functionality to use.

For an upsert, **all columns that are necessary for an insert are required** .

 **How it works** 

1. Postgres tries to insert a row (hence all the required columns need to be present)
2. If this fails because of some constraint, it updates the specified columns


If not all required columns are present, an error like `NULL value unexpected for <not-specified-column>` can occur.

## Update selected columns on conflict​

The `update_columns` field can be used to specify which columns to update in case a conflict occurs.

 **Example** : Insert a new object in the `article` table or, if the unique constraint `article_title_key` is violated,
update the `content` column of the existing article:

Note that the `published_on` column is left unchanged as it wasn't present in `update_columns` .

## Update selected columns on conflict using a filter​

A `where` condition can be added to the `on_conflict` clause to check a condition before making the update in case a
conflict occurs

 **Example** : Insert a new object in the `article` table, or if the unique key constraint `article_title_key` is
violated, update the `published_on` column specified in `update_columns` only if the previous `published_on` value is
lesser than the new value:

## Ignore request on conflict​

If `update_columns` is an **empty array** then on conflict the changes are ignored.

 **Example** : Insert a new object into the author table or, if the unique constraint `author_name_key` is violated,
ignore the request.

In this case, the insert mutation is ignored because there is a conflict and `update_columns` is empty.

## Upsert in nested mutations​

You can specify the `on_conflict` clause while inserting nested objects:

 **Example** :

### Nested upsert caveats​

Note

The process by which nested inserts/upserts are executed is documented[ here ](https://hasura.io/docs/latest/mutations/postgres/insert/#pg-nested-inserts).

Nested upserts will fail when:

- In case of an array relationship, the parent upsert does not affect any rows (i.e. `update_columns: []` for parent and
a conflict occurs), as the array relationship objects are inserted after the parent.
- In case of an object relationship, the nested object upsert does not affect any row (i.e. `update_columns: []` for
nested object and a conflict occurs), as the object relationship object is inserted before the parent.


To allow upserting in these cases, set `update_columns: [<conflict-columns>]` . By doing this, in case of a conflict, the
conflicted column/s will be updated with the new value (which is the same values as they had before and hence will
effectively leave them unchanged) and will allow the upsert to go through.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/mutations/postgres/upsert/#introduction)
- [ Convert insert mutation to upsert ](https://hasura.io/docs/latest/mutations/postgres/upsert/#convert-insert-mutation-to-upsert)
- [ Upsert is not a substitute for update ](https://hasura.io/docs/latest/mutations/postgres/upsert/#upsert-is-not-a-substitute-for-update)
- [ Update selected columns on conflict ](https://hasura.io/docs/latest/mutations/postgres/upsert/#update-selected-columns-on-conflict)
- [ Update selected columns on conflict using a filter ](https://hasura.io/docs/latest/mutations/postgres/upsert/#update-selected-columns-on-conflict-using-a-filter)
- [ Ignore request on conflict ](https://hasura.io/docs/latest/mutations/postgres/upsert/#ignore-request-on-conflict)
- [ Upsert in nested mutations ](https://hasura.io/docs/latest/mutations/postgres/upsert/#upsert-in-nested-mutations)
    - [ Nested upsert caveats ](https://hasura.io/docs/latest/mutations/postgres/upsert/#pg-nested-upsert-caveats)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)