# Permissions Examples

## Introduction​

This is a guide to help you set up a basic authorization architecture for your GraphQL fields. It is recommended that
you first check out[ Roles & Session variables ](https://hasura.io/docs/latest/auth/authorization/roles-variables/)and other pages in[ configuring permission rules ](https://hasura.io/docs/latest/auth/authorization/permissions/)which will be referred to throughout this
guide.

Here are some examples of common use cases.

## Unauthorized users​

Unauthorized users are those which are[ unauthenticated or not logged in ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/)and thus default to the defined
unauthorized role. Requests from these users will typically have no officially identifiable session variables.
Follow these steps in order to create permission rules for an anonymous user.

- Create a role called `anonymous` (this name is up to you, you could call the role `public` or anything else).
- We'll be adding `select` permissions. Generally, for security, you wouldn't be adding `insert` , `update` , or `delete` permissions.
- For the `select` permission condition, create a valid condition depending on your data model. For example, `is_published: {_eq: true}` or if you don't have a condition, then just set the permission to `Without any checks` ,
which is represented by an empty set of braces `{}` .
- Choose the right set of columns that will get exposed in the GraphQL schema as fields. Ensure that sensitive columns
are not exposed.


### Example​

Here's an example of allowing the defined unauthorized role, named in this case: `anonymous` , to query the `products` table for only rows where the `is_published` column is set to `true` .

Image: [ Access control for an anonymous role ](https://hasura.io/docs/assets/images/anonymous-role-example__permissions_2.16.1-7ee3dc92b18c6b31823996e5200b89c1.png)

We are also limiting the columns which can be returned by the query. If we wanted to allow the `anonymous` role to
be able to query the `products` table for all rows, we would simply set the "Row select permissions" to "Without any
checks".

See[ Unauthenticated / Public access ](https://hasura.io/docs/latest/auth/authentication/unauthenticated-access/)for steps to configure the
unauthorized user role in Hasura.

## Logged-in users​

- Create a role called `user` .
- Permissions in this case make use of a `user_id` or a `owner_id` column.
- Set up a permission for an `insert/select/update/delete` operation that uses said column. E.g.: `user_id: {_eq: "X-Hasura-User-Id"}` for a profile or shopping carts table.
- Note that the `X-Hasura-User-Id` is a[ dynamic session variable ](https://hasura.io/docs/latest/auth/authorization/roles-variables/)that is
set and returned from your[ auth service ](https://hasura.io/docs/latest/auth/authentication/index/), or as a request header.


### Example​

Here's an example of creating a permission which allows only users to access their own shopping carts. The `user_id` column is a column in the `carts` table which stores the `id` of the user who created it. We are restricting
access to rows of this table to requests which contain the same user id in the `X-Hasura-User-Id` session variable.

Image: [ Access control for a logged-in user ](https://hasura.io/docs/assets/images/set-user-permissions_step-1_permissions_2.16.1-f4120fbe12d1178c6cd260824b5b7348.png)

Now we can test out a query to see that when posing as that user, we can access only their carts and not those of
other users.

Image: [ API testing for a logged-in user ](https://hasura.io/docs/assets/images/set-user-permissions_step-2_permissions_2.16.1-19da26c8ee59a6d89feda2a38be4870e.png)

Posing as a user in testing

In development, if you're testing your logged-in users' access and aren't utilizing authenticated tokens, you must
include the `X-Hasura-Admin-Secret` header. You can[ learn more about this here ](https://hasura.io/docs/latest/auth/authentication/admin-secret-access/).

## Same table ownership information​

Suppose you have a multi-tenant application where a manager of a particular organization should be able to see all the
data that belongs to that particular organization. In this case, the particular table might have an id column
which denotes the organization.

Let's say we have an online store where each vendor on the store has its own products. We want to allow the manager
of a vendor to be able to see all the products that belong to that vendor and the indentifying `vendor_id` is saved
on the `products` table itself.

- Create a role called `manager` .
- Create a permission for `select` in the products table, which has the condition: `vendor_id: {_eq:
"X-Hasura-Vendor-Id"}` .
- `X-Hasura-Vendor-Id` is a[ session variable ](https://hasura.io/docs/latest/auth/authorization/roles-variables/)which is set and returned by
your[ auth service ](https://hasura.io/docs/latest/auth/authentication/index/)for an incoming request.


Image: [ Access control for a manager of an vendor ](https://hasura.io/docs/assets/images/same-table-ownership_step-1_permissions_2.16.1-19521cd3a963149b29b439578bb6f36c.png)

Image: [ GraphQL query for a manager of an vendor ](https://hasura.io/docs/assets/images/same-table-ownership_step-2_permissions_2.16.1-d610fb3030abf806584fc6ffafde5134.png)

## Related table ownership information​

Let's say the ownership or visibility information for a data model (table) is not present as a column in the table,
but in a different related table.

For example, suppose that in a products table we have a `added_by_user_id` column which stores the `id` of the user who
added the product but no `vendor_id` column on the table itself.

However, we want to allow other members of the vendor to be able to access the product too. We have another related
table `users_in_vendors` which associates users with vendors. The relationship from the `product` to the `users_in_vendors` table is named `userInVendorByUserId` and is configured as: `products.added_by_user_id  →
users_in_vendors.user_id` .

We can use this relationship to check that the `X-Hasura-Vendor-Id` on the incoming request session variable matches
the vendor which the user that added the product is a member of and therefore allow other members of the vendor
organization to access the product.

- Create a relationship called `userInVendorByUserId` from the product table.
    - Object relationship (product has only a single user which added it): `products.added_by_user_id  →
users_in_vendors.user_id` .
- Create a role called `manager` .
- Create a select permission on the `products` table, which has the condition: `{"userInVendorByUserId":{"vendor_id":{"_eq":"X-Hasura-Vendor-Id"}}}` .
    - This reads as: Allow the role `manager` to select if `users_in_vendors.vendor_id` has a `vendor_id` equal to
that of `X-Hasura-Vendor-Id` session variable on the incoming request.


Image: [ Different table ownership permissions ](https://hasura.io/docs/assets/images/different-table-ownership_step-1_permissions_2.16.1-90fb1a575388a71ec16582324d5bb7c4.png)

Image: [ Different table ownership permissions ](https://hasura.io/docs/assets/images/different-table-ownership_step-2_permissions_2.16.1-748acc824bf83cff9480d6afc560b8e6.png)

## Multiple roles per user​

Sometimes your data model requires that:

- Users can have multiple roles.
- Each role has access to different parts of your database schema.


If you have the information about roles and how they map to your data in the same database as the one configured with
the Hasura Engine, you can leverage relationships to define permissions that effectively control access to data and the
operations each role is allowed to perform.

To understand how this works, let's model the roles and corresponding permissions in the context of a blog app with the
following roles:

- `author` : Users with this role can **submit their own articles** .
- `reviewer` : Users with this role can **review articles assigned to them** and add a review comment to each
article. A mapping of articles to reviewers is maintained in the `reviewers` table.
- `editor` : Users with this role can edit and **publish any article** . They can also **leave a private rating for each
article** . However, they **cannot overwrite a reviewer's notes** . A list of editors is maintained in the `editors` table.


### Database Schema​

The following is a reference database schema for our example:

Image: [ Database schema example for multiple roles per user ](https://hasura.io/docs/assets/images/multirole-example-db-schema-0c8e46769b3bb3d8a4efa0d7281b0308.png)

Based on the above schema, we'll create the following tables:

```
-- user information from your auth system
users  (
  id  INT   PRIMARY   KEY ,
  name  TEXT ,
  profile JSONB ,   -- some profile information like display_name, etc.
  registered_at  TIMESTAMP   -- the time when this user registered
)
-- information about articles
articles  (
  id  INTEGER   PRIMARY   KEY ,
  title  TEXT ,
  author_id  INT   REFERENCES  users ( id ) ,   -- Foreign key to users :: id
  is_reviewed  BOOLEAN   DEFAULT   FALSE ,
  review_comment  TEXT ,
  is_published  BOOLEAN   DEFAULT   FALSE ,
  editor_rating  INTEGER
)
-- mapping of reviewers to articles
reviewers  (
  id  INTEGER   PRIMARY   KEY ,
  article_id  INTEGER   REFERENCES  articles ( id ) ,   -- Foreign key to articles :: id
  reviewer_id  INTEGER   REFERENCES  users ( id )   -- Foreign key to users :: id
)
-- a  list of editors
editors  (
  editor_id  INTEGER   PRIMARY   KEY   REFERENCES  users ( id )   -- Foreign key to users :: id
)
```

### Relationships​

Create an array relationship named `reviewers` based on the foreign key constraint `reviewers` :: `article_id` → `articles` :: `id` :

Image: [ Create an array relationship ](https://hasura.io/docs/assets/images/multirole-example-reviewers-array-relationship-df7096be608e9f08acb733750ec920db.png)

### Permissions​

The following is an example summary of the access control requirements for the `articles` table based on the above
schema:

| Client Name | author | reviewer | editor |
|---|---|---|---|
| insert | select | update | select | update | select |
|---|---|---|---|---|---|
| id | ✔ | ✔ | ✖ | ✔ | ✖ | ✔ |
| title | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| author_id | ✔ | ✔ | ✖ | ✔ | ✖ | ✔ |
| is_reviewed | ✖ | ✔ | ✔ | ✔ | ✔ | ✔ |
| review_comment | ✖ | ✔ | ✔ | ✔ | ✖ | ✔ |
| is_published | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ |
| editor_rating | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ |


 *Additional restrictions are required to ensure that a user with the role*  `author`  *can submit only their own article
i.e.*  `author_id`  *should be the same as the user's id* .

We'll create permission rules for the roles and Actions listed above ( *you can easily extend them for the Actions not
documented here* ) .

#### Permissions for role author​

`author`

- **Allow users with the role**  `author`  **to insert only their own articles** For this permission rule, we'll make use of two features of the GraphQL Engine's permissions system:
    - [ Column-level permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/column-level-permissions/): Restrict access to
certain columns only.

- [ Column presets ](https://hasura.io/docs/latest/schema/postgres/default-values/column-presets/): Session-variable-based column preset for the `author_id` column to automatically insert the user's ID i.e. the `X-Hasura-User-Id` session-variable's value. It
also helps us avoid explicitly passing the user's ID in the insert mutation.


 **Allow users with the role**  `author`  **to insert only their own articles** 

For this permission rule, we'll make use of two features of the GraphQL Engine's permissions system:

Image: [ Permissions for the role author ](https://hasura.io/docs/assets/images/multirole-example-author-insert-c8cf0c857c18ddeaa8dd5fdf15b900db.png)

Notice how we don't need to have an explicit row-level permission ( *a custom check* ) as only authenticated users with
the role `author` can perform this action. As we have a column preset for the `author_id` column that automatically
takes the author's ID ( *and the*  `id`  *column is an auto-increment integer field* ), we only need to allow access to the `title` column.

- **Allow users with the role**  `author`  **to select certain columns only**


Again, we'll use **column-level** permissions to restrict access to certain columns. Additionally, we need to define
row-level permissions ( *a custom check* ) to restrict access to only those articles authored by the current user:

Image: [ Column access for the role author ](https://hasura.io/docs/assets/images/multirole-example-author-select-2bf50d8b2668298d251fda5f2445944f.png)

The row-level permission rule shown here translates to " *if the value in the*  `author_id`  *column of this row is equal
to the user's ID i.e. the* X-Hasura-User-Id _session-variable's value, allow access to it* ".

`X-Hasura-User-Id`

#### Permissions for role reviewer​

`reviewer`

- **Allow users with the role**  `reviewer`  **to update articles assigned to them for reviews** For this use-case, we'll use[ relationship or nested-object permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#relationships-in-permissions)based on the array relationship `reviewers` to restrict access to assigned articles only.


 **Allow users with the role**  `reviewer`  **to update articles assigned to them for reviews** 

For this use-case, we'll use[ relationship or nested-object permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/row-level-permissions/#relationships-in-permissions)based on the array relationship `reviewers` to restrict access to assigned articles only.

Image: [ Permissions for the role reviewer ](https://hasura.io/docs/assets/images/multirole-example-reviewer-update-aea48d86abf91bee1804accc6c864c5a.png)

The array-relationship based permission rule in the above image reads as " *if the ID of any reviewer assigned to
this article is equal to the user's ID i.e. the X-Hasura-User-Id session-variable's value, allow access to it* ".
The columns' access is restricted using the column-level permissions highlighted above.

`X-Hasura-User-Id`

- **Allow users with the role**  `reviewer`  **to select articles assigned to them for reviews** This permission rule is pretty much the same as the one for update, the only difference being the column-level
permissions.


 **Allow users with the role**  `reviewer`  **to select articles assigned to them for reviews** 

This permission rule is pretty much the same as the one for update, the only difference being the column-level
permissions.

Image: [ Column access for the role reviewer ](https://hasura.io/docs/assets/images/multirole-example-reviewer-select-8dc78895eebc1cb56a741d21309aa25b.png)

#### Permissions for role editor​

`editor`

- **Allow editors to select any article's data** This is a straightforward rule - there's no need for any row-level permissions since editors have access to all rows
and they can *read* all columns.


 **Allow editors to select any article's data** 

This is a straightforward rule - there's no need for any row-level permissions since editors have access to all rows
and they can *read* all columns.

Image: [ Permissions for the role editor ](https://hasura.io/docs/assets/images/multirole-example-editor-select-1e89f4e4cd3d8940586e3e6fa188255f.png)

- **Allow editors to update an article** There's no need for row-level permissions in this case either but we need to restrict access to certain columns only:


 **Allow editors to update an article** 

There's no need for row-level permissions in this case either but we need to restrict access to certain columns only:

Image: [ Column access for the role editor ](https://hasura.io/docs/assets/images/multirole-example-editor-update-c8c12991a505d55dd1dad38c3d55956a.png)

## Multiple Permissions for the Same Role​

In some cases we might want to allow access to certain columns for a role only if a condition is met, while
allowing access to other columns based on a different condition.

Currently, it is not possible to define multiple column & row permission combinations for the same role. However, we
can work around this limitation by using[ views ](https://hasura.io/docs/latest/schema/postgres/views/).

 **Example** 

Let's say for privacy reasons we only want users to be able to access their own `email` , `phone` and `address` but
allow all users to access each others `name` and `city` information.

We have a table called `user_profile` with columns `(id, name, city, email, phone, address)` and we want the role `user` to be able to access:

- all columns only if the `id` column is the requesting user's id, i.e. the current user is the "owner" of the row.
- only the `id` , `name` and `city` columns for all other users.


We can achieve this via the following steps:

### Step 1: Create a view​

[ Create a view ](https://hasura.io/docs/latest/schema/postgres/views/#pg-create-views)called `user_profile_private` with columns `(user_id, email, phone, address)` :

```
CREATE   VIEW  user_profile_private  AS
   SELECT  id  AS  user_id ,  email ,  phone ,  address
     FROM  user_profile ;
```

Image: [ Create a view ](https://hasura.io/docs/assets/images/multiple-permissions-per-role_step-1_create-a-view_2.16.1-cd69bf9112a5cb996debd0b531f24b72.png)

### Step 2: Create a relationship​

For the table `user_profile` ,[ create a manual object relationship ](https://hasura.io/docs/latest/schema/postgres/table-relationships/create/#pg-create-manual-relationships)called `user_profile_private` using `user_profile.id -> user_profile_private.user_id` :

Image: [ Create a manual object relationship ](https://hasura.io/docs/assets/images/multiple-permissions-per-role_step-2_create-a-relationship_2.16.1-748b46f1f5a39762ea642d76b60d510d.png)

### Step 3: Define permissions​

On the `user_profile` table for the role `user` , create the following permissions for `select` :

- allow access to `id` , `name` and `city` without any row conditions.


Image: [ Column access for the role user ](https://hasura.io/docs/assets/images/multiple-permissions-per-role_step-3_define-public-permissions_2_16_1-80096ee017a3e49b2c0c9dcd07bf970e.png)

- On the `user_profile_private` view allow access to `id` , `phone` , `email` and `address` if the `user-id` passed
in the session variable is equal to the row's `user_id` .


Image: [ Column access for the role user based on row level permissions ](https://hasura.io/docs/assets/images/multiple-permissions-per-role_step-4_define-private-permissions_2.16.1-3751c0ad9a679df3e0489b4557630e30.png)

### Step 4: Query with appropriate access control​

Now we can fetch the required data with the appropriate access control by using the relationship.

If the `X-Hasura-Role` and the `X-Hasura-User-Id` session variables are set to `user` and `2` respectively (and the `X-Hasura-Admin-Secret` value is set to allow us to pose as the user), we'll get the following result:

Image: [ Column access for the role user based on row level permissions ](https://hasura.io/docs/assets/images/multiple-permissions-per-role_step-5_query-the-api_2.16.1-109203bd5db1096e05bc6f17f54d51ea.png)

Observe that the `user_profile_private` field is returned as `null` for all rows without the appropriate access.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#introduction)
- [ Unauthorized users ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#unauthorized-users-example)
    - [ Example ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#example)
- [ Logged-in users ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#logged-in-users)
    - [ Example ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#example-1)
- [ Same table ownership information ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#same-table-ownership-information)
- [ Related table ownership information ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#related-table-ownership-information)
- [ Multiple roles per user ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#nested-object-permissions-example)
    - [ Database Schema ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#database-schema)

- [ Relationships ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#relationships)

- [ Permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#permissions)
- [ Multiple Permissions for the Same Role ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#multiple-permissions-for-the-same-role)
    - [ Step 1: Create a view ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#step-1-create-a-view)

- [ Step 2: Create a relationship ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#step-2-create-a-relationship)

- [ Step 3: Define permissions ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#step-3-define-permissions)

- [ Step 4: Query with appropriate access control ](https://hasura.io/docs/latest/auth/authorization/permissions/common-roles-auth-examples/#unauthorized-users-example/#step-4-query-with-appropriate-access-control)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)