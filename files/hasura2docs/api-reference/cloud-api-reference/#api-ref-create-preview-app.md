# Hasura Cloud API Reference

## Introduction​

Hasura Cloud provides a GraphQL API to interact with services to create and manage your Cloud Projects using any GraphQL
client.

## Endpoint​

The Hasura Cloud API endpoint is `https://data.pro.hasura.io/v1/graphql` .

## Authentication​

Authentication is done using a Personal Access Token that you can create from the Hasura Cloud Dashboard. You can find
this option in the "My Account" section on bottom left.

Image: [ Create a Hasura Cloud personal access token ](https://hasura.io/docs/assets/images/create-new-hasura-access-token_cloud_2.8.1-4a1d15a8374700e676c5e34c0c6045f9.png)

Once you have created the token it should be used as a header in your requests in the format: `Authorization: pat <token>` .

Note

This token can be used to authenticate against all of your Hasura Cloud APIs and Projects. It is only revealed once on
creation. Make sure you keep it secure. The token will be valid until you delete it from the dashboard.

## APIs​

Each Hasura Cloud Project is backed by an API entity called "Tenant", with a distinct "Tenant ID" which is different
from the "Project ID". Each Project is associated with a Tenant. In some cases, like with the Metrics API, the Project
ID is used instead of Tenant ID.

- [ Create a Project ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#create-a-project)
- [ Get Project Tenant id ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#get-project-tenant-id)
- [ Get Tenant details ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#get-tenant-details)
- [ Delete a Tenant ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#delete-a-tenant)
- [ Get ENV Vars ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#get-env-vars)
- [ Update ENV Vars ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#update-env-vars)
- [ Create GitHub Preview App ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#api-ref-create-preview-app)
- [ Fetch Preview App Creation Status ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#api-ref-fetch-preview-app-creation-status)


### Create a Project​

```
mutation   createProject   {
   createTenant (
     cloud :   " aws "
     region :   " us-east-2 "
     envs :   [ {   key :   "HASURA_GRAPHQL_CORS_DOMAIN" ,   value :   "*"   } ,   {   key :   "MY_ENV_VAR_1" ,   value :   "my value 1"   } ]
   )   {
     id
     name
   }
}
```

### Get Project Tenant id​

```
query   getProjectTenantId   {
   projects_by_pk ( id :   "7a79cf94-0e53-4520-a560-1b02bf522f08" )   {
     id
     tenant   {
       id
     }
   }
}
```

### Get Tenant details​

```
query   getTenantDetails   {
   tenant_by_pk ( id :   "7a79cf94-0e53-4520-a560-1b02bf522f08" )   {
     id
     slug
     project   {
       id
       endpoint
     }
   }
}
```

### Delete a Tenant​

```
mutation   deleteTenant   {
   deleteTenant ( tenantId :   "7a79cf94-0e53-4520-a560-1b02bf522f08" )   {
     status
   }
}
```

### Get ENV Vars​

```
query   getTenantENV   {
   getTenantEnv ( tenantId :   "7a79cf94-0e53-4520-a560-1b02bf522f08" )   {
     hash
     envVars
   }
}
```

### Update ENV Vars​

```
mutation   updateTenantEnv   {
   updateTenantEnv (
     tenantId :   " 7a79cf94-0e53-4520-a560-1b02bf522f08 "
     currentHash :   " 6902a395d70072fbf8d36288f0eacc36c9d82e68 "
     envs :   [
       {   key :   "HASURA_GRAPHQL_ENABLE_CONSOLE" ,   value :   "true"   }
       {   key :   "ACTIONS_ENDPOINT" ,   value :   "https://my-actions-endpoint.com/actions"   }
     ]
   )   {
     hash
     envVars
   }
}
```

### Create GitHub Preview App​

Schedules the creation of a Hasura Cloud Project with Migrations and Metadata from a branch of a GitHub repo.

```
mutation   createGitHubPreviewApp   {
   createGitHubPreviewApp (
     payload :   {
       githubPersonalAccessToken :   " < github_access_token > "
       githubRepoDetails :   {   branch :   "main" ,   owner :   "my-org" ,   repo :   "my-repo" ,   directory :   "backend/hasura"   }
       projectOptions :   {
         cloud :   " aws "
         region :   " us-east-2 "
         plan :   " cloud_free "
         name :   " my-app_name "
         envVars :   [
           {   key :   "HASURA_GRAPHQL_AUTH_HOOK" ,   value :   "https://my-webhook.com"   }
           {   key :   "MY_ENV_VAR_1" ,   value :   "my value 1"   }
         ]
       }
     }
   )   {
     githubPreviewAppJobID
   }
}
```

#### Input arguments​

| Argument | Description |
|---|---|
|  `githubPersonalAccessToken`  | GitHub personal access token for Hasura Cloud to access the Migrations and Metadata from your repository. Refer to GitHub docs on how to create a[ GitHub personal access token ](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). The token should have read access to the repository. |
| under `githubRepoDetails` : `owner`  | GitHub repository owner (user or organization) |
| under `githubRepoDetails` : `repo`  | GitHub repository name. |
| under `githubRepoDetails` : `branch`  | Name of the branch from which to create a Preview App. |
| under `githubRepoDetails` : `directory`  | Path to the Hasura Project directory (typically created by the Hasura CLI) containing Migrations and Metadata. The path should be relative to the project's root directory. |
| under `projectOptions` : `name`  | Name of the Preview App. A Hasura Cloud project will be created with the same name. Can contain lowercase characters, numbers and hyphens. |
| under `projectOptions` : `cloud`  | The cloud provider to deploy the Preview App on. A Hasura Cloud project will be created in the specified cloud provider. Available: `aws` and `gcp` . |
| under `projectOptions` : `region`  | The region within the cloud provider to deploy the Preview App on. A Hasura Cloud project will be created in the specified region. Refer to the Hasura Cloud dashboard for available options. |
| under `projectOptions` : `plan`  | Pricing tier of the created Preview App. Available options: `cloud_ free` and `cloud_ payg` (corresponds to Free Tier and Professional Tier respectively). |
| under `projectOptions` : `envVars`  | ENV vars to be set for the created Preview App. |


#### Output Fields​

| Argument | Description |
|---|---|
|  `githubPreviewAppJobID`  | Job ID of the Preview App creation job. This does not mean the Preview App is created, the ID identifies the job responsible for creating the Preview App. For the status of the Preview App creation, query the[ getPreviewAppCreationStatus API ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-fetch-preview-app-creation-status). |


### Fetch Preview App Creation Status​

Preview App creation is a multistep process. This query fetches the status of the Preview App creation. The input `jobID` is the same ID obtained in the output of the[ Create GitHub Preview App ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app)mutation.

```
query   getPreviewAppCreationStatus ( $jobId :   uuid ! )   {
   jobs_by_pk ( id :   $jobId )   {
     id
     status
     tasks   {
       id
       name
       task_events   {
         id
         event_type
         public_event_data
         error
       }
     }
   }
}
```

#### Input Arguments​

| Argument | Description |
|---|---|
|  `id`  | Job ID of the Preview App creation job. The ID identifies the job responsible for creating the Preview App. This can be obtained from the output of the[ createGitHubPreviewApp API ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app). |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#introduction)
- [ Endpoint ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#endpoint)
- [ Authentication ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#authentication)
- [ APIs ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#apis)
    - [ Create a Project ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#create-a-project)

- [ Get Project Tenant id ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#get-project-tenant-id)

- [ Get Tenant details ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#get-tenant-details)

- [ Delete a Tenant ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#delete-a-tenant)

- [ Get ENV Vars ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#get-env-vars)

- [ Update ENV Vars ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#update-env-vars)

- [ Create GitHub Preview App ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#api-ref-create-preview-app)

- [ Fetch Preview App Creation Status ](https://hasura.io/docs/latest/api-reference/cloud-api-reference/#api-ref-create-preview-app/#api-ref-fetch-preview-app-creation-status)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)