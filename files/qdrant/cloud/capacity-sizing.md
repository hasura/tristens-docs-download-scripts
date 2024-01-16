# Capacity and sizing

We have been asked a lot about the optimal cluster configuration to serve a number of vectors.
The only right answer is “It depends”.

It depends on a number of factors and options you can choose for your collections.

## Basic configuration

If you need to keep all vectors in memory for maximum performance, there is a very rough formula for estimating the needed memory size looks like this:

`memory_size = number_of_vectors * vector_dimension * 4 bytes * 1.5
`

Extra 50% is needed for metadata (indexes, point versions, etc.) as well as for temporary segments constructed during the optimization process.

If you need to have payloads along with the vectors, it is recommended to store it on the disc, and only keep[ indexed fields ](../../concepts/indexing/#payload-index)in RAM.
Read more about the payload storage in the[ Storage ](../../concepts/storage/#payload-storage)section.

## Storage focused configuration

If your priority is to serve large amount of vectors with an average search latency, it is recommended to configure[ mmap storage ](../../concepts/storage/#configuring-memmap-storage).
In this case vectors will be stored on the disc in memory-mapped files, and only the most frequently used vectors will be kept in RAM.

The amount of available RAM will significantly affect the performance of the search.
As a rule of thumb, if you keep 2 times less vectors in RAM, the search latency will be 2 times lower.

The speed of disks is also important.[ Let us know ](mailto:cloud@qdrant.io)if you have special requirements for a high-volume search.

## Sub-groups oriented configuration

If your use case assumes that the vectors are split into multiple collections or sub-groups based on payload values,
it is recommended to configure memory-map storage.
For example, if you serve search for multiple users, but each of them has an subset of vectors which they use independently.

In this scenatio only the active subset of vectors will be kept in RAM, which allows
the fast search for the most active and recent users.

In this case you can estimate required memory size as follows:

`memory_size = number_of_active_vectors * vector_dimension * 4 bytes * 1.5
`

##### Table of contents

- [ Basic configuration ](https://qdrant.tech/documentation/cloud/capacity-sizing/#basic-configuration)
- [ Storage focused configuration ](https://qdrant.tech/documentation/cloud/capacity-sizing/#storage-focused-configuration)
- [ Sub-groups oriented configuration ](https://qdrant.tech/documentation/cloud/capacity-sizing/#sub-groups-oriented-configuration)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/capacity-sizing.md)
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