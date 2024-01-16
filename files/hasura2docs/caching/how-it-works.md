# How Caching Works

## Introduction​

Hasura Caching is a type of response caching that helps you store results of a given query in order to serve it more
quickly to your users. Hasura will cache the response of a given query under a cache key, and when another request
comes in which computes to the same cache key then it will deliver the cached result, without needing to query the
underlying data source. We explain how the cache key is computed in the[ next section ](https://hasura.io/docs/latest/caching/how-it-works/#how-is-the-cache-key-computed).

## How is the cache key computed?​

If the `@cached` directive is used in a GraphQL operation, Hasura computes a cache key. This is then used to look up and
store values in the cache.

The cache key is a hash of:

- the GraphQL query
- the GraphQL operation name
- the GraphQL variables of the query
- the[ role and session variables ](https://hasura.io/docs/latest/auth/authorization/roles-variables/)used in the permissions of the query (not
necessarily all of the session variables)
- request headers in case of[ Remote Schemas ](https://hasura.io/docs/latest/remote-schemas/overview/)or[ Actions ](https://hasura.io/docs/latest/actions/overview/)when `forward_client_headers` is `true`


If the computed cache key is found in the cache, then there is a cache hit.

This means that a cached result will not be delivered if:

- the session variables needed in the permissions of the query differ, even if the GraphQL query, variables, operation
name and everything else is the same
- the GraphQL variables differ, even if the GraphQL query is the same
- the operation name is different, even if the GraphQL query is the same
- the GraphQL query differs in one or more fields


TTL matters

Note that the cache hit also depends on the TTL and not just cache key. See[ below ](https://hasura.io/docs/latest/caching/how-it-works/#cache-invalidation)to know more
about cache TTL.

### GraphQL query​

This includes the entire GraphQL query text. Any difference in the GraphQL query text is considered a different query. **Only whitespace is ignored.** 

For example, all the following queries are considered **different** :

```
query   MyCachedQuery   @cached   {
   users   {
     id
     name
   }
}
```

```
query   MyCachedQuery   @cached   {
   users   {
     name
     id
   }
}
```

```
query   MyCachedQuery   @cached   {
   users   {
     id
     name
     created_at
   }
}
```

If the order of objects inside an input argument are changed, even then it is considered a **different** query:

```
query   MyCachedQuery   @cached   {
   profile ( where :   {   _and :   [ {   id :   {   _gt :   1   }   } ,   {   name :   {   _ilike :   "%x%"   }   } ]   } )   {
     id
     name
   }
}
```

```
query   MyCachedQuery   @cached   {
   profile ( where :   {   _and :   [ {   name :   {   _ilike :   "%x%"   }   } ,   {   id :   {   _gt :   1   }   } ]   } )   {
     id
     name
   }
}
```

Only whitespace is ignored, so the following queries are considered the **same** :

```
query   MyCachedQuery   @cached   {
   users   {
     name
     id
   }
}
```

```
query   MyCachedQuery   @cached   {
   users   {   name   id   }
}
```

### Operation name​

In the following example, the operation name is `MyCachedQuery` 

```
query   MyCachedQuery   @cached   {
   users   {
     id
     name
   }
}
```

If we use the same name, but change the query, then it is considered a **different** query:

```
query   MyCachedQuery   @cached   {
   users   {
     id
   }
}
```

### GraphQL variables​

The following example shows variables declared and used called `minDate` and `maxDate` . Usually, when executing the
operation, one would pass the actual value of these variables.

If these variable **values** differs across queries, then they are deemed **different** :

```
query   getNewlyJoinedUsers ( $minDate :   timestamptz ! ,   $maxDate :   timestamptz ! )   @cached   {
   users ( where :   {   _and :   [ {   created_at :   {   _gt :   $minDate   }   } ,   {   created_at :   {   _lt :   $maxDate   }   } ]   } )   {
     id
     name
   }
}
```

### Role and session variables​

Hasura resolves[ session variables ](https://hasura.io/docs/latest/auth/authorization/roles-variables/)via the[ authentication ](https://hasura.io/docs/latest/auth/authentication/index/)process. The role and (a subset of) session variables are used to
compute the cache key. A session variable will be part of the the cache key only if it is needed by the permission
rules for the query. Sessions variables which are not required in the execution plan for a query are not included in
the cache key. Therefore, the same cached result can be returned for requests where the session variables only
differ where they are not required in the query execution plan.

For example, if a JWT resolves to say `x-hasura-user-id` and `x-hasura-org-id` session variables, but the query only
uses the `x-hasura-user-id` in the permissions, then only the role and `x-hasura-user-id` would be used to compute the
cache key.

Public data and session variables

Public data usually do not have any permission rules and hence are easily reused for all requests (irrespective of user).
This data can be used in landing pages, item listings, news feeds, etc.

### Request headers​

Request headers (ignoring `x-request-id` header) are added to the cache key computation, when executing Remote Schema
or Action queries, if they have `forward_client_headers` set to `true` .

## Cache Invalidation​

Cache invalidation in Hasura is based on TTLs. Hasura doesn't support any other "automatic" way to invalidate cache
(like on specific mutations). However, there are[ API endpoints ](https://hasura.io/docs/latest/caching/caching-config/#clearing-items-from-the-cache)to clear the cache manually.

The default TTL is 60 seconds. This can be increased via the[ TTL argument ](https://hasura.io/docs/latest/caching/caching-config/#controlling-cache-lifetime)in the cached directive.

## Rate Limiting​

Cache writes are rate limited, with a rate depending on your plan. The rate limit is based on a leaky bucket algorithm.
If you exceed the rate limit, the HTTP response will indicate this with a warning header:

` Warning: 199 - cache-store-capacity-exceeded`

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/caching/how-it-works/#introduction)
- [ How is the cache key computed? ](https://hasura.io/docs/latest/caching/how-it-works/#how-is-the-cache-key-computed)
    - [ GraphQL query ](https://hasura.io/docs/latest/caching/how-it-works/#graphql-query)

- [ Operation name ](https://hasura.io/docs/latest/caching/how-it-works/#operation-name)

- [ GraphQL variables ](https://hasura.io/docs/latest/caching/how-it-works/#graphql-variables)

- [ Role and session variables ](https://hasura.io/docs/latest/caching/how-it-works/#role-and-session-variables)

- [ Request headers ](https://hasura.io/docs/latest/caching/how-it-works/#request-headers)
- [ Cache Invalidation ](https://hasura.io/docs/latest/caching/how-it-works/#cache-invalidation)
- [ Rate Limiting ](https://hasura.io/docs/latest/caching/how-it-works/#rate-limiting)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)