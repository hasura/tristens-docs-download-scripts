# Hasura Data Connectors Developer's Guide

# API Specification

| Version |
|---|
|  `0.1.0`  |


A data connector encapsulates a data source by implementing the protocol in this specification.

A data connector must implement several web service endpoints:

- A **capabilities** endpoint, which describes which features the data source is capable of implementing.
- A **schema** endpoint, which describes the resources provided by the data source, and the shape of the data they contain.
- A **query** endpoint, which reads data from one of the relations described by the schema endpoint.
- A **mutation** endpoint, which modifies the data in one of the relations described by the schema endpoint.
- An **explain** endpoint, which explains a query plan, without actually executing it.
- A **metrics** endpoint, which exposes runtime metrics about the data connector.