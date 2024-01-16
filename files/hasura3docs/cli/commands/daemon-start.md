# Hasura3 CLI: hasura3 daemon start

## Synopsis​

Start Hasura Secure Connect Daemon.

```
$ hasura3 daemon start --help
Start Hasura Secure Connect Daemon
Usage:
  hasura3 daemon start  [ flags ]
Examples:
  # Start the tunnel daemon on port 4321
   hasura3 daemon start --port  4321
Flags:
  -h, --help        help   for  start
      --port int   The TCP Port on  which  the Secure Connect Tunnel Daemon will run
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/daemon-start/#synopsis)