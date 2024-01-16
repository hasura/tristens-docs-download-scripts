# Cluster scaling

The amount of data is always growing and at some point you might need to upgrade the capacity of your cluster.
There are different options for how it can be done.

## Vertical scaling

Vertical scaling, also known as vertical expansion, is the process of increasing the capacity of a cluster by adding more resources, such as memory, storage, or processing power.

You can start with a minimal cluster configuration of 2GB of RAM and resize it up to 64GB of RAM (or even more if desired) over the time step by step with the growing amount of data in your application.
If your cluster consists of several nodes each node will need to be scaled to the same size.
Please note that vertical cluster scaling will require a short downtime period to restart your cluster.
In order to avoid a downtime you can make use of data replication, which can be configured on the collection level.
Vertical scaling can be initiated on the cluster detail page via the button “scale up”.

## Horizontal scaling

Vertical scaling can be an effective way to improve the performance of a cluster and extend the capacity, but it has some limitations.
The main disadvantage of vertical scaling is that there are limits to how much a cluster can be expanded.
At some point, adding more resources to a cluster can become impractical or cost-prohibitive.
In such cases, horizontal scaling may be a more effective solution.
Horizontal scaling, also known as horizontal expansion, is the process of increasing the capacity of a cluster by adding more nodes and distributing the load and data among them.
The horizontal scaling at Qdrant starts on the collection level.
You have to choose the number of shards you want to distribute your collection around while creating the collection.
Please refer to the[ sharding documentation ](../../guides/distributed_deployment/#sharding)section for details.

Important: The number of shards means the maximum amount of nodes you can add to your cluster. In the beginning, all the shards can reside on one node.
With the growing amount of data you can add nodes to your cluster and move shards to the dedicated nodes using the[ cluster setup API ](../../guides/distributed_deployment/#cluster-scaling).

We will be glad to consult you on an optimal strategy for scaling.[ Let us know ](mailto:cloud@qdrant.io)your needs and decide together on a proper solution. We plan to introduce an auto-scaling functionality. Since it is one of most desired features, it has a high priority on our Cloud roadmap.

##### Table of contents

- [ Vertical scaling ](https://qdrant.tech/documentation/cloud/cluster-scaling/#vertical-scaling)
- [ Horizontal scaling ](https://qdrant.tech/documentation/cloud/cluster-scaling/#horizontal-scaling)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/cluster-scaling.md)
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