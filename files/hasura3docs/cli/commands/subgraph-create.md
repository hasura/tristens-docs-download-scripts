# Hasura3 CLI: hasura3 subgraph create

## Synopsis​

Create a subgraph.

```
$ hasura3 subgraph create --help
Create a subgraph
Usage:
  hasura3 subgraph create  [ flags ]
Examples:
  # Create a subgraph "accounting" in a project
   hasura3 subgraph create --name accounting --project  < project-name >
Flags:
  -h, --help           help   for  create
  -n, --name string   Subgraph name  ( required )
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/subgraph-create/#synopsis)
