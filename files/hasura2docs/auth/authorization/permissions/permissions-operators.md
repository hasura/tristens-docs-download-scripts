# Permissions Operators

## Common operators (all column types except json, jsonb)​

| Operator | PostgreSQL equivalent | Description |
|---|---|---|
|  `_ eq`  |  `=`  | Equal to |
|  `_ ne`  |  `<>`  | Not equal to |
|  `_ gt`  |  `>`  | Greater than |
|  `_ lt`  |  `<`  | Less than |
|  `_ gte`  |  `>=`  | Greater than or equal to |
|  `_ lte`  |  `<=`  | Less than or equal to |
|  `_ in`  |  `IN`  | In array |
|  `_ nin`  |  `NOT IN`  | Not in array |
|  `_ is_ null`  |  `IS NULL`  | Is null |


## Logical operators​

| Operator | PostgreSQL equivalent | Description |
|---|---|---|
|  `_ and`  |  `AND`  | Logical `AND`  |
|  `_ or`  |  `OR`  | Logical `OR`  |
|  `_ not`  |  `NOT`  | Logical `NOT`  |


## Exists operator​

| Operator | PostgreSQL equivalent | Description |
|---|---|---|
|  `_ exists`  |  `EXISTS`  | Check for existence |


## String extended operators​

| Operator | PostgreSQL equivalent | Description |
|---|---|---|
|  `_ like`  |  `LIKE`  | Like |
|  `_ nlike`  |  `NOT LIKE`  | Not like |
|  `_ ilike`  |  `ILIKE`  | Case insensitive like |
|  `_ nilike`  |  `NOT ILIKE`  | Case insensitive not like |
|  `_ similar`  |  `SIMILAR TO`  | Similar |
|  `_ nsimilar`  |  `NOT SIMILAR TO`  | Not similar |
|  `_ regex`  |  `~`  | Regular expression match |
|  `_ iregex`  |  `~*`  | Case insensitive regex |
|  `_ nregex`  |  `!~`  | Not regex |
|  `_ niregex`  |  `!~*`  | Not case insensitive regex |


Similar

The SIMILAR TO operator in SQL returns true or false depending on whether its pattern matches the given string. It is
much the same as LIKE, except that it interprets the pattern using SQL99's definition of a regular expression. SQL99's
regular expressions are a curious cross between LIKE notation and common regular expression notation.

## Column comparison operators​

| Operator | Description |
|---|---|
|  `_ ceq`  | Column equal to |
|  `_ cne`  | Column not equal to |
|  `_ cgt`  | Column greater than |
|  `_ clt`  | Column less than |
|  `_ cgte`  | Column greater than or equal to |
|  `_ clte`  | Column less than or equal to |


## JSONB operators​

| Operator | PostgreSQL equivalent | Description |
|---|---|---|
|  `_ is_ null`  |  `IS NULL`  | Is null |
|  `_ contains`  |  `@&gt;`  | Contains (Does the left JSON value contain within it the right value?) |
|  `_ contained_ in`  |  `&lt;@`  | Contained in (Is the left JSON value contained within the right value?) |
|  `_ has_ key`  |  `?`  | Has key (Does the key/element string exist within the JSON value?) |
|  `_ has_ keys_ any`  |  `? |`  | Has keys any (Do any of these key/element strings exist?) |
|  `_ has_ keys_ all`  |  `?&amp;`  | Has keys all (Do all of these key/element strings exist?) |


### What did you think of this doc?

- [ Common operators (all column types except json, jsonb) ](https://hasura.io/docs/latest/auth/authorization/permissions/permissions-operators/#common-operators-all-column-types-except-json-jsonb)
- [ Logical operators ](https://hasura.io/docs/latest/auth/authorization/permissions/permissions-operators/#logical-operators)
- [ Exists operator ](https://hasura.io/docs/latest/auth/authorization/permissions/permissions-operators/#exists-operator)
- [ String extended operators ](https://hasura.io/docs/latest/auth/authorization/permissions/permissions-operators/#string-extended-operators)
- [ Column comparison operators ](https://hasura.io/docs/latest/auth/authorization/permissions/permissions-operators/#column-comparison-operators)
- [ JSONB operators ](https://hasura.io/docs/latest/auth/authorization/permissions/permissions-operators/#jsonb-operators)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)