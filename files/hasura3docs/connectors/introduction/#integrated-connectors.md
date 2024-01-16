# Introduction

## What is a data connector?​

A data connector is an HTTP service that exposes a set of APIs that Hasura uses to communicate with the data source. The
data connector is responsible for interpreting work to be done on behalf of the Hasura Engine, using the native query
language of the data source.

Data connectors, which are built using the[ NDC Specification ](http://hasura.github.io/ndc-spec/)and closely integrated
with the[ OpenDD spec ](https://github.com/hasura/open-data-domain-specification), enable anyone to connect rich,
highly-native data sources.

The NDC Specification defines a set of APIs that a data connector must implement. These APIs, which accept and return
JSON, are used by Hasura to communicate with the data connector agent. The NDC specification also defines a set of
metadata that the data connector agent must provide to Hasura. This metadata is used by Hasura to introspect the data
connector, generate the GraphQL schema, and execute operations against the data source.

You can[ build your own data connector ](https://hasura.io/docs/3.0/connectors/build-your-own-connector/), or use one of the many connectors
available on the[ Connector Hub ](https://hasura.io/connectors).

## Types of data connectors​

There are two main types of connectors available for use in Hasura v3 projects: Integrated and HTTP connectors.

### Integrated connectors​

Integrated connectors are configured and deployed via your project metadata only and do not require any additional
processes.

An example of an integrated connector is the[ Postgres Connector ](https://hasura.io/connectors/postgres).

### HTTP connectors​

HTTP connectors are configured and deployed **independently** of your project metadata and only the URL of the deployed
connector is required in your metadata.

While Hasura does not prescribe any process for deploying an HTTP connector it does provide the `connector` CLI plugin
for easily deploying connectors that use our SDKs. You can learn more in our[ connector deployment guide ](https://hasura.io/docs/3.0/connectors/deployment/#http-connectors).

An example of an HTTP connector is the[ SendGrid Connector ](https://hasura.io/connectors/sendgrid).

## What data connectors are available?​

Browse the[ Connector Hub ](https://hasura.io/connectors)for an up-to-date list of all available connectors.

### What did you think of this doc?

- [ What is a data connector? ](https://hasura.io/docs/3.0/connectors/introduction/#integrated-connectors/#what-is-a-data-connector)
- [ Types of data connectors ](https://hasura.io/docs/3.0/connectors/introduction/#integrated-connectors/#types-of-data-connectors)
    - [ Integrated connectors ](https://hasura.io/docs/3.0/connectors/introduction/#integrated-connectors/#integrated-connectors)

- [ HTTP connectors ](https://hasura.io/docs/3.0/connectors/introduction/#integrated-connectors/#http-connectors)
- [ What data connectors are available? ](https://hasura.io/docs/3.0/connectors/introduction/#integrated-connectors/#what-data-connectors-are-available)
