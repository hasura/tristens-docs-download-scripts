# Points

The points are the central entity that Qdrant operates with.
A point is a record consisting of a vector and an optional[ payload ](../payload).

You can search among the points grouped in one[ collection ](../collections)based on vector similarity.
This procedure is described in more detail in the[ search ](../search)and[ filtering ](../filtering)sections.

This section explains how to create and manage vectors.

Any point modification operation is asynchronous and takes place in 2 steps.
At the first stage, the operation is written to the Write-ahead-log.

After this moment, the service will not lose the data, even if the machine loses power supply.

## Awaiting result

If the API is called with the `&wait=false` parameter, or if it is not explicitly specified, the client will receive an acknowledgment of receiving data:

```
{

     "result" : {

         "operation_id" :  123 ,

         "status" :  "acknowledged" 

    },

     "status" :  "ok" ,

     "time" :  0.000206061 

}

```

This response does not mean that the data is available for retrieval yet. This
uses a form of eventual consistency. It may take a short amount of time before it
is actually processed as updating the collection happens in the background. In
fact, it is possible that such request eventually fails.
If inserting a lot of vectors, we also recommend using asynchronous requests to take advantage of pipelining.

If the logic of your application requires a guarantee that the vector will be available for searching immediately after the API responds, then use the flag `?wait=true` .
In this case, the API will return the result only after the operation is finished:

```
{

     "result" : {

         "operation_id" :  0 ,

         "status" :  "completed" 

    },

     "status" :  "ok" ,

     "time" :  0.000206061 

}

```

## Point IDs

Qdrant supports using both `64-bit unsigned integers` and `UUID` as identifiers for points.

Examples of UUID string representations:

- simple: `936DA01F9ABD4d9d80C702AF85C822A8`
- hyphenated: `550e8400-e29b-41d4-a716-446655440000`
- urn: `urn:uuid:F9168C5E-CEB2-4faa-B6BF-329BF39FA1E4`


That means that in every request UUID string could be used instead of numerical id.
Example:

```
PUT /collections/{collection_name}/points

{

    "points": [

        {

            "id": "5c56c793-69f3-4fbf-87e6-c4bf54c28c26",

            "payload": {"color": "red"},

            "vector": [0.9, 0.1, 0.1]

        }

    ]

}

```

```
from   qdrant_client   import  QdrantClient

from   qdrant_client.http   import  models



client  =  QdrantClient( "localhost" , port = 6333 )



client . upsert(

    collection_name = " {collection_name} " ,

    points = [

        models . PointStruct(

             id = "5c56c793-69f3-4fbf-87e6-c4bf54c28c26" ,

            payload = {

                 "color" :  "red" ,

            },

            vector = [ 0.9 ,  0.1 ,  0.1 ],

        ),

    ],

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.upsert( "{collection_name}" , {

  points :  [

    {

      id :   "5c56c793-69f3-4fbf-87e6-c4bf54c28c26" ,

      payload :  {

        color :   "red" ,

      },

      vector :  [ 0.9 ,  0.1 ,  0.1 ],

    },

  ],

});

```

```
use   qdrant_client::{client::QdrantClient,   qdrant::PointStruct}; 

use   serde_json::json; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client 

     .upsert_points_blocking( 

         "{collection_name}" .to_string(), 

         None , 

         vec![PointStruct::new( 

             "5c56c793-69f3-4fbf-87e6-c4bf54c28c26" .to_string(), 

             vec![ 0.05 ,   0.61 ,   0.76 ,   0.74 ], 

             json ! ( 

                 { "color" :  "Red" } 

             ) 

             .try_into() 

             .unwrap(), 

         )], 

         None , 

     ) 

     . await ? ; 

```

and

```
PUT /collections/{collection_name}/points

{

    "points": [

        {

            "id": 1,

            "payload": {"color": "red"},

            "vector": [0.9, 0.1, 0.1]

        }

    ]

}

```

```
client . upsert(

    collection_name = " {collection_name} " ,

    points = [

        models . PointStruct(

             id = 1 ,

            payload = {

                 "color" :  "red" ,

            },

            vector = [ 0.9 ,  0.1 ,  0.1 ],

        ),

    ],

)

```

```
client.upsert( "{collection_name}" , {

  points :  [

    {

      id:  1 ,

      payload :  {

        color :   "red" ,

      },

      vector :  [ 0.9 ,  0.1 ,  0.1 ],

    },

  ],

});

```

```
use   qdrant_client::qdrant::PointStruct; 

use   serde_json::json; 



client 

     .upsert_points_blocking( 

         1 , 

         None , 

         vec![PointStruct::new( 

             "5c56c793-69f3-4fbf-87e6-c4bf54c28c26" .to_string(), 

             vec![ 0.05 ,   0.61 ,   0.76 ,   0.74 ], 

             json ! ( 

                 { "color" :  "Red" } 

             ) 

             .try_into() 

             .unwrap(), 

         )], 

         None , 

     ) 

     . await ? ; 

```

