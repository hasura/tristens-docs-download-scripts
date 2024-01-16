# Security

Please read this page carefully. Although there are various ways to secure your Qdrant instances, **they are unsecured by default** .
You need to enable security measures before production use. Otherwise, they are completely open to anyone

## Authentication

 *Available as of v1.2.0* 

Qdrant supports a simple form of client authentication using a static API key.
This can be used to secure your instance.

To enable API key based authentication in your own Qdrant instance you must
specify a key in the configuration:

```
service : 

   # Set an api-key. 

   # If set, all requests must include a header with the api-key. 

   # example header: `api-key: <API-KEY>` 

   # 

   # If you enable this you should also enable TLS. 

   # (Either above or via an external service like nginx.) 

   # Sending an api-key over an unencrypted channel is insecure. 

   api_key :   your_secret_api_key_here 

```

For using API key based authentication in Qdrant cloud see the cloud[ Authentication ](https://qdrant.tech/documentation/cloud/authentication)section.

The API key then needs to be present in all REST or gRPC requests to your instance.
All official Qdrant clients for Python, Go, Rust, and .NET support the API key parameter.

```
curl  \

  -X GET https://localhost:6333  \

  --header  'api-key: your_secret_api_key_here' 

```

```
from   qdrant_client   import  QdrantClient



client  =  QdrantClient(

    url = "https://localhost" ,

    port = 6333 ,

    api_key = "your_secret_api_key_here" ,

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({

  url :   "http://localhost" ,

  port:  6333 ,

  apiKey :   "your_secret_api_key_here" ,

});

```

```
using   Qdrant.Client ;



var  client =  new  QdrantClient(

   "xyz-example.eu-central.aws.cloud.qdrant.io" ,

  https:  true ,

  apiKey:  "<paste-your-api-key-here>" 

);

```

```
use   qdrant_client::client::QdrantClient; 



let   client   =   QdrantClient::from_url( "https://xyz-example.eu-central.aws.cloud.qdrant.io:6334" ) 

         .with_api_key( "<paste-your-api-key-here>" ) 

         .build() ? ; 

```

### Read-only API key

In addition to the regular API key, Qdrant also supports a read-only API key.
This key can be used to access read-only operations on the instance.

```
service : 

   read_only_api_key :   your_secret_read_only_api_key_here 

```

Or with the environment variable:

`export   QDRANT__SERVICE__READ_ONLY_API_KEY = your_secret_read_only_api_key_here
`

Both API keys can be used simultaneously.

## TLS

 *Available as of v1.2.0* 

TLS for encrypted connections can be enabled on your Qdrant instance to secure
connections.

First make sure you have a certificate and private key for TLS, usually in `.pem` format. On your local machine you may use[ mkcert ](https://github.com/FiloSottile/mkcert#readme)to generate a self signed
certificate.

To enable TLS, set the following properties in the Qdrant configuration with the
correct paths and restart:

```
service : 

   # Enable HTTPS for the REST and gRPC API 

   enable_tls :   true 



# TLS configuration. 

# Required if either service.enable_tls or cluster.p2p.enable_tls is true. 

tls : 

   # Server certificate chain file 

   cert :   ./tls/cert.pem 



   # Server private key file 

   key :   ./tls/key.pem 

```

For internal communication when running cluster mode, TLS can be enabled with:

```
cluster : 

   # Configuration of the inter-cluster communication 

   p2p : 

     # Use TLS for communication between peers 

     enable_tls :   true 

```

With TLS enabled, you must start using HTTPS connections. For example:

`curl -X GET https://localhost:6333
`

```
from   qdrant_client   import  QdrantClient



client  =  QdrantClient(

    url = "https://localhost" ,

    port = 6333 ,

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ url :   "https://localhost" , port:  6333  });

```

```
use   qdrant_client::client::QdrantClient; 



let   client   =   QdrantClient::from_url( "https://localhost:6334" ).build() ? ; 

```

Certificate rotation is enabled with a default refresh time of one hour. This
reloads certificate files every hour while Qdrant is running. This way changed
certificates are picked up when they get updated externally. The refresh time
can be tuned by changing the `tls.cert_ttl` setting. You can leave this on, even
if you don’t plan to update your certificates. Currently this is only supported
for the REST API.

Optionally, you can enable client certificate validation on the server against a
local certificate authority. Set the following properties and restart:

```
service : 

   # Check user HTTPS client certificate against CA file specified in tls config 

   verify_https_client_certificate :   false 



# TLS configuration. 

# Required if either service.enable_tls or cluster.p2p.enable_tls is true. 

tls : 

   # Certificate authority certificate file. 

   # This certificate will be used to validate the certificates 

   # presented by other nodes during inter-cluster communication. 

   # 

   # If verify_https_client_certificate is true, it will verify 

   # HTTPS client certificate 

   # 

   # Required if cluster.p2p.enable_tls is true. 

   ca_cert :   ./tls/cacert.pem 

```

##### Table of contents

- [ Authentication ](https://qdrant.tech/documentation/guides/security/#authentication)
    - [ Read-only API key ](https://qdrant.tech/documentation/guides/security/#read-only-api-key)
- [ TLS ](https://qdrant.tech/documentation/guides/security/#tls)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/security.md)
- [ 
 Create an Issue
 ](https://github.com/qdrant/landing_page/issues/new/choose)


#### Product

- [ 
Use cases
 ](https://qdrant.tech/use-cases/)
- [ 
Solutions
 ](https://qdrant.tech/solutions/)
- [ 
Benchmarks
 ](https://qdrant.tech/benchmarks/)
- [ 
Demos
 ](https://qdrant.tech/demo/)
- [ 
Pricing
 ](https://qdrant.tech/pricing/)


#### Community

- [ 
 
Github
 ](https://github.com/qdrant/qdrant)
- [ 
 
Discord
 ](https://qdrant.to/discord)
- [ 
 
Twitter
 ](https://qdrant.to/twitter)
- [ 
 
Newsletter
 ](https://qdrant.tech/subscribe/)
- [ 
 
Contact us
 ](https://qdrant.to/contact-us)


#### Company

- [ 
Jobs
 ](https://qdrant.join.com)
- [ 
Privacy Policy
 ](https://qdrant.tech/legal/privacy-policy/)
- [ 
Terms
 ](https://qdrant.tech/legal/terms_and_conditions/)
- [ 
Impressum
 ](https://qdrant.tech/legal/impressum/)
- [ 
Credits
 ](https://qdrant.tech/legal/credits/)


#### Latest Publications

#### Combining the precision of exact keyword search with NN-based ranking

#### Qdrant 1.7.0 brought a bunch of new features. Let's take a closer look at them!

#### Qdrant 1.6 brings recommendations strategies and more flexibility to the Recommendation API.

- [  ](https://github.com/qdrant/qdrant)
- [  ](https://qdrant.to/linkedin)
- [  ](https://qdrant.to/twitter)
- [  ](https://qdrant.to/discord)
- [  ](https://www.youtube.com/channel/UC6ftm8PwH1RU_LM1jwG0LQA)


##### Thanks for using Qdrant!

Subscribe to our e-mail newsletter if you want to be updated on new features and news regarding
Qdrant.

Like what we are doing? Consider giving us a ⭐[ on Github ](https://github.com/qdrant/qdrant).

We use cookies to learn more about you. At any time you can delete or block cookies through your browser settings.