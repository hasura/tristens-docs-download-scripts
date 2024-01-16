# Updating Hasura Cloud v1.3 Projects to Hasura v2.0

## Introduction​

Hasura Cloud now creates new projects with Hasura `v2.0` by default. Due to some behavior and underlying architectural
changes in `v2.0` , existing projects have not been auto-updated to `v2.0` . You can update your older `v1.3` projects to `v2.0` by following this guide.

( *You can find the older guide to do this process manually* [ here ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2-manual/))

Note

In case you happen to have a large number of past cron and Event Trigger logs in your database, this might slow down the
update to v2 and might even cause DB errors in certain scenarios.

 **It is highly recommended to clean up past cron and Event Trigger logs data from the database before attempting the
update if you have a lot of historical data.** 

You can take a dump of this data before cleaning up if you wish to keep the log history.

## What has changed?​

Check the[ core updating to v2.0 guide ](https://hasura.io/docs/latest/resources/upgrade-hasura-v2/)and the[ release notes ](https://github.com/hasura/graphql-engine/releases)to see what new concepts, features and behavior
changes have been introduced in Hasura `v2.0` .

Note that Hasura v2 Cloud projects' Metadata is now stored in Metadata DBs managed by Hasura Cloud. Hence the new `HASURA_GRAPHQL_METADATA_DATABASE_URL` env var is not configurable on Hasura Cloud and is managed by Hasura Cloud
itself.

See the section on[ hasura_v1_v2_compatibility ](https://hasura.io/docs/latest/resources/upgrade-hasura-v2/#hasura-v1-v2-compatibility)to use a
Hasura v2 Cloud project like a Hasura v1 Cloud project.

## Estimated time needed for update​

Depending on the size of your project the update process should typically take around **5-10 minutes** to be completed.

## Project availability during update​

During the update process Hasura Cloud will need to place your project in a "Maintenance mode" till the process is
complete.

When **Cloud maintenance mode** is enabled, all Hasura Cloud project actions such as updating env vars, transferring
ownership, etc. will be disabled.

When **Server maintenance mode** is enabled, all actions updating the project Metadata such as tracking tables, adding
relationships, etc. will be disabled.

Hence it is recommended to update your project at a time convenient to all project collaborators.

Apart from the brief moments needed to enable/disable the server maintenance mode, **your GraphQL API will continue to
function during this period.** 

## Post-update steps​

- As with most major updates, we would recommend you to monitor and ensure all functionalities of your project are
working as expected post the update and the update did not cause any unexpected changes. Do get in touch with us in
case you notice anything unexpected.
- You can choose to unset the `HASURA_GRAPHQL_V1_BOOLEAN_NULL_COLLAPSE` env var that was added to your project during
the update to preserve a `v1.3` behavior that was modified in `v2.0` .[ See details ](https://hasura.io/docs/latest/resources/upgrade-hasura-v2/#hasura-v2-null-where-change). We recommend moving to the new behavior
by unsetting the env var after verifying your project is not impacted by the change.
- Check the[ Post update steps ](https://hasura.io/docs/latest/resources/upgrade-hasura-v2/#hasura-v1-to-v2-post-update-steps)section of the core
updating to v2.0 guide for other changes you should make post your project update.


## Update process​

Update option might not be currently enabled for all users

If you do not see the option to update your project as mentioned below, please reach out to support.

To start the update, you should see a button called `Update` next to your project on the Project list page as shown
below:

Image: [ Update project ](https://hasura.io/docs/assets/images/update-project-88d79ece3cc0a46350234342bd78518e.png)

Clicking on this button will trigger an update job that will perform a few tasks to update your current `v1.3` project
to `v2.0` .

Refer to the following task wise breakdown of the update job to understand what the job will be doing and to check your
project end state in case of any failures.

Do reach out to support if you observe any issues with the update process or run into any other problems post the v2.0
update.

### Update job sub-tasks​

The following is a task wise breakdown of the update to v2.0 job.

Each task in the update job has a **rollback strategy** in case any failures occur. If the rollback steps of any task
fail, the project might be in an unhealthy state in which case please get in touch with support immediately for
assistance.

#### Step 1: Initializing​

##### Step 1.1: Validating​

###### Sub-tasks:​

- Enable cloud maintenance mode
- Ensure infrastructure for update is available


###### On Failure:​

- Disable cloud maintenance mode
- **Project stays in v1.3**


##### Step 1.2: Enabling maintenance mode​

###### Sub-tasks:​

- Set `HASURA_GRAPHQL_ENABLE_MAINTENANCE_MODE` env var to enable server maintenance mode
- Set `HASURA_GRAPHQL_V1_BOOLEAN_NULL_COLLAPSE` env var to `true` to maintain `v1.3` behavior for `null` values in `where` filters.[ (Know more) ](https://hasura.io/docs/latest/resources/upgrade-hasura-v2/#hasura-v2-behavior-changes)


###### On Failure:​

- Unset `HASURA_GRAPHQL_V1_BOOLEAN_NULL_COLLAPSE` env var
- Unset `HASURA_GRAPHQL_ENABLE_MAINTENANCE_MODE` env var to disable server maintenance mode
- Disable cloud maintenance mode
- **Project stays in v1.3**


#### Step 2: Updating project​

##### Step 2.1: Migrating project metadata​

###### Sub-tasks:​

- Take a backup of server Metadata from user database & move Metadata to cloud Metadata database


###### On Failure:​

- Unset `HASURA_GRAPHQL_V1_BOOLEAN_NULL_COLLAPSE` env var
- Unset `HASURA_GRAPHQL_ENABLE_MAINTENANCE_MODE` env var to disable server maintenance mode
- Disable cloud maintenance mode
- **Project stays in v1.3**


##### Step 2.2: Creating v2.0 instance​

###### Sub-tasks:​

- Create `v2.0` instance
- Start routing requests to `v2.0` instance


###### On Failure:​

- Start routing requests back to `v1.3` instance
- Unset `HASURA_GRAPHQL_ENABLE_MAINTENANCE_MODE` env var to disable server maintenance mode
- Disable cloud maintenance mode
- **Project stays in v1.3**


##### Step 2.3: Migrating pending events, async actions data​

###### Sub-tasks:​

- Send signal to shutdown `v1.3` instance
- Wait for `v1.3` to gracefully shutdown after completing processing of any in-flight events
- Migrate pending events, async actions data to cloud Metadata database


###### On Failure:​

- Restart `v1.3` instance
- Start routing requests back to `v1.3` instance
- Unset `HASURA_GRAPHQL_ENABLE_MAINTENANCE_MODE` env var to disable server maintenance mode
- Disable cloud maintenance mode
- **Project stays in v1.3**


##### Step 2.4: Migrating processed events, async actions data​

###### Sub-tasks:​

- Migrate invocation logs of processed events, async actions to cloud Metadata database


###### On Failure:​

- **No action taken. Job continues to next task**
- Invocation logs of already processed events, async actions are not migrated. Contact support to assist with a manual
migration of the logs if needed


#### Step 3: Validating update​

##### Step 3.1: Disabling maintenance mode​

###### Sub-tasks:​

- Unset `HASURA_GRAPHQL_ENABLE_MAINTENANCE_MODE` env var to disable server maintenance mode
- Disable cloud maintenance mode


###### On Failure:​

- **No action taken. Job continues to next task**
- Server maintenance mode can be disabled manually by setting `HASURA_GRAPHQL_ENABLE_MAINTENANCE_MODE` env var to `false`
- Contact support if your project is in an unexpected state


##### Step 3.2: Check Metadata consistency​

###### Sub-tasks:​

- Check if Metadata is consistent


###### On Failure:​

- **No action taken. Job continues to next task**
- Check your project Metadata status on the Console *(Settings (⚙) -> Metadata status)* and attempt reloading metadata
if there is an unexpected inconsistency reported. Contact support if the inconsistency doesn't go away on metadata
reload.


#### 4. Project update complete​

Project update to `v2.0` is completed.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#introduction)
- [ What has changed? ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#what-has-changed)
- [ Estimated time needed for update ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#estimated-time-needed-for-update)
- [ Project availability during update ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#project-availability-during-update)
- [ Post-update steps ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#post-update-steps)
- [ Update process ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#update-process)
    - [ Update job sub-tasks ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#update-job-sub-tasks)
        - [ Step 1: Initializing ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-1-initializing)
            - [ Step 1.1: Validating ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-11-validating)

- [ Step 1.2: Enabling maintenance mode ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-12-enabling-maintenance-mode)

- [ Step 2: Updating project ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-2-updating-project)
    - [ Step 2.1: Migrating project metadata ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-21-migrating-project-metadata)

- [ Step 2.2: Creating v2.0 instance ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-22-creating-v20-instance)

- [ Step 2.3: Migrating pending events, async actions data ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-23-migrating-pending-events-async-actions-data)

- [ Step 2.4: Migrating processed events, async actions data ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#v2-update-migrate-invocation-logs)

- [ Step 3: Validating update ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-3-validating-update)
    - [ Step 3.1: Disabling maintenance mode ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#v2-update-disable-maintenance-mode)

- [ Step 3.2: Check Metadata consistency ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#v2-update-check-consistency)

- [ 4. Project update complete ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#4-project-update-complete)

- [ Step 1: Initializing ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-1-initializing)
    - [ Step 1.1: Validating ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-11-validating)

- [ Step 2: Updating project ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-2-updating-project)
    - [ Step 2.1: Migrating project metadata ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-21-migrating-project-metadata)

- [ Step 3: Validating update ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-3-validating-update)
    - [ Step 3.1: Disabling maintenance mode ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#v2-update-disable-maintenance-mode)

- [ Update job sub-tasks ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#update-job-sub-tasks)
    - [ Step 1: Initializing ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-1-initializing)
        - [ Step 1.1: Validating ](https://hasura.io/docs/latest/hasura-cloud/projects/move-project-v2/#sub-tasks-1/#step-11-validating)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)