are both possible.

## Upload points

To optimize performance, Qdrant supports batch loading of points. I.e., you can load several points into the service in one API call.
Batching allows you to minimize the overhead of creating a network connection.

The Qdrant API supports two ways of creating batches - record-oriented and column-oriented.
Internally, these options do not differ and are made only for the convenience of interaction.

Create points with batch:

```
PUT /collections/{collection_name}/points

{

    "batch": {

        "ids": [1, 2, 3],

        "payloads": [

            {"color": "red"},

            {"color": "green"},

            {"color": "blue"}

        ],

        "vectors": [

            [0.9, 0.1, 0.1],

            [0.1, 0.9, 0.1],

            [0.1, 0.1, 0.9]

        ]

    }

}

```

```
client . upsert(

    collection_name = " {collection_name} " ,

    points = models . Batch(

        ids = [ 1 ,  2 ,  3 ],

        payloads = [

            { "color" :  "red" },

            { "color" :  "green" },

            { "color" :  "blue" },

        ],

        vectors = [

            [ 0.9 ,  0.1 ,  0.1 ],

            [ 0.1 ,  0.9 ,  0.1 ],

            [ 0.1 ,  0.1 ,  0.9 ],

        ],

    ),

)

```

```
client.upsert( "{collection_name}" , {

  batch :  {

    ids :  [ 1 ,  2 ,  3 ],

    payloads :  [{ color :   "red"  }, { color :   "green"  }, { color :   "blue"  }],

    vectors :  [

      [ 0.9 ,  0.1 ,  0.1 ],

      [ 0.1 ,  0.9 ,  0.1 ],

      [ 0.1 ,  0.1 ,  0.9 ],

    ],

  },

});

```

or record-oriented equivalent:

```
PUT /collections/{collection_name}/points

{

    "points": [

        {

            "id": 1,

            "payload": {"color": "red"},

            "vector": [0.9, 0.1, 0.1]

        },

        {

            "id": 2,

            "payload": {"color": "green"},

            "vector": [0.1, 0.9, 0.1]

        },

        {

            "id": 3,

            "payload": {"color": "blue"},

            "vector": [0.1, 0.1, 0.9]

        }

    ]

}

```

```
client . upsert(

    collection_name = " {collection_name} " ,

    points = [

        models . PointStruct(

             id = 1 ,

            payload = {

                 "color" :  "red" ,

            },

            vector = [ 0.9 ,  0.1 ,  0.1 ],

        ),

        models . PointStruct(

             id = 2 ,

            payload = {

                 "color" :  "green" ,

            },

            vector = [ 0.1 ,  0.9 ,  0.1 ],

        ),

        models . PointStruct(

             id = 3 ,

            payload = {

                 "color" :  "blue" ,

            },

            vector = [ 0.1 ,  0.1 ,  0.9 ],

        ),

    ],

)

```

```
client.upsert( "{collection_name}" , {

  points :  [

    {

      id:  1 ,

      payload :  { color :   "red"  },

      vector :  [ 0.9 ,  0.1 ,  0.1 ],

    },

    {

      id:  2 ,

      payload :  { color :   "green"  },

      vector :  [ 0.1 ,  0.9 ,  0.1 ],

    },

    {

      id:  3 ,

      payload :  { color :   "blue"  },

      vector :  [ 0.1 ,  0.1 ,  0.9 ],

    },

  ],

});

```

```
use   qdrant_client::qdrant::PointStruct; 

use   serde_json::json; 



client 

     .upsert_points_batch_blocking( 

         "{collection_name}" .to_string(), 

         None , 

         vec![ 

             PointStruct::new( 

                 1 , 

                 vec![ 0.9 ,   0.1 ,   0.1 ], 

                 json ! ( 

                     { "color" :  "red" } 

                 ) 

                 .try_into() 

                 .unwrap(), 

             ), 

             PointStruct::new( 

                 2 , 

                 vec![ 0.1 ,   0.9 ,   0.1 ], 

                 json ! ( 

                     { "color" :  "green" } 

                 ) 

                 .try_into() 

                 .unwrap(), 

             ), 

             PointStruct::new( 

                 3 , 

                 vec![ 0.1 ,   0.1 ,   0.9 ], 

                 json ! ( 

                     { "color" :  "blue" } 

                 ) 

                 .try_into() 

                 .unwrap(), 

             ), 

         ], 

         None , 

         100 , 

     ) 

     . await ? ; 

```

All APIs in Qdrant, including point loading, are idempotent.
It means that executing the same method several times in a row is equivalent to a single execution.

In this case, it means that points with the same id will be overwritten when re-uploaded.

Idempotence property is useful if you use, for example, a message queue that doesn’t provide an exactly-ones guarantee.
Even with such a system, Qdrant ensures data consistency.

 *Available as of v0.10.0* 

If the collection was created with multiple vectors, each vector data can be provided using the vector’s name:

