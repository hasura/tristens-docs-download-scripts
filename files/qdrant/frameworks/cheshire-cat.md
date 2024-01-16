# Cheshire Cat

[ Cheshire Cat ](https://cheshirecat.ai/)is an open-source framework that allows you to develop intelligent agents on top of many Large Language Models (LLM). You can develop your custom AI architecture to assist you in a wide range of tasks.

Image: [ Cheshire cat ](https://qdrant.tech/documentation/frameworks/cheshire-cat/cat.jpg)

Image: [ Cheshire cat ](https://qdrant.tech/documentation/frameworks/cheshire-cat/cat.jpg)

## Cheshire Cat and Qdrant

Cheshire Cat uses Qdrant as the default[ Vector Memory ](https://cheshire-cat-ai.github.io/docs/conceptual/memory/vector_memory/)for ingesting and retrieving documents.

`# Decide host and port for your Cat. Default will be localhost:1865
CORE_HOST=localhost
CORE_PORT=1865

# Qdrant server
# QDRANT_HOST=localhost
# QDRANT_PORT=6333`

Cheshire Cat takes great advantage of the following features of Qdrant:

- [ Collection Aliases ](../../concepts/collections/#collection-aliases)to manage the change from one embedder to another.
- [ Quantization ](../../guides/quantization/)to obtain a good balance between speed, memory usage and quality of the results.
- [ Snapshots ](../../concepts/snapshots/)to not miss any information.
- [ Community ](https://discord.com/invite/tdtYvXjC4h)


Image: [ RAG Pipeline ](https://qdrant.tech/documentation/frameworks/cheshire-cat/stregatto.jpg)

Image: [ RAG Pipeline ](https://qdrant.tech/documentation/frameworks/cheshire-cat/stregatto.jpg)

## How to use the Cheshire Cat

### Requirements

To run the Cheshire Cat, you need to have[ Docker ](https://docs.docker.com/engine/install/)and[ docker-compose ](https://docs.docker.com/compose/install/)already installed on your system.

`docker run --rm -it -p 1865:80 ghcr.io/cheshire-cat-ai/core:latest
`

- Chat with the Cheshire Cat on[ localhost:1865/admin ](http://localhost:1865/admin).
- You can also interact via REST API and try out the endpoints on[ localhost:1865/docs ](http://localhost:1865/docs)


Check the[ instructions on github ](https://github.com/cheshire-cat-ai/core/blob/main/README.md)for a more comprehensive quick start.

### First configuration of the LLM

- Open the Admin Portal in your browser at[ localhost:1865/admin ](http://localhost:1865/admin).
- Configure the LLM in the `Settings` tab.
- If you don’t explicitly choose it using `Settings` tab, the Embedder follows the LLM.


## Next steps

For more information, refer to the Cheshire Cat[ documentation ](https://cheshire-cat-ai.github.io/docs/)and[ blog ](https://cheshirecat.ai/blog/).

- [ Getting started ](https://cheshirecat.ai/hello-world/)
- [ How the Cat works ](https://cheshirecat.ai/how-the-cat-works/)
- [ Write Your First Plugin ](https://cheshirecat.ai/write-your-first-plugin/)
- [ Cheshire Cat’s use of Qdrant - Vector Space ](https://cheshirecat.ai/dont-get-lost-in-vector-space/)
- [ Cheshire Cat’s use of Qdrant - Aliases ](https://cheshirecat.ai/the-drunken-cat-effect/)
- [ Discord Community ](https://discord.com/invite/bHX5sNFCYU)


##### Table of contents

- [ Cheshire Cat and Qdrant ](https://qdrant.tech/documentation/frameworks/cheshire-cat/#cheshire-cat-and-qdrant)
- [ How to use the Cheshire Cat ](https://qdrant.tech/documentation/frameworks/cheshire-cat/#how-to-use-the-cheshire-cat)
    - [ Requirements ](https://qdrant.tech/documentation/frameworks/cheshire-cat/#requirements)

- [ First configuration of the LLM ](https://qdrant.tech/documentation/frameworks/cheshire-cat/#first-configuration-of-the-llm)
- [ Next steps ](https://qdrant.tech/documentation/frameworks/cheshire-cat/#next-steps)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/cheshire-cat.md)
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