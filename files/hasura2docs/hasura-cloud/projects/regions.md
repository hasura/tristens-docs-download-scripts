# Deployment Regions

## Introduction​

You can deploy Hasura Cloud projects in one of the supported regions (more regions are coming soon). A project's region
of deployment can be selected while creating the project and it can be changed later from the project details.

## The importance of selecting the right region​

To get the best possible performance out from your Hasura APIs, we highly recommend hosting data sources (database/API)
and Hasura Projects in the same cloud provider region. See the sections below for more information on how to create a
project in a given region or how to move an existing project to another region.

## Selecting the region while creating a project​

Click on the `New Project` button on the project-list page. You can select the project's region of deployment from the `Select a region` dropdown.

Image: [ select regions while project creation ](https://hasura.io/docs/assets/images/regions-while-creation-2fb57759251cc8ff427a171c7a386585.png)

## Changing region of an existing project​

Go the the project details by clicking on the settings icon on your project card in the project list.

Image: [ select regions while project creation ](https://hasura.io/docs/assets/images/project-manage-5b37a214a39b39b6287136606da021c4.png)

The `Region` field displays the project's current region of deployment. For switching the region, click on the edit icon
in the `Region` field.

Image: [ select regions while project creation ](data:image/png;base64,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)

There might be a short downtime while your project is being moved to a different region. If your database allows
connections only from specific IP addresses, make sure you add the Hasura Cloud IP of this new region to the list of
allowed IP addresses.

Choose a region of your choice and hit `Save` .

Image: [ change region confirmation ](https://hasura.io/docs/assets/images/region-change-confirmation-20dce2ed2b8093c7769fae09d783eab4.png)

Note

Support for deploying a project in multiple regions is coming soon.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/projects/regions/#introduction)
- [ The importance of selecting the right region ](https://hasura.io/docs/latest/hasura-cloud/projects/regions/#the-importance-of-selecting-the-right-region)
- [ Selecting the region while creating a project ](https://hasura.io/docs/latest/hasura-cloud/projects/regions/#selecting-the-region-while-creating-a-project)
- [ Changing region of an existing project ](https://hasura.io/docs/latest/hasura-cloud/projects/regions/#changing-region-of-an-existing-project)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)