# Use Serverless Functions

## Introduction​

You can use serverless functions along with Event Triggers to design an
async business workflow without having to manage any dedicated
infrastructure.

As Hasura Event Triggers can deliver database events to any webhook,
serverless functions can be perfect candidates for their handlers.

## Why use serverless functions?​

1. Cost effectiveness.
2. No infra management.
3. Async business logic.


## Examples​

You can find a bunch of examples for various serverless cloud providers
in this repo:

[ https://github.com/hasura/graphql-engine/tree/master/community/boilerplates/event-triggers ](https://github.com/hasura/graphql-engine/tree/master/community/boilerplates/event-triggers).

### For example: update related data on a database event​

In this example we make a note taking app. Whenever a user updates their
note, we want to store a revision of that note in a separate table.

You can find the complete example at:

[ https://github.com/hasura/graphql-engine/tree/master/community/boilerplates/event-triggers/aws-lambda/nodejs6/mutation ](https://github.com/hasura/graphql-engine/tree/master/community/boilerplates/event-triggers/aws-lambda/nodejs6/mutation).

Let's consider the following simplified schema for the above:

```
notes  (
  id  INT   PRIMARY   KEY ,
  note  TEXT
)
note_revision  (
  id  INT   PRIMARY   KEY ,
  note  TEXT ,
  note_id  INT   FOREIGN   KEY   REFERENCES  notes ( id ) ,
  update_at  TIMESTAMP   DEFAULT   now ( )
)
```

Whenever an update happens to the `notes` table, we want to insert a row
into the `note_revision` table.

For this we[ set up an Event Trigger ](https://hasura.io/docs/latest/event-triggers/create-trigger/)on `UPDATE` to the `notes` table which calls an AWS Lambda function. The AWS Lambda
function itself uses a GraphQL mutation to insert a new row into the `note_revision` table. As the[ Event Trigger payload ](https://hasura.io/docs/latest/event-triggers/payload/)in case of updates gives us both the old and the new data, we can store
the old note data in our revision table.

Our AWS Lambda code looks like this:

```
// Lambda which gets triggered on insert, and in turns performs a mutation
const  fetch  =   require ( 'node-fetch' ) ;
const  adminSecret  =  process . env . ADMIN_SECRET ;
const  hgeEndpoint  =  process . env . HGE_ENDPOINT ;
const  query  =   `
  mutation updateNoteRevision ($noteId: Int!, $data: String!) {
    insert_note_revision (objects: [
      {
        note_id: $noteId,
        note: $data
      }
    ]) {
      affected_rows
    }
  }
` ;
exports . handler   =   ( event ,  context ,  callback )   =>   {
   let  request ;
   try   {
    request  =   JSON . parse ( event . body ) ;
   }   catch   ( e )   {
     return   callback ( null ,   {   statusCode :   400 ,   body :   'cannot parse hasura event'   } ) ;
   }
   const  response  =   {
     statusCode :   200 ,
     body :   'success' ,
   } ;
   const  qv  =   {   noteId :  request . event . data . old . id ,   data :  request . event . data . old . note   } ;
   fetch ( hgeEndpoint  +   '/v1/graphql' ,   {
     method :   'POST' ,
     body :   JSON . stringify ( {   query :  query ,   variables :  qv  } ) ,
     headers :   {   'Content-Type' :   'application/json' ,   'x-hasura-admin-secret' :  adminSecret  } ,
   } )
     . then ( res   =>  res . json ( ) )
     . then ( json   =>   {
       console . log ( json ) ;
       callback ( null ,  response ) ;
     } ) ;
} ;
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/event-triggers/serverless/#introduction)
- [ Why use serverless functions? ](https://hasura.io/docs/latest/event-triggers/serverless/#why-use-serverless-functions)
- [ Examples ](https://hasura.io/docs/latest/event-triggers/serverless/#examples)
    - [ For example: update related data on a database event ](https://hasura.io/docs/latest/event-triggers/serverless/#for-example-update-related-data-on-a-database-event)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)