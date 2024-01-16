# Storage

All data within one collection is divided into segments.
Each segment has its independent vector and payload storage as well as indexes.

Data stored in segments usually do not overlap.
However, storing the same point in different segments will not cause problems since the search contains a deduplication mechanism.

The segments consist of vector and payload storages, vector and payload[ indexes ](../indexing), and id mapper, which stores the relationship between internal and external ids.

A segment can be `appendable` or `non-appendable` depending on the type of storage and index used.
You can freely add, delete and query data in the `appendable` segment.
With `non-appendable` segment can only read and delete data.

The configuration of the segments in the collection can be different and independent of one another, but at least one `appendable’ segment must be present in a collection.

## Vector storage

Depending on the requirements of the application, Qdrant can use one of the data storage options.
The choice has to be made between the search speed and the size of the RAM used.

 **In-memory storage** - Stores all vectors in RAM, has the highest speed since disk access is required only for persistence.

 **Memmap storage** - Creates a virtual address space associated with the file on disk.[ Wiki ](https://en.wikipedia.org/wiki/Memory-mapped_file).
Mmapped files are not directly loaded into RAM. Instead, they use page cache to access the contents of the file.
This scheme allows flexible use of available memory. With sufficient RAM, it is almost as fast as in-memory storage.

### Configuring Memmap storage

There are two ways to configure the usage of memmap(also known as on-disk) storage:

- Set up `on_disk` option for the vectors in the collection create API:


 *Available as of v1.2.0* 

```
PUT /collections/{collection_name}

{

    "vectors": {

      "size": 768,

      "distance": "Cosine",

      "on_disk": true

    }

}

```

```
from   qdrant_client   import  QdrantClient, models



client  =  QdrantClient( "localhost" , port = 6333 )



