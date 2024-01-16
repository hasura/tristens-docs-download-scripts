# Hasura3 CLI: hasura3 secret delete

## Synopsis​

Delete/Remove a secret[aliases: rm, remove].

```
$ hasura3 secret delete --help
Delete/Remove a secret  [ aliases: rm, remove ]
Usage:
  hasura3 secret delete  [ flags ]
Aliases:
  delete, rm, remove
Examples:
  # Remove the Secret MY_KEY
   hasura3 secret delete --project  < project-name >  --environment default --subgraph default --key MY_KEY
Flags:
  -e, --environment string   Environment where the secret can be referenced  ( required )
  -h, --help                  help   for  delete
  -k, --key string           SetSecret key  ( required )
  -n, --subgraph string      Subgraph where the secret can be referenced  ( required )
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/secret-delete/#synopsis)
