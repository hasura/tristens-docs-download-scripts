# Paginate Query Results

## The limit & offset arguments​

The operators `limit` and `offset` are used for pagination.

 `limit` specifies the number of rows to retain from the result set and `offset` determines which slice to retain from
the results.

The following are examples of different pagination scenarios:

## Limit results​

 **Example:** Fetch the first 5 authors from the list of all authors:

## Limit results from an offset​

 **Example:** Fetch 5 authors from the list of all authors, starting with the 6th one:

## Limit results in a nested object​

 **Example:** Fetch a list of authors and a list of their first 2 articles:

## Keyset cursor based pagination​

Cursors are used to traverse across rows of a dataset. They work by returning a pointer to a specific row which can then
be used to fetch the next batch of data.

Keyset cursors are a column (or a set of columns) of the data that are used as the cursor. The column(s) used as the
cursor must be unique and sequential. This ensures that data is read after a specific row rather than relying on the
position of the row in the dataset as done by `offset` , and that duplicate records are not fetched again.

 **For example** , consider the following query to fetch a list of authors with a `where` clause used in place of `offset` :

Here we are fetching authors where the value of `id` is greater than 5. This will always skip the previously fetched
results which would have been ids 1 to 5, ensuring no duplicate results. Column `id` is acting as the cursor here,
unique and sequential.

The choice of cursor columns depends on the order of the expected results i.e. if the query has an `order_by` clause,
the column(s) used in the `order_by` need to be used as the cursor.

Columns such as `id` (auto-incrementing integer/big integer) or `created_at` (timestamp) are commonly used as cursors
when an order is not explicit, as they should be unique and sequential.

Where vs Offset

Keyset cursor based pagination using `where` is more performant than using `offset` because we can leverage database
indexes on the columns that are being used as cursors.

No order_by clause

Because we ran the above example without an `order_by` clause, it is accidental that we received those results.
Running a query without an `order_by` clause will return results in an arbitrary order.

### What did you think of this doc?

- [ The limit & offset arguments ](https://hasura.io/docs/3.0/graphql-api/queries/pagination/#the-limit--offset-arguments)
- [ Limit results ](https://hasura.io/docs/3.0/graphql-api/queries/pagination/#limit-results)
- [ Limit results from an offset ](https://hasura.io/docs/3.0/graphql-api/queries/pagination/#limit-results-from-an-offset)
- [ Limit results in a nested object ](https://hasura.io/docs/3.0/graphql-api/queries/pagination/#pg-nested-paginate)
- [ Keyset cursor based pagination ](https://hasura.io/docs/3.0/graphql-api/queries/pagination/#keyset-cursor-based-pagination)
