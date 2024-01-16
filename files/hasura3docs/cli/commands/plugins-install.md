# Hasura3 CLI: hasura3 plugins install

## Synopsis​

To install plugins that extend the functionality of the Hasura CLI, you can use the install command. This command will install the plugin from the index and add it to your configuration file..

```
$ hasura3 plugins  install  --help
To  install  plugins that extend the functionality of the Hasura CLI, you can use the  install  command. This  command  will  install  the plugin from the index and  add  it to your configuration file.
Usage:
  hasura3 plugins  install   [ plugin-name ]   [ flags ]
Aliases:
  install,  add
Examples:
   # Install a plugin:
  hasura3 plugins  install   [ plugin-name ]
Flags:
  -h, --help              help   for   install
      --version string   version to be installed
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/plugins-install/#synopsis)
