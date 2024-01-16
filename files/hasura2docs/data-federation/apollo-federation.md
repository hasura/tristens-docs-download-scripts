# Apollo Federation Support

## Introduction​

Hasura GraphQL Engine supports the Apollo Federation v1 spec, so you can add Hasura as a subgraph in your Apollo
federated gateway. You can also use Hasura generated table types in your other subgraphs by enabling tables for Apollo
Federation explicitly.

Supported from

Apollo Federation is available from Hasura version `v2.10.0` and above.

Enabling apollo-federation

Apollo Federation can be enabled using[ the server configuration ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#enable-apollo-federation)( `--enable-apollo-federation` flag or setting `HASURA_GRAPHQL_ENABLE_APOLLO_FEDERATION` to `true` ).

For backwards compatibility, the feature can also be enabled by adding `apollo_federation` to the `HASURA_GRAPHQL_EXPERIMENTAL_FEATURES` [ environment variable array ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/)or
with the server flag `--experimental-feature` .

## Using Hasura tables in other subgraphs​

Currently, only the types generated for the database source tables can be extended in other subgraphs. The primary key
will be used in the `@key` directive's `fields` argument. For example, enabling the table `user` for Apollo Federation
will generate the type `user` as follows:

```
type   user   @key ( fields :   "id" )   {
   id :   Int !
   name :   String
   ...
}
```

The Apollo Federation support in Hasura only allows extending other subgraphs with Hasura types. The other way i.e.
extending Hasura types with other subgraphs is not possible currently. We recommend using[ remote relationships ](https://hasura.io/docs/latest/remote-schemas/remote-relationships/index/)for extending types from other subgraphs in
Hasura.

Supported types

Other types such as action types, Remote Schema types, etc. cannot be extended to other subgraphs.

- Console
- CLI
- API


Prerequisite before enabling Apollo Federation on the Hasura Console

To enable Apollo Federation using the Hasura Console, you'll first need to add `apollo_federation` to the list of
experimental features using the[ HASURA_GRAPHQL_EXPERIMENTAL_FEATURES environment variable ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#experimental-features)array or with the[ server flag --experimental-feature ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#experimental-features). You can
learn more about setting these[ here ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/index/#setting-server-configurations).

Head to the `Data -> [table-name] -> Modify` tab in the Console and toggle the switch in the `Enable Apollo Federation` section:

Image: [ Set table as enum ](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWQAAABZCAYAAAAJiF7nAAAACXBIWXMAAAsSAAALEgHS3X78AAAPD0lEQVR42u2d4U8T2RqH90+6n+63/WZiYsJuJHHTkNCwRGJqBJJG0sglKxIBL+JtCCjoWi82pGKarXC3NXQ1YKyIoEYIERXkgoopKxnXNgiNfvjdczpnpkOZloKCXvl9eJLaTmfOmTnnmXfe8xa/S334CEIIIV+e73gSCCGEQiaEEEIhE0IIhUwIIYRCJoQQCpkQQgiFTAghFDIhhBAKmRBCKGRCCCEUMiGEUMiEEEIoZEIIoZAJIYRQyIQQQiETQgihkAkhhEJex0ywEXsPuOwpaUf03TY08l0MNQ55DDea7q3k3u6eD8WyHQ4vwp+pHVOBE5n+HQ5gfHU7L8Yr+D36sZyXprenX6sP0FTqynkN1xx3sxjt3K5xkHN8TCMc6IMvEMXYorWvc+is1PvlCr76IpPr5es/8e8r/8HR4/9CS3t3+rV8j+IhFPJWBHnU2sc6dD6mkL86Ib+OolqOD0fW9fnCQo7cvGN7jksP/yMtZsqHfD4hOxrhn1lB8r2F7Yoev5SQ58NwpSf6CbiOVunCujz3zQi5qHUE2vu11zD1KdfwaxPyhxXEZ+cw9XQOM29WvgoZW5Hb7FybUhi9FkL9RGpXSO3JQAju0cQuE/J87u3GL9WltytuCKL3YjsOVgihOarg8PgQnrVMjtkY2lq9cFV6UCxFIbdxt6Mztmgj5CrUBmPobD6B4pIqFFd60XlP21hc2jR6O1rgLNfbIL/Xen0O2gZ9fRFq0fvqCWOsX72u7sPUqs3NorwLoVgYTbUeFKXb1g7fQ22NHF7cDaLeI/pZImRY6sHBhgDCT5NbF7LoV+ic1zy3xZUtaLo6gRerBQrZ+yDPdosYvtqF6sNuFIn+FVWcQO2lEcy8z2yTFNeuNd1fNxy1Pvgve1FkI2RtRlzjhhNwyOOKbZ1i295xbf05LBPnrN+PmsNV6b6GtALGhzk2LDhaEFrMEyGvahgL+lBdqfpWXoeajijG3thcV3Ezbg31oamuLn3d9paJbQMTG46dbPk+mJhKkx0p71j6QpvEkTNDGF2RN7BRONofYEF9tvR8GM4zA7j250604xGcwgHHJpazPksg0u3D94HZz3OcPx/A6R3Gk92csnCcf7xOyAZFJZbXQnAzppD74BICc1SKKNTTCGeZkf4Qwp/9mHvSGZS2oPdlHnG9n4NPRbdFhxpR7anTpSGi7dobWp6+LqK3Tj/GwcDcmmjZN2sXvRvtdusT94AumLDKacZjXXAY25W6dbmofvoer2xeyKJffk+VOq6Qcblb9Utch3+OIL6VlIW4yernMonh8+r6ldbBVdsIh+qTo+2BLqN3Yj+HCkhdzUdRU6a30eFuEWJ1b3x9hXSLKnwYXi1gfLwbQX1ZleXY4rvl3jxCTmLsYmZsFpXrUk7/u9KPYS1Pm8x/539Ss4uO7YQs2anUxcLtEPZfW1BPFBkhJ56PChlHcC2+Q8IRQq745QK+P3UDsUTm/aWHEeyvv/D5hCwEf/nsFZyZp5DXCrmsRUSxi0iKCNGcCCVZkZ41olscRI0SRs11bd3kcDT0YWhWQ/xxWE10Jcwc4tKECNPvVQYwntQjVXOhTtwYXuTqq2xHieUxWE7uajW5r76yFbKzYwQvRASZfNqny1u8V92/mP6uT323uHlQj2Dfv0LvcXWjqIuqdhQuZO2W6pe4QXSO61F2/J4fzvRxPWh9uLJ1IZt9z0gz+VDsW8k2LKQVj6poWBy/7b4G7fVj9DZ7soQsrvl5/T2HV4lc3OhCqt9mHy3nsLiub22kWsj4eGncLMW1erpBDlmmN0r0G0R1cE6MS/leDPUVaiz1zK2/rq2DmJL9eZ05dr5cu1y8sxOv3ftysW8n0hU3/d1wP0qtEfITKePT/ei1ylh8VtHWD3f3gCAk+jmK0WUj6pxCvZDc/jaBtx8dUwmklp/hWFMEkWX9OJHuC9j3ezxznLZRzGYL+fQQevvFPn6bR0K+99czuGU7BiPYo4S8MHkbFd4rYtyI7TqHEFHR+9KdCJz+GzhyoR9HIvL7KTy5MwBnm76tMziF2ZRKW/wu/n0rsVtSFiJSFI/b2rsMyffrUxZ7j1qi4bs+NYnVI6U5yaYRDQXR6u1CfXMLnGrQu0KLeXLIKxjy6tFWUfOIPrFsxDVu3AQOi8f5Np9OnRJHhR9jOR7vTeGIbYbf6fnV4XMeU+QzefPbQsBuJZi2CV0iNjnw5GC7+Yivt7dwIY8Zbam13FQs4ndent44ZSEiaev1097pbUsa16lEPJ571TlrFVGycd1nPopzoSLd2mjm+He7slIWmUVRh6fLPP81lVXm8ZNZKan6uzY3ko3GxyaEnLzVlXXO9bE03OFeez5t25S5Po5zj3POESlZO+naRcg7I+S36WixYz4j3f0NPdh/yoc9QphPUmuF7JCP+ikl8p5uHBlZTkecvRd7UD+pUg1LkzhySog4sSwkLN6fEu+l5lHv7caesw/SEl6604/9/fH1EfKZ2xhPzKP5VA/OPH+LiL8HFbfeIvFQCXl5FsfEvq+pp5WlyRtCyo/SEf2SiPT3+J9hydjfS3FTEZ/p0l9O7+vYpH7jWRrpxz7jqYA5ZBsh3zfEkhFy8rGIJnNEbPmFLGWrpHR8UH9EXycuMdHa3LkXVg7lKmNLInyyKvf3zEf7XG3TEKrLSC8pHrsP2glDRJ2ONfsrVMjiZtSqpHYyZslnZo6bvhFsMYes3WjP23f/rOX4xs3QTsir06YQ7ShqfbBujSBbyAWNj00IOX7dq57cVErEKG/sUU9NlUF9TNi2aRG9tYaQJzYVIedKWchtd0LIv4oIsuO1VcgyMl7GzUCPiCLfrhWyJapNR5mDIspMCUmeFAJeyUTdERF1H5vUxSfFm3g5DGfgEX7tFPv+S8r8CuqffrQXshD+0sQA9tRbbgqGkP97G/uEZE3pStE39ePasi5kq2QXbgXx91MhHLkU0WkXx1RPAon7Yn/BeQq5cCEnEW1WE9sjJoJcCReTuO1woRFyVqRlF0mqR+a9DYMbLsRkBs0Iakvzr5CnUxG52mZNUaQjZFUFkB0hm9GaN50G2FKE7MkRIV+c3rKQkzHVrlIfht7bnyPzRmfcDDeIkPOWneUUcoHj45MjZMv5NMbrJwhZpifsFu8k8vXOV1oso/dCD5qf20hXRrpSdkubF/JNJeTUkpBs+yhGB/vT0fSTSBDH7s+iuW0AN1dyCzm9kBfoR8d/VSrFEPLzbCEviGjaXsizg8H1Ubgp6xD2/x5n2VvhQhYR3XElhwZ9YsfvB+AqySVkPZ83roljzUTNHLI52e1yrUZaoLQF/qeWyZ7UENfs+6gZk9YaCRsTUgmzyBCRNf95vA/D84uYueVTudwqPc9pyT8XnxzUKxVWFxE66c46R5vIIRv9kjnch3oOWXsY0CNxKf67K1uvsjDzrG7UXn+ViYBXk4gvJlUFSmNmUXVeHEubQ9hbty6HPNyhRFcdwJjlfCc1Ddr7jYRc4PgwhCzaWx9LFp5DvqpyyG9GzAVK80b2CUKW4s1OSxgRcraQd2qSj/7Wg4o7y/bS/eNKJg2QS8gyZSGkfuyR2kdCCPq0kORfKgI/G0TF2RB+lbne6SE4LvTD2T2VkaqtkLMwUxbPcEwIuFfdJBJC0DLnPfthvZDT0fSpG7hpjK1USs9LC2JXu3Hkfmr3LupZV9cLTVm86G8xqwOKKzKVArmEvI7yLkTf5KlGSIrHZneVuVLuqD6Bg6rcyX5hRj6OG6Lsy7Td6L+xICii2tCbDdpW6ceYakd8sEtPT2RXYoiorvVecgtVFtNm9YhZLWCcx+NRzKx+StlbUog0U4lQfFics2pV9mXkzy0LXHsdeaosZoUAzYoSD5zuE3DKMj3rTSNPyqKg8aHFUGup4jHXBnJUWQyfs1RZlFmqLCpEuxc/frKQv8Y65MTkAPYZgsxebFueR3NTN+qnUnmELP4dV4t6cqHNG0Lzo7eWut8r+FuTEu3KM7h/OYeK2wn7KouNhGws6p1Ri3rtN3DttcoLZwtZROrjtwfgONWD/W1BOM/e0Mv3ZFR9OoRejb/U25SQZRQ0drULLjFJZW2uqy2KaE+jvZAP+RGO9aH2qF7rK2tfQzMrhdUhm/W6sqa2Dq4GH3wxm8fopBBWuSv3j0CeBjPRb1RbM3FrzgdR79brcp0NQQy9Xiv6mZj4/Kheh5yux63zwb+mVnnzdciZ+mohrEONqL0Uw1Tyc9UhW2p1y4RMPe1oDU6YKZL43SBqDlWlP3OdDCA8PoLWQznqkE82wlGm6qWF4Gu8wUwNdt5FvQLGhzy3gwHUGG091IXwm/x1yGv7JsZDax+GXq5skEYpXMh2qYsvUe5msiIEdSZkRp3fOgm5EGgXofOPC33jFPorQrIrkekLGQnLxTuZuviSf8tiYWoSkfnd8Uu9hclHiLzmX3ujkHlOCCEUMoVMCKGQKWQKmRBCIRNCCIVMCCGEQiaEEAqZEEIIhUwIIRQyIYQQCpkQQihkQggh/69CHoj+gZONjfj553L8+OOPKCoq+qzIfcp9y2PIY/GiEUIoZBsRS1FKaf700084cOAAfvjhhzTytXzvc8tZIo9JMRNCKGTFuc7OtBwdDgdcLhfC4TDm5+exurqaRr6W78nP5DbbIWbZBl5AQsiuFrIhYxkJS+l++PAhL3IbuS2lTAghn1HIMlVgyHhsbGxDGRvIbbdLykxfEEJ2pZBl/lamIAqJjO0i5e1IX8g28UISQnaVkI3oWOaFNytjA/ldRsmEEPKJQpZlZ7JyYivRsTVK3o7qC9k2XkxCyK4RskwNyHI2WUGxVSHL78p9MG1BCCGfIGT5Aw25MCfL2rYqZPnd7Vjck23jxSSEUMgUMiGEMGXBlAUhhIt6XNQjhBCWvbHsjRDCH4bwhyGEEMKfTjM6JoRQyB/4x4UIIeSrFbJVyvzzm4QQ8oWFbKQv+AfqCSHkKxCyVcz8L5wIIeQrEDIhhBAKmRBCKGRCCCEUMiGEUMiEEEIoZEIIoZAJIYRQyIQQQiETQgihkAkhhEImhBBCIRNCCKGQCSGEQiaEEEIhE0IIhUwIIYRCJoQQCpkQQgiFTAghFDIhhBAKmRBCKGRCCCEUMiGEUMiEEEIoZEIIoZAJIYRQyIQQ8u3zP0smgHkCCiAFAAAAAElFTkSuQmCC)

To enable Apollo Federation using the Hasura CLI head to the particular `/metadata/databases/<schema_name>/tables/<schema_name>_<table_name>.yaml` file and add the database configuration as
below:

```
table :
   name :  <table_name >
   schema :  <schema_name >
apollo_federation_config :
   enable :  v1
```

Apply the Metadata using the Hasura CLI by running:

`hasura metadata apply`

To extend the types using the[ Hasura Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/table-view/), you can to enable it
with the particular `*_set_apollo_federation_config` call:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_set_apollo_federation_config" ,
   "args" :   {
     "source" :   "<source_name>" ,
     "table" :   "<table_name>" ,
     "apollo_federation_config" :   {
       "enable" :   "v1"
     }
   }
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/data-federation/apollo-federation/#introduction)
- [ Using Hasura tables in other subgraphs ](https://hasura.io/docs/latest/data-federation/apollo-federation/#using-hasura-tables-in-other-subgraphs)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)