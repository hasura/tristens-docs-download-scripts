# Relay API Reference - Query / Subscription

## query / subscription syntax​

```
query|subscription [<op-name>] {
  connection-object [([argument])]{
    connection-object-fields
  }
}
```

| Key | Required | Schema | Description |
|---|---|---|---|
| op-name | false | Value | Name query/subscription for observability |
| connection-object | true | [ ConnectionObject ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#connectionobject) | Name of the table connection |
| argument | false | [ Argument ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#argument) | One or more filter criteria, instructions for sorting order or pagination |


 **Example: Relay Query** 

```
query   {
   author_connection ( first :   2 )   {
     pageInfo   {
       hasNextPage
       endCursor
     }
     edges   {
       cursor
       node   {
         id
         name
         username
       }
     }
   }
}
```

 **Example: Relay Subscription** 

```
subscription   {
   author_connection ( first :   2 ) {
     pageInfo   {
       hasNextPage
       endCursor
     }
     edges   {
       cursor
       node   {
         id
         name
         username
       }
     }
   }
} q
```

Note

For details of usage, please see[ this page ](https://hasura.io/docs/latest/schema/postgres/relay-schema/).

## Syntax definitions​

### ConnectionObject​

```
connection-object {
  pageInfo: {
    hasNextPage
    hasPreviousPage
    startCursor
    endCursor
  }
  edges: {
    cursor
    node: {
      id
      field1
      field2
      json_field[(path: String)]
      ..
      nested object1
      nested object2
      aggregate nested object1
      ..
    }
  }
}
```

| Field | Type |
|---|---|
| pageInfo | [ PageInfo ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#pageinfo)! |
| edges | [[ Edge ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#edge)!]! |


Note

For more details on the Relay `connection` object type, refer to the[ Relay docs ](https://relay.dev/graphql/connections.htm#sec-Connection-Types).

### PageInfo​

Information useful for pagination.

```
type   PageInfo   {
   hasNextPage :   Boolean !
   hasPreviousPage :   Boolean !
   startCursor :   String !
   endCursor :   String !
}
```

Note

For more details on the Relay `PageInfo` object type, refer to the[ Relay docs ](https://relay.dev/graphql/connections.htm#sec-undefined.PageInfo).

### Edge​

Edge is an object type that consists of a[ cursor ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#cursor)and `node` fields. `node` is a table object type which
implements the Relay `Node` interface.

```
type   tableEdge   {
   cursor :   String !
   node :   table !
}
```

### Cursor​

The cursor field returns a unique non-null String value which is useful for[ pagination ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#paginationexp).

Note

For more details on the Relay `cursor` , refer to the[ Relay docs ](https://relay.dev/graphql/connections.htm#sec-Cursor).

### Argument​

```
[ DistinctOnExp ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#relaydistinctonexp)
|
[ WhereExp ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#relaywhereexp)
|
[ OrderByExp ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#relayorderbyexp)
|
[ PaginationExp ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#relaypaginationexp)
```

#### DistinctOnExp​

Same as the generic[ DistinctOnExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#distinctonexp)

#### WhereExp​

Same as the generic[ WhereExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#whereexp)

#### OrderByExp​

Same as the generic[ OrderByExp ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#orderbyexp)

#### PaginationExp​

 **Forward Pagination:** 

```
first: Integer
[after:
[ Cursor ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#cursor)
]
```

```
query   {
   article_connection ( first :   2 ,   after :   "eyJpZCIgOiAzfQ==" )   {
     pageInfo   {
       startCursor
       endCursor
       hasPreviousPage
       hasNextPage
     }
     edges   {
       cursor
       node   {
         title
         content
         author_id
       }
     }
   }
}
```

 **Backward Pagination:** 

```
[last: Integer]
[before:
[ Cursor ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#cursor)
]
```

```
query   {
   article_connection ( last :   2 ,   before :   "eyJpZCIgOiA0fQ==" )   {
     pageInfo   {
       startCursor
       endCursor
       hasPreviousPage
       hasNextPage
     }
     edges   {
       cursor
       node   {
         title
         content
         author_id
       }
     }
   }
}
```

### What did you think of this doc?

- [ query / subscription syntax ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#query--subscription-syntax)
- [ Syntax definitions ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#syntax-definitions)
    - [ ConnectionObject ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#connectionobject)

- [ PageInfo ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#pageinfo)

- [ Edge ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#edge)

- [ Cursor ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#cursor)

- [ Argument ](https://hasura.io/docs/latest/api-reference/relay-graphql-api/query/#argument)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)