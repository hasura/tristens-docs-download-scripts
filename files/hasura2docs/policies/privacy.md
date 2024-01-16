# Data Privacy and Access at Hasura

## Introduction​

We take privacy and security very seriously at Hasura and take all measures to protect your data. This document outlines
the measures we take to ensure that your data is secure and private.

## Environment variables​

On Hasura Cloud, environment variables are stored in a[ Hashicorp Vault ](https://www.vaultproject.io/)instance as
secrets which are not directly accessible to Hasura staff. It is strongly recommended to keep all secrets in
environment variables rather than string literals which will be accessible in your Hasura Metadata.

## Data storage​

Hasura's architecture necessitates connecting to your databases in order to serve queries to your applications and
end users. While your data passes through Hasura's systems, it remains exclusively in-memory, solely for query
processing purposes. No data persistence occurs within Hasura's systems. The only exception is when caching is
enabled for a query; in this case, query responses are cached within in-memory Redis instances, subject to a specified
TTL ([ refer to caching documentation ](https://hasura.io/docs/latest/caching/overview/)).

## Metadata security​

At Hasura, we take comprehensive measures to ensure the protection of your Metadata. Our practices are focused on
keeping sensitive information, such as schema definitions, access control rules, and relationships, secure from
unauthorized access and tampering. To achieve this, we employ strong encryption techniques for Metadata storage,
both at rest and during transmission.

## Log security​

Our logging practices are designed to maintain the highest level of security and data privacy. As part of our
commitment, we do not log query responses in any system logs, preventing unauthorized access or data leakage.

Additionally, to further safeguard your information, we do not log passwords.

## SOC Type 2 Compliance​

We are SOC Type 2 compliant. This means that we have undergone a rigorous audit by a third party to ensure that we have
the appropriate controls in place to protect your data. You can read more about our SOC Type 2 compliance[ here ](https://hasura.io/blog/announcement-hasura-cloud-achieves-soc2-type-2-certification/).

## GDPR and HIPAA Compliance​

We are[ GDPR ](https://gdpr-info.eu/)and[ HIPAA ](https://www.cdc.gov/phlp/publications/topic/hipaa.html)compliant.

## Hasura Privacy Policy​

Please see out[ privacy policy here ](https://hasura.io/legal/hasura-privacy-policy/)which details how we handle your
data.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/policies/privacy/#introduction)
- [ Environment variables ](https://hasura.io/docs/latest/policies/privacy/#environment-variables)
- [ Data storage ](https://hasura.io/docs/latest/policies/privacy/#data-storage)
- [ Metadata security ](https://hasura.io/docs/latest/policies/privacy/#metadata-security)
- [ Log security ](https://hasura.io/docs/latest/policies/privacy/#log-security)
- [ SOC Type 2 Compliance ](https://hasura.io/docs/latest/policies/privacy/#soc-type-2-compliance)
- [ GDPR and HIPAA Compliance ](https://hasura.io/docs/latest/policies/privacy/#gdpr-and-hipaa-compliance)
- [ Hasura Privacy Policy ](https://hasura.io/docs/latest/policies/privacy/#hasura-privacy-policy)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)