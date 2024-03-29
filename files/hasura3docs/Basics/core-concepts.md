# Core Concepts

The sprawl of microservices and APIs which any given product needs to connect to in order to function has led to a new
set of challenges for developers and architects.

In the modern era of building applications, the data layer is becoming increasingly complex; it's no longer just a
database, but a collection of databases, services, and APIs.

Hasura DDN introduces the concept of a **data supergraph** to help you manage this complexity.

## The state of the data layer​

Imagine the following sets of teams within a hypothetical company:

- **Product Management Team** : Responsible for the relational database storing product information. This team focuses on
cataloging products, managing inventory, and ensuring product details are accurate and up-to-date by use of a **relational PostgreSQL database** .
- **User Experience Team** : Manages a **MongoDB document database** and related APIs for storing user information. Their
focus is on maintaining user profiles, preferences, and ensuring privacy and security of user data.
- **Search Optimization Team** : Handles the **integration of an Algolia search service** for products and partner
stores. They work on optimizing search algorithms, ensuring relevant search results, and improving the overall search
experience for users.
- **Finance and Transactions Team** : Oversees the **Stripe payment service and underlying relational database** for
processing payments. This includes managing transaction security, payment gateway integrations, and ensuring smooth
financial transactions.
- **Logistics and Shipping Team** : Responsible for the **ShipStation shipping service, fulfilling orders, and the
underlying relational database that supports this process** . Their primary focus is on logistics, order tracking, and
ensuring timely delivery of products.
- **Data Science and Recommendations Team** : Manages the **Weaviate vector database** for storing user recommendations.
They work on personalization algorithms, user behavior analysis, and providing tailored product recommendations to
enhance user experience.


 **Product Management Team** : Responsible for the relational database storing product information. This team focuses on
cataloging products, managing inventory, and ensuring product details are accurate and up-to-date by use of a **relational PostgreSQL database** .

 **User Experience Team** : Manages a **MongoDB document database** and related APIs for storing user information. Their
focus is on maintaining user profiles, preferences, and ensuring privacy and security of user data.

 **Search Optimization Team** : Handles the **integration of an Algolia search service** for products and partner
stores. They work on optimizing search algorithms, ensuring relevant search results, and improving the overall search
experience for users.

 **Finance and Transactions Team** : Oversees the **Stripe payment service and underlying relational database** for
processing payments. This includes managing transaction security, payment gateway integrations, and ensuring smooth
financial transactions.

 **Logistics and Shipping Team** : Responsible for the **ShipStation shipping service, fulfilling orders, and the
underlying relational database that supports this process** . Their primary focus is on logistics, order tracking, and
ensuring timely delivery of products.

 **Data Science and Recommendations Team** : Manages the **Weaviate vector database** for storing user recommendations.
They work on personalization algorithms, user behavior analysis, and providing tailored product recommendations to
enhance user experience.

The diversity of teams within this hypothetical company, each with their unique focus and specialized data services,
epitomizes the common challenge in modern data management and API development. These teams all operate with distinct
APIs, schemas, and methodologies. This fragmentation not only complicates the process of developing applications but
also necessitates the involvement of skilled data architects and engineers to efficiently integrate and maintain these
varied data sources.

## Subgraphs​

In our e-commerce application example, each service above represents what we term a **subgraph** .

A subgraph is much more than just a single data source; it is all the metadata needed to act as a self-contained entity
that can be independently authored, owned, maintained, and deployed by an individual team, to then be an **interconnected part of a unified API** .

For API authors, this means the ability to build out an API — composed of different sources — in a simple, declarative
way. You can utilize unique access-control rules, authentication mechanisms, and custom business logic within your
subgraphs to create a secure and robust API.

Each subgraph in our example is a modular component of the data supergraph. These components securely work together to
overcome the traditional barriers posed by isolated data sources, facilitating a more fluid and interconnected data
layer. This integrated approach simplifies application development across diverse data systems, enabling faster
iteration and more efficient maintenance by engineering teams.

### How do I build a subgraph?​

Subgraphs are composed of related data sources — be that as traditional databases, or as custom business logic — and are
connected to your data layer using **data connectors** . Hasura DDN utilizes a number of data
connectors that work with popular databases, services, and APIs out-of-the-box; you can also build your own. **These
subgraphs can even include your own custom business logic as TypeScript functions that return or mutate data directly
via your GraphQL API.** This saves you the time and effort of building and maintaining your own APIs to manage data
sources and existing microservices.

After connecting your data source, you can then author your metadata using the[ Hasura CLI ](https://hasura.io/docs/3.0/cli/overview/)and our[ LSP-enabled VS Code extension ](https://marketplace.visualstudio.com/items?itemName=HasuraHQ.hasura). This metadata is
then deployed to your Hasura DDN instance, where it is used to build your subgraph and eventually serve your GraphQL
API.

## Supergraph​

A **data supergraph** is the framework that brings together all of your subgraphs into one secure API. This
orchestration allows for the creation of applications that span multiple data sources, services, third-party APIs,
business logic and — most importantly — teams, seamlessly bridging their complexities into a single layer.

For those responsible for maintaining the data layer, this means you now have a single, holistic API to manage, rather
than multiple disparate data sources and connections. This enables you to create CI/CD pipelines, monitor performance
using industry-standard observability tools, and manage access control in a more streamlined and efficient manner.

For your consumers, this means they have a single endpoint to access all the data they need, thereby reducing the
complexity of their applications. This also allows them to focus on building the best possible user experience, rather
than wrangling the underlying data layer.

### How do I build a supergraph?​

This happens automatically.

As you add subgraphs to your Hasura project, Hasura DDN automatically builds a supergraph of all your data sources. You
have the freedom and flexibility to define relationships — including fine-grained access control — across this
supergraph, connecting data sources together and making them available in ways that make sense for your application.

## Next steps​

Check out our[ getting started guide ](https://hasura.io/docs/3.0/getting-started/local-dev/)to learn how to build your first data supergraph.

### What did you think of this doc?

- [ The state of the data layer ](https://hasura.io/docs/3.0/basics/core-concepts/#the-state-of-the-data-layer)
- [ Subgraphs ](https://hasura.io/docs/3.0/basics/core-concepts/#subgraphs)
    - [ How do I build a subgraph? ](https://hasura.io/docs/3.0/basics/core-concepts/#how-do-i-build-a-subgraph)
- [ Supergraph ](https://hasura.io/docs/3.0/basics/core-concepts/#supergraph)
    - [ How do I build a supergraph? ](https://hasura.io/docs/3.0/basics/core-concepts/#how-do-i-build-a-supergraph)
- [ Next steps ](https://hasura.io/docs/3.0/basics/core-concepts/#next-steps)
