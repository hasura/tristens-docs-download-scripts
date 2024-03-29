# Configuration

## Introduction​

Hasura v3 introduces a new configuration model for projects on the Hasura Data Delivery Network (DDN). This model relies
on three types of files:

| File type | Description |
|---|---|
|  `hasura. yaml`  | The main configuration file. |
|  `build-profile-*. yaml`  | Build profiles for a project. |
|  `*. hml`  | Hasura metadata files for a project. |


### hasura.yaml​

This is the entry point to a Hasura project.

```
version :   1
project :  <PROJECT_NAME >
buildProfiles :
   -  build - profile.yaml
defaultBuildProfile :  build - profile.yaml
```

The `version` section is used to specify the version of the configuration file. The `project` field is used to specify
the project name.

The `hasura.yaml` file also contains a `buildProfiles` section. This section is used to specify the build profile files
associated with the project. As you can see from this example, we only have one build profile, `build-profile.yaml` which is also identified as the default to use when creating a new build. **The  default  profile is required for a
project.** 

`default`

### Build profiles​

Build profiles tell Hasura DDN how to construct your supergraph. A build profile will contain information about the
shared resources — such as your authentication configuration — and the resources belonging to the individual subgraphs
that make up your supergraph.

By default, the included `build-profile.yaml` file is populated with the following content:

```
version :   2
spec :
   environment :  default
   mode :  replace
   supergraph :
     resources :
       -  supergraph/*
   subgraphs :
     -   name :  default
       resources :
         -   "subgraphs/default/**/*.hml"
```

Here, you can see that the `build-profile.yaml` file contains `version` and `spec` sections. The `version` section is
used to specify the version of the configuration file.

The `spec` section contains the following fields:

| Field | Description |
|---|---|
|  `environment`  | The environment to use for the build. |
|  `mode`  | The mode to use for the build. `Replace` by default. |
|  `supergraph`  | The supergraph resources to use for the build. |
|  `subgraph`  | List of subgraphs and their resources to use for the build |


You can create additional build profile files for different environments you may need e.g., `staging` , `production` ,
etc. By combining build profiles which specify environments with version control, you can easily set up an effective
CI/CD pipeline for your project.

Each build profile file must be referenced by the `hasura.yaml` file in order to be used.

### Supergraph​

Your `supergraph` directory will contain two configuration files by default: the `auth-config.hml` and `compatibility-config.hml` files.

The `auth-config.hml` file defines the authentication configuration for your supergraph i.e., the configuration for how
the queries to your Hasura DDN project should be authenticated. The `compatibility-config.hml` file defines the
compatibility date of your supergraph metadata. You'd likely not want to change the compatibility config unless you're
sure about it.

#### AuthConfig​

```
kind :  AuthConfig
version :  v1
definition :
   allowRoleEmulationBy :  admin
   mode :
     webhook :
       method :  Post
       url :  https : //auth.pro.hasura.io/webhook/ddn ? role=admin
```

