# Schema/Metadata API Reference: Query collections (Deprecated)

Deprecation

In versions `v2.0.0` and above, the schema/Metadata API is deprecated in
favour of the[ schema API ](https://hasura.io/docs/latest/api-reference/schema-api/index/)and the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/).

Though for backwards compatibility, the schema/Metadata APIs will
continue to function.

## Introduction​

Group queries using query collections.

Create/rename/drop query collections and add/drop a query to a collection using
the following query types.

## create_query_collection​

 `create_query_collection` is used to define a collection.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "create_query_collection" ,
     "args" :   {
          "name" :   "my_collection" ,
          "comment" :   "an optional comment" ,
          "definition" :   {
              "queries" :   [
                  { "name" :   "query_1" ,   "query" :   "query { test {id name}}" }
               ]
          }
      }
}
```

Note

The queries in query collections are validated against the schema. So, adding an invalid query would result in inconsistent Metadata error.
As the query collection is used in allowlists and REST endpoints, they are validated as well.

### Args Syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ CollectionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#collectionname) | Name of the query collection |
| definition | true | [ CollectionQuery ](https://hasura.io/docs/latest/api-reference/syntax-defs/#collectionquery)array | List of queries |
| comment | false | text | Optional comment |


## rename_query_collection​

 `rename_query_collection` is used to rename a collection

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "rename_query_collection" ,
     "args" :   {
          "name" :   "my_collection" ,
          "new_name" :   "my_new_collection"
      }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ CollectionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#collectionname) | Name of the query collection to be replaced |
| new_name | true | [ CollectionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#collectionname) | New name of the query collection |


## drop_query_collection​

 `drop_query_collection` is used to drop a collection

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "drop_query_collection" ,
     "args" :   {
          "collection" :   "my_collection" ,
          "cascade" :   false
      }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| collection | true | [ CollectionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#collectionname) | Name of the query collection |
| cascade | true | boolean | When set to `true` , the collection (if present) is removed from the allowlist |


## add_query_to_collection​

 `add_query_to_collection` is used to add a query to a given collection.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "add_query_to_collection" ,
     "args" :   {
          "collection_name" :   "my_collection" ,
          "query_name" :   "query_2" ,
          "query" :   "query {test {name}}"
      }
}
```

### Args Syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| collection_name | true | [ CollectionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#collectionname) | Name of the query collection |
| query_name | true | [ QueryName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#queryname) | Name of the query |
| query | true | text | The GraphQL query text |


## drop_query_from_collection​

 `drop_query_from_collection` is used to remove a query from a given
collection.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "drop_query_from_collection" ,
     "args" :   {
          "collection_name" :   "my_collection" ,
          "query_name" :   "query_2"
      }
}
```

### Args Syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| collection_name | true | [ CollectionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#collectionname) | Name of the query collection |
| query_name | true | [ QueryName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#queryname) | Name of the query |


## add_collection_to_allowlist​

 `add_collection_to_allowlist` is used to add a collection to the allow-list.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "add_collection_to_allowlist" ,
     "args" :   {
          "collection" :   "my_collection"
      }
}
```

### Args Syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| collection | true | [ CollectionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#collectionname) | Name of a query collection to be added to the allow-list |


## drop_collection_from_allowlist​

 `drop_collection_from_allowlist` is used to remove a collection from the allow-list.

```
POST   /v1/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "drop_collection_from_allowlist" ,
     "args" :   {
          "collection" :   "my_collection_1"
      }
}
```

### Args Syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| collection | true | [ CollectionName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#collectionname) | Name of a query collection to be removed from the allow-list |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#introduction)
- [ create_query_collection ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-create-query-collection)
    - [ Args Syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-create-query-collection-syntax)
- [ rename_query_collection ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-rename-query-collection)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-rename-query-collection-syntax)
- [ drop_query_collection ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-drop-query-collection)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-drop-query-collection-syntax)
- [ add_query_to_collection ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-add-query-to-collection)
    - [ Args Syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-add-query-to-collection-syntax)
- [ drop_query_from_collection ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-drop-query-from-collection)
    - [ Args Syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-drop-query-from-collection-syntax)
- [ add_collection_to_allowlist ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-add-collection-to-allowlist)
    - [ Args Syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-add-collection-to-allowlist-syntax)
- [ drop_collection_from_allowlist ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-drop-collection-from-allowlist)
    - [ Args Syntax ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/query-collections/#schema-metadata-rename-query-collection-syntax/#schema-metadata-drop-collection-from-allowlist-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)