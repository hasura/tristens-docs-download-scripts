# Hasura Data Connectors Developer's Guide

# Mutations

The mutation endpoint accepts a mutation request, containing a collection of mutation operations to be performed in the context the data source, and returns a response containing a result for each operation.

The structure and requirements for specific fields listed below will be covered in subsequent chapters.

## Request

`POST /mutation`

## Request

See[ MutationRequest ](../../reference/types.html#mutationrequest)

## Request Fields

| Name | Description |
|---|---|
|  `operations`  | A list of mutation operations to perform |
|  `collection_relationships`  | Any[ relationships ](../queries/relationships.html)between collections involved in the mutation request |


## Mutation Operations

Each operation is described by a[ MutationOperation ](../../reference/types.html#mutationoperation)structure, which can be one of several types. However, currently[ procedures ](./procedures.html)are the only supported operation type.

## Response

See[ MutationResponse ](../../reference/types.html#mutationresponse)

## Requirements

- The `operation_results` field of the[ MutationResponse ](../../reference/types.html#mutationresponse)should contain one[ MutationOperationResults ](../../reference/types.html#mutationoperationresults)structure for each requested operation in the[ MutationRequest ](../../reference/types.html#mutationrequest).
- Each[ MutationOperationResults ](../../reference/types.html#mutationoperationresults)structure should indicate the number of affected rows, along with a list of those rows.
