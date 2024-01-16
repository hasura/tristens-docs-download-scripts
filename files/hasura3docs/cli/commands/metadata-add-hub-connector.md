# Hasura3 CLI: hasura3 metadata add-hub-connector

## Synopsis​

Adds the data connector and creates the required metadata files..

```
$ hasura3 metadata add-hub-connector --help
Adds the data connector and creates the required metadata files.
Usage:
  hasura3 metadata add-hub-connector  [ source-name ]   [ flags ]
Aliases:
  add-hub-connector, ahc
Examples:
# Add a Postgres Datasource
hasura3 metadata add-hub-connector  < source_name >  --id hasura/postgres --url = < pg_uri >  --subgraph  < subgraph_name >  --dir  < path to hasura.yaml >
# Add a TypeScript Connector
hasura3 metadata add-hub-connector bizlogic --id hasura/ts-deno --url = http://localhost:8100 --subgraph default --dir  < path to hasura.yaml >
Flags:
  -d, --dir string        Directory where the v3 project exists
  -h, --help               help   for  add-hub-connector
      --id string         Hasura Connector Hub ID of the data connector to use
      --profile string    Build profile to use, uses the default build profile  if  not provided
      --subgraph string   Name of the subgraph on  which  the connector needs to be added  ( default  "default" )
      --url string        Endpoint on  which  the data connector can be reached
Global Flags:
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/metadata-add-hub-connector/#synopsis)
