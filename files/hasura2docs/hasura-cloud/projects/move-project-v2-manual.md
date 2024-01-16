# Manually Move Hasura Cloud v1.3 Projects to Hasura v2.0

## Introduction​

Hasura Cloud now creates new projects with Hasura `v2.0` by default. Due to some underlying architectural changes in `v2.0` , existing projects have not yet been upgraded to `v2.0` .

In the meanwhile it is possible to manually "move" your project to use Hasura `v2.0` . You will lose any scheduled events
and the history of your processed events and async actions in the process though.

Do check the[ changelog ](https://github.com/hasura/graphql-engine/releases)first to see what changes and features have
been introduced.

## Move existing v1.3 project to a v2.0 project​

As it is not possible to actually upgrade your `v1.3` project to `v2.0` , you will have to essentially create a new
Hasura Project with `v2.0` and connect it with your database with the same Hasura Metadata as in the previous project.

### Step 1: Export Metadata from existing project​

See[ exporting metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/)to get a copy of the current Hasura Metadata on
your project.

Do ensure no further changes are made to the Hasura Metadata post this.

### Step 2: Create a v2.0 Cloud project​

See `Step 1` of[ creating projects ](https://hasura.io/docs/latest/hasura-cloud/projects/create/)to create a new Hasura Cloud `v2.0` project.

### Step 3: Connect your database with the name default to the new project​

See `Step 2` of[ creating projects ](https://hasura.io/docs/latest/hasura-cloud/projects/create/)to connect your existing database to the new
project. Please ensure you set the database name as `default` .

Note

After connecting a database to a `v2.0` project it will not be usable with a `v1.3` project. Hence it is recommended to
stop your `v1.3` project before doing this.

### Step 4: Apply the exported Metadata to the new project​

See[ applying metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/)to apply the earlier exported Metadata to the
new project.

Your GraphQL API should now be regenerated as in the earlier `v1.3` project.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2-manual/#introduction)
- [ Move existing v1.3 project to a v2.0 project ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2-manual/#move-existing-v13-project-to-a-v20-project)
    - [ Step 1: Export Metadata from existing project ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2-manual/#step-1-export-metadata-from-existing-project)

- [ Step 2: Create a v2.0 Cloud project ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2-manual/#step-2-create-a-v20-cloud-project)

- [ Step 3: Connect your database with the name default to the new project ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2-manual/#step-3-connect-your-database-with-the-name-default-to-the-new-project)

- [ Step 4: Apply the exported Metadata to the new project ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2-manual/#step-4-apply-the-exported-metadata-to-the-new-project)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)