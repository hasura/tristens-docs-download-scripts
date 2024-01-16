# Hasura GraphQL Engine on Azure with Container Instances and Postgres

## Introduction​

This guide walks you through deploying the Hasura GraphQL Engine on[ Azure ](https://azure.microsoft.com)using[ Container Instances ](https://azure.microsoft.com/en-us/services/container-instances/)with[ Azure Database for PostgreSQL server ](https://azure.microsoft.com/en-us/services/postgresql/).

## One-click deployment using ARM Template​

You can deploy all the resources mentioned in this guide with the one-click button below.

- With a new Postgres Server
- With an existing Postgres Server


[  ](https://portal.azure.com/#create/Microsoft.Template/uri/https%3a%2f%2fraw.githubusercontent.com%2fhasura%2fgraphql-engine%2fstable%2finstall-manifests%2fazure-container-with-pg%2fazuredeploy.json)

Image: [ Deploy to Azure ](https://aka.ms/deploytoazurebutton)

(This button takes you to the Azure Portal. Read more about this Resource Manager Template[ here ](https://github.com/hasura/graphql-engine/tree/stable/install-manifests/azure-container-with-pg)).

[  ](https://portal.azure.com/#create/Microsoft.Template/uri/https%3a%2f%2fraw.githubusercontent.com%2fhasura%2fgraphql-engine%2fstable%2finstall-manifests%2fazure-container%2fazuredeploy.json)

Image: [ Deploy to Azure ](https://aka.ms/deploytoazurebutton)

(This button takes you to the Azure Portal. Read more about this Resource Manager Template[ here ](https://github.com/hasura/graphql-engine/tree/stable/install-manifests/azure-container)).

## Pre-requisites​

- Valid Azure subscription with billing enabled or credits ([ click here ](https://azure.microsoft.com/en-us/free/)for a
free trial).
- [ Azure CLI ](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).


The Actions mentioned below can be executed using the Azure Portal and the Azure CLI. But for the sake of simplicity in
documentation, we are using Azure CLI; so that commands can be easily copy-pasted and executed.

Once you install the `CLI` , login to your Azure account:

`az login`

## Create a new Resource Group​

The Resource Groups are used to group various resources on Azure. Create a resource group called `hasura` at the `westus` location.

`az group create --name hasura --location westus`

## Provision a PostgreSQL server​

Note

If you already have a database setup, you can skip these steps and jump directly to[ Allow access to Azure Services ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#azure-allow-access).

After you create the resource group, create a Postgres server instance:

```
az postgres server create --resource-group hasura  \
   --name  "<server_name>"   \
   --location westus  \
   --admin-user hasura  \
   --admin-password  "<server_admin_password>"   \
   --sku-name GP_Gen5_2  \
   --version  10
```

Note

- Choose a unique name for `<server_name>` variable.
- Select a strong password for the `<server_admin_password>` variable, that must include uppercase, lowercase, and
numeric characters. You will need the password later to connect to the database. (make sure you escape the special
characters depending on your shell).


Note the hostname in the output, as indicated below:

```
.. .
"fullyQualifiedDomainName" :   "<server_name>.postgres.database.azure.com" ,
.. .
```

where; `<server_name>.postgres.database.azure.com` is the hostname.

Note

If you get an error saying `Specified server name is already used` , change the value of `--name` ( `<server_name>` ) to
something else.

## Create a new database​

Create a new database on the server:

```
az postgres db create --resource-group hasura  \
   --server-name  "<server_name>"   \
   --name hasura
```

## Allow access to Azure Services​

Create a firewall rule allowing access from Azure internal services:

```
az postgres server firewall-rule create --resource-group hasura  \
   --server-name  "<server_name>"   \
   --name  "allow-azure-internal"   \
   --start-ip-address  0.0 .0.0  \
   --end-ip-address  0.0 .0.0
```

## Create a Container Instance​

Launch Hasura using a container instance:

```
az container create --resource-group hasura  \
   --name hasura-graphql-engine  \
   --image hasura/graphql-engine  \
   --dns-name-label  "<dns-name-label>"   \
   --ports  80   \
   --environment-variables  "HASURA_GRAPHQL_SERVER_PORT" = "80"   "HASURA_GRAPHQL_ENABLE_CONSOLE" = "true"   "HASURA_GRAPHQL_ADMIN_SECRET" = "<admin-secret>" \
   --secure-environment-variables  "HASURA_GRAPHQL_DATABASE_URL" = "<database-url>"
```

 `<database-url>` should be replaced by the following format:

`postgres://hasura%4 0 < server_name > : < server_admin_password > @ < hostname > :5432/hasura`

If you'd like to connect to an existing database, use that server's database url.

Note

 `%40` is used in the username because Azure creates usernames as `admin-user@server-name` and since the database url
uses `@` to separate username-password from hostname, we need to url-escape it in the username. Any other special
character should be url-encoded.

If the `<dns-name-label>` is not available, choose another unique name and execute the command again.

## Setting up JWT​

Use the `HASURA_GRAPHQL_JWT_SECRET` env variable to setup JWT. To generate a new JWT config refer[ here ](https://hasura.io/docs/latest/auth/authentication/jwt/#generating-jwt-config).

Note

The `HASURA_GRAPHQL_JWT_SECRET` env variable requires JSON format. To create a container group with `az container create --environment-variables` flag you need to pass the variable as a key-value pair.

In order to use the env variable with the `az container create` command, pass the *JSON* value for the env
variable as a string by escaping the characters like so:

```
az container create --resource-group hasura  \
      --name hasura-graphql-engine  \
      --image hasura/graphql-engine  \
      --dns-name-label  "<dns-name-label>"   \
      --ports  80   \
      --environment-variables  "HASURA_GRAPHQL_SERVER_PORT" = "80"   \
       "HASURA_GRAPHQL_ENABLE_CONSOLE" = "true"   \
       "HASURA_GRAPHQL_ADMIN_SECRET" = "<admin-secret>"   \
       "HASURA_GRAPHQL_JWT_SECRET" =   \   "{ \" type \" :  \" RS512 \" , \" key \" :  \" -----BEGIN CERTIFICATE----- \\ nMIIDBzCCAe+gAwIBAgIJTpEEoUJ/bOElMA0GCSqGSIb3DQEBCwUAMCExHzAdBgNV \\ nBAMTFnRyYWNrLWZyOC51cy5hdXRoMC5jb20wHhcNMjAwNzE3MDYxMjE4WhcNMzQw \\ nMzI2MDYxMjE4WjAhMR8wHQYDVQQDExZ0cmFjay1mcjgudXMuYXV0aDAuY29tMIIB \\ nIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuK9N9FWK1hEPtwQ8ltYjlcjF \\ nX03jhGgUKkLCLxe8q4x84eGJPmeHpyK+iZZ8TWaPpyD3fk+s8BC3Dqa/Sd9QeOBh \\ nZH/YnzoB3yKqF/FruFNAY+F3LUt2P2t72tcnuFg4Vr8N9u8f4ESz7OHazn+XJ7u+ \\ ncuqKulaxMI4mVT/fGinCiT4uGVr0VVaF8KeWsF/EJYeZTiWZyubMwJsaZ2uW2U52 \\ n+VDE0RE0kz0fzYiCCMfuNNPg5V94lY3ImcmSI1qSjUpJsodqACqk4srmnwMZhICO \\ n14F/WUknqmIBgFdHacluC6pqgHdKLMuPnp37bf7ACnQ/L2Pw77ZwrKRymUrzlQID \\ nAQABo0IwQDAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBSOG3E+4lHiI+l0i91u \\ nxG2Rca2NATAOBgNVHQ8BAf8EBAMCAoQwDQYJKoZIhvcNAQELBQADggEBAKgmxr6c \\ nYmSNJOTPtjMFFDZHHX/7iwr+vqzC3nalr6ku8E3Zs0/IpwAtzqXp0eVVdPCWUY3A \\ nQCUTt63GrqshBHYAxTbT0rlXFkqL8UkJvdZQ3XoQuNsqcp22zlQWGHxsk3YP97rn \\ nltPI56smyHqPj+SBqyN/Vs7Vga9G8fHCfltJOdeisbmVHaC9WquZ9S5eyT7JzPAC \\ n5dI5ZUunm0cgKFVbLfPr7ykClTPy36WdHS1VWhiCyS+rKeN7KYUvoaQN2U3hXesL \\ nr2M+8qaPOSQdcNmg1eMNgxZ9Dh7SXtLQB2DAOuHe/BesJj8eRyENJCSdZsUOgeZl \\ nMinkSy2d927Vts8= \\ n-----END CERTIFICATE----- \" }"
      --secure-environment-variables  "HASURA_GRAPHQL_DATABASE_URL" = "<database-url>"
```

Note

Check out the[ Running with JWT ](https://hasura.io/docs/latest/auth/authentication/jwt/#running-with-jwt)section for the usage of `HASURA_GRAPHQL_JWT_SECRET` env variable.

## Open the Hasura Console​

That's it! Once the deployment is complete, navigate to the container instance's IP or hostname to open the Hasura
console:

```
az container show --resource-group hasura  \
   --name hasura-graphql-engine  \
   --query  "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}"   \
   --out table
```

The output will contain the FQDN in the format `<dns-name-label>.westus.azurecontainer.io` .

Visit the following URL for the Hasura Console:

`http://<dns-name-label>.westus.azurecontainer.io/console`

Replace `<dns-name-label>` with the label given earlier.

Image: [ Hasura Console ](https://storage.googleapis.com/graphql-engine-cdn.hasura.io/main-repo/img/azure_arm_aci_console_graphiql.png)

You can create tables and test your GraphQL queries here.

## Troubleshooting​

If your password contains special characters, check if the password is URL encoded and given as env variables. Also,
check for proper escaping of these characters based on your shell.

You can check the logs to see if the database credentials are proper and if Hasura is able to connect to the database.

If you're using an existing/external database, make sure the firewall rules for the database allows connection for Azure
services.

### Checking logs​

If the Console doesn't load, check the logs:

```
az container logs --resource-group hasura  \
   --name hasura-graphql-engine  \
   --container-name hasura-graphql-engine
# use --follow flag to stream logs
```

## Tearing down​

To clean up the deployment, delete the resource group:

`az group delete --resource-group hasura`

## References​

- [ Installing Azure CLI ](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [ Creating a Azure Postgres Server ](https://docs.microsoft.com/en-us/azure/postgresql/quickstart-create-server-database-azure-cli)
- [ Using Azure Container Instances ](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-quickstart)


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#introduction)
- [ One-click deployment using ARM Template ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#one-click-deployment-using-arm-template)
- [ Pre-requisites ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#pre-requisites)
- [ Create a new Resource Group ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#create-a-new-resource-group)
- [ Provision a PostgreSQL server ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#provision-a-postgresql-server)
- [ Create a new database ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#create-a-new-database)
- [ Allow access to Azure Services ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#azure-allow-access)
- [ Create a Container Instance ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#create-a-container-instance)
- [ Setting up JWT ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#setting-up-jwt)
- [ Open the Hasura Console ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#open-the-hasura-console)
- [ Troubleshooting ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#troubleshooting)
    - [ Checking logs ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#azure-logs)
- [ Tearing down ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#tearing-down)
- [ References ](https://hasura.io/docs/latest/deployment/deployment-guides/azure-container-instances-postgres/#azure-logs/#references)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)