# Deploy a Data Connector

## Integrated connectors​

[ Integrated connectors ](https://hasura.io/docs/3.0/connectors/introduction/#integrated-connectors)do not need to be deployed, and are
available for immediate use in any project. You can see a full list of integrated connectors on the[ Connector Hub ](https://hasura.io/connectors).

## HTTP connectors​

### Deploy an HTTP connector via a cloud provider​

[ HTTP connectors ](https://hasura.io/docs/3.0/connectors/introduction/#http-connectors)can easily be deployed to a variety of cloud providers.
Simply follow the deployment instructions of your chosen provider.

### Deploy an HTTP connector via Hasura using the CLI​

You can also deploy them to Hasura using our `connector` CLI plugin. You can see a full list of HTTP connectors on the[ Connector Hub ](https://hasura.io/connectors).

Open source repositories that are set up according to the connector convention can be used via the `connector` CLI
plugin.

Curious about an example?

See the[ SendGrid connector's repository ](https://github.com/hasura/ndc-sendgrid/tree/main#sendgrid-connector)to see
how the connector is set up.

Once you have the Hasura v3 CLI you can install the plugin as follows:

`hasura3 plugin  install  connector`

Limit access to your connector

You can set the `SERVICE_TOKEN_SECRET` environment variable to only allow requests from authorized clients. Set the
token while deploying the connector and then create a secret on Hasura Cloud with the same value:

`hasura3 secret  set  -k SERVICE_TOKEN_SECRET -v  < secret-value >`

Deploy the connector to Hasura Cloud:

```
hasura3 connector create my-connector:v1 \
  --github-repo-url https://github.com/hasura/cool-connector/tree/v0.7 \
  --config-file conf.json \
  --env SERVICE_TOKEN_SECRET='MY-SECRET-TOKEN-XXX123'
```

### Add connecotr to Metadata​

Get the URL for the deployed connector and add a `kind: DataConnector` object to your metadata:

```
kind :  DataConnector
version :  v2
definition :
   name :  my_connector
   url :
     singleUrl :
       value :  https : //my - connector - 9XXX7 - hyc5v23h6a - ue.a.run.app
   headers :
     Authorization :
       stringValueFromSecret :  SERVICE_TOKEN_SECRET
```

Build the new metadata:

`hasura3 build create -d  "add new connector"`

### What did you think of this doc?

- [ Integrated connectors ](https://hasura.io/docs/3.0/connectors/deployment/#integrated-connectors)
- [ HTTP connectors ](https://hasura.io/docs/3.0/connectors/deployment/#http-connectors)
    - [ Deploy an HTTP connector via a cloud provider ](https://hasura.io/docs/3.0/connectors/deployment/#deploy-an-http-connector-via-a-cloud-provider)

- [ Deploy an HTTP connector via Hasura using the CLI ](https://hasura.io/docs/3.0/connectors/deployment/#deploy-an-http-connector-via-hasura-using-the-cli)

- [ Add connecotr to Metadata ](https://hasura.io/docs/3.0/connectors/deployment/#add-connecotr-to-metadata)
