# Hasura3 CLI: hasura3 completion bash

## Synopsis​

Generate the autocompletion script for the bash shell..

```
$ hasura3 completion  bash  --help
Generate the autocompletion script  for  the  bash  shell.
This script depends on the  'bash-completion'  package.
If it is not installed already, you can  install  it via your OS's package manager.
To load completions  in  your current shell session:
     source   < ( hasura3 completion  bash )
To load completions  for  every new session, execute once:
#### Linux:
    hasura3 completion  bash   >  /etc/bash_completion.d/hasura3
#### macOS:
    hasura3 completion  bash   >   $( brew --prefix ) /etc/bash_completion.d/hasura3
You will need to start a new shell  for  this setup to take effect.
Usage:
  hasura3 completion  bash
Flags:
  -h, --help               help   for   bash
      --no-descriptions   disable completion descriptions
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/completion-bash/#synopsis)
