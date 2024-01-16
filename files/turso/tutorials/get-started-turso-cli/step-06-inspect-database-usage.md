# Step 6: Inspect database usage

New Turso accounts, are automatically subscribed to the free Starter plan, which
has limits to its monthly usage. Run the following command to see your account's
current usage among all of its databases as it relates to your plan limits:

`turso plan show`

You can see per-database usage with the following command:

`turso db inspect my-db`

The output looks similar to the following:

```
Total space used: 40 KiB
Number of rows read: 13
Number of rows written: 1
```

Add the `--verbose` flag to the command to see a detailed breakdown of usage per
table, index, and[ location ](https://docs.turso.tech/concepts#location).

note

Internally, Turso uses the[ SQLite dbstat virtual table ](https://www.sqlite.org/dbstat.html)to calculate usage
among all user-defined tables and indexes.

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