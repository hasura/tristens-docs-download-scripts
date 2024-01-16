# Transfer Existing Hasura Cloud Project to a New Project

## Introduction​

To transfer a project you will have to create a new Hasura Project and configure it with the same Hasura Metadata and
other configuration as in the previous project.

The following is a guide to achieve this.

## Step 1: Export Metadata from existing project​

See[ exporting metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/)to get a copy of the current Hasura Metadata on
your project.

Do ensure no further changes are made to the Hasura Metadata post this.

## Step 2: Create a new Cloud project with the same configuration​

See `Step 1` of[ creating projects ](https://hasura.io/docs/latest/hasura-cloud/projects/create/)to create a new Hasura Cloud project.

After project creation, update the Hasura Cloud configuration of the new project with the same configuration as the
earlier project. i.e. add the same ENV vars, custom domains, collaborators, billing, etc.

## Step 3: Apply the exported Metadata to the new project​

See[ applying metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/)to apply the earlier exported Metadata to the
new project.

The new project should now be generating the same GraphQL API as the earlier project.

## Step 4: Delete the earlier project​

See[ deleting projects ](https://hasura.io/docs/latest/hasura-cloud/projects/delete/)to delete the earlier project.

## Optional steps​

- If you are using Hasura Migrations on your project, please mark all existing Migrations as applied on the new project
using the following Hasura CLI command:
- You can[ rename ](https://hasura.io/docs/latest/hasura-cloud/projects/details/#rename-project)your new project to the same name as the earlier
project if you wish.
- If you haven't renamed your new project or set up a[ custom domain ](https://hasura.io/docs/latest/hasura-cloud/domains/)for your project, you
might want to update any clients consuming the GraphQL API to point to the new project's GraphQL endpoint.


If you are using Hasura Migrations on your project, please mark all existing Migrations as applied on the new project
using the following Hasura CLI command:

`hasura migrate apply --skip-execution --endpoint  < new-project-endpoint >  --admin-secret  < new-project-admin-secret >  --all-databases`

You can[ rename ](https://hasura.io/docs/latest/hasura-cloud/projects/details/#rename-project)your new project to the same name as the earlier
project if you wish.

If you haven't renamed your new project or set up a[ custom domain ](https://hasura.io/docs/latest/hasura-cloud/domains/)for your project, you
might want to update any clients consuming the GraphQL API to point to the new project's GraphQL endpoint.

## Zero-downtime transfer​

To achieve a zero-downtime transfer, you will need to have a[ custom domain ](https://hasura.io/docs/latest/hasura-cloud/domains/)attached to your
Cloud project. Once the new project is set up identically as the old one, you can update the DNS entries for your custom
domain to the new project to have a seamless transfer of traffic to the new project.

If you simply want to avoid updating your clients with the new project's API endpoint, you can simply[ rename ](https://hasura.io/docs/latest/hasura-cloud/projects/details/#rename-project)your new project with the same name as the earlier project.
This will cause a short downtime of your API after you delete your old project until you rename the new one.

## Caveats​

You will lose the following data from your earlier project in the process:

- all existing scheduled events
- all existing async actions
- past invocation logs of cron triggers


If you would like these to be transferred to the new project as well please get in touch with support regarding this
before deleting the old project.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-manual/#introduction)
- [ Step 1: Export Metadata from existing project ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-manual/#step-1-export-metadata-from-existing-project)
- [ Step 2: Create a new Cloud project with the same configuration ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-manual/#step-2-create-a-new-cloud-project-with-the-same-configuration)
- [ Step 3: Apply the exported Metadata to the new project ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-manual/#step-3-apply-the-exported-metadata-to-the-new-project)
- [ Step 4: Delete the earlier project ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-manual/#step-4-delete-the-earlier-project)
- [ Optional steps ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-manual/#optional-steps)
- [ Zero-downtime transfer ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-manual/#zero-downtime-transfer)
- [ Caveats ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-manual/#caveats)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)