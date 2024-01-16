# Allow List of Operations

## Introduction​

The **Allow List** is a list of safe operations ( *GraphQL queries, mutations or subscriptions* ) that is stored by the
GraphQL Engine in its Metadata. When enabled, it can be used to restrict the GraphQL Engine so that it executes **only** those operations that are present in the list.

## Enable Allow List​

Allow-list validation can be enabled by setting the `HASURA_GRAPHQL_ENABLE_ALLOWLIST` environment variable to `true` or
running the GraphQL Engine with the `--enable-allowlist` flag ( *default value is*  `false` ). See[ reference docs ](https://hasura.io/docs/latest/deployment/graphql-engine-flags/reference/#command-flags).

Note

Allow-list validation will not be enforced for the `admin` role.

## Open Allow List manager​

Head to the `API` tab and find the `Allow List` section in the Console.

Image: [ AllowList manager ](https://hasura.io/docs/assets/images/allowlist-manager-401cff2d7ab16ab6065c4691402d9ad7.png)

## Adding or removing an operation in Allow List​

- Console
- CLI
- API


Head to the `API` tab and find the `Allow List` section in the Console.

- **Write operation** : You can add an individual operation, like the one below, manually to the Allow List. These
operations require unique names. This unique name is used an identifier for the query in the collection, it is not
related to the operation name of the query.


```
query   ( $id :   Int ! )   {
   user_by_pk ( id :   $id )   {
     __typename
     id
     name
     company
   }
}
```

After writing your query or selecting a query from quick add dropdown menu, click `Add Operation` .

Image: [ Add operation ](https://hasura.io/docs/assets/images/write-operation-8d39113885733a207105979d47a60a42.png)

- **Upload File** : Alternatively, you can upload files, like this[ sample file ](https://gist.github.com/dsandip/8b1b4aa87708289d4c9f8fd9621eb025), to add multiple operations to the
Allow List. Each operation in the file will need a unique name. Once you've selected your file, click `Add Operation` .


Image: [ Upload operation ](https://hasura.io/docs/assets/images/upload-operation-1a23237b117cceddcc33179ef6fdad0b.png)

Head to the `/metadata/databases/query_collections.yaml` file and add the database configuration as below:

```
-   name :  allowed - queries
   definition :
     queries :
       -   name :  bv
         query :   | -
          query MyQuery  {
            test  {
              age
              id
             }
           }
       -   name :  operation_name
         query :   | -
          query MyQuery  {
            test  {
              age
              id
             }
           }
```

Apply the Metadata by running:

`hasura metadata apply`

Queries can be stored in collections and a collection can be added to or removed from the Allow List. See[ Collections & Allow List APIs ](https://hasura.io/docs/latest/api-reference/metadata-api/query-collections/)for API reference.

Note

- Allow List queries are validated against the schema. Adding an invalid query will result in an inconsistent Metadata
error.
- `__typename` introspection fields will be ignored when adding operations and comparing them to the Allow List.
- Any introspection queries that your client apps require must be explicitly added to the Allow List to allow running
them.
- The order of fields in a query will be **strictly** compared. E.g. assuming the query in the first example above is
part of the Allow List, the following query will be **rejected** :


Allow List queries are validated against the schema. Adding an invalid query will result in an inconsistent Metadata
error.

 `__typename` introspection fields will be ignored when adding operations and comparing them to the Allow List.

Any introspection queries that your client apps require must be explicitly added to the Allow List to allow running
them.

The order of fields in a query will be **strictly** compared. E.g. assuming the query in the first example above is
part of the Allow List, the following query will be **rejected** :

```
query   ( $id :   Int ! )   {
   user_by_pk ( id :   $id )   {
     __typename
     name
     id
     company
   }
}
```

- The Allow List is stored in Hasura's Metadata. To version control the state of the list, you are required to export
the Metadata. See[ Managing Hasura Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/)for more details.
- You can modify the Allow List without actually enabling it on your instance.


The Allow List is stored in Hasura's Metadata. To version control the state of the list, you are required to export
the Metadata. See[ Managing Hasura Metadata ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-metadata/)for more details.

You can modify the Allow List without actually enabling it on your instance.

## Role-based Allow List​

A role-based Allow List is useful when you would like a query collection(s) to be accessible to only certain roles.

Note

Server support for Role-based Allow Lists in Cloud/Enterprise products is available from version `v2.3` and Console
support is available from version `v2.13` . In OSS, role-based entries are ignored.

On older versions (which do not support role-based Allow Lists), any role-based Allow List Metadata entry will be
treated as global. Hence, caution is advised when using role-based Allow List Metadata with older versions.

- Console
- CLI
- API


Head to the `API` tab and find the `Allow List` section on the Console. On the left side bar, you can see a list of
query collections. After selecting a query collection, you can enable the roles which should have access to any query
collection via the `Permissions` tab.

Image: [ Role based allow list ](https://hasura.io/docs/assets/images/role-based-allow-list-ddf325b1fbb373fe6eb9b79b3c1c674c.png)

Head to the `/metadata/databases/allow_list.yaml` file and add the database configuration as below:

```
query_collections :
   -   name :  allowed - queries
     definition :
       queries :   [ ]
   -   name :  editor_allowed_queries
     definition :
       queries :   [ ]
   -   name :  user_allowed_queries
     definition :
       queries :   [ ]
allowlist :
   -   collection :  allowed - queries
     scope :
       global :   true
   -   collection :  editor_allowed_queries
     scope :
       global :   false
       roles :
         -  editor
   -   collection :  user_allowed_queries
     scope :
       global :   false
       roles :
         -  user
```

Apply the Metadata by running:

`hasura metadata apply`

You can update the roles in the Allow List by using the[ update_scope_of_collection_in_allowlist ](https://hasura.io/docs/latest/api-reference/metadata-api/query-collections/#metadata-update-scope-of-collection-in-allowlist)Metadata API.

## Quick-create allowed operations​

### Hasura Cloud​

This feature lets you add to the Allow List with one click from the record of past operations. (With Hasura GraphQL
Engine CE, Allow Lists must be managed manually).

Image: [ Hasura Cloud Console create new allowed operation ](https://hasura.io/docs/assets/images/allowlist-add-new-op-96e412ee9fdcdf30e73ec7f5bdb5eacf.png)

## Recommended usage​

The following are the recommended best practices for enabling/disabling Allow-List-based validation:

- **In development instances** : During development or in dev instances, disable the Allow List ( *default setting* ) to
enable complete access to the GraphQL schema. Add/remove operations in the Allow List and then export the Metadata for
version-control ( *so you can apply it to other instances* ).
- **In CI/CD instances** : Enable the Allow List for testing.
- **In production instances** : Enabling the Allow List is highly recommended when running the GraphQL Engine in
production.


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/security/allow-list/#enable-allow-list/#introduction)
- [ Enable Allow List ](https://hasura.io/docs/latest/security/allow-list/#enable-allow-list/#enable-allow-list)
- [ Open Allow List manager ](https://hasura.io/docs/latest/security/allow-list/#enable-allow-list/#open-allow-list-manager)
- [ Adding or removing an operation in Allow List ](https://hasura.io/docs/latest/security/allow-list/#enable-allow-list/#adding-or-removing-an-operation-in-allow-list)
- [ Role-based Allow List ](https://hasura.io/docs/latest/security/allow-list/#enable-allow-list/#role-based-allow-list)
- [ Quick-create allowed operations ](https://hasura.io/docs/latest/security/allow-list/#enable-allow-list/#quick-create-allowed-operations)
    - [ Hasura Cloud ](https://hasura.io/docs/latest/security/allow-list/#enable-allow-list/#hasura-cloud)
- [ Recommended usage ](https://hasura.io/docs/latest/security/allow-list/#enable-allow-list/#recommended-usage)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759811/main-web/Group_11455_3_azgk7w.png)

### Securing your API with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)