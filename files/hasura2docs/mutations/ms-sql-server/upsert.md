# MS SQL Server: Upsert Mutation

## Introduction​

An upsert query ensures the given set of rows are present in the database, inserting new rows or updating existing rows
as necessary, subject to certain criteria.

## Convert insert mutation to upsert​

Note

Only tables with **update** permissions are **upsertable** . i.e. a table's update permissions are respected before
updating an existing row in case of a match.

To convert an[ insert mutation ](https://hasura.io/docs/latest/mutations/ms-sql-server/insert/)into an upsert, you need to use the `if_matched` argument to specify:

- the **columns to be matched** for each row using the `match_columns` field.
- the **columns to be updated** in the case of a match using the `update_columns` field.
- a **condition** for updating the column using the `where` field, and


The value of the `update_columns` field determines the behavior of the upsert request as shown via the use cases below.

## Upsert is not a substitute for update​

The upsert functionality is sometimes confused with the update functionality. However, they work slightly differently.
An upsert mutation is used in the case when it's not clear if the respective row is already present in the database. If
it's known that the row is present in the database, `update` is the functionality to use.

For an upsert, **all columns that are necessary for an insert are required** .

 **How it works** 

1. MS SQL Server tries to insert a row (hence all the required columns need to be present)
2. If this fails because of some match, it updates the specified columns


If not all required columns are present, an error like `NULL value unexpected for <not-specified-column>` can occur.

## Update selected columns on match​

The `update_columns` field can be used to specify which columns to update in case a match occurs.

 **Example** : Insert a new object in the `article` table or, if the value of the `title` column matches a a `title` value
in an existing row, update the `content` column of the existing article:

Note that the `published_on` column is left unchanged as it wasn't present in `update_columns` .

Note

If `match_columns` is an **empty array** there is no basis for comparing new rows to existing rows. Thus the mutation
will always **insert** the values and will never update any rows.

 **Example** : Insert a new object into the article table, will not match on columns because none are specified.

This query is equivalent to a simple insert without an `if_matched` clause.

## Update selected columns on match subject to a filter​

A `where` condition can be added to the `if_matched` clause to check a condition before making the update in case a
match occurs.

 **Example** : Insert a new object in the `article` table, or if the value of the `title` column matches a a `title` value
in an existing row, update the `published_on` column specified in `update_columns` only if the previous `published_on` value is lesser than the new value:

## Ignore request on match​

If `update_columns` is an **empty array** then on match the changes are ignored.

 **Example** : Insert a new author object into the author table, unless there already exists an author with the same name.

In this case, the insert mutation is ignored because there is a match and `update_columns` is empty.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/mutations/ms-sql-server/upsert/#introduction)
- [ Convert insert mutation to upsert ](https://hasura.io/docs/latest/mutations/ms-sql-server/upsert/#convert-insert-mutation-to-upsert)
- [ Upsert is not a substitute for update ](https://hasura.io/docs/latest/mutations/ms-sql-server/upsert/#upsert-is-not-a-substitute-for-update)
- [ Update selected columns on match ](https://hasura.io/docs/latest/mutations/ms-sql-server/upsert/#update-selected-columns-on-match)
- [ Update selected columns on match subject to a filter ](https://hasura.io/docs/latest/mutations/ms-sql-server/upsert/#update-selected-columns-on-match-subject-to-a-filter)
- [ Ignore request on match ](https://hasura.io/docs/latest/mutations/ms-sql-server/upsert/#ignore-request-on-match)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)