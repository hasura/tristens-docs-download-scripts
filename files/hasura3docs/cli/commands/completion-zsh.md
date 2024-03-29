# Hasura3 CLI: hasura3 completion zsh

## Synopsis​

Generate the autocompletion script for the zsh shell..

```
$ hasura3 completion  zsh  --help
Generate the autocompletion script  for  the  zsh  shell.
If shell completion is not already enabled  in  your environment you will need
to  enable  it.  You can execute the following once:
     echo   "autoload -U compinit; compinit"   >>  ~/.zshrc
To load completions  in  your current shell session:
     source   < ( hasura3 completion  zsh )
To load completions  for  every new session, execute once:
#### Linux:
    hasura3 completion  zsh   >   " ${fpath [ 1 ] } /_hasura3"
#### macOS:
    hasura3 completion  zsh   >   $( brew --prefix ) /share/zsh/site-functions/_hasura3
You will need to start a new shell  for  this setup to take effect.
Usage:
  hasura3 completion  zsh   [ flags ]
Flags:
  -h, --help               help   for   zsh
      --no-descriptions   disable completion descriptions
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/completion-zsh/#synopsis)
