# Using a v3 Connector in a v2 Project via the Proxy

## Introduction​

The[ Connector Hub ](https://hasura.io/connectors)is designed to act as the new gold-standard for data source compatibility
and works seamlessly with Hasura v3 projects to integrate diverse datasets and interactions in your projects.

While this is immensely useful in a v3 context, what does it mean for your existing v2 projects? Will they be able to
use the new connectors?

The integrated Connector Proxy addresses this question by providing an optional `/v2` endpoint. Any connector using the
Hasura Connector SDKs will be able to enable this endpoint and be instantly compatible with existing v2 projects without
any further modification.

## Usage and configuration​

When deploying your connector with the[ connector plugin ](https://hasura.io/docs/3.0/connectors/introduction/#the-connector-cli-plugin),
simply enable the `ENABLE_V2_COMPATIBILITY` mode via an environment variable:

```
hasura3 connector create my-connector:v1 \
  --github-repo-url https://github.com/hasura/cool-connector/tree/v0.7 \
  --config-file conf.json \
  --env ENABLE_V2_COMPATIBILITY=true
```

If your connector has been configured with a `SERVICE_TOKEN_SECRET` , you will need your v2 project to configure the
proxy data connector with a corresponding configuration option.

For example, if your connector was created like so:

```
hasura3 connector create my-connector:v1 \
  --github-repo-url https://github.com/hasura/cool-connector/tree/v0.7 \
  --config-file conf.json \
  --env ENABLE_V2_COMPATIBILITY=true
  --env SERVICE_TOKEN_SECRET='MY-SECRET-TOKEN-XXX123'
```

Then your v2 project connector config would look like:

```
{
  "service_token_secret": "MY-SECRET-TOKEN-XXX123"
}
```

## Limitations​

The primary limitation of the proxy is that the v3 architecture no longer allows for dynamic configuration of connectors
and their configuration is set on creation.

This means that you will have to deploy a v3 connector per-usage scenario as per the v3 pattern.

You can then track entities as per a normal v2 project once the connector is available via the proxy endpoint.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/connectors/v2-compatibility/#introduction)
- [ Usage and configuration ](https://hasura.io/docs/3.0/connectors/v2-compatibility/#usage-and-configuration)
- [ Limitations ](https://hasura.io/docs/3.0/connectors/v2-compatibility/#limitations)