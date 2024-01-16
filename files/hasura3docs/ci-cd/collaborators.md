# Collaborators

## Introduction​

Any Hasura DDN user can create a project and share it with other users. This allows you to collaborate with other users
by giving them access to your project's metadata and builds. A collaborator can also access the project in the Console
to view metrics, test the API, and more.

## Collaborator lifecycle​

### Create​

A collaborator can be invited from the Console. In `Settings` > `Governance` > `Collaborators` , choose `+ Invite a collaborator` :

Image: [ Invite a collaborator ](https://hasura.io/docs/3.0/assets/images/0.0.1_console_invite-collaborator-26f80ebf23b981ceaf230fc3d5f40c90.png)

Then, enter their email address and choose which role to assign them:

Image: [ Invite a collaborator ](https://hasura.io/docs/3.0/assets/images/0.0.1_console_assign-collaborator-role-e95171f315e0df528439be940275982e.png)

### Manage​

Currently, collaborators can only be added or deleted from a project. If you wish to change the access level for a user,
simply delete them and re-add them with the new role.

| Role | Description |
|---|---|
| Admin | Admins have full access to the project meaning that they can create and edit metadata; create and apply builds. |
| Read Metadata & Explore GraphQL | Collaborators with this role can view the project's metadata and explore the GraphQL API, but they cannot make changes to the project. |


Project owners

Please note, only project owners can delete a project. Ownership transfer is planned for a future release.

### Delete​

You can remove a collaborator from the Console by selecting `Remove` next to a user's name:

Image: [ Invite a collaborator ](https://hasura.io/docs/3.0/assets/images/0.0.1_console_remove-collaborator-c7344e7784531f02ccd17b5fb46878f6.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/ci-cd/collaborators/#introduction)
- [ Collaborator lifecycle ](https://hasura.io/docs/3.0/ci-cd/collaborators/#collaborator-lifecycle)
    - [ Create ](https://hasura.io/docs/3.0/ci-cd/collaborators/#create)

- [ Manage ](https://hasura.io/docs/3.0/ci-cd/collaborators/#manage)

- [ Delete ](https://hasura.io/docs/3.0/ci-cd/collaborators/#delete)
