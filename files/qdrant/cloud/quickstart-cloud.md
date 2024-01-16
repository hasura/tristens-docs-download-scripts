# Quickstart

This page shows you how to use the Qdrant Cloud Console to create a free tier cluster and then connect to it with Qdrant Client.

## Step 1: Create a Free Tier cluster

1. Start in the **Overview** section of the[ Cloud Dashboard ](https://cloud.qdrant.io).
2. Under **Set a Cluster Up** enter a **Cluster name** .
3. Click **Create Free Tier** and then **Continue** .
4. Under **Get an API Key** , select the cluster and click **Get API Key** .
5. Save the API key, as you won’t be able to request it again. Click **Continue** .
6. Save the code snippet provided to access your cluster. Click **Complete** to finish setup.


Image: [ Embeddings ](https://qdrant.tech/docs/cloud/quickstart-cloud.png)

Image: [ Embeddings ](https://qdrant.tech/docs/cloud/quickstart-cloud.png)

## Step 2: Test cluster access

After creation, you will receive a code snippet to access your cluster. Your generated request should look very similar to this one:

```
curl  \

  -X GET  'https://xyz-example.eu-central.aws.cloud.qdrant.io:6333'   \

  --header  'api-key: <paste-your-api-key-here>' 

```

Open Terminal and run the request. You should get a response that looks like this:

`{ "title" : "qdrant - vector search engine" , "version" : "1.4.1" } 
`

 **Note:** The API key needs to be present in the request header every time you make a request via Rest or gRPC interface.

## Step 3: Authenticate via SDK

Now that you have created your first cluster and key, you might want to access Qdrant Cloud from within your application.
Our official Qdrant clients for Python, TypeScript, Go, Rust, and .NET all support the API key parameter.

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

##### Table of contents

- [ Step 1: Create a Free Tier cluster ](https://qdrant.tech/documentation/cloud/quickstart-cloud/#step-1-create-a-free-tier-cluster)
- [ Step 2: Test cluster access ](https://qdrant.tech/documentation/cloud/quickstart-cloud/#step-2-test-cluster-access)
- [ Step 3: Authenticate via SDK ](https://qdrant.tech/documentation/cloud/quickstart-cloud/#step-3-authenticate-via-sdk)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/quickstart-cloud.md)
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