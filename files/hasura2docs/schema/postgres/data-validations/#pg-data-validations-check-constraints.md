# Postgres: Data Validations

## Introduction​

Many times, we need to perform validations of input data before inserting or updating objects.

The best solution to implement a validation depends on the complexity of the validation logic and the layer where you
would like to add it.

- If you would like the validation logic to be a part of your database schema, Postgres check constraints or triggers
would be ideal solutions to add your validation.
- If you would like the validation logic to be at the GraphQL API layer, Hasura permissions can be used to add your
validation.
- If the validation logic requires complex business logic and/or needs information from external sources, you can use
Hasura Actions to perform your validation.


These solutions are explained in some more detail below.

## Using Postgres check constraints​

If the validation logic can be expressed by using only static values and the columns of the table, you can use[ Postgres check constraints ](https://www.postgresql.org/docs/current/ddl-constraints.html).

 **Example:** Check that the `rating` for an author is between 1 and 10 only.

Let's say we have the following table in our schema:

`author  ( id uuid ,  name  text ,  rating  integer )`

We can now add a check constraint to limit the `rating` values as follows:

- Console
- CLI
- API


Head to the `Modify` tab in the table page and add a check constraint in the `Check Constraints` section:

Image: [ Add check constraint ](https://hasura.io/docs/assets/images/validation-add-check-constraint-e26d804f9f5e9e9a966e3739ab4b28fb.png)

[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
following SQL statement to the `up.sql` file:

```
ALTER   TABLE  author
ADD   CONSTRAINT  authors_rating_check  CHECK   ( rating  >   0   AND  rating  <=   10 ) ;
```

Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)the above statement:

`ALTER   TABLE  author  DROP   CONSTRAINT  authors_rating_check ;`

Apply the migration by running:

`hasura migrate apply`

You can add a check constraint by using the[ run_sql ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql)schema API:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "run_sql" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "sql" :   "ALTER TABLE author ADD CONSTRAINT authors_rating_check CHECK (rating > 0 AND rating <= 10);"
   }
}
```

If someone now tries to add an author with a rating of `11` , the following error is thrown:

Learn more about[ Postgres check constraints ](https://www.postgresql.org/docs/current/ddl-constraints.html).

## Using Postgres triggers​

If the validation logic is more complex and requires the use of data from other tables and/or functions, then you can
use[ Postgres triggers ](https://www.postgresql.org/docs/current/sql-createtrigger.html).

 **Example:** Validate that an article's `content` does not exceed a certain number of words.

Suppose we have the following table in our schema:

`article  ( id uuid ,  title  text ,  content  text )`

We can now create a[ Postgres function ](https://www.postgresql.org/docs/current/sql-createfunction.html)that checks if
an article's content exceeds a certain number of words, and then add a[ Postgres trigger ](https://www.postgresql.org/docs/current/sql-createtrigger.html)that will call this function every
time before an article is inserted or updated.

- Console
- CLI
- API


- Head to the `Data -> SQL` section of the Hasura Console
- Enter the SQL statement below to create a Postgres function and trigger
- Hit the `Run` button


[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the SQL
statement below to create a Postgres function and trigger to the `up.sql` file. Also, add an SQL statement to the `down.sql` to revert the previous statement in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)the migration.

Apply the migration by running:

`hasura migrate apply`

You can add a Postgres function and trigger by using the[ run_sql ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql)schema API:

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "run_sql" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "sql" :   "<SQL statement below>"
   }
}
```

```
CREATE   FUNCTION  check_content_length ( )
RETURNS trigger  AS  $$
DECLARE  content_length INTEGER ;
BEGIN
   -- split article content into words and get count
   select  array_length ( regexp_split_to_array ( NEW . content ,   '\s' ) , 1 )   INTO  content_length ;
   -- throw an error if article content is too long
   IF  content_length  >   100   THEN
       RAISE   EXCEPTION   USING  ERRCODE =   '22000' ,  MESSAGE =   'Content can not have more than 100 words' ;
   END   IF ;
   -- return the article row if no error
   RETURN   NEW ;
END ;
$$  LANGUAGE  plpgsql ;
CREATE  TRIGGER check_content_length_trigger
  BEFORE  INSERT   OR   UPDATE   ON   "article"
   FOR  EACH  ROW
   EXECUTE   PROCEDURE  check_content_length ( ) ;
```

Now, if we try to insert an article whose content has more than 100 words, we'll receive the following error:

