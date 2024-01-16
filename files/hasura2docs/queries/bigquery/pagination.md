# BigQuery: Paginate Query Results

## The limit & offset arguments​

The operators `limit` and `offset` are used for pagination.

 `limit` specifies the number of rows to retain from the result set and `offset` determines which slice to retain from the results.

You can see the complete specification of the `limit` and `offset` arguments in the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#paginationexp).

The following are examples of different pagination scenarios:

## Limit results​

 **Example:** Fetch the first 5 authors from the list of all authors:

Note

The query field will be of the format `<dataset_name>_<table_name>` .

## Limit results from an offset​

 **Example:** Fetch 5 authors from the list of all authors, starting with
the 6th one:

## Limit results in a nested object​

 **Example:** Fetch a list of authors and a list of their first 2
articles:

## Fetch limited results along with data aggregated over all results (e.g. total count) in the same query​

Sometimes, some aggregated information on all the data is required along
with a subset of data.

E.g. the total count of results can be returned along with a page of
results. The count can then be used to calculate the number of pages
based on the limit that is set.

 **Example:** Fetch a list of articles where a certain condition is true
and get their count. Then limit the number of articles to return.

### What did you think of this doc?

- [ The limit & offset arguments ](https://hasura.io/docs/latest/queries/bigquery/pagination/#the-limit--offset-arguments)
- [ Limit results ](https://hasura.io/docs/latest/queries/bigquery/pagination/#limit-results)
- [ Limit results from an offset ](https://hasura.io/docs/latest/queries/bigquery/pagination/#limit-results-from-an-offset)
- [ Limit results in a nested object ](https://hasura.io/docs/latest/queries/bigquery/pagination/#bq-nested-paginate)
- [ Fetch limited results along with data aggregated over all results (e.g. total count) in the same query ](https://hasura.io/docs/latest/queries/bigquery/pagination/#fetch-limited-results-along-with-data-aggregated-over-all-results-eg-total-count-in-the-same-query)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)