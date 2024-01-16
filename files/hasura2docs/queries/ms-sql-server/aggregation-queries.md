# MS SQL Server: Aggregation Queries

## Aggregate fields​

You can fetch aggregations on columns along with nodes using an aggregation query.

The **name of the aggregate field** is of the form `<field-name> + _aggregate` .

Common aggregation functions are `count` , `sum` , `avg` , `max` , `min` , etc. You
can see the complete specification of the aggregate field in the[ API
reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#aggregateobject). Note that not
all aggregation functions are available for all data types.

Note

For more advanced use cases, you can use[ views ](https://hasura.io/docs/latest/schema/ms-sql-server/views/).

## Fetch aggregated data of an object​

 **Example:** Fetch a list of articles with aggregated data of their rating:

## Fetch aggregated data on nested objects​

The following is an example of a nested object query with aggregations on the **array relationship** between an author
and articles.

 **Example:** Fetch author with id "1" and a nested list of articles with aggregated data of their rating:

### What did you think of this doc?

- [ Aggregate fields ](https://hasura.io/docs/latest/queries/ms-sql-server/aggregation-queries/#aggregate-fields)
- [ Fetch aggregated data of an object ](https://hasura.io/docs/latest/queries/ms-sql-server/aggregation-queries/#fetch-aggregated-data-of-an-object)
- [ Fetch aggregated data on nested objects ](https://hasura.io/docs/latest/queries/ms-sql-server/aggregation-queries/#ms-sql-server-nested-aggregate)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)