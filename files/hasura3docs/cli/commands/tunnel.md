# Hasura3 CLI: hasura3 tunnel

## Synopsis​

Hasura Secure Connect service.

```
$ hasura3 tunnel --help
Hasura Secure Connect  service
Usage:
  hasura3 tunnel  [ command ]
Aliases:
  tunnel, tunnels
Available Commands:
  activate    Restart a paused tunnel
  create      Create a new tunnel
  delete      Delete/remove a tunnel  [ aliases: rm, remove ]
  list        List Tunnels  [ aliases: ls ]
  pause       Pause an active tunnel
Flags:
  -h, --help    help   for  tunnel
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
Use  "hasura3 tunnel [command] --help"   for   more  information about a command.
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/tunnel/#synopsis)
