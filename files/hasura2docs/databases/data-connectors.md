# Hasura Data Connectors

## Introduction​

Hasura Data Connectors provide an easy way to build connections to any data source and instantly obtain GraphQL APIs on
that data.

Currently, Hasura natively supports Postgres, MS SQL Server, and BigQuery databases. Data Connectors allow you to
connect Hasura to **any** other data source. Hasura has built Data Connectors for MySQL, Oracle, Snowflake, Amazon
Athena, MariaDB, and MongoDB, with more sources in the pipeline, but you can also use them to connect to
your data sources. Think Microsoft Excel, SQLite, CSV, AirTable and more.

For more information on databases, check out the[ Hasura Databases documentation ](https://hasura.io/docs/latest/databases/overview/)or to
jump right into integrating a native database,[ check out the Quickstart ](https://hasura.io/docs/latest/databases/quickstart/).

This documentation will guide you through understanding Hasura Data Connectors concepts and how to use them.

Active Development

Data Connectors are currently in active development and are likely to change considerably. We are working hard to make
them as stable as possible soon, but please be aware that breaking changes may occur.

## Hasura GraphQL Data Connector Agent​

The Hasura GraphQL Data Connector Agent is a service that acts as an intermediary middleware abstraction between a data
source and the Hasura GraphQL Engine via a REST API. It allows developers to implement Hasura's powerful GraphQL
experience on any data source they use. Further information about the design and implementation of the Agent service
can be found in the[ README.md of the Data Connector Agent repository ](https://github.com/hasura/graphql-engine/blob/master/dc-agents/README.md).

Image: [ Hasura GraphQL Data Connector Agent diagram ](https://hasura.io/docs/assets/images/data-connectors-agent-diagram-703e24937e0a2fabb4158c694d550e27.png)

In addition, an Agent can directly support new functionality without any other database upstream. The purpose of Data
Connector Agents is to quickly and easily allow developers to author new Agents to support a wide variety of new data
sources and use-cases.

## More with Data Connectors​

- [ Add a Data Connector to Hasura ](https://hasura.io/docs/latest/databases/data-connectors/adding-data-connectors/)
- [ Build a Data Connector for Hasura ](https://hasura.io/docs/latest/databases/data-connectors/data-connector-sdk/)
- [ Deploy custom code to Hasura Cloud with Jupyter Notebooks ](https://hasura.io/docs/latest/ai/integrations/jupyter-notebooks/)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/databases/data-connectors/#introduction)
- [ Hasura GraphQL Data Connector Agent ](https://hasura.io/docs/latest/databases/data-connectors/#hasura-graphql-data-connector-agent)
- [ More with Data Connectors ](https://hasura.io/docs/latest/databases/data-connectors/#more-with-data-connectors)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)