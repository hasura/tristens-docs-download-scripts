# High-Availability Configuration

## Introduction​

Hasura Cloud supports high-availability (HA) configurations for Cloud Enterprise projects.

We configure each Cloud Enterprise project across different Availability Zones (AZs). In the event of an incident, our
global gateway will ensure traffic is not routed to the affected compute instances while the systems are
auto-recovering.

This redundancy and ability to identify problematic instances provides you with protection against data center power
outages, natural disasters, and other incidents while ensuring your project is performant, handles scaling, and, most
importantly, is available.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/high-availability/#introduction)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)