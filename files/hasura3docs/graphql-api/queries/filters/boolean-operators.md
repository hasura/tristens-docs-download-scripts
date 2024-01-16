# Filter by Boolean Expressions

## Filter based on failure of some criteria (_not)​

The `_not` operator can be used to fetch results for which some condition does not hold true. i.e. to invert the filter
set for a condition.

 **Example:  _ not** 

Fetch all authors who don't have any published articles:

## Using multiple filters in the same query (_and, _or)​

You can group multiple parameters in the same `where` argument using the `_and` or the `_or` operators to filter results
based on more than one criterion.

Note

You can use the `_or` and `_and` operators along with the `_not` operator to create arbitrarily complex boolean
expressions involving multiple filtering criteria.

 **Example:  _ and** 

Fetch a list of articles published in a specific time-frame (for example: in year 2017):

Note

Certain `_and` expressions can be expressed in a simpler format using some syntactic sugar.

 **Example:  _ or** 

Fetch a list of articles rated more than 4 or published after "01/01/2018":

### What did you think of this doc?

- [ Filter based on failure of some criteria (_not) ](https://hasura.io/docs/3.0/graphql-api/queries/filters/boolean-operators/#filter-based-on-failure-of-some-criteria-_not)
- [ Using multiple filters in the same query (_and, _or) ](https://hasura.io/docs/3.0/graphql-api/queries/filters/boolean-operators/#using-multiple-filters-in-the-same-query-_and-_or)
