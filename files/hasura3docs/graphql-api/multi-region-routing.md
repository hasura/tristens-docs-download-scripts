# Multi-Region Routing with the Native Data Connector for PostgreSQL

With multi-region routing, you can easily ensure that the data is fetched from the data source closest to the user, thus
minimizing latency for the request.

For multi-region routing, you only need a supported data source deployed in (or near) more than one of the[ supported regions ](https://hasura.io/docs/3.0/graphql-api/multi-region-routing/#supported-regions).

Same schema for all databases

You must ensure that the schema for the different databases are exactly same. If there is any ambiguity between the
schemas, then the metadata build would fail.

## Configuration​

For multi-region routing, you will add configuration for each of the data sources' metadata objects

An example configuration for the PostgreSQL `HasuraHubDataConnector` is provided below:

```
kind :  HasuraHubDataConnector
version :  v1
definition :
   name :  db
   connectorId :  hasura/postgres
   connectorConfiguration :
     -   region :  gcp - europe - west1
       mode :  ReadOnly
       configuration :
         version :   1
         metadata :   &db-metadata
           tables :
             Album :
               schemaName :  public
               tableName :  Album
               columns :
                 AlbumId :
                   name :  AlbumId
                   type :  integer
         aggregateFunctions :
           integer :   { }
           text :   { }
         connectionUri :
           uri :
             stringValueFromSecret :  PG_EUROPE_URL
     -   region :  gcp - us - east4
       mode :  ReadWrite
       configuration :
         version :   1
         metadata :   *db-metadata
         aggregateFunctions :
           integer :   { }
           text :   { }
         connectionUri :
           uri :
             stringValueFromSecret :  PG_US_URL
```

For the above configuration, Hasura DDN will route all the write queries (mutations) to the database in the `gcp-us-east4` region and the read queries (query and subscriptions) to either `gcp-us-east4` or `gcp-europe-west1` based on the geolocation of the client.

## Supported regions​

Currently, Hasura DDN supports the following regions:

- `gcp-asia-south1`
- `gcp-asia-southeast1`
- `gcp-australia-southeast1`
- `gcp-europe-west1`
- `gcp-southamerica-east1`
- `gcp-us-east4`
- `gcp-us-west2`


### What did you think of this doc?

- [ Configuration ](https://hasura.io/docs/3.0/graphql-api/multi-region-routing/#configuration)
- [ Supported regions ](https://hasura.io/docs/3.0/graphql-api/multi-region-routing/#supported-regions)
