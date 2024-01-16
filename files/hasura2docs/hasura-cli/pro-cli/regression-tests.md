# Regression Tests

The Hasura CLI Pro plugin can be used to run regression tests from your terminal. This is typically useful in your CI/CD
workflows when you want to run tests in certain pipelines.

You can temporarily spin up a Hasura instance and then point the CLI to that instance to run tests.

## Setting up the test suite​

Before you can run tests, a test suite needs to be set up with operations that have been captured on your Hasura Project.

You can read more about setting up a test suite[ here ](https://hasura.io/docs/latest/cloud-ci-cd/regression-tests/#manage-test-suites).

## Getting a personal access token​

In order to communicate with Hasura's APIs, the CLI needs to be configured with an API access token.

Follow the instructions[ here ](https://hasura.io/docs/latest/hasura-cli/pro-cli/auth/)to get a personal access token (PAT).

E.g. PAT token: `ayrQdBG7UAzl642mLskLDtSuGNe7l9Bh8eIdQOtnXAG1GjxotHT38qOdSXl1smm` 

## Running a regression test suite programmatically​

### 1. Install the Hasura CLI and Pro add-on for CLI​

- [ Install ](https://hasura.io/docs/latest/hasura-cli/install-hasura-cli/)the Hasura CLI
- Install the Pro add-on for CLI: after installing the CLI, run the following command to install the add-on:


`hasura plugins  install  pro`

### 2. Configure the CI process​

Add the Pro Backend (Lux) URL endpoints and PAT token to the CI environment variables:

```
export   HASURA_PRO_METRICS_SERVER_ENDPOINT = < root-domain > /metrics
export   HASURA_PRO_DATA_SERVER_ENDPOINT = < root-domain > /data
export   HASURA_PRO_OAUTH_SERVER_ENDPOINT = < root-domain > /oauth
export   HASURA_ACCOUNT_PAT = < pat-token >
```

Note

The example assumes that the service URLs are Path based and not sub-domain based. This can be verified from the
Kubernetes Ingress rules configuration for these services. For example:

```
export   HASURA_PRO_METRICS_SERVER_ENDPOINT = mydomain.com/metrics
export   HASURA_PRO_DATA_SERVER_ENDPOINT = mydomain.com/data
export   HASURA_PRO_OAUTH_SERVER_ENDPOINT = mydomain.com/oauth
export   HASURA_ACCOUNT_PAT = ayrQdBG7UAzl642mLskLDtSuGNe7l9Bh8eIdQOtnXAG1GjxotHT38qOdSXl1smmp
```

## Running tests​

1. Head to the `Regression Testing` tab in the Hasura instance's Console.
2. In the `Run tests` tab, click `Run tests on CLI` to get the partial CLI command for running the regression tests on a
Hasura instance with the selected test suite (defined on this project or another).


For example:

`hasura pro regression-tests run --testsuite-id 17609e8f-c976-4d91-818d-235e0ac215e0 --project-id a6b3e7eb-bc46-4340-9ce9-72a0a8991b76`

You can run tests using the CLI by adding a Hasura endpoint via the `--endpoint` flag to the above command:

`hasura pro regression-tests run --testsuite-id  < test-suite-id >  --project-id  < project-id >   --endpoint  < hasura-instance-url >`

Note

In the hasura-instance-url, the `v1/graphql` suffix should not be present. If your GraphQL API is available at `https://65.1.138.103.nip.io/hge/v1/graphql` then the url is `https://65.1.138.103.nip.io/hge/` 

The endpoint URL can be an external Hasura instance or a Hasura Community Edition instance running inside the CI
environment.

This command fetches the entire test suite from Hasura Pro and runs the tests against the given endpoint. The results
will be reported to the terminal. You can also view the test run and the results later on the Hasura Console in the `Regression Tests` menu's `Past Runs` tab.

The report in the terminal lists all the tests in the test-suite and gives the status `success` or `failed` for each of
them. If there are any errors, the `Error` string is displayed and the count of passed and failed tests is also shown.
If all the tests pass, the command returns with the `0` exit code. In the event of any test failures, a non-zero exit
code is returned.

### What did you think of this doc?

- [ Setting up the test suite ](https://hasura.io/docs/latest/hasura-cli/pro-cli/regression-tests/#setting-up-the-test-suite)
- [ Getting a personal access token ](https://hasura.io/docs/latest/hasura-cli/pro-cli/regression-tests/#getting-a-personal-access-token)
- [ Running a regression test suite programmatically ](https://hasura.io/docs/latest/hasura-cli/pro-cli/regression-tests/#running-a-regression-test-suite-programmatically)
    - [ 1. Install the Hasura CLI and Pro add-on for CLI ](https://hasura.io/docs/latest/hasura-cli/pro-cli/regression-tests/#1-install-the-hasura-cli-and-pro-add-on-for-cli)

- [ 2. Configure the CI process ](https://hasura.io/docs/latest/hasura-cli/pro-cli/regression-tests/#2-configure-the-ci-process)
- [ Running tests ](https://hasura.io/docs/latest/hasura-cli/pro-cli/regression-tests/#running-tests)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)