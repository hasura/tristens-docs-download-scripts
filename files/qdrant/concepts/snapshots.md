# Snapshots

 *Available as of v0.8.4* 

Snapshots are performed on a per-collection basis and consist in a `tar` archive file containing the necessary data to restore the collection at the time of the snapshot.

This feature can be used to archive data or easily replicate an existing deployment.

## Store snapshots

The target directory used to store generated snapshots is controlled through the[ configuration ](../../guides/configuration)or using the ENV variable: `QDRANT__STORAGE__SNAPSHOTS_PATH=./snapshots` .

You can set the snapshots storage directory from the[ config.yaml ](https://github.com/qdrant/qdrant/blob/master/config/config.yaml)file. If no value is given, default is `./snapshots` .

```
storage : 

   # Specify where you want to store snapshots. 

   snapshots_path :   ./snapshots 

```

 *Available as of v1.3.0* 

While a snapshot is being created, temporary files are by default placed in the configured storage directory.
This location may have limited capacity or be on a slow network-attached disk. You may specify a separate location for temporary files:

```
storage : 

   # Where to store temporary files 

   temp_path :   /tmp 

```

## Create snapshot

To create a new snapshot for an existing collection:

`POST /collections/{collection_name}/snapshots
`

```
from   qdrant_client   import  QdrantClient



client  =  QdrantClient( "localhost" , port = 6333 )



client . create_snapshot(collection_name = " {collection_name} " )

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.createSnapshot( "{collection_name}" );

```

```
use   qdrant_client::client::QdrantClient; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client.create_snapshot( "{collection_name}" ). await ? ; 

```

This is a synchronous operation for which a `tar` archive file will be generated into the `snapshot_path` .

### Delete snapshot

 *Available as of v1.0.0* 

`DELETE /collections/{collection_name}/snapshots/{snapshot_name}
`

```
from   qdrant_client   import  QdrantClient



client  =  QdrantClient( "localhost" , port = 6333 )



client . delete_snapshot(

    collection_name = " {collection_name} " , snapshot_name = " {snapshot_name} " 

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.deleteSnapshot( "{collection_name}" ,  "{snapshot_name}" );

```

```
use   qdrant_client::client::QdrantClient; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client.delete_snapshot( "{collection_name}" ,   "{snapshot_name}" ). await ? ; 

```

## List snapshot

List of snapshots for a collection:

`GET /collections/{collection_name}/snapshots
`

```
from   qdrant_client   import  QdrantClient



client  =  QdrantClient( "localhost" , port = 6333 )



client . list_snapshots(collection_name = " {collection_name} " )

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.listSnapshots( "{collection_name}" );

```

```
use   qdrant_client::client::QdrantClient; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client.list_snapshots( "{collection_name}" ). await ? ; 

```

## Retrieve snapshot

To download a specified snapshot from a collection as a file:

`GET /collections/{collection_name}/snapshots/{snapshot_name}
`

## Restore snapshot

There is a difference in recovering snapshots in single-deployment node and distributed deployment mode.

### Recover during start-up

Single deployment is simpler, you can recover any collection on the start-up and it will be immediately available in the service.
Restoring snapshots is done through the Qdrant CLI at startup time.

The main entry point is the `--snapshot` argument which accepts a list of pairs `<snapshot_file_path>:<target_collection_name>` 

For example:

`./qdrant --snapshot /snapshots/test-collection-archive.snapshot:test-collection --snapshot /snapshots/test-collection-archive.snapshot:test-copy-collection 
`

The target collection **must** be absent otherwise the program will exit with an error.

If you wish instead to overwrite an existing collection, use the `--force_snapshot` flag with caution.

### Recover via API

 *Available as of v0.11.3* 

Recovering in cluster mode is more sophisticated, as Qdrant should maintain consistency across peers even during the recovery process.
As the information about created collections is stored in the consensus, even a newly attached cluster node will automatically create collections.
Recovering non-existing collections with snapshots won’t make this collection known to the consensus.

To recover snapshot via API one can use snapshot recovery endpoint:

```
PUT /collections/{collection_name}/snapshots/recover

{

  "location": "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.shapshot"

}

```

```
from   qdrant_client   import  QdrantClient



client  =  QdrantClient( "qdrant-node-2" , port = 6333 )



client . recover_snapshot(

     " {collection_name} " ,

     "http://qdrant-node-1:6333/collections/collection_name/snapshots/snapshot-2022-10-10.shapshot" ,

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.recoverSnapshot( "{collection_name}" , {

  location :   "http://qdrant-node-1:6333/collections/collection_name/snapshots/snapshot-2022-10-10.shapshot" ,

});

```

The recovery snapshot can also be uploaded as a file to the Qdrant server:

```
curl -X POST  'http://qdrant-node-1:6333/collections/collection_name/snapshots/upload'   \

    -H  'Content-Type:multipart/form-data'   \

    -F  'snapshot=@/path/to/snapshot-2022-10-10.shapshot' 

```

Qdrant will extract shard data from the snapshot and properly register shards in the cluster.
If there are other active replicas of the recovered shards in the cluster, Qdrant will replicate them to the newly recovered node by default to maintain data consistency.

### Snapshot priority

When recovering a snapshot, you can specify what source of data is prioritized
during recovery. It is important because different priorities can give very
different end results. The default priority is probably not what you expect.

The available snapshot recovery priorities are:

- `replica` : *(default)* prefer existing data over the snapshot.
- `snapshot` : prefer snapshot data over existing data.
- `no_sync` : restore snapshot without any additional synchronization.


To recover a new collection from a snapshot on a Qdrant cluster, you need to set
the `snapshot` priority. With `snapshot` priority, all data from the snapshot
will be recovered onto the cluster. With `replica` priority *(default)* , you’d
end up with an empty collection because the collection on the cluster did not
contain any points and that source was preferred.

 `no_sync` is for specialized use cases and is not commonly used. It allows
managing shards and transferring shards between clusters manually without any
additional synchronization. Using it incorrectly will leave your cluster in a
broken state.

To recover from an URL you specify a request parameter:

```
PUT /collections/{collection_name}/snapshots/recover

{

  "location": "http://qdrant-node-1:6333/collections/{collection_name}/snapshots/snapshot-2022-10-10.shapshot",

  "priority": "snapshot"

}

```

```
from   qdrant_client   import  QdrantClient, models



client  =  QdrantClient( "qdrant-node-2" , port = 6333 )



client . recover_snapshot(

     " {collection_name} " ,

     "http://qdrant-node-1:6333/collections/collection_name/snapshots/snapshot-2022-10-10.shapshot" ,

    priority = models . SnapshotPriority . SNAPSHOT,

)

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.recoverSnapshot( "{collection_name}" , {

  location :   "http://qdrant-node-1:6333/collections/collection_name/snapshots/snapshot-2022-10-10.shapshot" ,

  priority :   "snapshot" 

});

```

To upload a multipart file you specify it as URL parameter:

```
curl -X POST  'http://qdrant-node-1:6333/collections/collection_name/snapshots/upload?priority=snapshot'   \

    -H  'Content-Type:multipart/form-data'   \

    -F  'snapshot=@/path/to/snapshot-2022-10-10.shapshot' 

```

## Snapshots for the whole storage

 *Available as of v0.8.5* 

Sometimes it might be handy to create snapshot not just for a single collection, but for the whole storage, including collection aliases.
Qdrant provides a dedicated API for that as well. It is similar to collection-level snapshots, but does not require `collecton_name` :

### Create full storage snapshot

`POST /snapshots
`

```
from   qdrant_client   import  QdrantClient



client  =  QdrantClient( "localhost" , port = 6333 )



client . create_full_snapshot()

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.createFullSnapshot();

```

```
use   qdrant_client::client::QdrantClient; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client.create_full_snapshot(). await ? ; 

```

### Delete full storage snapshot

 *Available as of v1.0.0* 

`DELETE /snapshots/{snapshot_name}
`

```
from   qdrant_client   import  QdrantClient



client  =  QdrantClient( "localhost" , port = 6333 )



client . delete_full_snapshot(snapshot_name = " {snapshot_name} " )

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.deleteFullSnapshot( "{snapshot_name}" );

```

```
use   qdrant_client::client::QdrantClient; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client.delete_full_snapshot( "{snapshot_name}" ). await ? ; 

```

### List full storage snapshots

`GET /snapshots
`

```
from   qdrant_client   import  QdrantClient



client  =  QdrantClient( "localhost" , port = 6333 )



client . list_full_snapshots()

```

```
import  { QdrantClient }  from   "@qdrant/js-client-rest" ;



const  client  =   new  QdrantClient({ host :   "localhost" , port:  6333  });



client.listFullSnapshots();

```

```
use   qdrant_client::client::QdrantClient; 



let   client   =   QdrantClient::from_url( "http://localhost:6334" ).build() ? ; 



client.list_full_snapshots(). await ? ; 

```

### Download full storage snapshot

`GET /snapshots/{snapshot_name}
`

## Restore full storage snapshot

Restoring snapshots is done through the Qdrant CLI at startup time.

For example:

`./qdrant --storage-snapshot /snapshots/full-snapshot-2022-07-18-11-20-51.snapshot 
`

##### Table of contents

- [ Store snapshots ](https://qdrant.tech/documentation/concepts/snapshots/#store-snapshots)
- [ Create snapshot ](https://qdrant.tech/documentation/concepts/snapshots/#create-snapshot)
    - [ Delete snapshot ](https://qdrant.tech/documentation/concepts/snapshots/#delete-snapshot)
- [ List snapshot ](https://qdrant.tech/documentation/concepts/snapshots/#list-snapshot)
- [ Retrieve snapshot ](https://qdrant.tech/documentation/concepts/snapshots/#retrieve-snapshot)
- [ Restore snapshot ](https://qdrant.tech/documentation/concepts/snapshots/#restore-snapshot)
    - [ Recover during start-up ](https://qdrant.tech/documentation/concepts/snapshots/#recover-during-start-up)

- [ Recover via API ](https://qdrant.tech/documentation/concepts/snapshots/#recover-via-api)

- [ Snapshot priority ](https://qdrant.tech/documentation/concepts/snapshots/#snapshot-priority)
- [ Snapshots for the whole storage ](https://qdrant.tech/documentation/concepts/snapshots/#snapshots-for-the-whole-storage)
    - [ Create full storage snapshot ](https://qdrant.tech/documentation/concepts/snapshots/#create-full-storage-snapshot)

- [ Delete full storage snapshot ](https://qdrant.tech/documentation/concepts/snapshots/#delete-full-storage-snapshot)

- [ List full storage snapshots ](https://qdrant.tech/documentation/concepts/snapshots/#list-full-storage-snapshots)

- [ Download full storage snapshot ](https://qdrant.tech/documentation/concepts/snapshots/#download-full-storage-snapshot)
- [ Restore full storage snapshot ](https://qdrant.tech/documentation/concepts/snapshots/#restore-full-storage-snapshot)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/concepts/snapshots.md)
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