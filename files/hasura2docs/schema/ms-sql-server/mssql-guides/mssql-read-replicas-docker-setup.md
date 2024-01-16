# MS SQL Server Read Replicas Using Docker

## Introduction​

The following tutorial helps setting up a Docker container setup for the MS SQL Server Read Replicas.

This tutorial was highly influenced by[ this blog ](https://dbtut.com/index.php/2020/06/09/sql-server-2019-alwayson-availability-group-on-docker-containers)

## Step 1: Set up the Docker image with SQL Server​

### Create Docker file​

```
FROM  ubuntu:18.04
ARG  DEBIAN_FRONTEND=noninteractive
RUN  apt-get update
RUN  apt-get install apt-utils -y
RUN  apt-get install sudo wget curl gnupg gnupg1 gnupg2 -y
RUN  apt-get install software-properties-common systemd vim -y
RUN  wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
RUN  add-apt-repository  "$(wget -qO- https://packages.microsoft.com/config/ubuntu/18.04/mssql-server-2019.list)"
RUN  apt-get update
RUN  apt-get install -y mssql-server
RUN  /opt/mssql/bin/mssql-conf set hadr.hadrenabled  1
RUN  /opt/mssql/bin/mssql-conf set sqlagent.enabled true
EXPOSE  1433
ENTRYPOINT  /opt/mssql/bin/sqlservr
```

### Build Docker image​

`docker  build -t sqlag:ha  .`

## Step 2: Create the Docker configuration file with 3 SQL nodes​

Create three nodes:

- **sqlNode1** : Primary server
- **sqlNode2** and **sqlNode3** : Secondary Servers


```
services :
   db1 :
     container_name :  sqlNode1
     image :  sqlag : ha
     hostname :  sqlNode1
     domainname :  lab.local
     environment :
       SA_PASSWORD :   'Password1'
       ACCEPT_EULA :   'Y'
     ports :
       -   '1501:1433'
     extra_hosts :
       sqlNode2.labl.local :   '172.16.238.22'
       sqlNode3.labl.local :   '172.16.238.23'
     networks :
       internal :
         ipv4_address :  172.16.238.21
   db2 :
     container_name :  sqlNode2
     image :  sqlag : ha
     hostname :  sqlNode2
     domainname :  lab.local
     environment :
       SA_PASSWORD :   'Password1'
       ACCEPT_EULA :   'Y'
     ports :
       -   '1502:1433'
     extra_hosts :
       sqlNode1.lab.local :   '172.16.238.21'
       sqlNode3.lab.local :   '172.16.238.23'
     networks :
       internal :
         ipv4_address :  172.16.238.22
   db3 :
     container_name :  sqlNode3
     image :  sqlag : ha
     hostname :  sqlNode3
     domainname :  lab.local
     environment :
       SA_PASSWORD :   'Password1'
       ACCEPT_EULA :   'Y'
     ports :
       -   '1503:1433'
     extra_hosts :
       sqlNode1.lab.local :   '172.16.238.21'
       sqlNode2.lab.local :   '172.16.238.22'
     networks :
       internal :
         ipv4_address :  172.16.238.23
networks :
internal :
   ipam :
     driver :  default
     config :
       -   subnet :  172.16.238.0/24
```

`docker  compose up -d`

## Step 3: Figure the IP address of the gateway to connect​

```
$ >   ifconfig
br-7d762e376414:  flags = 416 3 < UP,BROADCAST,RUNNING,MULTICAST >   mtu  1500
     inet  172.16 .238.1  netmask  255.255 .255.0  broadcast  172.16 .238.255
     inet6 fe80::42:b0ff:fe8b:57ef  prefixlen  64   scopeid 0x2 0 < link >
     ether 02:42:b0:8b:57:ef  txqueuelen  0    ( Ethernet )
     RX packets  20022   bytes  2157399   ( 2.1  MB )
     RX errors  0   dropped  0   overruns  0   frame  0
     TX packets  36571   bytes  8365375   ( 8.3  MB )
     TX errors  0   dropped  0  overruns  0   carrier  0   collisions  0
```

From above, you can notice that the docker gateway is `172.16.238.1` , Once the docker container is up, we can connect to
the sql server via `172.16.238.1` and `1501` , `1502` and `1503` ports.

Test it out by trying to connect to any one of the node:

`$ >  sqlcmd -S  172.16 .238.1,1501 -U SA -P  "Password1"`

```
1 >   SELECT  name  FROM  master . dbo . sysdatabases ;
2 >  GO
```

## Step 4: Create certificates​

Follow the steps to create certificates on the nodes:

1. Create certificate for primary node, store it in a temp location in the node
2. Copy the certificate from the primary node to local system
3. Copy the certificate from local system to secondary nodes
4. Apply the certificate on secondary nodes


```
USE  master
GO
CREATE  LOGIN dbm_login  WITH  PASSWORD  =   'Password1' ;
CREATE   USER  dbm_user  FOR  LOGIN dbm_login ;
GO
CREATE  MASTER  KEY  ENCRYPTION  BY  PASSWORD  =   'Password1' ;
go
CREATE  CERTIFICATE dbm_certificate  WITH  SUBJECT  =   'dbm' ;
BACKUP  CERTIFICATE dbm_certificate
TO   FILE   =   '/tmp/dbm_certificate.cer'
WITH  PRIVATE  KEY   (
       FILE   =   '/tmp/dbm_certificate.pvk' ,
      ENCRYPTION  BY  PASSWORD  =   'Password1'
    ) ;
GO
```

Store the above sql file in `1-primary-setup-certificate.sql` . Then apply the transaction to primary node via the
following.

`sqlcmd -S  172.16 .238.1,1501 -U SA -P  "Password1"  -i  1 -primary-setup-certificate.sql`

Please note that for the rest of the setup, it would be easier if we do the following: 1. Create a sql file with the
transaction 2. Run the transaction via sqlcmd

Now, let's copy the certificate from primary and paste them into the secondary nodes.

```
docker   cp  sqlNode1:/tmp/dbm_certificate.cer  .
docker   cp  sqlNode1:/tmp/dbm_certificate.pvk  .
docker   cp  dbm_certificate.cer sqlNode2:/tmp/
docker   cp  dbm_certificate.pvk sqlNode2:/tmp/
docker   cp  dbm_certificate.cer sqlNode3:/tmp/
docker   cp  dbm_certificate.pvk sqlNode3:/tmp/
```

Connect to all the secondary nodes and execute the following SQL:

```
CREATE  LOGIN dbm_login  WITH  PASSWORD  =   'Password1' ;
CREATE   USER  dbm_user  FOR  LOGIN dbm_login ;
GO
CREATE  MASTER  KEY  ENCRYPTION  BY  PASSWORD  =   'Password1' ;
-- ALTER MASTER KEY REGENERATE WITH ENCRYPTION BY PASSWORD = 'Password1';
GO
CREATE  CERTIFICATE dbm_certificate
    AUTHORIZATION  dbm_user
    FROM   FILE   =   '/tmp/dbm_certificate.cer'
    WITH  PRIVATE  KEY   (
    FILE   =   '/tmp/dbm_certificate.pvk' ,
   DECRYPTION  BY  PASSWORD  =   'Password1'
) ;
```

## Step 5: Create the endpoint for Always On and setup health monitoring for the server​

Execute the following SQL first on primary node and then on the secondary nodes.

```
CREATE  ENDPOINT  [ Hadr_endpoint ]
    AS  TCP  ( LISTENER_IP  =   ( 0.0 .0 .0 ) ,  LISTENER_PORT  =   5022 )
    FOR  DATA_MIRRORING  (
      ROLE  =   ALL ,
      AUTHENTICATION  =  CERTIFICATE dbm_certificate ,
      ENCRYPTION  =  REQUIRED  ALGORITHM  AES
       ) ;
ALTER  ENDPOINT  [ Hadr_endpoint ]  STATE  =  STARTED ;
GRANT   CONNECT   ON  ENDPOINT:: [ Hadr_endpoint ]   TO   [ dbm_login ] ;
```

To enable the health monitoring, execute the SQL on all nodes:

```
ALTER  EVENT  SESSION   AlwaysOn_health  ON  SERVER  WITH   ( STARTUP_STATE = ON ) ;
GO
```

## Step 6: Create Always on Availability Group​

Execute the following SQL on primary node.

```
CREATE  AVAILABILITY  GROUP   [ AG1 ]
       WITH   ( CLUSTER_TYPE  =  NONE )
       FOR  REPLICA  ON
      N 'sqlNode1'
             WITH   (
            ENDPOINT_URL  =  N 'tcp://sqlNode1:5022' ,
            AVAILABILITY_MODE  =  ASYNCHRONOUS_COMMIT ,
               SEEDING_MODE  =  AUTOMATIC ,
               FAILOVER_MODE  =  MANUAL ,
            SECONDARY_ROLE  ( ALLOW_CONNECTIONS  =   ALL )
                ) ,
      N 'sqlNode2'
             WITH   (
            ENDPOINT_URL  =  N 'tcp://sqlNode2:5022' ,
            AVAILABILITY_MODE  =  ASYNCHRONOUS_COMMIT ,
               SEEDING_MODE  =  AUTOMATIC ,
               FAILOVER_MODE  =  MANUAL ,
            SECONDARY_ROLE  ( ALLOW_CONNECTIONS  =   ALL )
                ) ,
      N 'sqlNode3'
             WITH   (
            ENDPOINT_URL  =  N 'tcp://sqlNode3:5022' ,
            AVAILABILITY_MODE  =  ASYNCHRONOUS_COMMIT ,
               SEEDING_MODE  =  AUTOMATIC ,
               FAILOVER_MODE  =  MANUAL ,
            SECONDARY_ROLE  ( ALLOW_CONNECTIONS  =   ALL )
                ) ;
GO
ALTER  AVAILABILITY  GROUP   [ ag1 ]   GRANT   CREATE   ANY   DATABASE ;
GO
```

## Step 7: Join the secondary nodes to Availability Group (AG)​

Execute the following SQL only on secondary nodes.

```
ALTER  AVAILABILITY  GROUP   [ ag1 ]   JOIN   WITH   ( CLUSTER_TYPE  =  NONE ) ;
ALTER  AVAILABILITY  GROUP   [ ag1 ]   GRANT   CREATE   ANY   DATABASE ;
GO
```

## Step 8: Setting up the primary node with some values and database​

In this step, we'll create a database on primary and add some data to it and verify that the replication happens on
secondary nodes successfully.

Execute the following SQL on primary node.

```
CREATE   DATABASE  agtestdb ;
GO
ALTER   DATABASE  agtestdb  SET  RECOVERY  FULL ;
GO
BACKUP   DATABASE  agtestdb  TO   DISK   =   '/var/opt/mssql/data/agtestdb.bak' ;
GO
ALTER  AVAILABILITY  GROUP   [ ag1 ]   ADD   DATABASE   [ agtestdb ] ;
GO
USE  agtestdb ;
GO
CREATE   TABLE  inventory  ( id  INT ,  name NVARCHAR ( 50 ) ,  quantity  INT ) ;
GO
INSERT   INTO  inventory  VALUES   ( 1 ,   'banana' ,   150 ) ;   INSERT   INTO  Inventory  VALUES   ( 2 ,   'orange' ,   154 ) ;
GO
```

Connect to secondary replica and see the database and values. Test if the database has been replicated on secondary
nodes

```
➜ sqlcmd -S  172.16 .238.1,1502 -U SA -P  "Password1"
1 >  SELECT name FROM master.dbo.sysdatabases ;
2 >  GO
```

## Step 9: Setup Routing List URL​

In this step, we'll do the following:

1. Change the secondary replicas to allow read only connections
2. Create read only routing url for each nodes
3. Create the routing list


Note that, the read only routing URL should be such that you are able to connect from outside the container, so it's
better to provide the actual IP of the node.

Execute the following SQL on primary node.

```
ALTER  AVAILABILITY  GROUP   [ AG1 ]
MODIFY  REPLICA  ON
N 'sqlNode1'   WITH
    ( SECONDARY_ROLE  ( ALLOW_CONNECTIONS  =  READ_ONLY ) ) ;
ALTER  AVAILABILITY  GROUP   [ AG1 ]
MODIFY  REPLICA  ON
N 'sqlNode1'   WITH
    ( SECONDARY_ROLE  ( READ_ONLY_ROUTING_URL  =  N 'tcp://172.16.238.21:1433' ) ) ;
ALTER  AVAILABILITY  GROUP   [ AG1 ]
MODIFY  REPLICA  ON
N 'sqlNode2'   WITH
    ( SECONDARY_ROLE  ( ALLOW_CONNECTIONS  =  READ_ONLY ) ) ;
ALTER  AVAILABILITY  GROUP   [ AG1 ]
MODIFY  REPLICA  ON
N 'sqlNode2'   WITH
    ( SECONDARY_ROLE  ( READ_ONLY_ROUTING_URL  =  N 'tcp://172.16.238.22:1433' ) ) ;
ALTER  AVAILABILITY  GROUP   [ AG1 ]
MODIFY  REPLICA  ON
N 'sqlNode3'   WITH
       ( SECONDARY_ROLE  ( ALLOW_CONNECTIONS  =  READ_ONLY ) ) ;
ALTER  AVAILABILITY  GROUP   [ AG1 ]
MODIFY  REPLICA  ON
N 'sqlNode3'   WITH
       ( SECONDARY_ROLE  ( READ_ONLY_ROUTING_URL  =  N 'tcp://172.16.238.23:1433' ) ) ;
ALTER  AVAILABILITY  GROUP   [ AG1 ]
MODIFY  REPLICA  ON
N 'sqlNode1'   WITH
    ( PRIMARY_ROLE  ( READ_ONLY_ROUTING_LIST = ( ( 'sqlNode3' , 'sqlNode2' ) , 'sqlnode1' ) ) ) ;
ALTER  AVAILABILITY  GROUP   [ AG1 ]
MODIFY  REPLICA  ON
N 'sqlNode2'   WITH
    ( PRIMARY_ROLE  ( READ_ONLY_ROUTING_LIST = ( ( 'sqlNode1' , 'sqlNode3' ) , 'sqlnode2' ) ) ) ;
ALTER  AVAILABILITY  GROUP   [ AG1 ]
MODIFY  REPLICA  ON
N 'sqlNode3'   WITH
       ( PRIMARY_ROLE  ( READ_ONLY_ROUTING_LIST = ( ( 'sqlNode1' , 'sqlNode2' ) , 'sqlnode3' ) ) ) ;
GO
```

## Step 10: Create the listener URL​

This listener URL is used to route the Read only request to one of the Read only secondary replicas

Execute the following SQL on primary node.

```
ALTER  AVAILABILITY  GROUP   [ AG1 ]  REMOVE LISTENER  'AGListener' ;
GO
ALTER  AVAILABILITY  GROUP   [ AG1 ]
       ADD  LISTENER  'AGListener'   (   WITH  IP  (   ( N '172.16.238.21' ,  N '255.255.255.0' )   )   ,  PORT  =   1434   ) ;
GO
```

Let's go ahead and test, if we could connect to our secondary replicas using the listener URL. Note that, since we
marked read replicas as `ReadOnly` , we will only be able to connect to secondary nodes only when we provide the
ApplicationIntent as `ReadOnly` 

Let's first connect to out primary replica

`sqlcmd  - S  172.16 .238 .21 , 1434   - U SA   - d agtestdb  - P  "Password1"`

Now let's connect to secondary replicas using ReadIntent Only

`sqlcmd  - S  172.16 .238 .21 , 1434   - U SA   - d agtestdb  - P  "Password1"   - K ReadOnly`

## Next Steps​

With your read replicas set up, consider learning more about Hasura's[ Migrations, Metadata, and Seeds ](https://hasura.io/docs/latest/migrations-metadata-seeds/overview/).

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#introduction)
- [ Step 1: Set up the Docker image with SQL Server ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#step-1-set-up-the-docker-image-with-sql-server)
    - [ Create Docker file ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#create-docker-file)

- [ Build Docker image ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#build-docker-image)
- [ Step 2: Create the Docker configuration file with 3 SQL nodes ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#step-2-create-the-docker-configuration-file-with-3-sql-nodes)
- [ Step 3: Figure the IP address of the gateway to connect ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#step-3-figure-the-ip-address-of-the-gateway-to-connect)
- [ Step 4: Create certificates ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#step-4-create-certificates)
- [ Step 5: Create the endpoint for Always On and setup health monitoring for the server ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#step-5-create-the-endpoint-for-always-on-and-setup-health-monitoring-for-the-server)
- [ Step 6: Create Always on Availability Group ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#step-6-create-always-on-availability-group)
- [ Step 7: Join the secondary nodes to Availability Group (AG) ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#step-7-join-the-secondary-nodes-to-availability-group-ag)
- [ Step 8: Setting up the primary node with some values and database ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#step-8-setting-up-the-primary-node-with-some-values-and-database)
- [ Step 9: Setup Routing List URL ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#step-9-setup-routing-list-url)
- [ Step 10: Create the listener URL ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#step-10-create-the-listener-url)
- [ Next Steps ](https://hasura.io/docs/latest/schema/ms-sql-server/mssql-guides/mssql-read-replicas-docker-setup/#next-steps)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)