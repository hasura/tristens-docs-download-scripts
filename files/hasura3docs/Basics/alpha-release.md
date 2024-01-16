# The Alpha Release

## What is the Alpha release?​

The Alpha release is the first public rollout of the Hasura Data Delivery Network geared towards a limited use-case set.

This is an opportunity for our engaged community to have early access to DDN and explore this significant update to the
platform. We encourage our users to be true design partners providing feedback and suggestions as we take the platform
towards general availability. We invite community members to let us know their thoughts and questions[ here ](https://discord.com/channels/407792526867693568/1164275846538874900)and engage with our product and engineering
teams. To enable frictionless evaluation DDN, Alpha is completely free for 90 days for all Alpha users. We are rapidly
evolving the platform and will keep you updated with the progress.

Please note that there could be some breaking changes introduced in the Alpha version, however we will make sure not to
introduce any drastic changes. In most instances, it would require you to create new builds without the need for
refactoring the entire metadata. We will give you advance notice before any such changes are rolled out in production.
Also, customer support will be limited during this phase and most of the communication wil happen via direct
conversation with the Hasura team via discord channels, user groups, emails, and community calls.

## What is available to use in the Alpha release?​

The Alpha release offers an initial look into the power of Hasura DDN:

### API Authoring​

- **VS Code Extension:** [ A VS Code extension ](https://marketplace.visualstudio.com/items?itemName=HasuraHQ.hasura)for
Hasura DDN that provides a rich editing experience for OpenDD metadata.
- **LSP:** Language Server Protocol - a parser and validator for the OpenDD Specification that powers the VS Code
extension.
- **Hasura Console:** [ A UI ](https://console.hasura.io)for creating projects, viewing metadata, relationships and
running API queries.


### GraphQL API Features​

- **Queries:** Other GraphQL operations coming soon.
- [ Mutations: via Commands ](https://hasura.io/docs/3.0/data-domain-modeling/commands/)([ CQRS pattern ](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)). True database inserts, updates,
and deletes via the respective data connectors are coming soon.
- [ Permissions: ](https://hasura.io/docs/3.0/auth/authorization/index/)An OpenDD metadata object in Hasura DDN that defines the access
control or authorization rules on models and commands.
- [ Relationships: ](https://hasura.io/docs/3.0/data-domain-modeling/relationships/)An OpenDD metadata object in Hasura DDN that defines the
relationship between two models or between a model and a command. This facilitates data interconnection
- [ Relay: ](https://hasura.io/docs/3.0/data-domain-modeling/global-id/)The Relay global ID enables fetching any object directly, regardless
of what kind of object it is.


### CI/CD​

- [ Hasura3 CLI: ](https://hasura.io/docs/3.0/cli/overview/)A revamped Command-Line Interface for improved developer interactions.
- **Secure Connect:** A feature in Hasura DDN that creates secure tunnels to connect with local resources, aiding local
development while ensuring data security. It requires a local daemon to be run via the CLI.
- [ Builds: ](https://hasura.io/docs/3.0/ci-cd/builds/)Each metadata change in Hasura DDN represents an immutable build. Every build has a
unique GraphQL Endpoint that can be tested independently.
- [ Projects: ](https://hasura.io/docs/3.0/ci-cd/projects/)Builds are tied to projects and there is a one-to-many mapping between projects
and builds
- [ Collaborators: ](https://hasura.io/docs/3.0/ci-cd/collaborators/)A way to work together in Cloud projects.
- [ Subgraphs: ](https://hasura.io/docs/3.0/ci-cd/subgraphs/)A system to modularize metadata for better team collaboration.
- [ Secrets: ](https://hasura.io/docs/3.0/ci-cd/secrets/)a means of storing sensitive information as key-value pairs that you don't want
exposed in your metadata.


### Business Logic with Typescript​

[ Typescript with Deno ](https://github.com/hasura/ndc-typescript-deno).

### Native Data Connectors and SDKs​

- **Native Data Connector SDKs:** [ Rust ](https://github.com/hasura/ndc-hub#rust-sdk)and[ Typescript ](https://github.com/hasura/ndc-sdk-typescript)
- **Official Connectors:** [ Postgres ](https://github.com/hasura/ndc-postgres),[ Clickhouse ](https://github.com/hasura/ndc-clickhouse),[ Sendgrid ](https://github.com/hasura/ndc-sendgrid),


 **Native Data Connector SDKs:** [ Rust ](https://github.com/hasura/ndc-hub#rust-sdk)and[ Typescript ](https://github.com/hasura/ndc-sdk-typescript)

 **Official Connectors:** [ Postgres ](https://github.com/hasura/ndc-postgres),[ Clickhouse ](https://github.com/hasura/ndc-clickhouse),[ Sendgrid ](https://github.com/hasura/ndc-sendgrid),

## What are the known limitations of the Alpha release?​

Being the first glimpse into Hasura DDN, the Alpha release comes with some limitations:

- **Mutations, Event Triggers and Subscriptions:** Coming soon! Mutations and event triggers can be performed via[ Commands ](https://hasura.io/docs/3.0/data-domain-modeling/commands/)in the alpha release though. Please do check commands and Typescript
Connector out for business logic, mutations and event triggers.
- **Compatibility:** While the default GraphQL schema is compatible with Hasura v2, some advanced v2 features might not
be supported.
- **Migration Tools:** Complete migration tools from Hasura v2 to DDN are in development.
- **Data Connectors:** Not all previously supported data sources have connectors yet; however, the[ NDC SDKs ](https://hasura.io/docs/3.0/basics/alpha-release/#sdks-and-connectors)will soon bridge this gap.


Check out the[ FAQ section ](https://hasura.io/docs/3.0/faq/)for more information on the major changes from v2.

## What is the timeline for upcoming releases?​

The specific timeline for Hasura DDN Beta and General Availability will vary based on feature development and
improvements. We're dedicated to delivering robust and trustworthy releases on a periodic basis with detailed changelog
on the new capabilities. For the most current updates, always refer to our official announcements and release notes.

Thank you for being a part of this exciting journey with Hasura DDN. Your participation drives our innovation, and
together, we'll reshape the future of modern application development.

## Moving to a supergraph architecture​

- Before Hasura DDN
- After Hasura DDN


### Before Hasura DDN​

Businesses, while modernizing, face challenges in delivering digital experiences quickly and cost-effectively. Product
development teams are often bottle-necked, waiting on backend teams for secure and efficient data access. This results
in manually implementing custom APIs, microservice sprawl, orchestrating security policies, wasting time and stifling
innovation.

Image: [ Hasura DDN basics before diagram ](https://hasura.io/docs/3.0/assets/images/hasura-ddn-basics-before-diagram-9649df015481d611759ac1020403fcd5.png)

### After Hasura DDN​

In moving to a supergraph architecture with Hasura, organizations can significantly minimize the complexity of their
data infrastructure. By connecting directly to data sources via Hasura DDN and native data connectors (NDCs), the
requirement for hand-crafted APIs and microservices is vastly reduced and collaboration is enhanced with backend teams
contributing independently.

Data can be securely exposed and interconnected, allowing for the creation of a single, unified data graph, able to be
deployed for wide-ranging requirements from client apps to public APIs on globally distributed infrastructure for
minimal latency, scalability, and unwavering reliability.

Image: [ Hasura DDN basics after diagram ](https://hasura.io/docs/3.0/assets/images/hasura-ddn-basics-after-diagram-15e580dcf6aee734d9bb16a41d503b98.png)

### What did you think of this doc?

- [ What is the Alpha release? ](https://hasura.io/docs/3.0/basics/alpha-release/#what-is-the-alpha-release)
- [ What is available to use in the Alpha release? ](https://hasura.io/docs/3.0/basics/alpha-release/#what-is-available-to-use-in-the-alpha-release)
    - [ API Authoring ](https://hasura.io/docs/3.0/basics/alpha-release/#api-authoring)

- [ GraphQL API Features ](https://hasura.io/docs/3.0/basics/alpha-release/#graphql-api-features)

- [ CI/CD ](https://hasura.io/docs/3.0/basics/alpha-release/#cicd)

- [ Business Logic with Typescript ](https://hasura.io/docs/3.0/basics/alpha-release/#business-logic-with-typescript)

- [ Native Data Connectors and SDKs ](https://hasura.io/docs/3.0/basics/alpha-release/#sdks-and-connectors)
- [ What are the known limitations of the Alpha release? ](https://hasura.io/docs/3.0/basics/alpha-release/#what-are-the-known-limitations-of-the-alpha-release)
- [ What is the timeline for upcoming releases? ](https://hasura.io/docs/3.0/basics/alpha-release/#what-is-the-timeline-for-upcoming-releases)
- [ Moving to a supergraph architecture ](https://hasura.io/docs/3.0/basics/alpha-release/#moving-to-a-supergraph-architecture)
    - [ Before Hasura DDN ](https://hasura.io/docs/3.0/basics/alpha-release/#before-hasura-ddn)

- [ After Hasura DDN ](https://hasura.io/docs/3.0/basics/alpha-release/#after-hasura-ddn)