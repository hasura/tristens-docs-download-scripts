# Postgres: Database to Remote Schema Relationships

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

Remote Schema relationships from Postgres are supported from versions `v1.3.0` and above.

## Create Remote Schema relationships​

### Step 1: Add a Remote Schema and a database​

Add a Remote Schema and a database as described[ here ](https://hasura.io/docs/latest/remote-schemas/adding-schema/)and[ here ](https://hasura.io/docs/latest/databases/quickstart/), if not already added.

### Step 2: Define and create the relationship​

The following fields can be defined for a Remote Schema relationship:

- **Name** : Define a name for the relationship.
- **Remote Schema** : Select a Remote Schema among all the ones you've created.
- **Configuration** : Set up the join configuration, to inject values as input arguments of the Remote Schema field.
    - **From column** : Input injected from table column values.

- **From static value** : Input injected from a static value of your choice.


For example, let's assume that our database has a table `order(id int, user_id int)` and we've added a Remote Schema `user-remote-schema` .

1. We name the relationship `user` .
2. We select the `user-remote-schema` that we've added.
3. We set up the config to join the `id` input argument of our Remote Schema field to the `user_id` column of this
table (in this case, the `order` table).


- Console
- CLI
- API


- Head to the `Data -> [table-name] -> Relationships` tab.
- Click the `Add Relationship` button to open the widget.
- Search for the remote schema by name in the `To Reference` input box.
- Once selected, it will open the details section below to fill in the rest of the relationship definition.
- Define the relationship details and hit `Create Relationship` .


Head to the `Data -> [table-name] -> Relationships` tab.

Click the `Add Relationship` button to open the widget.

Search for the remote schema by name in the `To Reference` input box.

Once selected, it will open the details section below to fill in the rest of the relationship definition.

Define the relationship details and hit `Create Relationship` .

Image: [ Opening the remote relationship section ](https://hasura.io/docs/assets/images/add-remote-schema-rel-5e93a9814ae93a952ca3f3a9b1d4697d.png)

Update the `databases > [database-name] > tables > [table-name].yaml` file in the `metadata` directory:

```
-   table :
     schema :  public
     name :  order
   remote_relationships :
     -   name :  user
       definition :
         remote_field :
           user :
             arguments :
               id :  $user_id
         hasura_fields :
           -  user_id
         remote_schema :  user - remote - schema
```

Apply the Metadata by running:

`hasura metadata apply`

You can add a Remote Schema relationship by using the[ pg_create_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-pg-create-remote-relationship)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_remote_relationship" ,
   "args" :   {
     "name" :   "user" ,
     "source" :   "pg1" ,
     "table" :   {   "name" :   "order" ,   "schema" :   "public"   } ,
     "hasura_fields" :   [ "user_id" ] ,
     "remote_schema" :   "user-remote-schema" ,
     "remote_field" :   {
       "user" :   {
         "arguments" :   {
           "id" :   "$user_id"
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

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/#introduction)
- [ Create Remote Schema relationships ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/#create-remote-schema-relationships)
    - [ Step 1: Add a Remote Schema and a database ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/#step-1-add-a-remote-schema-and-a-database)

- [ Step 2: Define and create the relationship ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/#step-2-define-and-create-the-relationship)

- [ Step 3: Explore with GraphiQL ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/#step-3-explore-with-graphiql)
- [ Remote Schema relationship permissions ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/#pg-remote-schema-relationship-permissions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)