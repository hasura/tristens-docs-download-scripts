# Hasura Data Connectors Developer's Guide

# Explain

The explain endpoint accepts a[ query ](./queries/README.html)request, but without actually executing the query, returns a representation of the *execution plan* .

## Request

`POST /explain`

## Request

See[ QueryRequest ](../reference/types.html#queryrequest)

## Response

See[ ExplainResponse ](../reference/types.html#explainresponse)