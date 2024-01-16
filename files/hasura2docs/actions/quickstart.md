# Quickstart Actions

Actions extend your GraphQL schema, allowing it to include traditional REST endpoints. This quickstart will show you how
to implement an Action using the Console of your Hasura project. This Action, using a REST API, will convert a
currency value that we'll query directly from our GraphQL API.

 **All you need to do is to follow the steps listed below, but if you're more curious about what's happening, check out
the  recap at the bottom of the page .** 

##### DOCS E-COMMERCE SAMPLE APP

You can use this quickstart with any project, but it pairs well with our docs e-commerce sample app, which you can deploy to Hasura Cloud with one click below. If you've already deployed the sample app,[ access your existing project. ](https://cloud.hasura.io)

Image: [ Deploy to Hasura Cloud ](https://hasura.io/deploy-button.svg)

## Step 1: Open the Actions page​

From the Console of a Hasura Project, open the `Actions` page and click `Create` :

Image: [ Click create for new Action ](https://hasura.io/docs/assets/images/actions-quickstart_step-1_console_2-17-0-68d6ee232e0eb47684b12da656d55ddd.png)

## Step 2: Describe the Action​

Copy and paste the following string in the `Comment / Description` field at the top of the page:

`Convert currency with real-time exchange rates.`

Image: [ Add a description for your Action ](https://hasura.io/docs/assets/images/actions-quickstart_step-2_console_2-17-0-8325c6bc829ae86c65410c7c6659551f.png)

## Step 3: Define the Action​

Copy and paste the block below into the `Action Definition` field. It will take the place of all placeholder text:

```
type   Query   {
   currencyConverter ( CurrencyInfo :   InputParams ! ) :   ConvertedCurrency
}
```

Image: [ Define your Action ](https://hasura.io/docs/assets/images/actions-quickstart_step-3_console_2-17-0-73b07e73c3b31c0ff73acbb57a72c77e.png)

## Step 4: Configure your types​

Copy and paste the block below into the `Type Configuration` field. It will take the place of all placeholder text:

```
input   InputParams   {
   from :   String
   to :   String
   amt :   Int
}
type   Info   {
   rate :   Float
}
type   Query   {
   amount :   Int
   from :   String
   to :   String
}
type   ConvertedCurrency   {
   date :   String
   info :   Info
   query :   Query
   result :   Float
   success :   Boolean
}
```

Image: [ Click create for new Action ](https://hasura.io/docs/assets/images/actions-quickstart_step-4_console_2-17-0-c73be7711a89b54fe9c42dfb6a196bad.png)

## Step 5: Add the REST endpoint​

In the `Webhook Handler` field, copy and paste the following:

`https://api.exchangerate.host/convert`

Image: [ Click create for new Action ](https://hasura.io/docs/assets/images/actions-quickstart_step-5_console_2-17-0-0e124623f14b7a40c562330bdd738876.png)

## Step 6: Change the request options and add query params​

Click `Add Request Options Transform` and change the `Request Method` to `GET` :

Image: [ Click create for new Action ](https://hasura.io/docs/assets/images/actions-quickstart_step-6_console_2-17-0-1a27e53be3177a91f1e3ef12eab24e43.png)

Add the following query parameters and values as separate pairs in the available fields:

| Query Param | Value |
|---|---|
| from |  `{{$body. input. CurrencyInfo. from}}`  |
| to |  `{{$body. input. CurrencyInfo. to}}`  |
| amount |  `{{$body. input. CurrencyInfo. amt}}`  |


Scroll to the bottom of the page, click `Create Action` , then head to your API page.

## Step 7: Run a query​

Copy and paste the query on the left into your GraphiQL explorer and execute the query by clicking the `Play` button.
The response should look similar to what's on the right (depending on rates):

## Recap​

What just happened? Congrats! You just extended your GraphQL API with a REST endpoint 🎉

Actions can do a lot of things, but chances are - wherever you are in your GraphQL journey - you still have some legacy
REST APIs that you need to integrate with. Whether you built them yourself or you're trying to integrate with public
APIs, Actions are a great way to do that.

We started by[ describing our Action ](https://hasura.io/docs/latest/actions/quickstart/#step-2). This may seem like an excessive step, but - since our GraphQL API is
self-documenting - it's a good idea to add a description to your Action so that your consumers know what it does. The
value we entered is available as a tooltip in the GraphiQL explorer and in the API's documentation.

From there, we[ defined our Action ](https://hasura.io/docs/latest/actions/quickstart/#step-3). This is where we tell Hasura what our Action will do. In this case, we're
defining a `Query` that will return a `ConvertedCurrency` type. This is the type that we'll be returning from our REST
API. We haven't actually defined these types yet; we're just telling Hasura that when running this query, with these
inputs, we'll be returning a `ConvertedCurrency` type.

Next, we[ configured our types ](https://hasura.io/docs/latest/actions/quickstart/#step-4). This is where we tell Hasura what our `ConvertedCurrency` type looks like. We
defined the types of our inputs and output. In the case of our inputs, we're defining an `InputParams` type that will be
used as the input to our Action (i.e., a user will have to pass in an `InputParams` object that contains `from` , `to` ,
and `amt` when executing our Query).

We're also defining the types of our outputs. In this case, we're defining a `ConvertedCurrency` type that will be
returned from our REST API. It can be laborious to define these types, but Hasura can take care of that for you. The
Console's Type Generator is a great way to do that: simply paste in some sample JSON output from your endpoint and
Hasura will generate the types for you.

Image: [ Generate types from a REST API ](https://hasura.io/docs/assets/images/actions-quickstart_type-generator_console_2-17-0-6f54c3cc02952726872ca8f10c452a62.png)

Finally, we[ added the REST endpoint ](https://hasura.io/docs/latest/actions/quickstart/#step-5)and[ configured the request options ](https://hasura.io/docs/latest/actions/quickstart/#step-6). This is where we tell
Hasura where to send our request and what to send. In this case, we're sending a `GET` request to the `https://api.exchangerate.host/convert` endpoint. We're also passing in the `from` , `to` , and `amount` query parameters
that our REST API expects.

Hasura automatically amends the base url of the REST endpoint with these query parameters and their values from the
query to produce a request that looks like this:

`https://api.exchangerate.host/convert?from=EUR&to=USD&amount=1`

To learn about creating your own Actions, check out the[ Create Actions page ](https://hasura.io/docs/latest/actions/create/).

### What did you think of this doc?

- [ Step 1: Open the Actions page ](https://hasura.io/docs/latest/actions/quickstart/#step-1-open-the-actions-page)
- [ Step 2: Describe the Action ](https://hasura.io/docs/latest/actions/quickstart/#step-2)
- [ Step 3: Define the Action ](https://hasura.io/docs/latest/actions/quickstart/#step-3)
- [ Step 4: Configure your types ](https://hasura.io/docs/latest/actions/quickstart/#step-4)
- [ Step 5: Add the REST endpoint ](https://hasura.io/docs/latest/actions/quickstart/#step-5)
- [ Step 6: Change the request options and add query params ](https://hasura.io/docs/latest/actions/quickstart/#step-6)
- [ Step 7: Run a query ](https://hasura.io/docs/latest/actions/quickstart/#step-7-run-a-query)
- [ Recap ](https://hasura.io/docs/latest/actions/quickstart/#recap)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1686154570/hasura-con-2023/has-con-light-date_r2a2ud.png)

Image: [ arrow-icon ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1683723549/main-web/chevron-right_ldbi7d.png)

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)