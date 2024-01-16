# Postgres: Distinct Query Results

## The distinct_on argument​

You can fetch rows with only distinct values of a column using the `distinct_on` argument.

It is typically recommended to use `order_by` along with `distinct_on` to ensure we get predictable results *(otherwise
any arbitrary row with a distinct value of the column may be returned)* . Note that the `distinct_on` column needs to be
the first column in the `order_by` expression. See[ sort queries ](https://hasura.io/docs/latest/queries/postgres/sorting/)for more info on using `order_by` .

```
employees   (
   distinct_on :   [ employees_select_column ]
   order_by :   [ employees_order_by ]
) :   [ employees ] !
# select column enum type for "employees" table
enum   employees_select_column   {
   id
   name
   department
   salary
}
```

You can see the complete specification of the `distinct_on` argument in the[ API reference ](https://hasura.io/docs/latest/api-reference/graphql-api/query/#distinctonexp).

## Fetch results with distinct values of a particular field​

 **For example** , fetch the employee with the highest salary from each department:

### What did you think of this doc?

- [ The distinct_on argument ](https://hasura.io/docs/latest/queries/postgres/distinct-queries/#the-distinct_on-argument)
- [ Fetch results with distinct values of a particular field ](https://hasura.io/docs/latest/queries/postgres/distinct-queries/#fetch-results-with-distinct-values-of-a-particular-field)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)