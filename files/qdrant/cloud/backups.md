# Backups

There are situations where you need to restore your cluster because of application or system failure.
In most cases you will have a source of truth for your data in a regular database and would be able to reindex the data into your Qdrant vector search cluster.
However, encoding and uploading a big amount of data might require a long time.
For high availability critical projects we highly recommend relying on replication, which is always a better option, because it guarantees the proper cluster functionality as long as at least one replica is running.
For less critical use-cases you can make use of one of the available options.

## Automatic backups

The cloud platform offers an option for automatic backups of your clusters. It is possible to configure periodical file system level snapshots to restore a cluster from a hard copy.
On the cluster settings section you can choose how often a backup should be taken and how many copies you want to keep.

To restore a Qdrant cluster from backup, you can select a desired backup copy version and start the restore process.
Attention: during the restoring process the affected cluster will not be available because the cluster will be deleted and created from scratch from the backup copy.
Please also note, that if you changed the cluster setup after the copy was created, the new cluster will reset to the previous configuration.

## Self-service backups

Qdrant engine offers a snapshot API that allows to create a snapshot of a particular collection or even the whole storage.
Please refer to the[ snapshot documentation ](../../concepts/snapshots/)for details.

Here is how you can quickly snapshot and recover a collection:

1. Take a snapshot
    - In case of a single node cluster, simply call the snapshot endpoint on the exposed url.

- In case of a multi node cluster you’d need to take a snapshot on each node that the collection resides upon. To achieve this, you simply prepend `node-{num}-` to your cluster url and call the[ snapshot endpoint ](../../concepts/snapshots/#create-snapshot)on the individual hosts, starting with node 0 up to the number of nodes minus one.

- In the response you’ll get the name of the snapshot taken.

2. In case of a single node cluster, simply call the snapshot endpoint on the exposed url.

3. In case of a multi node cluster you’d need to take a snapshot on each node that the collection resides upon. To achieve this, you simply prepend `node-{num}-` to your cluster url and call the[ snapshot endpoint ](../../concepts/snapshots/#create-snapshot)on the individual hosts, starting with node 0 up to the number of nodes minus one.

4. In the response you’ll get the name of the snapshot taken.
5. Delete and recreate the collection.
6. Recover the snapshot
    - Call the[ recover endpoint ](../../concepts/snapshots/#recover-in-cluster-deployment)with location pointing to the snapshot file ( `file:///qdrant/snapshots/{collection_name}/{snapshot_file_name}` ) you got for each host.

7. Call the[ recover endpoint ](../../concepts/snapshots/#recover-in-cluster-deployment)with location pointing to the snapshot file ( `file:///qdrant/snapshots/{collection_name}/{snapshot_file_name}` ) you got for each host.


##### Table of contents

- [ Automatic backups ](https://qdrant.tech/documentation/cloud/backups/#automatic-backups)
- [ Self-service backups ](https://qdrant.tech/documentation/cloud/backups/#self-service-backups)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/backups.md)
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