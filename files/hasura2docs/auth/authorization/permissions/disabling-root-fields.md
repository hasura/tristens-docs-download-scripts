# Root Field Visibility

## Introduction​

Sometimes you may want a role to only have access to certain root fields of a table or have the table only be
accessible through a[ relationship ](https://hasura.io/docs/latest/schema/postgres/table-relationships/index/).

When you track a table in Hasura Engine, all the GraphQL root fields available to the role are exposed. Ie: Under
the `query` root field: `select` , `select_by_pk` and `select_aggregate` are exposed. Under the `subscription` root field, `select` , `select_by_pk` , `select_aggregate` and `select_stream` are exposed. Root field visibility can
disable specific query and subscription root fields.

Supported from

Root field visibility is supported in version `v2.8.0` and above.

- Console
- CLI
- API


You can disable specific root fields for queries and subscriptions by unchecking them in the Select permission for the
table and role in Console. This is located in the Console under **Data -> {table} -> Permissions -> {role} ->
select -> Root fields permissions ** 

Image: [ Disable root fields in Hasura Console ](https://hasura.io/docs/assets/images/disable-root-fields_console_2.11.1-2d972f71649e58dbfbdee0abd22b6e94.png)

You can disable root fields for queries and subscriptions specifying which are available for the `select_permissions` by
updating the specific `metadata -> databases -> [database-name] -> tables -> [table-name].yaml` file eg:

```
table :
   name :  users
   schema :  public
select_permissions :
   -   role :  user
     permission :
       columns :
         -  id
       filter :   { }
       query_root_fields :
         -  select_by_pk
       subscription_root_fields :
         -  select
         -  select_by_pk
         -  select_aggregate
delete_permissions :
   -   role :  user
   permission :
     backend_only :   true
     filter :   { }
```

Nulls and empty arrays

Setting the value of `query_root_fields` or `subscription_root_fields` to `null` or not defining it at all implies that
all fields are allowed and an empty array means no fields are allowed.

You can disable root fields for Select permissions with the

[ permissions Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/permission/)by specifying which should be available in
the `query_root_fields` and `subscription_root_fields` arrays, eg:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type"   :   "pg_create_select_permission" ,
   "args"   :   {
     "table"   :   "users" ,
     "role"   :   "user" ,
     "source" :   "default" ,
     "permission"   :   {
       "columns"   :   "*" ,
       "filter"   :   {
         "is_public" :   true
       } ,
       "query_root_fields" :   [ "select_by_pk" ] ,
       "subscription_root_fields" :   [ "select" ,   "select_by_pk" ]
     }
   }
}
```

Nulls and empty arrays

Setting the value of `query_root_fields` or `subscription_root_fields` to `null` or not defining it at all implies that
all fields are allowed and an empty array means no fields are allowed.

## Root field visibility use cases​

### Allow a table to be accessible only through a relationship​

Let's say we have two tables, `categories` and `products` defined as follows:

| Table | Columns | Relationships |
|---|---|---|
| categories |  `id` , `name`  | products (array relationship) |
| products |  `id` , `name` , `description` , `price`  | category (object relationship) |


We would like to configure permissions of the `guest` role such that they are only able to access the `products` of the `categories` which they can access i.e. access the `products` table only through the `categories` -> `products` relationship.

Modifying the select permission of the `products` table:

Image: [ Disable root fields in Hasura Console ](https://hasura.io/docs/assets/images/disable-all-root-fields_console_2.11.1-17d9dedb729ba97d56be1fe016048b2e.png)

Now that no `query_root_fields` or `subscription_root_fields` are enabled, the `guest` role won't be able to access
the `products` table directly and can only access the `products` table through the `categories` -> `products` relationship.

Image: [ Query with disabled root fields ](https://hasura.io/docs/assets/images/authorization_root-field-visibility-api-query_2-16-9b180094caf0453d63c829d05e0479ad.png)

Row permission considerations

If root fields are disabled then you may want to simplify the row filter permissions by giving it "without any checks"
access to all rows. But you should be cautious here because the field may be accessible through a different type e.g.
the `returning` field in a mutation output type.

### Access only via primary key​

Let's say you want to allow a client to fetch data from a table only if the client knows the primary key of a row in
that table.

In this case, regardless of the permission on the table, only `<table>_by_pk` should be exposed in `query_root` .

Image: [ Disable select root fields in Hasura Console ](https://hasura.io/docs/assets/images/disable-select-root-fields_console_2.11.1-033a0655f1a52605cf2be381c9eddef1.png)

### Disable subscription fields​

Allow a role to only be able to make query and not subscription requests.

Image: [ Disable subscription root fields in Hasura Console ](https://hasura.io/docs/assets/images/disable-subscription-root-fields_console_2.11.1-bf0f7a4860bda940105cd0f0811aa742.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authorization/permissions/disabling-root-fields/#introduction)
- [ Root field visibility use cases ](https://hasura.io/docs/latest/auth/authorization/permissions/disabling-root-fields/#root-field-visibility-use-cases)
    - [ Allow a table to be accessible only through a relationship ](https://hasura.io/docs/latest/auth/authorization/permissions/disabling-root-fields/#allow-a-table-to-be-accessible-only-through-a-relationship)

- [ Access only via primary key ](https://hasura.io/docs/latest/auth/authorization/permissions/disabling-root-fields/#access-only-via-primary-key)

- [ Disable subscription fields ](https://hasura.io/docs/latest/auth/authorization/permissions/disabling-root-fields/#disable-subscription-fields)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)