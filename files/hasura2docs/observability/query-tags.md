# Query Tags

## Introduction​

Query Tags are SQL comments which are made up of `(key=value)` pairs that are appended to the SQL statements generated
by Hasura for GraphQL operations. This enables the ability to get some application context in the database logs and also
use native database monitoring tools ( *e.g. pganalyze* ) for better performance analysis.

Example:

When the following query is sent to Hasura

```
query   GetChild   {
   child   {
     name
   }
}
```

Hasura attaches query tags ( *unless disabled* ) to the generated SQL statement it sends to the database.

`SELECT  name  FROM  child  /* request_id=487c2ed5-08a4-429a-b0e0-4666a82e3cc6, field_name=child, operation_name=GetChild */`

## Formats of Query Tags​

The format of the Query Tags describes how the *(Key,Value)* pairs are constructed. Currently we support two
formats of Query Tags:

1. Standard ( `standard` )
2. SQLCommenter ( `sqlcommenter` )


### Standard​

This format makes a collection of *key=value* pairs and separates each pair by a comma `,` . **This is the
default format for Query Tags** 

For eg:

`SELECT  name  FROM  child  /* request_id=487c2ed5-08a4-429a-b0e0-4666a82e3cc6, field_name=child, parameterized_query_hash=b2a71ce23928ca7f0021f9060e5d590e9f9bb00f, operation_name=GetChild */`

### SQLCommenter​

The specification for this format is defined at[ https://google.github.io/sqlcommenter/spec/ ](https://google.github.io/sqlcommenter/spec/)

For eg:

`SELECT  name  FROM  child  /* field_name='child', operation_name='GetChild', parameterized_query_hash='b2a71ce23928ca7f0021f9060e5d590e9f9bb00f' ,  request_id='487c2ed5-08a4-429a-b0e0-4666a82e3cc6' */`

## Information in Query Tags​

The following information is present in query tags for the GraphQL operations.

### Query and Mutation​

1. Request ID ( `request_id` ) - can be added by setting the `omit_request_id` flag to `false`
2. Operation Name ( `operation_name` )
3. (Root) field name (alias if provided) ( `field_name` )
4. Parameterized Query Hash ( `parameterized_query_hash` )


### Subscriptions​

1. (Root) field name (alias if provided) ( `field_name` )
2. Parameterized Query Hash ( `parameterized_query_hash` )


## Metadata Specification​

```
sources :
   name :   # Name of the source
   configuration :
   query_tags :   # Optional Field
     disabled :   # Optional Field | Type: Bool | Values: true or false
     format :   # Optional Field  | Values: standard or sqlcommenter
     omit_request_id :   # Optional Field | Type: Bool | Values: true or false
```

info

Note The default format for the Query Tags is `Standard` and it is enabled by default for all sources.

In the above Metadata spec:

1. The *query_tags* field is optional. If the *query_tags* field is not present for a source, then query
tags is enabled for the source and the format used is *standard* .
2. To disable query tags for any source, set the value of *disabled* field to *true* .
3. To override the default format ( *Standard* ) for query tags, use the *format* field.
4. To add the `request_id` part of the query tags for any source, set the value of *omit_request_id* field to *false* .


Compatibility with prepared statements

The `use_prepared_statements` flag supported by Postgres sources is largely incompatible with query tags. With query
tags enabled, two otherwise identical GraphQL queries may produce different SQL text, which negates the caching benefit
of prepared statements. If both query tags and `use_prepared_statements` are enabled at the same time, the `omit_request_id` should be set to `true` .

## Example Metadata Specification​

```
sources :
   -   name :  test_db
     configuration :
     query_tags :
       disabled :   true
   -   name :  hasura_db_herokou
       configuration :
       query_tags :
         format :  sqlcommenter
         omit_request_id :   false
   -   name :  hasura_db_2
       configuration :
       query_tags :
         format :  standard
         disabled :   true
```

## Metadata API To Set Query Tags​

```
type :   'set_query_tags'
args :
   source_name :   # Name of the source | Required
   disabled :   # Optional Field | Type: Bool | Values: true or false
   format :   # Optional Field  | Values: standard or sqlcommenter
   omit_request_id :   # Optional Field | Type: Bool | Values: true or false
```

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/observability/query-tags/#introduction)
- [ Formats of Query Tags ](https://hasura.io/docs/latest/observability/query-tags/#formats-of-query-tags)
    - [ Standard ](https://hasura.io/docs/latest/observability/query-tags/#standard)

- [ SQLCommenter ](https://hasura.io/docs/latest/observability/query-tags/#sqlcommenter)
- [ Information in Query Tags ](https://hasura.io/docs/latest/observability/query-tags/#information-in-query-tags)
    - [ Query and Mutation ](https://hasura.io/docs/latest/observability/query-tags/#query-and-mutation)

- [ Subscriptions ](https://hasura.io/docs/latest/observability/query-tags/#subscriptions)
- [ Metadata Specification ](https://hasura.io/docs/latest/observability/query-tags/#metadata-specification)
- [ Example Metadata Specification ](https://hasura.io/docs/latest/observability/query-tags/#example-metadata-specification)
- [ Metadata API To Set Query Tags ](https://hasura.io/docs/latest/observability/query-tags/#metadata-api-to-set-query-tags)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)