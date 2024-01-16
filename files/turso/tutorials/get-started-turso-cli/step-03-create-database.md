# Step 3: Create a logical database

When creating a logical database, Turso requires a[ location ](https://docs.turso.tech/concepts#location)for the[ primary ](https://docs.turso.tech/concepts#primary)instance. By default, it will select a default location based on your physical
location as suggested by your IP address.  To see all locations supported by
Turso, run the following command:

`turso db locations`

Your default location appears highlighted in the list.

To create a database using the default location with the name `my-db` :

`turso db create my-db`

It takes a few moments to create the database, then generates output similar to
the following (with replacements for the parts that may vary):

```
Created group default at [your location] in 9 seconds.
Created database my-db at group default in 6 seconds.
Start an interactive SQL shell with:
   turso db shell my-db
To see information about the database, including a connection URL, run:
   turso db show my-db
To get an authentication token for the database, run:
   turso db tokens create my-db
```

note

You can override the default location using the `--location` flag.

note

You'll see that Turso created both a "group" and a "database" for you. All
databases exist within a container called a "placement group". It's not
important to understand right now, but we'll come back to that later.

As suggested by the output, you can view information about the database using:

`turso db show my-db`

The output looks similar to the following:

```
Name:           my-db
URL:            libsql://my-db-[my-github-name].turso.io
ID:             [UUID]
Group:          default
Version:        [version]
Locations:      [location]
Size:           8.2 kB
Database Instances:
NAME     TYPE        LOCATION
[loc]    primary     [loc]
```

Note the following in the above output:

- [ Database URLs ](https://docs.turso.tech/reference/libsql-urls)use a custom `libsql` scheme, and are composed using a
combination of the name of the database and your GitHub ID.
- The URL is the[ logical database URL ](https://docs.turso.tech/reference/libsql-urls#logical-database-url)that you provide to[ libSQL client
libraries ](https://docs.turso.tech/libsql/client-access)to query the database. This URL automatically forwards the client
to the[ instance ](https://docs.turso.tech/concepts#instance)with the lowest latency.
- The[ primary ](https://docs.turso.tech/concepts#primary)instance has a random name that was assigned by the CLI.


To see a list of all logical databases associated with the account that's
currently logged in:

`turso db list`

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