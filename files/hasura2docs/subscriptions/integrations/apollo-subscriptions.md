# Setting up GraphQL Subscriptions Using Apollo Client for React

## Setup​

This guide demonstrates how to set up GraphQL subscriptions using Apollo Client for React applications. It assumes you
already have a basic Apollo Client setup according to the[ Apollo docs ](https://www.apollographql.com/docs/react/get-started/)and now want to enable subscriptions.

## Prerequisites​

[ Basic Apollo Client setup ](https://www.apollographql.com/docs/react/get-started/)

## Installation​

1. Install the necessary packages:


`npm   install  --save @apollo/client graphql-ws`

1. Import the required modules in the file where you initialized your client (usually your `App.js` file):


```
import   {   ApolloClient ,   HttpLink ,   InMemoryCache ,  split  }   from   '@apollo/client' ;
import   {   GraphQLWsLink   }   from   "@apollo/client/link/subscriptions" ;
import   {  createClient  }   from   "graphql-ws" ;
import   {  getMainDefinition  }   from   '@apollo/client/utilities' ;
```

1. Initialize the client with the following configuration:


```
const  httpLink  =   new   HttpLink ( {
   uri :   'https://<YOUR-HASURA-INSTANCE-URL>/v1/graphql'
} ) ;
const  wsLink  =   new   GraphQLWsLink ( createClient ( {
   url :   'wss://<YOUR-HASURA-INSTANCE-URL>/v1/graphql' ,
} ) ) ;
const  splitLink  =   split (
   ( {  query  } )   =>   {
     const  definition  =   getMainDefinition ( query ) ;
     return   (
      definition . kind   ===   'OperationDefinition'   &&
      definition . operation   ===   'subscription'
     ) ;
   } ,
  wsLink ,
  httpLink
) ;
const  client  =   new   ApolloClient ( {
   link :  splitLink ,
   cache :   new   InMemoryCache ( ) ,
} ) ;
```

This setup allows you to use queries and mutations over the defined `httpLink` and subscriptions over the `wsLink` through
the split function provided by the Apollo library. The split function takes a test function and two different links to
determine which link should be used to send the request.

This split link is then passed to the Apollo Client instance, which is then passed to the `ApolloProvider` component
as per the basic Apollo setup.

## Creating subscriptions​

Switching to a subscription in Apollo Client is as simple as changing the `useQuery` to `useSubscription` hook and
switching the keyword in the graphql query from `query` to `subscription` .

For example, change the following query:

```
query   GetProducts   {
   products   {
     id
     name
     price
   }
}
```

to this subscription:

```
subscription   GetProducts   {
   products   {
     id
     name
     price
   }
}
```

Usage with Next.js

When using this setup with Next.js, you will need to make sure that the `wsLink` is only initialized on the
client and not while rendering on the server. To achieve this, you can test that you're in the browser with `typeof
window !== 'undefined'` 

The `wsLink` can be created as follows:

```
const  wsLink  =   typeof   window   !==   "undefined"   ?   new   GraphQLWsLink ( createClient ( {
   url :   'ws://vast-fawn-54.hasura.app/v1/graphql' ,
} ) )   :   null ;
```

and the `splitLink` with a ternary as follows:

```
const  link  =   typeof   window   !==   "undefined"   &&  wsLink  !=   null
?   split (
   ( {  query  } )   =>   {
     const  definition  =   getMainDefinition ( query ) ;
     return   (
      definition . kind   ===   'OperationDefinition'   &&
      definition . operation   ===   'subscription'
     ) ;
   } ,
  wsLink ,
  httpLink
)   :  httpLink ;
```

## Further Reading​

[ Subscriptions in Hasura ](https://hasura.io/docs/latest/subscriptions/overview/).

### What did you think of this doc?

- [ Setup ](https://hasura.io/docs/latest/subscriptions/integrations/apollo-subscriptions/#setup)
- [ Prerequisites ](https://hasura.io/docs/latest/subscriptions/integrations/apollo-subscriptions/#prerequisites)
- [ Installation ](https://hasura.io/docs/latest/subscriptions/integrations/apollo-subscriptions/#installation)
- [ Creating subscriptions ](https://hasura.io/docs/latest/subscriptions/integrations/apollo-subscriptions/#creating-subscriptions)
- [ Further Reading ](https://hasura.io/docs/latest/subscriptions/integrations/apollo-subscriptions/#further-reading)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)