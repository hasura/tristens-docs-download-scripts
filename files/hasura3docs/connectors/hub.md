# Connector Hub

Hasura maintains a directory of[ available and upcoming v3 Connectors ](https://hasura.io/connectors/). This provides a
searchable and browsable index of connector versions. Each connector listed also has a details page with deployment
instructions.

The following instructions will explain how to have a connector listed on the connector's directory.

## Authoring your connector​

Follow the[ Build your own Connector ](https://hasura.io/docs/3.0/connectors/build-your-own-connector/)guide for
instructions on how to write a connector.

## Setting up a connector repository​

Currently, a connector must be published as an open source repository on GitHub.

This should include the following:

- A `README.md` documenting what the connector is, and how to use it.
- A `Dockerfile` that builds and runs your connector in the context of the `connector` plugin.


Dockerfile Requirements

If your connector relies on the `--volume` feature from the connector plugin, then your Dockerfile must **COPY** the
volume from a placeholder file/directory. This should be done as late in the Dockerfile as possible if you wish to
optimize for caching.

(See:[ the NDC-Typescript-Deno Dockerfile ](https://github.com/hasura/ndc-typescript-deno/blob/main/Dockerfile))

## Publishing your Connector on the Connector Hub​

All connectors listed on the Connector Hub currently require an entry in the[ ndc-hub repository registry ](https://github.com/hasura/ndc-hub/tree/main/registry). See the[ SendGrid Connector ](https://github.com/hasura/ndc-hub/tree/main/registry/sendgrid)for an example.

Once your repository is set up and tested with the[ Connector CLI Plugin ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/)you should open a pull request
against the[ NDC-Hub repo ](https://github.com/hasura/ndc-hub)to add a directory representing your connector.

It should contain:

- A `README.md` file
    - This should be a condensed version of the `README.md` in your connector repository that acts as a quickstart guide
for Hasura users.
- A `logo.png` file
    - This will appear next to your connector in the Connector Hub directory.
- A `metadata.json` file
    - This is used for indexing your connector and listing its published versions.


## Tagging your Connector Versions​

The `"source_code"` key in the `metadata.json` lists published versions of your connector.

We recommend that you tag releases of your connector in your repository according to[ "semver" ](https://semver.org).

You should include the Git hash of the version you are tagging so that stealth updates cannot be released without
review.

- `is_open_source` should be `true` , and
- `is_verified` should be `false`


For example:

```
    "source_code":{
        "is_open_source": true,
        "repository":"https://github.com/foo/bar/",
        "version":[
            {
                "tag": "v0.2",
                "hash": "c0b3f13893e24a41df084985908af7ced0265498",
                "is_verified": false
            },
            {
                "tag":"v0.1",
                "hash":"8dc16c427e4e0136ebf0cfba1de3831c7939befb",
                "is_verified": false
            }
        ]
    }
```

You can update your connector with new tags and details at any time, however all PRs will be reviewed by Hasura for the
immediate future.

## Verifying your Connector​

Please mark `"is_verified": false` in your connector metadata on initial publication.

If you wish to have your connector verified then you can raise this in the pull request discussion, or[ open an issue ](https://github.com/hasura/ndc-hub/issues/new).

More information about partnering with Hasura to have a verified version of your connector listed will be available
soon.

## Maintaining your Connector​

If you wish to have your connector listed on the Connector Hub, you should commit to making a best-effort to maintain the
connector to ensure that it is up-to-date with respect to:

- Hasura Compatibility
- Relevant Security Updates


The updates should be released as new versions of your connector.

### What did you think of this doc?

- [ Authoring your connector ](https://hasura.io/docs/3.0/connectors/hub/#authoring-your-connector)
- [ Setting up a connector repository ](https://hasura.io/docs/3.0/connectors/hub/#setting-up-a-connector-repository)
- [ Publishing your Connector on the Connector Hub ](https://hasura.io/docs/3.0/connectors/hub/#publishing-your-connector-on-the-connector-hub)
- [ Tagging your Connector Versions ](https://hasura.io/docs/3.0/connectors/hub/#tagging-your-connector-versions)
- [ Verifying your Connector ](https://hasura.io/docs/3.0/connectors/hub/#verifying-your-connector)
- [ Maintaining your Connector ](https://hasura.io/docs/3.0/connectors/hub/#maintaining-your-connector)
