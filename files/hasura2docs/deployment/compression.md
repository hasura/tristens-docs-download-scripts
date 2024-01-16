# HTTP Compression

The Hasura GraphQL Engine supports HTTP compression. The server looks
for the `Accept-Encoding` header in request. If the header contains `gzip` then the server uses[ Gzip ](https://en.wikipedia.org/wiki/Gzip)compression. Also, the server sets the `Content-Encoding` response
header value to `gzip` .

 **Only responses from "/v2/query" and "/v1/graphql" endpoints are
compressed.** 

### What did you think of this doc?

Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)