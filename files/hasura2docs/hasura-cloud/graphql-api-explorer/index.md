# Hasura GraphQL API Explorer

## TL;DR​

Browse, query, mutate, and subscribe to any GraphQL endpoint with our free, full-featured, in-browser[ GraphiQL app ](https://cloud.hasura.io/public/graphiql)without having to log into Hasura.

## Introduction​

The Hasura GraphQL API Explorer is a free and full-featured GraphiQL UI which is able to query, mutate, or subscribe to
any GraphQL endpoint.

You're able to use this feature to share and test an API endpoint with anyone who has the public URL.

The API Explorer replaces Hasura's legacy GraphQL API exploration tool,[ GraphQL Online ](https://graphiql-online.com/).

## Try out a public GraphQL API​

From the[ API Explorer landing page ](https://cloud.hasura.io/public/graphiql), you can use the quick links on the left
of the page to try out some existing public GraphQL APIs including **SpaceX** , **GitHub** , or **GraphQL Jobs** .

Image: [ API Explorer Landing Page ](https://hasura.io/docs/assets/images/connect-to-existing-api_graphql-api-explorer_v1-3ac3d6d6654c35d030bb95bf75e402fe.png)

Note

For the GitHub GraphQL API you can generate an[ API token for yourself here ](https://github.com/settings/tokens). Once
generated, replace the `<enter your token here>` placeholder in the `Authorization` header with your token to gain
access.

## Connect to any GraphQL API​

You can use the Hasura GraphQL API Explorer to connect to any publicly available GraphQL endpoint. Add your endpoint URL
to the endpoint field and click "Connect to Endpoint".

Image: [ API Explorer Share Link ](https://hasura.io/docs/assets/images/connect-to-api_graphql-api-explorer_v1-ac0b431def82d2fdd2bfa86b8963076f.png)

Once connected you are able to add any headers you may need to provide authentication or other parameters to the
endpoint.

Image: [ API Explorer Share Link ](https://hasura.io/docs/assets/images/add-headers_graphql-api-explorer_v1-e013fb2d4e922934a10bd273d18bd2f2.png)

## Testing a Hasura Cloud project​

Using the GraphQL API Explorer to test a Hasura Cloud project with public access requires only two pieces of
configuration for the project. Most importantly, you must set up unauthenticated access user roles. You can achieve this
by creating an `anonymous` role with the respective permissions.[ Read more here ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example)for detailed
steps.

The other piece of configuration is setting the `HASURA_GRAPHQL_UNAUTHORIZED_ROLE` environment variable to `anonymous` .[ Read more ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/#configuring-unauthenticated--public-access)on how to set up
unauthenticated/public access user roles.

The Hasura Cloud Project GraphQL API is publicly sharable, to allow users to access it without authentication. Navigate
to the project settings to find the public, sharable URL.

Image: [ API Explorer Share Link ](https://hasura.io/docs/assets/images/share-link_graphql-api-explorer_v1-396da1171bb489bafa17ee81a201c3e6.png)

Note

If an[ admin secret ](https://hasura.io/docs/latest/deployment/securing-graphql-endpoint/)is configured for your Hasura Project, Hasura GraphQL
Engine will automatically reject unauthenticated requests. In this case, for the project to be publicly accessible, the
admin secret has to be passed as a header in the GraphiQL interface under the **Request Headers** section. Be careful
not to leak a production admin secret publicly.

Image: [ API Explorer Header Admin Secret ](https://hasura.io/docs/assets/images/admin-secret-header_graphql-api-explorer_v1-4d21fc38065be915316f585e995c7691.png)

### Shareable URL construction​

Here are the supported, optional, configuration options which can be passed as URL query parameters to create a
shareable URL to the GraphQL Explorer. These must be[ http URL encoded ](https://www.urlencoder.org/).

| Parameter | Description |
|---|---|
| endpoint | URL pointing to a GraphQL service. |
| header | HTTP header to be supplied with requests. Multiple headers can be given by repeating the header param. |


Example:

`https : //cloud.hasura.io/public/graphiql?header=content-type:application/json&header=Authorization:bearer%20%3Center%20your%20token%20here%3E&endpoint=https://api.github.com/graphql`

Note

The header `content-type` is set to `application/json` by default if not provided in the URL.

### What did you think of this doc?

- [ TL;DR ](https://hasura.io/docs/latest/hasura-cloud/graphql-api-explorer/index/#tldr)
- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/graphql-api-explorer/index/#introduction)
- [ Try out a public GraphQL API ](https://hasura.io/docs/latest/hasura-cloud/graphql-api-explorer/index/#try-out-a-public-graphql-api)
- [ Connect to any GraphQL API ](https://hasura.io/docs/latest/hasura-cloud/graphql-api-explorer/index/#connect-to-any-graphql-api)
- [ Testing a Hasura Cloud project ](https://hasura.io/docs/latest/hasura-cloud/graphql-api-explorer/index/#testing-a-hasura-cloud-project)
    - [ Shareable URL construction ](https://hasura.io/docs/latest/hasura-cloud/graphql-api-explorer/index/#shareable-url-construction)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)