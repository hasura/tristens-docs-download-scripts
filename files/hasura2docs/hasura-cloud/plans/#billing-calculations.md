# Plans and Pricing

## Introduction​

[ Hasura Cloud ](https://cloud.hasura.io)offers three plans: Hasura Cloud Free, Hasura Cloud Professional, and Hasura
Cloud Enterprise.

Hasura Cloud billing is based on the consumption of resources. For paid plans, you can either pay as you go monthly in
arrears with the Cloud Professional Plan, or make an annual commitment with an upfront payment for the usage with the
Cloud Enterprise Plan.

Below, you'll find a guide to help you choose the right plan for your use case, an overview of each plan, and details on
how we calculate billing. Check out our[ pricing FAQ ](https://hasura.io/pricing#faq)for common questions.

## Choose the right plan​

To help you choose the right plan for your use case, this section describes the application types and use cases that are
best suited for each plan. For a full feature comparison list, see the[ pricing page ](https://hasura.io/pricing). To
better understand how we calculate billing, see the[ billing calculation ](https://hasura.io/docs/latest/hasura-cloud/plans/#billing-calculations/#billing-calculations)section.

| Application type | Plan | Features |
|---|---|---|
|     - Testing, starter, and hobby projects
 | : If you're interested in trying out Hasura Cloud, you can start with the Cloud Free plan. It's completely free to use, requires no credit card, and gives you a fully-managed GraphQL API - with some of our best features - right out of the box. |     - Instant GraphQL and REST APIs with role-based authorization
    - Premium connectors, including Snowflake, SQL Server, and more
    - Up to three Projects
    - Up to two data connectors
    - Up to 3M API requests/month
    - 100 MB of data passthrough per month
 |
|     - Low-scale production APIs
 | : If you're building a low-scale production API, you can start with the Cloud Professional plan. It's a pay-as-you-go monthly subscription plan. You only pay for your consumption every month. Consumption is calculated based on the[ number of hours ](https://hasura.io/docs/latest/hasura-cloud/plans/#billing-calculations)each Project runs and the amount of data passthrough. |     - Unlimited databases per project
    - Unlimited data passthrough at $0.13/GB
    - Up to 6M API requests/month
    - Performance tuning (query caching and read replicas)
    - Observability data and integrations
    - Core security features (for e.g., role-based API limits and allow lists)
 |
|     - High-scale production APIs
    - Mission-critical APIs
    - APIs with security and compliance needs
 | : For APIs that are mission-critical, require high-scale, and have security and compliance needs, we have the Cloud Enterprise plan, which offers the ability to commit to a minimum spending amount over a minimum 12-month commitment period. You can view the total amount of accrued usage during the commitment term and the amount of committed spending left in your account. You can renew your commitment if your commitment is depleted before the expiry of the commitment period.

Talk to a Hasura[ sales representative ](mailto:sales@hasura.io)to discuss your specific use case and the pricing. |     - Unlimited databases per project
    - Unlimited data passthrough at $0.13/GB
    - Unlimited API requests/month
    - Dedicated infrastructure and VPC peering
    - Unlimited query caching and read replicas
    - Advanced security (e.g., SSO) and compliance
    - Expert 24x7 technical support, with customizable SLAs
 |


- Testing, starter, and hobby projects


- Instant GraphQL and REST APIs with role-based authorization
- Premium connectors, including Snowflake, SQL Server, and more
- Up to three Projects
- Up to two data connectors
- Up to 3M API requests/month
- 100 MB of data passthrough per month


- Low-scale production APIs


- Unlimited databases per project
- Unlimited data passthrough at $0.13/GB
- Up to 6M API requests/month
- Performance tuning (query caching and read replicas)
- Observability data and integrations
- Core security features (for e.g., role-based API limits and allow lists)


- High-scale production APIs
- Mission-critical APIs
- APIs with security and compliance needs


- Unlimited databases per project
- Unlimited data passthrough at $0.13/GB
- Unlimited API requests/month
- Dedicated infrastructure and VPC peering
- Unlimited query caching and read replicas
- Advanced security (e.g., SSO) and compliance
- Expert 24x7 technical support, with customizable SLAs


## Billing calculations for Hasura Cloud Professional​

For Hasura Cloud Professional we calculate billing, using the following categories, per Project:

- Types of databases connected to the Project
- Data passthrough


Hasura Cloud Professional is billed for the number of hours each Project runs and the amount of data passthrough. The
price depends on the type(s) of database(s) connected to the Project. If a Project uses a generic Postgres database and
a premium database, **you are billed only once for a premium database no matter how many or how different types you
add** .

| Database Type | Rate |
|---|---|
| Generic Postgres | $1.50/active-hr |
| Snowflake | $3.00/active-hr |
| BigQuery | $3.00/active-hr |
| Athena | $3.00/active-hr |
| MSSQL | $3.00/active-hr |
| CockroachDB | $3.00/active-hr |
| Google AlloyDB | $3.00/active-hr |
| Citus / Hyperscale | $3.00/active-hr |
| MySQL | $3.00/active-hr |
| Oracle | $3.00/active-hr |
| MariaDB | $3.00/active-hr |


Active-hr

An hour is considered an active hour when an activity is attributed to a Project during that hour. A few examples of
activity are:

- any GraphQL, REST, Metadata API request
- an active subscription
- an open websocket connection
- an event-triggered activity


Projects without databases

A Project without a connected database is billed at $1.50/active-hr.

#### Data passthrough​

Hasura Cloud meters data passing through it to external services, including request data that is sent to upstream
services (e.g., databases) and response data sent to downstream services (e.g., web apps) at a rate of $0.13/GB.

You will be billed based on this volume of data which passes through your Project on Hasura Cloud every month.

#### Example Calculation​

Assuming thirty days in the month, you start with one Project with a Postgres data connector for the first twenty days
of the Project and add Snowflake data connector for the remaining 10 days.

Assuming your Project is active for 8 hrs a day

 `20 days * 8 hrs/day * $1.50/hr = $240` 

 `10 days * 8 hrs/day * $3.00/hr = $240` 

Let's assume the data passthrough for the entire month is 100 GB:

 `100 GB * $0.13/GB = $13 Total` 

The total cost for the month is $493.

## Usage Reports​

### Hasura Cloud Professional usage reports​

You can find the usage reports for your Hasura Cloud Professional plan in the Hasura Cloud dashboard. From the `Projects` page, locate the project you want to view the usage report for, click the `Settings` icon on the top right of
the project's card, then select `Usage` from the sidenav.

Image: [ Professional Plan Usage Reports Navigation ](https://hasura.io/docs/assets/images/billing-usage-professional-76cc45534d8101d9245bf5e3c921849e.png)

### Hasura Cloud Enterprise usage reports​

From the Hasura Cloud dashboard, click on `Enterprise` in the left sidebar. You will be able to see the usage reports
for your Hasura Cloud Enterprise plan.

Image: [ Cloud Enterprise Plan Usage Reports Navigation ](https://hasura.io/docs/assets/images/billing-usage-EE-d1cb046d115db2fa1938bab4e18a173b.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/hasura-cloud/plans/#billing-calculations/#introduction)
- [ Choose the right plan ](https://hasura.io/docs/latest/hasura-cloud/plans/#billing-calculations/#choose-the-right-plan)
- [ Billing calculations for Hasura Cloud Professional ](https://hasura.io/docs/latest/hasura-cloud/plans/#billing-calculations/#billing-calculations)
- [ Usage Reports ](https://hasura.io/docs/latest/hasura-cloud/plans/#billing-calculations/#usage-reports)
    - [ Hasura Cloud Professional usage reports ](https://hasura.io/docs/latest/hasura-cloud/plans/#billing-calculations/#hasura-cloud-professional-usage-reports)

- [ Hasura Cloud Enterprise usage reports ](https://hasura.io/docs/latest/hasura-cloud/plans/#billing-calculations/#hasura-cloud-enterprise-usage-reports)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)