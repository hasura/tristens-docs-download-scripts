# Using Qdrant asynchronously

Asynchronous programming is being broadly adopted in the Python ecosystem. Tools such as FastAPI[ have embraced this new
paradigm ](https://fastapi.tiangolo.com/async/), but it is also becoming a standard for ML models served as SaaS. For example, the Cohere SDK[ provides an async client ](https://cohere-sdk.readthedocs.io/en/latest/cohere.html#asyncclient)next to its synchronous counterpart.

Databases are often launched as separate services and are accessed via a network. All the interactions with them are IO-bound and can
be performed asynchronously so as not to waste time actively waiting for a server response. In Python, this is achieved by
using[ async/await ](https://docs.python.org/3/library/asyncio-task.html)syntax. That lets the interpreter switch to another task
while waiting for a response from the server.

## When to use async API

There is no need to use async API if the application you are writing will never support multiple users at once (e.g it is a script that runs once per day). However, if you are writing a web service that multiple users will use simultaneously, you shouldn’t be
blocking the threads of the web server as it limits the number of concurrent requests it can handle. In this case, you should use
the async API.

Modern web frameworks like[ FastAPI ](https://fastapi.tiangolo.com/)and[ Quart ](https://quart.palletsprojects.com/en/latest/)support
async API out of the box. Mixing asynchronous code with an existing synchronous codebase might be a challenge. The `async/await` syntax
cannot be used in synchronous functions. On the other hand, calling an IO-bound operation synchronously in async code is considered
an antipattern. Therefore, if you build an async web service, exposed through an[ ASGI ](https://asgi.readthedocs.io/en/latest/)server,
you should use the async API for all the interactions with Qdrant.

`asyncio.run`

`asyncio.create_task`

### Using Qdrant asynchronously

The simplest way of running asynchronous code is to use define `async` function and use the `asyncio.run` in the following way to run it:

```
from   qdrant_client   import  models



import   qdrant_client 

import   asyncio 





async   def   main ():

    client  =  qdrant_client . AsyncQdrantClient( "localhost" )



     # Create a collection 

     await  client . create_collection(

        collection_name = "my_collection" ,

        vectors_config = models . VectorParams(size = 4 , distance = models . Distance . COSINE),

    )



     # Insert a vector 

     await  client . upsert(

        collection_name = "my_collection" ,

        points = [

            models . PointStruct(

                 id = "5c56c793-69f3-4fbf-87e6-c4bf54c28c26" ,

                payload = {

                     "color" :  "red" ,

                },

                vector = [ 0.9 ,  0.1 ,  0.1 ,  0.5 ],

            ),

        ],

    )



     # Search for nearest neighbors 

    points  =   await  client . search(

        collection_name = "my_collection" ,

        query_vector = [ 0.9 ,  0.1 ,  0.1 ,  0.5 ],

        limit = 2 ,

    )



     # Your async code using AsyncQdrantClient might be put here 

     # ... 





asyncio . run(main())

```

The `AsyncQdrantClient` provides the same methods as the synchronous counterpart `QdrantClient` . If you already have a synchronous
codebase, switching to async API is as simple as replacing `QdrantClient` with `AsyncQdrantClient` and adding `await` before each
method call.

`qdrant-client`

## Supported Python libraries

Qdrant integrates with numerous Python libraries. Until recently, only[ Langchain ](https://python.langchain.com)provided async Python API support.
Qdrant is the only vector database with full coverage of async API in Langchain. Their documentation[ describes how to use
it ](https://python.langchain.com/docs/modules/data_connection/vectorstores/#asynchronous-operations).

##### Table of contents

- [ When to use async API ](https://qdrant.tech/documentation/tutorials/async-api/#when-to-use-async-api)
    - [ Using Qdrant asynchronously ](https://qdrant.tech/documentation/tutorials/async-api/#using-qdrant-asynchronously-1)
- [ Supported Python libraries ](https://qdrant.tech/documentation/tutorials/async-api/#supported-python-libraries)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/tutorials/async-api.md)
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