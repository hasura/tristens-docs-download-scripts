# Hasura3 CLI: hasura3 project delete

## Synopsis​

Delete a project from Hasura Cloud[aliases: remove, rm].

```
$ hasura3 project delete --help
Delete a project from Hasura Cloud  [ aliases: remove, rm ]
Usage:
  hasura3 project delete  [ flags ]
Aliases:
  delete, remove,  rm
Examples:
  # Delete a project
   hasura3 project delete --project  < project-name >
Flags:
  -h, --help    help   for  delete
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/project-delete/#synopsis)