Learn more about[ Postgres triggers ](https://www.postgresql.org/docs/current/sql-createtrigger.html).

## Using Hasura permissions​

Hasura permissions provides two different ways to validate data:

1. If input arguments of a mutations needs to be validated, you can use the[ input validation ](https://hasura.io/docs/latest/schema/postgres/input-validations/)feature. This
allows you to write custom validation logic that is run in an external webhook before hitting the
database to execute the mutation.
2. If the validation logic can be expressed **declaratively** using static
values and data from the database, then you can use[ row level
permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/)to
perform the validations. (Read more
about[ Authorization ](https://hasura.io/docs/latest/auth/authorization/index/)).


 **Example 1:** Validate that a valid email is being inserted

Suppose, we have the following table in our schema:

`customer  ( id uuid ,  name  text ,  city  text ,  email  text )`

Now, we can create a role `user` and add an input validation rule as follows:

- Console
- CLI
- API


Image: [ Using boolean expressions to build rules ](https://hasura.io/docs/assets/images/input-validation-create-permission-fa7453419abaa5ac06f883f67e1080fe.png)

You can define the input validation  in the `metadata -> databases -> [database-name] -> tables -> [table-name].yaml` file, eg:

```
-   table :
     schema :  public
     name :  customer
   insert_permissions :
     -   role :  user
       permission :
         columns :   [ ]
         filter :   { }
         validate_input :
           type :  http
           definition :
             url :  http : //www.somedomain.com/validateCustomerMutation
             forward_client_headers :   true
             timeout :   5
        
```

Apply the Metadata by running:

`hasura metadata apply`

You can define the input validations when using the[ permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/).
Example with a Postgres DB:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_insert_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "customer" ,
     "role" :   "user" ,
     "permission" :   {
       "columns" :   "*" ,
       "filter" :   { } ,
       "validate_input" :   {
         "type" :   "http" ,
         "definition" :   {
           "forward_client_headers" :   true ,
           "headers" :   [ ] ,
           "timeout" :   5 ,
           "url" :   "http://www.somedomain.com/validateCustomerMutation"
         }
       }
     }
   }
}
```

If we try to insert a customer with an invalid email, we will get a `validation-failed` error:

 **Example 2:** Validate that an `article` can be inserted only if `title` is not empty.

Suppose, we have the following table in our schema:

`article  ( id uuid ,  title  text ,  content  text ,  author_id uuid )`

Now, we can create a role `user` and add an insert validation rule as follows:

- Console
- CLI
- API


Image: [ validation using permission: title cannot be empty ](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAq8AAAGXCAMAAACqfknyAAADAFBMVEX////Y2NhNTU1VVVXMzMz09PTq6+r19fXj4+Pe3t54gJX///H///r6///0/////+u47//m/////sju/////+G9e1Piq29kltTm9fWMWnfJ/P//5cLn6Oj//+iy5//a///P0NC6urv//dbbnGVNTlvw8PDVlGNrnttNTVJnZWZ/ptr/79Cc2/6RgZbU1NTT/P99VH5ZisfHyMjKi1iBgoH437SOz/6Ex///3qADAwNdXV3/87yyc035w4JTdbKzeVhOX5FpZZms4f53g56Sxu/9zIwgICBvq+PBwcJ8vfL/5q//+eOrbl2Ef5bB6P5mTk2GxPf08tTE8f//88R9n9Gcz/abZlNNTnJNTmW76/ZZTk15g7WZmZvosnP/2Jd8fXtYgL2FVk6urKr5+PiGsuFkXlyzkJVwbnCFWXN5l8laeLR2XIp4VlNRbaGBl7WOX2ZjWFH/8drvyJEwMDCwkKb407b09eP577hRV4BvU1Kys7HetoSMkqTE9fZibqKBbl7vyKzZyEXwu3vk9v/b+v/R9fTO8P9qbGuV1P9cXWpwX1itnZ+t1fSDhZaSq84WFhbZ8//01Z7Qo5i7k3JnkMYNixD11bFfktBgZnZTWWXKjmSOkIpdbYyRob9nepiig5V+jaKZbmiQXk/+/PtjhcD19cN2jLCPvOi5lJe3gGhWZXsLp6PImnuNdWR1j75fWFxlX4r88PCdyOlOWnLcr594gaj415XCnJ0GlGspjA9dZWqfutmggmuVi7cSkThngbCKk8TjvaFjcYLYvq98teVJSUn4+f+uxtiUg3QHmYLezrpIyM+XrLG9siKLngl8ZVppV3xWWl2EvejL7d+loaioqMHu28jV5fKdh7E+jgyG1f70+e2hb15QjQ258OnHqqv50NroXH/EuznLsZd4tu7a+9KjbH3x3nLC2+9TzugSk1l2seP17p8Onohn2PCgpgrD6MIosrSqlYCQb43L133sdpSawb1plg2nrSyT39KGu7v04+GxwZWZ34mJrUT4+vucgRmSAAAfAklEQVR42uydAUwU19r3H8d+1e7O7rIsQgsFBFZZEIpK9RJERMAooEAXEC6CqkIRKwCmpipcMUBREQytRgUBkVosRNGiaqJtrGrUGBO11drcNtck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)

You can add roles and permissions in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  article
   insert_permissions :
     -   role :  user
       permission :
         check :
           title :
             _ne :   ''
```

Apply the Metadata by running:

`hasura metadata apply`

You can add an insert permission rule by using the[ pg_create_insert_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#metadata-pg-create-insert-permission)metadata
API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_insert_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "article" ,
     "role" :   "user" ,
     "permission" :   {
       "check" :   {
         "title" :   {
           "_ne" :   ""
         }
       }
     }
   }
}
```

If we try to insert an article with `title = ""` , we will get a `permission-error` :

 **Example 3:** Validate that an `article` can be inserted only if its `author` is active.

Suppose, we have 2 tables:

```
author  ( id uuid ,  name  text ,  is_active  boolean )
article  ( id uuid ,  author_id uuid ,  content  text )
```

Also, suppose there is an[ object relationship ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/#pg-graphql-relationships) `article.author` defined as:

`article . author_id  - >  author . id`

Now, we can create a role `user` and add an insert validation rule as follows:

- Console
- CLI
- API


Image: [ validation using permissions: author should be active ](https://hasura.io/docs/assets/images/validation-author-isactive-a204a8402ed6067bebe568936a9c128e.png)

You can add roles and permissions in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  article
   insert_permissions :
     -   role :  user
       permission :
         check :
           author :
             is_active :
               _eq :   true
```

Apply the Metadata by running:

`hasura metadata apply`

You can add an insert permission rule by using the[ pg_create_insert_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/#metadata-pg-create-insert-permission)metadata
API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_insert_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "article" ,
     "role" :   "user" ,
     "permission" :   {
       "check" :   {
         "author" :   {
           "is_active" :   true
         }
       }
     }
   }
}
```

If we try to insert an article for an author for whom `is_active = false` , we will receive a `permission-error` :

Note

Permissions are scoped to a user's role. So, if a validation check needs to be global then you will have to define it
for all roles which have insert/update permissions.

A few features on the roadmap should simplify this experience in the future.

## Using Hasura Actions​

If the validation requires complex custom business logic and/or needs information from external sources, you can use[ Actions ](https://hasura.io/docs/latest/actions/overview/)to perform your validation.

 **Example:** Check with an external service that an author's name is not deny-listed before inserting them.

Let's assume we have an external service that stores and manages deny-listed authors. Before inserting an author we need
to check with this service if they are deny-listed or not.

The validation process looks as follows:

Image: [ validation using actions: article not deny-listed ](https://hasura.io/docs/assets/images/diagram-actions-data-validation-c4be347899285b6a95c7bd4ec184b5bf.png)

Actions allow us to define[ custom types ](https://hasura.io/docs/latest/actions/types/index/)in our GraphQL schema.

We can[ create a new action ](https://hasura.io/docs/latest/actions/create/)called `InsertAuthor` that takes an `author` object with type `AuthorInput` as input and returns an object of type `AuthorOutput` .

```
type   Mutation   {
   InsertAuthor ( author :   AuthorInput ! ) :   AuthorOutput
}
input   AuthorInput   {
   name :   String !
   rating :   Int !
   is_active :   Boolean !
}
type   AuthorOutput   {
   id :   Int !
}
```

The business logic of an action - in our case the author validation - happens in the[ action handler ](https://hasura.io/docs/latest/actions/action-handlers/)which is an HTTP webhook which contains the code to call the external
service.

The following is a sample code that could be added to the event handler to implement the data validation:

```
function   getDenylistedAuthorsFromApi ( )   {
   // make external api call & return deny-listed authors list
}
function   insertAuthorViaHasura ( )   {
   // run insert_author mutation & return response
}
const  denylistedAuthors  =   getDenylistedAuthorsFromApi ( ) ;
if   ( denylistedAuthors . includes ( author . name ) )   {
   return  res . status ( 400 ) . json ( {   message :   'Author is deny-listed'   } ) ;
}   else   {
   const  insertAuthorResponse  =   insertAuthorViaHasura ( ) ;
   return  res . json ( insertAuthorResponse ) ;
}
```

When we now insert an author, our action handler will be called and it will check if the author is deny-listed. If it's
not, the author will be inserted and the `id` will be returned. If the author is deny-listed, we get the following error
message:

Note

For actual examples of data validations with actions, refer to the[ actions examples repo ](https://github.com/hasura/hasura-actions-examples/tree/master/data-validations).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/data-validations/#pg-data-validations-check-constraints/#introduction)
- [ Using Postgres check constraints ](https://hasura.io/docs/latest/schema/postgres/data-validations/#pg-data-validations-check-constraints/#pg-data-validations-check-constraints)
- [ Using Postgres triggers ](https://hasura.io/docs/latest/schema/postgres/data-validations/#pg-data-validations-check-constraints/#pg-data-validations-pg-triggers)
- [ Using Hasura permissions ](https://hasura.io/docs/latest/schema/postgres/data-validations/#pg-data-validations-check-constraints/#using-hasura-permissions)
- [ Using Hasura Actions ](https://hasura.io/docs/latest/schema/postgres/data-validations/#pg-data-validations-check-constraints/#using-hasura-actions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)