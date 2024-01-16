# Hasura3 CLI: hasura3 environment list

## Synopsis​

List all environment of a Hasura Project[alias: ls].

```
$ hasura3 environment list --help
List all environment of a Hasura Project  [ alias: ls ]
Usage:
  hasura3 environment list  [ flags ]
Aliases:
  list,  ls
Examples:
  # List all your environments in a project
   hasura3 environment list --project  < project-name >
Flags:
  -h, --help    help   for  list
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/environment-list/#synopsis)
