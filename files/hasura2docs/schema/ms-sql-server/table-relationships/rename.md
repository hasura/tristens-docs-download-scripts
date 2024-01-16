# MS SQL Server: Rename Relationships

An existing relationship can be renamed as follows:

- Console
- CLI
- API


 **Renaming Local Relationships** 

- Head to `Data -> [table-name] -> Relationships` in the Console
- Click on the `Rename` option for the relationship in question.


Image: [ Fill the relationship details ](https://hasura.io/docs/assets/images/rename-local-rel-step-1-eb3ca73dd275a44464d7a76bbb570b1f.png)

- This will open up a pop-up widget which will allow you to rename and save the relationship


Image: [ Fill the relationship details ](https://hasura.io/docs/assets/images/rename-local-rel-step-2-8d77bcbdc59385be3b3d065349191826.png)

 **Renaming Remote Relationships** 

Remote relationships cannot be renamed. They have to dropped and created again with the new name.

You can rename a relationship by changing the relationship name in the `tables.yaml` file inside the `metadata` directory:

```
-   table :
     schema :  public
     name :  articles
   object_relationships :
     -   name :  author
       using :
         foreign_key_constraint_on :  author_id
-   table :
     schema :  public
     name :  authors
```

Apply the Metadata by running:

`hasura metadata apply`

You can rename a relationship by using the[ mssql_rename_relationship Metadata API ](https://hasura.io/docs/latest/api-reference/metadata-api/relationship/#mssql-rename-relationship):

```
POST   /v1/metadata   HTTP/1.1
Content-Type :   application/json
X-Hasura-Role :   admin
{
   "type" :   "mssql_rename_relationship" ,
   "args" :   {
     "source" :   "<db_name>" ,
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