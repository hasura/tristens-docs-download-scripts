# Hasura3 CLI: hasura3 environment delete

## Synopsis​

Delete an environment from a Hasura Cloud Project[aliases: rm, remove].

```
$ hasura3 environment delete --help
Delete an environment from a Hasura Cloud Project  [ aliases: rm, remove ]
Usage:
  hasura3 environment delete  [ flags ]
Aliases:
  delete, rm, remove
Examples:
  # Delete the environment "staging"
   hasura3 environment delete --project  < project-name >  --name staging
Flags:
  -h, --help           help   for  delete
  -n, --name string   Name of the environment  ( required )
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/environment-delete/#synopsis)