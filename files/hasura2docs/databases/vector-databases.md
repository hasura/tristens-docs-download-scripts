# How Does Hasura Work with Vector Databases?

## What are vectors?​

Vectors are mathematical representations for unstructured data like text, audio, or video data. Vectors generated from
deep neural network models like large language models (LLMs) are of a high-dimension to capture multiple latent
features, which can be then used to classify text, or cluster related text.

Word vectors are numerical representations of individual words that capture their meaning and usage patterns. Each word
is represented as a vector in a high-dimensional space, where the dimensions correspond to different features or
attributes of the word, such as its context, syntactic role, and semantic properties.

## Vectors in the context of Large Language Models​

LLMs are trained on public datasets and until a certain point in time. They can't be used to answer questions on your
new organizational data.

For instance, at the moment, the last training date for OpenAI's `text-davinci-003` model was June 2021 and so it has no
idea about events in 2023.

However, we can steer an LLM to answer queries relevant to our new data by providing the context in which it should
answer the question. This is typically done by providing additional information that it can use. But, given the
limitation on the input size we have to pick the right data to feed to it as context.

We do this by taking all the textual data and chunking it, which is an important strategy for your LLM application.

Now when an input user query comes in, we search for chunks that have similar context and feed to our LLMs.

## Why do we need vector databases?​

Vector databases are optimized to search for similar vectors.

Chunking and then searching for relevant chunks can't be done at query time for large systems with a large amount of
text.

We first chunk and then store all chunked vectors in vector databases so that we can find relevant chunks using semantic
search at the time of query.

## How does Hasura work with vector databases?​

Hasura connects with vector databases just the same way as you would any other relational database. You can quickly and
easily deploy a custom data connector agent to connect to your vector database.

## Next steps​

- [ Connect to a Weaviate vector database ](https://hasura.io/docs/latest/databases/vector-databases/weaviate/)
- [ Learn more about Hasura Data Connectors ](https://hasura.io/docs/latest/databases/data-connectors/)
- [ Deploy a custom data connector agent to Hasura Cloud ](https://hasura.io/docs/latest/hasura-cli/connector-plugin/)


### What did you think of this doc?

- [ What are vectors? ](https://hasura.io/docs/latest/databases/vector-databases/#what-are-vectors)
- [ Vectors in the context of Large Language Models ](https://hasura.io/docs/latest/databases/vector-databases/#vectors-in-the-context-of-large-language-models)
- [ Why do we need vector databases? ](https://hasura.io/docs/latest/databases/vector-databases/#why-do-we-need-vector-databases)
- [ How does Hasura work with vector databases? ](https://hasura.io/docs/latest/databases/vector-databases/#how-does-hasura-work-with-vector-databases-1)
- [ Next steps ](https://hasura.io/docs/latest/databases/vector-databases/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)