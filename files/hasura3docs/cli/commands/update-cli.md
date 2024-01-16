# Hasura3 CLI: hasura3 update-cli

## Synopsis​

You can use this command to update the CLI to the latest version or a specific version. Each time you run a CLI command, if a new version is available, you will be prompted to update the CLI..

```
$ hasura3 update-cli --help
You can use this  command  to update the CLI to the latest version or a specific version. Each  time  you run a CLI command,  if  a new version is available, you will be prompted to update the CLI.
Usage:
  hasura3 update-cli  [ flags ]
Examples:
   # Update CLI to latest version:
  hasura3 update-cli
   # To disable auto-update check on the CLI, set
   # "show_update_notification": false
   # in ~/.hasura3/config.yaml
   # Update CLI to a specific version (say 2023.11.20):
  hasura3 update-cli --version  2023.11 .20
Flags:
  -h, --help              help   for  update-cli
      --version string   a specific version to  install
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/update-cli/#synopsis)
