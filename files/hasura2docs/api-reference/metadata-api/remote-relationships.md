# Metadata API Reference: Remote Relationships

## Introduction​

Remote Relationships allow you to join tables with Remote Schemas or tables on other databases.

Supported from

The Metadata API is supported for versions `v2.0.0` and above and replaces the older[ schema/metadata API ](https://hasura.io/docs/latest/api-reference/schema-metadata-api/index/).

## pg_create_remote_relationship​

 `pg_create_remote_relationship` is used to create a new remote relationship from a *Postgres table* to an existing
Remote Schema or database.

### To Remote Schema​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "pg_create_remote_relationship" ,
   "args" : {
     // name of the remote relationship
     "name" :   "messages" ,
     // name of the database
     "source" :   "app_db" ,
     // name of the table in the above database on which the relationship
     // is being defined
     "table" :   "users" ,
     "definition" :   {
       // this remote relationship is being defined to a resolver on a
       // Remote Schema
       "to_remote_schema" :   {
         // name of the target Remote Schema
         "remote_schema" :   "forum_api" ,
         // the fields on the table that need to be selected to pass the
         // required data to the Remote Schema's resolver
         "lhs_fields" :   [ "id" ] ,
         // the join condition - this would generate this upstream request:
         // query {
         //   messages(id: id_from_users_table) { .. }
         // }
         "remote_field" :   {
           "messages" :   {
             "arguments" :   {
               "user_id" : "$id"
             }
           }
         }
       }
     }
   }
}
```

### To database​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" : "pg_create_remote_relationship" ,
   "args" : {
     // name of the remote relationship
     "name" :   "orders" ,
     // name of the database
     "source" :   "app_db" ,
     // name of the table in the above database on which the relationship
     // is being defined
     "table" :   "users" ,
       "definition" :   {
         "to_source" :   {
         // the type of the relationship, an 'object' (many-to-one) or an
         // 'array' (one-to-many)
         "relationship_type" :   "array" ,
         // the database where the target table exists
         "source" :   "store_db" ,
         // name of the table which is the target of the remote
         // relationship
         "table" :   "orders" ,
         // the join condition is specified by a mapping of columns from
         // the source's table to the target's table, i.e,
         // app_db.users.id = store_db.orders.user_id
         "field_mapping" :   {
           "id" :   "user_id"
         }
       }
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | User defined name of the new remote relationship |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table on which the relationship is being defined |
| definition | true | [ RemoteRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipdefinition) | Definition of the remote relationship |


### Legacy format​

Prior to `v2.0.10` , `pg_create_remote_relationship` only supported creating remote relationships to Remote Schemas and
as such it supported a different format which is now considered legacy. graphql-engine supports this legacy syntax
but we highly recommend you to migrate to the newer format.

#### Old format example​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "pg_create_remote_relationship" ,
    "args" : {
       "name" :   "name_of_the_remote_relationship" ,
       "table" :   "users" ,
       "hasura_fields" :   [ "id" ] ,
       "remote_schema" :   "my-remote-schema" ,
       "remote_field" :   {
         "messages" :   {
            "arguments" :   {
               "user_id" : "$id"
            }
          }
       }
    }
}
```

