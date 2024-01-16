# Hasura3 CLI: hasura3 build

## Synopsis​

Manage Hasura DDN Project Builds[alias: builds].

```
$ hasura3 build --help
Manage Hasura DDN Project Builds  [ alias: builds ]
Usage:
  hasura3 build  [ command ]
Aliases:
  build, builds
Available Commands:
  apply       Apply a Build to a Hasura DDN Project
  create      Create a build  in  a Hasura Cloud Project
  delete      Delete a Build from a Hasura Cloud Project  [ aliases: rm, remove ]
  describe    Describe a Build  [ aliases: info, details ]
  list        List the builds of a Hasura Project  [ alias: ls ]
Flags:
  -h, --help    help   for  build
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
Use  "hasura3 build [command] --help"   for   more  information about a command.
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/build/#synopsis)