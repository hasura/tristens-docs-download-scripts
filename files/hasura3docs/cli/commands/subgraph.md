# Hasura3 CLI: hasura3 subgraph

## Synopsis​

Manage Hasura project subgraphs.

```
$ hasura3 subgraph --help
Manage Hasura project subgraphs
Usage:
  hasura3 subgraph  [ command ]
Available Commands:
  create      Create a subgraph
  delete      Remove a subgraph from Hasura Cloud Project  [ aliases: remove, rm ]
  describe    View subgraph details  [ aliases: details, info ]
  list        List all subgraphs  in  a Hasura project  [ alias: ls ]
Flags:
  -h, --help              help   for  subgraph
  -p, --project string   Hasura DDN Project Name
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
Use  "hasura3 subgraph [command] --help"   for   more  information about a command.
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/subgraph/#synopsis)
