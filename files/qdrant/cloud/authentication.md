# Authentication

This page shows you how to use the Qdrant Cloud Console to create a custom API key for a cluster. You will learn how to connect to your cluster using the new API key.

## Create API keys

The API key is only shown once after creation. If you lose it, you will need to create a new one.
However, we recommend rotating the keys from time to time. To create additional API keys do the following.

1. Go to the[ Cloud Dashboard ](https://qdrant.to/cloud).
2. Select **Access Management** to display available API keys.
3. Click **Create** and choose a cluster name from the dropdown menu.


 **Note:** You can create a key that provides access to multiple clusters. Select desired clusters in the dropdown box.

1. Click **OK** and retrieve your API key.


## Authenticate via SDK

Now that you have created your first cluster and key, you might want to access Qdrant Cloud from within your application.
Our official Qdrant clients for Python, TypeScript, Go, Rust, and .NET all support the API key parameter.

```
curl  \

  -X GET https://xyz-example.eu-central.aws.cloud.qdrant.io:6333  \

  --header  'api-key: <provide-your-own-key>' 



# Alternatively, you can use the `Authorization` header with the `Bearer` prefix 

curl  \

  -X GET https://xyz-example.eu-central.aws.cloud.qdrant.io:6333  \

  --header  'Authorization: Bearer <provide-your-own-key>' 

```

```
from   qdrant_client   import  QdrantClient



qdrant_client  =  QdrantClient(

     "xyz-example.eu-central.aws.cloud.qdrant.io" ,

    api_key = "<paste-your-api-key-here>" ,

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({

  host :   "xyz-example.eu-central.aws.cloud.qdrant.io" ,

  apiKey :   "<paste-your-api-key-here>" ,

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



let   client   =   QdrantClient::from_url( "xyz-example.eu-central.aws.cloud.qdrant.io:6334" ) 

     .with_api_key( "<paste-your-api-key-here>" ) 

     .build() 

     .unwrap(); 

```

##### Table of contents

- [ Create API keys ](https://qdrant.tech/documentation/cloud/authentication/#create-api-keys)
- [ Authenticate via SDK ](https://qdrant.tech/documentation/cloud/authentication/#authenticate-via-sdk)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/authentication.md)
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