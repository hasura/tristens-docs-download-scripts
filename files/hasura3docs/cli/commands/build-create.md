# Hasura3 CLI: hasura3 build create

## Synopsis​

Create a build in a Hasura Cloud Project.

```
$ hasura3 build create --help
Create a build  in  a Hasura Cloud Project
Usage:
  hasura3 build create  [ flags ]
Examples:
  # Create a build with the default build profile (hasura.yaml present in current working directory)
   hasura3 build create 
  # Create a build with an alternate build profile (hasura.yaml is not present in current working directory)
   hasura3 build create --profile build-profile-staging.yaml --dir  < path-to-hasura.yaml-file >  --description  "overridden build profile"
  # Create a Patch build by overriding the value present in the selected build profile (build-profile-preprod has build mode as patch)
   hasura build create --profile build-profile-preprod.yaml --patch-on-build latest 
  # Create a build with metadata.json file (Mode: Replace)
   hasura3 build create --mode replace --project  < project-name >  --metadata-from-file  < path-to-metadata.json-file >  --environment default --description  "profiless build"
Flags:
  -d, --description string           ( Optional )  description about the build
      --dry-run                     Prints the metadata used to create the build. No build artifact is generated
      --environment string          Environment to create the build in. To be used when building with metadata JSON only. When provided, --mode, --project and --metadata-from-file must also be provided
  -h, --help                         help   for  create
      --metadata-from-file string   Path to the metadata JSON file. To be used when building with metadata JSON only. When provided, --mode, --project and --environment must also be provided
      --mode string                 Can be patch or replace. To be used when building with metadata JSON only. When provided, --metadata-from-file, --project and --environment must also be provided
      --patch-on-build string       Override the patch on build value provided  in  the build profile, only valid  if  the mode is patch. Takes a build version, applied or latest as allowed values
      --profile string              Build profile to use, uses the default build profile  if  not provided
Global Flags:
      --dir string         Hasura project directory  in   which  hasura.yaml is present  ( default  "." )
      --log-level string   Log level. accepts DEBUG, WARN, INFO, ERROR, FATAL  ( default  "INFO" )
      --no-prompt           set  this flag to no prompt  for  anything, the  command  fails  if  any input is missing
  -o, --out string          format   in   which  the output should be printed, accepts table, json and yaml  ( default  "table" )
  -p, --project string     Hasura DDN Project Name
```

### What did you think of this doc?

- [ Synopsis ](https://hasura.io/docs/3.0/cli/commands/build-create/#synopsis)