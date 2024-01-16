# Working with connectors via the CLI connector plugin

This Hasura CLI plugin enables deployment and management of custom Hasura Data Connector agents to Hasura Cloud.

## Install the Hasura CLI Data Connector plugin​

To start deploying Data Connectors using the Data Connector plugin, the following pre-requisites need to be in place:

1. Install Hasura CLI
2. Update plugin index
3. Install cloud plugin
4. Authenticate the CLI with Hasura Cloud
5. Install connector plugin
6. Verify installation with the --help flag


hasura3 plugins list

hasura3 plugins install cloud

hasura3 login --pat your-personal-access-token

hasura3 plugins install connector

hasura3 connector --help

Personal Access Token (PAT)

You can generate a personal access token[ here ](https://cloud.hasura.io/account-settings/access-tokens).

## Uninstall the Hasura CLI Data Connector plugin​

To uninstall the Hasura CLI Data Connector plugin, use the `uninstall` command:

`hasura3 plugins uninstall connector`

## Usage​

Once you have the connector plugin installed you should be able to use the plugin to create and delete hosted
connectors.

Usage help:

```
> hasura3 connector --help
This Hasura CLI plugin enables deployment and management of custom Hasura data connector agent to Hasura cloud.
Further Reading:
  - https://hasura.io/docs/latest/databases/data-connectors/
  - https://github.com/hasura/graphql-engine/tree/master/dc-agents/reference
  - https://github.com/hasura/graphql-engine/blob/master/dc-agents/DOCUMENTATION.md
Usage:
  connector [command]
Available Commands:
  completion             Generate the autocompletion script for the specified shell
  create                 Create a new Hasura Cloud connector using CLI
  delete                 Delete a Hasura Cloud connector.
  generate-configuration Generate Hasura Connector configuration for the connector given in the flag --github-repo-url
  help                   Help about any command
  list                   List all Hasura Cloud data connectors owned by the user.
  logs                   Tails logs of a deployed custom Hasura data connector.
  status                 Prints the current status of the custom Hasura data connector deployment.
  version                get version information of connector CLI
Flags:
  -h, --help   help for connector
```

Create a connector:

```
hasura3 connector create my-connector:v1 \
  --github-repo-url https://github.com/hasura/cool-connector/tree/v0.7 \
  --config-file conf.json
```

Delete a connector:

`hasura3 connector delete my-connector:v1`

## Advanced Options​

### --env​

`--env`

To set environment variables when creating a connector you can use the `--env` flag:

```
hasura3 connector create my-connector:v1 \
  --github-repo-url https://github.com/hasura/cool-connector/tree/v0.7 \
  --config-file conf.json \
  --env LOG_LEVEL=DEBUG
```

### --volume​

`--volume`

To mount a volume for access by the connector you can use the[ docker --volume syntax ](https://docs.docker.com/storage/volumes/#choose-the--v-or---mount-flag).

This will provide the specified file or directory to the build process:

```
hasura3 connector create my-connector:v1 \
  --github-repo-url https://github.com/hasura/cool-connector/tree/v0.7 \
  --config-file conf.json \
  --volume ./my_data:/data
```

WARNING: Connector authors must have a `COPY` command in their `Dockerfile` corresponding to the expected volume mount
location.

### SERVICE_TOKEN_SECRET Environment Variable​

`SERVICE_TOKEN_SECRET`

If you wish your connector to only be accessed by Hasura you should set the `SERVICE_TOKEN_SECRET` environment variable
to a secure token and then configure your project metadata with the same token (ideally via the secrets function).

For example:

```
# Generate a secret token
> openssl rand  -base64 40
fErSXC6HDplAZtqxbHJVUmGqGG8AmtJleBquxeNhDsS0CCeXwTYJbg==
# Deploy Connector using token
> hasura3 connector create my-connector:v1 \
  --github-repo-url https://github.com/hasura/cool-connector/tree/v0.7 \
  --config-file conf.json \
  --env SERVICE_TOKEN_SECRET=fErSXC6HDplAZtqxbHJVUmGqGG8AmtJleBquxeNhDsS0CCeXwTYJbg==
> hasura3 connector list
my-cool-connector:v1 https://connector-9XXX7-hyc5v23h6a-ue.a.run.app active
# Include in project metadata
> code metadata.hml
> head metadata.hml
kind: DataSource
name: sendgrid
dataConnectorUrl:
  url: 'https://connector-9XXX7-hyc5v23h6a-ue.a.run.app'
auth:
  type: Bearer
  token: "fErSXC6HDplAZtqxbHJVUmGqGG8AmtJleBquxeNhDsS0CCeXwTYJbg=="
```

See the[ CLI secret documentation ](https://hasura.io/docs/3.0/cli/commands/secret/)for information on how to securely configure secrets
such as this token in your projects.

### What did you think of this doc?

- [ Install the Hasura CLI Data Connector plugin ](https://hasura.io/docs/3.0/connectors/deployment/plugin/#install-the-hasura-cli-data-connector-plugin)
- [ Uninstall the Hasura CLI Data Connector plugin ](https://hasura.io/docs/3.0/connectors/deployment/plugin/#uninstall-the-hasura-cli-data-connector-plugin)
- [ Usage ](https://hasura.io/docs/3.0/connectors/deployment/plugin/#usage)
- [ Advanced Options ](https://hasura.io/docs/3.0/connectors/deployment/plugin/#advanced-options)
    - [ --env ](https://hasura.io/docs/3.0/connectors/deployment/plugin/#--env)

- [ --volume ](https://hasura.io/docs/3.0/connectors/deployment/plugin/#--volume)

- [ SERVICE_TOKEN_SECRET Environment Variable ](https://hasura.io/docs/3.0/connectors/deployment/plugin/#service_token_secret-environment-variable)