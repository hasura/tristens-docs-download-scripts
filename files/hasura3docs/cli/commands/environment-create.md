# Hasura3 CLI: hasura3 environment create

## Synopsis​

Create an environment in a Hasura Project.

```
$ hasura3 environment create --help
Create an environment  in  a Hasura Project
Usage:
  hasura3 environment create  [ flags ]
Examples:
  # Create an environment "staging" in a project
   hasura3 environment create --name staging --project  < project-name >
Flags:
  -d, --description string   Environment description
  -h, --help                  help   for  create
  -n, --name string          Environment name  ( required )
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/environment-create/#synopsis)
