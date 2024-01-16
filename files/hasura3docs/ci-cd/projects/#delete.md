# Projects

## Introduction​

Broadly, a project is the configuration of your data supergraph.

A project specifies build profiles, each of which specify supergraph and subgraph configurations that are used create[ builds ](https://hasura.io/docs/3.0/ci-cd/builds/)which are snapshots of the project config and are used to serve your API.

## Initialize a Project​

We can create a new project and link it to its twin on Hasura DDN by using the Hasura CLI to create a new project.

### Login to Hasura DDN​

In order to link local and Hasura DDN projects, you'll need to authenticate your CLI. This can be done two ways:

- Via the browser (recommended)
- Using a Personal Access Token (PAT)


#### Browser​

`hasura3 login`

This will launch a browser window and prompt you to login to your Hasura DDN account. Once you've logged in, you can
close the browser window and return to your terminal.

#### PAT​

Alternatively, you can use a PAT to authenticate with the CLI.

You can create a PAT by navigating to the[ Access Tokens page ](https://cloud.hasura.io/account-settings/access-tokens)in your account settings. Where you can create a new token and copy the value.

Back in the Hasura CLI, run:

`hasura3 login --pat  < PAT >`

You should see a confirmation that you're now successfully logged in, and can now create a new project and
simultaneously link it to its twin on Hasura DDN.

### Create a new project​

`hasura3 init --dir  .`

You will be presented with the following options:

```
Create a new project
Empty project
```

Choose `Create a new project` .

### Configure a project​

The previous command will create a project on Hasura DDN and local files in a directory structure which will be used to
manage your project.

For more information on the project configuration files, see the[ configuration section ](https://hasura.io/docs/3.0/ci-cd/config/).

Running CLI commands without specifying a project name each time

By logging into Hasura DDN via the CLI and specifying the project name in the hasura.yaml file, the CLI will know which
project to use when running commands in the directory.

#### VS Code Extension​

The[ Hasura VS Code extension ](https://marketplace.visualstudio.com/items?itemName=HasuraHQ.hasura&ssr=false#review-details)is there to help you author and edit `hml` files in your subgraphs. It provides syntax highlighting, validation, and
autocompletion.

To use the extension, ensure you've[ installed it ](https://marketplace.visualstudio.com/items?itemName=HasuraHQ.hasura)and then run the `login` command using the command palette. You can access this by pressing `Ctrl+Shift+P` on Windows
and `Cmd+Shift+P` on Mac.

#### Create builds​

In order to see configurations in your metadata take effect you need to create a build. Head over to the[ Builds ](https://hasura.io/docs/3.0/ci-cd/builds/)section to learn about how to create and manage builds.

Alternatively, during development, you can use[ watch mode ](https://hasura.io/docs/3.0/cli/commands/watch/)to automatically create builds when
changes are detected in your project.

#### Describe a project​

You can get the relevant information of your project by using the CLI and running:

`hasura3 project describe`

You will see an output similar to the following:

```
+-------------+--------------------------------------------------------------+
| Name        | master-shrimp-9462                                           |
+-------------+--------------------------------------------------------------+
| ID          | fa2f39db-247d-4820-83c4-96cec5e6bd38                         |
+-------------+--------------------------------------------------------------+
| Console URL | https://console.hasura.io/project/master-shrimp-9462/graphql |
+-------------+--------------------------------------------------------------+
| Build Count | 1                                                            |
+-------------+--------------------------------------------------------------+
| Domain      | master-shrimp-9462.ddn.hasura.app                            |
+-------------+--------------------------------------------------------------+
```

#### List all projects​

You can list all the projects you have access to by running:

`hasura3 project list`

You will see an output similar to the following:

```
+-------------+-----------------------+--------------------------------------+-----------------------------------------------------------------+
| CREATED AT  |         NAME          |                  ID                  |                           CONSOLE URL                           |
+-------------+-----------------------+--------------------------------------+-----------------------------------------------------------------+
| 27 Nov 2023 | master-shrimp-9462    | fa2f39db-247d-4820-83c4-96cec5e6bd38 | https://console.hasura.io/project/master-shrimp-9462/graphql    |
+-------------+-----------------------+--------------------------------------+-----------------------------------------------------------------+
```

### Delete a project​

You can delete a project using the CLI by running:

`hasura3 project delete`

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/ci-cd/projects/#delete/#introduction)
- [ Initialize a Project ](https://hasura.io/docs/3.0/ci-cd/projects/#delete/#initialize-a-project)
    - [ Login to Hasura DDN ](https://hasura.io/docs/3.0/ci-cd/projects/#delete/#login-to-hasura-ddn)

- [ Create a new project ](https://hasura.io/docs/3.0/ci-cd/projects/#delete/#create-a-new-project)

- [ Configure a project ](https://hasura.io/docs/3.0/ci-cd/projects/#delete/#configure-a-project)

- [ Delete a project ](https://hasura.io/docs/3.0/ci-cd/projects/#delete/#delete-a-project)
