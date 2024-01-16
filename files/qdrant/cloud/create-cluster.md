# Create a cluster

This page shows you how to use the Qdrant Cloud Console to create a custom Qdrant Cloud cluster.

 **Prerequisite:** Please make sure you have provided billing information before creating a custom cluster.

1. Start in the **Clusters** section of the[ Cloud Dashboard ](https://cloud.qdrant.io).
2. Select **Clusters** and then click **+ Create** .
3. A window will open. Enter a cluster **Name** .
4. Currently, you can deploy to AWS or GCP. We are developing support for Azure.
5. Choose your data center region. If you have latency concerns or other topology-related requirements,[ let us know ](mailto:cloud@qdrant.io).
6. Configure RAM size for each node (1GB to 64GB).


Please read[ Capacity and Sizing ](../../cloud/capacity-sizing/)to make the right choice. If you need more capacity per node,[ let us know ](mailto:cloud@qdrant.io).

1. Choose the number of CPUs per node (0.5 core to 16 cores). The max/min number of CPUs is coupled to the chosen RAM size.
2. Select the number of nodes you want the cluster to be deployed on.


Each node is automatically attached with a disk space offering enough space for your data if you decide to put the metadata or even the index on the disk storage.

1. Click **Create** and wait for your cluster to be provisioned.


Your cluster will be reachable on port 443 and 6333 (Rest) and 6334 (gRPC).

Image: [ Embeddings ](https://qdrant.tech/docs/cloud/create-cluster.png)

Image: [ Embeddings ](https://qdrant.tech/docs/cloud/create-cluster.png)

## Next steps

You will need to connect to your new Qdrant Cloud cluster. Follow[ Authentication ](../../cloud/authentication/)to create one or more API keys.

Your new cluster is highly available and responsive to your application requirements and resource load. Read more in[ Cluster Scaling ](../../cloud/cluster-scaling/).

##### Table of contents

- [ Next steps ](https://qdrant.tech/documentation/cloud/create-cluster/#next-steps)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/create-cluster.md)
- [ 
 Create an Issue
 ](https://github.com/qdrant/landing_page/issues/new/choose)


#### Product

- [ 
Use cases
 ](https://qdrant.tech/use-cases/)
- [ 
Solutions
 ](https://qdrant.tech/solutions/)
- [ 
Benchmarks
 ](https://qdrant.tech/benchmarks/)
- [ 
Demos
 ](https://qdrant.tech/demo/)
- [ 
Pricing
 ](https://qdrant.tech/pricing/)


#### Community

- [ 
 
Github
 ](https://github.com/qdrant/qdrant)
- [ 
 
Discord
 ](https://qdrant.to/discord)
- [ 
 
Twitter
 ](https://qdrant.to/twitter)
- [ 
 
Newsletter
 ](https://qdrant.tech/subscribe/)
- [ 
 
Contact us
 ](https://qdrant.to/contact-us)


#### Company

- [ 
Jobs
 ](https://qdrant.join.com)
- [ 
Privacy Policy
 ](https://qdrant.tech/legal/privacy-policy/)
- [ 
Terms
 ](https://qdrant.tech/legal/terms_and_conditions/)
- [ 
Impressum
 ](https://qdrant.tech/legal/impressum/)
- [ 
Credits
 ](https://qdrant.tech/legal/credits/)


#### Latest Publications

#### Combining the precision of exact keyword search with NN-based ranking

#### Qdrant 1.7.0 brought a bunch of new features. Let's take a closer look at them!

#### Qdrant 1.6 brings recommendations strategies and more flexibility to the Recommendation API.

- [  ](https://github.com/qdrant/qdrant)
- [  ](https://qdrant.to/linkedin)
- [  ](https://qdrant.to/twitter)
- [  ](https://qdrant.to/discord)
- [  ](https://www.youtube.com/channel/UC6ftm8PwH1RU_LM1jwG0LQA)


##### Thanks for using Qdrant!

Subscribe to our e-mail newsletter if you want to be updated on new features and news regarding
Qdrant.

Like what we are doing? Consider giving us a ⭐[ on Github ](https://github.com/qdrant/qdrant).

We use cookies to learn more about you. At any time you can delete or block cookies through your browser settings.