#### Old format args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ QualifiedTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Object with table name and schema |
| hasura_fields | true | [ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgcolumn)or[ ComputedFieldName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#computedfieldname) | Column/Computed field(s) in the table that is used for joining with Remote Schema field. All join keys in `remote_ field` must appear here. |
| remote_schema | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema to join with |
| remote_field | true | [ RemoteField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remotefield) | The schema tree ending at the field in Remote Schema which needs to be joined with |


## pg_update_remote_relationship​

 `pg_update_remote_relationship` is used to update the definition of an *existing* remote relationship defined on a
Postgres table.

### To Remote Schema​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "pg_update_remote_relationship" ,
    "args" : {
       "name" :   "name_of_the_remote_relationship" ,
       "source" :   "name_of_the_source" ,
       "table" :   "users" ,
       // the updated definition
       "definition" :   {
         "to_remote_schema" :   {
           "remote_schema" :   "name_of_the_target_remote_schema" ,
           "lhs_fields" :   [ "id" ] ,
           "remote_field" :   {
             "messages" :   {
                "arguments" :   {
                   "user_id" : "$id"
                }
             }
           }
       }
    }
}
```

### To database​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "pg_update_remote_relationship" ,
    "args" : {
       "name" :   "name_of_the_remote_relationship" ,
       "source" :   "name_of_the_source" ,
       "table" :   "users" ,
       // the updated definition
       "definition" :   {
         "to_source" :   {
           "relationship_type" :   "array" ,
           "source" :   "name_of_the_target_source" ,
           "table" :   "table_on_the_target_source"
           "field_mapping" :   {
             "user_id" :   "user_id"
           }
         }
       }
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table on which the relationship is being defined |
| definition | true | [ RemoteRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipdefinition) | Definition of the remote relationship |


### Legacy format​

Prior to `v2.0.10` , `pg_update_remote_relationship` only supported updating remote relationships to Remote Schemas and
as such it supported a different format which is now considered legacy. graphql-engine supports this legacy syntax
but we highly recommend you to migrate to the newer format.

#### Old format example​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "pg_update_remote_relationship" ,
   "args" :   {
      "name" :   "name_of_the_remote_relationship" ,
      "table" :   "users" ,
      "source" :   "name_of_the_source" ,
      "hasura_fields" :   [ "id" ] ,
      "remote_schema" :   "my-remote-schema" ,
      "remote_field" :   {
        "posts" :   {
           "arguments" :   {
              "user_id" :   "$id" ,
              "likes" :   {
                 "lte" : "1000"
              }
           }
        }
      }
   }
}
```

#### Old format args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ QualifiedTable ](https://hasura.io/docs/latest/api-reference/syntax-defs/#qualifiedtable) | Object with table name and schema |
| hasura_fields | true | [[ PGColumn ](https://hasura.io/docs/latest/api-reference/syntax-defs/#pgcolumn)] | Column(s) in the table that is used for joining with Remote Schema field. All join keys in `remote_ field` must appear here. |
| remote_schema | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema to join with |
| remote_field | true | [ RemoteField ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remotefield) | The schema tree ending at the field in Remote Schema which needs to be joined with. |


## pg_delete_remote_relationship​

 `pg_delete_remote_relationship` is used to delete an existing remote relationship.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "pg_delete_remote_relationship" ,
     "args"   :   {
        "source" :   "name_of_the_source" ,
        "table" :   {
           "name" : "users" ,
           "schema" : "public"
        } ,
        "name" : "name_of_the_remote_relationship"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Object with table name and schema |
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |


## citus_create_remote_relationship​

 `citus_create_remote_relationship` is used to create a new remote relationship on a *Citus table* to an existing
Remote Schema or to a table on a different database.

### To Remote Schema​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "citus_create_remote_relationship" ,
    "args" : {
       // name of the remote relationship
       "name" :   "messages" ,
       // name of the database
       "source" :   "app_db" ,
       // name of the table in the above database on which the relationship
       // is being defined
       "table" :   "users" ,
       "definition" :   {
         // this remote relationship is being defined to a resolver on a
         // Remote Schema
         "to_remote_schema" :   {
           // name of the target Remote Schema
           "remote_schema" :   "forum_api" ,
           // the fields on the table that need to be selected to pass the
           // required data to the Remote Schema's resolver
           "lhs_fields" :   [ "id" ] ,
           // the join condition - this would generate this upstream request:
           // query {
           //   messages(user_id: id_from_users_table) { .. }
           // }
           "remote_field" :   {
             "messages" :   {
                "arguments" :   {
                   "user_id" : "$id"
                }
             }
           }
       }
    }
}
```

### To database​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "citus_create_remote_relationship" ,
    "args" : {
       // name of the remote relationship
       "name" :   "orders" ,
       // name of the database
       "source" :   "app_db" ,
       // name of the table in the above database on which the relationship
       // is being defined
       "table" :   "users" ,
       "definition" :   {
         "to_source" :   {
           // the type of the relationship, an 'object' (many-to-one) or an
           // 'array' (one-to-many)
           "relationship_type" :   "array" ,
           // the database where the target table exists
           "source" :   "store_db" ,
           // name of the table which is the target of the remote
           // relationship
           "table" :   "orders"
           // the join condition is specified by a mapping of columns from
           // the source's table to the target's table, i.e,
           // app_db.users.id = store_db.orders.user_id
           "field_mapping" :   {
             "id" :   "user_id"
           }
         }
       }
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table on which the relationship is being defined |
| definition | true | [ RemoteRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipdefinition) | Definition of the remote relationship |


## citus_update_remote_relationship​

 `citus_update_remote_relationship` is used to update the definition of an *existing* remote relationship defined on
a *Citus table* .

### To Remote Schema​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "citus_update_remote_relationship" ,
    "args" : {
       "name" :   "name_of_the_remote_relationship" ,
       "source" :   "name_of_the_source" ,
       "table" :   "users" ,
       // the updated definition
       "definition" :   {
         "to_remote_schema" :   {
           "remote_schema" :   "name_of_the_target_remote_schema" ,
           "lhs_fields" :   [ "id" ] ,
           "remote_field" :   {
             "messages" :   {
                "arguments" :   {
                   "user_id" : "$id"
                }
             }
           }
       }
    }
}
```

### To database​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "citus_update_remote_relationship" ,
    "args" : {
       "name" :   "name_of_the_remote_relationship" ,
       "source" :   "name_of_the_source" ,
       "table" :   "users" ,
       // the updated definition
       "definition" :   {
         "to_source" :   {
           "relationship_type" :   "array" ,
           "source" :   "name_of_the_target_source" ,
           "table" :   "table_on_the_target_source"
           "field_mapping" :   {
             "user_id" :   "user_id"
           }
         }
       }
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table on which the relationship is being defined |
| definition | true | [ RemoteRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipdefinition) | Definition of the remote relationship |


## citus_delete_remote_relationship​

 `citus_delete_remote_relationship` is used to delete an existing remote relationship.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "citus_delete_remote_relationship" ,
     "args"   :   {
        "source" :   "name_of_the_source" ,
        "table" :   {
           "name" : "users" ,
           "schema" : "public"
        } ,
        "name" : "name_of_the_remote_relationship"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table |
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |


## mssql_create_remote_relationship​

 `mssql_create_remote_relationship` is used to create a new remote relationship on an *mssql table* to an existing
Remote Schema or to a table on a different database.

### To Remote Schema​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "mssql_create_remote_relationship" ,
    "args" : {
       // name of the remote relationship
       "name" :   "messages" ,
       // name of the database
       "source" :   "app_db" ,
       // name of the table in the above database on which the relationship
       // is being defined
       "table" :   "users" ,
       "definition" :   {
         // this remote relationship is being defined to a resolver on a
         // Remote Schema
         "to_remote_schema" :   {
           // name of the target Remote Schema
           "remote_schema" :   "forum_api" ,
           // the fields on the table that need to be selected to pass the
           // required data to the Remote Schema's resolver
           "lhs_fields" :   [ "id" ] ,
           // the join condition - this would generate this upstream request:
           // query {
           //   messages(user_id: id_from_users_table) { .. }
           // }
           "remote_field" :   {
             "messages" :   {
                "arguments" :   {
                   "user_id" : "$id"
                }
             }
           }
       }
    }
}
```

### To database​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "mssql_create_remote_relationship" ,
    "args" : {
       // name of the remote relationship
       "name" :   "orders" ,
       // name of the database
       "source" :   "app_db" ,
       // name of the table in the above database on which the relationship
       // is being defined
       "table" :   "users" ,
       "definition" :   {
         "to_source" :   {
           // the type of the relationship, an 'object' (many-to-one) or an
           // 'array' (one-to-many)
           "relationship_type" :   "array" ,
           // the database where the target table exists
           "source" :   "store_db" ,
           // name of the table which is the target of the remote
           // relationship
           "table" :   "orders"
           // the join condition is specified by a mapping of columns from
           // the source's table to the target's table, i.e,
           // app_db.users.id = store_db.orders.user_id
           "field_mapping" :   {
             "id" :   "user_id"
           }
         }
       }
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table on which the relationship is being defined |
| definition | true | [ RemoteRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipdefinition) | Definition of the remote relationship |


## mssql_update_remote_relationship​

 `mssql_update_remote_relationship` is used to update the definition of an *existing* remote relationship defined on
an *MS SQL table* .

### To Remote Schema​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "mssql_update_remote_relationship" ,
    "args" : {
       "name" :   "name_of_the_remote_relationship" ,
       "source" :   "name_of_the_source" ,
       "table" :   "users" ,
       // the updated definition
       "definition" :   {
         "to_remote_schema" :   {
           "remote_schema" :   "name_of_the_target_remote_schema" ,
           "lhs_fields" :   [ "id" ] ,
           "remote_field" :   {
             "messages" :   {
                "arguments" :   {
                   "user_id" : "$id"
                }
             }
           }
       }
    }
}
```

### To database​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "mssql_update_remote_relationship" ,
    "args" : {
       "name" :   "name_of_the_remote_relationship" ,
       "source" :   "name_of_the_source" ,
       "table" :   "users" ,
       // the updated definition
       "definition" :   {
         "to_source" :   {
           "relationship_type" :   "array" ,
           "source" :   "name_of_the_target_source" ,
           "table" :   "table_on_the_target_source"
           "field_mapping" :   {
             "id" :   "user_id"
           }
         }
       }
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table on which the relationship is being defined |
| definition | true | [ RemoteRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipdefinition) | Definition of the remote relationship |


## mssql_delete_remote_relationship​

 `mssql_delete_remote_relationship` is used to delete an existing remote relationship.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "mssql_delete_remote_relationship" ,
     "args"   :   {
        "source" :   "name_of_the_source" ,
        "table" :   {
           "name" : "users" ,
           "schema" : "public"
        } ,
        "name" : "name_of_the_remote_relationship"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ TableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#tablename) | Name of the table on which the relationship is being defined |
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |


## bigquery_create_remote_relationship​

 `bigquery_create_remote_relationship` is used to create a new remote relationship on a *BigQuery table* to an
existing Remote Schema or to a table on a different database.

### To Remote Schema​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "bigquery_create_remote_relationship" ,
    "args" : {
       // name of the remote relationship
       "name" :   "messages" ,
       // name of the database
       "source" :   "app_db" ,
       // name of the table in the above database on which the relationship
       // is being defined
       "table" :   {
          "dataset" :   "<source_dataset_name>" ,
          "name" :   "users"
       } ,
       "definition" :   {
         // this remote relationship is being defined to a resolver on a
         // Remote Schema
         "to_remote_schema" :   {
           // name of the target Remote Schema
           "remote_schema" :   "forum_api" ,
           // the fields on the table that need to be selected to pass the
           // required data to the Remote Schema's resolver
           "lhs_fields" :   [ "id" ] ,
           // the join condition - this would generate this upstream request:
           // query {
           //   messages(user_id: id_from_users_table) { .. }
           // }
           "remote_field" :   {
             "messages" :   {
                "arguments" :   {
                   "user_id" : "$id"
                }
             }
           }
       }
    }
}
```

### To database​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_create_remote_relationship" ,
   "args" :   {
     // name of the remote relationship
     "name" :   "orders" ,
     // name of the database
     "source" :   "app_db" ,
     // name of the table in the above database on which the relationship
     // is being defined
     "table" :   {
         "dataset" :   "<source_dataset_name>" ,
         "name" :   "users"
     } ,
     "definition" :   {
       "to_source" :   {
         // the type of the relationship, an 'object' (many-to-one) or an
         // 'array' (one-to-many)
         "relationship_type" :   "array" ,
         // the database where the target table exists
         "source" :   "store_db" ,
         // name of the table which is the target of the remote
         // relationship
         "table" :   {
             "name" :   "orders" ,
             "dataset" :   "<target_dataset_name>"
         } ,
         // the join condition is specified by a mapping of columns from
         // the source's table to the target's table, i.e,
         // app_db.users.id = store_db.orders.user_id
         "field_mapping" :   {
           "id" :   "user_id"
         }
       }
     }
   }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ BigQueryTableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#bigquerytablename) | Name of the table on which the relationship is being defined |
| definition | true | [ RemoteRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipdefinition) | Definition of the remote relationship |


## bigquery_update_remote_relationship​

 `bigquery_update_remote_relationship` is used to update the definition of an *existing* remote relationship defined
on a *BigQuery table* .

### To Remote Schema​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "bigquery_update_remote_relationship" ,
    "args" : {
       "name" :   "name_of_the_remote_relationship" ,
       "source" :   "name_of_the_source" ,
       "table" :   "users" ,
       // the updated definition
       "definition" :   {
         "to_remote_schema" :   {
           "remote_schema" :   "name_of_the_target_remote_schema" ,
           "lhs_fields" :   [ "id" ] ,
           "remote_field" :   {
             "messages" :   {
                "arguments" :   {
                   "user_id" : "$id"
                }
             }
           }
       }
    }
}
```

### To database​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "bigquery_update_remote_relationship" ,
    "args" : {
       "name" :   "name_of_the_remote_relationship" ,
       "source" :   "name_of_the_source" ,
       "table" :   "users" ,
       // the updated definition
       "definition" :   {
         "to_source" :   {
           "relationship_type" :   "array" ,
           "source" :   "name_of_the_target_source" ,
           "table" :   "table_on_the_target_source"
           "field_mapping" :   {
             "user_id" :   "user_id"
           }
         }
       }
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ BigQueryTableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#bigquerytablename) | Name of the table on which the relationship is being defined |
| definition | true | [ RemoteRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipdefinition) | Definition of the remote relationship |


## bigquery_delete_remote_relationship​

 `bigquery_delete_remote_relationship` is used to delete an existing remote relationship.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
     "type"   :   "bigquery_delete_remote_relationship" ,
     "args"   :   {
        "source" :   "name_of_the_source" ,
        "table" :   {
           "name" : "users" ,
           "dataset" : "some_dataset_name"
        } ,
        "name" : "name_of_the_remote_relationship"
     }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| source | false | [ SourceName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#sourcename) | Name of the source database of the table (default: `default` ) |
| table | true | [ BigQueryTableName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#bigquerytablename) | Name of the table on which the relationship is being defined |
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |


## create_remote_schema_remote_relationship​

 `create_remote_schema_remote_relationship` is used to create a new remote relationship on a Remote Schema's type to
a table on a database or to another Remote Schema.

Supported types

Currently only[ object types ](https://spec.graphql.org/October2021/#sec-Objects)on a Remote Schema are supported.

### To Remote Schema​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "create_remote_schema_remote_relationship" ,
    "args" : {
       // name of the remote relationship
       "name" :   "messages" ,
       // name of the Remote Schema
       "remote_schema" :   "users_api" ,
       // the object type in the above Remote Schema on which the
       // relationship is being defined
       "type" :   "user" ,
       "definition" :   {
         // this remote relationship is being defined to a resolver on a
         // Remote Schema
         "to_remote_schema" :   {
           // name of the target Remote Schema
           "remote_schema" :   "forum_api" ,
           // the fields on the table that need to be selected to pass the
           // required data to the Remote Schema's resolver
           "lhs_fields" :   [ "id" ] ,
           // the join condition - this would generate this upstream request:
           // query {
           //   messages(user_id: id_from_user_type) { .. }
           // }
           "remote_field" :   {
             "messages" :   {
                "arguments" :   {
                   "user_id" : "$id"
                }
             }
           }
       }
    }
}
```

### To database​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "create_remote_schema_remote_relationship" ,
    "args" : {
       // name of the remote relationship
       "name" :   "messages" ,
       // name of the Remote Schema
       "remote_schema" :   "users_api" ,
       // the object type in the above Remote Schema on which the
       // relationship is being defined
       "type" :   "user" ,
       // name of the remote relationship
       "definition" :   {
         "to_source" :   {
           // the type of the relationship, an 'object' (many-to-one) or an
           // 'array' (one-to-many)
           "relationship_type" :   "array" ,
           // the database where the target table exists
           "source" :   "store_db" ,
           // name of the table which is the target of the remote
           // relationship
           "table" :   "orders"
           // the join condition is specified by a mapping of columns from
           // the Remote Schema's type to the target's table, i.e,
           // users_api.user.id = store_db.orders.user_id
           "field_mapping" :   {
             "id" :   "user_id"
           }
         }
       }
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| remote_schema | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema |
| type | true | [ GraphQLName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#graphqlname) | Name of the type on which the relationship is being defined |
| definition | true | [ RemoteRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipdefinition) | Definition of the remote relationship |


## update_remote_schema_remote_relationship​

 `update_remote_schema_remote_relationship` is used to update an existing remote
relationship defined on a Remote Schema's type.

### To Remote Schema​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "update_remote_schema_remote_relationship" ,
    "args" : {
       "name" :   "messages" ,
       "remote_schema" :   "users_api" ,
       "type" :   "user" ,
       // new definition of the remote relationship
       "definition" :   {
         "to_remote_schema" :   {
           "remote_schema" :   "forum_api" ,
           "lhs_fields" :   [ "id" ] ,
           "remote_field" :   {
             "messages" :   {
                "arguments" :   {
                   "user_id" : "$id"
                }
             }
           }
       }
    }
}
```

### To database​

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "update_remote_schema_remote_relationship" ,
    "args" : {
       "name" :   "messages" ,
       "remote_schema" :   "users_api" ,
       "type" :   "user" ,
       // new definition of the remote relationship
       "definition" :   {
         "to_source" :   {
           "relationship_type" :   "array" ,
           "source" :   "store_db" ,
           "table" :   "orders"
           "field_mapping" :   {
             "id" :   "user_id"
           }
         }
       }
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| remote_schema | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema |
| type | true | [ GraphQLName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#graphqlname) | Name of the type on which the relationship is being defined |
| definition | true | [ RemoteRelationshipDefinition ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipdefinition) | Definition of the remote relationship |


## delete_remote_schema_remote_relationship​

 `delete_remote_schema_remote_relationship` is used to delete an existing remote relationship defined on a Remote
Schema's type.

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
    "type" : "delete_remote_schema_remote_relationship" ,
    "args" : {
       "name" :   "messages" ,
       "remote_schema" :   "users_api" ,
       "type" :   "user"
    }
}
```

### Args syntax​

| Key | Required | Schema | Description |
|---|---|---|---|
| name | true | [ RemoteRelationshipName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoterelationshipname) | Name of the remote relationship |
| remote_schema | true | [ RemoteSchemaName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#remoteschemaname) | Name of the Remote Schema |
| type | true | [ GraphQLName ](https://hasura.io/docs/latest/api-reference/syntax-defs/#graphqlname) | Name of the type on which the relationship is being defined |


### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#introduction)
- [ pg_create_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-pg-create-remote-relationship)
    - [ To Remote Schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-remote-schema)

- [ To database ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-database)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-pg-create-remote-relationship-database-syntax)

- [ Legacy format ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#legacy-format)
- [ pg_update_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-pg-update-remote-relationship)
    - [ To Remote Schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-remote-schema-1)

- [ To database ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-database-1)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-pg-update-remote-relationship-syntax)

- [ Legacy format ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#legacy-format-1)
- [ pg_delete_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-pg-delete-remote-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-pg-delete-remote-relationship-syntax)
- [ citus_create_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-citus-create-remote-relationship)
    - [ To Remote Schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-remote-schema-2)

- [ To database ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-database-2)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-citus-create-remote-relationship-syntax)
- [ citus_update_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-citus-update-remote-relationship)
    - [ To Remote Schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-remote-schema-3)

- [ To database ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-database-3)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-citus-update-remote-relationship-syntax)
- [ citus_delete_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-citus-delete-remote-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-citus-delete-remote-relationship-syntax)
- [ mssql_create_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-mssql-create-remote-relationship)
    - [ To Remote Schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-remote-schema-4)

- [ To database ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-database-4)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-mssql-create-remote-relationship-syntax)
- [ mssql_update_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-mssql-update-remote-relationship)
    - [ To Remote Schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-remote-schema-5)

- [ To database ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-database-5)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-mssql-update-remote-relationship-syntax)
- [ mssql_delete_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-mssql-delete-remote-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-mssql-delete-remote-relationship-syntax)
- [ bigquery_create_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-bigquery-create-remote-relationship)
    - [ To Remote Schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-remote-schema-6)

- [ To database ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-database-6)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-bigquery-create-remote-relationship-syntax)
- [ bigquery_update_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-bigquery-update-remote-relationship)
    - [ To Remote Schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-remote-schema-7)

- [ To database ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-database-7)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-bigquery-update-remote-relationship-syntax)
- [ bigquery_delete_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-bigquery-delete-remote-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-bigquery-delete-remote-relationship-syntax)
- [ create_remote_schema_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-create-remote-schema-remote-relationship)
    - [ To Remote Schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-remote-schema-8)

- [ To database ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-database-8)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-create-remote-schema-remote-relationship-syntax)
- [ update_remote_schema_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-update-remote-schema-remote-relationship)
    - [ To Remote Schema ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-remote-schema-9)

- [ To database ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#to-database-9)

- [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-update-remote-schema-remote-relationship-syntax)
- [ delete_remote_schema_remote_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-delete-remote-schema-remote-relationship)
    - [ Args syntax ](https://hasura.io/docs/latest/api-reference/metadata-api/remote-relationships/#metadata-delete-remote-schema-remote-relationship-syntax)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)