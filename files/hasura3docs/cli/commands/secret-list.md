# Hasura3 CLI: hasura3 secret list

## Synopsis​

List all secrets[aliases: ls].

```
$ hasura3 secret list --help
List all secrets  [ aliases: ls ]
Usage:
  hasura3 secret list  [ flags ]
Aliases:
  list,  ls
Examples:
  # List all secrets in a project
   hasura3 secret list --project  < project-name >  
  # List all secrets in default environment (across all subgraph) of a project
   hasura3 secret list --project  < project-name >  --environment default
  # List all secrets in default subgraph (across all environments) of a project
   hasura3 secret list --project  < project-name >  --subgraph default
  # List all secrets in default environment in default subgraph
   hasura3 secret list --project  < project-name >  --subgraph default --environment default
Flags:
  -e, --environment string   Environment of secret
  -h, --help                  help   for  list
  -n, --subgraph string      Subgraph of secret
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/secret-list/#synopsis)
