# Debugging Actions

## Introduction​

While you're developing Actions for your application, to debug faster
you may want to see the exact details of the webhook call for the Action
as well.

To do so, start the server in[ debugging mode ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/config-examples/#dev-mode). In the case
of errors, the GraphQL response will contain debugging information of
the webhook calls in the `extensions.internal` field.

If you are using action transforms, then you will also see the `transformed_request` inside the `request` field.

 **For example** :

Additional Resources

Introduction to Hasura Actions -[ View
Recording ](https://hasura.io/events/webinar/hasura-actions/?pg=docs&plcmt=body&cta=view-recording&tech=).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/actions/debugging/#introduction)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)