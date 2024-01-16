# Dedicated VPC

## Introduction​

You can request a Dedicated VPC to be provisioned for you on Hasura Cloud. With Dedicated VPC, you will have better isolation in terms of:

- Compute for running projects on Hasura Cloud
- Network isolation
- A dedicated outbound IP address from Hasura Cloud
- The ability to connect your data sources and other endpoints over a private and secure network with VPC Peering
- Control over the version upgrades


Image: [ VPC Architecture ](https://hasura.io/docs/assets/images/vpc-architecture-afc954e333dab8064bae4dc4514aa86d.png)

Available on Hasura Cloud Enterprise

Dedicated VPC is only available as a part of the **Cloud Enterprise** plan. Peering requests are available for **AWS** and **GCP** .[ Contact Sales ](https://hasura.io/contact-us/)to know
more.

## Creating a VPC​

Once the feature is enabled for your account, you'll see a new tab on the dashboard called **VPCs** . All existing VPCs
can be found under VPCs tab on cloud dashboard. You can also initiate a request to create a new VPC. To request a new VPC, click on the **Create New
VPC** button on top. This will open a form with the following fields:

Image: [ VPC list ](https://hasura.io/docs/assets/images/view-vpc-list-be8f764b1113133c2b2fa6487508173b.png)

Enter the following details:

| Field | Description |
|---|---|
| Cloud Provider | The cloud provider where the VPC should be provisioned. |
| Region | The region where the VPC should be provisioned (note that projects will also be created in this region, too). |
| VPC Name | A display name for Hasura Dashboard. |
| VPC CIDR | A valid private IPV4 address range (/16) that should be used with this VPC. |


Examples of IP ranges

For example `172.16.0.0/16` , `10.10.0.0/16` are valid CIDR ranges. However, it cannot be `10.2.0.0/16` .

Additionally, your VPC CIDR cannot conflict with VPCs that you intend to peer with *this* VPC.

Once you submit the request, the VPC will appear as `Pending` . It will take about 10-20 minutes for your VPC to be
provisioned. Once it is provisioned, you will be able to see the VPC's details from your Cloud dashboard and create
peering and projects. You will receive an email when the VPC creation is successful.

If the provisioning fails, you'll see the VPC in a `Failed` state.[ Reach out to support ](https://hasura.io/help/)to
resolve this.

## Create projects within the VPC​

Once the VPC is provisioned, create a project by clicking on the **New Project** button in VPC details screen or[ get in touch with us ](https://hasura.io/help/)to migrate your existing Hasura Project to the VPC.

Image: [ Create VPC Project ](https://hasura.io/docs/assets/images/create-vpc-projects-cf258b00956a3a1e737d67e464631a57.png)

All projects within a VPC are listed under **Projects** .

Image: [ VPC Projects List ](https://hasura.io/docs/assets/images/vpc-projects-list-23ff72ada203d193f095eef5b61821ef.png)

If peering is not enabled, the project resides in a dedicated VPC on the Hasura side, but the traffic **from the project to the database** will be routed over the public internet.

## VPC Peering​

VPC Peering is necessary to establish a private and secure one-to-one connection from Hasura to your infrastructure. This includes databases, Remote Schemas, or Event / Schedueld Trigger endpoints running under your VPC.

Follow the Cloud provider-specific instruction to create VPC peering requests:

- [ AWS ](https://hasura.io/docs/latest/hasura-cloud/dedicated-vpc/aws-network-peering/)
- [ Azure ](https://hasura.io/docs/latest/hasura-cloud/dedicated-vpc/azure-network-peering/)
- [ GCP ](https://hasura.io/docs/latest/hasura-cloud/dedicated-vpc/gcp-network-peering/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/dedicated-vpc/#vpc-peering/#introduction)
- [ Creating a VPC ](https://hasura.io/docs/latest/hasura-cloud/dedicated-vpc/#vpc-peering/#creating-a-vpc)
- [ Create projects within the VPC ](https://hasura.io/docs/latest/hasura-cloud/dedicated-vpc/#vpc-peering/#create-projects-within-the-vpc)
- [ VPC Peering ](https://hasura.io/docs/latest/hasura-cloud/dedicated-vpc/#vpc-peering/#vpc-peering)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)