```
PUT /collections/{collection_name}/points

{

    "points": [

        {

            "id": 1,

            "vector": {

                "image": [0.9, 0.1, 0.1, 0.2],

                "text": [0.4, 0.7, 0.1, 0.8, 0.1, 0.1, 0.9, 0.2]

            }

        },

        {

            "id": 2,

            "vector": {

                "image": [0.2, 0.1, 0.3, 0.9],

                "text": [0.5, 0.2, 0.7, 0.4, 0.7, 0.2, 0.3, 0.9]

            }

        }

    ]

}

```

```
client . upsert(

    collection_name = " {collection_name} " ,

    points = [

        models . PointStruct(

             id = 1 ,

            vector = {

                 "image" : [ 0.9 ,  0.1 ,  0.1 ,  0.2 ],

                 "text" : [ 0.4 ,  0.7 ,  0.1 ,  0.8 ,  0.1 ,  0.1 ,  0.9 ,  0.2 ],

            },

        ),

        models . PointStruct(

             id = 2 ,

            vector = {

                 "image" : [ 0.2 ,  0.1 ,  0.3 ,  0.9 ],

                 "text" : [ 0.5 ,  0.2 ,  0.7 ,  0.4 ,  0.7 ,  0.2 ,  0.3 ,  0.9 ],

            },

        ),

    ],

)

```

```
client.upsert( "{collection_name}" , {

  points :  [

    {

      id:  1 ,

      vector :  {

        image :  [ 0.9 ,  0.1 ,  0.1 ,  0.2 ],

        text :  [ 0.4 ,  0.7 ,  0.1 ,  0.8 ,  0.1 ,  0.1 ,  0.9 ,  0.2 ],

      },

    },

    {

      id:  2 ,

      vector :  {

        image :  [ 0.2 ,  0.1 ,  0.3 ,  0.9 ],

        text :  [ 0.5 ,  0.2 ,  0.7 ,  0.4 ,  0.7 ,  0.2 ,  0.3 ,  0.9 ],

      },

    },

  ],

});

```

```
use   qdrant_client::qdrant::PointStruct; 

use   std::collections::HashMap; 



client 

     .upsert_points_blocking( 

         "{collection_name}" .to_string(), 

         None , 

         vec![ 

             PointStruct::new( 

                 1 , 

                 HashMap::from([ 

                     ( "image" .to_string(),   vec![ 0.9 ,   0.1 ,   0.1 ,   0.2 ]), 

                     ( 

                         "text" .to_string(), 

                         vec![ 0.4 ,   0.7 ,   0.1 ,   0.8 ,   0.1 ,   0.1 ,   0.9 ,   0.2 ], 

                     ), 

                 ]), 

                 HashMap::new().into(), 

             ), 

             PointStruct::new( 

                 2 , 

                 HashMap::from([ 

                     ( "image" .to_string(),   vec![ 0.2 ,   0.1 ,   0.3 ,   0.9 ]), 

                     ( 

                         "text" .to_string(), 

                         vec![ 0.5 ,   0.2 ,   0.7 ,   0.4 ,   0.7 ,   0.2 ,   0.3 ,   0.9 ], 

                     ), 

                 ]), 

                 HashMap::new().into(), 

             ), 

         ], 

         None , 

     ) 

     . await ? ; 

```

 *Available as of v1.2.0* 

Named vectors are optional. When uploading points, some vectors may be omitted.
For example, you can upload one point with only the `image` vector and a second
one with only the `text` vector.

