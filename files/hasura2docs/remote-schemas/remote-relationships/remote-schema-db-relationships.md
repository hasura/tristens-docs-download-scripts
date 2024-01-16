# Remote Schema to Database Relationships

## Introduction​

Remote Schema to database relationships extend the concept of joining data across tables, to joining across tables and
remote GraphQL sources. Once you create relationships between types from your database and types created from the remote
schema, you can then "join" them by running GraphQL queries.

Because Hasura is meant to be a GraphQL server that you can expose directly to your apps, Hasura also handles security
and authorization while providing remote joins.

Supported from

Relationships from Remote Schema to database are supported from versions `v2.6.0` and above.

## Create Remote Schema relationships​

### Step 1: Add a Remote Schema and a database​

Add a Remote Schema and a database as described[ here ](https://hasura.io/docs/latest/remote-schemas/adding-schema/)and[ here ](https://hasura.io/docs/latest/databases/overview/), if not already added.

### Step 2: Define and create the relationship​

The following fields can be defined for a Remote Schema relationship:

- **Name** : Define a name for the relationship.
- **Remote Schema** : Select a Remote Schema among all the ones you've created.
- **Configuration** : Set up the join configuration, to inject values as input arguments of the Remote Schema field.
    - **From column** : Input injected from table column values.


For example, let's assume that our database has a table `user(id integer, name text)` and we've added a Remote Schema `order-remote-schema` which is another GraphQL API. Now we want to create a relationship between the `order` field of
the Remote Schema and the `user` table of the source database.

1. We name the relationship `user` .
2. We select the source type `Order` of the Remote Schema that we'd like to join.
3. We select `pg1` as the reference database, `public` as the reference schema and `user` as the reference table.
4. We select `user_id` as the source field and `id` as the reference column.


- Console
- CLI
- API


- Head to the `Remote Schema -> [remote-schema-name] -> Relationships` tab.
- Click the `Add a new relationship` button.
- Define the relationship and hit `Add Relationship` .


Head to the `Remote Schema -> [remote-schema-name] -> Relationships` tab.

Click the `Add a new relationship` button.

Image: [ Opening the remote relationship section ](https://hasura.io/docs/assets/images/create-relationship-from-remote-schema-0a8cc99c71cb4c0faf38e6659b224b5e.png)

Define the relationship and hit `Add Relationship` .

Image: [ Defining the relationship ](https://hasura.io/docs/assets/images/configure-relationship-rs-to-db-34e0ab48e76817064e3c97bb980c41a0.png)

Update the `remote_schemas.yaml` file in the `metadata` directory:

```
-   name :  order - remote - schema
   definition :
     url :  https : //remote - schema - endpoint.com
   remote_relationships :
     -   relationships :
         -   name :  user
           definition :
             to_source :
               relationship_type :  object
               source :  pg1
               table :
                 schema :  public
                 name :  user
               field_mapping :
                 user_id :  id
```

Apply the Metadata by running:

`hasura metadata apply`

You can add a Remote Schema relationship by using the[ create_remote_schema_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-create-remote-schema-remote-relationship)Metadata API and update it by using the[ update_remote_schema_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-update-remote-schema-remote-relationship)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "create_remote_schema_remote_relationship" ,
   "args" :   {
     "name" :   "user" ,
     "remote_schema" :   "order-remote-schema" ,
     "type_name" :   "Order" ,
     "definition" :   {
       "to_source" :   {
         "relationship_type" :   "object" ,
         "source" :   "pg1" ,
         "table" :   {   "name" :   "user" ,   "schema" :   "public"   } ,
         "field_mapping" :   {
           "user_id" :   "id"
         }
       }
     }
   }
}
```

### Step 3: Explore with GraphiQL​

In the `API` tab, test out your Remote Schema relationship.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-db-relationships/#introduction)
- [ Create Remote Schema relationships ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-db-relationships/#create-remote-schema-relationships)
    - [ Step 1: Add a Remote Schema and a database ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-db-relationships/#step-1-add-a-remote-schema-and-a-database)

- [ Step 2: Define and create the relationship ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-db-relationships/#step-2-define-and-create-the-relationship)

- [ Step 3: Explore with GraphiQL ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-db-relationships/#step-3-explore-with-graphiql)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)