# Hasura3 CLI: hasura3 secret

## Synopsis​

Commands related to Hasura Cloud Secret Ops.

```
$ hasura3 secret --help
Commands related to Hasura Cloud Secret Ops
Usage:
  hasura3 secret  [ command ]
Aliases:
  secret, secrets
Available Commands:
  delete      Delete/Remove a secret  [ aliases: rm, remove ]
  get         Get the value of a secret key
  list        List all secrets  [ aliases: ls ]
   set          Create/Update a secret
Flags:
  -h, --help              help   for  secret
  -p, --project string   Hasura DDN Project Name
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
Use  "hasura3 secret [command] --help"   for   more  information about a command.
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/secret/#synopsis)
