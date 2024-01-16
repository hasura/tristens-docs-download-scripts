# Client SDKs

libSQL provides client SDKs that work for a variety of use cases:

- [ Local access ](https://docs.turso.tech//libsql/client-access#interactive-transactions/#local-access)(in-memory, or using the same database file
format as SQLite)
- [ Remote access ](https://docs.turso.tech//libsql/client-access#interactive-transactions/#remote-access)using a libSQL server instance (including
Turso)
- [ Hybrid access ](https://docs.turso.tech//libsql/client-access#interactive-transactions/#hybrid-access)using an embedded replica of data primarily hosted by libSQL
server


SDKs are provided for the following languages:

- [ JavaScript & TypeScript ](https://docs.turso.tech/libsql/client-access/javascript-typescript-sdk)
- [ Rust ](https://docs.turso.tech/libsql/client-access/rust-sdk)
- [ Python ](https://docs.turso.tech/libsql/client-access/python-sdk)
- [ Go ](https://docs.turso.tech/libsql/client-access/go-sdk)


## Access types​

### Local access​

When building an application that uses a local database, the client libraries
can act as a replacement for embedded SQLite (using the[ libSQL core library ](https://github.com/libsql/libsql)with native language bindings). The database can be in memory, or persisted to a
file using the same database file format as SQLite.

To use a libSQL client SDK for local database access, you must provide a `file:` URL with the path to the database file to use. The SDK attempts to create the
file if it doesn’t exist.

### Remote access​

When building an application that uses a remote libSQL server (including Turso),
you can use libSQL client libraries that communicate with the server over HTTP
using a custom protocol (“hrana”). This is appropriate for code deployed to edge
and serverless frameworks that act as an API gateway or middleware for a client
application.

To use a libSQL client SDK for remote database access, you must provide an `http:` , `https:` , or `libsql:` URL identifying the libSQL server to use.

#### Turso databases​

For databases hosted by Turso, you must provide a libsql URL and authentication
token.  The URL for a database can be found using the Turso CLI:

`$ turso db show  $DBNAME  --url`

You can generate a new[ database client authentication token ](https://docs.turso.tech/reference/turso-cli#database-client-authentication-tokens)using the
following command:

`$ turso db tokens create  $DBNAME`

### Hybrid access (embedded replica)​

info

Hybrid access with embedded replicas is currently only supported for the
JavaScript runtimes Node.js, Bun, and Deno with write access to a filesystem.
Support for hybrid access requires version 0.3.5 or later of the JavaScript SDK.

The libSQL client SDKs have the ability to maintain an embedded local copy of
the data hosted by a remote libSQL server for fast read access without requiring
network connectivity at the time of the query. Applications can request the
latest updates from the remote server by simply calling a method. libSQL then
figures out which changes on the remote server must be synchronized to the local
replica. When the host application performs a write operation, it’s forwarded to
the remote libSQL server for execution, similar to the way that all writes to a
libSQL server replica are forwarded to the primary instance.

## Client SDK capabilities​

### Batches​

With the libSQL client library, a batch is one or more SQL statements executed
in order in an implicit transaction. The transaction is controlled by the libSQL
backend. If all of the statements are successful, the transaction is committed.
If any of the statements fail, the entire transaction is rolled back and no
changes are made.

### Interactive transactions​

Interactive transactions allow you to execute a series of read and write
statements in the context of a[ SQLite transaction ](https://www.sqlite.org/lang_transaction.html). Reads and writes are all
consistent within the scope of that transaction, unaffected by other client
activity. The transaction API requires you to choose when to commit or roll back
the transaction.

danger

Interactive transactions effectively lock the entire database for writing when a
write is first performed, and until the transaction is committed or rolled back.
libSQL aborts transactions after a 5 second timeout. Transactions may negatively
impact overall database performance when used on high latency connections or
with busy databases.

### Embedded replicas​

In order to use an embedded replica for hybrid access, the SDK must be
initialized with three values:

- The URL of the remote database hosted by libSQL server
- An authentication token for that database (required only by Turso)
- The path to the local database file to be kept in sync with the remote
database. The local database file is fully compatible with SQLite.


caution

You should allow the libSQL SDK to create the local database files and perform
write operations on them. Writes from other sources are not supported, and the
data might be lost upon the next sync with the remote database.

When you provide a path to the local database file, two other files appear
alongside it with the same name as the database file you provide with "-shm" and
"-wal" suffixes. These files should be considered part of the local database. If
you need to relocate the embedded replica, these files should be moved along
with the main database file.

- [ Access types ](https://docs.turso.tech//libsql/client-access#interactive-transactions/#access-types)
    - [ Local access ](https://docs.turso.tech//libsql/client-access#interactive-transactions/#local-access)

- [ Remote access ](https://docs.turso.tech//libsql/client-access#interactive-transactions/#remote-access)

- [ Hybrid access (embedded replica) ](https://docs.turso.tech//libsql/client-access#interactive-transactions/#hybrid-access)
- [ Client SDK capabilities ](https://docs.turso.tech//libsql/client-access#interactive-transactions/#client-sdk-capabilities)
    - [ Batches ](https://docs.turso.tech//libsql/client-access#interactive-transactions/#batches)

- [ Interactive transactions ](https://docs.turso.tech//libsql/client-access#interactive-transactions/#interactive-transactions)

- [ Embedded replicas ](https://docs.turso.tech//libsql/client-access#interactive-transactions/#embedded-replicas)


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