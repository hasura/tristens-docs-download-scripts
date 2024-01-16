# Secure Connect Tunnels

## Introduction​

Secure Connect Tunnels allow you to securely connect a local database to your Hasura-hosted DDN project. This allows you
to interact with a local database via your Hasura project and use the Hasura Console and other Hasura services.

Typically, tunnels are used for local development to iterate quickly on your project. We recommend using a service such
as Docker to manage your local database and other local resources.

Additionally, you can use tunnels to test local data connectors, such as the[ TypeScript connector ](https://github.com/hasura/ndc-typescript-deno), before[ deploying ](https://hasura.io/docs/3.0/connectors/deployment/)them to Hasura DDN.

Using Docker

If you're not familiar with running a database via Docker, we recommend checking out the[ PostgreSQL docker getting started ](https://hub.docker.com/_/postgres)as an example.

## Tunnel lifecycle​

### Create​

The Hasura CLI creates and manages tunnels. The CLI utilizes a[ daemon ](https://en.wikipedia.org/wiki/Daemon_computing)that runs in the background and manages the tunnel. To create a tunnel, first start the daemon using the `daemon` command:

`hasura3 daemon start`

The daemon will block the window / tab while it runs. Once the daemon is running, you can create a tunnel using the `tunnel create` command in a new window / tab:

```
# e.g., hasura3 tunnel create localhost:5432
hasura3 tunnel create  < SOCKET >
```

What's a socket?

This argument is the socket address that the daemon will use to communicate with the tunnel.

It must include the IP address or hostname of the machine running the daemon, and a port number. For example, `localhost:5432` or `localhost:3306` .

This socket becomes the identifier for the tunnel. You can use the `tunnel list` command to see a list of all tunnels
that are currently running.

### Use​

After creating a tunnel, the CLI will return a URL that you can use to connect to your database. **You should use this
URL to form a connection string for your database, like this example using PostgreSQL:** 

`postgresql://<USERNAME>:<PASSWORD>@<URL_RETURNED_BY_THE_CLI>/<DATABASE_NAME>`

This connection string can now be used in your metadata to scaffold our your API and service requests in the Hasura
Console or from your projects endpoints.

Testing a data connector?

Simply pass the connection string using your local host and the port that the connector is running on. For example:

`http://localhost:8100`

#### Pause​

To pause a tunnel, use the `tunnel pause` command:

`hasura3 tunnel pause  < SOCKET >`

#### Activate​

To activate a tunnel, use the `tunnel activate` command:

`hasura3 tunnel activate  < SOCKET >`

### Delete​

To delete a tunnel, use the `tunnel delete` command:

`hasura3 tunnel delete  < SOCKET >`

To stop the daemon at any point, simply kill the process in your terminal using `Ctrl + C` .

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/ci-cd/tunnels/#introduction)
- [ Tunnel lifecycle ](https://hasura.io/docs/3.0/ci-cd/tunnels/#tunnel-lifecycle)
    - [ Create ](https://hasura.io/docs/3.0/ci-cd/tunnels/#create)

- [ Use ](https://hasura.io/docs/3.0/ci-cd/tunnels/#use)

- [ Delete ](https://hasura.io/docs/3.0/ci-cd/tunnels/#delete)
