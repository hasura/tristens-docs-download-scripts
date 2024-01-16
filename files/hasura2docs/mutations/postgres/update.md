# Postgres: Update Mutation

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
# single object update (supported from v1.2.0)
update_article_by_pk   (
   _inc :   article_inc_input
   _set :   article_set_input
   # primary key columns arg
   pk_columns :   article_pk_columns_input !
) :   article
```

As you can see from the schema:

- The `where` argument is compulsory to filter rows to be updated. See[ Filter queries ](https://hasura.io/docs/latest/queries/postgres/filters/index/)for filtering options. Objects can be updated based on filters
on their own fields or those in their nested objects. The `{}` expression can be used to update all rows.
- You can return the number of affected rows and the affected objects (with nested objects) in the response.


See the[ update mutation API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#update-syntax)for the full
specifications.

Note

- At least any one of `_set` , `_inc` operators or the jsonb operators `_append` , `_prepend` , `_delete_key` , `_delete_elem` , `_delete_at_path` is required.
- If a table is not in the `public` Postgres schema, the update mutation field will be of the format `update_<schema_name>_<table_name>` .


## Update an object by its primary key​

You can update a single object in a table using the primary key. The output type is the nullable table object. The
mutation returns the updated row object or `null` if the row does not exist.

 **Example:** Update an article where `id` is `1` :

 **Example:** Update a non-existent article:

Note

 `update_<table>_by_pk` will **only** be available if you have select permissions on at least the columns that make up
the primary key as well as update permissions on at least one column.

Supported from

The `update_<table>_by_pk` mutation is supported in versions `v1.2.0` and above.

## Update objects based on their fields​

 **Example:** Update the `rating` and `is_published` of articles with a low `rating` :

Using variables:

OR

## Update objects based on nested objects' fields​

 **Example:** Reset the `rating` of all articles authored by "Sidney":

## Update all objects​

You can update all objects in a table using the `{}` expression as the `where` argument. `{}` basically evaluates to `true` for all objects.

 **Example:** Reset rating of all articles:

## Run multiple updates with different conditions​

You can run multiple updates in sequence, each with its own `where` and `_set` , `_inc` , etc. clauses.

 **Example** :

Note

- The result is an array with the results of each entry in `updates` returned in order.
- If any of the updates error for whatever reason, all the others are rolled back as the updates are executed inside a
transaction.


Supported from

The `update_<table>_many` mutation is supported in versions `v2.10.0` and above.

## Increment/Decrement int columns​

You can increment/decrement an `int` column with a given value using the `_inc` operator.

 **Example:** Increment the `likes` of an article by 2:

 **Example:** Decrement the `likes` of an article by 2:

## Update jsonb columns​

The currently available `jsonb` operators are:

| Operator | Postgres equivalent | Function |
|---|---|---|
|  `_ append`  | || | append json value to a `jsonb` column |
|  `_ prepend`  | || | prepend json value to a `jsonb` column |
|  `_ delete_ key`  |  `-`  | delete top-level key from `jsonb` column |
|  `_ delete_ elem`  |  `-`  | delete array element from `jsonb` column |
|  `_ delete_ at_ path`  |  `#-`  | delete element at a path from `jsonb` column |


Note

