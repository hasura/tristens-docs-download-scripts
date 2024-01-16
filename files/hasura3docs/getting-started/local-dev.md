# Get Started with DDN

## Introduction​

In this guide, we'll walk you through the steps to create a new Hasura project, connect a database, execute your first
query, create lightning-fast production builds, and incorporate business logic using TypeScript — all with VS Code and
the **new Hasura CLI** . Throughout this guide, you'll be introduced to new Hasura concepts, like builds, our new
metadata structure, and more.

Get an instant API!

You can create a project via[ the Console ](https://console.hasura.io)— our web-based GUI — to spin up an API by just
providing a database url. However, we recommended you follow the guide on this page to set up your project via the CLI,
which will allow you to easily iterate on your project.

## Step 1: Prerequisites​

1. Install the[ new Hasura CLI ](https://hasura.io/docs/3.0/cli/installation/)
2. Install the[ Hasura VS Code extension ](https://marketplace.visualstudio.com/items?itemName=HasuraHQ.hasura)
3. Have a PostgreSQL database


You can connect a local PostgreSQL database to Hasura DDN using the new[ Hasura CLI ](https://hasura.io/docs/3.0/cli/overview/). If you don't
have a PostgreSQL database and prefer to connect to a cloud provider, check out our friends at[ Neon ](https://neon.tech).

Don't want to set up a database?

We've provisioned a read-only database for you to use for this guide if you'd like. You can use the following connection
string in Step 3:

`postgresql://read_only_user:readonlyuser@35.236.11.122:5432/v3-docs-sample-app`

I don't use VS Code

Good news! LSP support is coming soon to other editors. In the meantime, give[ VS Code ](https://code.visualstudio.com/download)a try — it's a great editor!

## Step 2: Log into Hasura​

After our prerequisites are taken care of, log into Hasura Cloud with the CLI:

`hasura3 login`

This will open up a browser window and initiate an OAuth2 login flow. If the browser window doesn't open automatically,
use the link shown in the terminal output to launch the flow.

New CLI?!

Yep! If you can't tell already, we've completely rewritten the CLI from the ground up. You can learn more about the new
commands by running:

`hasura3 --help`

## Step 3: Create a new project​

To create a new project, use the following command, passing the directory where you want to create the project as an
argument. This command will create the configuration files and directory structure by default. It will also prompt you
to create a new Hasura DDN project in the cloud too.

```
hasura3 init --dir  < PROJECT_DIRECTORY >
cd   < PROJECT_DIRECTORY >
```

The CLI will prompt you with the following:

```
Use the arrow keys to navigate: ↓ ↑ → ←
Please choose how you would like to initialise Hasura DDN?
  Create a new project         |          ( Start building on a new DDN project )
    Empty project
```

Choose `Create a new project` and the CLI will respond with the following:

```
Creating a new project
Creating hasura.yaml  .. .
Creating build-profile  .. .
Creating metadata.hml  .. .
Project  < PROJECT_NAME >  is created at  < DIR >
```

What's a project?

Each project on Hasura DDN can have a corresponding local project that can be used for development. This local project
contains the following structure by default:

```
├── build-profile.yaml
├── hasura.yaml
├── subgraphs
│   └── default
│       ├── commands
│       ├── dataconnectors
│       └── models
└── supergraph
    ├── auth-config.hml
    └── compatibility-config.hml
```

We'll dive into how to use these files as we continue through this guide. However, if you'd like more information on the
new project structure, see our page on[ project configuration ](https://hasura.io/docs/3.0/ci-cd/config/).

## Step 4: Connect a data source​

The next step is to add a data source to the project so that we can build APIs on that source. With Hasura DDN, a source
is added through a Data Connector. We will use the[ Postgres Data Connector ](https://hasura.io/connectors/postgres).

`hasura3 metadata add-hub-connector pg_db --dir  .  --subgraph default --id hasura/postgres --url  "postgresql://read_only_user:readonlyuser@35.236.11.122:5432/v3-docs-sample-app"`

This will also create a `.env` in the root of your project with the connection string you provided. This allows you to
use `.gitignore` to ignore the `.env` file and keep your connection string safe when committing your project to version
control.

We're passing a few flags to this command:

- `--dir .` tells the CLI to use the current directory as the project directory.
- `--subgraph default` tells the CLI to add the data source to the default[ subgraph ](https://hasura.io/docs/3.0/ci-cd/subgraphs/).
- `--id hasura/postgres` tells the CLI to use the `hasura/postgres` connector from the[ connector hub ](https://hasura.io/connectors).


Don't want to use our DB?

If you don't want to use our demo Postgres database, or you have a local database you want to try out with Hasura,
replace the url with your connection string.

For example, you can use a generic postgres connection string: `postgresql://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DATABASE_NAME>` . This works with local databases, too — you can
create a[ Secure Connect tunnel ](https://hasura.io/docs/3.0/ci-cd/tunnels/).

## Step 5: Start watch mode​

Now that we have added a data source and scaffolded our metadata, let's start Hasura's watch mode so that when we make
changes, our GraphQL API will update automatically:

`hasura3  watch  --dir  .`

The CLI will respond with the following warning to ensure you don't accidentally apply a build to your production
environment:

```
This command will create new builds in the selected environment "default" and change the current applied build.
We recommend using a test environment so that there is no disruption to existing work.
Do you want to continue?
```

This command will take over the current terminal tab and watch for changes to the folder. This will keep creating and
applying new **builds** — that represent a new version of the GraphQL API — as you make changes. If you'd like to learn
more about watch mode and what flags you can pass, check out the[ CLI docs on watch mode ](https://hasura.io/docs/3.0/cli/commands/watch/).

If you are using a local Postgres database, this command also creates a tunnel to your local machine to make the
database available to Hasura DDN.

Watch mode is for development only

You should not use watch mode in production. This leads to security vulnerabilities and performance issues.

What's a build?

This is the first concept we've introduced in this guide. Builds are a new concept in Hasura that allow you to quickly
iterate and prototype on your project's metadata. A build is an immutable, fully-functioning GraphQL API that represents
a milestone in your development cycle.

It may be helpful to think of builds as git commits. Since each is deployed on Hasura DDN, it can be shared with other
users.

Each build is completely independent. One project can have multiple builds, out of which, one is applied to production.
This workflow allows for easier rollbacks on production, and greater collaboration during development.

## Step 6: Launch VS Code and track tables​

Make sure the[ Hasura VS Code extension ](https://marketplace.visualstudio.com/items?itemName=HasuraHQ.hasura)is
installed and that you have logged in.

Launch VS Code in the project directory:

`code  < PROJECT_DIRECTORY >`

To log in, open the command palette (Ctrl+Shift+P or Cmd+Shift+P) and type `Hasura: Login` . This will open a browser
window and initiate a login flow. If the browser window doesn't open automatically, use the link shown in the
notification from VS Code to launch the flow.

Open the new `hml` file that was created at `subgraphs/default/dataconnectors/pg_db/pg_db.hml` . You'll see that Hasura
automatically introspected your data source and created your schema for you. From here, you can immediately track all
tables, views, relationships, and quickly scaffold out your metadata by using the Hasura VS Code extension.

Bring up the command palette, type `hasura track all` , and choose the option from the dropdown. Then, select your data
source's name (e.g., `pg_db` ) from the dropdown.

Your metadata files will be populated with everything you need to get started! 🎉

Image: [ VSCode data connector ](https://hasura.io/docs/3.0/assets/images/0.0.1_vscode-track-table-b3838e2adf2662239ee5f2054552bb2f.png)

A lot happened under the hood. Let's break it down:

- Within the `subgraphs/default/dataconnectors/pg_db` directory, a new `pg_types.hml` file was generated.
    - This file contains all of the types that were introspected from your data source and that your API will use.
- Within the `models` subdirectory, new named files for each of your models were created.
    - These files contain the metadata for each model, including their fields, permissions, relationships, and more.


What are models?

Models are a new way to represent your data in Hasura.

Models in the[ OpenDD Spec ](https://hasura.io/docs/3.0/data-domain-modeling/overview/)refer to a collection of objects (such as rows in a
relational database, or documents in a NoSQL database) of a given OpenDD Spec[ type ](https://hasura.io/docs/3.0/data-domain-modeling/types/).
Models are backed by a data source and can support CRUD operations. You can learn more about models[ here ](https://hasura.io/docs/3.0/data-domain-modeling/models/).

Ideally, you'll want to separate out each model into its own file. However, for the sake of this guide, we've kept them
all in one file.

## Step 7: Run your first query​

Head to the terminal where `hasura3 watch` is running. A new build was automatically generated when you imported models;
you can visit this using the link in the terminal output.

```
+---------------+------------------------------------------------------------+
| Build ID      | <BUILD_ID>                                                 |
+---------------+------------------------------------------------------------+
| Build Version | <BUILD_VERSION>                                            |
+---------------+------------------------------------------------------------+
| Build URL     | https://<PROJECT_NAME_AND_BUILD_ID>.ddn.hasura.app/graphql |
+---------------+------------------------------------------------------------+
| Project Id    | <PROJECT_ID>                                               |
+---------------+------------------------------------------------------------+
| Console Url   | https://console.hasura.io/project/<PROJECT_NAME>/graphql   |
+---------------+------------------------------------------------------------+
| FQDN          | <PROJECT_NAME_AND_BUILD_ID_STUB>.ddn.hasura.app            |
+---------------+------------------------------------------------------------+
| Environment   | default                                                    |
+---------------+------------------------------------------------------------+
```

We're using the docs sample app's schema for this guide's visuals, but you can use the GraphiQL Explorer to create your
query or write it manually:

Image: [ Execute a query ](https://hasura.io/docs/3.0/assets/images/0.0.1_console-execute-query-on-build-859fb8dd4c06c6f70a219ad293d06b76.png)

```
query   OrdersQuery   {
   orders   {
     id
     status
     delivery_date
     user   {
       id
       name
       email
     }
     product   {
       id
       name
     }
   }
}
```

## Step 8: Incorporate custom business logic​

With DDN, Hasura introduces a new way of writing custom business logic using the the TypeScript connector. This exposes
functions or procedures that can be added to Hasura metadata as a[ command ](https://hasura.io/docs/3.0/data-domain-modeling/commands/), which
can be made available over the GraphQL API as a query or a mutation.

First, we'll kill the `hasura watch` session by pressing `Ctrl + C` in the terminal. Then, we can create a new
TypeScript connector using the following command in the project's root:

`hasura3 metadata add-hub-connector ts_logic --dir  .  --subgraph default --id hasura/ts-deno --url http://localhost:8100`

This command will create all necessary files required by the `ts-deno` connector, including the DataConnector metadata
and TypeScript functions.

Now that we added a new connector, head to the tab where `hasura3 watch` was running and restart the command. Deno's
required to run the TypeScript connector locally, so you'll need to install it if you haven't already:

```
# install deno
curl  -fsSL https://deno.land/x/install/install.sh  |   sh
# start hasura watch
hasura3  watch
```

This command will now start the connector locally using `deno` and then creates a tunnel from Hasura Cloud to your local
machine so that it is reachable.

There will be a new file called `index.ts` in this directory. This file will contain a simple hello world function:

```
// subgraphs/default/dataconnectors/ts_logic/index.ts
export   function   hello ( ) :   string   {
   return   "hello world" ;
}
```

## Step 9: Track the function as a procedure​

Switch to VS Code and open `subgraphs/default/dataconnectors/ts_logic/ts_logic.hml` . The procedure `helloWorld` will be
underlined with a code action to track the function as a command in the subgraph. This will create a command metadata
object which will expose this function as a mutation. Just like before, your types will be generated for you.

Image: [ Track a function in VSCode ](https://hasura.io/docs/3.0/assets/images/0.0.1_track-ts-27a9cdab928f5b7a14faed965ea9be34.png)

## Step 10: Execute the function using GraphiQL​

A new build has been generated for you. You can run the following mutation in the GraphiQL Explorer to execute the
function:

```
mutation   tsFunctionQuery   {
   hello
}
```

Image: [ Track a function in VSCode ](https://hasura.io/docs/3.0/assets/images/0.0.1_ts-mutation-1456889263c8dc355b606bc765f3547a.png)

Since Deno and Hasura are watching for changes, you can modify the function and it will automatically update the API and
be available on DDN 🎉

## Step 11: Apply a build to production​

As we've been developing our API, Hasura generated new builds for us in the background. We can see these builds by
running the following command:

`hasura3 build list`

```
+---------------+-------------+------------+--------------------------------------------+--------------------------------+--------------------------------+
| BUILD VERSION | ENVIRONMENT | IS APPLIED |                 BUILD URL                  |          DESCRIPTION           |           CREATED AT           |
+---------------+-------------+------------+--------------------------------------------+--------------------------------+--------------------------------+
| dea725b352    | default     | true       | native-calf-5513-dea725b352.ddn.hasura.app | Watch build Thu, 30 Nov 2023   | Thu, 30 Nov 2023 15:35:00      |
|               |             |            |                                            | 09:34:58 CST                   | +0000                          |
+---------------+-------------+------------+--------------------------------------------+--------------------------------+--------------------------------+
```

Watch mode also **automatically** applies the newest build to the environment it's watching. This is one reason why
watch mode is incredibly powerful during development.

If you're not using watch mode, you can apply a build — which means it will serve as the API for the current
environment's build — using the following command:

`hasura3 build apply --version  < BUILD_VERSION >`

## What's next?​

### Iterate on your metadata​

We've just demonstrated how to quickly get set up and running with Hasura. Now that you've got a project up and running,
you can iterate on your metadata and build out your API. Head back to your IDE, make some modifications, create a new
build, and see what happens 🎉

Learn more about structuring your data supergraph by checking out our[ Data Domain Modeling ](https://hasura.io/docs/3.0/data-domain-modeling/overview/)section.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/getting-started/local-dev/#introduction)
- [ Step 1: Prerequisites ](https://hasura.io/docs/3.0/getting-started/local-dev/#step-1-prerequisites)
- [ Step 2: Log into Hasura ](https://hasura.io/docs/3.0/getting-started/local-dev/#step-2-log-into-hasura)
- [ Step 3: Create a new project ](https://hasura.io/docs/3.0/getting-started/local-dev/#step-3-create-a-new-project)
- [ Step 4: Connect a data source ](https://hasura.io/docs/3.0/getting-started/local-dev/#step-4-connect-a-data-source)
- [ Step 5: Start watch mode ](https://hasura.io/docs/3.0/getting-started/local-dev/#step-5-start-watch-mode)
- [ Step 6: Launch VS Code and track tables ](https://hasura.io/docs/3.0/getting-started/local-dev/#step-6-launch-vs-code-and-track-tables)
- [ Step 7: Run your first query ](https://hasura.io/docs/3.0/getting-started/local-dev/#step-7-run-your-first-query)
- [ Step 8: Incorporate custom business logic ](https://hasura.io/docs/3.0/getting-started/local-dev/#step-8-incorporate-custom-business-logic)
- [ Step 9: Track the function as a procedure ](https://hasura.io/docs/3.0/getting-started/local-dev/#step-9-track-the-function-as-a-procedure)
- [ Step 10: Execute the function using GraphiQL ](https://hasura.io/docs/3.0/getting-started/local-dev/#step-10-execute-the-function-using-graphiql)
- [ Step 11: Apply a build to production ](https://hasura.io/docs/3.0/getting-started/local-dev/#step-11-apply-a-build-to-production)
- [ What's next? ](https://hasura.io/docs/3.0/getting-started/local-dev/#whats-next)
