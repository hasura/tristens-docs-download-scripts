# SQLite extensions

caution

SQLite extensions are an experimental feature in Turso. Your observations and
feedback are welcome on our Discord.

SQLite extensions add optional features, supported by the SQLite community, that
can be used in queries handled by the SQLite query engine. The instances of[ libSQL server ](https://github.com/libsql/libsql#readme)managed by Turso can be configured to enable a select few
extensions.

## Enabling extensions​

Extensions are enabled using the `--enable-extensions` flag when creating a
database with the[ Turso CLI ](https://docs.turso.tech/reference/turso-cli). For example:

`$ turso db create my-db --enable-extensions`

Extensions can't be enabled for existing databases.

## List of extensions​

The following extensions are loaded into libSQL server for databases that have
extensions enabled.

| Extension | Purpose |
|---|---|
| [ SQLean Crypto ](https://github.com/nalgeon/sqlean/blob/main/docs/crypto.md) | Hashing, message digest, encoding, and decoding |
| [ SQLean Fuzzy ](https://github.com/nalgeon/sqlean/blob/main/docs/fuzzy.md) | Fuzzy string matching and phonetics |
| [ SQLean Math ](https://github.com/nalgeon/sqlean/blob/main/docs/math.md) | Advanced mathematical calculations |
| [ SQLean Regexp ](https://github.com/nalgeon/sqlean/blob/main/docs/regexp.md) | Regular expressions |
| [ SQLean Stats ](https://github.com/nalgeon/sqlean/blob/main/docs/stats.md) | Common statistical functions |
| [ SQLean Text ](https://github.com/nalgeon/sqlean/blob/main/docs/text.md) | String manipulation (reverse, split) |
| [ SQLean Unicode ](https://github.com/nalgeon/sqlean/blob/main/docs/unicode.md) | Case-insensitive string comparison for Unicode strings |
| [ SQLean UUID ](https://github.com/nalgeon/sqlean/blob/main/docs/uuid.md) | Limited support for RFC 4122 compliant UUIDs |
| [ Vector Similarity Search ](https://github.com/asg017/sqlite-vss) | Vector search capabilities based on[ Faiss ](https://faiss.ai/). |


note

SQLite maintains three official extensions that are enabled by default in Turso:[ JSON ](https://www.sqlite.org/json1.html),[ FTS5 ](https://www.sqlite.org/fts5.html)(full text search), and[ R*Tree ](https://www.sqlite.org/rtree.html)(range queries).

- [ Enabling extensions ](https://docs.turso.tech//reference/extensions/#enabling-extensions)
- [ List of extensions ](https://docs.turso.tech//reference/extensions/#list-of-extensions)


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