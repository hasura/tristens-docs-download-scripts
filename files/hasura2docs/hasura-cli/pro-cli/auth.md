# Authentication with the Hasura Pro CLI

All interactions from the CLI to Hasura's APIs are authenticated using a personal access token generated for your user
account.

To set up a token, execute the following command on the CLI:

`hasura pro login`

This command will show a prompt for entering the personal access token.

Head to your[ Hasura Cloud account settings ](https://cloud.hasura.io?skip_onboarding=true)to create a new token. You
can name it something like "cli". Note that the token will be shown only once and as soon as you copy the token, paste
it in your terminal prompt.

Keep this token secure!

This token can be used to authenticate against Hasura Pro APIs and your Hasura Cloud projects. Make sure you keep it
secure. This is a one-time operation. The token will be valid until you delete it.

### What did you think of this doc?

Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)