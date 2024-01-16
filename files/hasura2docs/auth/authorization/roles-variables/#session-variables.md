# Roles & Session Variables

## Roles​

Every table or view can have permission rules defined for users based on user **role** . You define your own
roles in the Hasura GraphQL Engine and then create permissions for each of them.

For example:

| Role | Description | Allowed Activity |
|---|---|---|
| anonymous | A user who is not logged-in | Only read from some restricted tables/views |
| user | A user who is logged in | CRUD on data that belongs to them |
| manager | A user that has access to other users' data | CRUD on all users' data |


See[ this section ](https://hasura.io/docs/latest/auth/authorization/permissions/)on how to configure permissions.

### The admin role​

By default, there is an `admin` role that can perform any operation on any table. It can be used like any other
user role when making queries where you would like full unrestricted permissions. The alternative to this method is to
use the[ admin secret header ](https://hasura.io/docs/latest/auth/authentication/admin-secret-access/).

### Role-based schema publishing​

For every role that you create, Hasura automatically publishes a different GraphQL schema that represents the right
fields, queries and mutations that are available to that role so that users with that role will only see a schema
which they are able to access.

### Create a new role​

New roles are created "on-the-fly" when a permission is configured for it.

- Console
- CLI
- API


In the **Console** , in **Data -> [table] -> Permissions** , enter a new role name and click on the `select` cell for the role in order to begin configuring permissions for that role. When the permissions are saved, the new
role will be created.

Image: [ Using boolean expressions to build rules ](https://hasura.io/docs/assets/images/authorization_create-new-role_2-16-1-552e53210d0901ded85127ef15c287c5.png)

Using the CLI, you can create a new role by defining permissions for it infile. Eg:

```
-   table :
     schema :  public
     name :  products
   select_permissions :
     -   role :  user
       permission :
         columns :   [ ]
         filter :
           price :
           _lt :   1000
```

Apply the metadata by running:

`hasura metadata apply`

By defining permissions for a role, the role is created.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_create_select_permission" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "products" ,
     "role" :   "user" ,
     "permission" :   {
       "columns" :   "*" ,
       "filter" :   {
         "price" :   {
           "_lt" :   1000
         }
       }
     }
   }
}
```

### Delete a role​

Deleting a role can be done from the[ permissions summary section ](https://hasura.io/docs/latest/auth/authorization/permissions/permissions-summary/).

### Copy a role​

Copying a role and its permissions can be done from the[ permissions summary section ](https://hasura.io/docs/latest/auth/authorization/permissions/permissions-summary/).

## Session variables​

Permissions usually incorporate *session variables* . Session variables are data returned from your
authentication service for each request.

In JWT mode, session variables are encoded into the payload of the JWT
token. In webhook mode, session variables are returned as a JSON object in the body of the response from the webhook.

Session variable key format

Session variables are case-insensitive and Hasura Engine only has access to session variables beginning with `X-Hasura-` .

When you are constructing permission rules there might be several variables that represent the required business
logic of having access to data. For example, if you have a SaaS application, you might restrict access based on a `client_id` variable. If you want to provide different levels of access on different devices, you might restrict
access based on a `device_type` variable. It is entirely up to you to decide what restrictions and permissions you
want to apply to your data.

Hasura allows you to create powerful permissions that can use any variable that is a property of the request.

Examples:

| Example | Role | Condition | Permission expression |
|---|---|---|---|
| Allow access to user's own row |  `user`  |  `user_ id` column is equal to the user id session variable in a request |  |
| Allow project admins access to anything that belongs to the project |  `project-admin`  |  `project_ id` column is equal to the project id session variable of the user |  |


Allow access to user's own row

 `user` 

 `user_ id` column is equal to the user id session variable in a request

```
{
   "user_id" :   {
     "_eq" :   "X-Hasura-User-Id"
   }
}
```

Allow project admins access to anything that belongs to the project

 `project-admin` 

 `project_ id` column is equal to the project id session variable of the user

```
{
   "project_id" :   {
     "_eq" :   "X-Hasura-Project-Id"
   }
}
```

Attribute-Based Access Control - ABAC

Session variables are analogous to *attributes* in a typical[ attribute-based access control ](https://en.wikipedia.org/wiki/Attribute-based_access_control)(ABAC) system.

## Model roles in Hasura​

Roles in Hasura are defined in a flat, non-hierarchical model.

Role systems can typically be modeled in two ways:

1. **Flat roles** : Non-hierarchical roles with each role requiring an independent access scope to be defined. This
is the model which is used in Hasura.
2. **Hierarchical roles** : Access scopes are nested depending on available roles.[ Roles in GitHub for organizations ](https://help.github.com/en/articles/managing-peoples-access-to-your-organization-with-roles)is an example of such modeling where access scopes are inherited by deeper roles. Eg:


Image: [ Hierarchical roles ](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABAQAAAHgCAYAAAAyir/cAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgAElEQVR42u3dzY8c5Z3A8fwv+LgHyC1ZYe8pWQg5RUAWLuvALs4BC6Q1iUEQZVm8WXwg9obAJcPBOJIBx4BiohhjhG3EBItB4s1eg7QYv7AIVvLLDjYmuLZ/NfM0z9T0jMdjGKb79/lIJWZ6uqtfcFU99e2q7m81AAAAQDrf8hIAAABAPoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAA34gjH37c7Js4aDKlnw689V5z8vSklQIAggAAoy12fB7ZtqvZunOfnUGTqTftHn+jXSb2TxyyggBAEABgdMWOzz47PjDDuc/ON2M7XmyPFgAAQQCAkROnCUQQAAYsHycsHwAIAgCMqDcOH2n+uPc1LwTM4Ve/e9qLAIAgAIAgAIIAAAgCAAgCIAgAgCAAgCAAggAACAIACAIgCACAIACAIACCAAAIAgAIAiAIAIAgAIAgAIIAAAgCAAgCIAgAIAgAgCAAggAAggAACAIgCAAgCACAIACCAACCAAAIAiAIACAIAIAgAIIAAIIAAAgCIAgAIAgAgCAAggAAggAAggAgCAAgCAAgCACCAACCAACCAAgCACAIACAIgCAAAIIAAIIACAIAIAgAIAiAIAAAggAAggAIAgAgCAAgCIAgAACCAACCwMg5ffpMc/T4hxe9LLxz6N1m/MDr7X/nmlf8PaaL3c+g+SMIACAIAIAgsETW3buhueLKq2fsoG96ZKy9bPzARPv7sd7fVl57fXtZmeL3Y/VtHh2b9fdde/bOmudTzzzXn5coIAgAIAgAgCCwjIPA/Q9u7v9+9PiJdqf+pltu798mfo+/x/Xi7+8cOtzu9F919TXtkQH1PK+7YXXvPh9op/I3BAEABAEAEASWYRC47Y717e/H5nhH/6Zbb293/mtxdEDc5rHHn5gxz4gHCAIACAIAIAgMQRAoRwBc2dvpj53/+x/cNONzBFZdM3U0wLr7HuhPa+6cigjr7tswcJ4IAgAIAgAgCCzzIFCiwJo71renCpTPCSifEVCCQNyuO5XrCAKCAACCAAAIAkMYBGpx3frd/3LKQPczAerfBQFBAABBAAAEgWVk7PEnpj4QcOOm/tcKlm8B6H+o4MbNzXU3ru6fJhDXKR8iGPofKtibR3zOQISAuE3Mp/uhgoKAIACAIAAAgsAycKq3w15/pWD8HO/81zvv23s7/PH5Ad2vFayPKijfRFBPJRgIAoIAAIIAAAgCy1Ds2Me5/rHjH4Egfo8d91PVIf/1deY7lSD+HlN8/WD3b915IggAIAgAgCAAggAAggAACAIgCAAgCACAIACCAACCAACCACAIACAIACAIAIIAAIIAAIIACAIAIAgAIAiAIAAAggAAggAIAgAgCAAgCIAgAACCAACCAAgCACAIACAIgCAAAIIAAIIACAIAIAgAIAiAIACAIAAAggAIAgAIAgAgCIAgAIAgAACCAAgCAAgCACAIgCAAgCAAAIIACAIACAIAIAiAIACAIAAAggAIAgAIAgCkDgLbd497IWCAk6cnm4e27PRCACAIADB6zn12vnlk2652xweYaf/EQUfQACAIADC6Drz1XhsF4miBk2cmTSZTb9o9/uZULDsjlgEgCAAwwiIGbN25r/ltbwfIZDLtanaPvyEGACAIAABL49VDf21WP/ipFwIAkhIEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACApQQAAchMEACCRFyY+b+4ZOzcrCDz98ufN2ofPeYEAQBAAAEZVBIGYShCIGPCdtZPNoQ++8OIAgCAAAIx6FPjRLz9tQ4AYAACCAACQLAqIAQCQlyAAAImdnrzgRQCApAQBAAAASEgQAGDJHfnw4+b3O/c3j2zbZTKln8Z2vNjsfGmiOXl60soBAEEAgNF14K332p2gNw4faXeATKbs00efnGx2j7/RLheiAACCAAAjKXZ2Htqyszl5xk4PdEUU2D3+phcCAEEAgNFz+P0Tzfbd414IGODcZ+fbYAYAggAAIydOE/jj3te8EDCHX/3uaS8CAIIAAIIACAIAIAgAIAiAIAAAggAAggAIAgAgCAAgCIAgAACCAACCAAgCACAIACAIgCAAAIIAAIIACAIAIAgAIAiAIACAIAAAggAIAgAIAgAgCIAgAIAgAACCAAgCAAgCACAIgCAAgCAAAIIACAIACAIAIAiAIACAIAAAggAIAgAIAgAIAoAgAIAgAIAgAAgCAAgCAAgCIAgAgCAAgCAAggAACAIACAIgCACAIACAIMByM37g9eaKK69uNj0y5sUQBAAQBAAQBAQBQQBBAABBAABBgHmNbX2iWXXt9c39D24WBAQBABAEABAElrunnnmuWXffA82aO9e3P9dOnT7T7iTv2rO3OXb8w2bs8Seadw4dbv8Wv9//4Kb2dnH7625c3ay794FZ8+iK28U8Yz5x3bh9zCcuL4+ne9lCH+9i510Hgfh5rvmHdw6923/egx5jvEaP9abTvdcufr7Y6yEIAIAgAIAgsOTuum9DuyN83Q2rm5tuub39eeW117c7s+Fob2c3Lrvp1tvby+Pn2MGNneArr76mnSICrLljffu32BG+mLLz/Q+9ecbt477L/d6/cXN7Wbmv+rGENXfePfV4eo+1PN4IEZc773K7eC5xnVXXTF2n+5wijMRlcZ14zmVe4wcm+teJ28blEQzKYxUEAEAQABbp+McXmh0vf948/MxnJtOSTU++8N8jHQRix757mPz2zmUlCMQObvzt6PET7VEDcVpAXB7vlhcRDa7q7SgvNAisu29D/7J1926Y87Kys10eb72DHo+zvmyx8y63i+d5qoohseNfP6f4e32d+G+JDHUQiHnFaxRHKsRrNspB4NAHX1hfmJZsemHi83ZMAAgCQAKvHvprs3rj2eY7ayebe8bOGQyZljYI7BntIHDb9Lv69U59qN91L0Gg3pkOJQgcrQ6XL/Or51NPJTKUne/6UPoSIua7rMy/PmKgPL41d9x9WfOe6zMESjiI1yimsqM/6DrltYggsJAwIgiYTJc+rf3N2eZ7P59sxwbCAAgCwAh7+NnzbQh4+uXPvRh8I0b9lIF4R7+7U192aMs73nMFgXhnvd0Rv3N9uzMd58pP7ZivnzGfehrrvIt/qTvt5fEOmsph+V9XEIjnW64z11SONqhfvwxBAL4JMTaIMPDb3lgBEASAEYwB3/vZpPqPIPA1Ku+4d4NAe+79RY4QmNpZnjrfvpxTH++cHx3wIYBdl3uEQDkMvzt93UGgPkJg0P2X0wgEAVgax3pjBFEABAFgxBz/5IIYgCCwBMq7+vUH4h3rBIC5gkDsSMdh8aeqw/cXarE77eXzAurHG3bt2XfZ8y63iyMeauVDA+M0hfJ5AXGkQi1CQf1NA4IALG0U+Nu1k+0phoAgAIyAf9x41mkCCAJLIHZwy4fkxc52BIL4OXZ6yzv9cwWBEhNi57hM5Wv4Tl8kEix2p7083ggR8bWA8RjKaQTdDwdcbBCI+ce84/Uo866fe//UiN5zjZ/j+XYjgSAASyvGDD/pjR0AQQAYcuXoABAElkbs8JfD4su5+PWHDMbfYwe3+0F68Y54nFZQf0ZAOX2g+w56V8w/rh9f4VfEzwu5LB5P+brB8njrvy923uV2Uzv5m7/8asE77551FETEgnLkQFwnfq+vU74SURCApXHhQtMeJeDIQhAEgCEXXye09uFzXggEgWUudoh/3Tnfvt0Znn5XnRwEAZZFEOhN8U1EO/Y7uhAEAWCola8VAkFgeZt693x9/2iCOE0gDruPUFA+kBBBAIwfAEEAsEFHEBgx9WHz3a//W8g3DSAIgPEDIAgANugIAkMsvm5v6iv5Di/qGwcQBMD4ARAEABt0BAEQBMD4ARAEwAYdBAEQBMD4ARAEwAYdBAEQBMD4AQQBwAYdBAEQBMD4AQQBwAYdBAEQBDB+8EKAIADYoIMgAIIAxg+AIADYoIMgAIIAxg+AIADYoIMgAIIAxg+AIADYoIMgAIIAxg+AIADYoIMgAIIAxg+AIADYoCMICAIgCGD8AAgCgA06ggAgCGD8AAgCgA06ggAIAmD8AAgCgA06ggAIAmD8AAgCgA06ggAIAmD8AAgCgA06ggAIAmD8AAgCgA06ggAIAmD8AAgCgA06y9GREx83v9+53wsBA3z0yclmbMeLXgiMHwBBALBBZzTFDs/+iUNeCKicPXe+XTbiKBowfgAEAcAGnZF08sxk88i2Xc325//S7Js4aDKln3a/8ma7TOwef9MKAuMHQBAAbNAZffFOqJ3Bb3ba9vw7zb/85k2vxTc8HXjrvfZ0GjB+AAQBwAYdWBKvHvprs/rBT70QgPEDCAKADTogCAAYP4AgANigA4IAYPwACAKADTogCADGD4AgANigA4IAYPwACAKADTogCADGD4AgANigA4IAYPwACAKADTogCADGD4AgANigA4IAYPwACAKADTogCADGD4AgANigA4IAYPwACAKADTogCADGD4AgANigA4IAYPwACAKADTogCADGD4AgANigA4IAYPwACAKADTogCADGD4AgADboAIIAYPwACAJggw4IAoIAYPwAggBggw4IAgDGDyAIADbogCAAGD8AggBggw4IAoDxAyAIADbogCAAGD8AggBggw4IAoDxAyAIADbogCAAGD8AggBggw4IAoDxAyAIADbogCAAGD8AggBggw4IAoDxAyAIADbogCAAGD8AggBggw4IAoDxAyAIADbogCAAGD8AggBggw4IAoDxAyAIADbogCAAGD8AggBggw4IAoDxAyAIgA06gCAAGD8AggDYoAOCgCAAGD+AIADYoAOCAIDxAwgCgA06IAgAxg9eCBAEABt0QBAAjB8AQQCwQQcEAcD4ARAEABt0QBAAjB8AQQCwQQcEAcD4ARAEABt0QBAAjB8AQQCwQQcEAcD4ARAEABt0QBAAjB8AQQCwQQcEAcD4ARAEABt0QBAAjB8AQQCwQQcEAcD4ARAEABt0QBAAjB8AQQCwQQcEAcD4ARAEABt0QBAAjB8AQQBs0L0QgCAAGD8AggDYoAMIAoDxAwgCgA06IAgAGD+AIADYoAOCAGD8YPwAggBggw4IAoDxAyAIADbogCAAGD8AggBggw4IAoDxAyAIADbogCAAGD8AggBggw4IAoDxAyAIADbogCAAGD8AggBggw4IAoDxAyAIADbogCAAGD8AggBwGZ5++fPm4AdfzNqgH+pdFn8D8jr+yYXm+McXBgaBFyasH8D4wfgBBAFgqMWG+/s/m2w36mWDHpd97+eT7X+BvCICfGft1PqhDgL3jJ1rVm886wWCxA4e+aL5+874IS77vvEDCALAcEaBtQ+faycxACjinb6IAlt2f94GgYgBP/rlp83pyQteHBAFZowfxAAQBIAhjgLf7Q36Y+BvYw50o8Df3Pp/7SQGAN0oEOOH7xo/gCAADH8UsDEH5ooCa39zVgwAjB9AEAAAAACyEAT4Wp08M9kc+fBjk8nUm5jp7Lnz/l2YTNYP1g8m00WmWB5AEGC4QsDpyeb3O/c3D23Z2Wzduc9kMvWmR7btag6/f8JAvzew2bl3wvrBZOqsH944fMQAomf3+JvWDyZTNf3qd083+ycOWTkgCDA8YmCzz4oLZvjok5PtIPd/ev/NbOdLE+2A/+xn3vGAfkg/M9luO4+cyH20QKwb4g0F6weYvX448NZ7XgwEAZa/eAd0bMeLXggYYN/EwWb77vG0zz+iSAxqgNkiBsTOcFbnPjvfRtPY+QFmrx9i+QBBgKHY4YkJmK1U/qzikOjMQQQutkMchwan3eH58ONma+IgAhcT4wfBDEEAQQAEgaEOAn/c+5p/CDAHQUAQAEEAQQBBAAQBQQAEAUEAEAQQBBAEQBAQBEAQEARAEBAEEAQQBEAQEARAEBAEQBAAQQBBAAQBQQAEAUEABAEQBBAEQBAQBEAQEARAEABBAEEABAFBAAQBQQAEARAEEARAEBAEQBAQBEAQAEEAQQAEAUEABAFBAAQBBAEQBEAQEARAEBAEQBBAEABBAAQBQQAEAUEABAEEARAEQBAQBEAQEARAEEAQAEEABAFBAAQBQQAEAQQBEARAEBAEQBAQBEAQQBBAEBAEQBAQBEAQEARAEEAQQBAABAFBAAQBQQAEAQQBBAEQBAQBQBAQBEAQQBBAEABBQBAABAFBAAQBBAEEARAEBAEQBAQBQBBAEEAQAEFAEABBQBAAQUAQQBBAEABBQBBguJ06fabZ/syfmvEDr3sxBIGhDwK79uxrp/kcO/5hs+mRsfa/cy0DMY+4rDb2+BP924AggCCAIACCgCCwDJzuDeaPGqQvWrx2V1x5dbPuvg1eDEFgqIPAhQsXmlXXXN+s+sEN817v/gc3t//mIwqED46daH+/6xcb+vO56dbbmxVXrezf5pVXJ9rr3HzrWgsGggCCAIIACAKCwHKx7t4N7UAdQUAQEAQWEgTeOXS4t954oB8SFxIE4iiCCAm79uy97McZETOORoj/jorynN459K4gAIIAgsBoDpi/zo3oN3XfgoAgMApB4LY71s8bBC62jF3KEQaD5nU5g/rFzC/+vpD7XOi8u0FgIfPPsl4SBIY/CCxkWVlIEPiqtucnT51u7yvmPX5g4mtZR1zO+uxS5xPXKa9X/RpmWF8IAggCCAIJjG19orny6mvajdzUgPmB/vmD8S7Bqmuvn7FBf+qZ59rL4r9FFPO4rLyrEBvNmJ569rn+vFf2/t49L3HQfdcb79vuuLudb9yuzBNBIFMQiEFmLANlGYmf63e5u8vQmjvXz1jOyrJT/h7X3fToWCc2TC1ng5bXev6DluFByvogzkWu7zvut/t4uo+l+/eV1XrlcuZdB4H7N27uXyeuf7H10v0bNw18veJdwrj9sB91IAgMZxBYOb0clH+rq35wfXtUQPHnPS/N2C4vJAjEdeI2cZRAfZ2YZt7XDTOWm1OnTs9az9zc+/3o8RPtUQddcWrCXMvx0d5jmG8dUT+OqdMbZi7D5XnH+uxS5vPDH6+evS7oXCfm+0pvPFSeU4xXYn1SrtNdv9avX/x/iP+W11YQQBAAQWBZiJ36dlB8y+3N9t7P5ZzDsuMdG712QFxtwMo7lfXOeWw047JSyGOwclVvwxjzjb+Vw53r25T7jsF0bCjLPOrrlI15DHxinnH4I4JApiAQy2CcA7xyOgrEzyXG1ctvLEPxewxIr7tx9YxlqOw4xDIef4vb1EGvLGexnNbLa1y3uwwvZOc3dtrLchvrjrh9efw33bJ21mUlOMZgPC6LKR5rPKf4OdYlZUdnsfMuQSBen3gOc62XYjBf1nlx/2WdWEeBer103Q2re9fZJAgIAkseBAZtY7+98tp+VH/q6Z3NimpZX2gQ6F5nrvu6+Z/WTl+nabfNcVn8PZbVWE/Vn18wKAgsdDmOx1cO0X/l1df666F6zFIeS3neg+ZdH63QnU95vD/88U++DAsvvNRfF8Rzitu0oaO6rxIX4/Yx7/LaPNa7z+7rF+vTWF+MTf9NEEAQAEFgWSiD71rZMJYNZ7sRq3Ywyg5HbODKwCMGFfV1ygaw1r1s0H2XjXsJC2Xg/VWczygICALDrCwL3ctimarfgesuv6c6pwoMOpe+zLueT3nHqxaX1cts+YTyMpVBe9lpr+9jexUAuyGxGzjqI5Le7s2zjpKLnXd53mvuuHvg61peoyund3wGXade39W3GXaCwHAGgdj5H7TtLjujX2UQqO8rLovlpJyyUK5T70zHZTGfn955z7xBoD70vuzI15eNbdk24zlMrQMmZtxPjD3q51Dm81i14z3osvpzAOrXoizXsc6pY8RU+NjQXtaegtV5rerHU16v+vUb1vWFIIAggCAwwsq7/93Bbxlclw1n2UkvH6YzNWB/fcbAPQYH9VEE5XDGuXZoyn3HdWIQU6ZynbLxH7QThCAgCEwZtAzFKQPdgW8czvvnPXvbnfbHHn9yziBQi0FtdxnuLtfxezmUtn43sKwf6ncHF3JZOfoo1iX1cypHK1zOvOf6UMEy/4iO5TZxX/X9l6Mqyvpu1NZLgsBofKhg2cku2+KvMgjU99W9Xfk9dnpjXRO/l/lcLAjUy+ygy8q79PVlZSxSQuSgINCNCIPmXaJAmU83CLQxojqqoPu8y2OLy7rrizKfhX4ApCCAIACCwDeiDJDnCgJfDu4n+oPhGGiUHYLYyMXv3TiwkCBQH74b99+dXhnRgbcgIAh81UFg6lzdtbOmMhguh8D/3bU3TP3tltsXFATKqQbzBYF4F74eCJd1wOUGgTistrtOKKcLLUUQmGu9VE5bEAQEgeUcBMrO/FIFgXbneM9L/UAZf4tl6Kp53hVfaBDoXhbvysd9tEcqTq8n4udLDQKD5lNOKyiPOT4YsVynHAVZz6M+NaG7roh1bYQLQQAEAQSBZa97vnEdBMrGNN7NL0cA1B+gVeJAOTS3/jDAhR4hcLEPCRQEBAFBYO5loXsIfz1gr5ez+jD5+U4ZuNQgMJfF7rR3TxnqPp+vIwiU+4yYsdCvJhQEBIHlHAQ2P/rYkgeBtw8ebo9OiuXtrvseaI9QOjXPp/svJgjE/UY0rHfaBz2WhQSB+U4HKPM+depMGyLjumWq3/gon0Mw34cECgIgCCAIDM1ORnnnK3bqB50fW9fxL98FnJjxwWMX23HoDqJvnv797YP/1W40Y4p3M+ObBgQBQUAQGLysTi0rU5f1zxnesq2/DD35zM52mSxfM1i+eaD8Pc77X65BoKxT4gP8yuMtnzhePv37coNAPP6YZ5l397NMyucylOuU9VL9yeGCgCCwHILA1A7t4fb3OFS/HKpettFzBYFY9su/7bIzXaLbYk8ZiPuObXfcvkzl9IGvIwiUNyBOTb+LfylBoN75/zIIXJhxqH9Zv8ZpEHGduCym+o2POIKgfJbCsSoi3NV7fcv6QhAAQQBBYNlrv9Kst6FaMf11OuXQu+55dnEUQFzn29WHAkb9j4Hzis75yvMFgRXVIHqu+65re/c2CAJZg0Ask7F8rKh25mMZrJehVdMD4zhctRveStT7aW9AHV+vtaIaeA9azi43CKwYsIO+kMvKO3ftQHv6U8fjOR6tgsBi5h23XzH9CeZxKHOZd3d9FztYcX9XzLNOHLX1kiAwpEcIxLdc9Jbp+Dda/p3+28b/7F8vjvaLy8qOcezAxr/9eh3RX69M7wjHjnz8fNcv/n3BQaAst/XnibTL1hxf67nYINCORbZsm3VqQrnv8hgXcoTAk/Xh/v35bOqvE6Zu89qs59T9KtTyOQL1+qK+H0EABAEEgaGJArHhjMP8uofE1Tv/5WvAarvaDyp7btYhvnF597pTHwL03CXd96DbIAhkDAL18hbLRW2+ZSiWsQh68fex6cN447KYT/2tAN3lLC4btLwv5Bs/yvqi/hTvhV5W7ieeS/2YL3fe5fd4XvH8Bx0CPOg1y7BeEgT2D+W6IKb4tzp1mP6G5rGtT876d9zdPpfLnn9x74x5/eHZ59p3v+vlpP57ff2yDPzh2T/1d3p/Pf0Y6s8UKV/BN+iQ+stZRzw1/XWD9bJZr5sGPe9B8ynrme58yrI9tvWJWR8YGHZJvrAAAASZSURBVFPs9NffulD+H5TTC7rri4WuNwUBBAEQBEAQEARAEBAEhkq8Sx7vqsfRBbUvpr96sBxtMEwicqwY8K0Ecfk/T5+2kIUggCCAIACCgCAAgoAgwEDxrUCxg7xqwNcIx+Xbp48kGLYgEIf5r/rBzOf0r/+xadapGYIACAIIAiAICAIgCAgCab196N32FIH4WtPyFadxCsGgU3KGRTm1KJ7LD2/8STv99M67Z52aIQiAIIAgAIKAIACCgCAAggAIAggCIAgIAiAICAIgCIAggCAAgoAgAIKAIACCAAgCCAIgCAgCIAgIAiAIIAiAIACCgCAAgoAgAIIAggAIAiAICAIgCAgCIAggCIAgAIKAIACCgCAAggCCAAgCIAgIAiAICAIgCCAIgCAAgoAgAIKAIACCAIIAgoAgAIKAIACCgCAAggCCAIIAIAgIAiAICAIgCCAIIAiAICAIAIKAIACCAIIAggAIAoIAIAgIAiAIIAggCIAgIAiAICAIAIIAggCCAAgCggAIAoIACAKCAIIAggAIAoIACAKCAAgCIAggCIAgIAiAICAIgCAAggDLw4G33mt2j7/phYABPvrkZDO240VBAJjl3GfnUweB7OtHmM+F3vTQlp3N2d56AgQBlrUjJz5O/Q4ozGf/xMHUO8Sxw2NAA4NFMMv8DnmsHx6Nd0BPewcUut7vja8fNb5GEGBYbH9+vDf9xUYdKnH0jMP9mmb3+Bvtu4DWD/ClOFw+Yln29UOsJ0UB+NKF6RgQ44fD75/wgiAIMFyD/jj0MVZgJlP2KQb6W3fuc+7ftPicEf8uTKaZ64eP/veklUMVT00m09T02I4XxQAEAYZXVH6TKfvkEHnrB5NpvgnrB5PJ+gFBAAAAAFgSggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEKCAAAAACQkCAAAAEBCggAAAAAkJAgAAABAQoIAAAAAJCQIAAAAQEIRBC6YTCaTyWQymUwmk8lkyjX9P2oQ2r4iBMQpAAAAAElFTkSuQmCC)

To convert the above GitHub hierarchical roles model into the one expected by Hasura, you will need to model roles
as partially captured by the table below which shows permissions for the `user` & `org-member` roles, `repositories` table and `select` operation:

| Role | Access Description | Example repositories table select permission rule |
|---|---|---|
| user | Allow access to personally created repositories |  |
| org-member | Allow access to personally created repositoriesthe organization's repositories |  |


Allow access to personally created repositories

```
{
   "creator_id" :   {
     "_eq" :   "X-Hasura-User-Id"
   }
}
```

Allow access to personally created repositoriesthe organization's repositories

```
{
   "_or" :   [
     {
       "creator_id" :   {
         "_eq" :   "X-Hasura-User-Id"
       }
     } ,
     {
       "organization" :   {
         "members" :   {
           "member_id" :   {
             "_eq" :   "X-Hasura-User-Id"
           }
         }
       }
     }
   ]
}
```

## Permission information availability​

Hasura Engine's permission rules require that information about which roles have access to which objects is available
when processing the permission rule.

Different users with the same role or the same user with different roles may have access to different sets of rows
of the same table.

In some cases this is straightforward - for example, to restrict access for users to only their shopping carts, a
trivial row-level permission like `"user_id": {"_eq": "X-Hasura-User-Id"}` in the shopping carts table `select` permission will suffice.

In others, like in the example below where we need to check whether the user is actually a member of the related
organization. The user information ( *ownership or relationship* ) must be available to define a permission rule.

```
{
   "_or" :   [
     {
       "creator_id" :   {
         "_eq" :   "X-Hasura-User-Id"
       }
     } ,
     {
       "organization" :   {
         "members" :   {
           "member_id" :   {
             "_eq" :   "X-Hasura-User-Id"
           }
         }
       }
     }
   ]
}
```

These non-trivial use cases are to be handled differently based on whether this information is available in the same
database or not.

### Relationship information is available in the same database​

Let's take a closer look at the permission for the `org-member` rule in the example from the previous section. The
rule reads as " *allow access to this data if it was created by this user or if this user is a member of the
organization that it belongs to* ".

The crucial piece of user information that is presumed to be available in the same database and that makes this an
effective rule, is the mapping of users ( *members* ) to organizations.

Since this information is available in the same database, it can be easily leveraged via[ Relationships in permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#relationships-in-permissions)( *see this
reference for another example of the same kind* ).

### Relationship information is not available in the same database​

When this user information is not available in the database that Hasura is configured to use, session variables on
the request are the only way to pass this information to a permission rule. In our example, let's assume the mapping
of users (members) to organizations may not have been available in the same database.

To convey this information, a session variable, say `X-Hasura-Allowed-Organizations` can be passed by your
authentication service to relay this information. We can then check for the following condition to emulate the same
rule: *is the organization that this repository belongs to within the list of the organizations the user is a
member of* .

The permission for the `org-member` role changes to this:

```
{
   "_or" :   [
     {
       "creator_id" :   {
         "_eq" :   "X-Hasura-User-Id"
       }
     } ,
     {
       "organization_id" :   {
         "_in" :   "X-Hasura-Allowed-Organizations"
       }
     }
   ]
}
```

Array session variables in permission rules

Support for using session variables for array operators like `_in` , `_nin` , `_has_any_keys` , `_has_all_keys` is
available in versions `v1.0.0-beta.3` and above.

When you use array operators such as `_in` in the permissions builder in the Hasura Console, it will automatically show
an array builder UI for your values. If your session variable value is already provided array, you can click the `
[X-Hasura-Allowed-Ids]` suggestion to remove the brackets and set your session variable in its place.

## Type formats of session variables​

Session variables are currently expected to only be strings and should be encoded based on Postgres's literals for the
relevant type.

For example, in the above, let's say `creator_id` and `organization_id` columns are of type `integer` , then the
values of `X-Hasura-User-Id` and `X-Hasura-Allowed-Organizations` should be of type `integer` and `integer[]` (an
integer array) respectively. To pass say a value `1` for `X-Hasura-User-Id` , it'll be " `1` " and if the allowed
organizations are `1` , `2` and `3` , then `X-Hasura-Allowed-Organizations` will be " `{1,2,3}` ". `{}` is the syntax for
specifying[ arrays in Postgres ](https://www.postgresql.org/docs/current/arrays.html#ARRAYS-INPUT).

The types and their formats are detailed[ here ](https://www.postgresql.org/docs/current/datatype.html). When in doubt
about the format for a type, you can always test it in the SQL window. To check if `s` is a valid literal for type `t` then, you can check it as follows:

`select   's' ::t ;`

If the above command returns data, then `s` is a valid literal of type `t` . For example, to check if `{hello,world}` is
a valid format of type `text[]` , you can run:

`select   '{hello,world}' :: text [ ] ;`

### What did you think of this doc?

- [ Roles ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#roles)
    - [ The admin role ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#the-admin-role)

- [ Role-based schema publishing ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#role-based-schema-publishing)

- [ Create a new role ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#create-a-new-role)

- [ Delete a role ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#delete-a-role)

- [ Copy a role ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#copy-a-role)
- [ Session variables ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#session-variables)
- [ Model roles in Hasura ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#model-roles-in-hasura)
- [ Permission information availability ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#permission-information-availability)
    - [ Relationship information is available in the same database ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#relationship-information-is-available-in-the-same-database)

- [ Relationship information is not available in the same database ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#relationship-information-is-not-available-in-the-same-database)
- [ Type formats of session variables ](https://hasura.io/docs/latest/auth/authorization/roles-variables/#session-variables/#type-formats-of-session-variables)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)