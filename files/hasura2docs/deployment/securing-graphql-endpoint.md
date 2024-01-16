# Secure the GraphQL Endpoint

To make sure that your GraphQL endpoint and the Hasura Console are not publicly accessible, you need to configure an
admin secret key.

Depending on your deployment method, follow one of these guides to configure an admin secret key, and prevent public
access to your GraphQL endpoint and the Hasura Console:

- Hasura Cloud projects have a randomly generated admin secret added by default at the time of creation.
- [ For Docker ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-secure)
- [ For Kubernetes ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#kubernetes-secure)
- [ For DigitalOcean ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#digital-ocean-secure)


Note

If you're looking at adding access control rules for your data to your GraphQL API then head to[ Authentication / access control ](https://hasura.io/docs/latest/auth/overview/). You can also find more information about[ Hasura security in general here ](https://hasura.io/docs/latest/security/overview/)and best practices[ here ](https://hasura.io/docs/latest/security/security-best-practices/).

### What did you think of this doc?

Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)