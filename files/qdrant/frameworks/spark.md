# Apache Spark

[ Spark ](https://spark.apache.org/)is a leading distributed computing framework that empowers you to work with massive datasets efficiently. When it comes to leveraging the power of Spark for your data processing needs, the[ Qdrant-Spark Connector ](https://github.com/qdrant/qdrant-spark)is to be considered. This connector enables Qdrant to serve as a storage destination in Spark, offering a seamless bridge between the two.

## Installation

You can set up the Qdrant-Spark Connector in a few different ways, depending on your preferences and requirements.

### GitHub Releases

The simplest way to get started is by downloading pre-packaged JAR file releases from the[ Qdrant-Spark GitHub releases page ](https://github.com/qdrant/qdrant-spark/releases). These JAR files come with all the necessary dependencies to get you going.

### Building from Source

If you prefer to build the JAR from source, you’ll need[ JDK 17 ](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)and[ Maven ](https://maven.apache.org/)installed on your system. Once you have the prerequisites in place, navigate to the project’s root directory and run the following command:

`mvn package -P assembly
`

This command will compile the source code and generate a fat JAR, which will be stored in the `target` directory by default.

### Maven Central

For Java and Scala projects, you can also obtain the Qdrant-Spark Connector from[ Maven Central ](https://central.sonatype.com/artifact/io.qdrant/spark).

```
<dependency> 

     <groupId> io.qdrant </groupId> 

     <artifactId> spark </artifactId> 

     <version> 1.6 </version> 

</dependency> 

```

## Getting Started

After successfully installing the Qdrant-Spark Connector, you can start integrating Qdrant with your Spark applications. Below, we’ll walk through the basic steps of creating a Spark session with Qdrant support and loading data into Qdrant.

### Creating a single-node Spark session with Qdrant Support

To begin, import the necessary libraries and create a Spark session with Qdrant support. Here’s how:

```
from   pyspark.sql   import  SparkSession



spark  =  SparkSession . builder . config(

         "spark.jars" ,

         "spark-1.0-assembly.jar" ,   # Specify the downloaded JAR file 

    )

     . master( "local[*]" )

     . appName( "qdrant" )

     . getOrCreate()

```

```
import   org.apache.spark.sql.SparkSession 



val  spark  =   SparkSession . builder

   . config ( "spark.jars" ,   "spark-1.0-assembly.jar" )   // Specify the downloaded JAR file

   . master ( "local[*]" ) 

   . appName ( "qdrant" ) 

   . getOrCreate () 

```

```
import   org.apache.spark.sql.SparkSession ; 



public   class   QdrantSparkJavaExample   { 

     public   static   void   main ( String []  args )   { 

        SparkSession spark  =  SparkSession . builder () 

                 . config ( "spark.jars" ,   "spark-1.0-assembly.jar" )   // Specify the downloaded JAR file

                 . master ( "local[*]" ) 

                 . appName ( "qdrant" ) 

                 . getOrCreate (); 

         ... 

     } 

} 

```

### Loading Data into Qdrant

Here’s how you can use the Qdrant-Spark Connector to upsert data:

```
< YourDataFrame > 

     . write

     . format( "io.qdrant.spark.Qdrant" )

     . option( "qdrant_url" ,  < QDRANT_URL > )   # REST URL of the Qdrant instance 

     . option( "collection_name" ,  < QDRANT_COLLECTION_NAME > )   # Name of the collection to write data into 

     . option( "embedding_field" ,  < EMBEDDING_FIELD_NAME > )   # Name of the field holding the embeddings 

     . option( "schema" ,  < YourDataFrame >. schema . json())   # JSON string of the dataframe schema 

     . mode( "append" )

     . save()

```

```
< YourDataFrame > 

     . write

     . format ( "io.qdrant.spark.Qdrant" ) 

     . option ( "qdrant_url" ,   QDRANT_URL )   // REST URL of the Qdrant instance

     . option ( "collection_name" ,   QDRANT_COLLECTION_NAME )   // Name of the collection to write data into

     . option ( "embedding_field" ,   EMBEDDING_FIELD_NAME )   // Name of the field holding the embeddings

     . option ( "schema" ,   < YourDataFrame >. schema . json ())   // JSON string of the dataframe schema

     . mode ( "append" ) 

     . save () 

```

```
< YourDataFrame > 

     . write () 

     . format ( "io.qdrant.spark.Qdrant" ) 

     . option ( "qdrant_url" ,  QDRANT_URL )   // REST URL of the Qdrant instance

     . option ( "collection_name" ,  QDRANT_COLLECTION_NAME )   // Name of the collection to write data into

     . option ( "embedding_field" ,  EMBEDDING_FIELD_NAME )   // Name of the field holding the embeddings

     . option ( "schema" ,   < YourDataFrame >. schema (). json ())   // JSON string of the dataframe schema

     . mode ( "append" ) 

     . save (); 

```

## Datatype Support

Qdrant supports all the Spark data types, and the appropriate data types are mapped based on the provided schema.

## Options and Spark Types

The Qdrant-Spark Connector provides a range of options to fine-tune your data integration process. Here’s a quick reference:

| Option | Description | DataType | Required |
|---|---|---|---|
|  `qdrant_url`  | REST URL of the Qdrant instance |  `StringType`  | ✅ |
|  `collection_name`  | Name of the collection to write data into |  `StringType`  | ✅ |
|  `embedding_field`  | Name of the field holding the embeddings |  `ArrayType(FloatType)`  | ✅ |
|  `schema`  | JSON string of the dataframe schema |  `StringType`  | ✅ |
|  `mode`  | Write mode of the dataframe |  `StringType`  | ✅ |
|  `id_field`  | Name of the field holding the point IDs. Default: A random UUID is generated |  `StringType`  | ❌ |
|  `batch_size`  | Max size of the upload batch. Default: 100 |  `IntType`  | ❌ |
|  `retries`  | Number of upload retries. Default: 3 |  `IntType`  | ❌ |
|  `api_key`  | Qdrant API key for authenticated requests. Default: null |  `StringType`  | ❌ |


For more information, be sure to check out the[ Qdrant-Spark GitHub repository ](https://github.com/qdrant/qdrant-spark). The Apache Spark guide is available[ here ](https://spark.apache.org/docs/latest/quick-start.html). Happy data processing!

##### Table of contents

- [ Installation ](https://qdrant.tech/documentation/frameworks/spark/#installation)
    - [ GitHub Releases ](https://qdrant.tech/documentation/frameworks/spark/#github-releases)

- [ Building from Source ](https://qdrant.tech/documentation/frameworks/spark/#building-from-source)

- [ Maven Central ](https://qdrant.tech/documentation/frameworks/spark/#maven-central)
- [ Getting Started ](https://qdrant.tech/documentation/frameworks/spark/#getting-started)
    - [ Creating a single-node Spark session with Qdrant Support ](https://qdrant.tech/documentation/frameworks/spark/#creating-a-single-node-spark-session-with-qdrant-support)

- [ Loading Data into Qdrant ](https://qdrant.tech/documentation/frameworks/spark/#loading-data-into-qdrant)
- [ Datatype Support ](https://qdrant.tech/documentation/frameworks/spark/#datatype-support)
- [ Options and Spark Types ](https://qdrant.tech/documentation/frameworks/spark/#options-and-spark-types)


- [ 
 Edit on GitHub
 ](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/spark.md)
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