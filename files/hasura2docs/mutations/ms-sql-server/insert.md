# MS SQL Server: Insert Mutation

## Auto-generated insert mutation schema​

 **For example** , the auto-generated schema for the insert mutation field for a table `article` looks like the following:

```
insert_article   (
   objects :   [ article_insert_input ! ] !
   if_matched :   article_if_matched
) :   article_mutation_response
# response of any mutation on the table "article"
type   article_mutation_response   {
   # number of affected rows by the mutation
   affected_rows :   Int !
   # data of the affected rows by the mutation
   returning :   [ article ! ] !
}
# single object insert
insert_article_one   (
   object :   article_insert_input !
   if_matched :   article_if_matched
) :   article
```

As you can see from the schema:

- `objects` argument is mandatory and you can pass multiple `objects` to the mutation.
- You can pass an `if_matched` argument to convert the mutation to an[ upsert mutation ](https://hasura.io/docs/latest/mutations/ms-sql-server/upsert/).
- You can return the number of affected rows and the affected objects (with nested objects) in the response.
- You can use the single object insert to get the inserted object directly as the mutation response.


Note

If a table is not in the `dbo` MS SQL Server schema, the insert mutation field will be of the format `insert_<schema_name>_<table_name>` .

## Insert a single object​

 **Example:** Insert a new `article` object and return the inserted article object in the response:

Using variables:

Note

The `insert_<object>_one` mutation will **only** be available if you have select permissions on the table, as it returns
the inserted row.

## Insert multiple objects of the same type in the same mutation​

 **Example:** Insert 2 new `article` objects and return both the article objects in the response:

Using variables:

## Insert an object and get a nested object in response​

 **Example:** Insert a new `article` object and return the inserted article object with its author in the response:

## Set a field to its default value during insert​

To set a field to its `default` value, just omit it from the input object, irrespective of the default value
configuration i.e. via MS SQL Server[ defaults ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-defaults/)or using[ column presets ](https://hasura.io/docs/latest/schema/ms-sql-server/default-values/mssql-column-presets/).

 **Example:** If the default value of `id` is set to auto-incrementing integer, there's no need to pass the `id` field to
the input object:

## Set a field to NULL during insert​

If a field is `nullable` in the database, to set its value to `null` , either pass its value as `null` or just omit it
from the input object.

 **Example:** If `age` is a nullable field, to set it to `null` , either don't pass the age field to the input object or
pass it as `null` :

OR

### What did you think of this doc?

- [ Auto-generated insert mutation schema ](https://hasura.io/docs/latest/mutations/ms-sql-server/insert/#auto-generated-insert-mutation-schema)
- [ Insert a single object ](https://hasura.io/docs/latest/mutations/ms-sql-server/insert/#insert-a-single-object)
- [ Insert multiple objects of the same type in the same mutation ](https://hasura.io/docs/latest/mutations/ms-sql-server/insert/#insert-multiple-objects-of-the-same-type-in-the-same-mutation)
- [ Insert an object and get a nested object in response ](https://hasura.io/docs/latest/mutations/ms-sql-server/insert/#insert-an-object-and-get-a-nested-object-in-response)
- [ Set a field to its default value during insert ](https://hasura.io/docs/latest/mutations/ms-sql-server/insert/#set-a-field-to-its-default-value-during-insert)
- [ Set a field to NULL during insert ](https://hasura.io/docs/latest/mutations/ms-sql-server/insert/#set-a-field-to-null-during-insert)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)