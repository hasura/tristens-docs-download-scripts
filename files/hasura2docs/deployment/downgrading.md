# Downgrade Hasura GraphQL Engine

## Step 1: Update Hasura GraphQL Engine image version​

The Hasura GraphQL Engine runs off a Docker image and downgrades are as
simple as changing the image tag to the version you want.

Based on your deployment method, follow the appropriate guide to
downgrade the GraphQL Engine version you're running:

- [ Updating on Docker ](https://hasura.io/docs/latest/deployment/deployment-guides/docker/#docker-update)
- [ Updating on Kubernetes ](https://hasura.io/docs/latest/deployment/deployment-guides/kubernetes/#kubernetes-update)


If the GraphQL Engine version you are downgrading to has a different
catalog version than your current, you will have to downgrade the
catalog to the corresponding version manually as described below.

## Step 2: Downgrade Hasura catalog version​

The Hasura GraphQL Engine maintains its Metadata state in a "catalog"
as described[ here ](https://hasura.io/docs/latest/migrations-metadata-seeds/metadata-format/). The schema of the
catalog is versioned. Updates to the Hasura GraphQL Engine may have
Hasura catalog version bumps.

Downgrades to the catalog need to be carried out manually in case you
are attempting to downgrade to a lower Hasura GraphQL Engine version.

From `v1.2.0` , you can downgrade the catalog from a particular version
to a previous version by executing the `graphql-engine` executable on
the command line, with the `downgrade` command, specifying the desired
catalog version using one of the `--to-` flags. For earlier versions,
it is recommended to first upgrade to the latest version and then use
the `downgrade` command to downgrade to the desired version.

The `downgrade` command is not part of the Hasura CLI but rather a
command on `graphql-engine` itself. The way to execute this command is
to run:

`docker  run -e  HASURA_GRAPHQL_DATABASE_URL = $DATABASE_URL  hasura/graphql-engine: < VERSION >  graphql-engine downgrade --to- < NEW-VERSION >`

You need to use a newer version of `graphql-engine` to downgrade to an
older version, since only the newer version knows how to downgrade from
that point in time. After you’ve executed the `downgrade` command using
the newer version, you should switch to the older version and run `graphql-engine serve` as normal.

Catalogue version downgrades will be executed sequentially and in a
single transaction.

Note

Running this command while Hasura GraphQL Engine is running might lead
to unexpected results. It is recommended to first bring down any running
Hasura GraphQL Engine instances before downgrading the catalog

Note

You can downgrade a Hasura GraphQL Engine v2 instance to v1 only if
there is only one database connected to it.

Issues with downgrading the catalog version?

Please note that downgrading the Hasura catalog version is unavailable from `v2.12.1` onward. We apologize for the inconvenience
and are working to restore this feature as soon as possible. In the meantime, should you need to execute the migration manually,
you can utilize the following SQL on your Metadata database:

```
ALTER   TABLE  hdb_catalog . hdb_version
   DROP   COLUMN  ee_client_id ,
   DROP   COLUMN  ee_client_secret ;
INSERT   INTO  hdb_catalog . hdb_version  ( version ,  upgraded_on )   VALUES   ( 47 ,   NOW ( ) )
     ON  CONFLICT  ( ( version  IS   NOT   NULL ) )
     DO   UPDATE   SET  version  =  EXCLUDED . version ;
```

This will downgrade your Hasura instance from catalog version 48 to version 47, which was introduced in `v2.0.7` .

### What did you think of this doc?

- [ Step 1: Update Hasura GraphQL Engine image version ](https://hasura.io/docs/latest/deployment/downgrading/#step-1-update-hasura-graphql-engine-image-version)
- [ Step 2: Downgrade Hasura catalog version ](https://hasura.io/docs/latest/deployment/downgrading/#step-2-downgrade-hasura-catalog-version)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)