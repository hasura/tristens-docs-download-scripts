# PrivateGPT

[ PrivateGPT ](https://docs.privategpt.dev/)is a production-ready AI project that allows you to inquire about your documents using Large Language Models (LLMs) with offline support.

PrivateGPT uses Qdrant as the default vectorstore for ingesting and retrieving documents.

## Configuration

Qdrant settings can be configured by setting values to the qdrant property in the `settings.yaml` file. By default, Qdrant tries to connect to an instance at http://localhost:3000.

Example:

```
qdrant : 

     url :   "https://xyz-example.eu-central.aws.cloud.qdrant.io:6333" 

     api_key :   "<your-api-key>" 

```

The available[ configuration options ](https://docs.privategpt.dev/manual/storage/vector-stores#qdrant-configuration)are:

| Field | Description |
|---|---|
| location | If `:memory:` - use in-memory Qdrant instance.
If `str` - use it as a `url` parameter. |
| url | Either host or str of `Optional[scheme], host, Optional[port], Optional[prefix]` .
Eg. `http://localhost:6333`  |
| port | Port of the REST API interface. Default: `6333`  |
| grpc_port | Port of the gRPC interface. Default: `6334`  |
| prefer_grpc | If `true` - use gRPC interface whenever possible in custom methods. |
| https | If `true` - use HTTPS(SSL) protocol. |
| api_key | API key for authentication in Qdrant Cloud. |
| prefix | If set, add `prefix` to the REST URL path.
Example: `service/v1` will result in `http://localhost:6333/service/v1/{qdrant-endpoint}` for REST API. |
| timeout | Timeout for REST and gRPC API requests.
Default: 5.0 seconds for REST and unlimited for gRPC |
| host | Host name of Qdrant service. If url and host are not set, defaults to ’localhost'. |
| path | Persistence path for QdrantLocal. Eg. `local_data/private_gpt/qdrant`  |
| force_disable_check_same_thread | Force disable check_same_thread for QdrantLocal sqlite connection. |


## Next steps

Find the PrivateGPT docs[ here ](https://docs.privategpt.dev/).

##### Table of contents

- [ Configuration ](https://qdrant.tech/documentation/frameworks/privategpt/#configuration)
- [ Next steps ](https://qdrant.tech/documentation/frameworks/privategpt/#next-steps)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/privategpt.md)
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