You can learn more about Postgres jsonb operators[ here ](https://www.postgresql.org/docs/current/static/functions-json.html#FUNCTIONS-JSONB-OP-TABLE).

 **Examples:** 

- [ Append a json to a jsonb column ](https://hasura.io/docs/latest/mutations/postgres/update/#append-a-json-to-a-jsonb-column)
- [ Prepend a json to a jsonb column ](https://hasura.io/docs/latest/mutations/postgres/update/#prepend-a-json-to-a-jsonb-column)
- [ Delete a top-level key from a jsonb column ](https://hasura.io/docs/latest/mutations/postgres/update/#delete-a-top-level-key-from-a-jsonb-column)
- [ Delete an element from a jsonb column storing a json array ](https://hasura.io/docs/latest/mutations/postgres/update/#delete-an-element-from-a-jsonb-column-storing-a-json-array)
- [ Delete an element at a specific path in a jsonb column ](https://hasura.io/docs/latest/mutations/postgres/update/#delete-an-element-at-a-specific-path-in-a-jsonb-column)


### Append a json to a jsonb column​

You can append any `jsonb` column with another json value by using the `_append` operator.

Since the input is a json value, it should be provided through a variable.

 **Example:** Append the json `{"key1": "value1"}` to the `jsonb` column `extra_info` of the `article` table:

### Prepend a json to a jsonb column​

You can prepend any `jsonb` column with another json value by using the `_prepend` operator.

Since the input is a json value, it should be provided through a variable.

 **Example:** Prepend the json `{"key0": "value0"}` to the `jsonb` column `extra_info` of the `article` table:

### Delete a top-level key from a jsonb column​

You can delete a top-level key of a `jsonb` column by using the `_delete_key` operator.

The input value should be a `String` .

 **Example:** Delete the key `key` in the `jsonb` column `extra_info` of the `article` table:

### Delete an element from a jsonb column storing a json array​

If a `jsonb` column is storing a json array, you can delete an element from the array using the `_delete_elem` operator.

The input value should be an `Int` .

 **Example:** Delete the element at position 2 in the array value of the `jsonb` column `extra_info` of the `article` table:

### Delete an element at a specific path in a jsonb column​

You can delete a field or element of a `jsonb` column at a specified path by using the `_delete_at_path` operator.

The input value should be a `String Array` .

 **Example:** Delete element at json path `name.last` in the `jsonb` column `extra_info` of the author table:

## Replace all nested array objects of an object​

In order to replace all existing nested array objects of an object, currently it's required to use two mutations: one to
delete all the existing objects and one to add a list of new nested objects.

 **Example:** Replace all articles of an author with a new list:

Nested updates

Hasura currently doesn't support nested updates. Follow[ this Github issue ](https://github.com/hasura/graphql-engine/issues/1573)for updates.

### What did you think of this doc?

- [ Auto-generated update mutation schema ](https://hasura.io/docs/latest/mutations/postgres/update/#auto-generated-update-mutation-schema)
- [ Update an object by its primary key ](https://hasura.io/docs/latest/mutations/postgres/update/#update-an-object-by-its-primary-key)
- [ Update objects based on their fields ](https://hasura.io/docs/latest/mutations/postgres/update/#update-objects-based-on-their-fields)
- [ Update objects based on nested objects' fields ](https://hasura.io/docs/latest/mutations/postgres/update/#update-objects-based-on-nested-objects-fields)
- [ Update all objects ](https://hasura.io/docs/latest/mutations/postgres/update/#update-all-objects)
- [ Run multiple updates with different conditions ](https://hasura.io/docs/latest/mutations/postgres/update/#multiple-updates)
- [ Increment/Decrement int columns ](https://hasura.io/docs/latest/mutations/postgres/update/#incrementdecrement-int-columns)
- [ Update jsonb columns ](https://hasura.io/docs/latest/mutations/postgres/update/#update-jsonb-columns)
    - [ Append a json to a jsonb column ](https://hasura.io/docs/latest/mutations/postgres/update/#append-a-json-to-a-jsonb-column)

- [ Prepend a json to a jsonb column ](https://hasura.io/docs/latest/mutations/postgres/update/#prepend-a-json-to-a-jsonb-column)

- [ Delete a top-level key from a jsonb column ](https://hasura.io/docs/latest/mutations/postgres/update/#delete-a-top-level-key-from-a-jsonb-column)

- [ Delete an element from a jsonb column storing a json array ](https://hasura.io/docs/latest/mutations/postgres/update/#delete-an-element-from-a-jsonb-column-storing-a-json-array)

- [ Delete an element at a specific path in a jsonb column ](https://hasura.io/docs/latest/mutations/postgres/update/#delete-an-element-at-a-specific-path-in-a-jsonb-column)
- [ Replace all nested array objects of an object ](https://hasura.io/docs/latest/mutations/postgres/update/#replace-all-nested-array-objects-of-an-object)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)