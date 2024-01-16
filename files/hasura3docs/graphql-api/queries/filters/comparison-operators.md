# Filter by Comparing Values

## Introduction​

Comparison operators are used to compare values of the same type. For example, to compare two numbers, two strings, two
dates, etc.

## Equality operators (_eq, _neq)​

The `_eq` (equal to) or the `_neq` (not equal to) operators are compatible with any type other than `json` or `jsonB` (like `Integer` , `Float` , `Double` , `Text` , `Boolean` , `Date` / `Time` / `Timestamp` , etc.).

The following are examples of using the equality operators on different types.

 **Example: Integer (works with Double, Float, Numeric, etc.)** 

Fetch data about an author whose `id`  *(an integer field)* is equal to 3:

 **Example: String or Text** 

Fetch a list of authors with `name`  *(a text field)* as "Sidney":

 **Example: Boolean** 

Fetch a list of articles that have not been published ( `is_published` is a boolean field):

 **Example: Date (works with Time, Timezone, etc.)** 

Fetch a list of articles that were published on a certain date ( `published_on` is a Date field):

 **Example: Integer (works with Integer, Float, Double, etc.)** 

Fetch a list of users whose age is *not* 30 ( `age` is an Integer field):

Caveat for "null" values

By design, the `_eq` or `_neq` operators will not return rows with `null` values.

To also return rows with `null` values, the `_is_null` operator needs to be used along with these joined by the `_or` operator.

For example, to fetch a list of articles where the `is_published` column is either `false` or `null` :

## Greater than or less than operators (_gt, _lt, _gte, _lte)​

The `_gt` (greater than), `_lt` (less than), `_gte` (greater than or equal to), `_lte` (less than or equal to) operators
are compatible with any type other than `json` or `jsonB` (like `Integer` , `Float` , `Double` , `Text` , `Boolean` , `Date` / `Time` / `Timestamp` , etc.).

The following are examples of using these operators on different types:

 **Example: Integer (works with Double, Float, Numeric, etc.)** 

This query retrieves all users whose age is less than 30. The `_lt` operator is a comparison operator that means "less
than". It is used to filter records based on a specified value.

 **Example: String or Text** 

Fetch a list of authors whose names begin with M or any letter that follows M *(essentially, a filter based on a
dictionary sort)* :

 **Example: Integer (works with Double, Float, etc.)** 

Fetch a list of all products with a price less than or equal to 10.

 **Example: Integer (works with Double, Float, etc.)** 

Fetch a list of articles rated 4 or more ( `rating` is an integer field):

 **Example: Date (works with Time, Timezone, etc.)** 

Fetch a list of articles that were published on or after date "01/01/2018":

## List based search operators (_in)​

The `_in` (in a list) operator is used to compare field values to a list of values. They are compatible with any
type other than `json` or `jsonB` (like `Integer` , `Float` , `Double` , `Text` , `Boolean` , `Date` / `Time` / `Timestamp` , etc.).

The following are examples of using these operators on different types:

 **Example: Integer (works with Double, Float, etc.)** 

Fetch a list of articles rated 1, 3 or 5:

## Filter or check for null values (_is_null)​

Checking for null values can be achieved using the `_is_null` operator.

 **Example: Filter null values in a field** 

Fetch a list of articles that have a value in the `published_on` field:

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/graphql-api/queries/filters/comparison-operators/#introduction)
- [ Equality operators (_eq, _neq) ](https://hasura.io/docs/3.0/graphql-api/queries/filters/comparison-operators/#equality-operators-_eq-_neq)
- [ Greater than or less than operators (_gt, _lt, _gte, _lte) ](https://hasura.io/docs/3.0/graphql-api/queries/filters/comparison-operators/#greater-than-or-less-than-operators-_gt-_lt-_gte-_lte)
- [ List based search operators (_in) ](https://hasura.io/docs/3.0/graphql-api/queries/filters/comparison-operators/#list-based-search-operators-_in)
- [ Filter or check for null values (_is_null) ](https://hasura.io/docs/3.0/graphql-api/queries/filters/comparison-operators/#filter-or-check-for-null-values-_is_null)
