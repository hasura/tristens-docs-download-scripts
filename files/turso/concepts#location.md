# Concepts

In order to better understand how Turso works, please read through the following
concepts that are used throughout this documentation.

## Location​

Turso databases are deployed using Fly.io, which allows Turso to host database
instances in[ many locations around the world ](https://fly.io/docs/reference/regions/), each identified with a three
letter code. When creating a logical database in a placement group with replica
locations, you should consider which locations best support the code running any
queries. In general, the physical distance between the code and the database
determines the latency, so it's recommended to benchmark your location options
for better performance.

By default, when the[ Turso CLI ](https://docs.turso.tech/reference/turso-cli)needs a primary location for a new placement
group, it will automatically choose a location based on the physical location of
the machine where you run the CLI. The default can be overridden on the command
line.

## Placement group​

Turso requires that all logical databases belong to a "placement group". These
groups define how the databases in the group are deployed and replicated
together in the same set of locations while also sharing the same managed
hardware. In the Turso CLI, a placement group is abbreviated as "[ group ](https://docs.turso.tech/reference/turso-cli#manage-placement-groups-and-logical-databases)". You
might also hear this feature referred to as "multitenancy", where the tenants
are databases you create that must share the same replication behavior and
managed servers.

Placement groups are configured with a single primary location and zero or more
replica locations. Each logical database that you create within the placement
group uses the same primary and replica locations - they are all "placed"
together, each using the same replication behavior on the same hardware.
However, each logical database within a placement group remains fully
independent and isolated in every other way.

Once a primary location is assigned to a placement group, it can't be moved to
another location. However, replica locations can be added and removed as needed.

## Logical database​

A logical database is a collection of libSQL databases, each with a schema and
data that exists in one primary location and zero or more replica locations for
the placement group in which it was created. The schema and data are
automatically replicated from the primary to all replicas in the group.

A logical database has a unique[ libSQL URL ](https://docs.turso.tech/reference/libsql-urls)that, when queried using the[ libSQL client SDKs ](https://docs.turso.tech/libsql/client-access), routes the client to the database instance at the location
with the lowest latency, therefore minimizing the total round trip time for read
operations.

## Instance​

A database instance is one component of a logical database in specific location.
An instance is serviced by a managed installation of[ libSQL server ](https://github.com/libsql/libsql#readme)running on
a single machine. Database instances of multiple logical databases in the same
placement group are handled by the same libSQL server process in the same
hardware.

There are two types of instances:[ primary ](https://docs.turso.tech//concepts#location/#primary)and[ replica ](https://docs.turso.tech//concepts#location/#replica).

### Primary​

The primary instance of a logical database is the main source of data for the
database. All changes to the logical database are handled by the primary, and
those changes are synchronized to all replica instances.

### Replica​

A replica instance of a logical database contains a copy of all data from the
primary, and is kept in sync with it as changes are made over time. Client
applications can connect directly to a replica for read and write operations,
but any writes are automatically forwarded to the primary. As such, read
operations have minimized latency, but write operations must make another hop to
the primary. Changes on the primary are then pushed to all replicas. The
replicas provide snapshot isolation for read transactions.

- [ Location ](https://docs.turso.tech//concepts#location/#location)
- [ Placement group ](https://docs.turso.tech//concepts#location/#placement-group)
- [ Logical database ](https://docs.turso.tech//concepts#location/#logical-database)
- [ Instance ](https://docs.turso.tech//concepts#location/#instance)
    - [ Primary ](https://docs.turso.tech//concepts#location/#primary)

- [ Replica ](https://docs.turso.tech//concepts#location/#replica)


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