The `AuthConfig` object is used to configure authentication for your data supergraph. You can learn more about
authentication in the[ Auth section ](https://hasura.io/docs/3.0/auth/overview/).

#### CompatibilityConfig​

```
kind :  CompatibilityConfig
date :   2023-10-19
```

The `CompatibilityConfig` object is used to configure the compatibility of your metadata with Hasura.

##### Compatibility Date​

The `CompatibilityConfig` object contains a `date` field which opts your metadata out of all backwards incompatible
changes made after that date. Any backwards incompatible changes made to Hasura DDN after that date won't impact your
metadata.

When starting a new project, this date should be set to today's date so that the most up-to-date behavior of Hasura is
used.

Older projects should also periodically update the compatibility date after going over the behavioral changes that have
happened since that older date.

### Subgraphs​

Inside the `subgraphs` directory, each subgraph is identified by a directory with the name of the subgraph. Within that,
we have included three directories to get you started:

```
└──  < SUBGRAPH_NAME >
│       ├── commands
│       ├── dataconnectors
│       └── models
```

A project is divided into one or more separate subgraphs which are referenced by a build profile.

The `default` subgraph is required and cannot be deleted.

Subgraphs can be used to group together objects in your metadata in a way that makes sense for you and your team.
Multiple `hml` files can belong to a subgraph, and you can have multiple subgraphs in a project. Objects in each hml
file must conform to the[ OpenDD Spec ](https://hasura.io/docs/3.0/data-domain-modeling/overview/)and[ subgraph rules ](https://hasura.io/docs/3.0/ci-cd/subgraphs/).

The CLI populates the `default` subgraph with `command` , `dataconnectors` , and `model` directories, but the organization
of these is completely customizable by you and your team.

What is HML?

These are both `hml` files, which is a new file format for Hasura metadata. It is a superset of the existing `yaml` format, and is designed to provide a more flexible and extensible way to define metadata. You can leverage the power of
the[ Hasura VS Code extension ](https://marketplace.visualstudio.com/items?itemName=HasuraHQ.hasura)to quickly and
easily author `hml` files.

Your `hml` files contain metadata objects according to the OpenDD spec. In the example above, we could add a `HasuraHubDataConnector` object to connect to a data source. Then, import our tables as models and create a build on
Hasura DDN.

However, in the next section, we'll look at how to use subgraphs to organize metadata and break up our `hml` file into
smaller, more governable pieces.

## Basic configuration​

When using the[ hasura3 CLI ](https://hasura.io/docs/3.0/cli/overview/)to create a new project, you'll run the following command:

`hasura3 init --dir  .`

This will generate a new project directory in the current folder with the following structure:

```
< PROJECT_DIRECTORY >
├── build-profile.yaml
├── hasura.yaml
├── subgraphs
│   └── default
│       ├── commands
│       ├── dataconnectors
│       └── models
└── supergraph
    ├── auth-config.hml
    └── compatibility-config.hml
```

.gitkeep

You will find empty .gitkeep files in some directories which are used to preserve empty directories in Git.

## Advanced configuration​

Let's consider a data supergraph wherein you'd like to test your API across multiple[ environments ](https://hasura.io/docs/3.0/ci-cd/environments/). We can use subgraphs to organize our metadata and break up our `hml` file into
smaller, more governable pieces. We can also utilize build profiles to create different builds for different
environments.

Imagine this file structure:

```
< PROJECT_NAME >
├── build-profile.yaml
├── build-profile-staging.yaml
├── hasura.yaml
├── subgraphs
│   └── app
│       ├── commands
│       ├── dataconnectors
│           └── app.hml
│       └── models
│           ├── cart_items.hml
│           ├── carts.hml
│           ├── categories.hml
│           ├── coupons.hml
│           ├── manufactuers.hml
│           ├── notifications.hml
│           ├── orders.hml
│           ├── products.hml
│           ├── reviews.hml
│           └── users.hml
└── supergraph
    ├── auth-config.hml
    └── compatibility-config.hml
```

### Build profiles​

In this example, we have two build profiles: `build-profile.yaml` and `build-profile-staging.yaml` . The `build-profile.yaml` file contains the following content:

```
version :   2
spec :
   environment :  default
   mode :  replace
   supergraph :
     resources :
       -  supergraph/*
   subgraphs :
     -   name :  app
       resources :
         -   "subgraphs/**/*.hml"
```

Whereas the `build-profile-staging.yaml` file contains the following content:

```
version :   2
spec :
   environment :  staging
   mode :  replace
   supergraph :
     resources :
       -  supergraph/*
   subgraphs :
     -   name :  app
       resources :
         -   "subgraphs/**/*.hml"
```

The two build profiles, `build-profile.yaml` and `build-profile-staging.yaml` , are designed to cater to different
environments. The `build-profile.yaml` is configured for the default environment and is set to include all subgraphs in
the subgraphs directory. This configuration is suitable for a general development team working on various parts of the
project.

As this is the default build profile, it will be used when you run the following command:

`hasura3 build create`

On the other hand, `build-profile-staging.yaml` is specifically configured for the staging environment and is intended
for testing with other staging services.

You can create a build with this profile by running the following command:

`hasura3 build create --profile build-profile-staging.yaml`

### hasura.yaml​

The `hasura.yaml` in the root of the project contains the following content:

```
version :   1
project :  <PROJECT_NAME >
buildProfiles :
   -  ./build - profile.yaml
   -  ./build - profile - staging.yaml
defaultBuildProfile :  build - profile.yaml
```

This lets Hasura DDN know that we have two build profiles, and that the `build-profile.yaml` is the default to use when
creating a new build.

### Custom Directory Structure​

You could choose to deviate from the default directory structure that the Hasura project initializes for you into one
that suits you and your team's needs.

For example, you could have a single file with all the metadata objects, including your `HasuraHubDataConnector` objects, models, and commands, as long as you specify that file to be in your subgraph resources in the build profile.
However, this would be difficult to manage and maintain.

You could also choose to arrange your subgraphs by data type. E.g., `subgraphs/default/users` , `subgraphs/defaultproducts` , etc.

The contents of the `hml` files can be that of any valid OpenDD metadata object as long as they conform to the rules of[ subgraphs ](https://hasura.io/docs/3.0/ci-cd/subgraphs/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/ci-cd/config/#supergraph/#introduction)
    - [ hasura.yaml ](https://hasura.io/docs/3.0/ci-cd/config/#supergraph/#hasurayaml)

- [ Build profiles ](https://hasura.io/docs/3.0/ci-cd/config/#supergraph/#build-profiles)

- [ Supergraph ](https://hasura.io/docs/3.0/ci-cd/config/#supergraph/#supergraph)

- [ Subgraphs ](https://hasura.io/docs/3.0/ci-cd/config/#supergraph/#subgraphs)
- [ Basic configuration ](https://hasura.io/docs/3.0/ci-cd/config/#supergraph/#basic-configuration)
- [ Advanced configuration ](https://hasura.io/docs/3.0/ci-cd/config/#supergraph/#advanced-configuration)
    - [ Build profiles ](https://hasura.io/docs/3.0/ci-cd/config/#supergraph/#build-profiles-1)

- [ hasura.yaml ](https://hasura.io/docs/3.0/ci-cd/config/#supergraph/#hasurayaml-1)

- [ Custom Directory Structure ](https://hasura.io/docs/3.0/ci-cd/config/#supergraph/#custom-directory-structure)
