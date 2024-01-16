# Deploying Hasura GraphQL Engine on Render

## Introduction​

This guide shows how to deploy the Hasura GraphQL Engine on[ Render ](https://render.com).

## One-click Deploy on Render​

Note

Make sure to[ create a free Render account ](https://render.com/register)first.

Once you're logged into your Render account, click the button below to deploy Hasura and a new managed PostgreSQL
database wired up to your Hasura instance.

[  ](https://render.com/deploy?repo=https://github.com/render-examples/hasura-graphql)

Image: [ render_deploy_button ](https://render.com/images/deploy-to-render-button.svg)

You will see the Hasura web service and PostgreSQL instance to be created:

Image: [ Deploy To Render Hasura Page ](https://hasura.io/docs/assets/images/deploy-to-render-hasura-6147ba97d3edb79797059069e5df2274.png)

That's it! Read on to configure your Hasura instance.

## Access your Hasura Console​

Once **Deploy to Render** succeeds, you can click through to your Hasura service page on Render's dashboard.

Image: [ Render Hasura Header ](https://hasura.io/docs/assets/images/deploy-to-render-hasura-header-d32a96a3569fe81575bb5e30685e577e.png)

You can monitor the deployment of the Hasura web service from the **Logs** tab. Once the service is up, use the link on
the service page to access your Hasura Console:

`https:// < your-hasura-slug > .onrender.com/`

You can create tables and test your GraphQL queries here.

## References​

- [ Render Hasura GraphQL on GitHub ](https://github.com/render-examples/hasura-graphql)
- [ Render Docs ](https://render.com/docs)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/deployment-guides/render-one-click/#introduction)
- [ One-click Deploy on Render ](https://hasura.io/docs/latest/deployment/deployment-guides/render-one-click/#one-click-deploy-on-render)
- [ Access your Hasura Console ](https://hasura.io/docs/latest/deployment/deployment-guides/render-one-click/#access-your-hasura-console)
- [ References ](https://hasura.io/docs/latest/deployment/deployment-guides/render-one-click/#references)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)