# libSQL database URLs

Throughout this documentation, the[ Turso CLI ](https://docs.turso.tech/reference/turso-cli), and the[ libSQL client SDKs ](https://docs.turso.tech/libsql/client-access/),
you will notice examples of URLs that start with `libsql://` . These URLs are
recognized by libSQL and Turso tools with the following meaning.

## Database endpoint identification​

A `libsql` URL identifies a libSQL logical database running[ libSQL server ](https://github.com/libsql/libsql#readme). A
logical database URL connects to an[ instance ](https://docs.turso.tech/concepts#instance)of the database (primary or
replica) with the lowest latency to the machine making the connection. You can
get the URL for a logical database using `turso db list` and `turso db show` .
Logical database URLs have the following format:

`libsql://[DB-NAME]-[ORG-NAME].turso.io`

info

Turso depends on the hosting service Fly.io to determine the lowest latency
instance for a client connection. Typically, this will be the geographically
closest instance to the machine running the client, though that may not always
be the case. A client using a logical database URL might connect to different
instances over time depending on how Fly.io observes network latency.

## Network protocol​

When provided with a libsql URL, libSQL client libraries are free to choose what
they consider to be the best (or only) available protocol that works in the
runtime environment where they are running. libSQL server supports both
WebSockets and HTTP. Some cloud and edge function providers might not support
WebSockets, with HTTP being the only working choice.

It's possible that some SDK features might not be available depending on the
chosen protocol. You should consult the SDK documentation for details. In the
future, each SDK will expose a way to find out which protocol was chosen by the
client object.

In order to optimize the latency of your application, or use libSQL server
instances other than those managed by Turso, you might want to choose a
protocol. The protocol is selected using the scheme of the URL. libSQL clients
generally support the following schemes: `http` , `https` , `ws` , `wss` . If you
want to specify the use HTTPS, you can replace the `libsql` scheme of the URL
with `https` . For example, a logical database URL that specifies `https` has the
following format:

`https://[DB-NAME]-[ORG-NAME].turso.io`

info

Turso databases support only the secure `https` and `wss` schemes. `ws` and `http` are typically only used when developing against a libSQL server instance
running locally that can't be configured with an SSL certificate.

The underlying data sent using WebSockets or HTTP is expressed as JSON.
Documentation for this protocol and the structure of its messages is
forthcoming.

### Latency optimization​

WebSockets tend to perform better when the client SDK can hold a socket open
over time to handle multiple queries. However, HTTP tends to perform better for
a single query since it requires fewer round trips between client and server.
You should benchmark both options if there is any doubt which is better for your
use case.

- [ Database endpoint identification ](https://docs.turso.tech//reference/libsql-urls/#database-endpoint-identification)
- [ Network protocol ](https://docs.turso.tech//reference/libsql-urls/#network-protocol)
    - [ Latency optimization ](https://docs.turso.tech//reference/libsql-urls/#latency-optimization)


- [ 

Sign Up




 ](https://api.turso.tech/?webui=true&type=signup)
- [ 

Star Our Repo






 ](https://github.com/libsql/libsql)


Sign Up

Star Our Repo

- [ About ](https://turso.tech/about-us)
- [ Investors ](https://turso.tech/investors)
- [ Blog ](https://blog.turso.tech)


- [ Turso Discord ](https://discord.com/invite/4B5D7hYwub)
- [ libSQL Discord ](https://discord.gg/VzbXemj6Rg)
- [ Follow us on Twitter ](https://twitter.com/tursodatabase)
- [ Schedule a Zoom ](https://calendly.com/d/gt7-bfd-83n/meet-with-chiselstrike)


- [ Turso GitHub ](https://github.com/tursodatabase/)
- [ Turso extended GitHub ](https://github.com/turso-extended/)
- [ libSQL GitHub ](http://github.com/tursodatabase/libsql)


- [ Privacy Policy ](https://turso.tech/privacy-policy)
- [ Terms of Use ](https://turso.tech/terms-of-use)


Image: [ Turso logo ](https://docs.turso.tech/img/turso.svg)