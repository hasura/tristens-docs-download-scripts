# Secrets

## Introduction​

Secrets are a means of storing sensitive information as key-value pairs that you don't want exposed in your `metadata.hml` file. This could be anything from a database password to an API key.

Secrets are stored in Hasura DDN and can be accessed by a single[ project ](https://hasura.io/docs/3.0/ci-cd/projects/).

## Secrets lifecycle​

### Set​

To create — or **set** — a secret, you'll first need a[ project ](https://hasura.io/docs/3.0/ci-cd/projects/)on Hasura DDN. Then, create
the secret using the CLI:

`hasura3 secret  set  --project  < PROJECT_NAME >  --environment  < ENVIRONMENT_NAME >  --subgraph  < SUBGRAPH_NAME >   --key  < KEY >  --value  < VALUE >  --description  "<DESCRIPTION>"`

### Use​

You can then use the key in your `hml` file:

```
connectionUri :
   uri :
     stringValueFromSecret :  <KEY >
```

### Delete​

You can delete a secret using the following command:

`hasura3 secret delete --project  < PROJECT_NAME >  --environment  < ENVIRONMENT_NAME >  --subgraph  < SUBGRAPH_NAME >   --key  < KEY >`

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/ci-cd/secrets/#introduction)
- [ Secrets lifecycle ](https://hasura.io/docs/3.0/ci-cd/secrets/#secrets-lifecycle)
    - [ Set ](https://hasura.io/docs/3.0/ci-cd/secrets/#set)

- [ Use ](https://hasura.io/docs/3.0/ci-cd/secrets/#use)

- [ Delete ](https://hasura.io/docs/3.0/ci-cd/secrets/#delete)
