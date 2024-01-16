# Authentication

Hasura gives you the power to authenticate users how you want, integrating with many popular auth services or your own existing custom solution hosted elsewhere.


#### Quick Links

- [ Check out the AuthConfig metadata. ](https://hasura.io/docs/3.0/auth/authentication/)
- [ Implement auth using JWT mode. ](https://hasura.io/docs/3.0/auth/authentication/jwt/)
- [ Implement auth using webhook mode. ](https://hasura.io/docs/3.0/auth/authentication/webhook/)


Embedded content: [ View content ](https://www.youtube.com/embed/KQ6MHzp6XzE?enablejsapi=1&origin=https://hasura.io)

Image: [ Authentication and authorization with Hasura ](https://hasura.io/docs/3.0/assets/images/auth-high-level-overview-diagram-0e382368ed24f0a214f1363003958e5e.png)

## Using Authentication​

### JWT Mode

With JWT Mode, Hasura can easily integrate with your existing authentication service and rapidly help you configure granular access to your data.

### Webhook Mode

With webhook mode you can specify a URL for Hasura to call which will return user information in session variables.

### Role Emulation

Hasura can be set up to emulate roles and process requests using the defined access-control rules for another role. This can be useful for testing without setting up authentication.

### What did you think of this doc?