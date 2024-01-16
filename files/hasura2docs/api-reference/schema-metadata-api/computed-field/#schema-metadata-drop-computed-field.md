# Schema/Metadata API Reference: Computed Fields (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

## Introduction​

 **computed field** is an extra field added to a table, its value is
computed via an SQL function which has the table row type as an input
argument. Currently, the Hasura GraphQL Engine supports functions
returning[ base types ](https://www.postgresql.org/docs/current/extend-type-system.html#id-1.8.3.5.9)or[ table row types ](https://www.postgresql.org/docs/current/rowtypes.html#ROWTYPES-DECLARING)as computed fields.

## add_computed_field​

 `add_computed_field` is used to define a computed field in a table.
There cannot be an existing column or relationship or computed field
with the same name.

Create a `computed field` called `full_name` on an `author`  *table* ,
using an SQL function called `author_full_name` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" : "add_computed_field" ,
     "args" : {
         "table" : {
             "name" : "author" ,
             "schema" : "public"
         } ,
         "name" : "full_name" ,
         "definition" : {
             "function" : {
                 "name" : "author_full_name" ,
                 "schema" : "public"
             } ,
             "table_argument" : "author_row"
         }
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| name | true | [ ComputedFieldName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#computedfieldname) | Name of the new computed field |
| definition | true | [ ComputedFieldDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#computedfielddefinition) | The computed field definition |
| comment | false | text | comment |


## drop_computed_field​

 `drop_computed_field` is used to drop a computed field of a table. If
there are other objects dependent on this computed field, like
permissions, the request will fail and report the dependencies unless `cascade` is set to `true` . If `cascade` is set to `true` , the dependent
objects are also dropped.

Drop a computed field `full_name` from a table `author` :

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type" : "drop_computed_field" ,
     "args" : {
         "table" : {
             "name" : "author" ,
             "schema" : "public"
         } ,
         "name" : "full_name" ,
         "cascade" :   false
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| name | true | [ ComputedFieldName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#computedfieldname) | Name of the computed field |
| cascade | false | Boolean | When set to `true` , all the dependent items (if any) on this computed fields are also dropped |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/computed-field/#schema-metadata-drop-computed-field/#introduction)
- [ add_computed_field ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/computed-field/#schema-metadata-drop-computed-field/#schema-metadata-add-computed-field)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/computed-field/#schema-metadata-drop-computed-field/#schema-metadata-add-computed-field-syntax)
- [ drop_computed_field ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/computed-field/#schema-metadata-drop-computed-field/#schema-metadata-drop-computed-field)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/computed-field/#schema-metadata-drop-computed-field/#schema-metadata-drop-computed-field-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)