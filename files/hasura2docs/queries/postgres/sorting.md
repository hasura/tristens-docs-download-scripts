# Postgres: Sort Query Results

## The order_by argument​

Results from your query can be sorted by using the `order_by` argument.
The argument can be used to sort nested objects too.

The sort order (ascending vs. descending) is set by specifying the `asc` or `desc` enum value for the column name in the `order_by` input object,
e.g. `{name: desc}` .

By default, for ascending ordering `null` values are returned at the end
of the results and for descending ordering `null` values are returned at
the start of the results. `null` values can be fetched first on
ascending ordering by specifying `asc_nulls_first` and last on
descending ordering by specifying `desc_nulls_last` enum value e.g. `{name: desc_nulls_last}` .

The `order_by` argument takes an array of objects to allow sorting by
multiple columns.

You can also use nested objects' fields to sort the results. Only **columns from object relationships** and **aggregates from array
relationships** can be used for sorting.

You can see the complete specification of the `order_by` argument in the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#orderbyexp).

The following are example queries for different sorting use cases:

## Sorting objects​

 **Example:** Fetch a list of authors sorted by their names in an
ascending order:

## Sorting nested objects​

 **Example:** Fetch a list of authors sorted by their names with a list
of their articles that is sorted by their rating:

## Sorting based on nested object's fields​

Only **columns from object relationships** and **aggregates from array
relationships** can be used for sorting.

### For object relationships​

For object relationships only columns can be used for sorting.

 **Example:** Fetch a list of articles that are sorted by their author's
ids in descending order:

### For array relationships​

For array relationships only aggregates can be used for sorting.

 **Example:** Fetch a list of authors sorted in descending order of their
article count:

 **Example:** Fetch a list of authors sorted in increasing order of their
highest article rating:

## Sorting based on computed fields​

Only scalar computed fields and aggregates of table computed fields can
be used for sorting.

### For scalar computed fields​

Scalar computed fields can be used for sorting just like columns.

 **Example:** Computed field `total_marks` is defined on `student` table
which calculates the sum of marks obtained in each subject. Fetch a list
of students sorted by their total marks:

### For table computed fields​

Aggregates of table being returned by table computed fields can be used
for sorting.

 **Example:** Computed field `get_articles` is defined to `author` table
returns list of articles. Fetch a list of authors sorted by their
articles count.

Note

Only computed fields whose associated SQL function with no input
arguments other than table row and hasura session arguments are
supported in order by.

Supported from

Ordering by computed fields is supported from version `v2.0.2` and above

## Sorting by multiple fields​

 **Example:** Fetch a list of articles that is sorted by their rating
(descending) and then on their published date (ascending with nulls
first):

Note

Key order in input object for order_by is[ not preserved ](https://github.com/hasura/graphql-engine/releases/tag/v2.0.0). This means you should only have a single key per object, or you may see unexpected behavior.

### What did you think of this doc?

- [ The order_by argument ](https://hasura.io/docs/latest/queries/postgres/sorting/#the-order_by-argument)
- [ Sorting objects ](https://hasura.io/docs/latest/queries/postgres/sorting/#sorting-objects)
- [ Sorting nested objects ](https://hasura.io/docs/latest/queries/postgres/sorting/#pg-nested-sort)
- [ Sorting based on nested object's fields ](https://hasura.io/docs/latest/queries/postgres/sorting/#sorting-based-on-nested-objects-fields)
    - [ For object relationships ](https://hasura.io/docs/latest/queries/postgres/sorting/#for-object-relationships)

- [ For array relationships ](https://hasura.io/docs/latest/queries/postgres/sorting/#for-array-relationships)
- [ Sorting based on computed fields ](https://hasura.io/docs/latest/queries/postgres/sorting/#sorting-based-on-computed-fields)
    - [ For scalar computed fields ](https://hasura.io/docs/latest/queries/postgres/sorting/#for-scalar-computed-fields)

- [ For table computed fields ](https://hasura.io/docs/latest/queries/postgres/sorting/#for-table-computed-fields)
- [ Sorting by multiple fields ](https://hasura.io/docs/latest/queries/postgres/sorting/#sorting-by-multiple-fields)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)