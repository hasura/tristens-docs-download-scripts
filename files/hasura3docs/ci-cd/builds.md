# Builds

## Introduction​

A build is a fully-functional, immutable supergraph which is built based on your project configuration.

Builds are created for a specific[ environment ](https://hasura.io/docs/3.0/ci-cd/environments/)and can be used to incrementally test your
project's API.

While there can be many builds for an environment, only one can be **applied** at a time to an environment. The applied
build is the one that is currently serving your API from your project's endpoint.

## Build lifecycle​

### Create​

To create a build, you'll first need a[ project ](https://hasura.io/docs/3.0/ci-cd/projects/). After which, you can create a build using the
following command:

`hasura3 build create`

The CLI will return information about your build:

```
+---------------+---------------------------------------------------------------+
| Build ID      | baa7f15d-5364-4cfd-b94c-8d2a8a51e6e2                          |
+---------------+---------------------------------------------------------------+
| Build Version | b6370d7d56                                                    |
+---------------+---------------------------------------------------------------+
| Build URL     | https://secure-catfish-9299-b6370d7d56.ddn.hasura.app/graphql |
+---------------+---------------------------------------------------------------+
| Project Id    | fc2d7717-e1f8-4213-9132-6a70f78b6026                          |
+---------------+---------------------------------------------------------------+
| Console Url   | https://console.hasura.io/project/secure-catfish-9299/graphql |
+---------------+---------------------------------------------------------------+
| FQDN          | secure-catfish-9299-b6370d7d56.ddn.hasura.app                 |
+---------------+---------------------------------------------------------------+
| Environment   | default                                                       |
+---------------+---------------------------------------------------------------+
| Description   |                                                               |
+---------------+---------------------------------------------------------------+
```

By default, the build will be created using the build profile you've identified as the default for your project in your `hasura.yaml` file. You can override this by specifying a different profile using the `--profile` flag:

`hasura3 build create --profile  < BUILD_PROFILE_FILE >`

At this point, you can interact with and test your API using the GraphQL API Endpoint and Console URL returned by the
CLI.

### Apply​

When you are happy with your build, you can apply it to a project's environment using the following command:

`hasura3 build apply --version  < BUILD_VERSION >`

The CLI will return the API endpoint for your supergraph:

```
+---------+----------------------------------------------------+
| API URL | https://secure-catfish-9299.ddn.hasura.app/graphql |
+---------+----------------------------------------------------+
```

### Delete​

Builds can be individually deleted using the following command:

`hasura3 build delete --version  < BUILD_VERSION >`

All builds for a project are deleted when a[ project is deleted ](https://hasura.io/docs/3.0/ci-cd/projects/#delete).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/ci-cd/builds/#introduction)
- [ Build lifecycle ](https://hasura.io/docs/3.0/ci-cd/builds/#build-lifecycle)
    - [ Create ](https://hasura.io/docs/3.0/ci-cd/builds/#create)

- [ Apply ](https://hasura.io/docs/3.0/ci-cd/builds/#apply)

- [ Delete ](https://hasura.io/docs/3.0/ci-cd/builds/#delete)