client . create_collection(

    collection_name = " {collection_name} " ,

    vectors_config = models . VectorParams(

        size = 768 , distance = models . Distance . COSINE, on_disk = True 

    ),

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.createCollection( "{collection_name}" , {

  vectors :  {

    size:  768 ,

    distance :   "Cosine" ,

    on_disk:  true ,

  },

});

```

```
use   qdrant_client::{ 

     client::QdrantClient, 

     qdrant::{vectors_config::Config,   CreateCollection,   Distance,   VectorParams,   VectorsConfig}, 

}; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client 

     .create_collection( & CreateCollection   { 

         collection_name:  "{collection_name}" .to_string(), 

         vectors_config:  Some (VectorsConfig   { 

             config:  Some (Config::Params(VectorParams   { 

                 size:  768 , 

                 distance:  Distance ::Cosine.into(), 

                 on_disk:  Some ( true ), 

                 .. Default ::default() 

             })), 

         }), 

         .. Default ::default() 

     }) 

     . await ? ; 

```

This will create a collection with all vectors immediately stored in memmap storage.
This is the recommended way, in case your Qdrant instance operates with fast disks and you are working with large collections.

- Set up `memmap_threshold_kb` option. This option will set the threshold after which the segment will be converted to memmap storage.


There are two ways to do this:

1. You can set the threshold globally in the[ configuration file ](../../guides/configuration/). The parameter is called `memmap_threshold_kb` .
2. You can set the threshold for each collection separately during[ creation ](../collections/#create-collection)or[ update ](../collections/#update-collection-parameters).


```
PUT /collections/{collection_name}

{

    "vectors": {

      "size": 768,

      "distance": "Cosine"

    },

    "optimizers_config": {

        "memmap_threshold": 20000

    }

}

```

```
from   qdrant_client   import  QdrantClient, models



client  =  QdrantClient( "localhost" , port = 6333 )



client . create_collection(

    collection_name = " {collection_name} " ,

    vectors_config = models . VectorParams(size = 768 , distance = models . Distance . COSINE),

    optimizers_config = models . OptimizersConfigDiff(memmap_threshold = 20000 ),

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.createCollection( "{collection_name}" , {

  vectors :  {

    size:  768 ,

    distance :   "Cosine" ,

  },

  optimizers_config :  {

    memmap_threshold:  20000 ,

  },

});

```

```
use   qdrant_client::{ 

     client::QdrantClient, 

     qdrant::{ 

         vectors_config::Config,   CreateCollection,   Distance,   OptimizersConfigDiff,   VectorParams, 

         VectorsConfig, 

     }, 

}; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client 

     .create_collection( & CreateCollection   { 

         collection_name:  "{collection_name}" .to_string(), 

         vectors_config:  Some (VectorsConfig   { 

             config:  Some (Config::Params(VectorParams   { 

                 size:  768 , 

                 distance:  Distance ::Cosine.into(), 

                 .. Default ::default() 

             })), 

         }), 

         optimizers_config:  Some (OptimizersConfigDiff   { 

             memmap_threshold:  Some ( 20000 ), 

             .. Default ::default() 

         }), 

         .. Default ::default() 

     }) 

     . await ? ; 

```

The rule of thumb to set the memmap threshold parameter is simple:

- if you have a balanced use scenario - set memmap threshold the same as `indexing_threshold` (default is 20000). In this case the optimizer will not make any extra runs and will optimize all thresholds at once.
- if you have a high write load and low RAM - set memmap threshold lower than `indexing_threshold` to e.g. 10000. In this case the optimizer will convert the segments to memmap storage first and will only apply indexing after that.


In addition, you can use memmap storage not only for vectors, but also for HNSW index.
To enable this, you need to set the `hnsw_config.on_disk` parameter to `true` during collection[ creation ](../collections/#create-a-collection)or[ updating ](../collections/#update-collection-parameters).

```
PUT /collections/{collection_name}

{

    "vectors": {

      "size": 768,

      "distance": "Cosine"

    },

    "optimizers_config": {

        "memmap_threshold": 20000

    },

    "hnsw_config": {

        "on_disk": true

    }

}

```

```
from   qdrant_client   import  QdrantClient, models



client  =  QdrantClient( "localhost" , port = 6333 )



client . create_collection(

    collection_name = " {collection_name} " ,

    vectors_config = models . VectorParams(size = 768 , distance = models . Distance . COSINE),

    optimizers_config = models . OptimizersConfigDiff(memmap_threshold = 20000 ),

    hnsw_config = models . HnswConfigDiff(on_disk = True ),

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.createCollection( "{collection_name}" , {

  vectors :  {

    size:  768 ,

    distance :   "Cosine" ,

  },

  optimizers_config :  {

    memmap_threshold:  20000 ,

  },

  hnsw_config :  {

    on_disk:  true ,

  },

});

```

```
use   qdrant_client::{ 

     client::QdrantClient, 

     qdrant::{ 

         vectors_config::Config,   CreateCollection,   Distance,   HnswConfigDiff, 

         OptimizersConfigDiff,   VectorParams,   VectorsConfig, 

     }, 

}; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client 

     .create_collection( & CreateCollection   { 

         collection_name:  "{collection_name}" .to_string(), 

         vectors_config:  Some (VectorsConfig   { 

             config:  Some (Config::Params(VectorParams   { 

                 size:  768 , 

                 distance:  Distance ::Cosine.into(), 

                 .. Default ::default() 

             })), 

         }), 

         optimizers_config:  Some (OptimizersConfigDiff   { 

             memmap_threshold:  Some ( 20000 ), 

             .. Default ::default() 

         }), 

         hnsw_config:  Some (HnswConfigDiff   { 

             on_disk:  Some ( true ), 

             .. Default ::default() 

         }), 

         .. Default ::default() 

     }) 

     . await ? ; 

```

## Payload storage

Qdrant supports two types of payload storages: InMemory and OnDisk.

InMemory payload storage is organized in the same way as in-memory vectors.
The payload data is loaded into RAM at service startup while disk and[ RocksDB ](https://rocksdb.org/)are used for persistence only.
This type of storage works quite fast, but it may require a lot of space to keep all the data in RAM, especially if the payload has large values attached - abstracts of text or even images.

In the case of large payload values, it might be better to use OnDisk payload storage.
This type of storage will read and write payload directly to RocksDB, so it won’t require any significant amount of RAM to store.
The downside, however, is the access latency.
If you need to query vectors with some payload-based conditions - checking values stored on disk might take too much time.
In this scenario, we recommend creating a payload index for each field used in filtering conditions to avoid disk access.
Once you create the field index, Qdrant will preserve all values of the indexed field in RAM regardless of the payload storage type.

You can specify the desired type of payload storage with[ configuration file ](../../guides/configuration/)or with collection parameter `on_disk_payload` during[ creation ](../collections/#create-collection)of the collection.

## Versioning

To ensure data integrity, Qdrant performs all data changes in 2 stages.
In the first step, the data is written to the Write-ahead-log(WAL), which orders all operations and assigns them a sequential number.

Once a change has been added to the WAL, it will not be lost even if a power loss occurs.
Then the changes go into the segments.
Each segment stores the last version of the change applied to it as well as the version of each individual point.
If the new change has a sequential number less than the current version of the point, the updater will ignore the change.
This mechanism allows Qdrant to safely and efficiently restore the storage from the WAL in case of an abnormal shutdown.

##### Table of contents

- [ Vector storage ](https://qdrant.tech/documentation/concepts/storage/#vector-storage)
    - [ Configuring Memmap storage ](https://qdrant.tech/documentation/concepts/storage/#configuring-memmap-storage)
- [ Payload storage ](https://qdrant.tech/documentation/concepts/storage/#payload-storage)
- [ Versioning ](https://qdrant.tech/documentation/concepts/storage/#versioning)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/storage.md)
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