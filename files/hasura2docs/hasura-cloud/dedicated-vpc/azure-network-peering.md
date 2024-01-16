# Azure VNet Peering

Your Dedicated VPC can be peered with other networks that you own on Azure. It will enable private connectivity to your
databases and other APIs from Hasura Cloud and you will not have to expose them publicly.

You can view all the requests and active peerings in the **Peering** tab.

## Create a peering request​

### Step 1: Create a new peering request​

To create a new peering request, click on the **Initiate Peering Request** button.

Image: [ Create Peering Request ](https://hasura.io/docs/assets/images/create-peering-request-162c074b1718097bd9c305351e16ea11.png)

Image: [ Peering Request ](https://hasura.io/docs/assets/images/azure-initiate-peering-28251d3401cc6433bcc2c63618c3fef6.png)

Fill in the form with the following details:

| Field | Description | Link |
|---|---|---|
| Display Name | The name you'll see in the Hasura Cloud dashboard. |  |
| Azure Tenant ID | Represents an organization in Azure Active Directory. You can find this value in the Azure Portal under Azure Active Directory | [ Azure Active Directory ](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview) |
| Azure Subscription ID | The unique identifier for your Azure subscription. You can find this in the Azure Portal on the Overview section of your Azure Virtual Network | [ your Azure Virtual Network ](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Network%2FvirtualNetworks) |
| Azure VNet resource group name | The identifier for the Azure resource group that the virtual network belongs to. You can find this in the Azure Portal on the Overview section of your Azure Virtual Network | [ Overview section of your Azure Virtual Network ](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Network%2FvirtualNetworks) |
| Azure VNet Name | The name of your Azure virtual network. You can find this in the Azure Portal on the Overview section of your Azure Virtual Network | [ Overview section of your Azure Virtual Network ](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Network%2FvirtualNetworks) |


Once you fill in these details and submit your request, you'll be taken to the next screen where you will have to grant
access to Hasura Cloud to initiate the peering.

### Step 2: Grant access to Hasura Cloud​

Image: [ Grant Access ](https://hasura.io/docs/assets/images/azure-grant-access-b291a9146d38812d466fb434e6523f54.png)

1. Go to the linked URL and approve. This creates a service principal on your Azure AD Tenant against our application. **This step does not grant us any access on your Azure Account yet.**
2. Run the command shown with your subscription ID to create a new role with only the required permissions. **Alternatively, you may skip this step and grant the default  Network Contributor  role in the next step.**
3. Verify your subscription ID, VNet resource group name and VNet Name in the command and run it to assign the role to
the service principal to grant Hasura access to initiate a VNet peering to the virtual network that was specified


Go to the linked URL and approve. This creates a service principal on your Azure AD Tenant against our application. **This step does not grant us any access on your Azure Account yet.** 

Run the command shown with your subscription ID to create a new role with only the required permissions. **Alternatively, you may skip this step and grant the default  Network Contributor  role in the next step.** 

`Network Contributor`

Verify your subscription ID, VNet resource group name and VNet Name in the command and run it to assign the role to
the service principal to grant Hasura access to initiate a VNet peering to the virtual network that was specified

Once this is done, we will initiate the VNet peering to the virtual network specified by you. The status of the peering
request will turn to `Active` when this is completed. You should be able to use private IP addresses as database URLs or
webhook URLs after this.

[ Reach out to support ](https://hasura.io/help/)if you face any issues.

If the status is shown as `Failed` , or if the status is stuck as `Request Pending` ,[ reach out to support ](https://hasura.io/help/).

### What did you think of this doc?

- [ Create a peering request ](https://hasura.io/docs/latest/hasura-cloud/dedicated-vpc/azure-network-peering/#create-a-peering-request)
    - [ Step 1: Create a new peering request ](https://hasura.io/docs/latest/hasura-cloud/dedicated-vpc/azure-network-peering/#step-1-create-a-new-peering-request)

- [ Step 2: Grant access to Hasura Cloud ](https://hasura.io/docs/latest/hasura-cloud/dedicated-vpc/azure-network-peering/#step-2-grant-access-to-hasura-cloud)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)