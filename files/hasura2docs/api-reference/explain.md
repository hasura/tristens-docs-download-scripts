# Explain API Reference

## Introduction​

The Explain API is an admin-only endpoint for analyzing queries and
subscriptions. Given a query and authorization role, it returns
backend-specific execution plans.

## Endpoint​

All requests are `POST` requests to the `/v1/graphql/explain` endpoint.

## API Spec​

### Request​

The request expects a JSON object with the following keys:

- `query` : the GraphQL query to be analyzed
- `user` (optional): the `x-hasura-role` along with session variables


```
POST   /v1/graphql/explain   HTTP/1.1
Content-Type :   application/json
{
      "query" :   "<query>" ,
      "user" :   {
          "x-hasura-role"   :   "..." ,
          "x-hasura-session-var1"   :   "..."
      }
}
```

#### Sample request​

```
POST   /v1/graphql/explain   HTTP/1.1
Content-Type :   application/json
{
      "query" :   {
          "query" :   "query getUsers { user { name }}" ,
          "operationName" :   "getUsers"
      }
}
```

### Response​

The response for a query is a list of plans, one for each field:

```
[
    {
        "field": String -- "name of the field",
        "sql": String -- "generated SQL for the operation",
        "plan": [String] -- "the database's execution plan for the generated SQL"
    }
]
```

The response for a subscription is a single plan, along with the
variables used to determine how the subscription will be multiplexed:

```
{
    "sql": String -- "generated SQL for the operation",
    "plan": [String] -- "the database's execution plan for the generated SQL"
    "variables": {
        "synthetic": [String], -- "introduced variables for enabling additional query multiplexing (values)"
        "query": Object -- "GraphQL query variables (names and values)"
        "session": Object -- "session variables referenced by the query (names and values)"
    }
}
```

#### Sample response for a query​

PostgreSQL backend:

```
[
   {
     "field" :   "user" ,
     "sql" :   "SELECT  coalesce(json_agg(\"root\" ), '[]' ) AS \"root\" FROM  (SELECT  row_to_json((SELECT  \"_1_e\"  FROM  (SELECT  \"_0_root.base\".\"name\" AS \"name\"       ) AS \"_1_e\"      ) ) AS \"root\" FROM  (SELECT  *  FROM \"public\".\"user\"  WHERE ('true')     ) AS \"_0_root.base\"      ) AS \"_2_root\"      " ,
     "plan" :   [
       "Aggregate  (cost=40.00..40.01 rows=1 width=32)" ,
       "  ->  Seq Scan on \"user\"  (cost=0.00..22.00 rows=1200 width=32)" ,
       "  SubPlan 1" ,
       "    ->  Result  (cost=0.00..0.01 rows=1 width=32)"
     ]
   }
]
```

Microsoft SQL Server backend:

```
[
   {
     "field" :   "user" ,
     "sql" :   "SELECT ISNULL((SELECT [t_user1].[name] AS [name]\nFROM [dbo].[user] AS [t_user1]\nFOR JSON PATH, INCLUDE_NULL_VALUES), '[]')" ,
     "plan" :   [
       "SELECT ISNULL((SELECT [t_user1].[name] AS [name]\nFROM [dbo].[user] AS [t_user1]\nFOR JSON PATH, INCLUDE_NULL_VALUES), '[]')" ,
       "  |--Compute Scalar(DEFINE:([Expr1003]=isnull([Expr1001],CONVERT_IMPLICIT(nvarchar(max),'[]',0))))" ,
       "       |--UDX(([t_user1].[name]))" ,
       "            |--Clustered Index Scan(OBJECT:([master].[dbo].[user].[PK__user__3213E83F04195C1B] AS [t_user1]))"
     ]
   }
]
```

#### Sample response for a subscription​

PostgreSQL backend:

```
{
   "sql" :   "SELECT  \"_subs\".\"result_id\" , \"_fld_resp\".\"root\" AS \"result\" FROM UNNEST(($1)::uuid[], ($2)::json[]) AS \"_subs\"(\"result_id\", \"result_vars\") LEFT OUTER JOIN LATERAL (SELECT  json_build_object('user', \"user\".\"root\" ) AS \"root\" FROM  (SELECT  coalesce(json_agg(\"root\" ), '[]' ) AS \"root\" FROM  (SELECT  row_to_json((SELECT  \"_1_e\"  FROM  (SELECT  \"_0_root.base\".\"name\" AS \"name\"       ) AS \"_1_e\"      ) ) AS \"root\" FROM  (SELECT  *  FROM \"public\".\"user\"  WHERE ('true')     ) AS \"_0_root.base\"      ) AS \"_2_root\"      ) AS \"user\"      ) AS \"_fld_resp\" ON ('true')      " ,
   "plan" :   [
     "Nested Loop Left Join  (cost=40.01..42.28 rows=100 width=48)" ,
     "  ->  Function Scan on _subs  (cost=0.01..1.00 rows=100 width=16)" ,
     "  ->  Materialize  (cost=40.00..40.03 rows=1 width=32)" ,
     "        ->  Subquery Scan on \"user\"  (cost=40.00..40.02 rows=1 width=32)" ,
     "              ->  Aggregate  (cost=40.00..40.01 rows=1 width=32)" ,
     "                    ->  Seq Scan on \"user\" user_1  (cost=0.00..22.00 rows=1200 width=32)" ,
     "                    SubPlan 1" ,
     "                      ->  Result  (cost=0.00..0.01 rows=1 width=32)"
   ] ,
   "variables" :   {
     "synthetic" :   [ ] ,
     "query" :   { } ,
     "session" :   { }
   }
}
```

