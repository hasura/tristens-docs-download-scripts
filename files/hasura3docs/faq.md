# Hasura FAQ

## What is the general architecture of Hasura DDN?​

Hasura DDN is built on the major advancements made in Hasura Version 3:

 **Hasura Runtime Engine:** The Hasura Engine is responsible for processing and serving APIs based on provided
metadata. In DDN, the engine is serverless by default and there is a clear separation of build time and runtime
concerns which is analogous to compiled programming languages. Metadata can now be authored, edited and deployed
declaratively without causing any downtime. The new engine can also serve production-grade APIs from the
edge with extremely high performance since it accesses metadata on a per-request basis and benefits from vastly
improved startup times. Essentially the cold start problem has been removed in DDN leading to zero-downtime rollouts.

 **Open Data Domain Specification (OpenDD Spec):** At the heart of Hasura API development is the OpenDD
specification. It is a format which defines the structure of metadata used by the Hasura runtime engine. Think of the
specification as an API contract generator helping you to reason about your data domains and model your applications
and APIs. It is a significant update to the existing Hasura metadata structure with fixed types such as `models` and `commands` . And by ensuring that it is API protocol agnostic it is easily extended to other API technologies
besides GraphQL such as gRPC and REST.[ Learn more ](https://hasura.io/docs/3.0/data-domain-modeling/overview/).

 **Native Data Connector (NDC) Specification:** The NDC specification describes how the API request will be executed and
how the engine will interact with the underlying data source and is a new data connectivity specification from Hasura.
In DDN, there is now no concept of "native databases" and access to all data sources including PostgreSQL will be
based on the native data connector specification. This helps in providing rich feature sets for *all* data sources as
compared to just a few select ones. Moreover, there is now a strong focus on enabling the community to build
data connector agents themselves. The specification and provided[ Rust ](https://github.com/hasura/ndc-hub#rust-sdk)and[ Typescript ](https://github.com/hasura/ndc-sdk-typescript)SDKs support building high-quality integrations for
almost any conceivable data source (both databases and APIs), offering features like native queries, push-down
capabilities, and connection pooling.[ Learn more ](https://hasura.io/docs/3.0/connectors/overview/).

 **Hasura Cloud:** The cloud layer in Hasura DDN, Hasura Cloud, introduces the Data Delivery Network (DDN) for global API
performance and availability. This layer also facilitates secure tunnels for local development using Hasura Secure
Connect and also offers tools for managing projects, builds, environments, secrets, subgraph namespaces and essentially
represents the control plane for Hasura DDN.

 **Hasura CLI:** The new Hasura CLI (Command-Line Interface), serves as a powerful tool for developers
to interact with the Hasura platform. It allows users to initialize projects, manage metadata, create builds, and deploy
production APIs both locally and in the cloud, easily.[ Learn More ](https://hasura.io/docs/3.0/cli/overview/)

 **Hasura Console:** The Hasura Console has been revamped to enable rapid onboarding, testing and troubleshooting. The
console now provides rich visualizations, deep dive metrics into models, enhanced traces, the new GraphiQL API
explorer, new operational health dashboard and a refurbished data manager that scales seamlessly with heavy loads.[Learn More]([ https://console.hasura.io/ ](https://console.hasura.io/))

 **Builds:** Each metadata change in Hasura now results in an atomic build which is represented by an immutable artifact
that is loaded onto Hasura DDN instantly. Which means there is inherent version control and the ability to push
metadata changes instantly and without errors.[ Learn more ](https://hasura.io/docs/3.0/ci-cd/builds/)

 **Environments:** Environments introduce the concept of infrastructure sharing and management in Hasura. Each build is
specific to an environment and provides a unique testing API. Users will need to create build profiles for each
environment. The idea is to give development teams total flexibility to iterate using dedicated resources without
affecting production workloads.[ Learn more ](https://hasura.io/docs/3.0/ci-cd/environments/)

 **Subgraphs:** Subgraphs introduce a module system for metadata. They allow multi-team organizations working on a
Hasura project to segment access to different metadata objects. A project's metadata is the amalgamation of metadata
objects from all its subgraphs, and each subgraph can be accessed and updated independently. It also helps in
avoiding conflicts when there are, for example, tables with the same names in different data sources.[ Learn more ](https://hasura.io/docs/3.0/ci-cd/subgraphs/)

## What will be the benefit for me, the developer? (Why would I want to use or switch to DDN?)​

- Significant improvements to metadata authoring and management.
    - No more cold start problem and instant changes to metadata. Deploy multiple times in an hour. Deploy with
lightning speed and sub-second CI/CD.

- No dependency on upstream services which means zero-downtime deployments.

- Code driven workflows with advanced code generation tooling.

- A single spec to define your whole API across diverse data sources.

- Declarative metadata authoring with full control on API schema generation.

- No metadata database - one less thing to manage in production.
- Connect to any data with Native Data Connectors (NDCs).
- Compose all your data sources, APIs and information into a single, powerful, inter-related supergraph.
- Work better with your team with improved version control and collaboration features.
- Unparalleled performance at any scale with optimized query execution and caching mechanisms.
- Serverless runtime for improved efficiency and reduced latency.
- Access a global edge network for low-latency, high-performance APIs with the Data Delivery Network (DDN).
- Bring the programming language of your choice such as Typescript to compose business logic
- Perform advanced mutations and workflows within the request response lifecycle.


## What CI/CD features does Hasura DDN offer?​

 **Instant CI/CD:** Hasura brings instant CI/CD capabilities, enabling developers to test and validate changes
rapidly.

 **CLI-Controlled Deployments:** The Hasura Command-Line Interface (CLI) plays a central role in controlling and managing
deployments. It allows developers to manage projects, create builds and promote them to production. This CLI-centric
approach simplifies the deployment process.[ Learn more ](https://hasura.io/docs/3.0/cli/overview/)

 **Builds and Project Shares:** With Hasura, metadata states are represented as builds. Once a build is thoroughly tested
and validated, it can be applied to a project as the live API and made available to API consumers globally. This
separation of build and production steps ensure a smoother transition from development to production.

 **Extremely Fast Builds:** Hasura also introduces cloud innovations that allow metadata builds to be created instantly,
regardless of the number of models. This means that deploying even a large number of models is a swift and seamless
process and developers can rapidly test multiple deployments within a day.

 **Zero Downtime Rollouts:** With Hasura, going to production is facilitated without restarts and with zero downtime.
This ensures that your API remains available to users while updates are being applied.

 **Metadata Version Control:** Hasura includes in-product metadata version control. Each build is associated with a
unique build ID, making it easier to track and manage different versions of your metadata. This enhances transparency
and auditability during the deployment process.

 **Environments:** With environments you can design workflows that best mimic your software development lifecycle. Using
environments enabled you to plan and manage infrastructure within your teams effectively.

### What can be automated?​

Since metadata authoring is mostly code driven using the new LSP and the CLI, many metadata related changes can
be automated using a version management and CI/CD tool of your choice.

## How does Hasura DDN connect to data sources?​

Native Data Connectors (NDC) are a framework introduced in Hasura DDN that enables developers to build custom data
connector agents. These agents facilitate the integration between Hasura and external data sources, allowing Hasura to
seamlessly interact with a wide range of databases, services, and APIs. NDCs can be built for almost any conceivable
source of data and are the only way to connect to data sources in Hasura DDN.

Native Data Connectors can either be self-hosted or hosted by Hasura.[ Learn more ](https://hasura.io/docs/3.0/connectors/overview/)

## Is Hasura DDN open source?​

The[ Hasura DDN engine ](https://github.com/hasura/v3-engine)and all[ Hasura data connectors ](https://hasura.io/connectors)are open-source.

## What is the pricing structure for DDN?​

DDN is completely free for 90 days for all Alpha users. Stay tuned for additional pricing information.

## What is the timeline for Hasura DDN? (When is v3 coming out?)​

Hasura DDN Alpha is now publicly available, and we will continue to add features and listen to feedback from our
community. We are expecting the Beta release in few months, followed by General Availability within the first
half of 2024. For the most up-to-date information on the timeline, we recommend referring to our[ official announcements and releases ](https://hasura.io/community/).

## What does Alpha release mean?​

This is the first public version of Hasura Data Delivery Network with a limited functionality set and some known issues.
This is to engage with the community at the earliest while continuing to work to make the platform stable and
functionality complete. As such, there may be some breaking changes introduced in the Alpha version. Also, customer support
will be limited during this phase and most communication from Hasurans will happen via direct conversation with the
team via Discord channels, user groups, and community calls.

## What is the recommended approach to metadata authoring?​

The recommended approach is to start via the CLI and the CLI init command. This will create local directory and file
scaffolding for you after which you can author metadata using our VS Code extension. The console is intended to be a
quick getting started tool and for visualization and monitoring.

We expect most metadata management will happen via the code driven tools that we have in DDN. We are investing in
extensive code generation capabilities via the LSP and users will still get to enjoy the quick authoring experiences
of v2 such as that of permission building, outside the console.

## Authoring metadata looks hard, how can I get started?​

The Hasura LSP (Language Server Protocol)[ plugin for VSCode ](https://marketplace.visualstudio.com/items?itemName=HasuraHQ.hasura)and other editors will help you
get started with authoring. It includes autocomplete, validations, code actions and go-to-definition features.

## Will DDN be self-hosted?​

DDN Alpha and Beta will not be available as self-hosted options. We are evaluating plans to meet the deployment
needs of our users as we move towards general availability.

### Why don’t you have a container I can download?​

Hasura DDN leverages a range of cloud services to offer comprehensive features and advanced innovations. We are
committed to delivering optimum value to our users with the benefits offered by a cloud-first approach

### Do I need a container to develop locally?​

No. Our enhanced metadata authoring capabilities allow you to work via the Hasura VS Code plugin and CLI and test and
visualize your API endpoints via deployments in the Hasura DDN console.

We strongly believe that this is a more enhanced experience than building locally and then migrating ton your
production endpoints.

## I’m operating in a given cloud provider region. How can I have Hasura run in the same region?​

Hasura DDN is strategically deployed in 10 regions worldwide. (We plan to increase coverage drastically as we move
closer to Beta and beyond) Depending on the origin of a request, we automatically activate an instance of Hasura in the
nearest region. This process is completed in under 10 milliseconds, ensuring consistently optimal performance,
closest to your users.

## Will Hasura DDN be compatible with Hasura v1/v2?​

The default generated GraphQL schema (ie: the API your consumers use) of Hasura DDN is compatible with v2 schemas
and will not change. However, Hasura DDN uses a completely new metadata structure and hence will require migration
tools to move metadata from v1/v2 metadata.

## Will Hasura v2 be supported after Hasura DDN is released?​

We will still support, maintain and improve Hasura v2 as per our[ version support policy ](https://hasura.io/docs/latest/policies/versioning/)and will be providing migration tools to
move Hasura v2 deployments to DDN in the near future.

## What is the difference between how Hasura v2 and DDN metadata is handled?​

In practical terms, the Hasura v2 metadata system was designed to draw extra information directly from the data source,
specifically details such as columns and fields.

This meant that whenever the Hasura GraphQL Engine was initialized, it had to probe or "introspect" the data source's
schema to create a GraphQL schema. This introduced delays at start-up especially if the data source was large or if
there were network issues.

OpenDD metadata operates differently as it is inherently self-contained and exists independent of any data source. This
leads to instant startup and deploy times and ensures consistency as the system is no longer polling an underlying
data source for schema information which may have changed.

The OpenDD metadata has full coverage, and details like fields and their respective types are predefined and embedded
within metadata. This design choice removes the need for the system to check the data source schema every time during
startup to shape a GraphQL schema. Instead, this introspection or probing of the data source's structure is now carried
out during the metadata creation, or build phase. This leads to massively improved startup times and ensures that the
metadata is consistent and self-contained.

## Will Hasura continue supporting existing plans, specifically, the Cloud Free and Professional plans?​

Yes. We are committed to maintaining & supporting the Free and Professional plans to ensure there is no disruption
to our users.

## I heard DDN is built in Rust. Why Rust over Haskell?​

We have a lot of love for Haskell. It's a beautiful language that we have been using for the Hasura engine since the
beginning, and will still be using it on Hasura v2. Without going into the weeds in a FAQ, we wanted to benefit from
Rust's performance, ecosystem and community for DDN. Rust is a modern, high-performance, and memory-safe language. It is
also gaining much traction in the cloud-native space, and we are excited to be using it for the significant parts of the
Hasura DDN codebase. If you are a Rust developer and want to do cool stuff, please check out our careers page.

## How do I migrate from v1/v2 to DDN? (What would be the experience of bringing graphQL APIs in v3?)​

We will provide a low-code migration tool for you to quickly port over to DDN in the coming months.

### If currently running a v2.x will it be moved automatically to v3?​

No, it will not. The v2 cloud projects will remain untouched and there will be no change of business. Moving to DDN
will be an opt-in process. Having said that, we strongly encourage upgrading to DDN early when features you require
are available. Our teams are available to make the migration process as smooth as possible.

### Can we request to lock ourselves to 2.x?​

The migration is an opt-in process, so you do not need to request to have yourselves locked to a particular version.
If however, you see no upgrade path even in the next two years, please give us a heads-up and we will work out
options with you.

### What is the migration path for the v2 Remote Schemas feature in v3?​

The way to utilize remote schemas in DDN has changed from v2. However, we will make sure that the developer
experience is the same or better than it is in v2 and will provide migration guidance for this use-case in the
coming months.

### Will Event and Scheduled Triggers be supported in Hasura DDN?​

Yes they will be but the developer experience will change. We are still in the design phase for this and will provide
more details in the coming months.

### Will Actions be supported in Hasura DDN?​

If you mean business logic and API integration then yes but there is no concept of 'Actions' in Hasura DDN. In
Hasura DDN Alpha you can now use Typescript directly for 'Action-like' functionality. What is better is that now you
can host your Action webhooks/functions on Hasura itself. Moreover, we will be scaling support to most other popular
languages such as Java, GoLang, Rust, Python and more.

### Will Remote Schemas (external GraphQL APIs) be supported in Hasura DDN?​

Yes, but there will not be a tab in Console or metadata object represented for Remote Schemas. All external GraphQL
APIs, previously known as Remote Schemas, will be utilized via Native Data Connectors. We will provide generic
connectors or connector SDKs so that you can bring in external GraphQL APIs in the low-code manner you are used to
in v2.

### Will mutations be supported in Hasura DDN?​

Yes, of course, but the developer experience of configuring mutations will change.

### What are the main changes to the Hasura Console?​

There has been a complete redesign of the Hasura Console with new panels for visualization and operational health.
We have totally revamped the GraphiQL and Data Manager tabs and have implemented all new settings panel for
environments, secrets, subgraphs and collaborators.

Moreover, there is no longer the concept of an admin secret in Hasura DDN. In fact, we will auto generate a Personal
Access Token (PAT) which will provide the previous admin secret functionality.

### Will v3 have a data manager in the console?​

Yes. A better version which can scale with large datasets and be used for many types of databases and not only
PostgreSQL.

### What about database migrations?​

Database migrations are deprecated. We will provide a generated SQL that you can use in an ORM tool of your choice. We
are open to any feedback on this product strategy. Do let us know about your pain point, and we can recommend a
solution that works best for you.

## Is a Hasura DDN API faster than a Hasura v2 API?​

Yes. Hasura DDN includes significant performance improvements compared to its predecessors. The optimizations
implemented in Hasura DDN aim to provide faster response times and improved scalability, ensuring a smooth and efficient
experience for your applications and users. We will be releasing detailed performance benchmarks in the coming months.

### What did you think of this doc?

- [ What is the general architecture of Hasura DDN? ](https://hasura.io/docs/3.0/faq/#what-is-the-general-architecture-of-hasura-ddn)
- [ What will be the benefit for me, the developer? (Why would I want to use or switch to DDN?) ](https://hasura.io/docs/3.0/faq/#what-will-be-the-benefit-for-me-the-developer-why-would-i-want-to-use-or-switch-to-ddn)
- [ What CI/CD features does Hasura DDN offer? ](https://hasura.io/docs/3.0/faq/#what-cicd-features-does-hasura-ddn-offer)
    - [ What can be automated? ](https://hasura.io/docs/3.0/faq/#what-can-be-automated)
- [ How does Hasura DDN connect to data sources? ](https://hasura.io/docs/3.0/faq/#how-does-hasura-ddn-connect-to-data-sources)
- [ Is Hasura DDN open source? ](https://hasura.io/docs/3.0/faq/#is-hasura-ddn-open-source)
- [ What is the pricing structure for DDN? ](https://hasura.io/docs/3.0/faq/#what-is-the-pricing-structure-for-ddn)
- [ What is the timeline for Hasura DDN? (When is v3 coming out?) ](https://hasura.io/docs/3.0/faq/#what-is-the-timeline-for-hasura-ddn-when-is-v3-coming-out)
- [ What does Alpha release mean? ](https://hasura.io/docs/3.0/faq/#what-does-alpha-release-mean)
- [ What is the recommended approach to metadata authoring? ](https://hasura.io/docs/3.0/faq/#what-is-the-recommended-approach-to-metadata-authoring)
- [ Authoring metadata looks hard, how can I get started? ](https://hasura.io/docs/3.0/faq/#authoring-metadata-looks-hard-how-can-i-get-started)
- [ Will DDN be self-hosted? ](https://hasura.io/docs/3.0/faq/#will-ddn-be-self-hosted)
    - [ Why don’t you have a container I can download? ](https://hasura.io/docs/3.0/faq/#why-dont-you-have-a-container-i-can-download)

- [ Do I need a container to develop locally? ](https://hasura.io/docs/3.0/faq/#do-i-need-a-container-to-develop-locally)
- [ I’m operating in a given cloud provider region. How can I have Hasura run in the same region? ](https://hasura.io/docs/3.0/faq/#im-operating-in-a-given-cloud-provider-region-how-can-i-have-hasura-run-in-the-same-region)
- [ Will Hasura DDN be compatible with Hasura v1/v2? ](https://hasura.io/docs/3.0/faq/#will-hasura-ddn-be-compatible-with-hasura-v1v2)
- [ Will Hasura v2 be supported after Hasura DDN is released? ](https://hasura.io/docs/3.0/faq/#will-hasura-v2-be-supported-after-hasura-ddn-is-released)
- [ What is the difference between how Hasura v2 and DDN metadata is handled? ](https://hasura.io/docs/3.0/faq/#what-is-the-difference-between-how-hasura-v2-and-ddn-metadata-is-handled)
- [ Will Hasura continue supporting existing plans, specifically, the Cloud Free and Professional plans? ](https://hasura.io/docs/3.0/faq/#will-hasura-continue-supporting-existing-plans-specifically-the-cloud-free-and-professional-plans)
- [ I heard DDN is built in Rust. Why Rust over Haskell? ](https://hasura.io/docs/3.0/faq/#i-heard-ddn-is-built-in-rust-why-rust-over-haskell)
- [ How do I migrate from v1/v2 to DDN? (What would be the experience of bringing graphQL APIs in v3?) ](https://hasura.io/docs/3.0/faq/#how-do-i-migrate-from-v1v2-to-ddn-what-would-be-the-experience-of-bringing-graphql-apis-in-v3)
    - [ If currently running a v2.x will it be moved automatically to v3? ](https://hasura.io/docs/3.0/faq/#if-currently-running-a-v2x-will-it-be-moved-automatically-to-v3)

- [ Can we request to lock ourselves to 2.x? ](https://hasura.io/docs/3.0/faq/#can-we-request-to-lock-ourselves-to-2x)

- [ What is the migration path for the v2 Remote Schemas feature in v3? ](https://hasura.io/docs/3.0/faq/#what-is-the-migration-path-for-the-v2-remote-schemas-feature-in-v3)

- [ Will Event and Scheduled Triggers be supported in Hasura DDN? ](https://hasura.io/docs/3.0/faq/#will-event-and-scheduled-triggers-be-supported-in-hasura-ddn)

- [ Will Actions be supported in Hasura DDN? ](https://hasura.io/docs/3.0/faq/#will-actions-be-supported-in-hasura-ddn)

- [ Will Remote Schemas (external GraphQL APIs) be supported in Hasura DDN? ](https://hasura.io/docs/3.0/faq/#will-remote-schemas-external-graphql-apis-be-supported-in-hasura-ddn)

- [ Will mutations be supported in Hasura DDN? ](https://hasura.io/docs/3.0/faq/#will-mutations-be-supported-in-hasura-ddn)

- [ What are the main changes to the Hasura Console? ](https://hasura.io/docs/3.0/faq/#what-are-the-main-changes-to-the-hasura-console)

- [ Will v3 have a data manager in the console? ](https://hasura.io/docs/3.0/faq/#will-v3-have-a-data-manager-in-the-console)

- [ What about database migrations? ](https://hasura.io/docs/3.0/faq/#what-about-database-migrations)
- [ Is a Hasura DDN API faster than a Hasura v2 API? ](https://hasura.io/docs/3.0/faq/#is-a-hasura-ddn-api-faster-than-a-hasura-v2-api)
