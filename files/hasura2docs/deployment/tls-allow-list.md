# Insecure TLS Allow List

## Introduction​

Transport Layer Security (TLS) is the successor to and improved protocol of SSL. It works in much the same way as
SSL, using encryption to protect the transfer of data and information and secure HTTP traffic.

The TLS Allow List represents a set of services in Hasura GraphQL Engine that are permitted to use self-signed CA
certificates - primarily intended for use in development and staging environments. These services can be whitelisted
by a host domain, and optionally a (service id) port.

## Add and remove hosts from the TLS allow list​

- Console
- CLI
- API


To add a host to the insecure TLS allow list in the Console go to the `Settings` tab (⚙) tab and click on `Insecure TLS Allow List` in the left sidebar. Click on *Add Domain* and enter the host domain and port (if
applicable). Click on *Add to Allow List* to add the host to the allow list.

Image: [ Add a host to the TLS allow list ](https://hasura.io/docs/assets/images/settings_insecure-tls-allow-list_2-17-0-f186e3043de4734bd5b158fdd7f03631.png)

To remove the host, click the *Delete* button.

To add a host to the insecure TLS allow list using metadata, go to the `metadata -> network.yaml` file, add the host
domain and port (if applicable) to the `tls_allowlist` section.

```
tls_allowlist :
   -   host :  localhost
     permissions :
       -  self - signed
     suffix :   "4183"
```

Apply the Metadata by running:

`hasura metadata apply`

To remove a host from the list, delete the entry and reapply the metadata.

To add a host to the TLS allow list using the API execute the following request with your defined host domain and
port (if applicable):

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "add_host_to_tls_allowlist" ,
   "args" :   {
     "host" :   "localhost" ,
     "suffix" :   "4183" ,
     "permissions" :   [ "self-signed" ]
   }
}
```

To remove a host from the list, execute the following request with the domain you want to remove:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "drop_host_from_tls_allowlist" ,
   "args" :   {
     "host" :   "localhost" ,
     "suffix" :   "4183"
   }
}
```

For more information see the[ API reference ](https://hasura.io/docs/latest/api-reference/metadata-api/network/#tls-allowlist).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/tls-allow-list/#introduction)
- [ Add and remove hosts from the TLS allow list ](https://hasura.io/docs/latest/deployment/tls-allow-list/#add-and-remove-hosts-from-the-tls-allow-list)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)