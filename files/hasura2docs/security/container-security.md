# Container Security

## Non-root user and group​

By default, all `hasura/graphql-engine` images come with a non-root user and group named `hasura` . Both the user ID
(UID) and group ID (GID) for this non-root user are `1001` .

We strongly recommend using this non-root user and group to run the `graphql-engine` container. This practice enhances
system security and mitigates potential risks in the event of a future container escape vulnerability.

If you're using docker-compose, this can be done by implementing the `user` field like this:

```
version :   '3.6'
services :
   graphql-engine :
     image :  hasura/graphql - engine : v2.30.0
     user :  1001 : 1001
     ports :
       -   '8080:8080'
```

Existing UID and GID

Since the non-root UID and GID is `1001` , you will need to make sure that the host machine in which the container is
running does not have an existing UID and GID that are `1001` . This will ensure that even if a container escape happens, the
attacker would not be able to do anything useful in the system.

### What did you think of this doc?

- [ Non-root user and group ](https://hasura.io/docs/latest/security/container-security/#non-root-user-and-group)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759811/main-web/Group_11455_3_azgk7w.png)

### Securing your API with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)