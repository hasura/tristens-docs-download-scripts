# Hasura GraphQL Engine One-click App on DigitalOcean Marketplace

## Introduction​

The Hasura GraphQL Engine is available as a One-click app on the DigitalOcean Marketplace. It is packed with a[ Postgres ](https://www.postgresql.org/)database and[ Caddy ](https://caddyserver.com/)webserver for easy and automatic
HTTPS using[ Let's Encrypt ](https://letsencrypt.org/).

## Deploying Hasura on DigitalOcean​

### Step 1: Create a Hasura One-click Droplet​

Click the button below to create a new Hasura GraphQL Engine Droplet through the DigitalOcean Marketplace. For first
time users, the link also contains a referral code which gives you $100 over days. A $5 droplet is good enough to support
most workloads. ( `Ctrl+Click` to open in a new tab)

[  ](https://marketplace.digitalocean.com/apps/hasura-graphql?action=deploy&refcode=c4d9092d2c48&utm_source=hasura&utm_campaign=docs)

Image: [ do_create_droplet_button ](https://graphql-engine-cdn.hasura.io/img/create_hasura_droplet.png)

### Step 2: Open the Console​

Once the Hasura GraphQL Engine Droplet is ready, you can visit the Droplet IP to open the Hasura Console, where you can
create tables, explore GraphQL APIs etc. Note that it might take 1 or 2 minutes for everything to start running.

The `Droplet IP` is highlighted in the image below:

Image: [ Dashboard for DigitalOcean droplet ](https://hasura.io/docs/assets/images/dashboard-digital-ocean-ef702fd0b9bf3c8036c81d5ae10ab27d.png)

The Hasura Console will be at:

`http:// < your_droplet_ip > /console`

The GraphQL endpoint will be:

`http:// < your_droplet_ip > /v1/graphql`

A Postgres database is also provisioned on the Droplet. Using the Console, you can create a table on this Postgres
instance and make your first GraphQL query.

Image: [ Hasura Console ](https://hasura.io/docs/assets/images/digital-ocean-hasura-console-49555214aff605c7cf71bcd0c668683b.png)

### Step 3: Create a table​

Navigate to `Data -> Add table` on the Console and create a table called `profile` with the following columns:

 `profile` 

| column name | type |
|---|---|
|  `id`  | Integer (auto-increment) |
|  `name`  | Text |


Choose `id` as the Primary key and click the `Add Table` button.

Image: [ Create a table ](https://hasura.io/docs/assets/images/digital-ocean-create-table-d993348afbf03199cb434efa464dbd7b.png)

### Step 4: Insert sample data​

Once the table is created, go to the `Insert Row` tab and insert some sample rows:

```
Thor
Iron Man
Hulk
Captain America
Black Widow
```

Image: [ Hasura Console - insert data ](https://hasura.io/docs/assets/images/digital-ocean-hasura-insert-data-4ba3c0288e1377ecd4e17dc2a1868973.png)

### Step 5: Try out GraphQL​

Switch to the `API` tab on top and execute the following GraphQL query:

```
query   {
   profile   {
     id
     name
   }
}
```

Image: [ Hasura Console - GraphiQL ](https://hasura.io/docs/assets/images/hasura-graphql-query-b4776e7197fb9550daaeda1290944517.png)

## Securing the GraphQL endpoint​

By default Hasura is exposed without any admin secret. Anyone can read and write to your database using GraphQL. When
deploying to production, you should secure the endpoint by adding an admin secret key and then setting up permission
rules on tables.

To add an admin secret key, follow the steps described below:

### Step 1: Connect to the Droplet via SSH​

`ssh  root@ < your_droplet_ip >`

### Step 2: Go to the /etc/hasura directory​

`/etc/hasura`

`cd  /etc/hasura`

### Step 3: Set an admin secret​

Edit `docker-compose.yaml` and un-comment the line that mentions admin secret key. Also change it to some unique secret:

```
vim  docker-compose.yaml
.. .
# un-comment next line to add an admin secret key
HASURA_GRAPHQL_ADMIN_SECRET:  < myadminsecretkey >
.. .
# type ESC followed by :wq to save and quit
```

### Step 4: Update the container​

`docker  compose up -d`

That's it. Visit the Console at `http://<your_droplet_ip>/console` and it should prompt for the admin secret key.
Further API requests can be made by adding the following header:

`X-Hasura-Admin-Secret:  < myadminsecretkey >`

## Adding a domain & enabling HTTPS​

If you own a domain, you can enable HTTPS on this Droplet by mapping the domain to the Droplet's IP. The Hasura GraphQL
Droplet is configured with Caddy which is an HTTP/2 web server with automatic HTTPS using Let's Encrypt.

### Step 1: Add a record mapping​

Go to your domain's DNS dashboard and add an A record mapping the domain to the Droplet IP.

### Step 2: Connect to the Droplet via SSH​

`ssh  root@ < your_droplet_ip >`

### Step 3: Go to the /etc/hasura directory​

`/etc/hasura`

`cd  /etc/hasura`

### Step 4: Edit the Caddyfile and change :80 to your domain​

`Caddyfile`

`:80`

```
vim  Caddyfile
.. .
 https://you.domain.example.com  {
  reverse_proxy * graphql-engine:8080  {
      header_up Host  { http.request.host }
      header_up X-Real-IP  { http.request.remote }
      header_up X-Forwarded-For  { http.request.remote }
      header_up X-Forwarded-Port  { http.request.port }
      header_up X-Forwarded-Proto  { http.request.scheme }
   }
}
.. .
# type ESC followed by :wq to save and quit
```

### Step 5: Restart the container​

`docker  compose restart caddy`

Go to `https://<your_domain>/console` to visit the Hasura Console.

## Updating to the latest version​

When a new version of the GraphQL Engine is released, you can upgrade to it by just changing the version tag in `docker-compose.yaml` . You can find the latest releases on the[ GitHub releases page ](https://github.com/hasura/graphql-engine/releases).

### Step 1: Connect to the Droplet via SSH​

`ssh  root@ < your_droplet_ip >`

### Step 2: Go to the /etc/hasura directory​

`/etc/hasura`

`cd  /etc/hasura`

### Step 3: Edit docker-compose.yaml and change the image tag to the latest one​

`docker-compose.yaml`

```
vim  docker-compose.yaml
.. .
graphql-engine:
   image: hasura/graphql-engine:latest_tag_here
.. .
# type ESC followed by :wq to save and quit
```

### Step 4: Restart the container​

`docker  compose up -d`

## Using DigitalOcean Managed Postgres Database​

### Step 1: Create a Postgres database​

Create a new Postgres database from the DigitalOcean console, preferably in the same region as the Droplet.

### Step 2: Get the database URL​

Once the database is created, under the "Overview" tab, from the "Connection Details" section, choose "Connection
string" from the dropdown. "Connection string" is the "Database URL". Copy it.

### Step 3: Connect to the Droplet via SSH​

`ssh  root@ < your_droplet_ip >`

### Step 4: Go to the /etc/hasura directory​

`/etc/hasura`

`cd  /etc/hasura`

### Step 5: Edit docker-compose.yaml and change the database URL​

`docker-compose.yaml`

```
vim  docker-compose.yaml
.. .
# change the url to use a different database
HASURA_GRAPHQL_DATABASE_URL:  < database-url >
.. .
# type ESC followed by :wq to save and quit
```

Similarly, the database URL can be changed to connect to any other Postgres database.

Note

If you're using Hasura with a restricted database user, make sure you go through[ Postgres permissions ](https://hasura.io/docs/latest/deployment/postgres-requirements/#postgres-permissions)to configure all required permissions
(not applicable with the default connection string with DO Managed Postgres).

#### Connection pooling​

Connection pooling is a built-in feature of graphql-engine. The default connection pool size is 50. If you need to
configure the pool size or the timeout, you can use the below environment variables.

- `HASURA_GRAPHQL_PG_CONNECTIONS` : Maximum number of Postgres connections that can be opened per stripe (default: 50).
- `HASURA_GRAPHQL_PG_TIMEOUT` : Each connection’s idle time before it is closed (default: 180 sec)


Note

If you still want to enable connection pooling on your managed database on DigitalOcean, you should do so in the `session` mode.

## Access database via psql​

To access the Postgres database via `psql` , you can use the following command via the terminal:

`docker   exec  -it hasura_postgres_1 psql -U postgres`

If you are using a hosted database[ as outlined above ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#do-managed-pg-db), it's a little different:

`docker   exec  -it hasura_postgres_1 psql -h  < your database url >  -p  < your port >  -d  < your database >  -U  < your database user >`

Note

Different hosted Postgres providers may have different requirements for connection, e.g. setting `sslmode` . Please refer
to your provider's documentation for generating the proper `psql` command flags.

## Logs​

### Step 1: Connect to the Droplet via SSH​

`ssh  root@ < your_droplet_ip >`

### Step 2: Go to the /etc/hasura directory​

`/etc/hasura`

`cd  /etc/hasura`

### Step 3: Check logs​

To checks logs for any container, use the following command:

`docker  compose logs  < container_name >`

Where `<container_name>` is one of `graphql-engine` , `postgres` or `caddy` .

## Troubleshooting​

Logs should be able to help you in most scenarios. If it doesn't, feel free to talk to us on[ Discord ](https://discord.gg/hasura).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#introduction)
- [ Deploying Hasura on DigitalOcean ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#deploying-hasura-on-digitalocean)
    - [ Step 1: Create a Hasura One-click Droplet ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-1-create-a-hasura-one-click-droplet)

- [ Step 2: Open the Console ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-2-open-the-console)

- [ Step 3: Create a table ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-3-create-a-table)

- [ Step 4: Insert sample data ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-4-insert-sample-data)

- [ Step 5: Try out GraphQL ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-5-try-out-graphql)
- [ Securing the GraphQL endpoint ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#digital-ocean-secure)
    - [ Step 1: Connect to the Droplet via SSH ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-1-connect-to-the-droplet-via-ssh)

- [ Step 2: Go to the /etc/hasura directory ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-2-go-to-the-etchasura-directory)

- [ Step 3: Set an admin secret ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-3-set-an-admin-secret)

- [ Step 4: Update the container ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-4-update-the-container)
- [ Adding a domain & enabling HTTPS ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#adding-a-domain--enabling-https)
    - [ Step 1: Add a record mapping ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-1-add-a-record-mapping)

- [ Step 2: Connect to the Droplet via SSH ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-2-connect-to-the-droplet-via-ssh)

- [ Step 3: Go to the /etc/hasura directory ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-3-go-to-the-etchasura-directory)

- [ Step 4: Edit the Caddyfile and change :80 to your domain ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-4-edit-the-caddyfile-and-change-80-to-your-domain)

- [ Step 5: Restart the container ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-5-restart-the-container)
- [ Updating to the latest version ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#do-updating)
    - [ Step 1: Connect to the Droplet via SSH ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-1-connect-to-the-droplet-via-ssh-1)

- [ Step 2: Go to the /etc/hasura directory ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-2-go-to-the-etchasura-directory-1)

- [ Step 3: Edit docker-compose.yaml and change the image tag to the latest one ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-3-edit-docker-composeyaml-and-change-the-image-tag-to-the-latest-one)

- [ Step 4: Restart the container ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-4-restart-the-container)
- [ Using DigitalOcean Managed Postgres Database ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#do-managed-pg-db)
    - [ Step 1: Create a Postgres database ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-1-create-a-postgres-database)

- [ Step 2: Get the database URL ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-2-get-the-database-url)

- [ Step 3: Connect to the Droplet via SSH ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-3-connect-to-the-droplet-via-ssh)

- [ Step 4: Go to the /etc/hasura directory ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-4-go-to-the-etchasura-directory)

- [ Step 5: Edit docker-compose.yaml and change the database URL ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-5-edit-docker-composeyaml-and-change-the-database-url)
- [ Access database via psql ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#digital-ocean-connect-psql)
- [ Logs ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#do-logs)
    - [ Step 1: Connect to the Droplet via SSH ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-1-connect-to-the-droplet-via-ssh-2)

- [ Step 2: Go to the /etc/hasura directory ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-2-go-to-the-etchasura-directory-2)

- [ Step 3: Check logs ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#step-3-check-logs)
- [ Troubleshooting ](https://hasura.io/docs/latest/deployment/deployment-guides/digital-ocean-one-click/#do-logs/#troubleshooting)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)