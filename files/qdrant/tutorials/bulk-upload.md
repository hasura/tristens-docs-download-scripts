# Bulk upload a large number of vectors

Uploading a large-scale dataset fast might be a challenge, but Qdrant has a few tricks to help you with that.

The first important detail about data uploading is that the bottleneck is usually located on the client side, not on the server side.
This means that if you are uploading a large dataset, you should prefer a high-performance client library.

We recommend using our[ Rust client library ](https://github.com/qdrant/rust-client)for this purpose, as it is the fastest client library available for Qdrant.

If you are not using Rust, you might want to consider parallelizing your upload process.

## Disable indexing during upload

In case you are doing an initial upload of a large dataset, you might want to disable indexing during upload.
It will enable to avoid unnecessary indexing of vectors, which will be overwritten by the next batch.

To disable indexing during upload, set `indexing_threshold` to `0` :

```
PUT /collections/{collection_name}

{

    "vectors": {

      "size": 768,

      "distance": "Cosine"

    },

    "optimizers_config": {

        "indexing_threshold": 0

    }

}

```

```
from   qdrant_client   import  QdrantClient, models



client  =  QdrantClient( "localhost" , port = 6333 )



client . create_collection(

    collection_name = " {collection_name} " ,

    vectors_config = models . VectorParams(size = 768 , distance = models . Distance . COSINE),

    optimizers_config = models . OptimizersConfigDiff(

        indexing_threshold = 0 ,

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

  },

  optimizers_config :  {

    indexing_threshold:  0 ,

  },

});

```

After upload is done, you can enable indexing by setting `indexing_threshold` to a desired value (default is 20000):

```
PATCH /collections/{collection_name}

{

    "optimizers_config": {

        "indexing_threshold": 20000

    }

}

```

```
from   qdrant_client   import  QdrantClient, models



client  =  QdrantClient( "localhost" , port = 6333 )



client . update_collection(

    collection_name = " {collection_name} " ,

    optimizer_config = models . OptimizersConfigDiff(indexing_threshold = 20000 ),

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.updateCollection( "{collection_name}" , {

  optimizers_config :  {

    indexing_threshold:  20000 ,

  },

});

```

## Upload directly to disk

When the vectors you upload do not all fit in RAM, you likely want to use[ memmap ](../../concepts/storage/#configuring-memmap-storage)support.

During collection[ creation ](../../concepts/collections/#create-collection),
memmaps may be enabled on a per-vector basis using the `on_disk` parameter. This
will store vector data directly on disk at all times. It is suitable for
ingesting a large amount of data, essential for the billion scale benchmark.

Using `memmap_threshold_kb` is not recommended in this case. It would require
the[ optimizer ](../../concepts/optimizer/)to constantly
transform in-memory segments into memmap segments on disk. This process is
slower, and the optimizer can be a bottleneck when ingesting a large amount of
data.

Read more about this in[ Configuring Memmap Storage ](../../concepts/storage/#configuring-memmap-storage).

## Parallel upload into multiple shards

In Qdrant, each collection is split into shards. Each shard has a separate Write-Ahead-Log (WAL), which is responsible for ordering operations.
By creating multiple shards, you can parallelize upload of a large dataset. From 2 to 4 shards per one machine is a reasonable number.

```
PUT /collections/{collection_name}

{

    "vectors": {

      "size": 768,

      "distance": "Cosine"

    },

    "shard_number": 2

}

```

```
from   qdrant_client   import  QdrantClient, models



client  =  QdrantClient( "localhost" , port = 6333 )



client . create_collection(

    collection_name = " {collection_name} " ,

    vectors_config = models . VectorParams(size = 768 , distance = models . Distance . COSINE),

    shard_number = 2 ,

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

  shard_number:  2 ,

});

```

##### Table of contents

- [ Disable indexing during upload ](https://qdrant.tech/documentation/tutorials/bulk-upload/#disable-indexing-during-upload)
- [ Upload directly to disk ](https://qdrant.tech/documentation/tutorials/bulk-upload/#upload-directly-to-disk)
- [ Parallel upload into multiple shards ](https://qdrant.tech/documentation/tutorials/bulk-upload/#parallel-upload-into-multiple-shards)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/tutorials/bulk-upload.md)
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