# Environments

## Introduction​

Environments allow you to organize your[ project ](https://hasura.io/docs/3.0/ci-cd/projects/)metadata by creating different environments for
different stages of your development lifecycle. You can create environments for `development` , `staging` , and `production` and then use them to create different builds for each environment.

Once you've created an environment you can then use it to create different builds by configuring a build profile file
for it. You'll then be able to access this environment's applied build via a different API endpoint.

## Environment lifecycle​

### Create​

You can create a new environment on Hasura DDN using the CLI by running:

`hasura3 environment create --name  < ENVIRONMENT_NAME >`

The CLI will return a response specifying the fully-qualified domain name of the environment, such as:

```
+------+--------------------------------------------+
| Name | testing                                    |
+------+--------------------------------------------+
| Fqdn | secure-catfish-9299-testing.ddn.hasura.app |
+------+--------------------------------------------+
```

In the Console, you'll now see the environment listed as an option in the project and you can select it to view the
builds for that environment.

### Manage​

Once you've created an environment, you can then use it to create different builds by configuring a build profile file
to reference the environment name under the `environments` key:

```
# build-profile-staging.yaml
version :   2
spec :
   environment :  staging
   mode :  replace
   supergraph :
     resources :
       -  supergraph - staging/*
   subgraphs :
     -   name :  default
       resources :
         -   "subgraphs/staging/**/*.hml"
```

In the example above, the `staging` environment, which would have been created in the previous step, is used for the
build.

We can title this file `build-profile-staging.yaml` and then reference it in the `hasura.yaml` file as an item in the
array of `buildProfiles` :

```
version :   1
project :  secure - catfish - 9299
buildProfiles :
   -  build - profile.yaml
   -  build - profile - staging.yaml
defaultBuildProfile :  build - profile.yaml
```

### Delete​

You can delete an environment using the CLI by running:

`hasura3 environment delete --name  < ENVIRONMENT_NAME >`

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/ci-cd/environments/#introduction)
- [ Environment lifecycle ](https://hasura.io/docs/3.0/ci-cd/environments/#environment-lifecycle)
    - [ Create ](https://hasura.io/docs/3.0/ci-cd/environments/#create)

- [ Manage ](https://hasura.io/docs/3.0/ci-cd/environments/#manage)

- [ Delete ](https://hasura.io/docs/3.0/ci-cd/environments/#delete)
