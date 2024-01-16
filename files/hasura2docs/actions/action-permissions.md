# Actions Permissions

## Introduction​

As with the other fields in the GraphQL schema, users need to be given access to an action.

## Set action permissions​

- Console
- CLI
- API


Head to the `Actions -> [action-name] -> Permissions` tab in the Console.

Image: [ Console action permission ](https://hasura.io/docs/assets/images/actions-permissions-48cc890d2d2c06aab254b0126ea25855.png)

Hit `Save` to give the role permission to access the action.

Go to `metadata/actions.yaml` in the Hasura Project directory.

Update the definition of the `insertAuthor` action as:

```
-  actions
   -   name :  insertAuthor
     definition :
       kind :  synchronous
       handler :   '{{ACTIONS_BASE_URL}}/insertAuthor'
     permissions :
     -   role :  user
     -   role :  publisher
```

Save the changes and run `hasura metadata apply` to set the permissions.

Action permissions can be set by using the[ create_action_permission ](https://hasura.io/docs/latest/api-reference/metadata-api/actions/#metadata-create-action-permission)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "create_action_permission" ,
   "args" :   {
     "action" :   "insertAuthor" ,
     "role" :   "user"
   }
}
```

Additional Resources

Introduction to Hasura Actions -[ View Recording ](https://hasura.io/events/webinar/hasura-actions/?pg=docs&plcmt=body&cta=view-recording&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/actions/action-permissions/#introduction)
- [ Set action permissions ](https://hasura.io/docs/latest/actions/action-permissions/#set-action-permissions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)