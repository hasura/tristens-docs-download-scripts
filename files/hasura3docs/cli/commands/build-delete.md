# Hasura3 CLI: hasura3 build delete

## Synopsis​

Delete a Build from a Hasura Cloud Project[aliases: rm, remove].

```
$ hasura3 build delete --help
Delete a Build from a Hasura Cloud Project  [ aliases: rm, remove ]
Usage:
  hasura3 build delete  [ flags ]
Aliases:
  delete, remove,  rm
Examples:
  # Delete a build from your project
   hasura3 build delete --project  < project-name >  --version  < build-version >
Flags:
  -h, --help              help   for  delete
      --version string   Version of the build to delete  ( required )
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/build-delete/#synopsis)
