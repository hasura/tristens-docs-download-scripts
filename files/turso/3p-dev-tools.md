# Third party developer tools

There are a number of tools supported by third party organizations that work
with Turso and libSQL.

- [ Migration tools ](https://docs.turso.tech//3p-dev-tools/#migration-tools)
- [ ORMs ](https://docs.turso.tech//3p-dev-tools/#orms)
- [ Query builders ](https://docs.turso.tech//3p-dev-tools/#query-builders)
- [ Compatibility libraries ](https://docs.turso.tech//3p-dev-tools/#compatibility-libraries)


If you're interested in adding libSQL support to your own tool, please reach out
to us to coordinate.

## Migration tools​

### Atlas​

[ Atlas ](https://atlasgo.io)is an open-source tool for managing and migrating database schemas using
modern DevOps principles. In order to work with a Turso database, you can simply
provide it with a `libsql+wss://` URL for your logical database wherever URLs
are accepted by the Atlas CLI. You must also provide an[ auth token ](https://docs.turso.tech/reference/turso-cli#authentication-tokens-for-client-access)in the URL.
For example:

`atlas schema inspect -u  "libsql+wss://<db-host>?authToken=<token>"`

[ Go to Atlas documentation for Turso integration. ](https://atlasgo.io/guides/sqlite/turso)

## ORMs​

### Drizzle ORM​

[ Drizzle ORM ](https://github.com/drizzle-team/drizzle-orm#readme)is a TypeScript ORM for SQL databases designed with maximum type
safety in mind. Drizzle supports libSQL, with an complete example that shows how
to build a Hono server that:

- Declares a Drizzle schema for tables
- Uses a Zod validator with the schema to handle incoming JSON
- Uses the schema make queries with a type-safe, fluent API
- Switch seamlessly between SQLite local file and Turso remote database


[ Go to the example for libSQL on the Drizzle GitHub. ](https://github.com/drizzle-team/drizzle-orm/tree/main/examples/libsql#readme)

### SQLAlchemy​

[ SQLAlchemy ](https://www.sqlalchemy.org/)is the Python SQL toolkit and Object Relational Mapper that gives
application developers the full power and flexibility of SQL. A dialect is
provided for libSQL, which works with Turso. The only requirement for Turso is
the construction of a URL in a special format that instructs SQLAlchemy to use
this dialect, which is discussed in the README of the dialect repo.

[ Go to the SQLAlchemy libSQL dialect repo on GitHub. ](https://github.com/libsql/sqlalchemy-libsql#readme)

## Query builders​

### Kysely​

[ Kysely ](https://github.com/kysely-org/kysely#readme)is a type-safe and autocompletion-friendly TypeScript SQL query builder.
libSQL provides a plugin (dialect) that allows you to take full advantage of the
features of Kysely.

[ Go to the Kysely libSQL dialect repo on GitHub. ](https://github.com/libsql/kysely-libsql#readme)

### Knex.js​

[ Knex.js ](https://knexjs.org/)is a "batteries included" SQL query builder for a variety of
databases, designed to be flexible, portable, and fun to use. It supports use of
libSQL server instances in the same way that it supports local SQLite files by
swapping the sqlite3 module with[ libsql-node-sqlite3 ](https://docs.turso.tech//3p-dev-tools/#libsql-node-sqlite3).

[ Go to example code in the libsql-node-sqlite3 README. ](https://github.com/libsql/libsql-node-sqlite3#usage-with-knex)

## Compatibility libraries​

### libsql-node-sqlite3 (node-sqlite3 replacement)​

The[ sqlite3 node module ](https://github.com/TryGhost/node-sqlite3#readme)is commonly used to access SQLite database files.
libSQL provides a drop-in replacement module for this that exposes the same API,
accessing a libSQL server instance instead. This replacement module can also be
used with[ Knex.js ](https://docs.turso.tech//3p-dev-tools/#knex-js).

[ Go to the libsql-node-sqlite3 repo on GitHub. ](https://github.com/libsql/libsql-node-sqlite3#readme)

- [ Migration tools ](https://docs.turso.tech//3p-dev-tools/#migration-tools)
    - [ Atlas ](https://docs.turso.tech//3p-dev-tools/#atlas)
- [ ORMs ](https://docs.turso.tech//3p-dev-tools/#orms)
    - [ Drizzle ORM ](https://docs.turso.tech//3p-dev-tools/#drizzle-orm)

- [ SQLAlchemy ](https://docs.turso.tech//3p-dev-tools/#sqlalchemy)
- [ Query builders ](https://docs.turso.tech//3p-dev-tools/#query-builders)
    - [ Kysely ](https://docs.turso.tech//3p-dev-tools/#kysely)

- [ Knex.js ](https://docs.turso.tech//3p-dev-tools/#knex-js)
- [ Compatibility libraries ](https://docs.turso.tech//3p-dev-tools/#compatibility-libraries)
    - [ libsql-node-sqlite3 (node-sqlite3 replacement) ](https://docs.turso.tech//3p-dev-tools/#libsql-node-sqlite3)


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