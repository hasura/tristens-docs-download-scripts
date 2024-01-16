# OpenDD Data Connectors

## Introduction​

A data connector is a way to specify where your data comes from and how it can be used. It can connect to various types
of data sources, like SQL databases, NoSQL databases, REST APIs, GraphQL APIs, files, and more.

You can declare a data connector and use it in your[ model's ](https://hasura.io/docs/3.0/data-domain-modeling/models/)configuration
by[ referencing it with the source ](https://hasura.io/docs/3.0/data-domain-modeling/models/#source)property, which connects that model to
the respective data connector.

In the Open Data Domain Specification (OpenDD spec), you can connect to data sources through a `DataConnector` or a `HasuraHubDataConnector` .

## DataConnector​

To create a data connector object, you will need to define an object with `kind: DataConnector` and `version: v1` .
The object `definition` should include four fields: `name` , `url` , `headers` and `schema` .

```
kind :  DataConnector
version :  v2
definition :
   name :  <DataConnectorName >
   url :  <DataConnectorURL >
   headers :  <DataConnectorHeaders >
   schema :  <SchemaResponse >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `name`  |  `String`  | true | Name of the Data Connector. |
|  `url`  | [ DataConnectorURL ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#dataconnectorurl) | true | URL to access the data connector. |
|  `headers`  | [ DataConnectorHeaders ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#dataconnectorheaders) | true | Request headers to pass on to the data connector. |
|  `schema`  | [ SchemaResponse ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#schemaresponse) | true | The schema response from the data connector. This includes `scalar_ types` , `object_ type` , `collections` , `functions` and `procedures` . |


### DataConnectorURL​

 `DataConnectorURL` is an object that either defines a single URL for the data connector or separate read/write URLs
for the data connector. For example, it can take either of the following

```
url :
   singleUrl :  <URL as Secret >
```

```
url :
   read :  <URL as Secret >
   write :  <URL as Secret >
```

The[ secret syntax ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#secret)should be used for URLs.

Read/Write URLs are used to access the appropriate data connector based on the GraphQL operation type. For example, if
the operation type is `Query` or `Subscription` , then the `read` URL will be used to access the data connector.
Similarly, for a `Mutation` operation, the `write` URL will be used.

### DataConnectorHeaders​

 `DataConnectorHeaders` is an object that defines the headers to be forwarded to the data connector when making requests.
The keys of this object are header names and the values are the header values in the[ secret syntax ](https://hasura.io/docs/3.0/data-domain-modeling/common-syntax/#secret).
E.g., if a bearer authorization token needs to be forwarded, the headers field would be:

```
headers :
   Authorization :
     value :  Bearer <token >
```

or if the header is coming from a secret:

```
headers:
  Authorization:
    stringValueFromSecret: <secret name>
```

### SchemaResponse​

 `SchemaResponse` is an object that defines the types, schema, functions, etc. of the data connector. This is usually
provided by the `/schema` endpoint of the data connector. It contains the following fields:

```
schema :
   scalar_types :  <ScalarTypes >
   object_types :  <ObjectTypes >
   collections :  <Collections >
   functions :  <Functions >
   procedures :  <Procedures >
```

The structure and detailed documentation of these fields can be found[ here ](https://hasura.github.io/ndc-spec/specification/schema/index.html).

### Example​

In this example, we'll create a data connector for the Chinook data set. The Chinook data set is a sample database that
represents a digital media store, including tables for artists, albums, tracks, and more. Each object we reference above
is present in the complete example below:

```
kind :  DataConnector
version :  v2
definition :
   name :  my_data_connector
   url :
     singleUrl :
       value :  http : //localhost : 8080
   schema :
     scalar_types :
       String :
         aggregate_functions :   { }
         comparison_operators :
           like :
             argument_type :
               type :  named
               name :  String
         update_operators :   { }
       Int :
         aggregate_functions :
           min :
             result_type :
               type :  nullable
               underlying_type :
                 type :  named
                 name :  Int
           max :
             result_type :
               type :  nullable
               underlying_type :
                 type :  named
                 name :  Int
         comparison_operators :   { }
         update_operators :   { }
     object_types :
       Artist :
         description :  An artist
         fields :
           ArtistId :
             description :  The artist's primary key
             arguments :   { }
             type :
               type :  named
               name :  Int
           Name :
             description :  The artist's name
             arguments :   { }
             type :
               type :  named
               name :  String
       Album :
         description :  An album
         fields :
           AlbumId :
             description :  The album's primary key
             arguments :   { }
             type :
               type :  named
               name :  Int
           Title :
             description :  The album's title
             arguments :   { }
             type :
               type :  named
               name :  String
           ArtistId :
             description :  The album's artist ID
             arguments :   { }
             type :
               type :  named
               name :  Int
       Track :
         description :  A track
         fields :
           TrackId :
             description :  The track's primary key
             arguments :   { }
             type :
               type :  named
               name :  Int
           Name :
             description :  The track's name
             arguments :   { }
             type :
               type :  named
               name :  String
           AlbumId :
             description :  The track's album ID
             arguments :   { }
             type :
               type :  named
               name :  Int
       artist_below_id :
         description :  An artist
         fields :
           ArtistId :
             description :  The artist's primary key
             arguments :
               id :
                 description :  The cyling id
                 type :
                   type :  named
                   name :  Int
             type :
               type :  named
               name :  Int
           Name :
             description :  The artist's name
             arguments :   { }
             type :
               type :  named
               name :  String
     collections :
       -   name :  Artist
         description :  A collection of artists
         arguments :   { }
         type :  Artist
         deletable :   false
         uniqueness_constraints :
           ArtistById :
             unique_columns :
               -  ArtistId
         foreign_keys :   { }
       -   name :  Album
         description :  A collection of albums
         arguments :   { }
         type :  Album
         deletable :   false
         uniqueness_constraints :
           AlbumById :
             unique_columns :
               -  AlbumId
         foreign_keys :   { }
       -   name :  Track
         description :  A collection of tracks
         arguments :   { }
         type :  Track
         deletable :   false
         uniqueness_constraints :
           TrackById :
             unique_columns :
               -  TrackId
         foreign_keys :   { }
       -   name :  artist_below_id
         description :  A collection of artists below a certain id
         arguments :
           id :
             description :  The ceiling id
             type :
               type :  named
               name :  Int
         type :  Artist
         deletable :   false
         uniqueness_constraints :   { }
         foreign_keys :   { }
     functions :   [ ]
     procedures :   [ ]
```

## HasuraHubDataConnector​

Instead of deploying your own data connector, Hasura metadata also allows you to directly configure and use one of the standard data connectors from the[ Connector Hub ](https://hasura.io/connectors/).

### Metadata Object​

To configure a HasuraHubDataConnector, you will need to add the following metadata object:

```
kind :  HasuraHubDataConnector
version :  v1
definition :
   name :  <DataConnectorName >
   connectorId :  <HasuraHubConnectorId >
   connectorConfiguration :  <ConnectorConfigurations >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `name`  |  `String`  | true | Name of the Data Connector. |
|  `connectorId`  |  `String`  | true | The Connector Hub ID of the connector to configure. Currently, only `hasura/postgres` is supported. |
|  `connectorConfiguration`  | [[ ConnectorConfiguration ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#connectorConfiguration)] | true | The configurations to deploy the connector, one for every region that the connector should be deployed in. |


#### ConnectorConfiguration​

ConnectorConfiguration defines the configuration to deploy a connector in a particular region.
Typically, you want to deploy the connector in a region that's closest to your database. The NDC schemas for deployments across all regions must be identical.

The structure of ConnectorConfiguration is as follows:

```
region :  <String >
mode :  <ReadOnly / ReadWrite / WriteOnly >
configuration :  <Connector specific configuration >
```

| Field | Type | Required | Description |
|---|---|---|---|
|  `region`  |  `String`  | true | Name of the cloud region. Eg: gcp-asia-south1 |
|  `mode`  |  `String`  | true | Whether this connector should support reads only, writes only, or both. |
|  `connectorConfiguration`  |  `Any`  | true | The configuration specific to the connector ID you chose from the Hub. |


### Example​

In this example we are configuring a postgres data connector using a postgres database URL in a single region.

```
kind :  HasuraHubDataConnector
version :  v1
definition :
   name :  foo
   connectorId :  hasura/postgres
   connectorConfiguration :
     -   region :  gcp - asia - south1
       mode :  ReadWrite
       configuration :
         version :   1
         connectionUri :
           uri :
             value :  postgres : //username : password@database - host/database_name
         metadata :  < ... >
```

After populating the URL, typically, the rest of configuration will be automatically authored through tooling (eg: Hasura VSCode extension).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#introduction)
- [ DataConnector ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#dataconnector)
    - [ DataConnectorURL ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#dataconnectorurl)

- [ DataConnectorHeaders ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#dataconnectorheaders)

- [ SchemaResponse ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#schemaresponse)

- [ Example ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#example)
- [ HasuraHubDataConnector ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#hasura-hub-data-connector)
    - [ Metadata Object ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#metadata-object)
        - [ ConnectorConfiguration ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#connectorConfiguration)

- [ Example ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#example-1)

- [ Metadata Object ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#metadata-object)
    - [ ConnectorConfiguration ](https://hasura.io/docs/3.0/data-domain-modeling/data-connectors/#hasura-hub-data-connector/#connectorConfiguration)
