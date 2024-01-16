# Vercel Integration

## Introduction​

You can connect your front-end[ Vercel ](https://vercel.com/dashboard)applications with a[ Hasura Cloud ](https://cloud.hasura.io/)project.

This integration does the following:

- Creates a new Hasura Cloud project which can serve as a unified back-end for one or more front-end applications i.e.
Vercel Projects depending on the scope of the integration.
- Configures necessary project settings i.e setting environment variables and exposing them on the client side. (Check
the[ list ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#vercel-environment-variables)of all environment variables set).


Creates a new Hasura Cloud project which can serve as a unified back-end for one or more front-end applications i.e.
Vercel Projects depending on the scope of the integration.

Configures necessary project settings i.e setting environment variables and exposing them on the client side. (Check
the[ list ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#vercel-environment-variables)of all environment variables set).

Image: [ Hasura Vercel Integration ](https://hasura.io/docs/assets/images/hasura-vercel-032902ea7996a2d57d7472403e9c30a8.png)

## Creating an Integration​

You can configure the[ official Hasura integration ](https://vercel.com/integrations/hasura)with your Vercel account.

Image: [ Hasura Official Integration page ](https://hasura.io/docs/assets/images/hasura-vercel-integration-b5c2512a7bbd51bf2fefc36835774189.png)

### Step 1: Prerequisites​

This integration requires you to have a Vercel account along with existing Vercel applications.

### Step 2: Initiate Integration​

- Navigate to the[ official Hasura integration ](https://vercel.com/integrations/hasura-v1)page and click on `Add Integration` .


Navigate to the[ official Hasura integration ](https://vercel.com/integrations/hasura-v1)page and click on `Add Integration` .

Image: [ Add Integration Button ](https://hasura.io/docs/assets/images/add-integration-button-acc92461749a6aec5bef0e2b0d46ff0f.png)

### Step 3: Select Vercel account​

- Select the account (personal or team) you want to install the integration on and click `Continue` .


Select the account (personal or team) you want to install the integration on and click `Continue` .

Image: [ Vercel Account Scope ](https://hasura.io/docs/assets/images/vercel-account-scope-699b45cd05e40030195f198bcb651590.png)

### Step 4: Select Integration Scope​

- Select the integration scope.| Scope | Description |
|---|---|
| All Projects | Configures all Vercel applications in the account. |
| Specific Projects | Configures only a subset of applications. |
- Click on `Add Integration` and a new window should pop up for the further steps specific to Hasura Cloud.


Select the integration scope.

| Scope | Description |
|---|---|
| All Projects | Configures all Vercel applications in the account. |
| Specific Projects | Configures only a subset of applications. |


Image: [ Vercel selected projects ](https://hasura.io/docs/assets/images/selected-projects-27d90b583e41c75d8d1916ee2dbf0514.png)

Click on `Add Integration` and a new window should pop up for the further steps specific to Hasura Cloud.

### Step 5: Configure Hasura Cloud​

- You'll be directed towards a Hasura Cloud signup or login page. This is skipped if you are already logged-in to Hasura
Cloud.
- Once you are logged in, a Hasura Cloud project is created for the integration and the required[ environment variables ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#vercel-environment-variables)are set for each Vercel project in the scope.
- Click on the first link to navigate to your Hasura Cloud project Console to configure your GraphQL API and connect to
a database. Check out the section on[ database setup ](https://hasura.io/docs/latest/hasura-cloud/projects/create/#cloud-projects-db-setup)on
how to do this.
- Click on `Install Integration` to install your integration.


You'll be directed towards a Hasura Cloud signup or login page. This is skipped if you are already logged-in to Hasura
Cloud.

Once you are logged in, a Hasura Cloud project is created for the integration and the required[ environment variables ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#vercel-environment-variables)are set for each Vercel project in the scope.

Image: [ Setup Progress ](https://hasura.io/docs/assets/images/setup-progress-a8aaa1be57c9f2f072003ef8c72918f0.png)

Click on the first link to navigate to your Hasura Cloud project Console to configure your GraphQL API and connect to
a database. Check out the section on[ database setup ](https://hasura.io/docs/latest/hasura-cloud/projects/create/#cloud-projects-db-setup)on
how to do this.

Image: [ Visit Console Button ](https://hasura.io/docs/assets/images/visit-console-88c809bfefb040f51b2ca51236303553.png)

Click on `Install Integration` to install your integration.

Image: [ Finish Setup Button ](https://hasura.io/docs/assets/images/install-integration-c474bcafec5d76591d29f3bb5b272591.png)

Note

Your integration will only be successfully configured upon clicking the `Install Integration` button.

### Step 6: Check finished setup​

- The Integration is now complete. You'll be redirected to the Vercel Dashboard.
- Click on `Configure` to navigate to Cloud Dashboard to see the latest project we created for you. This will be a
project with the tag `Vercel` on it.
- To change the scope of you integration, you can click on `Manage Access` to add/remove vercel applications from the
integration. Check out the[ Adding and removing projects from the Scope of Integration ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#vercel-change-scope)section
for more details.


The Integration is now complete. You'll be redirected to the Vercel Dashboard.

Image: [ Integration Complete ](https://hasura.io/docs/assets/images/integration-complete-34d2e7ea54b5f72c3562c81ea82bf3dd.png)

Click on `Configure` to navigate to Cloud Dashboard to see the latest project we created for you. This will be a
project with the tag `Vercel` on it.

Image: [ Integration Complete ](https://hasura.io/docs/assets/images/vercel-tag-project-a4e56b51676494b1957633ba4f53e9f7.png)

To change the scope of you integration, you can click on `Manage Access` to add/remove vercel applications from the
integration. Check out the[ Adding and removing projects from the Scope of Integration ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#vercel-change-scope)section
for more details.

## Environment variables​

- List of Hasura Cloud environment variables configured by the integration for each Vercel application in the scope of
the integration:| Title | Description |
|---|---|
| HASURA_PROJECT_ENDPOINT | GraphQL API endpoint of the Hasura Cloud project. |
| NEXT_PUBLIC_HASURA_PROJECT_ENDPOINT | GraphQL API endpoint to be exposed on the Next.js browser client. |
| HASURA_ADMIN_SECRET | Admin secret key to access your GraphQL API. |

    - You can check the environment variables configured by the integration for you in the respective Vercel Project's
settings on Vercel dashboard. These are set up for `Development` , `Preview` and `Production` environments. Check the[ Vercel docs ](https://vercel.com/docs/concepts/projects/environment-variables)for environment variables for further
reference.


List of Hasura Cloud environment variables configured by the integration for each Vercel application in the scope of
the integration:

| Title | Description |
|---|---|
| HASURA_PROJECT_ENDPOINT | GraphQL API endpoint of the Hasura Cloud project. |
| NEXT_PUBLIC_HASURA_PROJECT_ENDPOINT | GraphQL API endpoint to be exposed on the Next.js browser client. |
| HASURA_ADMIN_SECRET | Admin secret key to access your GraphQL API. |


You can check the environment variables configured by the integration for you in the respective Vercel Project's
settings on Vercel dashboard. These are set up for `Development` , `Preview` and `Production` environments. Check the[ Vercel docs ](https://vercel.com/docs/concepts/projects/environment-variables)for environment variables for further
reference.

Image: [ Environment variables ](https://hasura.io/docs/assets/images/environment-variables-da2ffb8ac5c952e695b0e316ec3787ce.png)

Note

- If a[ custom domain ](https://hasura.io/docs/latest/hasura-cloud/domains/)is added to the Hasura Cloud project, you'll have to set this custom
value to `HASURA_PROJECT_ENDPOINT` and `NEXT_HASURA_PROJECT_ENDPOINT` manually in the respective Vercel project's
settings.
- Similarly if the Hasura Cloud project's admin secret is changed, you will have to edit the `HASURA_ADMIN_SECRET` manually in the respective Vercel project's settings.


## Adding and removing projects from the Scope of Integration​

Once the integration is installed, you can change the scope of the integration.

- Navigate to the installed integration page and click on `Manage Access` . This will show you the current status of the
integration, i.e the projects that are currently configured.
- If the integration is installed for `All Projects` , you can change the scope to `Specific Projects` and select the
projects from the dropdown you want to keep the integration on. If installed for `Specific Projects` , you can add
individual projects from the dropdown or remove them from the list.
- Click on `Save` to save the changes.


Navigate to the installed integration page and click on `Manage Access` . This will show you the current status of the
integration, i.e the projects that are currently configured.

Image: [ Manage Access Button ](https://hasura.io/docs/assets/images/manage-access-button-da097f7df64941f9d48735c79b1fdddb.png)

If the integration is installed for `All Projects` , you can change the scope to `Specific Projects` and select the
projects from the dropdown you want to keep the integration on. If installed for `Specific Projects` , you can add
individual projects from the dropdown or remove them from the list.

Image: [ Manage Access For Projects ](https://hasura.io/docs/assets/images/manage-access-projects-e60538531d575b5cdc3097182ae2fb7b.png)

Click on `Save` to save the changes.

Note

Hasura Cloud project's environment variables will be automatically set for the added projects and will be removed for
the removed projects.

## Removing an Integration​

- To remove the configured integration, navigate to the `Integrations` sections in Vercel Dashboard and spot the Hasura
integration in the list. Click on `Manage` to navigate to the integration page.
- Scroll down to the bottom of the page and click on `Remove Integration` . Vercel will remove the integration along with
the set environment variables from the applications.


To remove the configured integration, navigate to the `Integrations` sections in Vercel Dashboard and spot the Hasura
integration in the list. Click on `Manage` to navigate to the integration page.

Image: [ Vercel Integration Tab ](https://hasura.io/docs/assets/images/integration-tab-a285a7b7df40b6b3e1b6c77a30941687.png)

Scroll down to the bottom of the page and click on `Remove Integration` . Vercel will remove the integration along with
the set environment variables from the applications.

Image: [ Remove Vercel Integration ](https://hasura.io/docs/assets/images/remove-integration-9c46a75f6cd4416ef85d5fd60c28062f.png)

Your Hasura Cloud project will not be affected.

## Support​

File a support ticket by navigating to the[ Help & Support ](https://cloud.hasura.io/support/create-ticket)tab on the
Hasura Cloud dashboard if you face any issues.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#introduction)
- [ Creating an Integration ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#creating-an-integration)
    - [ Step 1: Prerequisites ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#step-1-prerequisites)

- [ Step 2: Initiate Integration ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#step-2-initiate-integration)

- [ Step 3: Select Vercel account ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#step-3-select-vercel-account)

- [ Step 4: Select Integration Scope ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#step-4-select-integration-scope)

- [ Step 5: Configure Hasura Cloud ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#step-5-configure-hasura-cloud)

- [ Step 6: Check finished setup ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#step-6-check-finished-setup)
- [ Environment variables ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#vercel-environment-variables)
- [ Adding and removing projects from the Scope of Integration ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#vercel-change-scope)
- [ Removing an Integration ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#removing-an-integration)
- [ Support ](https://hasura.io/docs/latest/hasura-cloud/vercel-integration/#support)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)