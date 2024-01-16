# Hasura3 CLI: hasura3 build apply

## Synopsis​

Apply a Build to a Hasura DDN Project.

```
$ hasura3 build apply --help
Apply a Build to a Hasura DDN Project
Usage:
  hasura3 build apply  [ flags ]
Examples:
  # Apply a build to your project
   hasura3 build apply --project  < project-name >  --version  < build-version >
Flags:
  -h, --help              help   for  apply
      --version string   Version of the build to apply  ( required )
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/build-apply/#synopsis)
