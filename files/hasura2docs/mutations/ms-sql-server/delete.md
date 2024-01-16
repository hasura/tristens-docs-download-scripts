# MS SQL Server: Delete Mutation

## Auto-generated delete mutation schema​

 **For example** , the auto-generated schema for the delete mutation field for a table `article` looks like the following:

```
delete_article   (
   where :   article_bool_exp !
) :   article_mutation_response
# response of any mutation on the table "article"
type   article_mutation_response   {
   # number of affected rows by the mutation
   affected_rows :   Int !
   # data of the affected rows by the mutation
   returning :   [ article ! ] !
}
# single object delete
delete_article_by_pk   (
   # all primary key columns args
   id :   Int
) :   article
```

As you can see from the schema:

- The `where` argument is compulsory to filter rows to be deleted. See[ Filter queries ](https://hasura.io/docs/latest/queries/postgres/filters/index/)for filtering options. Objects can be deleted based on filters
on their own fields or those in their nested objects. The `{}` expression can be used to delete all rows.
- You can return the number of affected rows and the affected objects (with nested objects) in the response.


See the[ delete mutation API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#delete-syntax)for the full
specifications.

Note

If a table is not in the default `dbo` MS SQL Server schema, the delete mutation field will be of the format `delete_<schema_name>_<table_name>` .

## Delete an object by its primary key​

You can delete a single object in a table using the primary key. The output type is the nullable table object. The
mutation returns the deleted row object or `null` if the row does not exist.

 **Example:** Delete an article where `id` is `1` :

 **Example:** Delete a non-existent article:

Note

 `delete_<table>_by_pk` will **only** be available if you have select permissions on the table, as it returns the deleted
row.

## Delete objects based on their fields​

 **Example:** Delete all articles rated less than 3:

## Delete objects based on nested objects' fields​

 **Example:** Delete all articles written by a particular author:

## Delete all objects​

You can delete all objects in a table using the `{}` expression as the `where` argument. `{}` basically evaluates to `true` for all objects.

 **Example:** Delete all articles:

### What did you think of this doc?

- [ Auto-generated delete mutation schema ](https://hasura.io/docs/latest/mutations/ms-sql-server/delete/#auto-generated-delete-mutation-schema)
- [ Delete an object by its primary key ](https://hasura.io/docs/latest/mutations/ms-sql-server/delete/#delete-an-object-by-its-primary-key)
- [ Delete objects based on their fields ](https://hasura.io/docs/latest/mutations/ms-sql-server/delete/#delete-objects-based-on-their-fields)
- [ Delete objects based on nested objects' fields ](https://hasura.io/docs/latest/mutations/ms-sql-server/delete/#delete-objects-based-on-nested-objects-fields)
- [ Delete all objects ](https://hasura.io/docs/latest/mutations/ms-sql-server/delete/#delete-all-objects)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)