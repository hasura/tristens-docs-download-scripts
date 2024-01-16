# MS SQL Server: Create Relationships

## Introduction​

A relationship from one table/view to another can be created by defining a link between a column of the table/view to a
column of the other table/view.

Typically, relationships between tables are defined using foreign-key constraints. But in some cases, it might not be
possible to use foreign-key constraints to create the relationship. For example, while trying to create a relationship
involving a view or Native Query since foreign-keys cannot be created on them.

## Using foreign keys​

Say we created two tables, `authors(id, name)` and `articles(id, title, content, rating, author_id)` .

Let us now connect these tables to enable nested queries using a foreign-key:

### Step 1: Add foreign-key constraint​

Let's add a foreign-key constraint to the `author_id` column in the `articles` table.

- Console
- CLI
- API


In the Console, navigate to the `Modify` tab of the `articles` table. Click the `Add` button in the Foreign Keys section
and configure the `author_id` column as a foreign-key for the `id` column in the `authors` table:

Image: [ Add foreign-key constraint ](https://hasura.io/docs/assets/images/add-foreign-key-mssql-856d3bd3a8c7c2a05752db99e4840723.png)

[ Create a migration manually ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#create-manual-migrations)and add the
following SQL statement to the `up.sql` file:

```
ALTER   TABLE  articles
ADD   FOREIGN   KEY   ( author_id )   REFERENCES  authors ( id ) ;
```

Add the following statement to the `down.sql` file in case you need to[ roll back ](https://hasura.io/docs/latest/migrations-metadata-seeds/manage-migrations/#roll-back-migrations)the above statement:

```
ALTER   TABLE  articles
DROP   CONSTRAINT  articles_author_id_fkey ;
```

Apply the migration by running:

`hasura migrate apply`

You can add a foreign-key constraint using the[ schema_run_sql Metadata API ](https://hasura.io/docs/latest/api-reference/schema-api/run-sql/#schema-run-sql):

```
POST   /v2/query   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "run_sql" ,
   "args" :   {
     "source" :   "<db-name>" ,
     "sql" :   "ALTER TABLE articles ADD FOREIGN KEY (author_id) REFERENCES authors(id);"
   }
}
```

### Step 2: Create an object relationship​

Each article has one author. This is an `object relationship` .

- Console
- CLI
- API


The Console infers potential relationships using the foreign-key created above and recommends these in the `Relationships` tab of the `articles` table.

Add an `object relationship` named `author` for the `articles` table as shown here:

Image: [ Create an object relationship ](https://hasura.io/docs/assets/images/add-1-1-relationship-dddde9ddc6a81292928ee7d5b665288c.png)

You can add an object relationship in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  articles
   object_relationships :
     -   name :  author
       using :
         foreign_key_constraint_on :  author_id
-   table :
     schema :  public
     name :  authors
```

Apply the Metadata by running:

`hasura metadata apply`

You can create an object relationship by using the[ mssql_create_object_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#mssql-create-object-relationship)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_create_object_relationship" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "table" :   "articles" ,
     "name" :   "author" ,
     "using" :   {
       "foreign_key_constraint_on"   :   [ "author_id" ]
     }
   }
}
```

We can now run a nested object query that is based on this `object relationship` .

Fetch a list of articles and each article's author:

### Step 3: Create an array relationship​

An author can write multiple articles. This is an `array relationship` .

You can add an `array relationship` in the same fashion as an `object relationship` as shown above.

- Console
- CLI
- API


On the Console, add an `array relationship` named `articles` for the `authors` table as shown here:

Image: [ Create an array relationship ](https://hasura.io/docs/assets/images/add-1-many-relationship-379651c4384a8ca912e70b284d32ec88.png)

We can now run a nested object query that is based on this `array relationship` .

You can add an array relationship in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  articles
   object_relationships :
     -   name :  author
       using :
         foreign_key_constraint_on :  author_id
-   table :
     schema :  public
     name :  authors
   array_relationships :
     -   name :  articles
       using :
         foreign_key_constraint_on :
           column :  author_id
           table :
             schema :  public
             name :  articles
```

Apply the Metadata by running:

`hasura metadata apply`

You can create an array relationship by using the[ mssql_create_array_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#mssql-create-array-relationship)metadata
API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_create_array_relationship" ,
   "args" :   {
     "table" :   "author" ,
     "name" :   "articles" ,
     "source" :   "<db_name>" ,
     "using" :   {
       "foreign_key_constraint_on"   :   {
           "table"   :   "articles" ,
           "columns"   :   [ "author_id" ]
         }
       }
     }
   }
```

Fetch a list of authors and a nested list of each author's articles:

## Using manual relationships​

Let's say you have a table `authors (id, name)` and a[ view ](https://hasura.io/docs/latest/schema/ms-sql-server/views/)' +
' `author_avg_rating (id, avg)` which has the average rating of articles for each author.

Let us now create an `object relationship` called `avg_rating` from the `authors` table to the `author_avg_rating` view
using a manual relationship:

- Console
- CLI
- API


 **Step 1: Open the manual relationship section** 

- Open the Console and navigate to the `Data -> authors -> Relationships` tab.
- Click on the `Add Relationship` button:


Image: [ Open the manual relationship widget ](https://hasura.io/docs/assets/images/add-manual-rel-open-widget-3be03d95a2ab09f43617989c50f00b12.png)

 **Step 2: Fill in the relationships details ** 

Once the widget is open, fill in the name of the relationship and pick a reference source

Image: [ Define the relationship name and target ](https://hasura.io/docs/assets/images/add-manual-rel-add-name-pick-source-58889f4d29d33a04caf20738c1a9143d.png)

This will open up a "details" section below where you can fill in the rest of the relationship definition

Image: [ Fill the relationship details ](https://hasura.io/docs/assets/images/add-manual-rel-fill-details-ace1fef8c61f59ad2f2d763769217a28.png)

 **Step 3: Create the relationship** 

Now click on the `Create Relationship` button to proceed.

Image: [ Fill the relationship details ](https://hasura.io/docs/assets/images/add-manual-rel-create-final-step-0a52db1c3c199e50d208a543e21ba9f5.png)

You can add a manual relationship in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  articles
-   table :
     schema :  public
     name :  authors
   object_relationships :
     -   name :  avg_rating
       using :
         manual_configuration :
           remote_table :
             schema :  public
             name :  author_average_rating
           column_mapping :
             id :  author_id
-   table :
     schema :  public
     name :  author_average_rating
```

Apply the Metadata by running:

`hasura metadata apply`

You can add a manual relationship by using the[ mssql_create_object_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#mssql-create-object-relationship)Metadata API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_create_object_relationship" ,
   "args" :   {
     "table" :   "authors" ,
     "name" :   "avg_rating" ,
     "source" :   "<db_name>" ,
     "using" :   {
       "manual_configuration" :   {
         "remote_table" :   "author_average_rating" ,
         "column_mapping" :   {
           "id" :   "author_id"
         }
       }
     }
   }
}
```

We can now run a nested object query that is based on this `object relationship` .

Fetch a list of authors with the average rating of their articles:

## Tracking existing relationships inferred via foreign-keys​

As mentioned in the Introduction section above, relationships can be inferred via foreign-keys that exist in your
database:

- Console
- CLI
- API


The Console infers potential relationships using existing foreign-keys and recommends these on the `Data -> Schema` page

Image: [ Track all relationships ](https://hasura.io/docs/assets/images/schema-track-relationships-1291b623e5b873a3d1eaf7dbb80ea83a.png)

You can choose to track the relationships individually using the `Track` buttons or hit the `Track all` button to track
all the inferred relationships in one go.

You can add relationships in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  articles
   object_relationships :
     -   name :  author
       using :
         foreign_key_constraint_on :  author_id
-   table :
     schema :  public
     name :  authors
   array_relationships :
     -   name :  articles
       using :
         foreign_key_constraint_on :
           column :  author_id
           table :
             schema :  public
             name :  articles
```

Apply the Metadata by running:

`hasura metadata apply`

You can create multiple relationships by using the[ mssql_create_object_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#mssql-create-object-relationship)and
the[ mssql_create_array_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#mssql-create-array-relationship)Metadata APIs:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bulk" ,
   "args" :   [
     {
       "type" :   "mssql_create_object_relationship" ,
       "args" :   {
         "source" :   "<db_name>" ,
         "table" :   "articles" ,
         "name" :   "author" ,
         "using" :   {
           "foreign_key_constraint_on" :   "author_id"
         }
       }
     } ,
     {
       "type" :   "mssql_create_array_relationship" ,
       "args" :   {
         "source" :   "<db_name>" ,
         "table" :   "authors" ,
         "name" :   "articles" ,
         "using" :   {
           "foreign_key_constraint_on"   :   {
             "table"   :   "articles" ,
             "column"   :   "author_id"
           }
         }
       }
     }
   ]
}
```

## Tracking relationships between tables and Native Queries​

As mentioned in the Introduction section above, a relationship from a table to a Native Query can only be set up manually.

- API


Given a table named `articles` and an existing Native Query named `get_author` ,
we can set up a relationship between the two.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bulk" ,
   "args" :   [
     {
       "type" :   "mssql_create_object_relationship" ,
       "args" :   {
         "source" :   "<db_name>" ,
         "table" :   "articles" ,
         "name" :   "author" ,
         "using" :   {
           "manual_configuration" :   {
             "remote_native_query" :   "get_author" ,
             "column_mapping" :   {
               "id" :   "author_id"
             }
           }
         }
       }
     }
   ]
}
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/create/#introduction)
- [ Using foreign keys ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/create/#ms-sql-server-relationships-using-fkey)
    - [ Step 1: Add foreign-key constraint ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/create/#step-1-add-foreign-key-constraint)

- [ Step 2: Create an object relationship ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/create/#step-2-create-an-object-relationship)

- [ Step 3: Create an array relationship ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/create/#step-3-create-an-array-relationship)
- [ Using manual relationships ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/create/#ms-sql-server-create-manual-relationships)
- [ Tracking existing relationships inferred via foreign-keys ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/create/#tracking-existing-relationships-inferred-via-foreign-keys)
- [ Tracking relationships between tables and Native Queries ](https://hasura.io/docs/latest/schema/ms-sql-server/table-relationships/create/#tracking-relationships-between-tables-and-native-queries)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)