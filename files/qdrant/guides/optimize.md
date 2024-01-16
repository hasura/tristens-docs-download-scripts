# Optimize Qdrant

Different use cases have different requirements for balancing between memory, speed, and precision.
Qdrant is designed to be flexible and customizable so you can tune it to your needs.

Image: [ Trafeoff ](https://qdrant.tech/docs/tradeoff.png)

Image: [ Trafeoff ](https://qdrant.tech/docs/tradeoff.png)

Let’s look deeper into each of those possible optimization scenarios.

## Prefer low memory footprint with high speed search

The main way to achieve high speed search with low memory footprint is to keep vectors on disk while at the same time minimizing the number of disk reads.

Vector quantization is one way to achieve this. Quantization converts vectors into a more compact representation, which can be stored in memory and used for search. With smaller vectors you can cache more in RAM and reduce the number of disk reads.

To configure in-memory quantization, with on-disk original vectors, you need to create a collection with the following configuration:

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

    "quantization_config": {

        "scalar": {

            "type": "int8",

            "always_ram": true

        }

    }

}

```

```
from   qdrant_client   import  QdrantClient

from   qdrant_client.http   import  models



client  =  QdrantClient( "localhost" , port = 6333 )



client . create_collection(

    collection_name = " {collection_name} " ,

    vectors_config = models . VectorParams(size = 768 , distance = models . Distance . COSINE),

    optimizers_config = models . OptimizersConfigDiff(memmap_threshold = 20000 ),

    quantization_config = models . ScalarQuantization(

        scalar = models . ScalarQuantizationConfig(

             type = models . ScalarType . INT8,

            always_ram = True ,

        ),

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

    memmap_threshold:  20000 ,

  },

  quantization_config :  {

    scalar :  {

       type :   "int8" ,

      always_ram:  true ,

    },

  },

});

```

```
use   qdrant_client::{ 

     client::QdrantClient, 

     qdrant::{ 

         quantization_config::Quantization,   vectors_config::Config,   CreateCollection,   Distance, 

         OptimizersConfigDiff,   QuantizationConfig,   QuantizationType,   ScalarQuantization, 

         VectorParams,   VectorsConfig, 

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

         quantization_config:  Some (QuantizationConfig   { 

             quantization:  Some (Quantization::Scalar(ScalarQuantization   { 

                 r#type:  QuantizationType ::Int8.into(), 

                 always_ram:  Some ( true ), 

                 .. Default ::default() 

             })), 

         }), 

         .. Default ::default() 

     }) 

     . await ? ; 

```

 `mmmap_threshold` will ensure that vectors will be stored on disk, while `always_ram` will ensure that quantized vectors will be stored in RAM.

Optionally, you can disable rescoring with search `params` , which will reduce the number of disk reads even further, but potentially slightly decrease the precision.

```
POST /collections/{collection_name}/points/search

{

    "params": {

        "quantization": {

            "rescore": false

        }

    },

    "vector": [0.2, 0.1, 0.9, 0.7],

    "limit": 10

}

```

```
from   qdrant_client   import  QdrantClient

from   qdrant_client.http   import  models



client  =  QdrantClient( "localhost" , port = 6333 )



