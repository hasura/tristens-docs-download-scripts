# Try Hasura Enterprise Edition

## Introduction​

Trying and evaluating Hasura Enterprise features with your current Hasura setup is now easier and self-serve. Starting
with Hasura GraphQL Engine version `v2.23.0` , you can get started with your 30-day Enterprise Edition Trial in **under a minute** !

During your trial period you will have access to all the[ Enterprise Edition features ](https://hasura.io/docs/latest/enterprise/overview/)to
help you successfully evaluate Hasura Enterprise for your use case.

Note

- The `hasura/graphql-engine` image includes both open-source and proprietary components. The open-source portions are
licensed under the[ Apache License, Version 2.0 ](https://www.apache.org/licenses/LICENSE-2.0). The proprietary
components include features for Hasura Enterprise and are enabled with a license provided by Hasura. If you would like
to use an image with only the open source components, please use Docker images on[ this page ](https://hub.docker.com/r/hasura/graphql-engine/tags?page=1&name=-ce)that contain `-ce` . (example: `hasura/graphql-engine:2.23-ce` )
- Use of a Hasura Enterprise Edition Trial is only recommended for evaluation during the trial period and not for
production use.
- Supported in `v2.23.0` onwards.
- Your Hasura instance must be connected to the internet to use the Hasura Enterprise Edition Trial. If you are running Hasura in an airgap environment, please[ contact Hasura Sales ](mailto:sales@hasura.io)to get a license key for trying Hasura Enterprise.


The `hasura/graphql-engine` image includes both open-source and proprietary components. The open-source portions are
licensed under the[ Apache License, Version 2.0 ](https://www.apache.org/licenses/LICENSE-2.0). The proprietary
components include features for Hasura Enterprise and are enabled with a license provided by Hasura. If you would like
to use an image with only the open source components, please use Docker images on[ this page ](https://hub.docker.com/r/hasura/graphql-engine/tags?page=1&name=-ce)that contain `-ce` . (example: `hasura/graphql-engine:2.23-ce` )

Use of a Hasura Enterprise Edition Trial is only recommended for evaluation during the trial period and not for
production use.

Supported in `v2.23.0` onwards.

Your Hasura instance must be connected to the internet to use the Hasura Enterprise Edition Trial. If you are running Hasura in an airgap environment, please[ contact Hasura Sales ](mailto:sales@hasura.io)to get a license key for trying Hasura Enterprise.

## Activate your Enterprise Edition Trial​

### Step 1. Run Hasura​

You can run Hasura instances in a container environment of your choice. Please follow this[ guide for getting started ](https://hasura.io/docs/latest/enterprise/getting-started/quickstart-docker/), which describes how to install Hasura GraphQL Engine using
Docker.

If you are already running Hasura inside a Docker container with open-source features, then you just need to change the
Docker container tag to `v2.23.0` or above and then redeploy the container.

Please make sure that your `docker-compose.yaml` does not have the `HASURA_GRAPHQL_EE_LICENSE_KEY` environment variable set. If you already have a license key, you can try Hasura Enterprise directly by following instructions[ here ](https://hasura.io/docs/latest/enterprise/upgrade-ce-to-ee/).

### Step 2. Register for your 30-day free Trial​

Once Hasura is running, you can register for an Enterprise Edition Trial using the Hasura Console. In the Hasura
Console, click on the `Enterprise` button in the top right and fill out the registration form.

Image: [ Enterprise Edition Trial register button ](https://hasura.io/docs/assets/images/Trials_Register_Button-21f7c94a1f16bc85ed93899268a16ef2.png)

Filling out this form will automatically create a Hasura Cloud account. **If you already have an existing Hasura Cloud
account, please use the same credentials in the form** . You can use the same Hasura Cloud account to centrally manage
all your enterprise licenses (this feature to be added soon).

Please see the[ FAQ ](https://hasura.io/docs/latest/enterprise/try-hasura-enterprise-edition/#frequently-asked-questions)section in case you are facing issues with registration.

Image: [ Enterprise Edition Trial Registration Form ](https://hasura.io/docs/assets/images/Trials_Registration_form-7c76c7471ed347f92a1957567c3def69.png)

Image: [ Enterprise Edition Trial Success ](https://hasura.io/docs/assets/images/Trials_Succeeded-494b20ad9ed7d869ac0b63e93edba834.png)

### Step 3. Restart your container​

Once you have registered for the Enterprise Edition Trial, restart your Hasura GraphQL Engine instance. This is
required only once.

Example:

`docker-compose  restart graphql-engine`

Now, refresh the Hasura Console and you're all set to explore Hasura Enterprise Edition 🎉

Image: [ Enterprise Edition Trial Activated view ](https://hasura.io/docs/assets/images/Trials_Activated-3c2692381a415fbf9fde07fbaa3a06bc.png)

To view all Enterprise Edition features you've just enabled, click the `EE` button in the navigation bar.
Conveniently, this also displays the number of days remaining in your trial period.

Image: [ EE Trial Benefits View ](https://hasura.io/docs/assets/images/Trials_EE_Benefits-5afa81e01ac2b6b7fb07aef008b6c6b9.png)

The license information can also be found in the `Settings` view.

Image: [ EE License view ](https://hasura.io/docs/assets/images/Trials_View_State-80109410ef4e15ab985e1e9a71997eeb.png)

## Frequently Asked Questions​

### I registered for the trial but I can't see the Enterprise Edition features. Where are they?​

If you have already registered, please restart your Docker container once.

### I restarted my Hasura Docker container but I still can't see Enterprise Edition features. What should I do?​

Please try registering for the trial again by filling out the registration form, in case previous registration attempt
failed due to some reason. If the issue persists, please[ contact us ](https://hasura.io/contact-us-eetrial)and we'll be
happy to help you.

### I need some more time to explore Enterprise Edition; how can I extend my Trial license?​

Please[ contact us ](https://hasura.io/contact-us-eetrial)and our team will assist you.

### Will the Enterprise Edition Trial work for a multiple-replica setup of Hasura?​

Yes, you would need to register once, and all the replicas of your Hasura backed by same metadata database will have
Enterprise Edition features enabled.

### I am already in an Enterprise Edition evaluation period; how can I continue evaluation with a different Hasura​

environment?

In your new Hasura instance, open the Console and click on `Enterprise` . Then, select `Activate Existing License` .
Please enter the same credentials you used for the initial Trial registration. Restart Hasura and now the same Trial
license will be applied to this new instance too.

### Why do I need to enter a password to register for a Trial?​

As you register for the Enterprise Edition Trial, we use the email and password to create a Hasura Cloud account. This
will be used for verification and also help manage your Enterprise licenses in the future (this feature to be added
soon).

### I forgot the password with which I registered; how do I enable the Trial now?​

Please head to[ Hasura Cloud ](https://cloud.hasura.io/login)and click on 'Forgot?' to recover your password. Please use
the updated password to register for the Enterprise Edition Trial.

### I use an OAuth login on Hasura Cloud; how do I register for an Enterprise Edition Trial?​

You can register for a Trial with same email, but a new password. Your Hasura Cloud account will be updated with the new
password.

### I use SSO on Hasura Cloud to login; how do I enable an Enterprise Edition Trial?​

Please register with a different email or[ contact us ](https://hasura.io/contact-us-eetrial)if you want to continue
with the same email. We will add support for SSO users in future.

### What kind of data does Hasura collect during an Enterprise Edition Trial?​

[ This guide ](https://hasura.io/docs/latest/policies/telemetry/)elaborates on the data collected by Hasura in line with the[ Hasura privacy policy ](https://hasura.io/legal/hasura-privacy-policy/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/enterprise/try-hasura-enterprise-edition/#introduction)
- [ Activate your Enterprise Edition Trial ](https://hasura.io/docs/latest/enterprise/try-hasura-enterprise-edition/#activate-your-enterprise-edition-trial)
- [ Frequently Asked Questions ](https://hasura.io/docs/latest/enterprise/try-hasura-enterprise-edition/#frequently-asked-questions)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)