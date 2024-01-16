# Create a Hasura Seed Data Migration

## Use case​

It's often useful to add some initial Seed data into your database as part of the initialization process, with Hasura
Seeds you can do that. This is particularly useful for adding a testing user or to pre-populate values if you have set a
table in Hasura as an enum table to expose it as GraphQL enums in the GraphQL API.

## Create a Hasura Seed file​

You can use the Hasura CLI to automatically create Seed files for you based on the data which is already in a table in a
database.

`hasura seed create myAuthorsSeed --from-table author`

Select the database containing the table you've specified.

`? Select a database to use`

CLI will log

`INFO created seed file successfully     file=/Users/me/myDemoProject/seeds/default/1656499378904_myAuthorsSeed.sql`

If you open the file created you will see standard pure SQL insert statements with the data contained in the database.
Eg:

```
SET  check_function_bodies  =   false ;
INSERT   INTO   public . author  ( id ,  name )   VALUES   ( '1' ,   'Woolf' ) ;
INSERT   INTO   public . author  ( id ,  name )   VALUES   ( '2' ,   'Tolkien' ) ;
INSERT   INTO   public . author  ( id ,  name )   VALUES   ( '3' ,   'Austen' ) ;
INSERT   INTO   public . author  ( id ,  name )   VALUES   ( '4' ,   'Orwell' ) ;
```

Want to generate seed data for a table that doesn't exist yet?

You can still use the `hasura seed create` command! Simply leave off the `--from-table` flag and accompanying argument,
and Hasura will launch an editor in which you can write your own SQL statements. Upon saving and quitting the editor,
Hasura will create a seed file for you in the `/seeds/default` directory.

## Apply a Hasura Seed file​

To apply a seeds file to your Hasura instance you can use the `apply` Hasura CLI command. Eg:

`hasura seed apply --file 1656499378904_myNewAuthorsSeed.sql`

If you do not specify a database with the `--database-name` flag then the CLI will prompt you to choose the database to
apply the seeds to and as long as there are no conflicts and the SQL executes successfully to input the data then the
CLI will log:

`INFO Seeds planted`

Success!

### What did you think of this doc?

- [ Use case ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-seeds/#use-case)
- [ Create a Hasura Seed file ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-seeds/#create-a-hasura-seed-file)
- [ Apply a Hasura Seed file ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-seeds/#apply-a-hasura-seed-file)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)