client . search(

    collection_name = " {collection_name} " ,

    query_vector = [ 0.2 ,  0.1 ,  0.9 ,  0.7 ],

    search_params = models . SearchParams(

        quantization = models . QuantizationSearchParams(rescore = False )

    ),

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.search( "{collection_name}" , {

  vector :  [ 0.2 ,  0.1 ,  0.9 ,  0.7 ],

  params :  {

    quantization :  {

      rescore:  false ,

    },

  },

});

```

```
use   qdrant_client::{ 

     client::QdrantClient, 

     qdrant::{QuantizationSearchParams,   SearchParams,   SearchPoints}, 

}; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client 

     .search_points( & SearchPoints   { 

         collection_name:  "{collection_name}" .to_string(), 

         vector:  vec ! [ 0.2 ,   0.1 ,   0.9 ,   0.7 ], 

         params:  Some (SearchParams   { 

             quantization:  Some (QuantizationSearchParams   { 

                 rescore:  Some ( false ), 

                 .. Default ::default() 

             }), 

             .. Default ::default() 

         }), 

         limit:  3 , 

         .. Default ::default() 

     }) 

     . await ? ; 

```

## Prefer high precision with low memory footprint

In case you need high precision, but don’t have enough RAM to store vectors in memory, you can enable on-disk vectors and HNSW index.

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

         vectors_config::Config,   CreateCollection,   Distance,   HnswConfigDiff,   OptimizersConfigDiff, 

         VectorParams,   VectorsConfig, 

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

In this scenario you can increase the precision of the search by increasing the `ef` and `m` parameters of the HNSW index, even with limited RAM.

```
... 

"hnsw_config" :  {

     "m" :  64 ,

     "ef_construct" :  512 ,

     "on_disk" :  true 

}

... 

```

The disk IOPS is a critical factor in this scenario, it will determine how fast you can perform search.
You can use[ fio ](https://gist.github.com/superboum/aaa45d305700a7873a8ebbab1abddf2b)to measure disk IOPS.

## Prefer high precision with high speed search

For high speed and high precision search it is critical to keep as much data in RAM as possible.
By default, Qdrant follows this approach, but you can tune it to your needs.

Is is possible to achieve high search speed and tunable accuracy by applying quantization with re-scoring.

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

    "quantization_config": {

        "scalar": {

            "type": "int8",

            "always_ram": true

        }

    }

}

```

```
from   qdrant_client   import  QdrantClient

from   qdrant_client.http   import  models



client  =  QdrantClient( "localhost" , port = 6333 )



client . create_collection(

    collection_name = " {collection_name} " ,

    vectors_config = models . VectorParams(size = 768 , distance = models . Distance . COSINE),

    optimizers_config = models . OptimizersConfigDiff(memmap_threshold = 20000 ),

    quantization_config = models . ScalarQuantization(

        scalar = models . ScalarQuantizationConfig(

             type = models . ScalarType . INT8,

            always_ram = True ,

        ),

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

    memmap_threshold:  20000 ,

  },

  quantization_config :  {

    scalar :  {

       type :   "int8" ,

      always_ram:  true ,

    },

  },

});

```

```
use   qdrant_client::{ 

     client::QdrantClient, 

     qdrant::{ 

         quantization_config::Quantization,   vectors_config::Config,   CreateCollection,   Distance, 

         OptimizersConfigDiff,   QuantizationConfig,   QuantizationType,   ScalarQuantization, 

         VectorParams,   VectorsConfig, 

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

         quantization_config:  Some (QuantizationConfig   { 

             quantization:  Some (Quantization::Scalar(ScalarQuantization   { 

                 r#type:  QuantizationType ::Int8.into(), 

                 always_ram:  Some ( true ), 

                 .. Default ::default() 

             })), 

         }), 

         .. Default ::default() 

     }) 

     . await ? ; 

```

There are also some search-time parameters you can use to tune the search accuracy and speed:

```
POST /collections/{collection_name}/points/search

{

    "params": {

        "hnsw_ef": 128,

        "exact": false

    },

    "vector": [0.2, 0.1, 0.9, 0.7],

    "limit": 3

}

```

```
from   qdrant_client   import  QdrantClient, models



client  =  QdrantClient( "localhost" , port = 6333 )



client . search(

    collection_name = " {collection_name} " ,

    search_params = models . SearchParams(hnsw_ef = 128 , exact = False ),

    query_vector = [ 0.2 ,  0.1 ,  0.9 ,  0.7 ],

    limit = 3 ,

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.search( "{collection_name}" , {

  vector :  [ 0.2 ,  0.1 ,  0.9 ,  0.7 ],

  params :  {

    hnsw_ef:  128 ,

    exact:  false ,

  },

  limit:  3 ,

});

```

```
use   qdrant_client::{ 

     client::QdrantClient, 

     qdrant::{SearchParams,   SearchPoints}, 

}; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client 

     .search_points( & SearchPoints   { 

         collection_name:  "{collection_name}" .to_string(), 

         vector:  vec ! [ 0.2 ,   0.1 ,   0.9 ,   0.7 ], 

         params:  Some (SearchParams   { 

             hnsw_ef:  Some ( 128 ), 

             exact:  Some ( false ), 

             .. Default ::default() 

         }), 

         limit:  3 , 

         .. Default ::default() 

     }) 

     . await ? ; 

```

- `hnsw_ef` - controls the number of neighbors to visit during search. The higher the value, the more accurate and slower the search will be. Recommended range is 32-512.
- `exact` - if set to `true` , will perform exact search, which will be slower, but more accurate. You can use it to compare results of the search with different `hnsw_ef` values versus the ground truth.


## Latency vs Throughput

- There are two main approaches to measure the speed of search:
    - latency of the request - the time from the moment request is submitted to the moment a response is received

- throughput - the number of requests per second the system can handle


Those approaches are not mutually exclusive, but in some cases it might be preferable to optimize for one or another.

To prefer minimizing latency, you can set up Qdrant to use as many cores as possible for a single request.
You can do this by setting the number of segments in the collection to be equal to the number of cores in the system. In this case, each segment will be processed in parallel, and the final result will be obtained faster.

```
PUT /collections/{collection_name}

{

    "vectors": {

      "size": 768,

      "distance": "Cosine"

    },

    "optimizers_config": {

        "default_segment_number": 16

    }

}

```

```
from   qdrant_client   import  QdrantClient, models



client  =  QdrantClient( "localhost" , port = 6333 )



client . create_collection(

    collection_name = " {collection_name} " ,

    vectors_config = models . VectorParams(size = 768 , distance = models . Distance . COSINE),

    optimizers_config = models . OptimizersConfigDiff(default_segment_number = 16 ),

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

    default_segment_number:  16 ,

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

             default_segment_number:  Some ( 16 ), 

             .. Default ::default() 

         }), 

         .. Default ::default() 

     }) 

     . await ? ; 

```

To prefer throughput, you can set up Qdrant to use as many cores as possible for processing multiple requests in parallel.
To do that, you can configure qdrant to use minimal number of segments, which is usually 2.
Large segments benefit from the size of the index and overall smaller number of vector comparisons required to find the nearest neighbors. But at the same time require more time to build index.

```
PUT /collections/{collection_name}

{

    "vectors": {

      "size": 768,

      "distance": "Cosine"

    },

    "optimizers_config": {

        "default_segment_number": 2

    }

}

```

```
from   qdrant_client   import  QdrantClient, models



client  =  QdrantClient( "localhost" , port = 6333 )



client . create_collection(

    collection_name = " {collection_name} " ,

    vectors_config = models . VectorParams(size = 768 , distance = models . Distance . COSINE),

    optimizers_config = models . OptimizersConfigDiff(default_segment_number = 2 ),

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

    default_segment_number:  2 ,

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

             default_segment_number:  Some ( 2 ), 

             .. Default ::default() 

         }), 

         .. Default ::default() 

     }) 

     . await ? ; 

```

##### Table of contents

- [ Prefer low memory footprint with high speed search ](https://qdrant.tech/documentation/guides/optimize/#prefer-low-memory-footprint-with-high-speed-search)
- [ Prefer high precision with low memory footprint ](https://qdrant.tech/documentation/guides/optimize/#prefer-high-precision-with-low-memory-footprint)
- [ Prefer high precision with high speed search ](https://qdrant.tech/documentation/guides/optimize/#prefer-high-precision-with-high-speed-search)
- [ Latency vs Throughput ](https://qdrant.tech/documentation/guides/optimize/#latency-vs-throughput)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/optimize.md)
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