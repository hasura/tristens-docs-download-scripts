# Import Action from OpenAPI Spec

## Introduction​

The most common use case for Actions is to expose an existing API as a GraphQL query. To make this easier, we have added
the ability to import an Action from an[ OpenAPI spec ](https://swagger.io/specification/). OpenAPI is a widely used
standard for describing REST APIs, and many APIs already have an OpenAPI spec available. This feature allows you to
upload an OpenAPI spec, select the operation you want to expose as an Action, and Hasura will automatically prepopulate
the Action definition for you.

## Importing an Action from an OpenAPI spec​

You can import an Action from an OpenAPI spec by clicking the "Import from OpenAPI" button from the Actions page of the
Console, or "Import OpenAPI" in the "Create" dropdown on the left sidebar.

Image: [ Import from OpenAPI buttons ](https://hasura.io/docs/assets/images/import-openapi-f11985e5e6710df089803d0cf2ea662e.png)

You will be redirected to the OpenAPI spec import page.

Either select a file (YAML or JSON) or paste the contents of an OpenAPI spec into the text box:

The specification is then parsed, the operations are listed and the `Base URL` field is automatically populated from the `servers` field.

For each operation, you will either see a "Modify" and "Delete", or "Create" button, depending on whether the operation
is already imported as an Action or not.

Clicking "Modify" will bring you to the Action definition page, where you can further customize the Action definition.
Clicking "Delete" will delete the Action.

Clicking "Create" will create an Action with the operation's details prepopulated.

You can now use this imported Action in your GraphQL API!

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/actions/open-api/#introduction)
- [ Importing an Action from an OpenAPI spec ](https://hasura.io/docs/latest/actions/open-api/#importing-an-action-from-an-openapi-spec)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)