# Integration with Postgres

If you have an existing Postgres database and want to replicate some portion of
it to Turso, you can do that using the[ pg_turso ](https://github.com/turso-extended/pg_turso/)Postgres plugin. pg_turso
allows you to configure specific tables and materialized views for replication.

caution

pg_turso is currently experimental and not yet ready for production use.

To work with pg_turso, you must:

- Build the plugin from source.
- Install the plugin using `CREATE EXTENSION`
- Choose tables and materialized views to replicate
- Choose a frequency at which updates are pushed to Turso
- Invoke a provided function to begin scheduling


Data replicated to Turso must be considered read-only for database clients.
Writes to Turso replicas are not reflected back into Postgres.

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