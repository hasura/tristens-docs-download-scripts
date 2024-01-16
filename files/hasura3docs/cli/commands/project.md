# Hasura3 CLI: hasura3 project

## Synopsis​

Manage Hasura DDN Projects.

```
$ hasura3 project --help
Manage Hasura DDN Projects
Usage:
  hasura3 project  [ command ]
Aliases:
  project, projects
Available Commands:
  create      Create a new project  in  Hasura Cloud
  delete      Delete a project from Hasura Cloud  [ aliases: remove, rm ]
  describe    View project details  [ aliases: details, info ]
  list        View a list of your projects on Hasura Cloud  [ alias: ls ]
Flags:
  -h, --help    help   for  project
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
Use  "hasura3 project [command] --help"   for   more  information about a command.
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/project/#synopsis)
