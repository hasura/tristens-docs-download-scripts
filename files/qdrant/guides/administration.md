# Administration

Qdrant exposes administration tools which enable to modify at runtime the behavior of a qdrant instance without changing its configuration manually.

## Locking

A locking API enables users to restrict the possible operations on a qdrant process.
It is important to mention that:

- The configuration is not persistent therefore it is necessary to lock again following a restart.
- Locking applies to a single node only. It is necessary to call lock on all the desired nodes in a distributed deployment setup.


Lock request sample:

```
POST /locks

{

    "error_message": "write is forbidden",

    "write": true

}

```

Write flags enables/disables write lock.
If the write lock is set to true, qdrant doesn’t allow creating new collections or adding new data to the existing storage.
However, deletion operations or updates are not forbidden under the write lock.
This feature enables administrators to prevent a qdrant process from using more disk space while permitting users to search and delete unnecessary data.

You can optionally provide the error message that should be used for error responses to users.

## Recovery mode

 *Available as of v1.2.0* 

Recovery mode can help in situations where Qdrant fails to start repeatedly.
When starting in recovery mode, Qdrant only loads collection metadata to prevent
going out of memory. This allows you to resolve out of memory situations, for
example, by deleting a collection. After resolving Qdrant can be restarted
normally to continue operation.

In recovery mode, collection operations are limited to[ deleting ](../../concepts/collections/#delete-collection)a
collection. That is because only collection metadata is loaded during recovery.

To enable recovery mode with the Qdrant Docker image you must set the
environment variable `QDRANT_ALLOW_RECOVERY_MODE=true` . The container will try
to start normally first, and restarts in recovery mode if initialisation fails
due to an out of memory error. This behavior is disabled by default.

If using a Qdrant binary, recovery mode can be enabled by setting a recovery
message in an environment variable, such as `QDRANT__STORAGE__RECOVERY_MODE="My recovery message"` .

##### Table of contents

- [ Locking ](https://qdrant.tech/documentation/guides/administration/#locking)
- [ Recovery mode ](https://qdrant.tech/documentation/guides/administration/#recovery-mode)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/administration.md)
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