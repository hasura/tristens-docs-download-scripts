# Data consistency

Turso is built on top of[ libSQL ](https://github.com/libsql/libsql#readme), which is a fork of[ SQLite ](https://sqlite.org). SQLite, as an
embedded database, offers a strictly serializable consistency model. However,
libSQL, as a network-accessible and replicated database provided by[ libSQL
server ](https://github.com/libsql/libsql#readme), can not offer such a strong guarantee.

## Connections​

There are two types of connections involved with libSQL server:

- The HTTP or websocket connection a client makes to a server instance.
- The underlying[ SQLite database connection ](https://www.sqlite.org/c3ref/open.html)established within the server.


For the purpose of this documentation, a SQLite database connection is referred
to as a *process* , which issues an ordered sequence of queries with results.
Each database operation exposed by libSQL server (execute a statement,[ batch ](https://docs.turso.tech/libsql/client-access#batches),
or[ interactive transaction ](https://docs.turso.tech/libsql/client-access#interactive-transactions)) is executed within a dedicated process, isolated
from all other processes running concurrently.

## Read and write behavior​

### On the primary instance​

All operations by processes connected to the[ primary ](https://docs.turso.tech/concepts#primary)are linearizable, forming
a ordered sequence of completed operations (a history).

#### All writes are serialized​

All write operations are fully serialized on the primary. When a transaction
performs a write operation, all other write operations must wait for the
transaction to complete in order to preserve this serialization.

danger

Take care when using an[ interactive transaction ](https://docs.turso.tech/libsql/client-access#interactive-transactions)that perform a write
operation. Since writes are fully serialized on the primary, a long-running or
abandoned transaction will block all writes from other processes until libSQL
aborts the transaction after a 5 second timeout.

### On the replicas​

#### Writes are forwarded to the primary​

All writes from a process connected to a[ replica ](https://docs.turso.tech/concepts#replica)are automatically forwarded
to the primary and applied there. Changes to the primary are eventually pulled
from each replica and made available locally. A process is guaranteed to see all
writes that happened on the primary up until (at least) the last write performed
by the process. There are no hard guarantees on how long it will take for a
replica to observe a change from the primary, considering network latency and
availability, and total load on the primary.

#### Reads are local and not globally ordered​

All reads by a process come from the locally replicated database. Peer replicas
are not necessarily all in sync with each other. Reads from different replicas
can yield different data until each replica receives the latest changes from the
primary. Furthermore, concurrent reads on a replica may observe snapshots of
data from different points in time.

### Monotonic reads​

All database instances offer monotonic reads. A read operation will never appear
to yield data older than a prior read on the same instance.

## Transactional consistency​

A transaction ([ batch ](https://docs.turso.tech/libsql/client-access#batches)or[ interactive transaction ](https://docs.turso.tech/libsql/client-access#interactive-transactions)) is equivalent to a[ SQLite
transaction ](https://www.sqlite.org/lang_transaction.html)and observes its semantics.

During a transaction:

- All reads operations are guaranteed snapshot isolation. A transactional read
will never yield changes from other processes.
- All write operations performed by a process are immediately visible to itself
in a subsequent read operation. The writes are isolated from all other ongoing
transactions. As such, libSQL transactions are considered serializable.


All reads operations are guaranteed snapshot isolation. A transactional read
will never yield changes from other processes.

All write operations performed by a process are immediately visible to itself
in a subsequent read operation. The writes are isolated from all other ongoing
transactions. As such, libSQL transactions are considered serializable.

- [ Connections ](https://docs.turso.tech//reference/data-consistency/#connections)
- [ Read and write behavior ](https://docs.turso.tech//reference/data-consistency/#read-and-write-behavior)
    - [ On the primary instance ](https://docs.turso.tech//reference/data-consistency/#on-the-primary-instance)

- [ On the replicas ](https://docs.turso.tech//reference/data-consistency/#on-the-replicas)

- [ Monotonic reads ](https://docs.turso.tech//reference/data-consistency/#monotonic-reads)
- [ Transactional consistency ](https://docs.turso.tech//reference/data-consistency/#transactional-consistency)


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