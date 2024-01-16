# MS SQL Server: Update Mutation

## Auto-generated update mutation schema​

 **For example** , the auto-generated schema for the update mutation field for a table `article` looks like the following:

```
update_article   (
   _inc :   article_inc_input
   _set :   article_set_input
   where :   article_bool_exp !
) :   article_mutation_response
# response of any mutation on the table "article"
type   article_mutation_response   {
   # number of affected rows by the mutation
   affected_rows :   Int !
   # data of the affected rows by the mutation
   returning :   [ article ! ] !
}
# single object update
update_article_by_pk   (
   _inc :   article_inc_input
   _set :   article_set_input
   # primary key columns arg
   pk_columns :   article_pk_columns_input !
) :   article
```

As you can see from the schema:

- The `where` argument is compulsory to filter rows to be updated. See[ Filter queries ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/index/)for filtering options. Objects can be updated based on
filters on their own fields or those in their nested objects. The `{}` expression can be used to update all rows.
- You can return the number of affected rows and the affected objects (with nested objects) in the response.


See the[ update mutation API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#update-syntax)for the full
specifications.

Note

- At least any one of `_set` , `_inc` operators is required.
- If a table is not in the `dbo` MS SQL Server schema, the update mutation field will be of the format `update_<schema_name>_<table_name>` .


## Update an object by its primary key​

You can update a single object in a table using the primary key. The output type is the nullable table object. The
mutation returns the updated row object or `null` if the row does not exist.

 **Example:** Update an article where `id` is `1` :

 **Example:** Update a non-existent article:

Note

 `update_<table>_by_pk` will **only** be available if you have select permissions on the table, as it returns the updated
row.

## Update objects based on their fields​

 **Example:** Update the `rating` and `is_published` of articles with a low `rating` :

Using variables:

OR

## Update objects based on nested objects' fields​

 **Example:** Reset the `rating` of all articles authored by "Sidney":

## Update all objects​

You can update all objects in a table using the `{}` expression as the `where` argument. `{}` basically evaluates to `true` for all objects.

 **Example:** Reset rating of all articles:

## Increment/Decrement int columns​

You can increment/decrement an `int` column with a given value using the `_inc` operator.

 **Example:** Increment the `likes` of an article by 2:

 **Example:** Decrement the `likes` of an article by 2:

## Replace all nested array objects of an object​

In order to replace all existing nested array objects of an object, currently it's required to use two mutations: one to
delete all the existing objects and one to add a list of new nested objects.

 **Example:** Replace all articles of an author with a new list:

### What did you think of this doc?

- [ Auto-generated update mutation schema ](https://hasura.io/docs/latest/mutations/ms-sql-server/update/#auto-generated-update-mutation-schema)
- [ Update an object by its primary key ](https://hasura.io/docs/latest/mutations/ms-sql-server/update/#update-an-object-by-its-primary-key)
- [ Update objects based on their fields ](https://hasura.io/docs/latest/mutations/ms-sql-server/update/#update-objects-based-on-their-fields)
- [ Update objects based on nested objects' fields ](https://hasura.io/docs/latest/mutations/ms-sql-server/update/#update-objects-based-on-nested-objects-fields)
- [ Update all objects ](https://hasura.io/docs/latest/mutations/ms-sql-server/update/#update-all-objects)
- [ Increment/Decrement int columns ](https://hasura.io/docs/latest/mutations/ms-sql-server/update/#incrementdecrement-int-columns)
- [ Replace all nested array objects of an object ](https://hasura.io/docs/latest/mutations/ms-sql-server/update/#replace-all-nested-array-objects-of-an-object)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)