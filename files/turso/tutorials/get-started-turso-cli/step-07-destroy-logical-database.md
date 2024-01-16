# Step 7: Destroy the logical database

The CLI can destroy the entire[ logical database ](https://docs.turso.tech/concepts#logical-database), including the[ primary ](https://docs.turso.tech/concepts#primary)and
all of its[ replicas ](https://docs.turso.tech/concepts#replica)with the following command:

`turso db destroy my-db`

This is a very dangerous command since it deletes all data in the database and
cannot be reversed. The CLI will interactively prompt you to ask if it’s OK to
do so:

```
Database my-db, and all its data will be destroyed.
Are you sure you want to do this? [y/n]:
```

Type “y” + return to continue destroying the database.

Notes about destroying logical databases:

- There is no recovery from a destroyed logical database.
- You can bypass the interactive prompt for use with automated scripts using the `--yes` flag.


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