# Hasura3 CLI: hasura3 login

## Synopsis​

Login to Hasura Cloud.

```
$ hasura3 login --help
Login to Hasura Cloud
Usage:
  hasura3 login  [ flags ]
Examples:
  # Login with browser
 hasura3 login
  # Login with Personal Access token
 hasura3 login --pat  < your-personal-access-token >
Flags:
  -h, --help          help   for  login
      --pat string   Personal Access token  [ env: HASURA_DDN_PAT ]
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/login/#synopsis)
