# Step 2: Setting up Turso

Proceeding to setting up a database for the app, run the following command to
create a new Turso database.

`turso db create the-mug-store`

Next, get and set up the database credentials so that the data within Turso can
be consumed by our app.

For the database url run the following command.

`turso db show the-mug-store --url`

Inside the Cloudflare wrangler configuration file `wrangler.toml` add a new `[vars]` section and list the database url as follows.

```
[ vars ]
TURSO_DB_URL   =   "YOUR-DATABASE-URL"
```

In this section of the Cloudflare workers configuration file, we list the
environment variables that we don’t consider as sensitive within our app.

For the database auth token, run the following command.

`turso db tokens create the-mug-store`

Since the auth token is a sensitive environment variable “secret” we store it by
using the wrangler CLI, or directly on the project’s dashboard on Cloudflare.
But, to do so we first need to grant the wrangler app permissions to use our
Cloudflare account, we do that by running the `wrangler login` command.

The following tab will be opened on our browser after running the last command.

Image: [ Wrangler access request ](https://docs.turso.tech/assets/images/04-wrangler-access-5daeae3bc9a59dbf20c801512f54a57b.png)

Image: [ Wrangler access request ](https://docs.turso.tech/assets/images/04-wrangler-access-5daeae3bc9a59dbf20c801512f54a57b.png)

Click on “Allow” on the resulting permissions page to proceed.

Then, on the terminal run `wrangler secret put TURSO_DB_AUTH_TOKEN` , and paste
the database auth token we obtained above when prompted.

For local development, create a `.dev.vars` file at the project’s root directory
and add the `TURSO_DB_AUTH_TOKEN` key assigning it the obtained token.

`TURSO_DB_AUTH_TOKEN = "YOUR-DATABASE-TOKEN"`

Next up, we'll be setting up Drizzle for simplified database queries within the
app.

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