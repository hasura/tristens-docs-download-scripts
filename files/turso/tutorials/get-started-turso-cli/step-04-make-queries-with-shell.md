# Step 4: Make queries with the shell

The output of `turso db create` in the last step shows a command to run to start
an interactive shell:

`turso db shell my-db`

```
Connected to my-db at libsql://my-db-[my-github-name].turso.io
Welcome to Turso SQL shell!
Type ".quit" to exit the shell and ".help" to list all available commands.
→
```

See that the shell is working with a simple "hello world" SQL statement:

```
→  select "hello world" as message;
MESSAGE
hello world
```

note

The shell requires that SQL commands terminate with a semicolon. If you enter a
string that does not, the shell will continue accepting lines of SQL input until
a terminating semicolon is provided.

note

Turso is backed by libSQL, which is a fork of SQLite, so you must provide SQL
commands in the SQLite dialect.

Create and populate a table, and view its contents by copying the following SQL
statements into the shell:

```
→  create table users (id text, email text);
→  insert into users values ("001", "test@foo.com");
→  select * from users;
ID   EMAIL
001  test@foo.com
```

Run `.help` to see a list of shell commands. You can see the commands `.tables` and `.schema` and use them to inspect the structure of the database:

```
→  .tables
users
→  .schema
CREATE TABLE users (id text, email text)
```

 `.quit` or CTRL-d ends the shell.

`→  .quit`

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