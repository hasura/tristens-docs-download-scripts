# Hasura3 CLI: hasura3 metadata

## Synopsis​

Manage Hasura DDN Projects' Metadata.

```
$ hasura3 metadata --help
Manage Hasura DDN Projects' Metadata
Usage:
  hasura3 metadata  [ command ]
Available Commands:
  add-hub-connector Adds the data connector and creates the required metadata files.
Flags:
  -h, --help    help   for  metadata
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
Use  "hasura3 metadata [command] --help"   for   more  information about a command.
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/metadata/#synopsis)
