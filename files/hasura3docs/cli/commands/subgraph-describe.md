# Hasura3 CLI: hasura3 subgraph describe

## Synopsis​

View subgraph details[aliases: details, info].

```
$ hasura3 subgraph describe --help
View subgraph details  [ aliases: details, info ]
Usage:
  hasura3 subgraph describe  [ flags ]
Aliases:
  describe, details, info
Examples:
  # View details of a "accounting" subgraph
   hasura3 subgraph describe --project  < project-name >  --name accounting
Flags:
  -h, --help           help   for  describe
  -n, --name string   Subgraph name  ( required )
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/subgraph-describe/#synopsis)
