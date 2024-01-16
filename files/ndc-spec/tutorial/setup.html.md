# Hasura Data Connectors Developer's Guide

# Setup

To compile and run the reference implementation, you will need to install a Rust toolchain, and then run:

```
git
clone
git@github.com:hasura/ndc-spec.git
cd
ndc-spec/ndc-reference
cargo build
cargo run
```

Alternatively, you can run the reference implementation entirely inside a Docker container:

```
git
clone
git@github.com:hasura/ndc-spec.git
cd
ndc-spec
docker build -t reference_connector .
docker run -it reference_connector
```

Either way, you should have a working data connector running on[ http://localhost:8100/ ](http://localhost:8100/), which you can test as follows:

`curl http://localhost:8100/schema`