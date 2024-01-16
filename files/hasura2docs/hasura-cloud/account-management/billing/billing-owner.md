# Billing Owner

## Introduction​

You can invite a billing owner to take responsibility of the project's invoicing. The `Collaborators` tab displays the
current user who is in charge of project billing as well as the user who has been invited to take on the billing owner
responsibility.

## Invite a billing owner​

### Invite a new collaborator as billing owner​

Click `Invite a Collaborator` to invite a new collaborator as a billing owner by their email.

Image: [ Collaborators tab ](https://hasura.io/docs/assets/images/collab-view-07c76ae25ec8ec6b6fe40e6f4cd55098.png)

After entering their email, select `Admin` as the collaborator type, then select the `Billing Owner` privilege.

Image: [ User Collaborator with Billing Owner Privilege ](https://hasura.io/docs/assets/images/invite-bm-collab-0d738bde8172f258876d2642705a28c3.png)

Note

Only a single invitation can exist at a time for a billing owner. If an invitation already exists for a billing owner,
please revoke that invitation and then invite another user.

### Invite an existing collaborator to become billing owner​

Click on the collaborator you want to invite as a billing owner.

Under the user's existing collaborator type, check the `Billing Owner` privilege and click `Update` .

Image: [ Add Billing Owner Privilege ](https://hasura.io/docs/assets/images/add-bm-privilege-0ae4f06a68dd39b2f60f11ef01373544.png)

## Accept / reject billing owner invitation​

You can see the projects that you have been invited to handle billing for on the project listing page and choose to
either accept or reject them.

Image: [ Projects invited to handle billing for ](https://hasura.io/docs/assets/images/project-bm-invitation-bb13180017606925ef85a465b292fe45.png)

## Remove a billing owner​

### Remove billing owner completely as a collaborator​

Only the owner of a project can remove a collaborator with billing owner privilege and take back the responsibility of
billing for their project.

To remove a billing owner, click on the billing owner collaborator and then click on the remove icon on the top right:

Image: [ Remove billing owner collaborator ](https://hasura.io/docs/assets/images/remove-bm-87ba43d148408a6d40ce6d9ccb74ea64.png)

Note

If the billing owner collaborator has other privileges apart from `Billing Owner` , following the above steps will remove
all those privileges too. In case you only want to remove the `Billing Owner` privilege, follow the steps under[ Remove Billing Owner Privilege ](https://hasura.io/docs/latest/hasura-cloud/account-management/billing/billing-owner/#remove_bm_privilege).

### Remove only billing owner privilege for a collaborator​

Only the owner of a project can remove a collaborator's billing owner privilege and take back the responsibility of
billing for their project.

To remove a collaborator's `Billing Owner` privilege, click on the billing owner collaborator.

Image: [ Click billing owner collaborator ](https://hasura.io/docs/assets/images/click-bm-collab-94921493346c758e739a75fc7452bf70.png)

Remove the `Billing Owner` privilege for that user and click `Update` .

Image: [ Remove billing owner privilege ](https://hasura.io/docs/assets/images/remove-bm-privilege-c625fb5cad9bb7811a8f97e751cd1a5e.png)

## Resend billing owner invitation​

If you have invited a billing owner, you can click on the `Invited` button to resend the invitation.

Image: [ Resend billing owner invitation ](https://hasura.io/docs/assets/images/resend-bm-invitation-c2ac7ffa6eea20bb9e79feec21b20199.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/account-management/billing/billing-owner/#introduction)
- [ Invite a billing owner ](https://hasura.io/docs/latest/hasura-cloud/account-management/billing/billing-owner/#invite-a-billing-owner)
    - [ Invite a new collaborator as billing owner ](https://hasura.io/docs/latest/hasura-cloud/account-management/billing/billing-owner/#invite-a-new-collaborator-as-billing-owner)

- [ Invite an existing collaborator to become billing owner ](https://hasura.io/docs/latest/hasura-cloud/account-management/billing/billing-owner/#invite-an-existing-collaborator-to-become-billing-owner)
- [ Accept / reject billing owner invitation ](https://hasura.io/docs/latest/hasura-cloud/account-management/billing/billing-owner/#accept--reject-billing-owner-invitation)
- [ Remove a billing owner ](https://hasura.io/docs/latest/hasura-cloud/account-management/billing/billing-owner/#remove-a-billing-owner)
    - [ Remove billing owner completely as a collaborator ](https://hasura.io/docs/latest/hasura-cloud/account-management/billing/billing-owner/#remove-billing-owner-completely-as-a-collaborator)

- [ Remove only billing owner privilege for a collaborator ](https://hasura.io/docs/latest/hasura-cloud/account-management/billing/billing-owner/#remove_bm_privilege)
- [ Resend billing owner invitation ](https://hasura.io/docs/latest/hasura-cloud/account-management/billing/billing-owner/#resend-billing-owner-invitation)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)