# Hasura3 CLI: hasura3 tunnel create

## Synopsis​

Create a new tunnel.

```
$ hasura3 tunnel create --help
Create a new tunnel
Usage:
  hasura3 tunnel create  [ socket ]   [ flags ]
Examples:
  # Create a tunnel that is using the daemon running on localhost:1432
   hasura3 tunnel create localhost:1432
Flags:
  -h, --help    help   for  create
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/tunnel-create/#synopsis)
