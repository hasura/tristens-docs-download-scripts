# BigQuery: Database to Remote Schema Relationships

## Introduction​

Database to Remote Schema relationships extend the concept of joining data across tables, to joining across tables and
remote GraphQL sources. Once you create relationships between types from your database and types created from remote
schemas, you can then "join" them by running GraphQL queries.

These APIs can be custom GraphQL servers you write, third party SaaS APIs, or even other Hasura instances.

Because Hasura is meant to be a GraphQL server that you can expose directly to your apps, Hasura also handles security
and authorization while providing remote joins.

Note

To see example use cases, check out this[ blog post ](https://hasura.io/blog/remote-joins-a-graphql-api-to-join-database-and-other-data-sources/).

Supported from

Remote Schema relationships from BigQuery are supported from versions `v1.3.0` and above.

## Create Remote Schema relationships​

### Step 1: Add a Remote Schema and a database​

Add a Remote Schema and a database as described[ here ](https://hasura.io/docs/latest/remote-schemas/adding-schema/)and[ here ](https://hasura.io/docs/latest/databases/overview/), if not already added.

### Step 2: Define and create the relationship​

The following fields can be defined for a Remote Schema relationship:

- **Name** : Define a name for the relationship.
- **Remote Schema** : Select a Remote Schema among all the ones you've created.
- **Configuration** : Set up the join configuration, to inject values as input arguments of the Remote Schema field.
    - **From column** : Input injected from table column values.


For example, let's assume that our database has a table `articles(id int, author_id int)` and we've added a remote
schema `author-remote-schema` .

1. We name the relationship `user` .
2. We select the `author-remote-schema` that we've added.
3. We set up the config to join the `id` input argument of our Remote Schema field to the `author_id` column of this
table (in this case, the `articles` table).


- Console
- CLI
- API


- Head to the `Data -> [table-name] -> Relationships` tab.
- Click the `Add a remote relationship` button.
- Define the relationship and hit `Save` .


Head to the `Data -> [table-name] -> Relationships` tab.

Click the `Add a remote relationship` button.

Image: [ Opening the remote relationship section ](https://hasura.io/docs/assets/images/add-remote-schema-relationship-18cebc6e38d6057b83cf07fb2014ed2a.png)

Define the relationship and hit `Save` .

Image: [ Defining the relationship ](https://hasura.io/docs/assets/images/define-remote-schema-relationship-6ef7370713075ebda5a1f9461cc4bbba.png)

Update the `databases > [database-name] > tables > [table-name].yaml` file in the `metadata` directory:

```
-   table :
     dataset :  source
     name :  author
   remote_relationships :
     -   name :  author
       definition :
         remote_field :
           author :
             arguments :
               id :  $id
         hasura_fields :
           -  author_id
         remote_schema :  author - remote - schema
```

Apply the Metadata by running:

`hasura metadata apply`

You can add a Remote Schema relationship by using the[ bigquery_create_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-bigquery-create-remote-relationship)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_create_remote_relationship" ,
   "args" :   {
     "name" :   "articles" ,
     "source" :   "bq-source" ,
     "table" :   {
       "dataset" :   "<source_dataset_name>" ,
       "name" :   "author"
     } ,
     "definition" :   {
       "to_remote_schema" :   {
         "remote_schema" :   "<remote_schema_name>" ,
         "lhs_fields" :   [ "id" ] ,
         "remote_field" :   {
           "articles" :   {
             "arguments" :   {
               "author_id" :   "$id"
             }
           }
         }
       }
     }
   }
}
```

### Step 3: Explore with GraphiQL​

In the `API` tab, test out your Remote Schema relationship.

## Remote Schema relationship permissions​

Remote Schema relationship permissions are derived from the[ Remote Schema permissions ](https://hasura.io/docs/latest/remote-schemas/auth/remote-schema-permissions/)defined for the role. When a remote
relationship permission cannot be derived, the remote relationship field will not be added to the schema for the role.

Some cases in which a remote relationship permission cannot be derived are:

1. There are no Remote Schema permissions defined for the role.
2. The role doesn't have access to the field or types that are used by the remote relationship.


Note

Remote relationship permissions apply only if Remote Schema permissions are enabled in GraphQL Engine.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/bigquery/remote-relationships/remote-schema-relationships/#introduction)
- [ Create Remote Schema relationships ](https://hasura.io/docs/latest/schema/bigquery/remote-relationships/remote-schema-relationships/#create-remote-schema-relationships)
    - [ Step 1: Add a Remote Schema and a database ](https://hasura.io/docs/latest/schema/bigquery/remote-relationships/remote-schema-relationships/#step-1-add-a-remote-schema-and-a-database)

- [ Step 2: Define and create the relationship ](https://hasura.io/docs/latest/schema/bigquery/remote-relationships/remote-schema-relationships/#step-2-define-and-create-the-relationship)

- [ Step 3: Explore with GraphiQL ](https://hasura.io/docs/latest/schema/bigquery/remote-relationships/remote-schema-relationships/#step-3-explore-with-graphiql)
- [ Remote Schema relationship permissions ](https://hasura.io/docs/latest/schema/bigquery/remote-relationships/remote-schema-relationships/#remote-schema-relationship-permissions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)