Microsoft SQL Server backend:

```
{
   "sql" :   "SELECT ISNULL((SELECT [row].[result_id] AS [result_id],\n       [result].[json] AS [result]\nFROM OPENJSON((N''+NCHAR(91)+''+NCHAR(91)+''+NCHAR(34)+'00000000-0000-0000-0000-000000000000'+NCHAR(34)+','+NCHAR(123)+''+NCHAR(34)+'synthetic'+NCHAR(34)+''+NCHAR(58)+''+NCHAR(91)+''+NCHAR(93)+','+NCHAR(34)+'query'+NCHAR(34)+''+NCHAR(58)+''+NCHAR(123)+''+NCHAR(125)+','+NCHAR(34)+'session'+NCHAR(34)+''+NCHAR(58)+''+NCHAR(123)+''+NCHAR(125)+''+NCHAR(125)+''+NCHAR(93)+''+NCHAR(93)+''))\n     WITH ([result_id] UNIQUEIDENTIFIER '$[0]',\n          [result_vars] NVARCHAR(MAX) '$[1]' AS JSON) AS [row]\nOUTER APPLY (SELECT ISNULL((SELECT (SELECT ISNULL((SELECT [t_user1].[name] AS [name]\n                     FROM [dbo].[user] AS [t_user1]\n                     FOR JSON PATH, INCLUDE_NULL_VALUES), '[]')) AS [user]\n             FOR JSON PATH, INCLUDE_NULL_VALUES, WITHOUT_ARRAY_WRAPPER), '[]')) \nAS [result]([json])\nFOR JSON PATH, INCLUDE_NULL_VALUES), '[]')" ,
   "plan" :   [
     "SELECT ISNULL((SELECT [row].[result_id] AS [result_id],\n       [result].[json] AS [result]\nFROM OPENJSON((N''+NCHAR(91)+''+NCHAR(91)+''+NCHAR(34)+'00000000-0000-0000-0000-000000000000'+NCHAR(34)+','+NCHAR(123)+''+NCHAR(34)+'synthetic'+NCHAR(34)+''+NCHAR(58)+''+NCHAR(91)+''+NCHAR(93)+','+NCHAR(34)+'query'+NCHAR(34)+''+NCHAR(58)+''+NCHAR(123)+''+NCHAR(125)+','+NCHAR(34)+'session'+NCHAR(34)+''+NCHAR(58)+''+NCHAR(123)+''+NCHAR(125)+''+NCHAR(125)+''+NCHAR(93)+''+NCHAR(93)+''))\n     WITH ([result_id] UNIQUEIDENTIFIER '$[0]',\n          [result_vars] NVARCHAR(MAX) '$[1]' AS JSON) AS [row]\nOUTER APPLY (SELECT ISNULL((SELECT (SELECT ISNULL((SELECT [t_user1].[name] AS [name]\n                     FROM [dbo].[user] AS [t_user1]\n                     FOR JSON PATH, INCLUDE_NULL_VALUES), '[]')) AS [user]\n             FOR JSON PATH, INCLUDE_NULL_VALUES, WITHOUT_ARRAY_WRAPPER), '[]')) \nAS [result]([json])\nFOR JSON PATH, INCLUDE_NULL_VALUES), '[]')" ,
     "  |--Compute Scalar(DEFINE:([Expr1010]=isnull([Expr1008],CONVERT_IMPLICIT(nvarchar(max),'[]',0))))" ,
     "       |--UDX((OPENJSON_EXPLICIT.[result_id], [Expr1007]))" ,
     "            |--Nested Loops(Left Outer Join)" ,
     "                 |--Table-valued function" ,
     "                 |--Compute Scalar(DEFINE:([Expr1007]=isnull([Expr1005],CONVERT_IMPLICIT(nvarchar(max),'[]',0))))" ,
     "                      |--UDX(([Expr1004]))" ,
     "                           |--Compute Scalar(DEFINE:([Expr1004]=isnull([Expr1001],CONVERT_IMPLICIT(nvarchar(max),'[]',0))))" ,
     "                                |--UDX(([t_user1].[name]))" ,
     "                                     |--Clustered Index Scan(OBJECT:([master].[dbo].[user].[PK__user__3213E83F9704D3EC] AS [t_user1]))"
   ] ,
   "variables" :   {
     "synthetic" :   [ ] ,
     "query" :   { } ,
     "session" :   { }
   }
}
```

## Disabling Explain API​

The Explain API is part of the[ Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/index/)and can
only be disabled by disabling the same.

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/api-reference/explain/#introduction)
- [ Endpoint ](https://hasura.io/docs/latest/api-reference/explain/#endpoint)
- [ API Spec ](https://hasura.io/docs/latest/api-reference/explain/#api-spec)
    - [ Request ](https://hasura.io/docs/latest/api-reference/explain/#request)

- [ Response ](https://hasura.io/docs/latest/api-reference/explain/#response)
- [ Disabling Explain API ](https://hasura.io/docs/latest/api-reference/explain/#disabling-explain-api)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)