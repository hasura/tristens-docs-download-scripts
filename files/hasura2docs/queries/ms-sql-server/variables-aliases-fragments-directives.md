# Use Variables / Aliases / Fragments / Directives in Queries

## Using variables​

In order to make a query re-usable, it can be made dynamic by using
variables.

 **Example:** Fetch an author by their `author_id` :

## Using aliases​

Aliases can be used to return objects with a different name than their
field name. This is especially useful while fetching the same type of
objects with different arguments in the same query.

 **Example:** First, fetch all articles. Second, fetch the two top-rated
articles. Third, fetch the worst-rated article:

## Using fragments​

Sometimes, queries can get long and confusing. A fragment is a set of
fields with any chosen name. This fragment can then be used to represent
the defined set.

 **Example:** Creating a fragment for a set of `article` fields ( `id` and `title` ) and using it in a query:

## Using directives​

Directives make it possible to include or skip a field based on a
boolean expression passed as a query variable.

### @include(if: Boolean)​

With `@include(if: Boolean)` , it is possible to include a field in the
query result based on a Boolean expression.

 **Example:** The query result includes the field `publisher` , as `$with_publisher` is set to `true` :

 **Example:** The query result doesn't include the field `publisher` , as `$with_publisher` is set to `false` :

### @skip(if: Boolean)​

With `@skip(if: Boolean)` , it is possible to exclude (skip) a field in
the query result based on a Boolean expression.

 **Example:** The query result doesn't include the field `publisher` , as `$with_publisher` is set to `true` :

 **Example:** The query result includes the field `publisher` , as `$with_publisher` is set to `false` :

### What did you think of this doc?

- [ Using variables ](https://hasura.io/docs/latest/queries/ms-sql-server/variables-aliases-fragments-directives/#using-variables)
- [ Using aliases ](https://hasura.io/docs/latest/queries/ms-sql-server/variables-aliases-fragments-directives/#using-aliases)
- [ Using fragments ](https://hasura.io/docs/latest/queries/ms-sql-server/variables-aliases-fragments-directives/#using-fragments)
- [ Using directives ](https://hasura.io/docs/latest/queries/ms-sql-server/variables-aliases-fragments-directives/#using-directives)
    - [ @include(if: Boolean) ](https://hasura.io/docs/latest/queries/ms-sql-server/variables-aliases-fragments-directives/#includeif-boolean)

- [ @skip(if: Boolean) ](https://hasura.io/docs/latest/queries/ms-sql-server/variables-aliases-fragments-directives/#skipif-boolean)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)