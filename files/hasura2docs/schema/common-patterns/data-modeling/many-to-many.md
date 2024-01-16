# Modeling Many-to-Many Table Relationships

## Introduction​

A `many-to-many` relationship between two tables can be established by creating a table typically called as **bridge/junction/join table** and adding **foreign-key constraints** from it to the original tables.

Say we have the following two tables in our database schema:

```
articles  (
  id  SERIAL   PRIMARY   KEY ,
  title  TEXT
   . . .
)
tags  (
  id  SERIAL   PRIMARY   KEY ,
  tag_value  TEXT
   . . .
)
```

These two tables are related via a `many-to-many` relationship. i.e:

- an `article` can have many `tags`
- a `tag` has many `articles`


## Step 1: Set up a table relationship in the database​

This `many-to-many` relationship can be established in the database by:

1. Creating a **bridge table** called `article_tag` with the following structure:


Creating a **bridge table** called `article_tag` with the following structure:

```
article_tag  (
  id  SERIAL   PRIMARY   KEY
  article_id  INT
  tag_id  INT
   UNIQUE   ( article_id ,  tag_id )
   . . .
)
```

Note

If you can have multiple rows linking the same `article` and `tag` in your model, you can skip the unique constraint on `(article_id, tag_id)` 

1. Adding **foreign key constraints** in the `article_tag` table for:
    - the `articles` table using the `article_id` and `id` columns of the tables respectively

- the `tags` table using the `tag_id` and `id` columns of the tables respectively

2. the `articles` table using the `article_id` and `id` columns of the tables respectively

3. the `tags` table using the `tag_id` and `id` columns of the tables respectively


Adding **foreign key constraints** in the `article_tag` table for:

The table `article_tag` sits between the two tables involved in the many-to-many relationship and captures possible
permutations of their association via the foreign keys.

## Step 2: Set up GraphQL relationships​

To access the nested objects via the GraphQL API,[ create the following relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/create/):

- Array relationship, `article_tags` from `articles` table using `article_tag :: article_id -> id`
- Object relationship, `tag` from `article_tag` table using `tag_id -> tags :: id`
- Array relationship, `tag_articles` from `tags` table using `article_tag :: tag_id -> id`
- Object relationship, `article` from `article_tag` table using `article_id -> articles :: id`


## Query using many-to-many relationships​

We can now:

- fetch a list of `articles` with their `tags` :


- fetch a list of `tags` with their `articles` :


## Insert using many-to-many relationships​

We can now:

- insert an `article` with `tags` where the `tag` might already exist (assume unique `value` for `tag` ):


- insert a `tag` with `articles` where the `tag` might already exist (assume unique `value` for `tag` ):


Note

You can avoid the `on_conflict` clause if you will never have conflicts.

## Fetching relationship information​

The intermediate fields `article_tags` & `tag_articles` can be used to fetch extra information about the relationship.
For example, you can have a column like `tagged_at` in the `article_tag` table which you can fetch as follows:

## Flattening a many-to-many relationship query​

In case you would like to flatten the above queries and avoid the intermediate fields `article_tags` & `tag_articles` ,
you can[ create the following views ](https://hasura.io/docs/latest/schema/postgres/views/)additionally and then query using relationships created
on these views:

```
CREATE   VIEW  article_tags_view  AS
   SELECT  article_id ,  tags . *
     FROM  article_tag  LEFT   JOIN  tags
       ON  article_tag . tag_id  =  tags . id
CREATE   VIEW  tag_articles_view  AS
   SELECT  tag_id ,  articles . *
     FROM  article_tag  LEFT   JOIN  articles
       ON  article_tag . article_id  =  articles . id
```

Now[ create the following relationships ](https://hasura.io/docs/latest/schema/postgres/table-relationships/create/):

- Array relationship, `tags` from the `articles` table using `article_tags_view :: article_id -> id`
- Array relationship, `articles` from the `tags` table using `tag_articles_view :: tag_id -> id`


We can now:

- fetch articles with their tags without an intermediate field:


- fetch tags with their articles without an intermediate field:


Note

 **We do not recommend this** flattening pattern of modeling as this introduces an additional overhead of managing
permissions and relationships on the newly created views. e.g. You cannot query for the author of the nested articles
without setting up a new relationship to the `authors` table from the `tag_articles_view` view.

In our opinion, the cons of this approach seem to outweigh the pros.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/many-to-many/#introduction)
- [ Step 1: Set up a table relationship in the database ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/many-to-many/#step-1-set-up-a-table-relationship-in-the-database)
- [ Step 2: Set up GraphQL relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/many-to-many/#step-2-set-up-graphql-relationships)
- [ Query using many-to-many relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/many-to-many/#query-using-many-to-many-relationships)
- [ Insert using many-to-many relationships ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/many-to-many/#insert-using-many-to-many-relationships)
- [ Fetching relationship information ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/many-to-many/#fetching-relationship-information)
- [ Flattening a many-to-many relationship query ](https://hasura.io/docs/latest/schema/common-patterns/data-modeling/many-to-many/#flattening-a-many-to-many-relationship-query)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)