# Hasura3 CLI: hasura3 secret get

## Synopsis​

Get the value of a secret key.

```
$ hasura3 secret get --help
Get the value of a secret key
Usage:
  hasura3 secret get  [ flags ]
Examples:
  # Get the value of secret MY_KEY
   hasura3 secret get --project  < project-name >  --key MY_KEY
  # Get the value of secret MY_KEY in default environment (across all subgraphs) of a project
   hasura3 secret get --project  < project-name >  --key MY_KEY --environment default
  # Get the value of secret MY_KEY in default subgraph (across all environments) of a project
   hasura3 secret get --project  < project-name >  --subgraph default -key MY_KEY
  # Get the value of secret MY_KEY in default environment in default subgraph
   hasura3 secret get --project  < project-name >  --subgraph default --environment default -key MY_KEY
Flags:
  -e, --environment string   Environment of secret
  -h, --help                  help   for  get
  -k, --key string           SetSecret key  ( required )
  -n, --subgraph string      Subgraph of secret
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/secret-get/#synopsis)
