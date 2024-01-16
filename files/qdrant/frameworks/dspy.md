# Stanford DSPy

[ DSPy ](https://github.com/stanfordnlp/dspy)is the framework for solving advanced tasks with language models (LMs) and retrieval models (RMs). It unifies techniques for prompting and fine-tuning LMs — and approaches for reasoning, self-improvement, and augmentation with retrieval and tools.

- Provides composable and declarative modules for instructing LMs in a familiar Pythonic syntax.
- Introduces an automatic compiler that teaches LMs how to conduct the declarative steps in your program.


Provides composable and declarative modules for instructing LMs in a familiar Pythonic syntax.

Introduces an automatic compiler that teaches LMs how to conduct the declarative steps in your program.

Qdrant can be used as a retrieval mechanism in the DSPy flow.

## Installation

For the Qdrant retrieval integration, include `dspy-ai` with the `qdrant` extra:

`pip install dspy-ai [ qdrant ] 
`

## Usage

We can configure `DSPy` settings to use the Qdrant retriever model like so:

```
import   dspy 

from   dspy.retrieve.qdrant_rm   import  QdrantRM



from   qdrant_client   import  QdrantClient



turbo  =  dspy . OpenAI(model = "gpt-3.5-turbo" )

qdrant_client  =  QdrantClient()   # Defaults to a local instance at http://localhost:6333/ 

qdrant_retriever_model  =  QdrantRM( "collection-name" , qdrant_client, k = 3 )



dspy . settings . configure(lm = turbo, rm = qdrant_retriever_model)

```

Using the retriever is pretty simple. The `dspy.Retrieve(k)` module will search for the top-k passages that match a given query.

```
retrieve  =  dspy . Retrieve(k = 3 )

question  =   "Some question about my data" 

topK_passages  =  retrieve(question) . passages



print ( f "Top  { retrieve . k }  passages for question:  { question }   \n " ,  " \n " )



for  idx, passage  in   enumerate (topK_passages):

     print ( f " { idx + 1 } ]" , passage,  " \n " )

```

With Qdrant configured as the retriever for contexts, you can set up a DSPy module like so:

```
class   RAG (dspy . Module):

     def  __init__(self, num_passages = 3 ):

         super () . __init__()



        self . retrieve  =  dspy . Retrieve(k = num_passages)

         ... 



     def   forward (self, question):

        context  =  self . retrieve(question) . passages

         ... 

```

With the generic RAG blueprint now in place, you can add the many interactions offered by DSPy with context retrieval powered by Qdrant.

## Next steps

Find DSPy usage docs and examples[ here ](https://github.com/stanfordnlp/dspy#4-documentation--tutorials).

##### Table of contents

- [ Installation ](https://qdrant.tech/documentation/frameworks/dspy/#installation)
- [ Usage ](https://qdrant.tech/documentation/frameworks/dspy/#usage)
- [ Next steps ](https://qdrant.tech/documentation/frameworks/dspy/#next-steps)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/dspy.md)
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