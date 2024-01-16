# BigQuery: Data Validations

## Introduction​

Many times, we need to perform validations of input data before selecting, inserting or updating objects.

BigQuery does not natively support constraints, primary or foreign keys.

However, if you would like the validation logic to be at the GraphQL API layer, Hasura permissions can be used to add
your validation.

These solutions are explained in some more detail below.

## Using Hasura permissions​

If the validation logic can be expressed **declaratively** using static values and data from the database, then you can
use[ row level permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/)to perform the validations.
(Read more about[ Authorization ](https://hasura.io/docs/latest/auth/authorization/index/)).

 **Example 1:** Validate that the `editor` role can only select `article` s with empty titles.

Suppose, we have the following tables in our schema:

```
authors  ( id  int ,  name  text )
articles  ( id  int ,  title  text ,  author_id  int ,  body  text )
```

Now, we can create a role `editor` and add a select validation rule as follows:

- Console
- CLI
- API


You can add roles and permissions in the `tables.yaml` file inside the `metadata` directory:

```
table :
   dataset :  bigquery
   name :  articles
select_permissions :
   -   role :  editor
     permission :
       columns :   '*'
       filter :
         title :
           _eq :   ''
```

Apply the Metadata by running:

`hasura metadata apply`

You can add an select permission rule by using the[ bigquery_create_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_create_select_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   {
       "name" :   "articles" ,
       "dataset" :   "bigquery"
     } ,
     "role" :   "editor" ,
     "permission" :   {
       "filter" :   {
         "title" :   {
           "_eq" :   ""
         }
       }
     }
   }
}
```

If we set the `X-Hasura-Role` to `editor` and try to select all articles, only those with empty string titles will be
returned:

 **Example 2:** Validate that `author` roles can only select an `article` if the `author_id` matches `X-Hasura-User-Id` 

Suppose, we have 2 tables:

```
authors  ( id  int ,  name  text )
articles  ( id  int ,  title  text ,  author_id  int ,  body  text )
```

Also, suppose there is an[ object relationship ](https://hasura.io/docs/latest/schema/bigquery/table-relationships/index/) `articles.author` defined
as:

`articles . author_id  - >  authors . id`

Now, we can create a role `author` and add an select validation rule as follows:

- Console
- CLI
- API


You can add roles and permissions in the `tables.yaml` file inside the `metadata` directory:

```
table :
   dataset :  bigquery
   name :  articles
select_permissions :
   -   role :  author
     permission :
       columns :   '*'
       filter :
         author_id :
           _eq :  X - Hasura - User - Id
```

Apply the Metadata by running:

`hasura metadata apply`

You can add a select permission rule by using the[ bigquery_create_select_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_create_select_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   {
       "name" :   "articles" ,
       "dataset" :   "bigquery"
     } ,
     "role" :   "author" ,
     "permission" :   {
       "filter" :   {
         "author_id" :   {
           "_eq" :   "X-Hasura-User-Id"
         }
       }
     }
   }
}
```

If we set the `X-Hasura-Role` and `X-Hasura-User-Id` headers, then try to select all articles, only those where the `author_id` matches the current `X-Hasura-User-Id` will be returned:

Note

Permissions are scoped to a user's role. So, if a validation check needs to be global then you will have to define it
for all roles which have insert/update permissions.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/bigquery/data-validations/#introduction)
- [ Using Hasura permissions ](https://hasura.io/docs/latest/schema/bigquery/data-validations/#using-hasura-permissions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)