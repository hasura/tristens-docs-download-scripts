# Turso CLI in review

Congratulations, you’ve finished the Turso CLI tutorial! You should now be able
to effectively use most of the functionality provided by the CLI.

## Commands you learned​

### turso auth signup​

`turso auth signup`

This starts the signup process that allows the CLI to work with Turso databases.

### turso auth login​

`turso auth login`

This starts the authentication process, similar to `turso auth signup` . Since
the authentication token you receive expires after 7 days, you must run this
periodically to continue working with your databases.

### turso db locations​

`turso db locations`

This lists all supported[ locations ](https://docs.turso.tech/concepts#location), highlighting your current default location.

### turso db create​

`turso db create`

This creates a new[ logical database ](https://docs.turso.tech/concepts#logical-database)in a placement group. A default placement
group is created if one doesn't yet exist.

### turso db show​

`turso db show`

This shows details for a specific logical database, including its URL and all of
the instances in all locations.

### turso db list​

`turso db list`

This lists all of the logical databases associated with the account that’s
currently logged in.

### turso db shell​

`turso db shell`

This starts an interactive shell to issue SQL statements against your database.
By default it uses the primary, and you can also point it to a replica using its
URL.

### turso group locations add​

`turso group locations add`

This adds a new location to a placement group, replicating all of the databases
in that group to that location.

### turso db inspect​

`turso db inspect`

This shows current database usage for billing purposes.

### turso db destroy​

`turso db destroy`

This destroys a specific replica by name, or all replicas in a named location,
or the entire database.

### turso auth logout​

`turso auth logout`

This removes the authentication token previously provided by `turso auth login` ,
requiring you to log in again to continue working with your databases.

### Built-in help​

The CLI has help available.  The following command summarizes the top-level
commands available:

`turso  help`

For each specific command, you can add the `--help` flag to get details on all
the sub-commands and flags. For example:

```
turso db --help
turso db create --help
```

### Reference documentation​

To learn about additional the functionality of the CLI, consult its[ reference
documentation ](https://docs.turso.tech/reference/turso-cli).

- [ Commands you learned ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#commands-you-learned)
    - [ turso auth signup ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#turso-auth-signup)

- [ turso auth login ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#turso-auth-login)

- [ turso db locations ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#turso-db-locations)

- [ turso db create ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#turso-db-create)

- [ turso db show ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#turso-db-show)

- [ turso db list ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#turso-db-list)

- [ turso db shell ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#turso-db-shell)

- [ turso group locations add ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#turso-group-locations-add)

- [ turso db inspect ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#turso-db-inspect)

- [ turso db destroy ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#turso-db-destroy)

- [ turso auth logout ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#turso-auth-logout)

- [ Built-in help ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#built-in-help)

- [ Reference documentation ](https://docs.turso.tech//tutorials/get-started-turso-cli/turso-cli-review/#reference-documentation)


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