# Hasura Data Connectors Developer's Guide

# Pagination

Once the irrelevant rows have been filtered out, the `execute_query` function applies the `limit` and `offset` arguments by calling the `paginate function:

```
let
paginated:
Vec
<Row> = paginate(filtered.into_iter(), query.limit, query.offset);
```

The `paginate` function is implemented using the `skip` and `take` functions on iterators:

```
fn   paginate
<I:
Iterator
<Item = Row>>(
    collection: I,
    limit:
Option
<
u32
>,
    offset:
Option
<
u32
>,
) ->
Vec
<Row> {
let
start = offset.unwrap_or(
0
).try_into().unwrap();
match
limit {
Some
(n) => collection.skip(start).take(n.try_into().unwrap()).collect(),
None
=> collection.skip(start).collect(),
    }
}
```