# Postgres: Filter Using Values of Computed Fields

## Introduction​

You can use computed fields to filter your query results.

For example:

```
query   {
   author ( where :   {   full_name :   {   _ilike :   "%bob%"   }   } )   {
     id
     first_name
     last_name
   }
}
```

The behavior of the comparison operators depends on whether the computed fields return scalar type values or set of
table rows.

- In case of scalar type, a row will be returned if the computed field returned scalar value satisfied the defined
condition.
- In case of table row type, a row will be returned if **any of the returned rows** sastisfy the defined condition.


Let's look at a few use cases based on the above:

## Fetch if the scalar value returned by the computed field satisfies a condition​

 **Example:** 

A computed field `total_marks` defined to a `student` table which computes the total sum of marks obtained from each
subject. Fetch all students whose total marks is above "80":

## Fetch if any of the returned table rows by the computed field satisfy a condition​

 **Example:** 

A computed field `get_published_articles` defined to a `author` table which returns set of `article` rows published.
Fetch all authors who have atleast a published article in medicine field:

## Fetch if aggregate value of the returned table rows by the computed field satisfies a condition​

 **Example:** 

A computed field `get_published_articles` defined to a `author` table which returns set of `article` rows published.
Fetch all authors whose count of published articles is more than 10:

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/queries/postgres/filters/using-computed-fields/#introduction)
- [ Fetch if the scalar value returned by the computed field satisfies a condition ](https://hasura.io/docs/latest/queries/postgres/filters/using-computed-fields/#fetch-if-the-scalar-value-returned-by-the-computed-field-satisfies-a-condition)
- [ Fetch if any of the returned table rows by the computed field satisfy a condition ](https://hasura.io/docs/latest/queries/postgres/filters/using-computed-fields/#fetch-if-any-of-the-returned-table-rows-by-the-computed-field-satisfy-a-condition)
- [ Fetch if aggregate value of the returned table rows by the computed field satisfies a condition ](https://hasura.io/docs/latest/queries/postgres/filters/using-computed-fields/#fetch-if-aggregate-value-of-the-returned-table-rows-by-the-computed-field-satisfies-a-condition)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)