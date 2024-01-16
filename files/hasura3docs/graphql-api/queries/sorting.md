# Sort Query Results

## The order_by argument​

Results from your query can be sorted by using the `order_by` argument. The argument can be used to sort nested objects
too.

The sort order (ascending vs. descending) is set by specifying the `Asc` or `Desc` enum value for the column name in the `order_by` input object, e.g. `{name: Desc}` .

By default, for ascending ordering `null` values are returned at the end of the results and for descending ordering `null` values are returned at the start of the results.

The `order_by` argument takes an array of objects to allow sorting by multiple columns.

You can also use nested objects' fields to sort the results. Only columns from object relationships ** and ** aggregates
from array relationships** can be used for sorting.

The following are example queries for different sorting use cases:

## Sorting objects​

 **Example:** Fetch a list of authors sorted by their names in ascending order:

## Sorting nested objects​

 **Example:** Fetch a list of authors sorted by their names with a list of their articles that is sorted by their rating:

## Sorting based on nested object's fields​

Only **columns from object relationships** and **aggregates from array relationships** can be used for sorting.

### For object relationships​

For object relationships only columns can be used for sorting.

 **Example:** Fetch a list of articles that are sorted by their author's ids in descending order:

### For array relationships​

For array relationships only aggregates can be used for sorting.

 **Example:** Fetch a list of authors sorted in descending order of their article count:

 **Example:** Fetch a list of authors sorted in increasing order of their highest article rating:

### For scalar computed fields​

Scalar computed fields can be used for sorting just like columns.

 **Example:** Computed field `total_marks` is defined on `student` table which calculates the sum of marks obtained in*each subject. Fetch a list of students sorted by their total marks:

### For table computed fields​

Aggregates of table being returned by table computed fields can be used for sorting.

 **Example:** Computed field `get_articles` is defined to `author` table returns list of articles. Fetch a list of*authors sorted by their articles count.

Note

Only computed fields whose associated SQL function with no input arguments other than table row and hasura session
arguments are supported in order by.

## Sorting by multiple fields​

 **Example:** Fetch a list of articles that is sorted by their rating (descending) and then on their published date
(ascending):

Note

Key order in input object for order_by is not preserved. This means you should only have a single key per object, or you
may see unexpected behavior.

### What did you think of this doc?

- [ The order_by argument ](https://hasura.io/docs/3.0/graphql-api/queries/sorting/#the-order_by-argument)
- [ Sorting objects ](https://hasura.io/docs/3.0/graphql-api/queries/sorting/#sorting-objects)
- [ Sorting nested objects ](https://hasura.io/docs/3.0/graphql-api/queries/sorting/#pg-nested-sort)
- [ Sorting based on nested object's fields ](https://hasura.io/docs/3.0/graphql-api/queries/sorting/#sorting-based-on-nested-objects-fields)
    - [ For object relationships ](https://hasura.io/docs/3.0/graphql-api/queries/sorting/#for-object-relationships)

- [ For array relationships ](https://hasura.io/docs/3.0/graphql-api/queries/sorting/#for-array-relationships)

- [ For scalar computed fields ](https://hasura.io/docs/3.0/graphql-api/queries/sorting/#for-scalar-computed-fields)

- [ For table computed fields ](https://hasura.io/docs/3.0/graphql-api/queries/sorting/#for-table-computed-fields)
- [ Sorting by multiple fields ](https://hasura.io/docs/3.0/graphql-api/queries/sorting/#sorting-by-multiple-fields)
