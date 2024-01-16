# Hasura3 CLI: hasura3 plugins

## Synopsis​

The functionality of the CLI can be extended by using plugins. For a list of all available plugins, run `hasura3 plugins list` , or visit this repository:[ https://github.com/hasura/cli-plugins-index ](https://github.com/hasura/cli-plugins-index)..

```
$ hasura3 plugins --help
The functionality of the CLI can be extended by using plugins. For a list of all available plugins, run ` ` hasura3 plugins list ` `, or visit this repository: https://github.com/hasura/cli-plugins-index.
If you're interested  in  contributing, please  open  a PR against this repo to  add  new plugin.
Usage:
  hasura3 plugins  [ command ]
Aliases:
  plugins, plugin
Available Commands:
   install      Install a plugin from the index
  list        List all available plugins from index, versions and installation status
  uninstall   Uninstall a plugin
  upgrade     Upgrade a plugin to a newer version
Flags:
  -h, --help    help   for  plugins
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
Use  "hasura3 plugins [command] --help"   for   more  information about a command.
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/plugins/#synopsis)
