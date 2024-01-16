# Action Relationships

## Introduction​

Actions are a way to extend your GraphQL schema with custom queries or mutations which call a REST endpoint. It is a
typical case that an Action's response is actually related to existing objects in the schema and as such, should be
connected with the rest of the graph.

For example, a custom `insertAuthor` action will be related to the `author` object in the schema. Hence, we would want
to be able to get information about the `author` from the graph as a response of the `insertAuthor` mutation.

## Support for Action relationships​

Below, you can find information about the different types of relationship patterns that are supported for Actions.

| Relationship Type | Description |
|---|---|
| Action to Database |  **Joins are supported  from  Actions  to  tables in Postgres databases.** However, Action to database joins are not currently supported for other databases. |
| Action to Action | Actions can be joined to each other by using a Hasura instance as a federation gateway, or "parent" supergraph. You can find more information about this pattern[ here ](https://hasura.io/docs/latest/actions/action-relationships/#action-to-action-relationships). |
| Action to Remote Schema | An Action cannot be joined to a Remote Schema. |


## Using an Action's output types in relationships​

Actions can be connected to the rest of the graph by setting up relationships on its return output type.

This allows complex responses to be returned as an Action's response by traversing the graph via the output type's
relationships.

 **For example** , given the action:

```
type   Mutation   {
   updateAuthor ( id :   Int ! ,   name :   String ! ) :   UpdateAuthorOutput
}
type   UpdateAuthorOutput   {
   author_id :   Int !
}
```

We can create an object relationship called `updatedAuthor` between the `UpdateAuthorOutput` object type and the `author` table using the `UpdateAuthorOutput.author_id` and `author.id` fields.

The object type will now be modified as:

```
type   UpdateAuthorOutput   {
   author_id :   Int !
   updatedAuthor :   author
}
```

Now we can make a mutation request with a complex response such as:

```
mutation   updateAuthorAndGetArticles ( $id :   Int ,   $name :   String )   {
   updateAuthor ( id :   $id ,   name :   $name )   {
     author_id
     updatedAuthor   {
       id
       name
       articles   {
         id
         title
       }
     }
   }
}
```

See more details at[ custom object type relationships ](https://hasura.io/docs/latest/actions/types/index/)

### Creating relationships for custom object types​

You can create relationships for custom output types by:

- Console
- CLI
- API


Head to the `Actions -> [action-name] -> Relationships` tab in the Console for the Action returning the output type.

Set the output type relationship as shown below:

Image: [ Console action relationship ](https://hasura.io/docs/assets/images/actions-relationship-8bd56e8063579b006fe3502c96f019a8.png)

Hit `Save` to create the relationship.

Go to `metadata/actions.yaml` in the Hasura Project directory.

Update the definition of the `UpdateAuthorOutput` object type as:

```
-  custom_types
   -  objects
     -   name :  UpdateAuthorOutput
       relationships :
       -   name :  updatedAuthor
         type :  object
         remote_table :
           schema :  public
           name :  author
         field_mapping :
           author_id :  id
```

Save the changes and run `hasura metadata apply` to create the relationship.

Action relationships can be added while defining custom types via the[ set_custom_types ](https://hasura.io/docs/latest/api-reference/metadata-api/custom-types/#metadata-set-custom-types)Metadata API:

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
         "name" :   "UpdateAuthorOutput" ,
         "fields" :   [
           {
             "name" :   "author_id" ,
             "type" :   "Int!"
           }
         ] ,
         "relationships" :   [
           {
             "name" :   "updatedAuthor" ,
             "type" :   "object" ,
             "remote_table" :   "author" ,
             "field_mapping" :   {
               "author_id" :   "id"
             }
           }
         ]
       }
     ]
   }
}
```

## Action to Action relationships​

Hasura supports creating relationships between data originating from different REST APIs which have been added as
Actions by using a Hasura instance as a federation gateway, or "parent" supergraph.

Image: [ Join Actions to Actions using self-referential Remote Schemas ](https://hasura.io/docs/assets/images/data-federation_action-to-action-joins-4001d50679068c6cdfe820ac2b69c40a.png)

To achieve this we can add a "child" Hasura instance to a "parent" or "gateway" Hasura instance as a Remote Schema. This
allows relationships to be created between types from two different Actions in the child instance by creating a[ Remote Schema to Remote Schema ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/remote-schema-relationships/)relationship on
the same Remote Schema.

Remote Schema Action to Action workaround

Currently, this method of adding a child instance as a Remote Schema to achieve Action to Action relationships is a
viable and effective workaround. In the future we will be adding a more native method of creating Action to Action
relationships without utilizing Remote Schemas.

Additional Resources

Introduction to Hasura Actions -[ View Recording ](https://hasura.io/events/webinar/hasura-actions/?pg=docs&plcmt=body&cta=view-recording&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/actions/action-relationships/#introduction)
- [ Support for Action relationships ](https://hasura.io/docs/latest/actions/action-relationships/#support-for-action-relationships)
- [ Using an Action's output types in relationships ](https://hasura.io/docs/latest/actions/action-relationships/#using-an-actions-output-types-in-relationships)
    - [ Creating relationships for custom object types ](https://hasura.io/docs/latest/actions/action-relationships/#creating-relationships-for-custom-object-types)
- [ Action to Action relationships ](https://hasura.io/docs/latest/actions/action-relationships/#action-to-action-relationships)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)