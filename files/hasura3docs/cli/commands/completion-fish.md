# Hasura3 CLI: hasura3 completion fish

## Synopsis​

Generate the autocompletion script for the fish shell..

```
$ hasura3 completion fish --help
Generate the autocompletion script  for  the fish shell.
To load completions  in  your current shell session:
    hasura3 completion fish  |   source
To load completions  for  every new session, execute once:
    hasura3 completion fish  >  ~/.config/fish/completions/hasura3.fish
You will need to start a new shell  for  this setup to take effect.
Usage:
  hasura3 completion fish  [ flags ]
Flags:
  -h, --help               help   for  fish
      --no-descriptions   disable completion descriptions
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/completion-fish/#synopsis)
