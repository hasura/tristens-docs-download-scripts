# Hasura3 CLI: hasura3 secret set

## Synopsis​

Create/Update a secret.

```
$ hasura3 secret  set  --help
Create/Update a secret
Usage:
  hasura3 secret  set   [ flags ]
Examples:
  # Create a Secret MY_KEY=myValue
   hasura3 secret  set  --project  < project-name >  --environment default --subgraph default --key MY_KEY --value myValue --description  "test secret"
Flags:
  -d, --description string   Description  for  the secret
  -e, --environment string   Environment where the secret can be referenced  ( required )
  -h, --help                  help   for   set
  -k, --key string           SetSecret key  ( required )
  -n, --subgraph string      Supergraph or Subgraph where the secret can be referenced
  -v, --value string         Value of the secret  ( required )
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/secret-set/#synopsis)
