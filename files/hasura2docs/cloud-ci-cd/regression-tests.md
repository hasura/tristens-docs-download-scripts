# Regression Tests on Hasura Cloud

## Introduction​

Hasura Cloud includes a comprehensive test bench that lets you seamlessly compile a test suite on each project,
executable on any GraphQL Engine instance (ex: staging, prod).

Here's a reference development workflow that is enabled by Hasura Cloud:

1. Build your database schema and configure Hasura as required by your frontend apps or public GraphQL API.
2. Deploy changes to production after testing them.
3. Create a regression suite on production.
4. Iterate on your GraphQL schema to support new features or edits.
    - Test changes in your dev instance against the production instance’s regression test suite. Fix any issues
highlighted by the tests or plan to communicate regressions to affected stakeholders.

5. Test changes in your dev instance against the production instance’s regression test suite. Fix any issues
highlighted by the tests or plan to communicate regressions to affected stakeholders.
6. Run all changes through a CI/CD pipeline
    - Run Regression tests programmatically for all changes in the team

7. Run Regression tests programmatically for all changes in the team
8. Promote changes to prod


Image: [ Regression testing process diagram ](https://hasura.io/docs/assets/images/regression-testing-diagram-a2d7bf9ad1478f3a5ef0ac0d5ed19dfe.png)

## Manage test suites​

Each Hasura Cloud project can be configured with a separate test suite. Ideally, you want to create a regression test
suite on an project which has received requests with operations you’d like to continue supporting or ensure are not
“broken” - production or a shared QA project which receives operations in your app or, if you have a public GraphQL API,
those from your consumers.

Image: [ Manage regression test suites ](https://hasura.io/docs/assets/images/regression-tests-suites-4c7fb9ad25cba5af9d5b6a66aab01f4b.png)

## Quick-create tests​

Add important operations to your test suite with one click by adding them from your project's operation history:

Image: [ Add tests to regression test suites ](https://hasura.io/docs/assets/images/regression-tests-add-operations-3666aa2d5a2b2d759f1288ff6ac52b8b.png)

## Run test suites​

A good development workflow would require that tests be run 1) early in the dev process, and 2) automatically with
changes, to ensure changes to the schema don't break functionality.

A test suite configured on a Hasura Cloud project can be run on the same instance or any other Hasura Cloud project
registered to your team, including local ones. This is how we recommend that you incorporate regression tests into your
GraphQL Engine workflows:

### Run regression tests manually​

Let’s say you’re a developer iterating on a feature and, as part of your work, need to modify your Postgres schema or
the Hasura configuration. It is likely that you are doing so by running the Console via the Hasura CLI to generate
Migrations that you can version control. Before committing your changes in git, you should run tests to get an early
warning for potential regressions. Your team may want to designate the test suite from your production instance (or a
suitable alternative) as the default suite to be used for this, and you can choose to run this test suite on your local
or development instance.

Image: [ Run regression tests ](https://hasura.io/docs/assets/images/regressions-run-prod-tests-on-dev-158341e81085d6790cee84e5166732db.png)

For example, if the column ‘title’ (in a typical authors and articles schema) has been modified as part of a feature
iteration. Assuming the operation from the previous example is part of the test suite on production, here’s how the
feedback on this change looks like:

Image: [ Regression test results ](https://hasura.io/docs/assets/images/regression-tests-results-e31711a4ca29397bb28cfaa5683c8934.png)

As you can see, one of the tests fails because it expects a field, title, to be part of the type articles - which is
something our proposed change just modified and removed support for.

### Run regression tests in CI/CD flow​

Image: [ Run regression tests via CLI ](https://hasura.io/docs/assets/images/regression-tests-run-cli-079d10fa6b9b27fa55841cf2a7439d7d.png)

This command will fetch the entire test suite from Hasura Pro and run the tests against given endpoint using the admin
secret and report the result on the terminal. The test run and the results will also be available on the Hasura Console.

You can use the Hasura Pro CLI to programmatically trigger execution of a test suite in your automated testing setup,
typically in CI scripts.

In order to communicate with Hasura’s APIs, the CLI needs to be configured with an API access token (which you can
create via your Hasura Cloud settings). If you want to set the token up on a non-interactive environment, like a CI
pipeline, you can obtain a token and then add to `~/.hasura/pro_config.yaml` with the following format:

`pat:  < token >`

## View test suite results​

Image: [ Regression tests past results ](https://hasura.io/docs/assets/images/regression-tests-past-runs-2123ec0fcd7b12753d5737f0c9667a4f.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/cloud-ci-cd/regression-tests/#introduction)
- [ Manage test suites ](https://hasura.io/docs/latest/cloud-ci-cd/regression-tests/#manage-test-suites)
- [ Quick-create tests ](https://hasura.io/docs/latest/cloud-ci-cd/regression-tests/#quick-create-tests)
- [ Run test suites ](https://hasura.io/docs/latest/cloud-ci-cd/regression-tests/#run-test-suites)
    - [ Run regression tests manually ](https://hasura.io/docs/latest/cloud-ci-cd/regression-tests/#run-regression-tests-manually)

- [ Run regression tests in CI/CD flow ](https://hasura.io/docs/latest/cloud-ci-cd/regression-tests/#run-regression-tests-in-cicd-flow)
- [ View test suite results ](https://hasura.io/docs/latest/cloud-ci-cd/regression-tests/#view-test-suite-results)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)