# Deploying Hasura GraphQL Engine on Koyeb

## Introduction​

This guide explains how to deploy the Hasura GraphQL Engine on the[ Koyeb Serverless Platform ](https://koyeb.com).

## Prerequisites​

To successfully follow and complete this guide, you need:

- A PostgreSQL database to use as the Hasura GraphQL Engine backend.
- A[ Koyeb account ](https://app.koyeb.com)to deploy and run the Hasura GraphQL Engine.


## One-click deploy to Koyeb​

To deploy Hasura to Koyeb quickly, click the button below:

[  ](https://app.koyeb.com/deploy?name=hasura-demo&type=docker&image=hasura/graphql-engine&env%5BHASURA_GRAPHQL_DATABASE_URL%5D=CHANGE_ME&env%5BHASURA_GRAPHQL_ENABLE_CONSOLE%5D=true&env%5BHASURA_GRAPHQL_ADMIN_SECRET%5D=CHANGE_ME&ports=8080;http;/)

Image: [ Deploy to Koyeb ](https://www.koyeb.com/static/images/deploy/button.svg)

On the configuration screen, set the `HASURA_GRAPHQL_DATABASE_URL` environment variable to the connection string for your database and the `HASURA_GRAPHQL_ADMIN_SECRET` environment variable to a secret value to access the Hasura Console.

Click the **Deploy** button when you are finished.  When the deployment completes, you can[ access the Hasura Console ](https://hasura.io/docs/latest/deployment/deployment-guides/koyeb/#access-the-hasura-console).

## Deploy Hasura GraphQL Engine on Koyeb manually​

To deploy the Hasura GraphQL Engine on Koyeb manually, we use the `hasura/graphql-engine` Docker image.

On the[ Koyeb control panel ](https://app.koyeb.com/), click the **Create App** button. You land on the first page of the Koyeb App creation form.

Image: [ Koyeb App creation form ](https://hasura.io/docs/assets/images/koyeb-hasura-app-creation-9ef0118a1a6dc1834d434fcc5692ed51.png)

1. Select **Docker** as the deployment method.
2. Fill the `Image` field with `hasura/graphql-engine` .  Leave the `Tag` field blank to use the latest image.  Click **Next** to continue.
3. Click the **Advanced** button to access additional options.
4. In the **Environment variables** section, configure the environment variables required to properly run the Hasura GraphQL Engine:
    - `HASURA_GRAPHQL_DATABASE_URL` : The environment variable containing the PostgreSQL URL, i.e. `postgres://<user>:<password>@<host>:<port>/<database>` . Since this value contains sensitive information, select the "Secret" type.  Secrets are encrypted at rest and are ideal for storing sensitive data like API keys, OAuth tokens, etc.  Choose "Create secret" in the "Value" drop-down menu and enter the secret value in the "Create secret" form.

- `HASURA_GRAPHQL_ENABLE_CONSOLE` : Set to `true` . This will expose and allow you to access the Hasura Console.

- `HASURA_GRAPHQL_ADMIN_SECRET` : The secret to access the Hasura Console. As with the `HASURA_GRAPHQL_DATABASE_URL` , we strongly recommend using a secret to store this value.

5. `HASURA_GRAPHQL_DATABASE_URL` : The environment variable containing the PostgreSQL URL, i.e. `postgres://<user>:<password>@<host>:<port>/<database>` . Since this value contains sensitive information, select the "Secret" type.  Secrets are encrypted at rest and are ideal for storing sensitive data like API keys, OAuth tokens, etc.  Choose "Create secret" in the "Value" drop-down menu and enter the secret value in the "Create secret" form.

6. `HASURA_GRAPHQL_ENABLE_CONSOLE` : Set to `true` . This will expose and allow you to access the Hasura Console.

7. `HASURA_GRAPHQL_ADMIN_SECRET` : The secret to access the Hasura Console. As with the `HASURA_GRAPHQL_DATABASE_URL` , we strongly recommend using a secret to store this value.
8. In the **Exposing your service** section, change the `Port` from `80` to `8080` to match the port that the `hasura/graphql-engine` Docker image app listens on. Koyeb uses this setting to perform application health checks and to properly route incoming HTTP requests. If you want the Hasura GraphQL Engine to be available on a specific path, you can change the default one ( `/` ) to the path of your choice.
9. Give your App a name, i.e `hasura-demo` , and click **Deploy** .


Select **Docker** as the deployment method.

Fill the `Image` field with `hasura/graphql-engine` .  Leave the `Tag` field blank to use the latest image.  Click **Next** to continue.

Click the **Advanced** button to access additional options.

In the **Environment variables** section, configure the environment variables required to properly run the Hasura GraphQL Engine:

In the **Exposing your service** section, change the `Port` from `80` to `8080` to match the port that the `hasura/graphql-engine` Docker image app listens on. Koyeb uses this setting to perform application health checks and to properly route incoming HTTP requests. If you want the Hasura GraphQL Engine to be available on a specific path, you can change the default one ( `/` ) to the path of your choice.

Give your App a name, i.e `hasura-demo` , and click **Deploy** .

The deployment should be up and running in a few seconds.

## Access the Hasura Console​

Once your Koyeb App is deployed, you can click the App link in the Koyeb control panel to access the Hasura Console:

Image: [ Koyeb control panel ](https://hasura.io/docs/assets/images/koyeb-hasura-service-221f0712aceb053325516b09ec1332c2.png)

`https://<your-app-name>-<your-org-name>.koyeb.app/`

At any time, you can track your Hasura service status in the Koyeb Control Panel and view the Hasura GraphQL Engine web service logs in the **Logs** tab of your service.

## References​

- [ Koyeb Docs ](https://koyeb.com/docs%3E)
- [ Koyeb Hasura tutorial ](https://www.koyeb.com/tutorials/deploy-the-hasura-graphql-engine-to-expose-and-create-apis-from-your-databases-on-koyeb)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/deployment-guides/koyeb/#introduction)
- [ Prerequisites ](https://hasura.io/docs/latest/deployment/deployment-guides/koyeb/#prerequisites)
- [ One-click deploy to Koyeb ](https://hasura.io/docs/latest/deployment/deployment-guides/koyeb/#one-click-deploy-to-koyeb)
- [ Deploy Hasura GraphQL Engine on Koyeb manually ](https://hasura.io/docs/latest/deployment/deployment-guides/koyeb/#deploy-hasura-graphql-engine-on-koyeb-manually)
- [ Access the Hasura Console ](https://hasura.io/docs/latest/deployment/deployment-guides/koyeb/#access-the-hasura-console)
- [ References ](https://hasura.io/docs/latest/deployment/deployment-guides/koyeb/#references)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)