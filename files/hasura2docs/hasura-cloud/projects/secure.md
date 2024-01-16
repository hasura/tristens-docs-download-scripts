# Secure Projects

## Introduction​

To make sure that your GraphQL endpoint is not publicly accessible, a randomly generated admin secret key is added by
default to your project at the time of project creation.

## Updating the admin secret​

### Step 1: Go to settings​

On the project overview, click on the settings icon on the top right of the relevant project.

Image: [ Go to settings ](https://hasura.io/docs/assets/images/secure-settings-b8069dce2e01b9f0626c32dc9ec6ddc1.png)

### Step 2: Navigate to env vars​

On the `Env vars` tab, you will see the `HASURA_GRAPHQL_ADMIN_SECRET` env var.

Image: [ Navigate to env vars ](https://hasura.io/docs/assets/images/secure-admin-envvar-c6ed34b76cb5e2ef69e2e0394fbb719a.png)

### Step 3: Update admin secret​

Click on the `HASURA_GRAPHQL_ADMIN_SECRET` env var to update the value.

Image: [ Set admin secret ](https://hasura.io/docs/assets/images/secure-update-envvar-348992427ec1ac2ee5386abb12b6e66c.png)

## Accessing Hasura​

When you launch the Console from the Hasura Cloud dashboard, you'll be authenticated as an admin. If you want to make
API calls from outside the Console, you need to pass the admin secret as the *x-hasura-admin-secret* request
header.

Note

The admin secret should be treated like a password i.e. it should be kept secret and shouldn't be passed from frontend
clients. Refer[ this ](https://hasura.io/docs/latest/auth/authentication/index/)to set up user authentication.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/projects/secure/#introduction)
- [ Updating the admin secret ](https://hasura.io/docs/latest/hasura-cloud/projects/secure/#updating-the-admin-secret)
    - [ Step 1: Go to settings ](https://hasura.io/docs/latest/hasura-cloud/projects/secure/#step-1-go-to-settings)

- [ Step 2: Navigate to env vars ](https://hasura.io/docs/latest/hasura-cloud/projects/secure/#step-2-navigate-to-env-vars)

- [ Step 3: Update admin secret ](https://hasura.io/docs/latest/hasura-cloud/projects/secure/#step-3-update-admin-secret)
- [ Accessing Hasura ](https://hasura.io/docs/latest/hasura-cloud/projects/secure/#accessing-hasura)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)