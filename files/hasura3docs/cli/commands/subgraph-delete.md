# Hasura3 CLI: hasura3 subgraph delete

## Synopsis​

Remove a subgraph from Hasura Cloud Project[aliases: remove, rm].

```
$ hasura3 subgraph delete --help
Remove a subgraph from Hasura Cloud Project  [ aliases: remove, rm ]
Usage:
  hasura3 subgraph delete  [ flags ]
Aliases:
  delete, rm, remove
Examples:
  # Delete the subgraph "accounting"
   hasura3 subgraph delete --project  < project-name >  --name accounting
Flags:
  -h, --help           help   for  delete
  -n, --name string   Subgraph to be deleted  ( required )
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/subgraph-delete/#synopsis)
