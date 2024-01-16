# Add a Hasura GraphQL Data Connector Agent to Metadata

To use a custom Hasura GraphQL Data Connector Agent, follow the following steps in the Hasura Console to add it to the
Hasura GraphQL Engine metadata. Before following the steps, make sure the custom connector is deployed and accessible.

- Console
- CLI
- API


1. Navigate to the Data tab in the project's Console.
2. Click on the `Manage` button.
3. Click on the `Data Connector Agents` button.
4. Click on the `Add Agent` button.
5. Enter the values for name and Agent endpoint. Click `Connect` and you're done!
6. Once the above is done, the new driver supported by the custom connector will be available as one of the options
in the `Connect Database` page.


Navigate to the Data tab in the project's Console.

Image: [ Hasura GraphQL Data Connector Agent diagram ](https://hasura.io/docs/assets/images/data-tab-f533481ebe5bad60fbd300b76e71d0a1.png)

Click on the `Manage` button.

Image: [ Hasura GraphQL Data Connector Agent diagram ](https://hasura.io/docs/assets/images/manage-db-96ad1b6c74512dac684c84fa99a0d95f.png)

Click on the `Data Connector Agents` button.

Image: [ Hasura GraphQL Data Connector Agent diagram ](https://hasura.io/docs/assets/images/connect-agent-01dd7a7a8f52e5654493803c83be30c5.png)

Click on the `Add Agent` button.

Image: [ Hasura GraphQL Data Connector Agent diagram ](https://hasura.io/docs/assets/images/add-agent-351a4d472dae6017b68ba28932cac944.png)

Enter the values for name and Agent endpoint. Click `Connect` and you're done!

Image: [ Hasura GraphQL Data Connector Agent diagram ](https://hasura.io/docs/assets/images/connect-final-edc8a51e00f0ec8800484325ead042b7.png)

Once the above is done, the new driver supported by the custom connector will be available as one of the options
in the `Connect Database` page.

Image: [ Hasura GraphQL Data Connector Agent diagram ](https://hasura.io/docs/assets/images/updated-driver-list-c83e224ad299520a54e43cc7b4c3efb2.png)

You can add a Data Connector Agent by adding its config to the `/metadata/backend_configs.yaml` file:

```
dataconnector :
   sqlite :
     uri :  <data - connector - agent - url >
```

Apply the Metadata by running:

`hasura metadata apply`

You can add a Data Connector Agent to Hasura via the `dc_add_agent` Metadata API.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "dc_add_agent" ,
   "args" :   {
       "name" :   "sqlite" ,
       "url" :   "<url-where-data-connector-agent-is-deployed>"
   }
}
```

### What did you think of this doc?

Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)