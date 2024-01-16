# Local development

A Turso database[ instance ](https://docs.turso.tech/concepts#instance)runs an open-source server called[ libSQL server ](https://github.com/libsql/libsql#readme).
This server:

- Handles incoming client connections over HTTP and websockets
- Offers a JSON-based wire protocol for clients
- Connects the client to the embedded[ libSQL ](https://github.com/libsql/libsql)database engine (a fork of
SQLite) to execute queries
- Manages the underlying database data in a[ SQLite database
file ](https://docs.turso.tech//reference/local-development/#about-sqlite-database-files)


Turso adds additional features and configurations on top of libSQL server:

- DNS and secure sockets with SSL
- Client authentication with database tokens provided by the[ Turso CLI ](https://docs.turso.tech/reference/turso-cli)
- World-wide instance location support
- Serverless instance scaling
- Automatic replication between instances


For daily development, you might be satisfied with the core features provided by
libSQL server, without the additional features offered by Turso. You might also
want to avoid any costs incurred by working with server instances managed by
Turso. For these cases, you have three supported options for building and
testing client code written with the[ libSQL client SDKs ](https://docs.turso.tech/libsql/client-access):

- [ Read and write local SQLite data files directly ](https://docs.turso.tech//reference/local-development/#use-local-sqlite-database-files)
- [ Run libSQL server locally using the Turso CLI ](https://docs.turso.tech//reference/local-development/#run-libsql-server-using-the-turso-cli)
- [ Build and run an instance of libSQL server locally ](https://docs.turso.tech//reference/local-development/#build-and-run-libsql-server-separately)


## Use local SQLite database files​

If you are building for an environment that offers read-write access to a local
filesystem, using a SQLite database file is the easiest option. Some development
environments for serverless backends don't offer access to a filesystem, such as
Wrangler for Cloudflare Workers. Be sure to check the product documentation to
find out if you have local filesystem access for your environment.

The libSQL client libraries support the use of local[ SQLite database
files ](https://docs.turso.tech//reference/local-development/#about-sqlite-database-files)to service queries without any intermediate
service. To configure a libSQL client to use a local file, you must provide a `file:` URL to the SDK when creating a client instance. This URL replaces the[ libsql URL ](https://docs.turso.tech/reference/libsql-urls)you get from the Turso CLI for the purpose of local development.

For example, using the[ Python SDK ](https://docs.turso.tech/libsql/client-access/python-sdk):

```
import  libsql_client
client  =  libsql_client . create_client_sync (
    url = "file:///path/to/file"
)
```

And using the[ JavaScript SDK ](https://docs.turso.tech/libsql/client-access/javascript-typescript-sdk):

```
import   {  createClient  }   from   "@libsql/client" ;
const  client  =   createClient ( {
     url :   "file:///path/to/file"
} ) ;
```

info

The JavaScript SDK only supports file URLs when using the default `@libsql/client` import (not the alternate `web` or `http` imports designed for
some serverless backend environments). This works in Node.js-compatible
environments that have access to the local filesystem.

You can also use relative file paths in the form `file:relative/path/to/file` .

Note that no `authToken` is required when connecting to a file URL. You may
provide one, but it will have no effect on the client.

## Run libSQL server using the Turso CLI​

The Turso CLI can invoke libSQL server on your machine with the following
command:

`$ turso dev`

It provides a URL that you can use to connect the Turso CLI shell and client
code. Learn more about `turso dev` in the[ Turso CLI documentation ](https://docs.turso.tech/reference/turso-cli#use-libsql-server-locally).

## Build and run libSQL server separately​

You can build and run an instance of libSQL server on your local machine. There
are multiple ways to do this, and they are covered in the[ documentation to
build and run libSQL server ](https://github.com/libsql/sqld/blob/main/docs/BUILD-RUN.md).

## Using a local libSQL server instead of Turso​

Once you have a local libSQL server running, you can use an `http` or `ws` URL
in place of your libsql URL to connect to it. For example, libSQL server runs by
default on port 8080, so the URL for that is `ws://127.0.0.1:8080` . This URL
replaces the[ libsql URL ](https://docs.turso.tech/reference/libsql-urls)you get from the Turso CLI for the purpose of local
development.

libSQL server uses a dedicated directory to manage a[ SQLite database
file ](https://docs.turso.tech//reference/local-development/#about-sqlite-database-files)along with other metadata. By default, the
file lives in the relative path `data.sqld/data` where the server was started.

## About SQLite database files​

SQLite has a documented file format for its database files. It's not necessary
to understand this format, but you can use any tool that understands these files
in order to work with them outside of your code. In particular, SQLite provides
a[ command line shell ](https://www.sqlite.org/cli.html)for this purpose. This shell can make it easier for you
to create and populate a database for your local development without having to
use a client SDK.

SQLite does not have very flexible[ support for multiple processes ](https://sqlite.org/faq.html#q5). If you want
to write to a database file manged by libSQL server or some other running
process, you should first stop that process in order to avoid `SQLITE_BUSY` errors.

- [ Use local SQLite database files ](https://docs.turso.tech//reference/local-development/#use-local-sqlite-database-files)
- [ Run libSQL server using the Turso CLI ](https://docs.turso.tech//reference/local-development/#run-libsql-server-using-the-turso-cli)
- [ Build and run libSQL server separately ](https://docs.turso.tech//reference/local-development/#build-and-run-libsql-server-separately)
- [ Using a local libSQL server instead of Turso ](https://docs.turso.tech//reference/local-development/#using-a-local-libsql-server-instead-of-turso)
- [ About SQLite database files ](https://docs.turso.tech//reference/local-development/#about-sqlite-database-files)


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