When uploading a point with an existing ID, the existing point is deleted first,
then it is inserted with just the specified vectors. In other words, the entire
point is replaced, and any unspecified vectors are set to null. To keep existing
vectors unchanged and only update specified vectors, see[ update vectors ](https://qdrant.tech/documentation/concepts/points/#update-vectors).

 *Available as of v1.7.0* 

Points can contain dense and sparse vectors.

A sparse vector is an array in which most of the elements have a value of zero.

It is possible to take advantage of this property to have an optimized representation, for this reason they have a different shape than dense vectors.

They are represented as a list of `(index, value)` pairs, where `index` is an integer and `value` is a floating point number. The `index` is the position of the non-zero value in the vector. The `values` is the value of the non-zero element.

For example, the following vector:

`[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 0.0, 0.0]`

can be represented as a sparse vector:

`[(6, 1.0), (7, 2.0)]`

Qdrant uses the following JSON representation throughout its APIs.

```
{

   "indices" : [ 6 ,  7 ],

   "values" : [ 1.0 ,  2.0 ]

}

```

The `indices` and `values` arrays must have the same length.
And the `indices` must be unique.

If the `indices` are not sorted, Qdrant will sort them internally so you may not rely on the order of the elements.

Sparse vectors must be named and can be uploaded in the same way as dense vectors.

```
PUT /collections/{collection_name}/points

{

    "points": [

        {

            "id": 1,

            "vector": {

                "text": {

                    "indices": [6, 7],

                    "values": [1.0, 2.0]

                }

            }

        },

        {

            "id": 2,

            "vector": {

                "text": {

                    "indices": [1, 1, 2, 3, 4, 5],

                    "values": [0.1, 0.2, 0.3, 0.4, 0.5]

                }

            }

        }

    ]

}

```

```
client . upsert(

    collection_name = " {collection_name} " ,

    points = [

        models . PointStruct(

             id = 1 ,

            vector = {

                 "text" : models . SparseVector(

                    indices = [ 6 ,  7 ],

                    values = [ 1.0 ,  2.0 ],

                )

            },

        ),

        models . PointStruct(

             id = 2 ,

            vector = {

                 "text" : models . SparseVector(

                    indices = [ 1 ,  2 ,  3 ,  4 ,  5 ],

                    values =  [ 0.1 ,  0.2 ,  0.3 ,  0.4 ,  0.5 ],

                )

            },

        ),

    ],

)

```

```
client.upsert( "{collection_name}" , {

  points :  [

    {

      id:  1 ,

      vector :  {

        text :  {

          indices :  [ 6 ,  7 ],

          values :  [ 1.0 ,  2.0 ]

        },

      },

    },

    {

      id:  2 ,

      vector :  {

        text :  {

          indices = [ 1 ,  2 ,  3 ,  4 ,  5 ],

          values =  [ 0.1 ,  0.2 ,  0.3 ,  0.4 ,  0.5 ],

        },

      },

    },

  ],

});

```

```
use   qdrant_client::qdrant::{PointStruct,   Vector}; 

use   std::collections::HashMap; 



client 

     .upsert_points_blocking( 

         "{collection_name}" .to_string(), 

         vec![ 

             PointStruct::new( 

                 1 , 

                 HashMap::from([ 

                     ( 

                         "text" .to_string(), 

                         Vector::from( 

                             (vec![ 6 ,   7 ],   vec![ 1.0 ,   2.0 ]) 

                         ), 

                     ), 

                 ]), 

                 HashMap::new().into(), 

             ), 

             PointStruct::new( 

                 2 , 

                 HashMap::from([ 

                     ( 

                         "text" .to_string(), 

                         Vector::from( 

                             (vec![ 1 ,   2 ,   3 ,   4 ,   5 ],   vec![ 0.1 ,   0.2 ,   0.3 ,   0.4 ,   0.5 ]) 

                         ), 

                     ), 

                 ]), 

                 HashMap::new().into(), 

             ), 

         ], 

         None , 

     ) 

     . await ? ; 

```

## Modify points

To change a point, you can modify its vectors or its payload. There are several
ways to do this.

### Update vectors

 *Available as of v1.2.0* 

This method updates the specified vectors on the given points. Unspecified
vectors are kept unchanged. All given points must exist.

REST API ([ Schema ](https://qdrant.github.io/qdrant/redoc/index.html#operation/update_vectors)):

```
PUT /collections/{collection_name}/points/vectors

{

    "points": [

        {

            "id": 1,

            "vector": {

                "image": [0.1, 0.2, 0.3, 0.4]

            }

        },

        {

            "id": 2,

            "vector": {

                "text": [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

            }

        }

    ]

}

```

```
client . update_vectors(

    collection_name = " {collection_name} " ,

    points = [

        models . PointStruct(

             id = 1 ,

            vector = {

                 "image" : [ 0.1 ,  0.2 ,  0.3 ,  0.4 ],

            },

        ),

        models . PointStruct(

             id = 2 ,

            vector = {

                 "text" : [ 0.9 ,  0.8 ,  0.7 ,  0.6 ,  0.5 ,  0.4 ,  0.3 ,  0.2 ],

            },

        ),

    ],

)

```

```
client.updateVectors( "{collection_name}" , {

  points :  [

    {

      id:  1 ,

      vector :  {

        image :  [ 0.1 ,  0.2 ,  0.3 ,  0.4 ],

      },

    },

    {

      id:  2 ,

      vector :  {

        text :  [ 0.9 ,  0.8 ,  0.7 ,  0.6 ,  0.5 ,  0.4 ,  0.3 ,  0.2 ],

      },

    },

  ],

});

```

```
use   qdrant_client::qdrant::PointVectors; 

use   std::collections::HashMap; 



client 

     .update_vectors_blocking( 

         "{collection_name}" , 

         None , 

         & [ 

             PointVectors   { 

                 id:  Some ( 1. into()), 

                 vectors:  Some ( 

                     HashMap::from([( "image" .to_string(),   vec![ 0.1 ,   0.2 ,   0.3 ,   0.4 ])]).into(), 

                 ), 

             }, 

             PointVectors   { 

                 id:  Some ( 2. into()), 

                 vectors:  Some ( 

                     HashMap::from([( 

                         "text" .to_string(), 

                         vec![ 0.9 ,   0.8 ,   0.7 ,   0.6 ,   0.5 ,   0.4 ,   0.3 ,   0.2 ], 

                     )]) 

                     .into(), 

                 ), 

             }, 

         ], 

         None , 

     ) 

     . await ? ; 

```

To update points and replace all of its vectors, see[ uploading
points ](https://qdrant.tech/documentation/concepts/points/#upload-points).

### Delete vectors

 *Available as of v1.2.0* 

This method deletes just the specified vectors from the given points. Other
vectors are kept unchanged. Points are never deleted.

REST API ([ Schema ](https://qdrant.github.io/qdrant/redoc/index.html#operation/deleted_vectors)):

```
POST /collections/{collection_name}/points/vectors/delete

{

    "points": [0, 3, 100],

    "vectors": ["text", "image"]

}

```

```
client . delete_vectors(

    collection_name = " {collection_name} " ,

    points_selector = models . PointIdsList(

        points = [ 0 ,  3 ,  100 ],

    ),

    vectors = [ "text" ,  "image" ],

)

```

```
client.deleteVectors( "{collection_name}" , {

  points :  [ 0 ,  3 ,  10 ],

  vectors :  [ "text" ,  "image" ],

});

```

```
use   qdrant_client::qdrant::{ 

     points_selector::PointsSelectorOneOf,   PointsIdsList,   PointsSelector,   VectorsSelector, 

}; 



client 

     .delete_vectors_blocking( 

         "{collection_name}" , 

         None , 

         & PointsSelector   { 

             points_selector_one_of:  Some (PointsSelectorOneOf::Points(PointsIdsList   { 

                 ids:  vec ! [ 0. into(),   3. into(),   10. into()], 

             })), 

         }, 

         & VectorsSelector   { 

             names:  vec ! [ "text" .into(),   "image" .into()], 

         }, 

         None , 

     ) 

     . await ? ; 

```

To delete entire points, see[ deleting points ](https://qdrant.tech/documentation/concepts/points/#delete-points).

### Update payload

Learn how to modify the payload of a point in the[ Payload ](../payload/#update-payload)section.

## Delete points

REST API ([ Schema ](https://qdrant.github.io/qdrant/redoc/index.html#operation/delete_points)):

```
POST /collections/{collection_name}/points/delete

{

    "points": [0, 3, 100]

}

```

```
client . delete(

    collection_name = " {collection_name} " ,

    points_selector = models . PointIdsList(

        points = [ 0 ,  3 ,  100 ],

    ),

)

```

```
client. delete ( "{collection_name}" , {

  points :  [ 0 ,  3 ,  100 ],

});

```

```
use   qdrant_client::qdrant::{ 

     points_selector::PointsSelectorOneOf,   PointsIdsList,   PointsSelector, 

}; 



client 

     .delete_points_blocking( 

         "{collection_name}" , 

         None , 

         & PointsSelector   { 

             points_selector_one_of:  Some (PointsSelectorOneOf::Points(PointsIdsList   { 

                 ids:  vec ! [ 0. into(),   3. into(),   100. into()], 

             })), 

         }, 

         None , 

     ) 

     . await ? ; 

```

Alternative way to specify which points to remove is to use filter.

```
POST /collections/{collection_name}/points/delete

{

    "filter": {

        "must": [

            {

                "key": "color",

                "match": {

                    "value": "red"

                }

            }

        ]

    }

}

```

```
client . delete(

    collection_name = " {collection_name} " ,

    points_selector = models . FilterSelector(

         filter = models . Filter(

            must = [

                models . FieldCondition(

                    key = "color" ,

                    match = models . MatchValue(value = "red" ),

                ),

            ],

        )

    ),

)

```

```
client. delete ( "{collection_name}" , {

  filter :  {

    must :  [

      {

        key :   "color" ,

        match :  {

          value :   "red" ,

        },

      },

    ],

  },

});

```

```
use   qdrant_client::qdrant::{ 

     points_selector::PointsSelectorOneOf,   Condition,   Filter,   PointsSelector, 

}; 



client 

     .delete_points_blocking( 

         "{collection_name}" , 

         None , 

         & PointsSelector   { 

             points_selector_one_of:  Some (PointsSelectorOneOf::Filter(Filter::must([ 

                 Condition::matches( "color" ,   "red" .to_string()), 

             ]))), 

         }, 

         None , 

     ) 

     . await ? ; 

```

This example removes all points with `{ "color": "red" }` from the collection.

## Retrieve points

There is a method for retrieving points by their ids.

REST API ([ Schema ](https://qdrant.github.io/qdrant/redoc/index.html#operation/get_points)):

```
POST /collections/{collection_name}/points

{

    "ids": [0, 3, 100]

}

```

```
client . retrieve(

    collection_name = " {collection_name} " ,

    ids = [ 0 ,  3 ,  100 ],

)

```

```
client.retrieve( "{collection_name}" , {

  ids :  [ 0 ,  3 ,  100 ],

});

```

```
client 

     .get_points( 

         "{collection_name}" , 

         None , 

         & [ 0. into(),   30. into(),   100. into()], 

         Some ( false ), 

         Some ( false ), 

         None , 

     ) 

     . await ? ; 

```

This method has additional parameters `with_vectors` and `with_payload` .
Using these parameters, you can select parts of the point you want as a result.
Excluding helps you not to waste traffic transmitting useless data.

The single point can also be retrieved via the API:

REST API ([ Schema ](https://qdrant.github.io/qdrant/redoc/index.html#operation/get_point)):

`GET /collections/{collection_name}/points/{point_id}
`

## Scroll points

Sometimes it might be necessary to get all stored points without knowing ids, or iterate over points that correspond to a filter.

REST API ([ Schema ](https://qdrant.github.io/qdrant/redoc/index.html#operation/scroll_points)):

```
POST /collections/{collection_name}/points/scroll

{

    "filter": {

        "must": [

            {

                "key": "color",

                "match": {

                    "value": "red"

                }

            }

        ]

    },

    "limit": 1,

    "with_payload": true,

    "with_vector": false

}

```

```
client . scroll(

    collection_name = " {collection_name} " ,

    scroll_filter = models . Filter(

        must = [

            models . FieldCondition(key = "color" , match = models . MatchValue(value = "red" )),

        ]

    ),

    limit = 1 ,

    with_payload = True ,

    with_vectors = False ,

)

```

```
client.scroll( "{collection_name}" , {

  filter :  {

    must :  [

      {

        key :   "color" ,

        match :  {

          value :   "red" ,

        },

      },

    ],

  },

  limit:  1 ,

  with_payload:  true ,

  with_vector:  false ,

});

```

```
use   qdrant_client::qdrant::{Condition,   Filter,   ScrollPoints}; 



client 

     .scroll( & ScrollPoints   { 

         collection_name:  "{collection_name}" .to_string(), 

         filter:  Some (Filter::must([Condition::matches( 

             "color" , 

             "red" .to_string(), 

         )])), 

         limit:  Some ( 1 ), 

         with_payload:  Some ( true .into()), 

         with_vectors:  Some ( false .into()), 

         .. Default ::default() 

     }) 

     . await ? ; 

```

Returns all point with `color` = `red` .

```
{

     "result" : {

         "next_page_offset" :  1 ,

         "points" : [

            {

                 "id" :  0 ,

                 "payload" : {

                     "color" :  "red" 

                }

            }

        ]

    },

     "status" :  "ok" ,

     "time" :  0.0001 

}

```

The Scroll API will return all points that match the filter in a page-by-page manner.

All resulting points are sorted by ID. To query the next page it is necessary to specify the largest seen ID in the `offset` field.
For convenience, this ID is also returned in the field `next_page_offset` .
If the value of the `next_page_offset` field is `null` - the last page is reached.

## Counting points

 *Available as of v0.8.4* 

Sometimes it can be useful to know how many points fit the filter conditions without doing a real search.

Among others, for example, we can highlight the following scenarios:

- Evaluation of results size for faceted search
- Determining the number of pages for pagination
- Debugging the query execution speed


REST API ([ Schema ](https://qdrant.github.io/qdrant/redoc/index.html#tag/points/operation/count_points)):

```
POST /collections/{collection_name}/points/count

{

    "filter": {

        "must": [

            {

                "key": "color",

                "match": {

                    "value": "red"

                }

            }

        ]

    },

    "exact": true

}

```

```
client . count(

    collection_name = " {collection_name} " ,

    count_filter = models . Filter(

        must = [

            models . FieldCondition(key = "color" , match = models . MatchValue(value = "red" )),

        ]

    ),

    exact = True ,

)

```

```
client.count( "{collection_name}" , {

  filter :  {

    must :  [

      {

        key :   "color" ,

        match :  {

          value :   "red" ,

        },

      },

    ],

  },

  exact:  true ,

});

```

```
use   qdrant_client::qdrant::{Condition,   CountPoints,   Filter}; 



client 

     .count( & CountPoints   { 

         collection_name:  "{collection_name}" .to_string(), 

         filter:  Some (Filter::must([Condition::matches( 

             "color" , 

             "red" .to_string(), 

         )])), 

         exact:  Some ( true ), 

     }) 

     . await ? ; 

```

Returns number of counts matching given filtering conditions:

```
{

     "count" :  3811 

}

```

## Batch update

 *Available as of v1.5.0* 

You can batch multiple point update operations. This includes inserting,
updating and deleting points, vectors and payload.

A batch update request consists of a list of operations. These are executed in
order. These operations can be batched:

- [ Upsert points ](https://qdrant.tech/documentation/concepts/points/#upload-points): `upsert` or `UpsertOperation`
- [ Delete points ](https://qdrant.tech/documentation/concepts/points/#delete-points): `delete_points` or `DeleteOperation`
- [ Update vectors ](https://qdrant.tech/documentation/concepts/points/#update-vectors): `update_vectors` or `UpdateVectorsOperation`
- [ Delete vectors ](https://qdrant.tech/documentation/concepts/points/#delete-vectors): `delete_vectors` or `DeleteVectorsOperation`
- [ Set payload ](https://qdrant.tech/documentation/concepts/points/#set-payload): `set_payload` or `SetPayloadOperation`
- [ Overwrite payload ](https://qdrant.tech/documentation/concepts/points/#overwrite-payload): `overwrite_payload` or `OverwritePayload`
- [ Delete payload ](https://qdrant.tech/documentation/concepts/points/#delete-payload-keys): `delete_payload` or `DeletePayloadOperation`
- [ Clear payload ](https://qdrant.tech/documentation/concepts/points/#clear-payload): `clear_payload` or `ClearPayloadOperation`


The following example snippet makes use of all operations.

REST API ([ Schema ](https://qdrant.github.io/qdrant/redoc/index.html#tag/points/operation/batch_update)):

```
POST /collections/{collection_name}/points/batch

{

    "operations": [

        {

            "upsert": {

                "points": [

                    {

                        "id": 1,

                        "vector": [1.0, 2.0, 3.0, 4.0],

                        "payload": {}

                    }

                ]

            }

        },

        {

            "update_vectors": {

                "points": [

                    {

                        "id": 1,

                        "vector": [1.0, 2.0, 3.0, 4.0]

                    }

                ]

            }

        },

        {

            "delete_vectors": {

                "points": [1],

                "vector": [""]

            }

        },

        {

            "overwrite_payload": {

                "payload": {

                    "test_payload": "1"

                },

                "points": [1]

            }

        },

        {

            "set_payload": {

                "payload": {

                    "test_payload_2": "2",

                    "test_payload_3": "3"

                },

                "points": [1]

            }

        },

        {

            "delete_payload": {

                "keys": ["test_payload_2"],

                "points": [1]

            }

        },

        {

            "clear_payload": {

                "points": [1]

            }

        },

        {"delete": {"points": [1]}}

    ]

}

```

```
client . batch_update_points(

    collection_name = collection_name,

    update_operations = [

        models . UpsertOperation(

            upsert = models . PointsList(

                points = [

                    models . PointStruct(

                         id = 1 ,

                        vector = [ 1.0 ,  2.0 ,  3.0 ,  4.0 ],

                        payload = {},

                    ),

                ]

            )

        ),

        models . UpdateVectorsOperation(

            update_vectors = models . UpdateVectors(

                points = [

                    models . PointVectors(

                         id = 1 ,

                        vector = [ 1.0 ,  2.0 ,  3.0 ,  4.0 ],

                    )

                ]

            )

        ),

        models . DeleteVectorsOperation(

            delete_vectors = models . DeleteVectors(points = [ 1 ], vector = [ "" ])

        ),

        models . OverwritePayloadOperation(

            overwrite_payload = models . SetPayload(

                payload = { "test_payload" :  1 },

                points = [ 1 ],

            )

        ),

        models . SetPayloadOperation(

            set_payload = models . SetPayload(

                payload = {

                     "test_payload_2" :  2 ,

                     "test_payload_3" :  3 ,

                },

                points = [ 1 ],

            )

        ),

        models . DeletePayloadOperation(

            delete_payload = models . DeletePayload(keys = [ "test_payload_2" ], points = [ 1 ])

        ),

        models . ClearPayloadOperation(clear_payload = models . PointIdsList(points = [ 1 ])),

        models . DeleteOperation(delete = models . PointIdsList(points = [ 1 ])),

    ],

)

```

```
client.batchUpdate( "{collection_name}" , {

  operations :  [

    {

      upsert :  {

        points :  [

          {

            id:  1 ,

            vector :  [ 1.0 ,  2.0 ,  3.0 ,  4.0 ],

            payload :  {},

          },

        ],

      },

    },

    {

      update_vectors :  {

        points :  [

          {

            id:  1 ,

            vector :  [ 1.0 ,  2.0 ,  3.0 ,  4.0 ],

          },

        ],

      },

    },

    {

      delete_vectors :  {

        points :  [ 1 ],

        vector :  [ "" ],

      },

    },

    {

      overwrite_payload :  {

        payload :  {

          test_payload:  1 ,

        },

        points :  [ 1 ],

      },

    },

    {

      set_payload :  {

        payload :  {

          test_payload_2:  2 ,

          test_payload_3:  3 ,

        },

        points :  [ 1 ],

      },

    },

    {

      delete_payload :  {

        keys :  [ "test_payload_2" ],

        points :  [ 1 ],

      },

    },

    {

      clear_payload :  {

        points :  [ 1 ],

      },

    },

    {

       delete :  {

        points :  [ 1 ],

      },

    },

  ],

});

```

```
use   qdrant_client::qdrant::{ 

     points_selector::PointsSelectorOneOf, 

     points_update_operation::{ 

         DeletePayload,   DeleteVectors,   Operation,   PointStructList,   SetPayload,   UpdateVectors, 

     }, 

     PointStruct,   PointVectors,   PointsIdsList,   PointsSelector,   PointsUpdateOperation, 

     VectorsSelector, 

}; 

use   serde_json::json; 

use   std::collections::HashMap; 



client 

     .batch_updates_blocking( 

         "{collection_name}" , 

         & [ 

             PointsUpdateOperation   { 

                 operation:  Some (Operation::Upsert(PointStructList   { 

                     points:  vec ! [PointStruct::new( 

                         1 , 

                         vec![ 1.0 ,   2.0 ,   3.0 ,   4.0 ], 

                         json ! ({}).try_into().unwrap(), 

                     )], 

                 })), 

             }, 

             PointsUpdateOperation   { 

                 operation:  Some (Operation::UpdateVectors(UpdateVectors   { 

                     points:  vec ! [PointVectors   { 

                         id:  Some ( 1. into()), 

                         vectors:  Some (vec![ 1.0 ,   2.0 ,   3.0 ,   4.0 ].into()), 

                     }], 

                 })), 

             }, 

             PointsUpdateOperation   { 

                 operation:  Some (Operation::DeleteVectors(DeleteVectors   { 

                     points_selector:  Some (PointsSelector   { 

                         points_selector_one_of:  Some (PointsSelectorOneOf::Points( 

                             PointsIdsList   { 

                                 ids:  vec ! [ 1. into()], 

                             }, 

                         )), 

                     }), 

                     vectors:  Some (VectorsSelector   { 

                         names:  vec ! [ "" .into()], 

                     }), 

                 })), 

             }, 

             PointsUpdateOperation   { 

                 operation:  Some (Operation::OverwritePayload(SetPayload   { 

                     points_selector:  Some (PointsSelector   { 

                         points_selector_one_of:  Some (PointsSelectorOneOf::Points( 

                             PointsIdsList   { 

                                 ids:  vec ! [ 1. into()], 

                             }, 

                         )), 

                     }), 

                     payload:  HashMap ::from([( "test_payload" .to_string(),   1. into())]), 

                 })), 

             }, 

             PointsUpdateOperation   { 

                 operation:  Some (Operation::SetPayload(SetPayload   { 

                     points_selector:  Some (PointsSelector   { 

                         points_selector_one_of:  Some (PointsSelectorOneOf::Points( 

                             PointsIdsList   { 

                                 ids:  vec ! [ 1. into()], 

                             }, 

                         )), 

                     }), 

                     payload:  HashMap ::from([ 

                         ( "test_payload_2" .to_string(),   2. into()), 

                         ( "test_payload_3" .to_string(),   3. into()), 

                     ]), 

                 })), 

             }, 

             PointsUpdateOperation   { 

                 operation:  Some (Operation::DeletePayload(DeletePayload   { 

                     points_selector:  Some (PointsSelector   { 

                         points_selector_one_of:  Some (PointsSelectorOneOf::Points( 

                             PointsIdsList   { 

                                 ids:  vec ! [ 1. into()], 

                             }, 

                         )), 

                     }), 

                     keys:  vec ! [ "test_payload_2" .to_string()], 

                 })), 

             }, 

             PointsUpdateOperation   { 

                 operation:  Some (Operation::ClearPayload(PointsSelector   { 

                     points_selector_one_of:  Some (PointsSelectorOneOf::Points(PointsIdsList   { 

                         ids:  vec ! [ 1. into()], 

                     })), 

                 })), 

             }, 

             PointsUpdateOperation   { 

                 operation:  Some (Operation::Delete(PointsSelector   { 

                     points_selector_one_of:  Some (PointsSelectorOneOf::Points(PointsIdsList   { 

                         ids:  vec ! [ 1. into()], 

                     })), 

                 })), 

             }, 

         ], 

         None , 

     ) 

     . await ? ; 

```

To batch many points with a single operation type, please use batching
functionality in that operation directly.

##### Table of contents

- [ Awaiting result ](https://qdrant.tech/documentation/concepts/points/#awaiting-result)
- [ Point IDs ](https://qdrant.tech/documentation/concepts/points/#point-ids)
- [ Upload points ](https://qdrant.tech/documentation/concepts/points/#upload-points)
- [ Modify points ](https://qdrant.tech/documentation/concepts/points/#modify-points)
    - [ Update vectors ](https://qdrant.tech/documentation/concepts/points/#update-vectors)

- [ Delete vectors ](https://qdrant.tech/documentation/concepts/points/#delete-vectors)

- [ Update payload ](https://qdrant.tech/documentation/concepts/points/#update-payload)
- [ Delete points ](https://qdrant.tech/documentation/concepts/points/#delete-points)
- [ Retrieve points ](https://qdrant.tech/documentation/concepts/points/#retrieve-points)
- [ Scroll points ](https://qdrant.tech/documentation/concepts/points/#scroll-points)
- [ Counting points ](https://qdrant.tech/documentation/concepts/points/#counting-points)
- [ Batch update ](https://qdrant.tech/documentation/concepts/points/#batch-update)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/points.md)
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