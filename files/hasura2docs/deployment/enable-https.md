# Enable HTTPS

## Setting up HTTPS​

Hasura GraphQL Engine does not handle SSL/TLS for your API. That means,
Hasura GraphQL Engine cannot serve your API on an HTTPS URL.

You should use a reverse proxy (like Nginx, Caddy, Kong, Traefik etc.)
or the cloud provider's native load balancer SSL termination features to
secure your API.

## Sample configurations​

Here are a few sample configurations for some popular proxies:

### Nginx​

Here is a sample `nginx.conf` to proxy requests to Hasura:

```
server   {
   listen   80 ;
   listen   443  ssl ;
   server_name  hasura.<my-domain.com> ;
   location  /   {
     proxy_pass  http://localhost:8080/ ;
     proxy_http_version  1.1 ;
     proxy_set_header  Upgrade  $http_upgrade ;
     proxy_set_header  Connection  "upgrade" ;
   }
}
```

Please note that setting up SSL is not covered in this guide. You can
find more information at[ Nginx docs ](https://nginx.org/en/docs/http/configuring_https_servers.html).

To serve Hasura with a URL prefix instead of a separate subdomain, use `location /hasura/` or similar.

### Caddy​

Here is a sample `Caddyfile` to proxy requests to Hasura:

```
hasura. < my-domain.com >   {
  reverse_proxy localhost:8080
}
```

Caddy has TLS provisioning built-in with Let's Encrypt or ZeroSSL. You can find the docs at[ Caddy website ](https://caddyserver.com/docs/automatic-https).

In order to serve at a URL prefix, use the following configuration:

```
< my-domain.com >   {
  handle_path /hasura*  {
    reverse_proxy localhost:8080
   }
  handle  {
     # Fallback for otherwise unhandled requests
   }
}
```

### Traefik​

Here are sample `traefik.toml` and `traefik-dynamic.toml` files to proxy requests to Hasura:

```
#traefik.toml
[providers]
  [providers.file]
    filename = "traefik-dynamic.toml"
[api]
  dashboard = true
  debug = true
[entryPoints]
  [entryPoints.web]
    address = ":80"
    [entryPoints.web.http]
      [entryPoints.web.http.redirections]
        [entryPoints.web.http.redirections.entryPoint]
          to = "web-secure"
          scheme = "https"
  [entryPoints.web-secure]
    address = ":443"
[certificatesResolvers.sample.acme]
  email = "myemail@example.com"
  storage = "acme.json"
  [certificatesResolvers.sample.acme.httpChallenge]
    # used during the challenge
    entryPoint = "web"
```

```
#traefik-dynamic.toml
[http]
    [http.routers]
       [http.routers.my-router]
          rule = "Host(`hasura.example.com`)"
          service = "hasura"
          entryPoints = ["web-secure"]
       [http.routers.my-router.tls]
          certResolver = "sample"
    [http.services]
        [http.services.hasura.loadbalancer]
            [[http.services.hasura.loadbalancer.servers]]
                url = "http://127.0.0.1:5000"
```

In order to serve at a URL prefix, use the following configuration:

```
#traefik-dynamic.toml
...
    [http.routers]
       [http.routers.my-router]
          rule = "Host(`example.com`) && Path(`/hasura`))"
          service = "hasura"
          entryPoints = ["web-secure"]
       [http.routers.my-router.tls]
          certResolver = "sample"
...
```

Please note that setting up SSL is not covered in this guide. You can
find more information at the[ Traefik docs ](https://doc.traefik.io/traefik/https/overview).

### What did you think of this doc?

- [ Setting up HTTPS ](https://hasura.io/docs/latest/deployment/enable-https/#setting-up-https)
- [ Sample configurations ](https://hasura.io/docs/latest/deployment/enable-https/#sample-configurations)
    - [ Nginx ](https://hasura.io/docs/latest/deployment/enable-https/#nginx)

- [ Caddy ](https://hasura.io/docs/latest/deployment/enable-https/#caddy)

- [ Traefik ](https://hasura.io/docs/latest/deployment/enable-https/#traefik)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)