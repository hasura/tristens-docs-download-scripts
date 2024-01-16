# Haystack

[ Haystack ](https://haystack.deepset.ai/)serves as a comprehensive NLP framework, offering a modular methodology for constructing
cutting-edge generative AI, QA, and semantic knowledge base search systems. A critical element in contemporary NLP systems is an
efficient database for storing and retrieving extensive text data. Vector databases excel in this role, as they house vector
representations of text and implement effective methods for swift retrieval. Thus, we are happy to announce the integration
with Haystack - `QdrantDocumentStore` . This document store is unique, as it is maintained externally by the Qdrant team.

The new document store comes as a separate package and can be updated independently of Haystack:

`pip install qdrant-haystack
`

 `QdrantDocumentStore` supports[ all the configuration properties ](https://qdrant.tech/documentation/collections/#create-collection)available in
the Qdrant Python client. If you want to customize the default configuration of the collection used under the hood, you can
provide that settings when you create an instance of the `QdrantDocumentStore` . For example, if you’d like to enable the
Scalar Quantization, you’d make that in the following way:

```
from   qdrant_haystack.document_stores   import  QdrantDocumentStore

from   qdrant_client.http   import  models



document_store  =  QdrantDocumentStore(

     ":memory:" ,

    index = "Document" ,

    embedding_dim = 512 ,

    recreate_index = True ,

    quantization_config = models . ScalarQuantization(

        scalar = models . ScalarQuantizationConfig(

             type = models . ScalarType . INT8,

            quantile = 0.99 ,

            always_ram = True ,

        ),

    ),

)

```

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