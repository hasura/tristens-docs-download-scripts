# Postgres Constraints

## Introduction​

[ Postgres constraints ](https://www.postgresql.org/docs/current/ddl-constraints.html)are used to define rules for
columns in a database table. They ensure that no invalid data is entered into the database.

Note

For more detailed information on Postgres constraints, please refer to the[ Postgres documentation ](https://www.postgresql.org/docs/current/ddl-constraints.html).

## Postgres constraints​

There are different types of constraints that can be used with Postgres.

### Primary key constraints​

A `PRIMARY KEY` is used to identify each row of a table uniquely.

 **Identify the author's id as the primary key of the authors table:** 

```
CREATE   TABLE  authors (
  id  INT   PRIMARY   KEY ,
  name            TEXT      NOT   NULL
) ;
```

### Foreign key constraints​

A foreign key constraint specifies that the values in a column must match the values appearing in a row of another
table. Foreign key constraints are used to create relationships between tables.

 **Define the author_id in the articles table as a foreign key to the id column in the authors table:** 

```
CREATE   TABLE  authors (
  id  SERIAL   PRIMARY   KEY ,
  name            TEXT      NOT   NULL ,
  email           TEXT      UNIQUE
) ;
CREATE   TABLE  articles (
  id  SERIAL   PRIMARY   KEY ,
  title           TEXT      NOT   NULL ,
  author_id  INTEGER ,
   FOREIGN   KEY   ( author_id )   REFERENCES  authors  ( id )
) ;
```

### Not-null constraints​

A not-null constraint allows you to specify that a column's value cannot be `null` .

 **Validate that an author's name cannot be null:** 

```
CREATE   TABLE  authors (
  id  SERIAL   PRIMARY   KEY ,
  name            TEXT      NOT   NULL
) ;
```

### Unique constraints​

Unique constraints prevent database entries with a duplicate value of the respective column.

 **Validate that an author's email is unique:** 

```
CREATE   TABLE  authors (
  id  SERIAL   PRIMARY   KEY ,
  name            TEXT      NOT   NULL ,
  email           TEXT      UNIQUE
) ;
```

### Check constraints​

Check constraints allow you to specify a `Boolean` expression for one or several columns. This Boolean expression must
be satisfied (equal to `true` ) by the column value for the object to be inserted.

 **Validate that an author's rating is between 1 and 10:** 

```
CREATE   TABLE  authors (
  id  SERIAL   PRIMARY   KEY ,
  name            TEXT      NOT   NULL ,
  rating          INT       NOT   NULL   CHECK ( rating  >   0   AND  rating  <=   10 )
) ;
```

## Postgres constraints & Hasura​

Most Postgres constraints (primary key, foreign key, not-null and unique constraints) can be added to Hasura natively
when[ creating tables ](https://hasura.io/docs/latest/schema/postgres/tables/#pg-create-tables).

Postgres check constraints can be used as a form of data validation in Hasura and can be added[ as described here ](https://hasura.io/docs/latest/schema/postgres/data-validations/#pg-data-validations-check-constraints).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/constraints/#introduction)
- [ Postgres constraints ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/constraints/#postgres-constraints-1)
    - [ Primary key constraints ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/constraints/#primary-key-constraints)

- [ Foreign key constraints ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/constraints/#foreign-key-constraints)

- [ Not-null constraints ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/constraints/#not-null-constraints)

- [ Unique constraints ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/constraints/#unique-constraints)

- [ Check constraints ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/constraints/#check-constraints)
- [ Postgres constraints & Hasura ](https://hasura.io/docs/latest/schema/postgres/postgres-guides/constraints/#postgres-constraints--hasura)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)