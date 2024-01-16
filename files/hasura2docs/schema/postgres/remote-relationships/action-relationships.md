# Postgres: Action to Database Relationships

## Introduction​

Action relationships allow you to join data across tables and actions. Once you create relationships between types from
your database and types created from actions, you can then "join" them by running GraphQL queries.

[ Actions ](https://hasura.io/docs/latest/actions/overview/)are a way to extend Hasura’s schema with custom business logic using custom queries and
mutations. The resolvers for these custom fields are written in REST endpoints. They are especially useful for setting
up serverless functions as resolvers.

## Create an action relationship​

### Step 1: Create an action​

Create an action either[ from scratch ](https://hasura.io/docs/latest/actions/create/)or[ derived from an existing mutation ](https://hasura.io/docs/latest/actions/derive/).

### Step 2: Define and create the relationship​

The following values can be defined for an action relationship:

- **Relationship type** : Select a type of relationship.
    - **Object relationship** : For one-to-one relationships.

- **Array relationship** : For one-to-many relationships.
- **Relationship name** : Create a name for the relationship.
- **Reference schema** : Select a reference schema from your database.
- **Reference table** : Select a table from your database.
- **From** : Select a field returned in the action response.
- **To** : Select a column from the reference table to join the field to.


In this example, we're creating a relationship for the `createUser` action. We're creating a relationship called `user` ,
from the `id` field returned in the action response, to the `id` column of the `users` table.

- Console
- CLI
- API


- Head to the `Actions -> [action-name] -> Relationships` tab.
- Click `Add a relationship` .
- In the section opened by the above step, fill out the following fields and hit `Save` .


Head to the `Actions -> [action-name] -> Relationships` tab.

Click `Add a relationship` .

Image: [ Opening the action relationship section ](https://hasura.io/docs/assets/images/add-action-relationship-e87524c0d99898f29f7baebb512c90d5.png)

In the section opened by the above step, fill out the following fields and hit `Save` .

Image: [ Defining the relationship ](https://hasura.io/docs/assets/images/define-action-relationship-c5a3bb608012316d565ffbc8831f4082.png)

You can add an action relationship by adding it to the respective custom type in the `actions.yaml` file inside the `metadata` directory:

```
-  custom_types
   -  objects
     -   name :  UserOutput
       relationships :
       -   remote_table :
           schema :  public
           name :  users
         name :  user
         type :  object
         field_mapping :
           id :  id
```

Apply the Metadata by running:

`hasura metadata apply`

You can create an action relationship when defining custom types via the[ set_custom_types ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-types/#metadata-set-custom-types)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "set_custom_types" ,
   "args" :   {
     "scalars" :   [ ] ,
     "enums" :   [ ] ,
     "input_objects" :   [ ] ,
     "objects" :   [
       {
         "name" :   "UserOutput" ,
         "fields" :   [
           {
             "name" :   "id" ,
             "type" :   "Int!"
           }
         ] ,
         "relationships" :   [
           {
             "name" :   "user" ,
             "type" :   "object" ,
             "remote_table" :   "users" ,
             "field_mapping" :   {
               "id" :   "id"
             }
           }
         ]
       }
     ]
   }
}
```

### Step 3: Explore with GraphiQL​

In the `API` tab, test out your action relationship.

If your table has an existing[ remote relationship ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/), you can also query the
fields from the Remote Schema.

In the[ Remote Schema relationships ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/remote-schema-relationships/)section, we
joined our `users` table with a remote[ Auth0 ](https://auth0.com/)schema. Here, we're able to get the Auth0 profile
data of the user returned from our action.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/action-relationships/#introduction)
- [ Create an action relationship ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/action-relationships/#create-an-action-relationship)
    - [ Step 1: Create an action ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/action-relationships/#step-1-create-an-action)

- [ Step 2: Define and create the relationship ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/action-relationships/#step-2-define-and-create-the-relationship)

- [ Step 3: Explore with GraphiQL ](https://hasura.io/docs/latest/schema/postgres/remote-relationships/action-relationships/#step-3-explore-with-graphiql)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)