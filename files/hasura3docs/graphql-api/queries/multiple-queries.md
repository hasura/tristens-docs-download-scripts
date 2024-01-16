# Multiple Queries in a Request

## Execution​

You can fetch objects of different unrelated types in the same query.

## Run multiple top level queries in the same request​

 **For example** , fetch a list of `authors` and a list of `articles` :

## Fetch limited results along with data aggregated over all results (e.g. total count) in the same query​

Sometimes, some aggregated information on all the data is required along with a subset of data.

E.g. the total count of results can be returned along with a page of results. The count can then be used to calculate
the number of pages based on the limit that is set.

 **Example:** Fetch a list of articles where a certain condition is true and get their count. Then limit the number of
articles to return.

### What did you think of this doc?

- [ Execution ](https://hasura.io/docs/3.0/graphql-api/queries/multiple-queries/#execution)
- [ Run multiple top level queries in the same request ](https://hasura.io/docs/3.0/graphql-api/queries/multiple-queries/#run-multiple-top-level-queries-in-the-same-request)
- [ Fetch limited results along with data aggregated over all results (e.g. total count) in the same query ](https://hasura.io/docs/3.0/graphql-api/queries/multiple-queries/#fetch-limited-results-along-with-data-aggregated-over-all-results-eg-total-count-in-the-same-query)
