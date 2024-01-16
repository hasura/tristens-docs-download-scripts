# Hasura3 CLI: hasura3 watch

## Synopsis​

Watch a local Hasura project.

```
$ hasura3  watch  --help
Watch a  local  Hasura project
Usage:
  hasura3  watch   [ flags ]
Examples:
  # Watch and re-create a build on any file changes 
   hasura3  watch  --dir  < path-to-hasura.yaml-file >   
  # To override the default build profile, provide the --profile flag with a build-profile
   hasura3  watch  --profile build-profile-staging.yaml --dir  < path-to-hasura.yaml-file >
Flags:
  -h, --help              help   for   watch
      --profile string   Build profile to use, uses the default build profile  if  not provided
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/watch/#synopsis)