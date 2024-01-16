# Installation options

## Docker

The easiest way to start using Qdrant is to run it from a ready-made Docker image.
The latest versions are always available on[ DockerHub ](https://hub.docker.com/r/qdrant/qdrant/tags?page=1&ordering=last_updated).

Make sure that Docker daemon is installed and running:

`sudo docker info
`

- If you do not see the server listed, start the Docker daemon.
- On Linux, Docker needs `sudo` privileges. To run Docker commands without `sudo` privileges, create a docker group and add your users (see[ Post-installation Steps for Linux ](https://docs.docker.com/engine/install/linux-postinstall/)for details).


Pull the image:

`docker pull qdrant/qdrant
`

Run the container:

```
docker run -p 6333:6333  \

    -v  $( pwd ) /path/to/data:/qdrant/storage  \

    qdrant/qdrant

```

With this command, you will start a Qdrant instance with the default configuration.
It will store all data in `./path/to/data` directory.

By default, Qdrant uses port 6333, so at[ localhost:6333 ](http://localhost:6333)you should see the welcome message.

## From source

Qdrant is written in Rust and can be compiled into a binary executable.
This installation method can be helpful if you want to compile Qdrant for a specific processor architecture or if you do not want to use Docker for some reason.

Before compiling, make sure that the necessary libraries and the[ rust toolchain ](https://www.rust-lang.org/tools/install)are installed.
The current list of required libraries can be found in the[ Dockerfile ](https://github.com/qdrant/qdrant/blob/master/Dockerfile).

Build Qdrant with Cargo:

`cargo build --release --bin qdrant
`

After a successful build, the binary is available at `./target/release/qdrant` .

## Python client

In addition to the service itself, Qdrant has a distinct python client, which has some additional features compared to[ clients ](https://qdrant.tech/documentation/quick_start/#clients)generated from OpenAPI directly.

To install this client, just run the following command:

`pip install qdrant-client
`

## Kubernetes

You can use a ready-made[ Helm Chart ](https://helm.sh/docs/)to run Qdrant in your Kubeternetes cluster.

```
helm repo add qdrant https://qdrant.to/helm

helm install qdrant-release qdrant/qdrant

```

Read further instructions in[ qdrant-helm ](https://github.com/qdrant/qdrant-helm)repository.

##### Table of contents

- [ Docker ](https://qdrant.tech/documentation/guides/installation/#docker)
- [ From source ](https://qdrant.tech/documentation/guides/installation/#from-source)
- [ Python client ](https://qdrant.tech/documentation/guides/installation/#python-client)
- [ Kubernetes ](https://qdrant.tech/documentation/guides/installation/#kubernetes)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/installation.md)
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