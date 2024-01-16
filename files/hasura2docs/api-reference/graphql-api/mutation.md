# API Reference - Mutation

## insert (upsert) syntax​

```
mutation [<mutation-name>] {
  <mutation-field-name> (
    [<input-object>!]
    [conflict-clause]
  )
  [mutation-response!]
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
| mutation-name | false | Value | Name of mutation for observability |
| mutation-field-name | true | Value | Name of the auto-generated mutation field, e.g. *insert_author*  |
| input-object | true | [ InputObjects ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#inputobjects) | Name of the auto-generated mutation field |
| mutation-response | true | [ MutationResponse ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#mutationresponse) | Object to be returned after mutation succeeds |
| on-conflict | false | [ OnConflictClause ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#postgres-on-conflict) | In Postgres, converts *insert* to *upsert* by handling conflict |
| if-matched | false | [ IfMatchedClause ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#sqlserver-if-matched) | In MS SQL Server, converts *insert* to *upsert* using a match |


 **Example: Insert** 

```
mutation   insert_article   {
   insert_article ( objects :   [ {   title :   "Software is gluttonous" ,   content :   "Something happened in HP" ,   author_id :   3   } ] )   {
     returning   {
       id
       title
     }
   }
}
```

 **Example: Upsert** 

```
mutation   upsert_author   {
   insert_author (
     objects :   [ {   name :   "John" ,   id :   12   } ]
     on_conflict :   {   constraint :   author_name_key ,   update_columns :   [ name ,   id ]   }
   )   {
     affected_rows
   }
}
```

## insert_one syntax​

```
mutation [<mutation-name>] {
  <mutation-field-name> (
    [<input-object>!]
    [conflict-clause]
  )
  [mutation-response!]
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
| mutation-name | false | Value | Name of mutation for observability |
| mutation-field-name | true | Value | Name of the auto-generated mutation field, e.g. *insert_author_one*  |
| input-object | true | [ InputObject ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#inputobject) | Name of the auto-generated mutation field |
| mutation-response | true | [ SimpleObject ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#simpleobject) | Object to be returned after mutation succeeds |
| on-conflict | false | [ OnConflictClause ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#postgres-on-conflict) | In Postgres, converts *insert* to *upsert* by handling conflict |
| if-matched | false | [ IfMatchedClause ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#sqlserver-if-matched) | In MS SQL Server, converts *insert* to *upsert* using a match |


 **Example: Insert One** 

```
mutation   insert_article_one   {
   insert_article_one ( object :   {   title :   "Software is gluttonous" ,   content :   "Something happened in HP" ,   author_id :   3   } )   {
     id
     title
   }
}
```

## update_by_pk syntax​

```
mutation [<mutation-name>] {
  <mutation-field-name> (
    [pk-columns-argument!],
    [set-argument!]
  )
  <object-fields>
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
| mutation-name | false | Value | Name of mutation for observability |
| mutation-field-name | true | Value | Name of the auto-generated update mutation field, e.g. *update_author_by_pk*  |
| pk-columns-argument | true | [ pkColumnsArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#pkcolumnsargexp) | Primary key(s) for row(s) to be updated |
| set-argument | false | [ setArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#setargexp) | Data to be updated in the table |
| inc-argument | false | [ incArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#incargexp) | Integer value to be incremented to Int columns in the table (Negative integers can be used to decrement) |
| append-argument | false | [ appendArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#appendargexp) | JSON value to be appended to JSONB columns in the table |
| prepend-argument | false | [ prependArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#prependargexp) | JSON value to be prepended to JSONB columns in the table |
| delete-key-argument | false | [ deleteKeyArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#deletekeyargexp) | Key to be deleted in the value of JSONB columns in the table |
| delete-elem-argument | false | [ deleteElemArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#deleteelemargexp) | Array element to be deleted in the value of JSONB columns in the table |
| delete-at-path-argument | false | [ deleteAtPathArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#deleteatpathargexp) | Element at path to be deleted in the value of JSONB columns in the table |


 **Example: Update by PK** 

```
mutation   update_articles   {
   update_article_by_pk ( pk_columns :   {   id :   1   } ,   _set :   {   is_published :   true   } )   {
     id
     title
   }
}
```

## update syntax​

```
mutation [<mutation-name>] {
  <mutation-field-name> (
    [where-argument!],
    [set-argument!]
  )
  [mutation-response!]
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
| mutation-name | false | Value | Name of mutation for observability |
| mutation-field-name | true | Value | Name of the auto-generated update mutation field, e.g. *update_author*  |
| where-argument | true | [ whereArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#whereargexp) | Selection criteria for rows to be updated |
| set-argument | false | [ setArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#setargexp) | Data to be updated in the table |
| inc-argument | false | [ incArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#incargexp) | Integer value to be incremented to Int columns in the table |
| append-argument | false | [ appendArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#appendargexp) | JSON value to be appended to JSONB columns in the table |
| prepend-argument | false | [ prependArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#prependargexp) | JSON value to be prepended to JSONB columns in the table |
| delete-key-argument | false | [ deleteKeyArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#deletekeyargexp) | Key to be deleted in the value of JSONB columns in the table |
| delete-elem-argument | false | [ deleteElemArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#deleteelemargexp) | Array element to be deleted in the value of JSONB columns in the table |
| delete-at-path-argument | false | [ deleteAtPathArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#deleteatpathargexp) | Element at path to be deleted in the value of JSONB columns in the table |
| mutation-response | true | [ MutationResponse ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#mutationresponse) | Object to be returned after mutation succeeds |


 **Example: Update** 

```
mutation   update_author   {
   update_author ( where :   {   id :   {   _eq :   3   }   } ,   _set :   {   name :   "Jane"   } )   {
     affected_rows
   }
}
```

## delete_by_pk syntax​

```
mutation [<mutation-name>] {
  <mutation-field-name> (
    column1: value1
    column2: value2
  )
  <object-fields>
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
| mutation-name | false | Value | Name of mutation for observability |
| mutation-field-name | true | Value | Name of the auto-generated delete mutation field, e.g. *delete_author_by_pk*  |


 **Example: Delete by PK** 

```
mutation   delete_articles   {
   delete_article_by_pk ( id :   1 )   {
     id
     title
   }
}
```

## delete syntax​

```
mutation [<mutation-name>] {
  <mutation-field-name> (
    [where-argument!]
  )
  [mutation-response!]
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
| mutation-name | false | Value | Name of mutation for observability |
| mutation-field-name | true | Value | Name of the auto-generated delete mutation field, e.g. *delete_author*  |
| where-argument | true | [ whereArgExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#whereargexp) | Selection criteria for rows to delete |
| mutation-response | true | [ MutationResponse ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#mutationresponse) | Object to be returned after mutation succeeds |


 **Example: Delete** 

```
mutation   delete_articles   {
   delete_article ( where :   {   author :   {   id :   {   _eq :   7   }   }   } )   {
     affected_rows
     returning   {
       id
     }
   }
}
```

Note

For more examples and details of usage, please see[ this ](https://hasura.io/docs/latest/mutations/postgres/index/).

## Syntax definitions​

### Mutation response​

```
{
  affected_rows
  returning {
    response-field1
    response-field2
    ..
  }
}
```

 **Example** 

```
{
   affected_rows
   returning   {
     id
     author_id
   }
}
```

### objects argument​

```
objects: [
  {
    field1: value,
    field2: value,
    <object-rel-name>: {
      data: <Input-Object>!,
      on_conflict: <Conflict-Clause>
    },
    <array-rel-name>: {
      data: [<Input-Object>!]!,
      on_conflict: <Conflict-Clause>
    }
    ..
  },
  ..
]
# no nested objects
```

 **Example** 

```
objects :   [
   {
     title :   "Software is eating the world" ,
     content :   "This week, Hewlett-Packard..." ,
     author :   {
       data :   {
         id :   1 ,
         name :   "Sydney"
       }
     }
   }
]
```

### object argument​

```
object: {
  field1: value,
  field2: value,
  <object-rel-name>: {
    data: <Input-Object>!,
    on_conflict: <Conflict-Clause>
  },
  <array-rel-name>: {
    data: [<Input-Object>!]!,
    on_conflict: <Conflict-Clause>
  }
  ..
}
```

 **Example** 

```
object :   {
   title :   "Software is eating the world" ,
   content :   "This week, Hewlett-Packard..." ,
   author :   {
     data :   {
       id :   1 ,
       name :   "Sydney"
     }
   }
}
```

### on_conflict argument for Postgres​

The `on_conflict` clause is used to convert an *insert* mutation to an *upsert* mutation. *Upsert* respects the table's *update* permissions before editing an existing row in case of a conflict. Hence the `on_conflict` clause is permitted
only if a table has *update* permissions defined.

```
on_conflict: {
  constraint: table_constraint!
  update_columns: [table_update_column!]!
  where: table_bool_exp
}
```

 **Example** 

```
on_conflict :   {
   constraint :   author_name_key
   update_columns :   [ name ]
   where :   { id :   { _lt :   1 } }
}
```

### if_matched argument for MS SQL Server​

The `if_matched` clause is used to convert an *insert* mutation to an *upsert* mutation. *Upsert* respects the table's *update* permissions before editing a matched row. Hence the `if_matched` clause is permitted only if a table has *update* permissions defined.

```
if_matched: {
  match_columns: table_match_column! | [table_match_column!]!
  update_columns: table_update_column! | [table_update_column!]!
  where: table_bool_exp
}
```

 **Example** 

```
if_matched :   {
   match_columns :   id
   update_columns :   [ name ]
   where :   { id :   { _eq :   7 } }
}
```

### pk_columns argument​

The `pk_columns` argument is used to identify an object by its primary key columns in *update* mutations.

```
pk_columns: {
  column-1: value-1
  column-2: value-2
}
```

 **Example** 

```
pk_columns :   {
   id :   1
   name :   "Harry"
}
```

### where argument​

```
where:
[ BoolExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#boolexp)
```

 **Example** 

```
where :   {
   rating :   { _eq :   5 }
}
```

#### BoolExp​

```
[ AndExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#andexp)
|
[ OrExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#orexp)
|
[ NotExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#notexp)
|
[ TrueExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#trueexp)
|
[ ColumnExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#columnexp)
```

##### AndExp​

```
{
  _and: [
[ BoolExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#boolexp)
]
}
```

 **Example** 

```
_and :   [
   { rating :   { _gt :   5 } } ,
   { updated_at :   { _gt :   "2019-01-01" } }
]
```

##### OrExp​

```
{
  _or: [
[ BoolExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#boolexp)
]
}
```

 **Example** 

```
_or :   [
   { rating :   { _is_null :   true } } ,
   { rating :   { _lt :   4 } }
]
```

##### NotExp​

```
{
  _not:
[ BoolExp ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#boolexp)
}
```

 **Example** 

```
_not :   {
   title :   { _eq :   "" }
}
```

##### TrueExp​

`{}`

 **Example** 

`author ( where :   { articles :   { } } )`

Note

 `{}` evaluates to true whenever an object exists (even if it's `null` ).

##### ColumnExp​

```
{
  field-name: {
[ Operator ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#operator)
: Value }
}
```

 **Example** 

`{ rating :   { _eq :   5 } }`

##### Operator​

 **Generic operators (all column types except json, jsonb):** 

- `_eq`
- `_ne`
- `_in`
- `_nin`
- `_gt`
- `_lt`
- `_gte`
- `_lte`


 **Text related operators:** 

- `_like`
- `_nlike`
- `_ilike`
- `_nilike`
- `_similar`
- `_nsimilar`
- `_iregex`
- `_niregex`
- `_regex`
- `_nregex`


 **Checking for NULL values:** 

- `_is_null` (takes true/false as values)


### _set argument​

```
_set: {
  field-name-1 : value,
  field-name-2 : value,
  ..
}
```

### _inc argument​

```
_inc: {
  field-name-1 : int-value,
  field-name-2 : int-value,
  ..
}
```

### _append argument​

```
_append: {
  field-name-1 : $json-variable-1,
  field-name-2 : $json-variable-1,
  ..
}
```

 **Example** 

```
{
   "json-variable-1" :   "value" ,
   "json-variable-2" :   "value"
}
```

### _prepend argument​

```
_prepend: {
  field-name-1 : $json-variable-1,
  field-name-2 : $json-variable-1,
  ..
}
```

 **Example** 

```
{
   "json-variable-1" :   "value" ,
   "json-variable-2" :   "value"
}
```

### _delete_key argument​

```
_delete_key: {
  field-name-1 : "key",
  field-name-2 : "key",
  ..
}
```

### _delete_elem argument​

```
_delete_elem: {
  field-name-1 : int-index,
  field-name-2 : int-index,
  ..
}
```

### _delete_at_path argument​

```
_delete_at_path: {
  field-name-1 : ["path-array"],
  field-name-2 : ["path-array"],
  ..
}
```

### What did you think of this doc?

- [ insert (upsert) syntax ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#insert-upsert-syntax)
- [ insert_one syntax ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#insert-upsert-one-syntax)
- [ update_by_pk syntax ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#update-by-pk-syntax)
- [ update syntax ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#update-syntax)
- [ delete_by_pk syntax ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#delete-by-pk-syntax)
- [ delete syntax ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#delete-syntax)
- [ Syntax definitions ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#syntax-definitions)
    - [ Mutation response ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#mutationresponse)

- [ objects argument ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#inputobjects)

- [ object argument ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#inputobject)

- [ on_conflict argument for Postgres ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#postgres-on-conflict)

- [ if_matched argument for MS SQL Server ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#sqlserver-if-matched)

- [ pk_columns argument ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#pkcolumnsargexp)

- [ where argument ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#whereargexp)

- [ _set argument ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#setargexp)

- [ _inc argument ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#incargexp)

- [ _append argument ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#appendargexp)

- [ _prepend argument ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#prependargexp)

- [ _delete_key argument ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#deletekeyargexp)

- [ _delete_elem argument ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#deleteelemargexp)

- [ _delete_at_path argument ](https://hasura.io/docs/latest/api-reference/graphql-api/mutation/#deleteatpathargexp)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)