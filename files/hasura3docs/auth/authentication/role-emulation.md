# Role Emulation

## Introduction​

You can configure authentication to allow certain roles to emulate other roles. This can be useful during development
to test access-control rules without setting up authentication.

To set up role emulation, the `AuthConfig` Hasura metadata object accepts a field called `allowRoleEmulationBy` .

When `allowRoleEmulationBy` is set up, Hasura will check for the value of the `x-hasura-role` session variable
which is returned in the webhook or JWT response to be equal to the value set in the `allowRoleEmulationBy` . If the
values are equal, then role emulation will be enabled for that request.

When role emulation is enabled for a request, the session variables, including the role, will be used from
the HTTP request headers instead of from the JWT or webhook.

### Role emulation scenario setup​

In the example below, we set up role emulation for the `user` role, allowing a `user` to emulate any other role:

```
---
kind :  AuthConfig
version :  v1
definition :
   allowRoleEmulationBy :  user
   webhook :
     webhookUrl :  https : //myauth.service.com/validate - request
```

Then, the following GraphQL request is made:

```
POST   /graphql   HTTP/2.0
Content-Type :   application/json
x-hasura-role :   author
x-hasura-author-id :   2
{
   "query" :   "query GetAuthor { author { id name } }" ,
   "variables" :   null ,
   "operationName" :   "GetAuthor"
}
```

This request will be executed normally using the `author` role and access-control rules related to the `author` role
will be applied to the request, for example: returning only the `id` and `name` fields of the author with `id` 2.

### Role emulation scenario 1​

Now, let's assume the authentication webhook responds with the following session variables for the request:

```
{
   "x-hasura-role" :   "user"
}
```

Then, because the `user` role is allowed to emulate other roles, (as per the `allowRoleEmulationBy: user` value in our
AuthConfig) the GraphQL request will be executed as the `author` role, because the `x-hasura-role: author` value is set
in the headers of the request, along with `x-hasura-author-id: 2` .

### Role emulation scenario 2​

If the authentication webhook response is as follows:

```
{
   "x-hasura-role" :   "user" ,
   "x-hasura-author-id" :   1
}
```

Then even in this case, because the `user` role is making the request and is allowed to emulate other roles,
the GraphQL request will be executed as the `author` role, as that is the role stipulated in the request headers.

Thus, the value of the session variable `x-hasura-author-id` will be 2 and not 1.

### Role emulation scenario 3​

To illustrate an unsuccessful emulation scenario; if the webhook response were the following:

```
{
   "x-hasura-role" :   "author" ,
   "x-hasura-author-id" :   1
}
```

Then, the GraphQL query will be executed as the `author` role and **only** the session variables from the authentication
webhook response will be considered.

This is because the author role is not allowed to emulate other roles via HTTP request headers. All session variables
for this role will be extracted from either a verified JWT or authentication webhook response.

Therefore, in this case, the value of the session variable `x-hasura-author-id` will be 1 as returned by the
authentication webhook response and not 2 as specified in the request headers.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/3.0/auth/authentication/role-emulation/#introduction)
    - [ Role emulation scenario setup ](https://hasura.io/docs/3.0/auth/authentication/role-emulation/#role-emulation-scenario-setup)

- [ Role emulation scenario 1 ](https://hasura.io/docs/3.0/auth/authentication/role-emulation/#role-emulation-scenario-1)

- [ Role emulation scenario 2 ](https://hasura.io/docs/3.0/auth/authentication/role-emulation/#role-emulation-scenario-2)

- [ Role emulation scenario 3 ](https://hasura.io/docs/3.0/auth/authentication/role-emulation/#role-emulation-scenario-3)
