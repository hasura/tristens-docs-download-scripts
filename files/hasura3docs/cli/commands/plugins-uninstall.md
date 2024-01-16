# Hasura3 CLI: hasura3 plugins uninstall

## Synopsis​

To uninstall a plugin, run the uninstall command with the name of the plugin as an argument. If unsure of the plugin's name, you can run the `Hasura plugins list` command to see a list of all the available plugins..

```
$ hasura3 plugins uninstall --help
To uninstall a plugin, run the uninstall  command  with the name of the plugin as an argument. If unsure of the plugin's name, you can run the  ` Hasura plugins list `   command  to see a list of all the available plugins.
Usage:
  hasura3 plugins uninstall  [ plugin-name ]   [ flags ]
Aliases:
  uninstall, remove
Examples:
   # Uninstall a plugin
  hasura3 plugins uninstall  [ plugin-name ]
Flags:
  -h, --help    help   for  uninstall
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/plugins-uninstall/#synopsis)
