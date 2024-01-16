# Quickstart Caching

By utilizing Hasura Engine's caching layer you will significantly improve the performance of queries while at the same
time reduce the load on your data sources. This quickstart guide will walk you through the process of setting up caching
for your GraphQL API.

##### DOCS E-COMMERCE SAMPLE APP

You can use this quickstart with any project, but it pairs well with our docs e-commerce sample app, which you can deploy to Hasura Cloud with one click below. If you've already deployed the sample app,[ access your existing project. ](https://cloud.hasura.io)

Image: [ Deploy to Hasura Cloud ](https://hasura.io/deploy-button.svg)

## Basic Caching​

To try out caching in the Console, simply click the "Cache" button in the GraphiQL panel in the API tab to add the `@cached` directive to your query in the editor. Of course, you can also write this out manually. For this example we
are getting the `id` and `name` of all `products` in the database with:

```
query   MyProducts   @cached   {
   products   {
     id
     name
   }
}
```

You'll be able to see improvements in the response time of the query when the `@cached` directive is added. Note
that the first query with a `@cached` directive will always be a cache miss, but subsequent queries will be cache hits.

## Setting the time-to-live (TTL)​

The `@cached` directive has an optional argument `ttl` which can be used to set the time-to-live (TTL) for the cache.

The TTL is the time for which the cache is valid. After the TTL expires, the cache is invalidated and the next request
will be a cache miss. The TTL is defined in an integer of seconds.

```
query   MyProducts   @cached ( ttl :   120 )   {
   products   {
     id
     name
   }
}
```

Image: [ Setting the time-to-live integer argument for the cached directive ](https://hasura.io/docs/assets/images/caching_ttl_2-21-0-524025b29a8ccb17e7a078dfcd79425d.png)

Default TTL

By default the TTL is set to 60 seconds.

## Forcing a cache refresh​

The `@cached` directive has an optional boolean argument of `refresh` which can be used to force a cache refresh. This
is useful when you want to ensure that the cache is refreshed after a mutation. When this argument is used the query
will take the longer, non-cached time to execute.

```
query   MyProducts   @cached ( refresh :   true )   {
   products   {
     id
     name
   }
}
```

Image: [ Setting the refresh argument for the cached directive ](https://hasura.io/docs/assets/images/caching_force-refresh_2-21-0-27b351653d7d16ef2537080a9611b303.png)

## Recap​

What just happened? Well, you just supercharged your query performance using Hasura caching.

You can now use the `@cached` directive to add caching to your queries, set the length of time they should live for
with the TTL directive and force a cache refresh if you need to. 🎉

[ See the caching config section ](https://hasura.io/docs/latest/caching/caching-config/)for a full description of the caching configuration
options.

### What did you think of this doc?

- [ Basic Caching ](https://hasura.io/docs/latest/caching/quickstart/#basic-caching)
- [ Setting the time-to-live (TTL) ](https://hasura.io/docs/latest/caching/quickstart/#setting-the-time-to-live-ttl)
- [ Forcing a cache refresh ](https://hasura.io/docs/latest/caching/quickstart/#forcing-a-cache-refresh)
- [ Recap ](https://hasura.io/docs/latest/caching/quickstart/#recap)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)