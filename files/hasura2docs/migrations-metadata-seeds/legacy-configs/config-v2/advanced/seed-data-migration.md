# Create a Seed Data Migration (config v2)

## Use case​

It can be convenient to add some seed data into tables as part of the DB
init process.

## Step 1: Run the Console via the Hasura CLI​

In order to make sure that the Migrations get created, the Console needs
to be run via the Hasura CLI.

## Step 2: Navigate to the SQL section​

On the Hasura Console, click on the `Data` tab and then on the `SQL` link on the left hand side.

## Step 3: Write an insert statement​

The next step is to write an insert statement that populates the
database with seed data like the following:

```
INSERT   INTO  addresses  ( id ,  location )   VALUES
   ( 1 ,   'Bangalore' ) ,
   ( 2 ,   'Tel Aviv' ) ,
   ( 3 ,   'Zurich' ) ;
INSERT   INTO  authors  ( id ,  name ,  address_id )   VALUES
   ( 1 ,   'Sarah' ,   3 ) ,
   ( 2 ,   'Joey' ,   1 ) ,
   ( 3 ,   'Rachel' ,   2 ) ;
INSERT   INTO  articles  ( id ,  title ,  content ,  author_id )   VALUES
   ( 1 ,   'How to make fajitas' ,   'Recipe on making the best fajitas in the world' ,   1 ) ,
   ( 2 ,   'How to climb mount everest' ,   'Guide on successfully climbing the hightest mountain in the world' ,   3 ) ,
   ( 3 ,   'How to be successful on broadway' ,   'What it takes for you to be a successful performer at broadway' ,   2 ) ;
```

## Step 4: Mark the insert as a migration​

Check the box `This is a migration` and give the migration a name, e.g. `insert_seed_data` .

## Step 5: Run the statement​

Hit the `Run!` button.

## Step 6: Verify data & migration​

If the insert statement was successful, the data is now added to the DB.

Navigate to the `migrations` directory in your Hasura Project. The
latest Migration will be the the insert statement that was just run.

### What did you think of this doc?

- [ Use case ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/seed-data-migration/#use-case)
- [ Step 1: Run the Console via the Hasura CLI ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/seed-data-migration/#step-1-run-the-console-via-the-hasura-cli)
- [ Step 2: Navigate to the SQL section ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/seed-data-migration/#step-2-navigate-to-the-sql-section)
- [ Step 3: Write an insert statement ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/seed-data-migration/#step-3-write-an-insert-statement)
- [ Step 4: Mark the insert as a migration ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/seed-data-migration/#step-4-mark-the-insert-as-a-migration)
- [ Step 5: Run the statement ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/seed-data-migration/#step-5-run-the-statement)
- [ Step 6: Verify data & migration ](https://hasura.io/docs/latest/migrations-metadata-seeds/legacy-configs/config-v2/advanced/seed-data-migration/#step-6-verify-data--migration)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)