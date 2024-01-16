# Interfaces

 **Note:** If you are using a language that is not listed here, you can use the REST API directly or generate a client for your language
using[ OpenAPI ](https://github.com/qdrant/qdrant/blob/master/docs/redoc/master/openapi.json)or[ protobuf ](https://github.com/qdrant/qdrant/tree/master/lib/api/src/grpc/proto)definitions.

## Client Libraries

|  | Client Repository | Installation | Version |
|---|---|---|---|
| [  ](https://python-client.qdrant.tech/) |  **Python**  |  `pip install qdrant-client[fastembed]`  |  **Latest Release** ,[ API Docs ](https://python-client.qdrant.tech/) |
| Image: [ typescript ](https://qdrant.tech/docs/misc/ts.webp) |  **Typescript**  |  `npm install @qdrant/js-client-rest`  |  **Latest Release**  |
| Image: [ rust ](https://qdrant.tech/docs/misc/rust.webp) |  **Rust**  |  `cargo add qdrant-client`  |  **Latest Release**  |
| Image: [ golang ](https://qdrant.tech/docs/misc/go.webp) |  **Go**  |  `go get github.com/qdrant/go-client`  |  **Latest Release**  |
| Image: [ .net ](https://qdrant.tech/docs/misc/dotnet.webp) |  **.NET**  |  `dotnet add package Qdrant.Client`  |  **Latest Release**  |


Image: [ python ](https://qdrant.tech/docs/misc/python.webp)

Image: [ typescript ](https://qdrant.tech/docs/misc/ts.webp)

Image: [ rust ](https://qdrant.tech/docs/misc/rust.webp)

Image: [ golang ](https://qdrant.tech/docs/misc/go.webp)

Image: [ .net ](https://qdrant.tech/docs/misc/dotnet.webp)

## API Reference

All interaction with Qdrant takes place via the REST API. We recommend using REST API if you are using Qdrant for the first time or if you are working on a prototype.

| API | Documentation |
|---|---|
| REST API | [ OpenAPI Specification ](https://qdrant.github.io/qdrant/redoc/index.html) |
| gRPC API | [ gRPC Documentation ](https://github.com/qdrant/qdrant/blob/master/docs/grpc/docs.md) |


### gRPC Interface

The gRPC methods follow the same principles as REST. For each REST endpoint, there is a corresponding gRPC method.

As per the[ configuration file ](https://github.com/qdrant/qdrant/blob/master/config/config.yaml), the gRPC interface is available on the specified port.

```
service : 

   grpc_port :   6334 

```

Running the service inside of Docker will look like this:

```
docker run -p 6333:6333 -p 6334:6334  \

    -v  $( pwd ) /qdrant_storage:/qdrant/storage:z  \

    qdrant/qdrant

```

 **When to use gRPC:** The choice between gRPC and the REST API is a trade-off between convenience and speed. gRPC is a binary protocol and can be more challenging to debug. We recommend using gRPC if you are already familiar with Qdrant and are trying to optimize the performance of your application.

## Qdrant Web UI

Qdrant’s Web UI is an intuitive and efficient graphic interface for your Qdrant Collections, REST API and data points.

In the **Console** , you may use the REST API to interact with Qdrant, while in **Collections** , you can manage all the collections and upload Snapshots.

Image: [ Qdrant Web UI ](https://qdrant.tech/articles_data/qdrant-1.3.x/web-ui.png)

Image: [ Qdrant Web UI ](https://qdrant.tech/articles_data/qdrant-1.3.x/web-ui.png)

### Accessing the Web UI

First, run the Docker container:

```
docker run -p 6333:6333 -p 6334:6334  \

    -v  $( pwd ) /qdrant_storage:/qdrant/storage:z  \

    qdrant/qdrant

```

The GUI is available at `http://localhost:6333/dashboard` 

##### Table of contents

- [ Client Libraries ](https://qdrant.tech/documentation/interfaces/#client-libraries)
- [ API Reference ](https://qdrant.tech/documentation/interfaces/#api-reference)
    - [ gRPC Interface ](https://qdrant.tech/documentation/interfaces/#grpc-interface)
- [ Qdrant Web UI ](https://qdrant.tech/documentation/interfaces/#qdrant-web-ui)
    - [ Accessing the Web UI ](https://qdrant.tech/documentation/interfaces/#accessing-the-web-ui)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/interfaces.md)
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