# MindsDB

[ MindsDB ](https://mindsdb.com)is an AI automation platform for building AI/ML powered features and applications. It works by connecting any source of data with any AI/ML model or framework and automating how real-time data flows between them.

With the MindsDB-Qdrant integration, you can now select Qdrant as a database to load into and retrieve from with semantic search and filtering.

 **MindsDB allows you to easily** :

- Connect to any store of data or end-user application.
- Pass data to an AI model from any store of data or end-user application.
- Plug the output of an AI model into any store of data or end-user application.
- Fully automate these workflows to build AI-powered features and applications


## Usage

To get started with Qdrant and MindsDB, the following syntax can be used.

```
CREATE   DATABASE   qdrant_test 

WITH   ENGINE   =   "qdrant" , 

PARAMETERS   =   { 

     "location" :   ":memory:" , 

     "collection_config" :   { 

         "size" :   386 , 

         "distance" :   "Cosine" 

     } 

} 

```

The available arguments for instantiating Qdrant can be found[ here ](https://github.com/mindsdb/mindsdb/blob/23a509cb26bacae9cc22475497b8644e3f3e23c3/mindsdb/integrations/handlers/qdrant_handler/qdrant_handler.py#L408-L468).

## Creating a new table

- Qdrant options for creating a collection can be specified as `collection_config` in the `CREATE DATABASE` parameters.
- By default, UUIDs are set as collection IDs. You can provide your own IDs under the `id` column.


```
CREATE   TABLE   qdrant_test.test_table   ( 

    SELECT   embeddings, '{"source": "bbc"}'   as   metadata   FROM   mysql_demo_db.test_embeddings 

); 

```

## Querying the database

#### Perform a full retrieval using the following syntax.

`SELECT   *   FROM   qdrant_test.test_table 
`

By default, the `LIMIT` is set to 10 and the `OFFSET` is set to 0.

#### Perform a similarity search using your embeddings

```
SELECT   *   FROM   qdrant_test.test_table 

WHERE   search_vector   =   ( select   embeddings   from   mysql_demo_db.test_embeddings   limit   1 ) 

```

#### Perform a search using filters

```
SELECT   *   FROM   qdrant_test.test_table 

WHERE   ` metadata. source `   =   'bbc' ; 

```

#### Delete entries using IDs

```
DELETE   FROM   qtest.test_table_6 

WHERE   id   =   2 

```

#### Delete entries using filters

```
DELETE   *   FROM   qdrant_test.test_table 

WHERE   ` metadata. source `   =   'bbc' ; 

```

#### Drop a table

`  DROP   TABLE   qdrant_test.test_table; 
`

## Next steps

You can find more information pertaining to MindsDB and its datasources[ here ](https://docs.mindsdb.com/).

##### Table of contents

- [ Usage ](https://qdrant.tech/documentation/frameworks/mindsdb/#usage)
- [ Creating a new table ](https://qdrant.tech/documentation/frameworks/mindsdb/#creating-a-new-table)
- [ Querying the database ](https://qdrant.tech/documentation/frameworks/mindsdb/#querying-the-database)
    -

- 
- [ Next steps ](https://qdrant.tech/documentation/frameworks/mindsdb/#next-steps)



- 


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/mindsdb.md)
- [ 
 Create an Issue
 ](https://github.com/qdrant/landing_page/issues/new/choose)


#### Product

- [ 
Use cases
 ](https://qdrant.tech/use-cases/)
- [ 
Solutions
 ](https://qdrant.tech/solutions/)
- [ 
Benchmarks
 ](https://qdrant.tech/benchmarks/)
- [ 
Demos
 ](https://qdrant.tech/demo/)
- [ 
Pricing
 ](https://qdrant.tech/pricing/)


#### Community

- [ 
 
Github
 ](https://github.com/qdrant/qdrant)
- [ 
 
Discord
 ](https://qdrant.to/discord)
- [ 
 
Twitter
 ](https://qdrant.to/twitter)
- [ 
 
Newsletter
 ](https://qdrant.tech/subscribe/)
- [ 
 
Contact us
 ](https://qdrant.to/contact-us)


#### Company

- [ 
Jobs
 ](https://qdrant.join.com)
- [ 
Privacy Policy
 ](https://qdrant.tech/legal/privacy-policy/)
- [ 
Terms
 ](https://qdrant.tech/legal/terms_and_conditions/)
- [ 
Impressum
 ](https://qdrant.tech/legal/impressum/)
- [ 
Credits
 ](https://qdrant.tech/legal/credits/)


#### Latest Publications

#### Combining the precision of exact keyword search with NN-based ranking

#### Qdrant 1.7.0 brought a bunch of new features. Let's take a closer look at them!

#### Qdrant 1.6 brings recommendations strategies and more flexibility to the Recommendation API.

- [  ](https://github.com/qdrant/qdrant)
- [  ](https://qdrant.to/linkedin)
- [  ](https://qdrant.to/twitter)
- [  ](https://qdrant.to/discord)
- [  ](https://www.youtube.com/channel/UC6ftm8PwH1RU_LM1jwG0LQA)


##### Thanks for using Qdrant!

Subscribe to our e-mail newsletter if you want to be updated on new features and news regarding
Qdrant.

Like what we are doing? Consider giving us a ⭐[ on Github ](https://github.com/qdrant/qdrant).

We use cookies to learn more about you. At any time you can delete or block cookies through your browser settings.