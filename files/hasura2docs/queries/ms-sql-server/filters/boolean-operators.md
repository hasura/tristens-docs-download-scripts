# MS SQL Server: Filter Using Boolean Expressions

## Filter based on failure of some criteria (_not)​

The `_not` operator can be used to fetch results for which some condition does not hold true. i.e. to invert the filter
set for a condition.

 **Example:  _ not** 

Fetch all authors who don't have any published articles:

## Using multiple filters in the same query (_and, _or)​

You can group multiple parameters in the same `where` argument using the `_and` or the `_or` operators to filter results
based on more than one criteria.

Note

You can use the `_or` and `_and` operators along with the `_not` operator to create arbitrarily complex boolean
expressions involving multiple filtering criteria.

 **Example:  _ and** 

Fetch a list of articles published in a specific time-frame (for example: in year 2017):

Note

Certain `_and` expressions can be expressed in a simpler format using some syntactic sugar. See the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#andexp)for more details.

 **Example:  _ or** 

Fetch a list of articles rated more than 4 or published after "01/01/2018":

Note

The `_or` operator expects an array of expressions as input. If an object is passed as input it will behave like the `_and` operator as explained in the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#orexp)

### What did you think of this doc?

- [ Filter based on failure of some criteria (_not) ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/boolean-operators/#filter-based-on-failure-of-some-criteria-_not)
- [ Using multiple filters in the same query (_and, _or) ](https://hasura.io/docs/latest/queries/ms-sql-server/filters/boolean-operators/#using-multiple-filters-in-the-same-query-_and-_or)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)