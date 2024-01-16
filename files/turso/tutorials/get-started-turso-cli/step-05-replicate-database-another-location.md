# Step 5: Replicate the database to another location

note

In step 3, you created a database in a[ placement group ](https://docs.turso.tech/concepts#placement-group)named "default" with a
primary[ location ](https://docs.turso.tech/concepts#location)near you. The placement group defines the set of locations
where the database is replicated. When you create additional databases in this
group it will also exist in the same set of locations, all hosted by the same
hardware at those locations.

## Replicate a database by adding a location to its placement group​

You can add and remove replica locations easily with the Turso CLI. Adding a
location to a placement group automatically replicates all of the databases in
that group to the new location. Adding replica locations reduces latency for
database queries that originate in places near those locations. This is why
Turso is referred to as an "edge" database - you can better serve users who are
geographically distributed by placing copies of data closer to them.

Add a new location in Tokyo, Japan (nrt) to your "default" group with the
following command:

`turso group locations  add  default nrt`

## Understand billing for placement groups​

Adding a location to a placement group incurs the cost of one location for the
purpose of billing. On the free starter plan, you have an allowance of three
locations to use for creating multiple placement groups or adding replica
locations to a group. Right now, your "default" placement group costs two
locations: one for the primary location near you, and one for the replica
location in Tokyo.

If you add a new logical database to this placement group, it will **not** incur
the cost of another location for billing. All of the databases in a placement
group are hosted together on the same hardware. On the free starter plan, you have an allowance of 500 logical databases.

## Viewing replica information​

You can see the list of locations for the "default" placement group:

`turso group locations list default`

You can also see the list of locations for a specific logical database using the `show` command you used earlier:

`turso db show my-db`

```
Name:           my-db
URL:            libsql://my-db-[my-github-name].turso.io
ID:             [UUID]
Group:          default
Version:        [version]
Locations:      [location], nrt
Size:           8.2 kB
Database Instances:
NAME     TYPE        LOCATION
[loc]    primary     [loc]
nrt      replica     nrt
```

- [ Replicate a database by adding a location to its placement group ](https://docs.turso.tech//tutorials/get-started-turso-cli/step-05-replicate-database-another-location/#replicate-a-database-by-adding-a-location-to-its-placement-group)
- [ Understand billing for placement groups ](https://docs.turso.tech//tutorials/get-started-turso-cli/step-05-replicate-database-another-location/#understand-billing-for-placement-groups)
- [ Viewing replica information ](https://docs.turso.tech//tutorials/get-started-turso-cli/step-05-replicate-database-another-location/#viewing-replica-information)


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