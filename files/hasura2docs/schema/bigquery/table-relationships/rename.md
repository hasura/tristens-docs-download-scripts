# BigQuery: Rename Relationships

An existing relationship can be renamed as follows:

- Console
- API


- Head to `Data -> [table-name] -> Relationships` in the Console
- Drop the existing relationship
- Recreate the relationship with the new name


You can rename a relationship by using the[ bigquery_rename_relationship ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#metadata-bq-rename-relationship)metadata
API:

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "bigquery_rename_relationship" ,
   "args" :   {
     "source" :   "<db_name>" ,
     "dataset" :   "bigquery" ,
     "table" :   "articles" ,
     "name" :   "article_details" ,
     "new_name" :   "article_detail"
   }
}
```

Note

You might not be allowed to drop a relationship if it has been referenced elsewhere (e.g. in a permissions rule).

In this case you will have to delete the references first, rename the relationship, and then re-add the references.

### What did you think of this doc?

Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)