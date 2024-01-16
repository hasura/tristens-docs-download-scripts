# Postgres: Paginate Query Results

## The limit & offset arguments​

The operators `limit` and `offset` are used for pagination.

 `limit` specifies the number of rows to retain from the result set and `offset` determines which slice to retain from
the results.

You can see the complete specification of the `limit` and `offset` arguments in the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#paginationexp).

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

Note

Keyset cursor based pagination using `where` is more performant than using `offset` because we can leverage database
indexes on the columns that are being used as cursors.

## Fetch limited results along with data aggregated over all results (e.g. total count) in the same query​

Sometimes, some aggregated information on all the data is required along with a subset of data.

E.g. the total count of results can be returned along with a page of results. The count can then be used to calculate
the number of pages based on the limit that is set.

 **Example:** Fetch a list of articles where a certain condition is true and get their count. Then limit the number of
articles to return.

Caveat

If this needs to be done over[ subscriptions ](https://hasura.io/docs/latest/subscriptions/postgres/index/), two subscriptions will need to be run
as Hasura follows the[ GraphQL spec ](https://graphql.github.io/graphql-spec/June2018/#sec-Single-root-field)which
allows for only one root field in a subscription.

### What did you think of this doc?

- [ The limit & offset arguments ](https://hasura.io/docs/latest/queries/postgres/pagination/#the-limit--offset-arguments)
- [ Limit results ](https://hasura.io/docs/latest/queries/postgres/pagination/#limit-results)
- [ Limit results from an offset ](https://hasura.io/docs/latest/queries/postgres/pagination/#limit-results-from-an-offset)
- [ Limit results in a nested object ](https://hasura.io/docs/latest/queries/postgres/pagination/#pg-nested-paginate)
- [ Keyset cursor based pagination ](https://hasura.io/docs/latest/queries/postgres/pagination/#keyset-cursor-based-pagination)
- [ Fetch limited results along with data aggregated over all results (e.g. total count) in the same query ](https://hasura.io/docs/latest/queries/postgres/pagination/#fetch-limited-results-along-with-data-aggregated-over-all-results-eg-total-count-in-the-same-query)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)