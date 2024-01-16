# Hasura3 CLI: hasura3 build list

## Synopsis​

List the builds of a Hasura Project[alias: ls].

```
$ hasura3 build list --help
List the builds of a Hasura Project  [ alias: ls ]
Usage:
  hasura3 build list  [ flags ]
Aliases:
  list,  ls
Examples:
  # List all builds (across all environments) in your project
   hasura3 build list --project  < project-name >
 
  # List all builds in the default environment of your project
   hasura3 build list --project  < project-name >  --environment default
Flags:
      --environment string    ( optionally )  list builds by an environment
  -h, --help                  help   for  list
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/build-list/#synopsis)
